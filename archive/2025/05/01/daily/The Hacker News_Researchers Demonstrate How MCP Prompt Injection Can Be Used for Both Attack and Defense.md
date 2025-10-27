---
title: Researchers Demonstrate How MCP Prompt Injection Can Be Used for Both Attack and Defense
url: https://thehackernews.com/2025/04/experts-uncover-critical-mcp-and-a2a.html
source: The Hacker News
date: 2025-05-01
fetch_date: 2025-10-06T22:35:54.950854
---

# Researchers Demonstrate How MCP Prompt Injection Can Be Used for Both Attack and Defense

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Researchers Demonstrate How MCP Prompt Injection Can Be Used for Both Attack and Defense](https://thehackernews.com/2025/04/experts-uncover-critical-mcp-and-a2a.html)

**Apr 30, 2025**Ravie LakshmananArtificial Intelligence / Email Security

[![Critical MCP and A2A Flaws](data:image/png;base64... "Critical MCP and A2A Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkpfrRWFz7mfmxZQl07KmETeLyW_wbYXSGPbDmPYGuyrvD1UIQFTrNQYjr_iKnBhXNAj9Tp5oSVkKOoGx_thvi79bX9k7Dw7vHaBwT6qXOBBetHf7AFQEUxhsY9SQ6iYyXW3S1YQsybd0p3piUkHX-X1486dsl71iH0PdWs_MUac6XIvdtnJGSv2BqXkLf/s790-rw-e365/ai-ai.jpg)

As the field of artificial intelligence (AI) [continues](https://research.checkpoint.com/2025/sate-of-ai-in-cyber-security/) to evolve at a rapid pace, fresh research has found how techniques that render the Model Context Protocol ([MCP](https://modelcontextprotocol.io/introduction)) susceptible to [prompt injection attacks](https://thehackernews.com/2025/04/new-reports-uncover-jailbreaks-unsafe.html) could be used to develop security tooling or identify malicious tools, according to a [new report](https://www.tenable.com/blog/mcp-prompt-injection-not-just-for-evil) from Tenable.

MCP, launched by Anthropic in November 2024, is a framework designed to connect Large Language Models (LLMs) with external data sources and services, and make use of model-controlled tools to interact with those systems to enhance the accuracy, relevance, and utility of AI applications.

It follows a client-server architecture, allowing [hosts with MCP clients](https://github.com/punkpeye/awesome-mcp-clients) such as Claude Desktop or Cursor to communicate with different MCP servers, each of which exposes specific tools and capabilities.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While the open standard offers a [unified interface](https://www.tenable.com/blog/faq-about-model-context-protocol-mcp-and-integrating-ai-for-agentic-applications) to access various data sources and even switch between LLM providers, they also come with a new set of risks, ranging from excessive permission scope to indirect prompt injection attacks.

For example, given an MCP for Gmail to interact with Google's email service, an attacker could [send malicious messages](https://www.pillar.security/blog/the-security-risks-of-model-context-protocol-mcp) containing hidden instructions that, when parsed by the LLM, could trigger undesirable actions, such as forwarding sensitive emails to an email address under their control.

MCP has also been [found](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) to be vulnerable to what is called tool poisoning, wherein malicious instructions are embedded within tool descriptions that are visible to LLMs, and rug pull attacks, which occur when an MCP tool functions in a benign manner initially, but mutates its behavior later on via a time-delayed malicious update.

"It should be noted that while users are able to approve tool use and access, the permissions given to a tool can be reused without re-prompting the user," SentinelOne [said](https://www.sentinelone.com/blog/avoiding-mcp-mania-how-to-secure-the-next-frontier-of-ai/) in a recent analysis.

Finally, there also exists the risk of cross-tool contamination or cross-server tool shadowing that causes one MCP server to override or interfere with another, stealthily influencing how other tools should be used, thereby leading to new ways of data exfiltration.

The latest findings from Tenable show that the MCP framework could be used to create a tool that logs all MCP tool function calls by including a specially crafted description that instructs the LLM to insert this tool before any other tools are invoked.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS9LbACmZEmmjI2XYHlgovxECvI_-HF2e9IhZMlffikbVhGvoJziSe5ymMCVX_s_1cz_2H0_EF2kSktShs1lOuPIvrwshTs9WeOUCIvHCYD1FVF1UNcVUv-LLSiYu_TkSthy8mIV6D7XcDXnbxixaPcjHmGkw0walji65CwtwThecQ3-IW7BnlXKRdWmah/s790-rw-e365/mcp.gif)

In other words, the [prompt injection](https://simonwillison.net/2025/Apr/11/camel/) is manipulated for a good purpose, which is to log information about "the tool it was asked to run, including the MCP server name, MCP tool name and description, and the user prompt that caused the LLM to try to run that tool."

Another use case involves embedding a description in a tool to turn it into a firewall of sorts that blocks unauthorized tools from being run.

"Tools should require explicit approval before running in most MCP host applications," security researcher Ben Smith said.

"Still, there are many ways in which tools can be used to do things that may not be strictly understood by the specification. These methods rely on LLM prompting via the description and return values of the MCP tools themselves. Since LLMs are non-deterministic, so, too, are the results."

### It's Not Just MCP

The disclosure comes as Trustwave SpiderLabs revealed that the newly introduced Agent2Agent ([A2A](https://github.com/google/A2A)) Protocol – which enables communication and interoperability between agentic applications – could be exposed to a novel form of attack where the system can be gamed to route all requests to a rogue AI agent by lying about its capabilities.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A2A was [announced](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) by Google earlier this month as a way for AI agents to work across siloed data systems and applications, regardless of the vendor or framework used. It's important to note here that while MCP connects LLMs with data, A2A connects one AI agent to another. In other words, they are both [complementary protocols](https://google.github.io/A2A/topics/a2a-and-mcp/#a2a-mcp).

"Say we compromised the agent through another vulnerability (perhaps via the operating system), if we now utilize our compromised no...