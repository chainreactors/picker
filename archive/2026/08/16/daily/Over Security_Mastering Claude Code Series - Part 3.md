---
title: Mastering Claude Code Series - Part 3
url: https://attacker-codeninja.github.io/2026-08-16-Mastering-Claude-Code-Series-3/
source: Over Security
date: 2026-08-16
fetch_date: 2026-08-17T02:54:35.881043
---

# Mastering Claude Code Series - Part 3

[![Logo](/assets/img/code_ninja_svg.svg)
**ATTACKER-CODENINJA.GITHUB.IO**  /  Mastering Claude Code Series - Part 3](/)

LIVE

[Home](/)
[Bug Bounty](/category/bug-bounty/)
[AWS Projects](/category/aws-projects/)
[Claude Code Masterclass](/category/claude-code-masterclass-series/)

August 16, 2026

# Mastering Claude Code Series - Part 3

[Claude Code](/tags#Claude Code)
[Context Engineering](/tags#Context Engineering)

# Claude Code Foundation (Part 2)

Hello Everyone! 👋 Welcome back to **Part 3** of the **Mastering Claude Code Series**.

In our previous post, we took a deep dive into the 3-Layer Architecture of Claude Code (The Brain, The Harness, and The Tools). We saw how they work together, and why understanding this is crucial for mastering AI-assisted development.

But before we dive back into the next set of foundational concepts, let’s hit pause for a moment. ⏸️

Whenever you learn something completely new and paradigm-shifting (like the fact that the AI model is stateless and doesn’t actually touch your files directly), it’s completely natural to have questions.

So, instead of just rushing forward to continue the foundation, **let’s first address and explore some of the most burning doubts** you might have from the previous part. Clearing these up will make everything that follows much easier to understand! 💡

---

![Context Engineering Explained](/assets/img/context-engineering-explained.png)

---

### 🧐 Doubt #1: Why does AI ignore my rules even if I just told it?

In our last post, we explained that when the AI “forgets” something, it’s often because that information was pushed out of the Context Window.

> *“The AI did not forget in the human sense. The reality is that the relevant information was simply no longer present in the reconstructed context package.”*

While that is directionally correct, it is only **half the story.**

When an AI model seems to ignore your instructions or forget a rule, there are actually **two entirely different mechanisms** at play.

Mixing them up is a huge mistake if you want to master AI.

#### Mechanism 1: Absence (It was physically removed)

This is what we talked about previously. As the conversation gets too long, older information is literally removed, truncated, or heavily summarized by the harness to save space.

* **What happens:** The information is physically missing from the package sent to the AI’s Brain.
* **The Result:** The model literally has no idea you ever gave it that instruction.

#### Mechanism 2: Dilution / Low Salience (It got buried)

This is the silent killer of AI productivity.

In this scenario, your instruction *is* still inside the context package. It hasn’t disappeared or been deleted. However, the context window has become so bloated with giant code files, error logs, and long conversations that your one small rule gets completely buried.

**Let’s understand this with a simple human example:**
Imagine you are a chef in a busy kitchen.

* If a waiter hands you a single sticky note that says, *“Table 4 wants no onions,”* you will easily remember it and follow the rule.
* But imagine if the waiter hands you a 50-page menu, 10 different recipes, a list of inventory, 20 customer reviews, and right in the middle of page 32, there is a tiny sentence that says, *“Table 4 wants no onions.”*

What happens? You didn’t “forget” how to read, and the instruction wasn’t deleted from the paper. But because there was so much other loud, distracting information, your brain naturally **under-weighted** that tiny instruction. It lost its importance.

**This is exactly how an AI model’s “attention mechanism” works.**

* **What happens:** When you feed the AI thousands of lines of code and logs, its attention is spread too thin. Your specific instruction (like *“always use strict typing”*) loses its “weight” or visibility. This is called *Low Salience*.
* **The Result:** The model didn’t technically forget. It simply got overwhelmed by the noise and ignored your rule because everything else in the context was screaming for its attention.

> **💡 The Big Takeaway:**
> When your AI misbehaves, you must diagnose it like an engineer:
>
> Did my instruction get physically pushed out of the context (Absence), or did it just get drowned out by too much noise (Dilution)?

---

### 🧐 Doubt #2: “But my CLAUDE.md file is in the context! Why does the AI still ignore my rules?”

This is a fantastic question. You might be thinking: *“I put my strict rules in the `CLAUDE.md` file. I know for a fact that the harness keeps this file in the context package at all times. It is never absent. So why does the AI still ignore it?”*

If it’s not an **Absence** problem, it is definitely a **Dilution** problem. Even if your `CLAUDE.md` is physically inside the context, your rules are still missing the mark for three specific reasons:

#### 1. Recency Bias (The “Shiny New Toy” Syndrome)

AI models have a strong “recency bias.” This means they naturally give much more weight and importance to the *most recent* messages.

If your `CLAUDE.md` file was loaded at the very beginning of the session (Turn 1), and you are now on Turn 50, that static instruction feels “old” to the model’s attention mechanism. It is technically there, but the model cares significantly more about what you just typed 5 seconds ago.

#### 2. Instruction Competition (Tug of War)

In any given prompt, the model is receiving a lot of competing instructions all at once:

* The core system rules
* Your `CLAUDE.md` rules
* Your actual chat message
* The raw outputs of the tools it just ran

All these inputs are fighting to “win” the model’s attention. If your `CLAUDE.md` rule is poorly written or buried, it simply loses the tug of war against the other inputs.

#### 3. AI is Probabilistic, Not Deterministic

Traditional programming code is deterministic: `If X, then execute Y`. It is a 100% mathematical guarantee.

AI models do not work this way. They are probabilistic. When you give the AI a rule, it creates a *strong statistical tendency* for the AI to follow it, but it is **never a 100% guarantee.**

---

### 🛠️ How Do We Fix This? (The Mitigations)

If saying it once in a `CLAUDE.md` file isn’t enough, how do we actually force the AI to listen? We have to use smart engineering mitigations to beat the Dilution problem:

1. **Repeated Reminders:** If a rule is critically important, you cannot just say it once at the start of the session and hope for the best. You have to continuously re-inject it alongside your prompts. (Think of it like repeatedly reminding a child).
2. **External Memory Files (`TODO.md` / `SESSION_LOG.md`):** Do not rely on the AI’s internal context window to remember your project state. Create physical tracker files in your directory and instruct the AI to *explicitly read* them before taking any action.
3. **Context Compaction (Clearing the Noise):** If the conversation gets too long and noisy, the best mitigation is to simply start a fresh chat session. This clears out all the “junk” data and makes your core rules “heavy” and important again!

> *Note: Even with all these tricks, missing a rule in a massive, complex project is still possible. Context management is an actively researched area in AI, not a fully solved problem!*

---

### 📚 Industry Proof: You Are Not Alone (10 Real-World References)

If you think this is just a personal theory, don’t worry. The exact challenges (and solutions) we just discussed are some of the most actively researched topics in the AI industry right now.

Here is proof from across the internet that the greatest AI minds are fighting the same battles:

1. **The “Lost in the Middle” Paper (Stanford/UC Berkeley, 2023):** A landmark academic paper mathematically proved that LLMs suffer from severe “attention decay.” They remember the beginning and end of a prompt perfectly, but lose information buried in the middle (this proves our *Low Salience* concept).
2. **Context Window vs. Attention Budget:** AI ...