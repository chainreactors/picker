---
title: AI Injection Attacks
url: https://textslashplain.com/2025/09/05/ai-injection-attacks/
source: text/plain
date: 2025-09-06
fetch_date: 2025-10-02T19:44:45.679320
---

# AI Injection Attacks

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# AI Injection Attacks

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-09-052025-09-19](https://textslashplain.com/2025/09/05/ai-injection-attacks/)Posted in[design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[AI](https://textslashplain.com/tag/ai/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

A hot infosec topic these days is “*How can we prevent abuse of AI agents?*”

While AI introduces [awesome new capabilities](https://textslashplain.com/2025/04/15/vibe-coding-for-security/), it also entails an enormous set of risks from the obvious and mundane to the esoteric and elaborate.

As a browser security person, I’m most often asked about [indirect prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) attacks, whereby a client’s AI (e.g. in-browser or on device) is tasked with interacting with content from the Internet. The threat here is that the AI Agent might mistakenly treat the web content it interacts with as instructions from the Agent’s user, and so hypnotized, fall under the control of the author of that web content. Malicious web content could then direct the Agent (now [a confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem)) to undertake unsafe actions like sharing private data about the user, performing transactions using that user’s wallet, etc.

### Nothing New Under the Sun

Injection attacks can be found all over the cybersecurity landscape.

The most obvious example is found in **memory safety vulnerabilities**, whereby an attacker overflows a content data buffer and that data is incorrectly treated as code. That vulnerability roots back to a fundamental design choice in common computing architectures: the “[Von Neumann Architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture),” whereby code and data are comingled in the memory of the system. While convenient for many reasons, it gave rise to an entire class of attacks that would’ve been prevented by the “[Harvard Architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture)” whereby the data and instructions would be plainly *distinct*. One of the major developments of 20 years ago– Data Execution Prevention / No eXecute (DEP/NX) was a processor feature that would more clearly delineate data and code in an attempt to prevent this mistake. And the [list of “alphabet soup” mitigations](https://textslashplain.com/2025/04/01/defensive-technology-exploit-protection/) has only grown over the years.

Injection attacks go far beyond low-level CPU architecture and are found all over, including in the Web Platform, which adopted a Von Neumann-style design in which the static text of web pages is comingled with inline scripting code, giving rise to the ever-present threat of [**Cross-Site Scripting**](https://textslashplain.com/tag/xss/). And here again, we ended up with protection features like the XSS Filter (IE), XSS Auditor (Chrome) and opt-in features to put the genie back in the bottle (e.g. [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)) by preventing content and script from mingling in dangerous ways.

I’ll confess that I don’t understand nearly enough about how LLM AIs operate to understand whether the “Harvard Architecture” is even *possible* for an LLM, but from the questions I’m getting, it clearly is not the common architecture.

### What Can Be Done?

In a world where AI is subject to injection attacks, what can we do about it?

One approach would be to ensure that the Agent cannot load “unsafe” web content. Since I work on [SmartScreen](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/), a reputation service for blocking access to known-unsafe sites, I’m often asked whether we could just block Agent from accessing bad sites just as we would for a regular human browser user. And yes, we should and do, but this is wildly insufficient: SmartScreen blocks sites found to be phishing, distributing malware, or conducting tech scams, but the [set of bad sites grows by the second](https://textslashplain.com/2023/10/13/beware-urls-are-pointers-to-mutable-entities/), and it’s very unlikely that a site conducting a prompt injection attack would even be recognized today.

If blocking bad sites doesn’t work, maybe we could allow only “known good” sites? This too is problematic. There’s no concept of a “trustworthy sites list” per-se. The closest SmartScreen has is a “Top traffic” list, but that just reflects a list of high-traffic sites that are considered to be *unlikely* sources of the specific types of malicious threats SmartScreen addresses (e.g. phishing, malware, tech scams). And it’s worse than that — many “known good” sites **contain untrusted content** like user-generated comments/posts, ads, snippets of text from other websites, etc. A “known good” site that allows untrusted 3rd-party content would represent a potential source of a prompt injection attack.

Finally, another risk-limiting design might be to **limit the Agent’s capabilities**, either **requiring constant approval** from a supervising human, or by **employing heavy sandboxing** whereby the Agent operates from an isolated VM that does not have access to any user-information or [ambient authority](https://textslashplain.com/2024/04/10/browser-security-bugs-that-arent-javascript-in-pdf/#:~:text=PDFs%20get%20any-,ambient%20authority,-based%20upon%20the). So neutered, a hypnotised Agent could not cause much damage.

Unfortunately, any Agent that’s running in a sandbox doesn’t have access to resources (e.g. the user’s data or credentials) that are critical for achieving compelling scenarios (“*Book a table for two at a nice restaurant, order flowers, and email an calendar reminder to my wife*“), such that a sandboxed Agent may be much less compelling to an everyday human.

### Aside: Game Theory

Despite the many security risks introduced by Agentic AI, product teams are racing ahead to integrate more and more capable Agent functionality into their products, (including [completing purchase transactions](https://guard.io/labs/scamlexity-we-put-agentic-ai-browsers-to-the-test-they-clicked-they-paid-they-failed)).

AI companies are racing toward ever-more-empowered Agents because everyone is scared that one of the other AI companies is gonna come out with some less cautious product and that more powerful, less restricted product is gonna win the market. So we end up in the situation with the US at the end of the 1950s, whereby the Russians had 4 working ICBMs but the United States had convinced ourselves they had 1000. In response to this fear, the US itself built a thousand ICBMs, so the Russians then built a thousand ICBMs, and so on, until we both basically bankrupted the world over the next few decades.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2025/09/05/ai-injection-attacks/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2025/09/05/ai-injection-attacks/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-09-052025-09-19](https://textslashplain.com/2025/09/05/ai-injection-attacks/)Posted in[design](https://textslashplain.com/category/design/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[AI](https://textslashplain.com/tag/ai/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & ...