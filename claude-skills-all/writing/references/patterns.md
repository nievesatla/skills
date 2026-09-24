# AI writing patterns

The catalog behind the `writing` skill. Patterns are grouped by the default choice they come from and ordered strongest first within each group. Sections A and E justify an edit on one sighting. Anything marked *weak alone* needs company from other tells in the same passage before you act on it.

Why these exist: a language model picks the choice that fits the widest range of readers. A human writer chooses for one reader and one subject, so their choices are uneven and specific. Word habits change with each model release; the structural habits persist, which is why structure leads this list.

## A. Staging instead of stating

### A1. Negative parallelism (reframes)

The hardest ban. A sentence, pair of sentences, heading, or caption fails if it dismisses or minimizes X, then upgrades to Y. The word "not" doesn't have to appear.

Shapes:
- This isn't X. This is Y. / It's not X, it's Y.
- Not X. Y. / No X. Just Y. / Not a X. Not a Y. A Z.
- Not only X, but also Y. / It's not just about X, it's about Y. / X rather than Y.
- Forget X. Focus on Y. / Stop thinking X. Start thinking Y.
- Less X, more Y. / X is dead. Y is the future.
- The question isn't X, it's Y. / You don't need X. You need Y.
- It was never about X. It was always about Y.
- X? No. Y.
- A clipped negative tail: "..., no guessing."

Softer versions with the same pivot: "While X may seem...", "Sure, X...", "At first glance...", "On the surface...", "Most people think...", "Conventional wisdom says...". Pivot words to watch when they perform a reframe: but, yet, actually, really, instead, rather, ultimately, in reality, the truth is, what matters is, the real, the deeper, the hidden, the overlooked.

It crosses sentence boundaries:
- "Most teams think they have a hiring problem. They have a standards problem." → "The team's standards are unclear."
- "People blame the algorithm. The input data is broken." → "The input data is broken."
- "This does not mean every choice is equal. It means there is no external system that confirms which choice is right." → "No external system confirms which choice is right, although the choices still have different consequences."
- "Is this a productivity problem? No. It's an attention problem." → "Attention is the constraint."

Headings too: "Not a tool. A system.", "From chaos to clarity", "The real problem" → "The system", "Input problems".

Fix: delete the rejected half, then write the positive claim as a direct sentence. "It's not about the prompt. It's about the context." → "Context controls the output."

Allowed: contrast that corrects a specific belief the reader actually holds, or a factual, legal, technical, date, number, name, or scope error. "The meeting is on Tuesday, not Thursday." Also fine when both halves carry information.

### A2. One-line closers, kickers, and dramatic fragments

Watch for: a one-sentence paragraph that restates the paragraph before it; "That is the real win."; "Read that again."; "Let that sink in."; the same closer after several sections; a row of fragments ("No aesthetic prior. No nostalgia."); "X. And Y. And Z."; "That's it. That's the whole thing."; a word in ALL CAPS or with periods between words (every. single. day.); a final "deep" line that turns the point into a metaphor or aphorism.

