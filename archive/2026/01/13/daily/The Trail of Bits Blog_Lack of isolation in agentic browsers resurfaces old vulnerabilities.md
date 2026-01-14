---
title: Lack of isolation in agentic browsers resurfaces old vulnerabilities
url: https://blog.trailofbits.com/2026/01/13/lack-of-isolation-in-agentic-browsers-resurfaces-old-vulnerabilities/
source: The Trail of Bits Blog
date: 2026-01-13
fetch_date: 2026-01-14T03:34:27.873613
---

# Lack of isolation in agentic browsers resurfaces old vulnerabilities

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Lack of isolation in agentic browsers resurfaces old vulnerabilities

[Lucas Bourtoule](/authors/lucas-bourtoule/)

January 13, 2026

[machine-learning](/categories/machine-learning/), [attacks](/categories/attacks/), [threat-modeling](/categories/threat-modeling/), [exploits](/categories/exploits/)

Page content

* [**Threat model: A deadly combination of tools**](#threat-model-a-deadly-combination-of-tools)
  + [**The trust zones**](#the-trust-zones)
  + [**Trust zone violations**](#trust-zone-violations)
  + [**Combining violations to create exploits**](#combining-violations-to-create-exploits)
* [**Demonstrating real-world attacks**](#demonstrating-real-world-attacks)
  + [**Manipulation attacks: Controlling what the agent believes and says**](#manipulation-attacks-controlling-what-the-agent-believes-and-says)
    - [**False information:** Reflected XSS for AI](#false-information-reflected-xss-for-ai)
    - [**Session confusion through magic links**](#session-confusion-through-magic-links)
  + [**Data exfiltration attacks: Stealing sensitive information**](#data-exfiltration-attacks-stealing-sensitive-information)
    - [**Chat content leak: basic exfiltration**](#chat-content-leak-basic-exfiltration)
    - [**Cross-site data leak:** CSRF for the AI Era](#cross-site-data-leak-csrf-for-the-ai-era)
    - [**Location leak via web search**](#location-leak-via-web-search)
  + [**Persistence attacks: Long-term compromise**](#persistence-attacks-long-term-compromise)
    - [**Same-site data leak:** persistent XSS revisited](#same-site-data-leak-persistent-xss-revisited)
    - [**History pollution**](#history-pollution)
* [**Securing agentic browsers: A path forward**](#securing-agentic-browsers-a-path-forward)
  + [**Short-term mitigations**](#short-term-mitigations)
    - [**Isolate tool browsing contexts**](#isolate-tool-browsing-contexts)
    - [**Split tools into task-based components**](#split-tools-into-task-based-components)
    - [**Provide content review mechanisms**](#provide-content-review-mechanisms)
  + [**Long-term architectural solutions**](#long-term-architectural-solutions)
    - [**Implement an extended same-origin policy for AI agents**](#implement-an-extended-same-origin-policy-for-ai-agents)
    - [**Adopt holistic AI security frameworks**](#adopt-holistic-ai-security-frameworks)
    - [**Decouple content processing from task planning**](#decouple-content-processing-from-task-planning)
* [**What we learned**](#what-we-learned)

With browser-embedded AI agents, we’re essentially starting the security journey over again. We exploited a lack of isolation mechanisms in multiple agentic browsers to perform attacks ranging from the dissemination of false information to cross-site data leaks. These attacks, which are functionally similar to cross-site scripting (XSS) and cross-site request forgery (CSRF), resurface decades-old patterns of vulnerabilities that the web security community spent years building effective defenses against.

The root cause of these vulnerabilities is inadequate isolation. Many users implicitly trust browsers with their most sensitive data, using them to access bank accounts, healthcare portals, and social media. The rapid, bolt-on integration of AI agents into the browser environment gives them the same access to user data and credentials. Without proper isolation, these agents can be exploited to compromise any data or service the user’s browser can reach.

In this post, we outline a generic threat model that identifies four trust zones and four violation classes. We demonstrate real-world exploits, including data exfiltration and session confusion, and we provide both immediate mitigations and long-term architectural solutions. (We do not name specific products as the affected vendors declined coordinated disclosure, and these architectural flaws affect agentic browsers broadly.)

For developers of agentic browsers, our key recommendation is to extend the Same-Origin Policy to AI agents, building on proven principles that successfully secured the web.

## **Threat model: A deadly combination of tools**

To understand why agentic browsers are vulnerable, we need to identify the trust zones involved and what happens when data flows between them without adequate controls.

### **The trust zones**

In a typical agentic browser, we identify four primary trust zones:

1. **Chat context:** The agent’s client-side components, including the agentic loop, conversation history, and local state (where the AI agent “thinks” and maintains context).
2. **Third-party servers:** The agent’s server-side components, primarily the LLM itself when provided as an API by a third party. User data sent here leaves the user’s control entirely.
3. **Browsing origins:** Each website the user interacts with represents a separate trust zone containing independent private user data. Traditional browser security (the Same-Origin Policy) should keep these strictly isolated.
4. **External network:** The broader internet, including attacker-controlled websites, malicious documents, and other untrusted sources.

This simplified model captures the essential security boundaries present in most agentic browser implementations.

### **Trust zone violations**

Typical agentic browser implementations make various tools available to the agent: fetching web pages, reading files, accessing history, making HTTP requests, and interacting with the Document Object Model (DOM). From a threat modeling perspective, each tool creates data transfers between trust zones. Due to inadequate controls or incorrect assumptions, this often results in unwanted or unexpected data paths.

We’ve distilled these data paths into four classes of trust zone violations, which serve as primitives for constructing more sophisticated attacks:

**INJECTION:** Adding arbitrary data to the chat context through an untrusted vector. It’s well known that LLMs cannot distinguish between data and instructions; this fundamental limitation is what enables prompt injection attacks. Any tool that adds arbitrary data to the chat history is a prompt injection vector; this includes tools that fetch webpages or attach untrusted files, such as PDFs. Data flows from the **external network** into the **chat context**, crossing the system’s external security boundary.

**CTX\_IN (context in):** Adding sensitive data to the chat context from browsing origins. Examples include tools that retrieve personal data from online services or that include excerpts of the user’s browsing history. When the AI model is owned by a third party, this data flows from **browsing origins** through the **chat context** and ultimately to **third-party servers**.

**REV\_CTX\_IN (reverse context in):** Updating browsing origins using data from the chat context. This includes tools that log a user in or update their browsing history. The data crosses the same security boundary as CTX\_IN, but in the opposite direction: from the **chat context** back into **browsing origins**.

**CTX\_OUT (context out):** Using data from the chat context in external requests. Any tool that can make HTTP requests falls into this category, as side channels always exist. Even indirect requests pose risks, so tools that interact with webpages or manipulate the DOM should also be included. This represents data flowing from the **chat context** to the **external network**, where attackers can observe it.

### **Combining violations to create exploits**

Individual trust zone violations are concerning, but the real danger emerges when they’re combined. INJECTION alone can implant false information in the chat history without the user noticing, potentially influencing decisions. The combination of INJECTION and CTX\_OUT leaks data from the chat history to attacker-controlled servers. While chat data is not nec...