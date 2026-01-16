---
title: Interactive Replays of Conversations: A New Tool
url: https://zeltser.com/interactive-replays/
source: Lenny Zeltser
date: 2026-01-15
fetch_date: 2026-01-16T03:30:32.322099
---

# Interactive Replays of Conversations: A New Tool

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# Interactive Replays of Conversations: A New Tool

Conversation replays add an engaging dimension to training materials and docs. Save the conversation and your annotations in a data file, then use my tool to generate a self-contained HTML player you can embed anywhere.

![Interactive Replays of Conversations: A New Tool - illustration](/assets/interactive-replays.DwhVzRkZ_17MedJ.webp)

Security training often involves showing how attacks unfold through text conversations—malicious emails, social engineering calls, BEC interactions, and so on. Showing how attackers build trust over multiple messages helps people understand the pattern. Screenshots lose the temporal element and traditional videos are hard to maintain.

I released [conversation-replay](https://github.com/lennyzeltser/conversation-replay), a command-line tool you can use to generate animated replays from text conversations. You can even add annotations at key moments to highlight what the viewers should notice, such as a red flag in the scammer’s message, a suspicious request, or a clever social engineering tactic.

The tool produces a self-contained, embeddable HTML player.

## Example: Scammer’s Chat Interactions

For example, the following replay shows a classic “I’m stuck in London” scam chat, based on a [transcript documented by Rakesh Agrawal](http://rake.sh/blog/2009/01/20/facebook-fraud-a-transcript/). The scammer used a compromised account to impersonate the victim’s friend. (You can [open it in a new tab](/media/london-scam-replay.html).)

## Example: Reddit AMA Highlights

You can use conversation replays in other ways. For instance, below is a replay of the highlights from a [Reddit AMA I did several years ago](https://www.reddit.com/r/IAmA/comments/j676h9/im_lenny_zeltser_cybersecurity_practitioner/) about cybersecurity careers and practical security advice. This examples shows that you can structure the conversation into multiple sections. (You can [open it in a new tab](/media/reddit-ama-replay.html).)

## Example: AI-Assisted IR Report Writing

The following replay demonstrates how an AI assistant can help write incident response reports, from my post on [writing good IR reports with AI](/good-ir-reports-with-ai). (You can [open it in a new tab](/media/ir-report-replay.html).)

## Getting Started

To create a replay, you define your conversation in a YAML file. It’s a structured text format that specifies who was talking, what they said, and where your annotations should appear. The schema is documented within the tool itself. If you’re not comfortable writing YAML directly, your AI assistant will do this for you if you give it the conversation transcript.

Once you have the YAML file, run a command like this to generate the replay file:

```
npx conversation-replay build conversation.yaml -o output.html
```

This works on any system with [Node.js](https://nodejs.org/) installed. The `npx` command downloads the tool automatically, so no separate installation needed.

Consider where animated replays might improve your training materials. Sometimes showing how a conversation unfolds matters more than summarizing what was said, providing the raw transcript, or using AI to generate a lengthy podcast out of it.

More on

[Communication](/topic/communication)[Tools](/topic/tools)

2 min to read

January 15, 2026

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. As CISO at Axonius, he leads the security and IT program, focusing on trust and growth. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

[Learn more →](/about)

© 2026 Lenny Zeltser