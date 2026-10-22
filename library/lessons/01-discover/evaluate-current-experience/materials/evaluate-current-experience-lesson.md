---
title: "Evaluate Current Experience"
subtitle: "Judge what exists against clear principles, with evidence you can show"
type: lesson
program: private-training
tags: [evaluation, heuristic-evaluation, cognitive-walkthrough, severity-rating, wcag, usability, current-state, ai-workflow]
level: junior, mid
duration: "90 min"
date: 2026-10-01
programs: [ui-ux-fundamentals:02]
draft: true
slides: ""
previous-session: "Design Thinking for UX Designer"
next-session: "Customer Understanding"
---

## Overview

Most junior designers have never been shown how to judge a design properly. They ship a flow, or inherit one, and the only tool they have is taste: "this feels off", "I'd change the colour". Taste is a fine starting point and a weak argument. It can't be checked, it can't be ranked, and nobody else on the team can act on it.

This session gives a junior designer the foundation to evaluate an experience that already exists, whether they designed it themselves without guidance or inherited it from someone else. The session runs theory first, then practice. The theory covers choosing a method for the stage the project is in, Nielsen's 10 usability heuristics, what a strong finding looks like, severity rating, and a short talk on where AI fits. Practice follows, on the mentee's own flow: evaluate it by hand (20 minutes), rate the findings (5 minutes), and only then use AI for 12 minutes to cross-check, review, build their own `evaluation.md` file, and preview the `evaluation.html` page they will generate as homework. An accessibility check against WCAG 2.1 AA is a take-home pass, not taught live.

The order is deliberate. A mentee who learns the principles first can tell when AI is wrong. A mentee who starts with AI learns to accept whatever it says.

> **Sync note (2026-10-22):** the structure below was reverse-synced from the Vietnamese deck `slides/Evaluate Current Experience (VI).dc.html`, the version used in a session on 2026-10-13. Content that the deck no longer teaches (place-your-project, match-the-symptom, the guided checkout practice, calibration on the Appendix D issues) is kept under Reserve Activities. Theory block timings are estimates `[to confirm]`. The three practice blocks (20, 5 and 12 minutes) come from the deck. The pre-sync versions are in `_archive/`.

This lesson sits between Design Thinking and Customer Understanding. It builds on the screen flow the mentee captured in Design Thinking, and it hands off a ranked list of what is wrong and where. Customer Understanding then picks up the question an evaluation can't answer: why. Mid-level mentees must take this session before Desk Research; seniors can skip it by passing the senior fast-track below. Desk Research then uses the mentee's `evaluation.md` as one of its evidence sources.

---

## Learning Objectives

By the end of this session, students will be able to:

1. **Choose** the right evaluation method for the stage their project is in
2. **Apply** usability heuristics to a live product, with evidence for every issue
3. **Rate** issues by severity so the biggest problems rise to the top
4. **Use** AI to brainstorm, structure, and visualise their findings, while keeping every judgment their own

---

## Success Check

- A heuristic evaluation of your current product is complete
- Issues are ranked by severity, and each one has a screenshot or example

**In-session checkpoint:** one flow of your own product evaluated, with about 5 findings (3 to 5 is enough), each rated 0 to 4 and each with a screenshot. The full Success Check above is met when the assignment is submitted.

---

## Plain-Language Glossary

Say each of these once, in plain words, before using it. Keep this list on screen or in the handout.

| Term | Plain meaning |
|---|---|
| Evaluation | Judging something that already exists against a standard, to find where users will struggle. It is not a redesign. |
| Heuristic | A rule of thumb. A principle that holds across most products, not a rule for one screen. |
| Finding | One issue, written with what you saw, where, which principle it breaks, and proof. |
| Severity | How bad an issue is, so the worst gets fixed first. |
| Evidence | A screenshot or example anyone can look at and see the same thing you saw. |
| Walkthrough | Stepping through one task as a first-time user would, asking four questions at every step. |

---

## Materials Needed

- A live food-delivery app on the mentor's phone or screen, used only for the opening. Live apps change without warning, so keep one screenshot of its checkout as a backup.
- The seeded checkout set (Appendix F): 5 screens of a neutral mock food-delivery checkout with planted issues and an answer key, built as `assets/seeded-checkout/01-cart.png` to `05-payment-failed.png` (source: `checkout-set.html`). Reserve material: used only in the reserve guided-practice activity, not in the current session plan.
- `library/frameworks/framework-nielsen-usability-heuristics.md`: teach the 10 heuristics from this file. The lesson below groups and simplifies it for juniors, it doesn't replace it.
- `library/frameworks/framework-severity-rating-scale.md`: teach the 0 to 4 scale and its factors from this file.
- The ten heuristic principle slides (Heuristic 01 to 10), already inside the built deck `slides/Evaluate Current Experience.dc.html`. They come from the former Audit & Desk Research deck
- The Heuristics Cheat Sheet (Appendix A): one page, handed out before Part 2. Print from `assets/heuristics-cheat-sheet.html`
- The Evaluation Worksheet (Appendix B): the manual template the mentee fills in during Practice A and B. Print from `assets/evaluation-worksheet.html`
- `assets/heuristics.md`: the principles as a markdown file for the AI (rules, output format, two worked examples). The mentee attaches it in Practice C (the cross-check step) and keeps it in the AI foundation folder. The slide calls this file `principles.md` `[to confirm: pick one name]`
- Reserve material: the three pre-written calibration issues (Appendix D) and the six symptom cards (Appendix E). They serve the Senior Fast-Track and the reserve activities, not the current session plan
- For the AI block: an AI chat tool for the brainstorm and `evaluation.md` steps, and an AI tool that can create files (an AI coding tool, or a chat tool with file creation) for the `evaluation.html` homework step. The AI foundation folder from earlier sessions is the working folder.

---

## Pre-Class Preparation

Ask the mentee to do the following before the session:

1. **Pick one key flow in your own product** (a flow you designed, or one you inherited). Choose a flow with 4 to 8 steps, such as sign-up, search to result, or checkout. Not the whole product. If you captured a screen flow in Design Thinking, use that one, so the same flow carries into Customer Understanding.
2. **Capture it as screenshots**, one per step, in order. Name them `01-...png`, `02-...png`. Resize to about 1200 px wide so the later HTML file stays small.
3. **Check confidentiality.** If the product is internal or customer-facing at work, blur or replace any real customer data and check your company's rules on what can go into an AI tool. If in doubt, evaluate a personal or portfolio project instead.
4. **Confirm the AI foundation folder and an AI tool are set up** from earlier sessions. This lesson assumes they are.

---

## Session Plan

| Act | Block | Topic | Duration |
|---|---|---|---|
| 1 · Frame | Opening (theory) | Spot one problem, opinion isn't a finding, the four-part finding | 4 min |
| 2 · Method | Teaching | Choose a method by project stage | 4 min |
| 3 · Principles | Teaching | What heuristic evaluation is, Nielsen's 10: overview page, one slide per principle | 14 min |
| 4 · Apply | Teaching | What a finding looks like: weak vs strong, three tests | 4 min |
| 5 · Severity | Teaching | What severity is, the scale, three questions, the 2x2, severity as a next move | 9 min |
| 6 · AI | Teaching (talk) | AI assists, you decide; the five-step workflow; three levels of AI evaluation | 7 min |
| 7 · Practice A | Activity (manual) | Evaluate your own flow, no AI | 20 min |
| 8 · Practice B | Activity (manual) | Rate your own findings, no AI | 5 min |
| 9 · Practice C | Build with AI | Cross-check, review, build `evaluation.md`, visualise `evaluation.html` | 12 min |
| 10 · Close | Wrap | Checkpoint, homework, bridge to Customer Understanding | 4 min |

**Scripted total: 83 min (theory 42, practice 37, close 4), with a 7-minute buffer inside the 90-minute slot.** The practice times (20, 5, 12) come from the deck. The theory times are estimates `[to confirm]`. Nothing before Practice C asks the mentee to use AI: AI appears as a 7-minute talk in act 6, and hands-on only after the mentee has evaluated and rated their own flow by hand. Expect act 3 and Practice A to run long; the buffer is for them.

**If time runs short, cut in this order:**

1. Skip the optional knowledge check after Part 4
2. In Part 4, the mentor plots the 2x2 instead of the mentee
3. In Part 4, "From severity to a next move" shrinks to one spoken sentence per level, with no worked case
4. The `evaluation.html` step (Visualise) in Practice C moves entirely to homework
5. The three-levels talk in Part 5 becomes a handout the mentee reads at home

Do not cut Practice A. It is the point of the session.

> **Story logic:** The session moves from *why* (an opinion isn't a finding) to *how to choose* (method by stage) to *what to judge against* (principles) to *what a good finding looks like* (evidence) to *how to rank* (severity) to *where AI fits* (a short talk), and only then to *doing it yourself* (manual, on the mentee's own flow), and last *doing it faster and sharing it* (AI). By the end, the mentee has a ranked, evidenced evaluation of their own product, and an `evaluation.md` they can reuse on every future project.

---

## Senior Fast-Track (skip check)

Seniors may skip this session if they can already do what it teaches. Run this check before booking the session. It is not part of the 90-minute plan or the slide deck, and takes about 15 minutes.

1. **Rate (8 min):** Give the mentee the three calibration issues from Appendix D (C1 to C3) without the suggested ratings. They rate each 0 to 4 and give a one-line reason.
2. **Write (7 min):** They pick a flow in their own product and write one finding in the four-part format (what I saw, where, which principle, proof), with a screenshot.

**Pass:** all three ratings are within one point of the mentor's suggested rating, the reasoning names frequency and impact, and the finding has all four parts with real proof. A pass means the mentee skips this session and goes straight to Desk Research. They bring any current-state notes in place of `evaluation.md`.

**Not yet:** run the full session, or only Parts 2 to 4 (principles, what a finding looks like, severity) if the gap is narrow. Say which gap showed up (ratings without reasoning, findings without proof, principles misnamed) so the mentee knows what to practise.

---

## Core Content

### Opening: Opinion Isn't a Finding

**Spot it (1 min).** Show the food-delivery checkout screen. Ask: *"Find one thing that would slow a hungry customer down. Tell me what it is."* Take two answers.

Then name what just happened. Both answers were a start, and both were probably opinions: "it's cluttered", "the button is hard to see". Those are real reactions, but they can't be checked, can't be ranked, and a teammate can't act on them.

**The shift (3 min).** An evaluation turns a reaction into something usable. It has four parts:

1. **What I saw**: an observation anyone could confirm
2. **Where**: the exact screen and step
3. **Which principle it breaks**: the standard you're judging against
4. **Proof**: a screenshot or example

> **No screenshot, no finding.** This is the one rule the whole session rests on.

Evaluation is also not redesign. Describing the problem and proposing the fix are two different jobs. Today's job is only the first.

---

### Part 1: Choose a Method by Stage

#### The question to ask first

Before judging anything, ask: *what do I have, and what do I need to know?* The method follows from the stage your project is in.

**Where is your project?**

