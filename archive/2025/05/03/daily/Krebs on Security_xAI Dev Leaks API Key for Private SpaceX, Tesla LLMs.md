---
title: xAI Dev Leaks API Key for Private SpaceX, Tesla LLMs
url: https://krebsonsecurity.com/2025/05/xai-dev-leaks-api-key-for-private-spacex-tesla-llms/
source: Krebs on Security
date: 2025-05-03
fetch_date: 2025-10-06T22:34:13.703349
---

# xAI Dev Leaks API Key for Private SpaceX, Tesla LLMs

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-knowbe4/41.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# xAI Dev Leaks API Key for Private SpaceX, Tesla LLMs

May 1, 2025

[36 Comments](https://krebsonsecurity.com/2025/05/xai-dev-leaks-api-key-for-private-spacex-tesla-llms/#comments)

An employee at Elon Musk’s artificial intelligence company **xAI** leaked a private key on **GitHub** that for the past two months could have allowed anyone to query private xAI large language models (LLMs) which appear to have been custom made for working with internal data from Musk’s companies, including **SpaceX**, **Tesla** and **Twitter/X,** KrebsOnSecurity has learned.

![](https://krebsonsecurity.com/wp-content/uploads/2025/05/x-ai.png)

**Philippe Caturegli**, “chief hacking officer” at the security consultancy **Seralys**, was [the first to publicize the leak](https://www.linkedin.com/posts/caturegli_yo-xai-your-devs-are-leaking-api-keys-on-activity-7321566948020953088-6KXj?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAliaMB3BQO-WOS-eUh-XU4HAd5h8pTzkI) of credentials for an x.ai application programming interface (API) exposed in the GitHub code repository of a technical staff member at xAI.

Caturegli’s post on LinkedIn caught the attention of researchers at **GitGuardian**, a company that specializes in detecting and remediating exposed secrets in public and proprietary environments. GitGuardian’s systems constantly scan GitHub and other code repositories for exposed API keys, and fire off automated alerts to affected users.

GitGuardian’s **Eric Fourrier** told KrebsOnSecurity the exposed API key had access to several unreleased models of **Grok**, the AI chatbot developed by xAI. In total, GitGuardian found the key had access to at least 60 fine-tuned and private LLMs.

“The credentials can be used to access the X.ai API with the identity of the user,” GitGuardian wrote in an email explaining their findings to xAI. “The associated account not only has access to public Grok models (grok-2-1212, etc) but also to what appears to be unreleased (grok-2.5V), development (research-grok-2p5v-1018), and private models (tweet-rejector, grok-spacex-2024-11-04).”

Fourrier found GitGuardian had alerted the xAI employee about the exposed API key nearly two months ago — on March 2. But as of April 30, when GitGuardian directly alerted xAI’s security team to the exposure, the key was still valid and usable. xAI told GitGuardian to report the matter through its bug bounty program at **HackerOne**, but just a few hours later the repository containing the API key was removed from GitHub.

“It looks like some of these internal LLMs were fine-tuned on SpaceX data, and some were fine-tuned with Tesla data,” Fourrier said. “I definitely don’t think a Grok model that’s fine-tuned on SpaceX data is intended to be exposed publicly.”

xAI did not respond to a request for comment. Nor did the 28-year-old xAI technical staff member whose key was exposed.

**Carole Winqwist**, chief marketing officer at GitGuardian, said giving potentially hostile users free access to private LLMs is a recipe for disaster.

“If you’re an attacker and you have direct access to the model and the back end interface for things like Grok, it’s definitely something you can use for further attacking,” she said. “An attacker could it use for prompt injection, to tweak the (LLM) model to serve their purposes, or try to implant code into the supply chain.”

The inadvertent exposure of internal LLMs for xAI comes as Musk’s so-called **Department of Government Efficiency** (DOGE) has been feeding sensitive government records into artificial intelligence tools. In February, **The Washington Post** [reported](https://www.washingtonpost.com/nation/2025/02/06/elon-musk-doge-ai-department-education/) DOGE officials were feeding data from across the Education Department into AI tools to probe the agency’s programs and spending.

The Post said DOGE plans to replicate this process across many departments and agencies, accessing the back-end software at different parts of the government and then using AI technology to extract and sift through information about spending on employees and programs.

“Feeding sensitive data into AI software puts it into the possession of a system’s operator, increasing the chances it will be leaked or swept up in cyberattacks,” Post reporters wrote.

Wired reported in March that DOGE has [deployed a proprietary chatbot called GSAi](https://www.wired.com/story/gsai-chatbot-1500-federal-workers/) to 1,500 federal workers at the **General Services Administration**, part of an effort to automate tasks previously done by humans as DOGE continues its purge of the federal workforce.

A **Reuters** [report](https://www.reuters.com/technology/artificial-intelligence/musks-doge-using-ai-snoop-us-federal-workers-sources-say-2025-04-08/) last month said Trump administration officials told some U.S. government employees that DOGE is using AI to surveil at least one federal agency’s communications for hostility to President Trump and his agenda. Reuters wrote that the DOGE team has heavily deployed Musk’s Grok AI chatbot as part of their work slashing the federal government, although Reuters said it could not establish exactly how Grok was being used.

Caturegli said while there is no indication that federal government or user data could be accessed through the exposed x.ai API key, these private models are likely trained on proprietary data and may unintentionally expose details related to internal development efforts at xAI, Twitter, or SpaceX.

“The fact that this key was publicly exposed for two months and granted access to internal models is concerning,” Caturegli said. “This kind of long-lived credential exposure highlights weak key management and insufficient internal monitoring, raising questions about safeguards around developer access and broader operational security.”

*This entry was posted on Thursday 1st of May 2025 08:52 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [DOGE](https://krebsonsecurity.com/category/doge/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Carole Winqwist](https://krebsonsecurity.com/tag/carole-winqwist/) [Department of Government Efficiency](https://krebsonsecurity.com/tag/department-of-government-efficiency/) [Eric Fourrier](https://krebsonsecurity.com/tag/eric-fourrier/) [General Services Administration](https://krebsonsecurity.com/tag/general-services-administration/) [GitGuardian](https://krebsonsecurity.com/tag/gitguardian/) [GitHub](https://krebsonsecurity.com/tag/github/) [Grok](https://krebsonsecurity.com/tag/grok/) [GSAi](https://krebsonsecurity.com/tag/gsai/) [Philippe Caturegli](https://krebsonsecurity.com/tag/philippe-caturegli/) [Reuters](https://krebsonsecurity.com/tag/reuters/) [Seralys](https://krebsonsecurity.com/tag/seralys/) [SpaceX](https://krebsonsecurity.com/tag/spacex/) [Tesla](https://krebsonsecurity.com/tag/tesla/) [The Washington Post](https://krebsonsecurity.com/tag/the-washington-post/) [Twitter/X](https://krebsonsecurity.com/tag/twitter-x/) [xAI](https://krebsonsecurity.com/tag/xai/)

Post navigation

[← Alleged ‘Scattered Spider’ Member Extradited to U.S.](https://krebsonsecurity.com/2025/04/alleged-scattered-spider-member-extradited-to-u-s/)
[Pakistani Firm Shipped Fentanyl Analogs, Scams to US →](https://krebs...