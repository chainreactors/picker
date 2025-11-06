---
title: Anthropic Changes MCP Calls Into Filesystem-based Skills
url: https://danielmiessler.com/blog/anthropic-downplays-mcps?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2025-11-05
fetch_date: 2025-11-06T03:16:11.538837
---

# Anthropic Changes MCP Calls Into Filesystem-based Skills

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Anthropic Changes MCP Calls Into Filesystem-based Skills

They're recommending a filesystem and code-based structure for calling tools instead of using MCPs each time

[#ai](/archives/?tag=ai) [#anthropic](/archives/?tag=anthropic) [#mcp](/archives/?tag=mcp) [#development](/archives/?tag=development)

Anthropic just came out with [a new article about code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) which is pretty extraordinary.

Pontificating...

It's nuanced, but it sure *seems* like they just threw massive shade at MCPs, and basically deprecated them down to being like service directories.

Look at the subtitle of their post:

> Direct tool calls consume context for each definition and result. Agents scale better by writing code to call tools instead. Anthropic Engineering

*Dayum.*

They go on to throw more rocks.

> Every intermediate result must pass through the model. In this example, the full call transcript flows through twice. For a 2-hour sales meeting, that could mean processing an additional 50,000 tokens. Even larger documents may exceed context window limits, breaking the workflow. With large documents or complex data structures, models may be more likely to make mistakes when copying data between tool calls. Anthropic Engineering

Then they say you can do something like this instead:

> With code execution environments becoming more common for agents, a solution is to present MCP servers as code APIs rather than direct tool calls. The agent can then write code to interact with MCP servers. This approach addresses both challenges: agents can load only the tools they need and process data in the execution environment before passing results back to the model. Anthropic Engineering

To me this is treating the MCP like a directory of things you can call, and then having your agents write your own code for calling them.

In other words, *not* calling them anymore using the MCP itself.

They give an example of turning each tool that comes back from the MCP into a Typescript tool-calling file that agents can use to invoke that particular tool *in code*. And they specifically mention the advantage of agents being able to do things with those results or whatever, using just code, that doesn't involve AI calls.

Look at the advantage they say this gives:

> The agent discovers tools by exploring the filesystem: listing the ./servers/ directory to find available servers (like google-drive and salesforce), then reading the specific tool files it needs (like getDocument.ts and updateRecord.ts) to understand each tool's interface. This lets the agent load only the definitions it needs for the current task. This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%.Anthropic, from the same article

I'm so in love with this. It's more filesystem-based structure, which I'm already all-in on for my context management. Now tool-calling is becoming file-system based too.

So they're heading in a direction I was already heading anyway, which is to just write direct API calls, but they're doing doing it in a much cooler way with these compostable files that can be shared.

That depends on the server-side not changing, of course.

*I think they might have just turned MCP tool calls into Skills.*

I guess in this world MCPs are still powerful, but more as a directory of what's possible, and what gets done manually/directly as opposed to the mechanism for actually doing it.

Unbelievably cool.

I'm so very much migrating immediately.

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills "Share on LinkedIn") [HN Hacker News](https://ul.live/share/hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills "Share on Hacker News")  [Reddit](https://ul.live/share/reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills "Share on Reddit")  [Facebook](https://ul.live/share/facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills "Share on Facebook")  [Forward](https://ul.live/share/email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fanthropic-downplays-mcps&title=Anthropic%20Changes%20MCP%20Calls%20Into%20Filesystem-based%20Skills)

Search

This post was tagged with:

aianthropicmcpdevelopment

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2025 Daniel Miessler. All rights reserved.