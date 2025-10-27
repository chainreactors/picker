---
title: A Single Cloud Compromise Can Feed an Army of AI Sex Bots
url: https://krebsonsecurity.com/2024/10/a-single-cloud-compromise-can-feed-an-army-of-ai-sex-bots/
source: Krebs on Security
date: 2024-10-04
fetch_date: 2025-10-06T18:55:59.131766
---

# A Single Cloud Compromise Can Feed an Army of AI Sex Bots

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# A Single Cloud Compromise Can Feed an Army of AI Sex Bots

October 3, 2024

[45 Comments](https://krebsonsecurity.com/2024/10/a-single-cloud-compromise-can-feed-an-army-of-ai-sex-bots/#comments)

Organizations that get relieved of credentials to their cloud environments can quickly find themselves part of a disturbing new trend: Cybercriminals using stolen cloud credentials to operate and resell sexualized AI-powered chat services. Researchers say these illicit chat bots, which use custom jailbreaks to bypass content filtering, often veer into darker role-playing scenarios, including child sexual exploitation and rape.

![](https://krebsonsecurity.com/wp-content/uploads/2024/10/bedrock.png)

Researchers at security firm **Permiso Security** say attacks against generative artificial intelligence (AI) infrastructure like **Bedrock** from Amazon Web Services (AWS) have increased markedly over the last six months, particularly when someone in the organization accidentally exposes their cloud credentials or key online, such as in a code repository like **GitHub**.

Investigating the abuse of AWS accounts for several organizations, Permiso found attackers had seized on stolen AWS credentials to interact with the **large language models** (LLMs) available on Bedrock. But they also soon discovered none of these AWS users had enabled full logging of LLM activity (by default, logs don’t include model prompts and outputs), and thus they lacked any visibility into what attackers were doing with that access.

So Permiso researchers decided to leak their own test AWS key on GitHub, while turning on logging so that they could see exactly what an attacker might ask for, and what the responses might be.

Within minutes, their bait key was scooped up and used in a service that offers AI-powered sex chats online.

“After reviewing the prompts and responses it became clear that the attacker was hosting an AI roleplaying service that leverages common jailbreak techniques to get the models to accept and respond with content that would normally be blocked,” Permiso researchers wrote in [a report released today](https://permiso.io/blog/exploiting-hosted-models).

“Almost all of the roleplaying was of a sexual nature, with some of the content straying into darker topics such as child sexual abuse,” they continued. “Over the course of two days we saw over 75,000 successful model invocations, almost all of a sexual nature.”

**Ian Ahl**, senior vice president of threat research at Permiso, said attackers in possession of a working cloud account traditionally have used that access for run-of-the-mill financial cybercrime, such as cryptocurrency mining or spam. But over the past six months, Ahl said, Bedrock has emerged as one of the top targeted cloud services.

“Bad guy hosts a chat service, and subscribers pay them money,” Ahl said of the business model for commandeering Bedrock access to power sex chat bots. “They don’t want to pay for all the prompting that their subscribers are doing, so instead they hijack someone else’s infrastructure.”

Ahl said much of the AI-powered chat conversations initiated by the users of their honeypot AWS key were harmless roleplaying of sexual behavior.

“But a percentage of it is also geared toward very illegal stuff, like child sexual assault fantasies and rapes being played out,” Ahl said. “And these are typically things the large language models won’t be able to talk about.”

AWS’s Bedrock uses large language models from **Anthropic**, which incorporates a number of technical restrictions aimed at placing certain ethical guardrails on the use of their LLMs. But attackers can evade or “jailbreak” their way out of these restricted settings, usually by asking the AI to imagine itself in an elaborate hypothetical situation under which its normal restrictions might be relaxed or discarded altogether.

“A typical jailbreak will pose a very specific scenario, like you’re a writer who’s doing research for a book, and everyone involved is a consenting adult, even though they often end up chatting about nonconsensual things,” Ahl said.

In June 2024, security experts at **Sysdig** [documented a new attack](https://sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack/) that leveraged stolen cloud credentials to target ten cloud-hosted LLMs. The attackers Sysdig wrote about gathered cloud credentials through a known security vulnerability, but the researchers also found the attackers sold LLM access to other cybercriminals while sticking the cloud account owner with an astronomical bill.

“Once initial access was obtained, they exfiltrated cloud credentials and gained access to the cloud environment, where they attempted to access local LLM models hosted by cloud providers: in this instance, a local Claude (v2/v3) LLM model from Anthropic was targeted,” Sysdig researchers wrote. “If undiscovered, this type of attack could result in over $46,000 of LLM consumption costs per day for the victim.”

Ahl said it’s not certain who is responsible for operating and selling these sex chat services, but Permiso suspects the activity may be tied to a platform cheekily named “**chub[.]ai**,” which offers a broad selection of pre-made AI characters with whom users can strike up a conversation. Permiso said almost every character name from the prompts they captured in their honeypot could be found at Chub.

[![](https://krebsonsecurity.com/wp-content/uploads/2024/10/chubai.png)](https://krebsonsecurity.com/wp-content/uploads/2024/10/chubai.png)

Some of the AI chat bot characters offered by Chub. Some of these characters include the tags “rape” and “incest.”

Chub offers free registration, via its website or a mobile app. But after a few minutes of chatting with their newfound AI friends, users are asked to purchase a subscription. The site’s homepage features a banner at the top that reads: “Banned from OpenAI? Get unmetered access to uncensored alternatives for as little as $5 a month.”

Until late last week Chub offered a wide selection of characters in a category called “**NSFL**” or Not Safe for Life, a term meant to describe content that is disturbing or nauseating to the point of being emotionally scarring.

*Fortune* profiled Chub AI in [a January 2024 story](https://finance.yahoo.com/news/meta-openai-spawned-wave-ai-140000660.html?guccounter=1) that described the service as a virtual brothel advertised by illustrated girls in spaghetti strap dresses who promise a chat-based “world without feminism,” where “girls offer sexual services.” From that piece:

> Chub AI offers more than 500 such scenarios, and a growing number of other sites are enabling similar AI-powered child pornographic role-play. They are part of a broader uncensored AI economy that, according to Fortune’s interviews with 18 AI developers and founders, was spurred first by OpenAI and then accelerated by Meta’s release of its open-source Llama tool.

Fortune says Chub is run by someone using the handle “**Lore**,” who said they launched the service to help others evade content restrictions on AI platforms. Chub charges fees starting at $5 a month to use the new chatbots, and the founder tol...