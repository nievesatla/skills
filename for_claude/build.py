"""Rebuild for_claude/ from the skills at the repo root, for upload to Claude Desktop.

Run from anywhere: python3 for_claude/build.py

For each root skill (except SKIP) it copies the folder here, rewrites the
frontmatter as plain single-line YAML with only the keys Desktop accepts,
zips it as <skill>.zip with the folder at the zip root, and checks the
Desktop upload rules. Edit the root skills, never the copies here.
"""
import json, os, re, shutil, sys, zipfile

OUT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(OUT)
SKIP = {"xlsx"}  # collides with Anthropic's built-in xlsx skill on Desktop
ALLOWED = ["name", "description", "license", "allowed-tools", "metadata"]
OPTIONAL_REFS = {"references/voice-profile.md"}  # created by the user later


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fields, key = {}, None
    for line in m.group(1).split("\n"):
        km = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            fields[key] = "" if val in (">", ">-", "|", "|-") else val
        elif key:
            fields[key] = (fields[key] + " " + line.strip()).strip()
    for k, v in fields.items():
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            fields[k] = v[1:-1].replace('\\"', '"')
    return fields, text[m.end():]


def render(fields):
    lines = ["---"]
    for k in ALLOWED:
        if fields.get(k):
            v = fields[k]
            lines.append(f"{k}: {json.dumps(v, ensure_ascii=False) if k == 'description' else v}")
    return "\n".join(lines) + "\n---\n"


def check(skill, fields, dst):
    errs = []
    name, desc = fields.get("name", ""), fields.get("description", "")
    if name != skill or not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errs.append(f"name {name!r} must equal folder name and be lowercase-hyphen, max 64")
    if not desc or len(desc) > 1024:
        errs.append(f"description must be 1-1024 chars (is {len(desc)})")
    if "<" in desc or ">" in desc:
        errs.append("description contains < or >")
    dropped = [k for k in fields if k not in ALLOWED]
    if dropped:
        errs.append(f"frontmatter keys Desktop rejects: {dropped}")
    body = open(os.path.join(dst, "SKILL.md")).read()
    for ref in set(re.findall(r"(?:references|scripts|assets)/[\w./-]+\.\w+|LICENSE\.txt", body)):
        if ref not in OPTIONAL_REFS and not os.path.exists(os.path.join(dst, ref)):
            errs.append(f"points to missing file {ref}")
    return errs


for entry in os.listdir(OUT):
    path = os.path.join(OUT, entry)
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif entry.endswith(".zip"):
        os.remove(path)

failed = False
for skill in sorted(os.listdir(ROOT)):
    src = os.path.join(ROOT, skill)
    if skill in SKIP or not os.path.isfile(os.path.join(src, "SKILL.md")):
        continue
    dst = os.path.join(OUT, skill)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store"))
    fields, body = parse_frontmatter(open(os.path.join(dst, "SKILL.md")).read())
    if fields is None:
        print(f"FAIL {skill}: no YAML frontmatter")
        failed = True
        continue
    errs = check(skill, fields, dst)
    open(os.path.join(dst, "SKILL.md"), "w").write(render(fields) + body)
    with zipfile.ZipFile(os.path.join(OUT, f"{skill}.zip"), "w", zipfile.ZIP_DEFLATED) as zf:
        for dirpath, _, files in os.walk(dst):
            for f in sorted(files):
                full = os.path.join(dirpath, f)
                zf.write(full, os.path.relpath(full, OUT))
    print(f"{'FAIL' if errs else 'ok  '} {skill}" + "".join(f"\n       - {e}" for e in errs))
    failed |= bool(errs)

sys.exit(1 if failed else 0)