| Stage | What you have | Good starting method |
|---|---|---|
| Draft | Screens exist, nothing shipped, no users yet | Heuristic evaluation, then a walkthrough of the one key task |
| Live, you designed it | A shipped flow and some data | Analytics and feedback to find where, then heuristic evaluation on those spots |
| Live, you inherited it | Someone else's product, often with a backlog of complaints | Analytics and feedback first (fast), then heuristic evaluation on the flagged flows |

#### Three methods, one line each

| Method | The question it answers | Needs | Limit |
|---|---|---|---|
| Analytics, feedback review, SUS | *Where* are users struggling, and how much? | Existing data, support tickets, reviews, or a short survey | Tells you where and how much, not why |
| Cognitive walkthrough | Can a first-time user finish *this one task*, step by step? | One task and the screens | Slow. One task at a time |
| Heuristic evaluation | Does this design break well-known principles? | Screens and the principle list. No users needed | It is judgment. It finds many problems but not all of them |

**SUS (System Usability Scale)** in one breath: a 10-statement survey answered on a 5-point agree scale. The result is a score from 0 to 100, and around 68 is the commonly cited average. It tells you *how well* the product is doing overall, not *what* is wrong.

**The cognitive walkthrough** gets one sentence live, because it isn't practised in this session. The four questions go on the Cheat Sheet. At every step of one task, it asks:

1. Will the user try to do the right thing at this step?
2. Will they notice the right action is available?
3. Will they connect that action with what they're trying to do?
4. After they act, will they see that it worked?

A "no" to any of the four is a finding.

**Usability testing with real users** is the next step up when you need to see behaviour, not judge a design. It is taught later in the track. Evaluation tells you where to point it.

#### Your own design is the hardest one to see

If you designed it, you know why every choice was made, so you can't see it as a first-time user would. Three habits help:

- Do a task, not a tour. Walk it as someone who has never seen it, with a goal ("reorder my usual meal").
- Judge against the principle list, not your memory of why you chose it.
- Read the on-screen text out loud. Jargon and vague labels become obvious.

A finding in your own work isn't a failure. It's the evaluation doing its job.

*No slide for this in the current deck. Use the three habits as coaching during Practice A.*

---

### Part 2: The Principles

#### What heuristic evaluation is

**What.** Checking a design against a set of proven usability principles (heuristics). A few evaluators walk the screens and note where a principle is broken. No users are needed.

**Why use it.** It is fast and cheap: no recruiting and no test session. It finds problems before users meet them. It gives the team evidence and a shared language.

**When.** On a draft, before user testing. Before release, as a last pass. After launch, when there are complaints or drop-off. It does not replace user testing.

Teach the ten from `framework-nielsen-usability-heuristics.md`. Show all ten on **one overview page first**, grouped into three families so a junior has a map. Then take **each principle on its own slide**, about a minute each: the plain meaning, one broken food-delivery example, and one check-for line. The ten slides are reused as is from the Audit & Desk Research deck (Heuristic 01 to 10, already inside the built deck): each has a definition, a Why it matters line, and a bad and good UI example. Teach the slide's own example first, then use the food-delivery line in the tables below as the bridge to the checkout. Budget 2 minutes for the definition, 1 for the overview and 11 for the ten slides `[to confirm: estimates]`. Hand out the Cheat Sheet at the Part 2 divider and tell the mentee to keep it beside them for the rest of the session. Don't ask a discussion question on every slide: each slide's speaker notes mark the ones that earn one.

#### Family 1: Can I see and understand what's going on?

| Heuristic | In plain words | What it looks like broken (food delivery) |
|---|---|---|
| 1 Visibility of system status | The product tells me what's happening | After tapping Place Order, the screen sits on a spinner. Did my payment work? |
| 2 Match with the real world | It speaks my language | A line labelled "SF" instead of "Service fee" |
| 6 Recognition over recall | I don't have to remember things | The promo code I entered earlier isn't shown on the order summary |
| 8 Aesthetic and minimalist design | Only what matters is on screen | Upsell banners push the order total below the fold |

#### Family 2: Can I stay in control and recover?

| Heuristic | In plain words | What it looks like broken (food delivery) |
|---|---|---|
| 3 User control and freedom | I can undo or back out | Pressing Back from payment empties my cart |
| 5 Error prevention | It stops me making the mistake | The tip field accepts 5000 when I meant 5.00 |
| 9 Recognise, diagnose, recover from errors | Errors tell me what to do next | "Payment failed. Error 4012." and nothing else |

#### Family 3: Is it predictable and efficient?

| Heuristic | In plain words | What it looks like broken (food delivery) |
|---|---|---|
| 4 Consistency and standards | Same thing, same look, same word | "Checkout" on one screen, "Pay now" on another, for the same step |
| 7 Flexibility and efficiency | Fast for people who've done it before | No way to reorder a past meal or save an address |
| 10 Help and documentation | Help is there when I need it | No explanation of what the "service fee" covers |

**Tip for juniors:** when you spot a problem and can't name the heuristic, find the family first ("this is about not knowing what's happening") and then narrow to the heuristic. If a problem fits two heuristics, pick the closest one and note the second. Don't stall.

#### Take-home: the accessibility check (WCAG 2.1 AA)

Not taught live. Hand it out with the Cheat Sheet. After class, the mentee runs one extra pass on the same screens, with four fast checks:

| Check | What to look for | Reference |
|---|---|---|
| Text contrast | Body text at least 4.5:1 against its background. Large text and UI component borders at least 3:1 | WCAG 1.4.3, 1.4.11 (AA) |
| Colour alone | Is anything communicated by colour only (a red field with no message)? | WCAG 1.4.1 (A) |
| Labels | Does every input have a visible label, not just placeholder text? | WCAG 3.3.2 (A) |
| Touch targets | Tap targets about 44 x 44 pt. Note: WCAG 2.1 doesn't require this at AA, it is a recommended practice | Best practice (2.5.5 is AAA) |

Log accessibility issues in the same worksheet, using the check name in the Heuristic column.

---

### Part 3: Apply It in the Workplace (What a Finding Looks Like)

From this part on, every activity uses the mentee's own product. The food-delivery examples only illustrate the finding format. Restate the four-part format: what I saw, where, which principle, proof. No screenshot, no finding. Keep the Cheat Sheet beside you.

#### What a good finding looks like

| Weak | Strong |
|---|---|
| "The checkout is confusing." | At Review order, the service fee is labelled "SF" with no explanation. A user can't tell what they're paying for before they commit. Breaks *Match with the real world*. Screenshot attached. |

> The strong example is a format demonstration, not a claim about any real app. The mentee's findings come from what they actually see in their own product.

**Three tests for a finding.** Before logging an issue, check it against these:

1. **Is it something you saw, not felt?** "The button is grey" is a sighting. "It looks ugly" isn't.
2. **Does it affect what the user can do or understand?** If not, it's a preference.
3. **Is it a problem, not a fix?** "Make the button blue" is a solution. Write the problem it would solve.

---

### Part 4: Rate Severity

Teach from `framework-severity-rating-scale.md`.

#### What severity is, and why rate at all

Severity is a number from 0 to 4 for how seriously a problem harms the user. A list of 25 findings is a list of complaints. A ranked list is a plan. Three reasons to rate:

1. **A team cannot fix everything.** A list of 30 issues has to become an order of work.
2. **It separates what matters from what doesn't.** Without a score, a tiny grey mismatch gets the same attention as a lost cart.
3. **The whole team gets one language.** A number is easier to agree on than an opinion.

#### The scale

| Score | Label | Meaning |
|---|---|---|
| 0 | Not a problem | Not a usability issue. Don't log it |
| 1 | Cosmetic | Fix if there's spare time |
| 2 | Minor | Low priority |
| 3 | Major | Important, high priority |
| 4 | Catastrophe | Must fix before release |

#### Three plain questions

Don't guess a number. Ask:

1. **How often?** Does everyone hit it, or only some people on some days?
2. **How bad when it happens?** Can the user recover, or are they stuck, charged twice, or losing data?
3. **Does it keep happening?** Is it confusing once, then learned, or does it cost the user every time?

If a fourth thing is on your mind, ask whether it damages trust in the product. Data loss and double charges do. The framework doc calls this market impact.

#### From answers to a number: the 2x2

Plot each issue on two axes: **frequency** (rare to often) and **impact** (small to big).

| | Rare | Often |
|---|---|---|
| **Big impact** | Usually 2 or 3 | Usually 3 or 4 |
| **Small impact** | Usually 0 or 1 | Usually 2 |

Then use the third question to nudge: if it **keeps costing the user every time**, round up. If it **wears off after the first time**, round down. The top-right of the plot is where you start your report.

> Two evaluators rarely give the same number. The goal is to land within one point of each other, and to be able to explain why.

#### Calibrate

Calibration now happens in Practice B, on the mentee's own findings. The three issues in Appendix D stay available for the Senior Fast-Track and as a reserve activity.

#### From severity to a next move (2 min)

A severity number also decides how to respond when the person who owns the build declines a change. Run one short case, with no names: a developer or product owner does not want to add a pop-up that the designer proposed.

Three moves, in order:

1. **Ask what happens to the user without the change.** Can they still finish the task and recover from a mistake, or are they blocked or losing data?
2. **Argue from evidence, not taste or favour.** Name the principle, the observed behaviour, the user impact and the severity, and attach the screenshot.
3. **If it cannot be built, propose an alternative that keeps the outcome for the user.** For example, an inline message at the point of the problem instead of a pop-up.

Severity then sets how hard to hold:

| Severity | Typical response |
|---|---|
| 1 to 2 | Accept the "no", or park it in the backlog |
| 3 | Make the case with evidence, and look for an alternative |
| 4 | Hold the position. It must be fixed before release |

> The learner may not own the decision. The goal is to give the decision-maker clear evidence and a workable alternative, not to win the argument. A junior designer who cannot settle it escalates with the evidence in hand.

> This is the author's working method. It is not drawn from published research. The 0 to 4 scale itself comes from the severity framework cited in Further Resources.

---

### Part 5: AI as an Assistant (Talk)

By now the mentee has the principles and the severity scale. AI is introduced to extend their own judgment, not to replace it. Practice A and B come first and are manual. AI is used hands-on only in Practice C.

#### The rule: AI assists, you decide

AI can look at a screenshot and miss the thing you saw, or invent something that isn't there. It has no idea who your users are. The mentee's manual pass is what lets them tell the difference. Say this out loud at the start of the block.

Every AI suggestion goes through three gates before it reaches the worksheet:

1. **Gate 1: can I see it on the screen?** Point to the exact element. If not, drop it.
2. **Gate 2: does it break a principle?** Name the principle. If not, drop it.
3. **Gate 3: would a real user hit it?** If it is only true in theory, drop it.

Say what AI will not do today: rate severity, change the mentee's scores, or suggest a redesign. The scores stay the mentee's. Expect to discard some suggestions. That means the check is working. Before uploading anything, blur real customer data and follow the company's rules.

#### The five-step workflow (overview)

