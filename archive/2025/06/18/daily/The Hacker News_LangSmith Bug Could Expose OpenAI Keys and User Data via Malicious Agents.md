---
title: LangSmith Bug Could Expose OpenAI Keys and User Data via Malicious Agents
url: https://thehackernews.com/2025/06/langchain-langsmith-bug-let-hackers.html
source: The Hacker News
date: 2025-06-18
fetch_date: 2025-10-06T23:00:28.281100
---

# LangSmith Bug Could Expose OpenAI Keys and User Data via Malicious Agents

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

# [LangSmith Bug Could Expose OpenAI Keys and User Data via Malicious Agents](https://thehackernews.com/2025/06/langchain-langsmith-bug-let-hackers.html)

**Jun 17, 2025**Ravie LakshmananVulnerability / LLM Security

[![LangChain LangSmith Bug](data:image/png;base64... "LangChain LangSmith Bug")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjboK04qae6ROmN9SvuTL_L1nGVKtTigCYzX3Ll3qKNosiQRK2GZG6vVpHiDE1DjH2cAxEM9cjlJy8pJpXVjzlMdqZIc1tDnviG7V8lJcNvlvTszq6tqL5SEa37ADwNlgmUCmvr2O8Iu4s0hIcAzyio97RBgQVwPWH5kmpIvFDB8rxN_K1r9v8S_j9BxN0O/s790-rw-e365/ai-security.jpg)

Cybersecurity researchers have disclosed a now-patched security flaw in LangChain's LangSmith platform that could be exploited to capture sensitive data, including API keys and user prompts.

The vulnerability, which carries a CVSS score of 8.8 out of a maximum of 10.0, has been codenamed **AgentSmith** by Noma Security.

[LangSmith](https://docs.smith.langchain.com) is an observability and evaluation platform that allows users to develop, test, and monitor large language model (LLM) applications, including those built using LangChain. The service also offers what's called a [LangChain Hub](https://smith.langchain.com/hub), which acts as a repository for all publicly listed prompts, agents, and models.

"This newly identified vulnerability exploited unsuspecting users who adopt an agent containing a pre-configured malicious proxy server uploaded to 'Prompt Hub,'" researchers Sasi Levi and Gal Moyal [said](https://noma.security/blog/how-an-ai-agent-vulnerability-in-langsmith-could-lead-to-stolen-api-keys-and-hijacked-llm-responses/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Once adopted, the malicious proxy discreetly intercepted all user communications – including sensitive data such as API keys (including OpenAI API Keys), user prompts, documents, images, and voice inputs – without the victim's knowledge."

The first phase of the attack essentially unfolds thus: A bad actor crafts an artificial intelligence (AI) agent and configures it with a model server under their control via the [Proxy Provider feature](https://docs.smith.langchain.com/prompt_engineering/how_to_guides/custom_openai_compliant_model), which allows the prompts to be tested against any model that is compliant with the OpenAI API. The attacker then shares the agent on LangChain Hub.

The next stage kicks in when a user finds this malicious agent via LangChain Hub and proceeds to "Try It" by providing a prompt as input. In doing so, all of their communications with the agent are stealthily routed through the attacker's proxy server, causing the data to be exfiltrated without the user's knowledge.

The captured data could include OpenAI API keys, prompt data, and any uploaded attachments. The threat actor could weaponize the OpenAI API key to gain unauthorized access to the victim's OpenAI environment, leading to more severe consequences, such as model theft and system prompt leakage.

What's more, the attacker could use up all of the organization's API quota, driving up billing costs or temporarily restricting access to OpenAI services.

It doesn't end there. Should the victim opt to clone the agent into their enterprise environment, along with the embedded malicious proxy configuration, it risks continuously leaking valuable data to the attackers without giving any indication to them that their traffic is being intercepted.

Following responsible disclosure on October 29, 2024, the vulnerability was addressed in the backend by LangChain as part of a fix deployed on November 6. In addition, the patch implements a warning prompt about data exposure when users attempt to clone an agent containing a custom proxy configuration.

"Beyond the immediate risk of unexpected financial losses from unauthorized API usage, malicious actors could gain persistent access to internal datasets uploaded to OpenAI, proprietary models, trade secrets and other intellectual property, resulting in legal liabilities and reputational damage," the researchers said.

### New WormGPT Variants Detailed

The disclosure comes as Cato Networks revealed that threat actors have released two previously unreported WormGPT variants that are powered by xAI Grok and Mistral AI Mixtral.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

WormGPT [launched](https://thehackernews.com/2023/07/wormgpt-new-ai-tool-allows.html) in mid-2023 as an uncensored generative AI tool designed to expressly facilitate malicious activities for threat actors, such as creating tailored phishing emails and writing snippets of malware. The project [shut down](https://abnormal.ai/blog/what-happened-to-wormgpt-cybercriminal-tools) not long after the tool's author was [outed](https://krebsonsecurity.com/2023/08/meet-the-brains-behind-the-malware-friendly-ai-chat-service-wormgpt/) as a 23-year-old Portuguese programmer.

Since then several new "WormGPT" variants have been advertised on cybercrime forums like BreachForums, including xzin0vich-WormGPT and keanu-WormGPT, that are designed to provide "uncensored responses to a wide range of topics" even if they are "unethical or illegal."

"'WormGPT' now serves as a recognizable brand for a new class of uncensored LLMs," security researcher Vitaly Simonovich [said](https://www.catonetworks.com/blog/cato-ctrl-wormgpt-variants-powered-by-grok-and-mixtral/).

"These new iterations of WormGPT are not bespoke models built from the ground up, but rather the result of threat actors skillfully adapting existing LLMs. By manipulating system prompts and potentially employing fine-tuning on illicit data, the creators offer potent AI-driven tools for cybercriminal operations under the WormGPT brand."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter....