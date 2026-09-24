# Voice

Style rules can't make writing sound like a particular person, because voice lives in measurable habits nobody thinks to state: how long sentences run, where rhythm breaks, which words never appear. This file covers building a profile from real samples and holding drafts to it.

Boundary: model the user's own voice at their request. Don't build a profile of another person from their writing in order to pass as them.

## Mode

- `references/voice-profile.md` exists → apply it.
- Missing, or the user asks to recalibrate → calibrate.
- Missing and the user just wants a draft → use the default voice in SKILL.md. Don't start calibration unprompted; offer it in one line if the user is clearly writing as themselves often.

## Calibrate

1. **Collect.** Ask for 5 samples of the user's real writing: 150+ words each where possible, final versions they were happy with, not heavily edited by someone else (including AI), ideally from the contexts they'll write in. If all samples are one genre, say the profile covers that genre and will extrapolate elsewhere. Then ask for explicit rules: sentence length, rhythm, forbidden words and phrases, punctuation bans or loves, tones they want available ("dry, direct, occasionally warm; never peppy").
2. **Measure.** Extract each pattern and its rate. Voice is a set of rates, not a set of features; a move the user makes once per 500 words, used every paragraph, becomes caricature.
   - Sentence mechanics: average length, range, fragments, how often a long sentence is followed by a short one
   - Paragraph shape: typical length, one-line paragraphs
   - Punctuation: dashes, semicolons, parentheses, ellipses, exclamation points, Oxford comma
   - Register: contraction rate, formality, jargon, profanity, favorite intensifiers
   - Signature moves: cold opens, closes, emphasis, humor, hedging
   - Never-list: words generic writing would use that appear in none of the samples, merged with their stated bans
3. **Reconcile.** If a stated rule contradicts the samples ("keep sentences short" but samples average 24 words), ask whether to match how they write or how they want to write. Stated rules win ties the user doesn't resolve.
4. **Save.** Fill in the template below, show it for approval with 2 or 3 short quoted snippets from the samples, then save it as `references/voice-profile.md` and the samples in `references/samples/`. If this skill lives somewhere Claude can't write to, tell the user the profile only lasts for this conversation until they save it into the skill folder.

Failure modes: too few or too-short samples (proceed if they insist, mark fields low-confidence); samples that contradict each other (probably different registers, so profile them as separate contexts rather than averaging); no samples at all (rules-only profile from a short interview, weaker, say so).

## Apply

1. Load the profile at the start of any writing task. Load raw samples only when the profile underdetermines something: a thin genre, a long piece, a tricky tonal call.
2. Draft in the voice from the first word. Structure and rhythm are decided while drafting and can't be patched in afterward.
3. Flex by register within the voice. When writing in a context the profile doesn't cover, extrapolate conservatively and say so.
4. Verify with the voice item in the attack list in SKILL.md.
5. When the user edits your output or says "I'd never say that", add it to Learned corrections so it never needs repeating.

## Precedence

The profile overrides the generic style rules in SKILL.md and `patterns.md`. If the user genuinely writes with em dashes or loves a word the generic list bans, their profile wins. Accuracy still beats everything.

## Profile template

```markdown
# Voice profile: [name]

Calibrated: [date] from [n] samples ([genres]). Confidence: [high/medium/low per section].

## Sentences
- Average length: [n] words; range [min]-[max]
- Fragments: [rate]
- Long-then-short pattern: [rate]

## Paragraphs
- Typical length: [n] sentences
- One-line paragraphs: [rate]

## Punctuation
- Dashes: [never / rate]
- Semicolons: [ ]
- Parentheses: [ ]
- Exclamation points: [ ]
- Oxford comma: [yes/no]

## Register
- Contractions: [rate]
- Formality: [ ]
- Profanity: [ ]
- Jargon comfort: [ ]

## Signature moves
- Opens: [ ]
- Closes: [ ]
- Emphasis: [ ]
- Humor: [ ]
- Hedging: [ ]

## Never-list (add to patterns.md bans)
- [words and constructions]

## Tones available
- [e.g. dry, direct, occasionally warm; never peppy]

## Per-context notes
- Email: [ ]
- LinkedIn: [ ]
- Long-form: [ ]

## Touchstones
> [short quoted snippet]
> [short quoted snippet]

## Learned corrections
- [date]: [what they changed and the rule it implies]
```