| Step | Time | What happens |
|---|---|---|
| 1 Prep | Done beforehand | Save the principles and the severity scale as one markdown file (the principles file). It is the standard AI checks against, and it is reused on every run |
| 2 Cross-check | 3 min | Give AI the flow (screenshots) and the principles file. It returns possible issues. Ask it to name the screen and the principle for each |
| 3 Review | 3 min | Run each suggestion through the three gates and drop what fails. This comes before step 4 so invented issues never reach the main file |
| 4 Build | 4 min | AI arranges what is left into `evaluation.md`. The severity scores stay the mentee's. Note which scores AI suggested |
| 5 Visualise | 2 min | Generate `evaluation.html` from `evaluation.md`: a ranked table and the 2x2. `evaluation.md` is the source. To change anything, edit the `.md` and regenerate, never edit the `.html` |

Final check: the number of findings matches, no score has changed, and three random rows match the screenshots. Common mistake: skipping step 3 because the AI output "sounds right". Sounding right is not the same as being right.

#### Beyond today: three levels of AI evaluation (2 min, talk only)

What the mentee just did is level 1. Name the other two so they know where the practice goes next. Do not demo them live.

| Level | How it works | You still do | Where it breaks |
|---|---|---|---|
| 1. You capture, AI compares | You take the screenshots. AI gets them plus the principles as a text file, and returns a list of possible issues | Capture, verify every suggestion, rate severity | Only as complete as your screenshots. Today's level |
| 2. Paste a URL, a tool audits | A dedicated heuristic-evaluation tool opens the page itself, scores each principle and attaches evidence | Compare its findings with your manual worksheet. Judge what it got right and what it missed | Public pages only. Behind a login it sees nothing. Scores can look more certain than they are |
| 3. An agent walks the flow | A browser-automation agent clicks through a flow, captures every step, then evaluates against the principles | Define the task and the success path. Check the evidence. Log in by hand when the flow needs it | Web only. Needs setup. It follows the path you give it, so it can miss what a confused first-time user would try |

**Why the manual pass still matters at every level.** Research comparing a vision-capable AI model with expert evaluators found it recovered only about a fifth of the issues the experts found (21.2%), added issues of its own, and produced false positives from hallucination. It did best on *Match with the real world* and *Aesthetic and minimalist design*, and worst on flexibility, control and efficiency, which need interaction rather than a still image. Feedback quality also dropped as a design was revised over several rounds. Source: *Can GPT-4o Evaluate Usability Like Human Experts?* (arXiv 2506.16345) and *Generating Automatic Feedback on UI Mockups with Large Language Models* (arXiv 2403.13139).

Tie it back to the seeded set: the "Back empties the cart" issue (P5) is an interaction problem. A still screenshot can't show it, so an AI working from stills will not find it. A level 3 agent could.

**Make the level 1 principles file reusable.** The Cheat Sheet is the mentee's principles file. Saved as a markdown file in the AI foundation folder, the same file feeds level 1 today, a level 2 comparison later, and a level 3 agent when they are ready.

---

### Practice A: Evaluate Your Own Flow (Manual, 20 min)

No AI in this block. The mentee uses the Cheat Sheet, the Worksheet, and their screenshots.

