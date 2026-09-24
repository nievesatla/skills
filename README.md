# Skills

My personal library of Claude skills. Each folder is one skill: a `SKILL.md` that tells Claude when to use it and how to do the job, plus optional `references/` files it loads when needed.

## Install

**Claude Code:** copy or symlink the skill folders you want into `~/.claude/skills/` (all projects) or `.claude/skills/` inside a project.

```bash
git clone git@github.com:nievesatla/skills.git
ln -s "$PWD/skills/writing" ~/.claude/skills/writing
```

**Claude apps:** zip a single skill folder and upload it as a custom skill in Claude's settings.

## Skills

| Skill | What it does |
|---|---|
| `writing` | Drafts, edits, tightens, and de-AIs prose in your own voice |
| `social-media` | LinkedIn hooks, viral-post recipes, LinkedIn post analytics, TC Social carousels |
| `deck-outliner` | Clarifying questions, slide outline, then a content sheet to paste into Gamma or another deck builder |
| `client-brief` | One-page prep brief on a prospect before a call |
| `negotiation` | Negotiation playbook for a deal (template, fill in the placeholders) |
| `infographic-builder` | Turns text into a single 1080×1350 infographic |
| `handoff` | Compresses a conversation into a doc a new session can pick up from |
| `ste` | ASD-STE100 Simplified Technical English, only when invoked with `/ste` |
| `devils-advocate` | Attacks a draft or plan with its strongest counterarguments |
| `fact-checker` | Checks every factual claim in a draft against primary sources |
| `go-deeper` | Pushes a shallow take past the obvious answer |
| `decide` | Breaks a stuck decision into options, criteria, and a recommendation |
| `deep-research-synthesizer` | Synthesizes many sources into cited findings |
| `reddit-researcher` | 30-day research sweep across Reddit, X, YouTube, HN, and the web (needs Apify) |
| `grill-me` | Asks 10 to 15 questions and confirms a spec before building |
| `be-a-human` | Pushes back on thin briefs before doing the work |
| `prompt-master` | Turns a brain-dump request into a clean task spec |
| `short-term-memory` | Shapes replies around next actions and numbered steps |
| `how-to` | Coaches a beginner step by step to a finished result |
| `xlsx` | Spreadsheet creation and editing, with financial-model conventions |
| `write-a-skill` | Turns a described behavior into a new `SKILL.md` |
| `skill-audit` | Reviews this library for overlap and weak triggers |

## Contributing

Read [AGENTS.md](AGENTS.md) first. It covers the skill format, how the skills depend on each other, and known issues.

## Credits

`writing` adapts material from [blader/humanizer](https://github.com/blader/humanizer) and [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop), both MIT licensed. Their notices are in [writing/LICENSES.md](writing/LICENSES.md).
