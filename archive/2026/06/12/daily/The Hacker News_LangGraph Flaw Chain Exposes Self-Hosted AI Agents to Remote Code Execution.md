---
title: LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution
url: https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html
source: The Hacker News
date: 2026-06-12
fetch_date: 2026-06-13T06:12:07.891191
---

# LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution](https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html)

**Ravie Lakshmanan**Jun 12, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifnUd6CRFC-YdhoEDgmNoLtKUYjbZvqQJOETqK59Zd5Pk_epd9uGMfPCrujB3grOrajNxMls_p7TWQwnyCxFo1Ou8MM70yUh3dP04776sp-xk3O8544Z9YD-v_konqCTv1eX_42iMBkr4j5c-h0_I5dyBWvrr_3jrphGH3xLcZgaDAN1uH8OA5rWerJE5B/s1700-e365/langgraph.jpg)

Cybersecurity researchers have disclosed details of three now-patched security flaws impacting [LangGraph](https://www.langchain.com/langgraph), including a critical vulnerability chain that could result in remote code execution.

LangGraph is an open-source framework created by LangChain to build complex, stateful, and multi-agent artificial intelligence (AI) agentic applications.

"An SQL injection in LangGraph's function could allow attackers to gain full control via remote code execution of a server by exploiting weaknesses in how the system processes and handles data," Check Point [said](https://blog.checkpoint.com/research/when-your-ai-agents-memory-becomes-a-security-liability/).

The list of identified vulnerabilities is as follows -

* **[CVE-2025-67644](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-9rwj-6rc7-p77c)** (CVSS score: 7.3) - A SQL injection vulnerability exists in LangGraph's SQLite checkpoint implementation that allows attackers to manipulate SQL queries through metadata filter keys. (Affects langgraph-checkpoint-sqlite versions before 3.0.1)
* **[CVE-2026-28277](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-g48c-2wqr-h844)** (CVSS score: 6.8) - An unsafe [msgpack](https://msgpack.org/index.html) deserialization vulnerability in LangGraph that could be used to trigger object reconstruction when a checkpoint is loaded by an attacker who can modify checkpoint data. (Affects langgraph versions before 1.0.10)
* **[CVE-2026-27022](https://github.com/langchain-ai/langgraphjs/security/advisories/GHSA-5mx2-w598-339m)** (CVSS score: 6.5) - A RediSearch Query Injection in @langchain/langgraph-checkpoint-redis that can be used to bypass access controls. (Affects @langchain/langgraph-checkpoint-redis versions before 1.0.1)

"The vulnerability chain is exploitable in self-hosted deployments using the SQLite or Redis checkpointer with user-controlled filter input," Check Point said. "LangChain's managed platform (LangSmith Deployment), is not affected."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Security researcher Yarden Porat, who is credited with discovering and reporting all three flaws, [said](https://research.checkpoint.com/2026/from-sqli-to-rce-exploiting-langgraphs-checkpointer/) CVE-2025-67644 and CVE-2026-28277 could be chained to achieve remote code execution.

Specifically, the attack chain hinges on the application exposing the [get\_state\_history()](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/get_state_history) endpoint, which then allows an attacker to retrieve historical checkpoints based on their metadata. It requires the following steps -

* The attacker prepares a msgpack payload containing instructions to execute arbitrary code.
* The attacker sends a malicious filter parameter that exploits the SQL injection vulnerability to return a fake checkpoint row to the database query results, where the checkpoint column contains attacker-controlled serialized data.
* When the application processes the query results, it deserializes the malicious checkpoint's BLOB.
* The attacker exploits the unsafe deserialization vulnerability to execute the attacker's payload, giving them remote code execution on the server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV-YjfyONNV77yQ5KwfXDgnEWA0TadqpAvsJvAS7wexd3CK9UVe3n44HrRYJl6CgsIV_diJc1ZLFSPJ7AJu8RCXVsy-xgKYx4XR8lcXQh6qF-Wqnhr5L9rImOGP0iefsoYnDXhyphenhyphenUEIYbX-Ce7c_lyGNCbnMNloiz4b-54Na_LtY0OhTJXfmDvPgJhFTEiU/s1700-e365/sql.jpg)

LangGraph has described CVE-2026-28277 as a post-exploitation issue, where successful exploitation requires the ability to write attacker-controlled checkpoint data and turn that into code execution in the application runtime, and it does not pose any risks to existing LangSmith-hosted deployments.

In such a scenario, this escalation from write access to checkpoint store" to code execution may "expose runtime secrets or provide access to other systems the runtime can reach," LangGraph maintainers said. "The described threat model requires an attacker to tamper with the checkpoint persistence layer used by the deployment; typical hosted configurations are designed to prevent such access."

Check Point said the findings illustrate how classic vulnerability classes like SQL injection can become more potent when they manifest inside AI agent frameworks that carry elevated access and trust, thereby opening the door to sensitive data exposure.

Users are advised to apply the latest fixes, implement authentication for self-hosted LangGraph servers, avoid long-lived static secrets, enforce network segmentation, treat AI agents as privileged identities, and apply the principle of least privilege (PoLP) to limit the agent's access footprint.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[*...