**Setup (2 min).** Confirm the flow and screenshots. Confirm which entry point applies: *I designed this* (use the three habits from Part 1) or *I inherited this* (note any known complaints, but judge the screens, don't repeat the complaints).

**Evaluate (16 min).** For each step of the flow:

1. Look at the screen as a first-time user doing the task.
2. Check each family: seeing and understanding, control and recovery, predictable and efficient.
3. Log every issue in the Worksheet with the four-part format (what I saw, where, which principle, proof) and a screenshot file name.

**Target: about 5 findings (3 to 5 is enough).** Quality over count. The accessibility check is a take-home. Rating happens in Practice B.

**Share back (2 min).** Mentee names their strongest finding and the evidence for it.

**Facilitator watch-fors:**

- A list of ten cosmetic points and nothing about the task. Redirect to the task
- Solutions written instead of problems. Ask: "What is the problem that fix would solve?"
- Findings with no screenshot. They don't count yet
- Defending the design instead of logging the issue ("I did it that way because..."). Acknowledge it, then log it
- Two people choosing different principles for the same issue is a good discussion, not a mistake. Use the Cheat Sheet to name the principle

---

### Practice B: Rate Your Own Findings (Manual, 5 min)

Take the findings from Practice A. Rate each from 0 to 4, silently, using the 2x2 and the three questions: how often, how bad, does it keep happening. Compare with the mentor (in a class, with a neighbour). Where the two ratings differ by more than one point, explain the reasoning. The reasoning matters more than matching the number. Log frequency, impact and severity in the Worksheet.

**Facilitator watch-fors:**

- Everything rated 4. Ask: "If everything is a catastrophe, what's first?"
- Ratings based on taste. Ask the three questions again

---

### Practice C: Build Your Evaluation With AI (12 min)

Keep the prompts (see AI in Practice) on screen. Step 1 (Prep) is already done: the principles file is ready. The mentee works on their own flow and their own findings.

#### Step 2: Cross-check (3 min)

The mentee gives AI their screenshots and `assets/heuristics.md` (the Cheat Sheet as a markdown file) and asks it to brainstorm issues they may have missed, one family at a time. AI does not rate severity and does not suggest fixes at this stage.

#### Step 3: Review (3 min)

For every AI suggestion, the mentee asks three questions:

1. **Can I see it on the screen?** (Point to the exact element.)
2. **Does it really break that principle?**
3. **Would a real user hit it?**

Yes to all three: add it to the Worksheet with a screenshot and rate it yourself. Otherwise discard it. Expect to discard some.

#### Step 4: Build your own `evaluation.md` (4 min)

The mentee asks AI to turn their finished Worksheet into a single `evaluation.md` using the schema in Appendix C. AI structures. It does not add findings and does not change the mentee's severity scores.

Save the file in the AI foundation folder. It is a reusable asset: next project, the mentee starts from the same schema.

**Check the output:** the number of findings matches the Worksheet, every finding has an evidence file name, and no score has changed.

#### Step 5: Visualise `evaluation.html` (2 min, then homework)

In class, the mentor shows the prompt and a finished `evaluation.html` built from a sample `evaluation.md`. The mentee generates their own as homework, asking an AI tool that can create files to read `evaluation.md` and generate one HTML page: a summary, a table ranked from highest severity to lowest with the screenshot embedded in each row, and the 2x2 plot with each issue as a numbered point.

- **Embed the screenshots in the HTML** so it is one portable file. Resized images keep it small.
- **`evaluation.md` is the source of truth.** To change a score, edit the `.md` and regenerate the `.html`. Never edit the `.html` by hand.
- **The page must pass its own checks.** Ask for text contrast of at least 4.5:1 and for severity to be shown by number or shape as well as colour.

**Check the output:** spot-check three rows against the `.md`, and check the position of three points on the plot.

---

### Close (4 min)

1. Read the in-session checkpoint aloud and check it against the mentee's work: one flow, about 5 findings (3 to 5 is enough), each rated and each with a screenshot. Say that the full Success Check is met with the assignment.
2. Brief the homework.
3. Name where evaluation stops: it tells you *what* is wrong and *where*. It can't tell you *why* users struggle. Ask: *"Pick your top finding. What do you believe about your user that makes it a problem, and how do you know?"* Take one answer.
4. Bridge: *"Next session, Customer Understanding, starts from there. Your `evaluation.md` shows where friction is likely. Talking to real users tells you why, and which of your beliefs are wrong."*

> **Facilitator note:** Mid-level mentees take Desk Research between this session and Customer Understanding. For them, the bridge is the same, with the findings in `evaluation.md` becoming evidence in Desk Research.

---

## Activities

### Activity: Evaluate Your Own Flow
**Type:** In-class · Worksheet (Appendix B) · no AI
**Time:** 20 min
**Format:** Solo, with coaching

See Practice A.

---

### Activity: Rate Your Own Findings
**Type:** In-class · Worksheet (Appendix B) · no AI
**Time:** 5 min
**Format:** Solo, then compare with the mentor (or a neighbour in a class)

See Practice B.

---

### Activity: Build Your Evaluation With AI
**Type:** In-class · AI chat tool, plus a demo of an AI tool that creates files
**Time:** 12 min
**Format:** Solo, with coaching

See Practice C.

---

## Reserve Activities (not in the current session plan)

These ran in earlier versions of the session. They are kept for a lighter or longer slot and for the Senior Fast-Track. They use Appendices D, E and F.

### Activity: Place Your Project and Pick a Method
**Type:** In-class · discussion
**Time:** 3 min (was inside Part 1)
**Format:** Solo, then share

1. **(1 min)** Place your project on the stage table: draft, live and you designed it, or live and you inherited it.
2. **(1 min)** Pick one method to start with and write one line on why.
3. **(1 min)** Share back. Mentor challenges one choice: "What would you learn that you don't already know?"

---

### Activity: Match the Symptom
**Type:** In-class · Appendix E
**Time:** 3 min (was the end of Part 2)
**Format:** Solo, then reveal

1. **(2 min)** Read each of the six symptom cards. Name the principle number and its family.
2. **(1 min)** Reveal. If a symptom fits two principles, accept either when the mentee can say why. Ask which two were hardest to place.

---

### Activity: Evaluate the Checkout Together
**Type:** In-class · seeded checkout set (Appendix F) + Cheat Sheet
**Time:** 12 min
**Format:** Mentor models, then solo, then share

1. **(3 min)** Mentor models one finding end to end.
2. **(6 min)** Mentee finds two more findings in the four-part format, each with a screenshot.
3. **(3 min)** Compare and discuss.

**How the guided practice runs**

1. **Mentor models one finding end to end** on the seeded checkout set (Appendix F), using the service fee finding. Think aloud: what I saw, where, which family, which heuristic, then capture the screenshot and circle the spot. About 3 minutes.
2. **Mentee finds two more**, using the same four-part format and the Cheat Sheet. About 6 minutes.
3. **Share back.** Compare with the answer key. Did anyone choose a different heuristic for the same issue? That's fine, and a good discussion. About 3 minutes.

The seeded set has nine planted issues and the mentee only needs two. Accept an unplanted issue too, if it passes the three tests.

---

### Activity: Calibrate Severity
**Type:** In-class · Appendix D
**Time:** 5 min (was inside Part 4)
**Format:** Solo, then pair

1. **(2 min)** Rate the three issues silently using the 2x2 and the three questions.
2. **(3 min)** Compare with the mentor. Where you differ by more than one point, explain your reasoning.

---

## AI in Practice: Cross-check, Build, Visualise

This session's AI use is deliberately late and deliberately limited. The mentee does the judging. AI helps them see more, structure what they found, and show it.

### 🤖 The three prompts

**Cross-check (step 2):**

> *"I'm evaluating the [flow name] of [product]. Attached are screenshots of each step, in order. The attached heuristics.md has the usability principles in three groups, with rules and an output format. Follow it. Review one group at a time. For each possible problem, tell me which step, point to the exact element or quote the exact text, and name the principle. Do not rate severity. Do not suggest redesigns. If you can't tell from the screenshot, say 'not sure'."*
> [attach heuristics.md]

**Build `evaluation.md` (step 4):**

> *"Here is my completed findings worksheet: [paste]. Turn it into one markdown file named evaluation.md using exactly this structure: [paste the schema from Appendix C]. Do not add findings. Do not change any severity score. If a field is missing, write MISSING instead of guessing."*

**Generate `evaluation.html` (step 5, homework):**

> *"Read evaluation.md. Generate one self-contained HTML file named evaluation.html with: (1) a summary header, (2) a table sorted by severity, highest first, with each row showing the id, title, heuristic, severity, and the screenshot, (3) a 2x2 plot with frequency on the horizontal axis and impact on the vertical axis, each issue shown as a numbered point. Embed the screenshots in the file. Use only data from evaluation.md. Text contrast at least 4.5:1, and show severity with a number or shape as well as colour."*

### 🧠 Critical thinking

- Where did AI point to something that wasn't on the screen? What gave it away?
- What did you catch in your manual pass that AI missed? What did AI catch that you missed?
- Rating severity needs to know your users and your business. What did AI not know?
- Which of your findings needed interaction, not a still image? Could levels 2 or 3 have found it?

### ✍️ Prompt engineering tip

Tell AI what *not* to do. "Do not rate severity" and "do not change any score" keep the judgment with you and make the output easier to check. Constraints are as useful as instructions.

### ⚖️ Ethics consideration

Screenshots of real products can contain customer data or confidential designs. Before uploading anything to an AI tool, blur personal data and check your company's rules. And an AI-written explanation of an issue is not evidence. Only the screenshot is.

---

## Assessment

### Quick knowledge check

Optional. Run verbally in the buffer after Part 4, or set as a take-home self-check:

1. Your analytics show a big drop-off at one step and you have no budget for user testing. Which method do you start with, and then which?
2. What makes something a finding rather than an opinion?
3. Two issues both happen often. One is a confusing label, the other charges the customer twice. Which goes first, and why?
4. A developer declines a change you rated 2, and another you rated 4. Which do you hold, which do you let go, and what do you bring to the conversation?

---

## Assignments

### Assignment: Finish and Share Your Evaluation

> `[to confirm]` The deck slide shows a shorter assignment: evaluate the current experience of your own product with heuristic evaluation, rate each finding by severity, add a screenshot to each, and submit one evaluation worksheet, done by hand or with AI support. The detailed version below is kept until Winnie confirms which one stands. The Customer Understanding handoff depends on the "Open questions about users" item.

**Due:** Before next session
**Time estimate:** 2 to 2.5 hours
**Type:** Analysis · Your real project

1. Complete the evaluation of your first flow. In class you logged 3 to 5 findings, so cover every remaining step.
2. Evaluate **a second flow** of the same product, using the same manual-first order: Worksheet first, then AI to brainstorm.
3. Run the four accessibility checks from the Cheat Sheet on both flows and log what you find in the Worksheet.
4. Make sure every finding has a screenshot or example and a severity from 0 to 4.
5. Generate your final `evaluation.md` covering both flows, then use the HTML prompt to generate `evaluation.html`.
6. Write one line at the top of `evaluation.md`: which method you started with and why.
7. At the bottom of `evaluation.md`, add a section called "Open questions about users". For your top three findings, write one line each: *what do I believe about the user here that I haven't checked?* You'll use these in Customer Understanding.
8. Optional stretch: ask a peer to rate your top three issues without seeing your scores, then compare. Where you differ by more than one point, write down why.
9. Optional stretch (level 2): run one public page of your product through a dedicated AI heuristic-evaluation tool. Compare its findings with your worksheet in three lists: both found, only you found, only the tool found. Write one line on which list surprised you.

**Deliverable:** `evaluation.md` and `evaluation.html`, covering two flows, at least 6 findings in total, ranked by severity, each with evidence, plus three open questions about users. Save to your homework folder before the next session.

> **AI in Practice:** *"Here is my evaluation.md: [paste]. Check it against my screenshots. Which findings are vague, missing evidence, or written as solutions instead of problems? Don't edit anything, just list them."*

---

## Practice Dataset

Mentees who can't bring their own product can evaluate the full seeded checkout set (Appendix F) end to end with the same Worksheet.

---

## Appendix A: Heuristics Cheat Sheet (one page)

**Family 1: Can I see and understand what's going on?**

- 1 Visibility of system status: after any action, show what happened
- 2 Match with the real world: use the user's words
- 6 Recognition over recall: show it, don't make me remember it
- 8 Aesthetic and minimalist design: if it doesn't help the task, remove it

**Family 2: Can I stay in control and recover?**

- 3 User control and freedom: undo, cancel, go back safely
- 5 Error prevention: stop the mistake before it happens
- 9 Recognise, diagnose, recover from errors: say what went wrong and what to do next

**Family 3: Is it predictable and efficient?**

- 4 Consistency and standards: same thing, same look, same word
- 7 Flexibility and efficiency: shortcuts for repeat users
- 10 Help and documentation: help at the point of need

**Take-home accessibility check (WCAG 2.1 AA):** contrast 4.5:1 text and 3:1 UI parts · not colour alone · visible labels · tap targets about 44 pt (best practice)

**Walkthrough (each step of one task), a "no" to any is a finding:**

1. Will they try to do the right thing at this step?
2. Will they notice the right action is available?
3. Will they connect that action with what they're trying to do?
4. After they act, will they see that it worked?

**Finding format:** What I saw · Where · Which principle · Proof

**Severity:** 0 not a problem · 1 cosmetic · 2 minor · 3 major · 4 catastrophe

---

## Appendix B: Evaluation Worksheet (manual)

| # | Where (screen / step) | What I saw | Heuristic or WCAG check | Evidence (file name) | Frequency (rare / sometimes / often) | Impact (small / medium / big) | Severity (0 to 4) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |

---

## Appendix C: `evaluation.md` Schema

```
# Evaluation: [product], [flow]

- Date:
- Evaluator:
- Method: [which method you started with, and why, in one line]
- Scope: [flow name, number of steps]

## Findings (ranked by severity, highest first)

### F1: [short title]
- Where:
- What I saw:
- Heuristic or WCAG check:
- Evidence: [screenshot file name]
- Frequency:
- Impact:
- Severity: [0 to 4]

### F2: [short title]
...
```

A suggested fix is deliberately not part of the schema. Evaluation describes the problem. Fixes come later.

---

## Appendix D: Calibration Issues (food delivery, illustrative)

These are teaching examples, not claims about any real app. C1 and C2 also appear in the seeded checkout set (Appendix F), so the mentee has already seen those screens.

| # | Issue | Mentor's suggested rating and reasoning |
|---|---|---|
| C1 | After tapping Place Order, the screen stays on checkout with a spinner for 8 to 10 seconds and no confirmation. Some users tap again and place a double order. (Visibility of system status, Error prevention) | **4.** Everyone who orders hits the wait, the impact is a double charge, and trust is at stake. Many would argue 3. The reasoning matters more than the number. |
| C2 | The service fee line is labelled "SF" with no explanation. (Match with the real world, Help and documentation) | **2.** Every order sees it and it keeps happening, but impact is small: confusion, not a blocked task. Raise to 3 if you argue it harms trust. |
| C3 | The promo code field uses a slightly different grey from the other fields on the same screen. (Consistency and standards) | **1.** Rarely noticed, no effect on completing the task. |

---

## Appendix E: Match the Symptom (six cards)

Read each card. The mentee names the principle and its family. If a symptom fits two, accept either with a reason.

| # | Symptom (food delivery) | Principle | Family |
|---|---|---|---|
| 1 | The order status says "Preparing" for 40 minutes and never changes | 1 Visibility of system status | See and understand |
| 2 | A confirmation dialog asks "Proceed with disposition?" | 2 Match with the real world | See and understand |
| 3 | I removed an item from my cart by accident and there is no undo | 3 User control and freedom | Control and recover |
| 4 | Stars on the rating screen, thumbs on the review screen, for the same rating | 4 Consistency and standards | Predictable and efficient |
| 5 | The delivery address field accepts a 3-digit postcode | 5 Error prevention | Control and recover |
| 6 | "Something went wrong." and a Close button | 9 Recognise, diagnose, recover from errors | Control and recover |

---

## Appendix F: Seeded Checkout Set

Five screens of a neutral mock food-delivery checkout (no real brand), exported at about 1200 px wide: Cart, Review order, Payment, Placing order, Payment failed. Nine issues are planted, so every mentee faces the same findings. The mentor models P1. The mentee finds two others.

| ID | Screen | Planted issue | Principle(s) | Suggested severity |
|---|---|---|---|---|
| P1 | Review order | The fee line is labelled "SF" with no explanation | 2 Match, 10 Help | 2 |
| P2 | Review order | The promo code applied earlier is missing from the summary | 6 Recognition over recall | 2 |
| P3 | Review order | Three banners push the order total below the fold | 8 Minimalist design | 2 |
| P4 | Payment | The tip field accepts 5000 | 5 Error prevention | 3 |
| P5 | Payment | Back from this screen empties the cart | 3 User control and freedom | 3 |
| P6 | Payment | The button says "Pay now"; the cart screen said "Checkout" for the same step | 4 Consistency and standards | 1 |
| P7 | Placing order | A spinner and no confirmation, with the button still tappable | 1 Visibility, 5 Error prevention | 4 |
| P8 | Payment failed | "Payment failed. Error 4012." with no next step | 9 Recover from errors | 3 |
| P9 | Cart | The past-orders list has no Reorder button | 7 Flexibility and efficiency | 2 |

**Built:** the five screens are original mocks (fictional brand "Biteline"), exported at 1170 px wide in `assets/seeded-checkout/`. Calibration issues C1 (P7) and C2 (P1) in Appendix D reuse these screens.

**Mentor notes on the set:**

- **P5 (Back empties the cart) is behaviour, not visible in a still.** The mentor narrates it. Use the Payment screen as the location evidence. Don't pick P5 as the modelled finding, and don't expect mentees to find it from the PNG alone.
- **P7 shows the spinner and an enabled "Place order" button.** The 8 to 10 second wait is narrated.
- **P2:** the Cart screen shows promo SAVE5 applied. The Review order summary has no promo line.
- **P3:** on Review order the total sits below the fold, behind the sticky button.
- **P4:** the tip field shows 5000 and the total reads $5,023.30.

---

## Further Resources

- **Nielsen's 10 Usability Heuristics (internal):** `library/frameworks/framework-nielsen-usability-heuristics.md`
- **Severity Rating Scale (internal):** `library/frameworks/framework-severity-rating-scale.md`
- **NN/g, 10 Usability Heuristics for User Interface Design:** https://www.nngroup.com/articles/ten-usability-heuristics/
- **NN/g, How to Rate the Severity of Usability Problems:** https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
- **W3C, WCAG 2.1 Quick Reference:** https://www.w3.org/WAI/WCAG21/quickref/

---

*Created by Winnie Nguyen · Private Training · Last updated October 2026 (prep pass 7 Oct)*
