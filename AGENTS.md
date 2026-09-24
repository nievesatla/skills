# AGENTS.md

A personal library of Claude skills. Each skill is a folder with a `SKILL.md` that tells Claude when to use it and how to do the job. This file explains the layout, what each skill is for, and the conventions to follow when changing anything here.

## Layout

```
skills/
├── AGENTS.md          this file
└── <skill>/           one top-level folder per skill, nothing else
    ├── SKILL.md       required: YAML frontmatter + instructions
    ├── references/    optional: detail loaded only when SKILL.md points to it
    ├── scripts/       optional: code the skill runs
    └── assets/        optional: images, templates
```

Every folder at the root is a skill, and each one is self-contained, so any skill can be copied or moved to another repo on its own.

## Skill format

Every `SKILL.md` starts with frontmatter:

```yaml
---
name: skill-name          # must match the folder name
description: >-           # the only thing Claude sees before deciding to load the skill
  What it does, the exact phrases and situations that should trigger it,
  and when NOT to use it.
---
```

The `description` does the triggering, so it names concrete user phrases and situations, not categories like "helps with writing". Keep the body focused on procedure and standards Claude wouldn't apply by default. Move long catalogs, templates, and examples into `references/` and have `SKILL.md` say when to read each file. Use `write-a-skill` to draft new skills and `skill-audit` to check the library for overlap.

## Skills

### Writing and communication

| Skill | Job |
|---|---|
| `writing` | The one skill for prose quality: drafting, humanizing, tightening, self-critique loop, AI-pattern audits, and the user's voice profile. Merged from humanizer, red-pen, tighten, personal-voice, and the two upstream repos below |
| `social-media` | LinkedIn hooks, viral-post recipes, Apify LinkedIn post analytics, and TC Social Instagram carousels, one reference file per workflow. Merged from linkedin-hook, viral-recipe, linkedin-post-report, and tc-social-carousel. Built to be moved to another repo later |
| `ste` | Rewrite in ASD-STE100 Simplified Technical English. Explicit invocation only (`/ste`), on purpose |
| `client-brief` | One-page brief on a prospect before a call; runs `writing` on its prose |
| `negotiation` | Multi-expert negotiation playbook for a deal; still a template with placeholders to fill |
| `deck-outliner` | Ask clarifying questions, agree a slide outline, then produce a content sheet (on-slide text, visuals, speaker notes, paste-ready block) to hand to Gamma or another deck builder |
| `infographic-builder` | Turn text into a single 1080×1350 infographic PNG |
| `handoff` | Compress a conversation into a handoff doc for a new session or colleague |

### Thinking and critique

| Skill | Job |
|---|---|
| `devils-advocate` | Attack a draft or plan with its strongest realistic counterarguments |
| `fact-checker` | Verify every factual claim in a draft against primary sources |
| `go-deeper` | Push a shallow take three "why" layers down |
| `decide` | Turn a stuck decision into options, criteria, and a recommendation |
| `deep-research-synthesizer` | Synthesize many sources into cited, actionable findings |
| `reddit-researcher` | 30-day research sweep across Reddit, X, YouTube, LinkedIn, HN, and the web via Apify actors |

### Working style and intake

| Skill | Job |
|---|---|
| `grill-me` | Ask 10 to 15 questions and confirm a spec before building anything non-trivial |
| `be-a-human` | Push back on thin briefs, ask 5 to 8 hard questions, then deliver with a position |
| `prompt-master` | Restructure a brain-dump request into a clean task spec before executing |
| `short-term-memory` | Shape every reply for a reader with limited short-term memory: next action first, numbered steps, time estimates |
| `how-to` | Coach a beginner step by step to a finished result with Claude |

### Tools and meta

| Skill | Job |
|---|---|
| `xlsx` | Create, edit, and analyze spreadsheet files |
| `write-a-skill` | Turn a described behavior into a properly structured `SKILL.md` |
| `skill-audit` | Review the library for overlap, dead weight, vague triggers, and gaps |

## How the pieces fit

- `writing` owns prose quality everywhere. Other skills that produce sentences (client-brief, negotiation, deck-outliner, social-media) point to it instead of carrying their own banned-word lists.
- Precedence inside `writing`: accuracy, then clarity, then specificity, then the user's voice profile, then the generic anti-AI rules. The voice profile lives at `writing/references/voice-profile.md` once calibrated (it doesn't exist yet).
- `social-media` lets hook lines keep their platform conventions (trailing colons, "Here's...") and lets TC Social's lowercase-first brand voice win. The reframe ban ("It's not X, it's Y") applies everywhere.
- `ste` deliberately stays separate: it requires no contractions and fixed sentence limits, which conflict with `writing`'s defaults, and it only fires when named.
- Intake overlaps: `grill-me`, `be-a-human`, and `prompt-master` all gate work behind questions or restructuring. They can fire on the same request. Worth sharpening their descriptions or merging if that becomes a problem.

## Known issues

- `be-a-human`: frontmatter is broken. It has only `name`, and the real description sits below it in escaped Markdown (`\---`, `\#\#`), probably from a rich-text paste. It won't trigger reliably until the file is cleaned up.
- `ste`: references `references/word-substitutions.md` and `references/examples.md`, which don't exist.
- `xlsx`: references `scripts/recalc.py`, `scripts/office/soffice.py`, and `LICENSE.txt`, none of which are here.
- `deep-research-synthesizer`, `infographic-builder`: reference a `LICENSE.txt` that isn't here.
- `negotiation` and `client-brief`: still contain `[ PLACEHOLDER ]` fields to fill in.
- `xlsx`: an older copy of Anthropic's built-in xlsx skill, with extra financial-modeling rules the current built-in dropped. It triggers on the same requests as the built-in version.
- `social-media/references/viral-recipe.md`: the `[REFERENCE POST]` block at the bottom is empty until a real post is pasted in.
- `short-term-memory` is written to apply to every reply on every topic. If this library is shared with anyone else, that skill should stay personal.

## Working in this repo

- Edit skills in place and commit each logical change separately so any skill can be restored from history. The first commit is the untouched import of the original library.
- When merging skills, delete the originals in the same commit and update every other skill that referenced them (search for the old names).
- Keep `name` equal to the folder name.
- Don't paste text from rich-text editors without checking for escaped Markdown.
- New skills go in a new top-level folder. Don't add grouping folders; they break the one-folder-per-skill layout that Claude's skill loaders expect.

## Upstream sources

- https://github.com/blader/humanizer (MIT)
- https://github.com/petergyang/no-ai-slop (MIT)

Both are folded into `writing`. When pulling in more content from them, keep their license notices (see `writing/LICENSES.md`).
