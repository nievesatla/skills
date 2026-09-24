---
name: deck-outliner
description: >-
  Plan a presentation's content before anyone builds slides: ask the clarifying
  questions, agree a slide-by-slide outline, then produce a content sheet
  (exact on-slide text, visual direction, speaker notes, and a paste-ready block)
  that the user hands to Gamma, a Slides or design tool, PowerPoint, or another
  deck builder. Use whenever the user mentions a deck, slides, a presentation,
  a talk, a workshop, a keynote, a webinar, or a pitch deck, e.g. "outline a
  deck on", "I'm giving a talk on", "turn this into a presentation", "what
  should my slides say", "prep content for Gamma". Does not design, style, or
  generate slides itself. Do not use for LinkedIn posts, newsletters, blog
  drafts, one-pagers, or ad copy.
---
# Deck outliner

Most bad decks fail before design: no clear point, slides with three jobs each, and titles that label a topic instead of saying something. This skill fixes the content and stops there. The output is a content sheet a person can paste into Gamma or give to any deck builder, so the building tool only has to handle layout and visuals.

The user controls structure; this skill controls the thinking and the words. Nothing moves to the content sheet until the outline is approved.

If this folder has a `references/` directory with a brand voice guide or example decks, read them first. They override the defaults below.

## Step 1: Clarifying questions

Check what the user already gave you, then ask for what's missing in one numbered batch. Prefer options over open questions. Ask at most 8. If the brief is already tight, say so in one line and go to Step 2.

Required (don't guess these):
1. **Goal.** What should the audience decide, believe, or do when it ends?
2. **Audience.** Who's in the room, what do they already know, and are they skeptical, neutral, or already bought in?
3. **Setting.** Presented live, sent as a read-ahead, or both? This decides how dense the slides get.
4. **Length.** Minutes or slide count.
5. **Source material.** Notes, docs, data, or links to pull from. Name what you'd need but don't have yet.

Ask when relevant:
6. **Must-haves.** Required slides (agenda, team, pricing, Q&A), numbers that must appear, anything off limits.
7. **Tone and look.** Formal or casual; brand colors, fonts, or an image style if they have one.
8. **Destination.** Gamma, a Slides or design tool, PowerPoint, Google Slides, or something else. Default to a generic format if they don't know.

If an answer is vague on something required, ask one follow-up that pins it down, then move on. If the user says "just go", use the defaults at the bottom of this file and list the assumptions you made at the top of the outline.

## Step 2: Outline

Start with the storyline, then the slides.

- **Core message:** one sentence the audience should repeat afterward.
- **Arc:** 3 to 5 beats in plain words (e.g. problem, cost of doing nothing, the fix, proof, the ask).
- **Slides**, each as:

```
Slide 3: Churn doubled after the price change
Job: show the cost of doing nothing. Chart of monthly churn, Jan to Sep.
```

Rules:
- One job per slide. If a slide needs "and" to describe its job, split it.
- Titles state the takeaway, not the topic. "Churn doubled after the price change" beats "Churn analysis". Vary their grammatical shape so they don't read like a template.
- Slide 1 earns attention with a specific claim, number, or question from the material. The last slide gives one clear next step.
- Check the count against time: roughly 1 to 2 minutes per slide when presented live.
- Mark missing content inline as `[NEED: Q3 churn figure]` rather than inventing it.

Show the full outline and wait for explicit approval. The user can cut, merge, reorder, or rewrite anything. Keep slide numbers stable across revisions, and name what changed in one line each time.

## Step 3: Content sheet

After approval, write the full content sheet. Save it as one Markdown file named `<deck-slug>-content.md` and send it to the user. If you can't create files, put the whole sheet in a single fenced code block so it copies cleanly.

### Sheet structure

```markdown
# [Deck title]

## Brief
- Goal: [what the audience should do or decide]
- Audience: [who, what they know, their stance]
- Setting and length: [live / read-ahead], [n] slides, [n] minutes
- Tone: [...]
- Visual direction: [style, colors, fonts, image style, or "builder's choice"]
- Open items: [every [NEED] still unresolved]

## Slides

### Slide 1: [Title]
- Layout: [title | statement | bullets | two-column comparison | chart | image + text | quote | section divider | closing / CTA]
- On slide:
  - [exact text that appears on the slide]
- Visual: [what the image, diagram, or chart shows; for charts: type, the actual data values, and which series or point to highlight]
- Speaker notes: [what the presenter says]
- Source: [where each number or claim came from]

(repeat for every slide)

## Paste-ready
[the destination-specific block described below]
```

### Density

- **Presented live:** sparse slides. At most 5 bullets, each under about 12 words; fragments are fine. The explanation goes in the speaker notes (roughly 60 to 150 words a slide).
- **Read-ahead:** slides carry the argument on their own. Full sentences are fine, still one idea per slide. Speaker notes can be short or empty.

### Paste-ready block

Only on-slide text: no speaker notes, no layout labels, no sources. One section per slide, title as a heading.

- **Gamma:** separate slides with a line containing only `---`. When pasting, choose Gamma's option to split cards on those breaks (card-by-card, not automatic), or it will re-chunk the content to its own card count. Choose the option to keep the text as written if the user wants the exact wording. Put the Brief's tone and visual direction in Gamma's prompt or theme settings rather than the pasted text.
- **Slides or design tools and other builders:** give them the whole sheet. The Brief and the Visual lines are the design instructions.
- **PowerPoint or Google Slides by hand:** the Slides section is the build list; paste the notes into each slide's speaker notes.

End the reply with a short handoff line saying which block to paste where and listing any open `[NEED]` items. Don't generate the deck or pick a design.

## Writing

All text in the outline and the sheet goes through the `writing` skill if it's installed. Slides have a few allowances of their own: fragments are fine on slides, bullets don't need to be sentences, and repeating a key term exactly is better than finding a synonym. Numbers use digits. Never invent a statistic, quote, customer name, or logo; mark it `[NEED]`.

## Check before delivering the sheet

- Every slide has one job, and its title states the takeaway.
- The titles alone, read in order, tell the story.
- Slide 1 opens with something specific; the last slide asks for one thing.
- Slide count fits the time.
- Every number has a source line, or a `[NEED]`.
- The on-slide text in the paste-ready block matches the slide sections word for word.
- Density matches the setting.

## Defaults

Used when the user says "just go" or leaves something unspecified. Edit these to match how you usually present.

- Setting: presented live
- Length: 10 slides, about 15 minutes
- Tone: direct, plain English, no hype
- Destination: generic Markdown (works for Gamma and most builders)
- Visual direction: builder's choice
- Always include: a closing slide with one next step. No agenda slide under 12 slides.

## Out of scope

Designing or styling slides, building .pptx files or Gamma decks, editing an existing Gamma deck, and non-deck content (posts, newsletters, blogs, one-pagers). If the user wants the deck built in the same conversation, deliver the content sheet first, then hand off to whatever deck tool is available.
