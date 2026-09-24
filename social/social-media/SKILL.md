---
name: social-media
description: >-
  Social media content work: LinkedIn hooks (the 2 lines before "...see more"),
  reproducing a viral post's recipe for a new topic, analyzing an Apify LinkedIn
  posts export into a report and SOP, and TC Social Instagram carousels. Use
  when the user asks for a hook or post opening, shares a carousel or newsletter
  visual and wants a hook, says "this post went viral, capture why" or "recreate
  this post", uploads a LinkedIn posts scrape or asks "what's working on my
  LinkedIn", or asks for a TC Social carousel, IG slides, or a swipe post. Not
  for general prose editing (use the writing skill) or standalone infographics
  (use infographic-builder).
---
# Social media

Four workflows that share one skill. Pick the one that matches the request, then read only that reference file.

| Request | Read |
|---|---|
| Hook, opening lines, "first line", "what should the first lines be" for a LinkedIn post | `references/linkedin-hooks.md` |
| "This post went viral", "what's the recipe", "recreate this post for another topic" | `references/viral-recipe.md` |
| Apify LinkedIn posts CSV/XLSX, "analyze my LinkedIn posts", "what's working" | `references/post-report.md` |
| TC Social carousel, Instagram carousel, IG slides, swipe post | `references/tc-social-carousel.md` |

If a request spans two (a full post: hook plus body), run them in order: hook first, then the body.

## How this relates to the writing skill

Body copy, captions, and anything written in full sentences go through the `writing` skill's rules and red-pen loop. Two platform conventions override it, and only where stated:

- **Hook lines.** The two hook lines may use the patterns in the hook library: a trailing colon on line 2, "Here's...", parenthetical intensifiers like "(exact)", and "How to... in 30 min:". These are the proven format. Everything after the fold follows the writing skill.
- **TC Social voice.** Lowercase-first sentences, no exclamation marks, no emoji. Those brand rules win over any default.

Banned everywhere, hooks included: "It's not X, it's Y" and every other reframe in the writing skill's `patterns.md` A1. Never invent a number; hooks and captions use real figures from the source material.

## Moving this skill

This folder is self-contained. To install it elsewhere, copy `social-media/` as a whole. It has no dependency on the rest of the repo except the soft reference to the `writing` skill above; if that skill isn't installed where this one goes, the voice rules in each reference file still apply on their own.