Fix: cut a closer that repeats. Merge fragments into a sentence with a specific claim. For a fake-profound kicker, delete it outright (don't rewrite it into a better metaphor) and end on the clearest concrete sentence already there. If the ending needs closure, add a plain takeaway or next action.

> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.

> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### A3. Summary-recap endings and announce-then-repeat structure

"In conclusion", "Ultimately", "Overall", or a last paragraph that restates the piece. Also an intro that announces what the piece will say. Cut both: start inside the point, end on the last concrete point, takeaway, or next action.

### A4. Sayings that sound deep

Watch for: the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter, X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of.

> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.

> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

### A5. Staged run-ups and faux-insight setups

Run-ups: Let's dive in, let's explore, let's unpack, let's break this down, here's what you need to know, without further ado, heads up, quick note, Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, Let me be clear, I'll be honest, The uncomfortable truth is.

Faux insight (flatters the writer as the lone expert): This is the part most people skip, What most people get wrong, Here's what nobody tells you, The part everyone misses, Nobody is talking about, Most people don't realize.

Fix: remove the run-up, not just its tone. "Honestly" inside a casual sentence is ordinary; the tell is the standalone opener before a routine claim.

> Is it worth the price? Honestly? It depends on how often you'll use it.

> Whether it's worth the price depends on how often you'll use it.

### A6. Colon reveals

A noun phrase, a colon, then a dramatic reveal: "The detail that makes it work: a separate agent grades it." "The best part: it learns." Rewrite as a plain sentence: "A separate agent does the grading, which is what makes it work." Use colons for lists, labels, and quotes. Prefer sentence case after a colon.

### A7. Rhetorical setups

"What if I told you...", "Think about it:", "Plot twist:", self-answered "Question? Answer." pairs. Drop the setup and make the point.

### A8. Arguing with no one

Watch for: This isn't (mainly) about, I'm not saying, To be clear, Don't get me wrong, This is not to say, Some might say... but, A tempting approach would be, One might be tempted to, You might think... but.

The text answers an objection or rejects an option that appears nowhere else. Remove the defense; if it holds a real claim, state the claim. Keep an objection the text attributes or answers in full, and an option a reader would actually weigh.

> Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.

> Session tokens are rotated every 24 hours, in place, and clients refresh transparently.

### A9. Interpretive metadiscourse

Lines that step outside the subject to tell the reader what to notice or how to weigh it: "That last part matters more than it sounds", "The key point is", "As you can see", "This distinction matters", a redundant "In other words", "In this section", "This article will cover", "Let me walk you through". Delete the aside if the point is clear; otherwise replace it with support.

## B. Rhythm by rule

### B1. Forced triads

Ideas arrive in threes to sound complete: "faster, smarter, and more reliable", three parallel examples, three short facts then a lesson. One triple per piece at most. Prefer pairs, a single adjective, or four items if four is true. Keep three when the meaning has three parts.

> A career can look promising and fail. A relationship can feel important and end. A skill can take years and remain useless. These decisions rarely explain themselves.

> A career can look promising and fail. So can a relationship that felt important and ended, or a skill that took years and remained useless. These decisions rarely explain themselves.

### B2. Metronome rhythm and repeated shapes

Perfectly parallel sentences, paragraphs of identical length, the same sentence opening several times in a row ("She noted the door. She noted the lock. She filed both away."), "Whether you're a beginner or a seasoned pro...", a tidy summary sentence at the end of every section. Humans write lopsided. Merge, change the subject, or lead with the action. Deliberate repetition for rhythm ("She came. She saw. She conquered.") is fine.

### B3. Dashes

Final text contains no em dashes (—) or en dashes (–), and no spaced hyphens or double hyphens used as dashes, unless the user's voice uses them; then match their rate. Replace with:
- Two sentences: "The launch failed. Nobody had tested payments."
- A comma: "It works, mostly."
- Parentheses for a true aside: "The budget (all $40 of it) ran out."
- A colon when introducing: "One thing mattered: speed."

Don't mechanically swap a dash for " - ". If the sentence needed a dash, it usually needs restructuring. Leave dashes in code, commands, paths, and URLs.

### B4. Stacked qualifiers *(weak alone)*

"could potentially", "might arguably", "it's also possible", "in some cases it may". Keep a qualifier only when the meaning needs it. Keep scope statements, legal and safety notices, and real uncertainty. "I think", "maybe", "to be honest" stay when they're the writer's real doubt or spoken rhythm.

> It could potentially possibly be argued that the policy might have some effect on outcomes. → The policy may affect outcomes.

### B5. Passive voice and missing subjects *(weak alone)*

"No configuration file needed. The results are preserved automatically." → "You don't need a configuration file. The system saves the results automatically." Also: don't let inanimate things do human verbs ("the decision emerged").

### B6. Hyphenated pairs everywhere *(weak alone)*

Keep the hyphen before a noun ("a high-quality report"), drop it after ("the report is high quality").

## C. Inflation and borrowed authority

The fact underneath is usually sound. Keep it, remove the dressing.

### C1. Stock vocabulary

Cut unless quoting or discussing the word, or unless it carries literal meaning in context:

actually (as a pivot), additionally, align, accelerate, accentuate, adaptive, beacon, best-in-class, boast(s), bolstered, breakthrough, bustling, captivate, commendable, comprehensive, crucial, cutting-edge, data-driven, deep dive, delve, democratize, disruptive, dive into, dynamic, effortless, elevate, embark, emphasize, empower, enduring, enhance, ever-evolving, facilitate, foster, frictionless, future-proof, game-changer, garner, groundbreaking, harness, hidden gem, highlight (verb), holistic, immersive, innovative, insightful, integrated, interplay, intricate, intricacies, intuitive, journey (metaphorical), key (adjective), landscape (metaphorical), leading-edge, leverage (verb), look no further, meticulous(ly), mission-critical, multifaceted, must-visit, navigate (metaphorical), nestled, optimize, paradigm (shift), paramount, pioneering, pivotal, plug-and-play, predictive, proactive, quietly, realm, redefine, reimagine, rest assured, revolutionize, rich history, robust, scalable, seamless, showcase, state-of-the-art, streamline, supercharge, surpass, synergy, synergize, tapestry, testament, trailblazing, transformative, transparent, turnkey, underscore, unleash, unlock, unparalleled, unprecedented, utilize, valuable, versatile, vibrant, visionary. Also the phrases "this is huge" and "this changes everything".

Add the user's own banned words from their voice profile.

Replacements are boring on purpose: use, big, helps, also, shows, has.

Often-empty adverbs: just, literally, honestly, simply, truly, fundamentally, importantly, crucially, inherently, inevitably, very, really, extremely, incredibly. Cut when they add nothing; keep when they carry emphasis, uncertainty, contrast, or the writer's rhythm.

> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape.

> Somali cuisine also includes camel meat. Pasta, introduced during Italian colonization, is still common, especially in the south.

### C2. Inflated significance

Watch for: stands as a testament, a pivotal or crucial moment, plays a key/vital role, marks a shift, shaping the, underscores its importance, reflects a broader, enduring legacy, setting the stage for, evolving landscape, indelible mark, solidifies its position; "Despite these challenges... continues to thrive"; stock "Challenges and Legacy" or "Future Outlook" sections; send-offs like "the future looks bright", "exciting times ahead". Also false ranges ("from ancient traditions to modern innovation") with no meaningful middle.

State the fact and let the reader judge its weight. End on the last concrete fact.

> The launch marks a pivotal moment for the company. → The launch is the company's first paid product.

### C3. Shallow -ing riders

highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, cultivating, fostering, encompassing, showcasing, paving the way for, opening the door to. An -ing phrase bolted onto a fact to make it sound analyzed.

> The launch adds file search, highlighting the team's commitment to better workflows.

> The launch adds file search, so users can find old drafts without leaving the editor.

### C4. Sales language

boasts, vibrant, rich (figurative), profound, exemplifies, commitment to, natural beauty, nestled, in the heart of, renowned, featuring, diverse array, breathtaking, stunning, must-visit.

> Nestled within the breathtaking region of Gonder, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage. → Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### C5. Avoiding is, are, and has

serves as, stands as, functions as, marks, represents a, boasts a, features a, offers a, plays a role in, helps to, aims to, seeks to. Use is, are, has, uses, gives, shows.

> Gallery 825 serves as LAAA's exhibition space. The gallery features four spaces and boasts over 3,000 square feet. → Gallery 825 is LAAA's exhibition space. It has four rooms totaling 3,000 square feet.

Related: weak verb phrases. "Made a decision" → "decided". "Has the ability to" → "can". "Perform compression of" → "compress".

### C6. Borrowed authority and weasel attribution

experts argue, studies show, industry reports suggest, many argue, widely regarded as, observers have cited; lists of prestige outlets; follower counts. Name the source and what it said, or cut the claim. If the user has no source, ask or mark `[VERIFY]`. Never invent a source.

### C7. Vague association

associated with, in connection with, linked to, tied to. Name the actual relationship if the source gives it ("founded and conducts"). If it doesn't, keep the vague wording rather than inventing a role.

### C8. Synonym cycling (elegant variation)

"Sarah" → "the seasoned operator" → "the executive". "The agent reviews... The assistant scores... The tool suggests..." If the clear word is right, repeat it.

### C9. Analogies and metaphors

Default: no analogies. Use one only if all of these pass: the subject is unfamiliar or technical; the analogy makes it easier; it's shorter than the literal version; it's exact enough not to mislead; it reads normally aloud. Frequency: zero under 800 words, at most one for 800 to 1,500 words, at most one per 1,500 words after that. Never stack them.

Banned setups: Think of it as, Imagine, Picture, It's like, As if, Works like, Acts like, A bridge between, A lens for, A roadmap for, The engine of, The backbone of, The DNA of.

Banned families for abstract work: journey, battlefield, ecosystem, engine/fuel, map/compass, signal/noise (unless literal), iceberg, north star, flywheel, scaffolding, plumbing, gardening, chess, sports, puzzle.

Banned metaphor verbs for ideas and products: sanded down, bolted on, stripped back, stitched together, woven, layered, carved out, baked in, distilled, unpacked, crystallized, sharpened, surfaced, amplified, anchored, cemented, bridged. Use literal verbs: cut, added, removed, changed, joined, showed, explained, reduced, fixed, chose.

> Your onboarding is a leaky bucket. → 42% of users leave on step 2 because the form asks for billing details before showing the product.

### C10. The portability test

If a sentence could move unchanged to another person, company, or product, it's filler. Cut it or replace it with a fact, mechanism, consequence, or judgment specific to this subject.

## D. Formatting by rule

### D1. Bold and labeled lists

Bold sprinkled mid-sentence; vertical lists where every item gets a bold label and a colon. Remove the bold. Turn a labeled list into prose when the labels add nothing. Bold at most 1 or 2 moments per section.

> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.

> The update improves the interface and speeds up load times.

### D2. Structure where prose belongs

Bullets for thinking rather than genuine lists; headers over a 400-word piece or a two-sentence section; the bold-term-colon skeleton for an essay.

### D3. Decorative headings

Title Case Headings, emoji or arrows in headings and list items, a horizontal rule between every section, a top heading that repeats the title, a heading followed by a one-line paragraph that restates it. Use sentence case and remove the decoration.

### D4. Curly quotes *(weak alone)*

Curly quotes where the target format uses straight ones.

### D5. Numbers

Use digits for numbers (3 years, 500 users).

## E. Leftovers from the chat and the draft

Remove outright.

### E1. Chat residue

Great question, Certainly, Of course, Happy to help, You're absolutely right, I hope this helps, Would you like me to..., Want me to...?, Should I continue?, Let me know if..., Here is a... Remove the wrapper, keep the content.

### E2. Email boilerplate

I hope this email finds you well, please don't hesitate, feel free to, I wanted to reach out to touch base regarding, I wanted to provide a quick update, after careful consideration.

### E3. Engagement bait

Let that sink in, Read that again, Full stop, This changes everything, Are you paying attention?, You're not ready for this.

### E4. Dead openings and transitions

Openings: In today's (fast-paced) world, In an era of, In the age of, It is important to note, It's worth noting, Notably, In order to, At the end of the day, Moving forward, Going forward, It goes without saying, When it comes to, In terms of, With regard to, In this article I will, Despite its strengths X faces challenges.

Transitions: Furthermore, Additionally, Moreover, Thus, Hence, Overall (sentence-initial), In conclusion, Ultimately, That said, That being said, With that in mind, On top of that. Use a real transition or none.

### E5. Knowledge-limit disclaimers and guesses

As of my last update, based on available information, not widely documented, maintains a low profile, likely grew up, it is believed that. State what the source doesn't show, or cut the sentence. Never present a guess as a fact.

### E6. Writing about the previous version

Docs and comments that describe what the text replaced instead of current behavior. Mention the old version only in change logs, release notes, and migration guides.

## When not to act

- A *weak alone* tell with no other tells nearby.
- A watched phrase inside a quotation, title, proper name, or a passage discussing the phrase.
- Salutations and sign-offs on a letter.
- Text written before November 30, 2022.
- Anything that carries the writer's voice: an unusual specific detail, mixed feelings, era-bound slang or in-jokes, a first-person choice they can explain, a real aside or self-correction.

People who judge by feel do little better than chance. Several tells together are the evidence.

## Sources

Merged from the user's local humanizer, red-pen, tighten, and personal-voice skills; [blader/humanizer](https://github.com/blader/humanizer) v3 (itself based on Wikipedia's "Signs of AI writing"); and [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop). License notices are in `../LICENSES.md`.
