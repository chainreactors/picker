---
title: DOGE Denizen Marko Elez Leaked API Key for xAI
url: https://krebsonsecurity.com/2025/07/doge-denizen-marko-elez-leaked-api-key-for-xai/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-16
fetch_date: 2025-10-06T23:56:19.568305
---

# DOGE Denizen Marko Elez Leaked API Key for xAI

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# DOGE Denizen Marko Elez Leaked API Key for xAI

July 14, 2025

[61 Comments](https://krebsonsecurity.com/2025/07/doge-denizen-marko-elez-leaked-api-key-for-xai/#comments)

**Marko Elez**, a 25-year-old employee at Elon Musk’s **Department of Government Efficiency** (DOGE), has been granted access to sensitive databases at the U.S. Social Security Administration, the Treasury and Justice departments, and the Department of Homeland Security. So it should fill all Americans with a deep sense of confidence to learn that Mr. Elez over the weekend inadvertently published a private key that allowed anyone to interact directly with more than four dozen large language models (LLMs) developed by Musk’s artificial intelligence company **xAI**.

![](https://krebsonsecurity.com/wp-content/uploads/2025/05/x-ai.png)

On July 13, Mr. Elez committed a code script to GitHub called “agent.py” that included a private application programming interface (API) key for xAI. The inclusion of the private key was first flagged by **GitGuardian**, a company that specializes in detecting and remediating exposed secrets in public and proprietary environments. GitGuardian’s systems constantly scan GitHub and other code repositories for exposed API keys, and fire off automated alerts to affected users.

**Philippe Caturegli**, “chief hacking officer” at the security consultancy **Seralys,**said the exposed API key allowed access to at least 52 different LLMs used by xAI. The most recent LLM in the list was called “grok-4-0709” and was created on July 9, 2025.

**Grok**, the [generative AI chatbot](https://x.ai/grok) developed by xAI and integrated into **Twitter/X**, relies on these and other LLMs (a query to Grok before publication shows Grok currently uses Grok-3, which was launched in Feburary 2025). Earlier today, xAI [announced](https://x.com/xai/status/1944776899420377134) that the Department of Defense will begin using Grok as part of [a contract worth up to $200 million](https://www.washingtonpost.com/technology/2025/07/14/elon-musk-grok-defense-department/). The contract award came less than a week after Grok began [spewing antisemitic rants and invoking Adolf Hitler](https://www.npr.org/2025/07/09/nx-s1-5462609/grok-elon-musk-antisemitic-racist-content).

Mr. Elez did not respond to a request for comment. The code repository containing the private xAI key was removed shortly after Caturegli notified Elez via email. However, Caturegli said the exposed API key still works and has not yet been revoked.

“If a developer can’t keep an API key private, it raises questions about how they’re handling far more sensitive government information behind closed doors,” Caturegli told KrebsOnSecurity.

Prior to joining DOGE, [Marko Elez](https://en.wikipedia.org/wiki/Marko_Elez) worked for a number of Musk’s companies. His DOGE career began at the Department of the Treasury, and a legal battle over DOGE’s access to Treasury databases showed Elez was sending unencrypted personal information [in violation of the agency’s policies](https://www.theverge.com/news/630894/doge-treasury-lawsuit-marko-elez-unencrypted-emails).

While still at Treasury, Elez resigned after **The Wall Street Journal** [linked him to social media posts](https://www.wsj.com/tech/doge-staffer-resigns-over-racist-posts-d9f11a93) that advocated racism and eugenics. When **Vice President J.D. Vance** lobbied for Elez to be rehired, **President Trump** agreed and Musk reinstated him.

Since his re-hiring as a DOGE employee, Elez has been granted access to databases at one federal agency after another. **TechCrunch** [reported in February 2025](https://techcrunch.com/2025/03/17/doge-staffer-violated-treasury-rules-by-emailing-unencrypted-personal-data/) that he was working at the Social Security Administration. In March, **Business Insider** [found](https://www.businessinsider.com/doge-staffer-fertility-clinic-pronatalist-department-of-labor) Elez was part of a DOGE detachment [assigned to the Department of Labor](https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/).

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/markoelez.png)

In April, **The New York Times** [reported](https://www.nytimes.com/interactive/2025/02/27/us/politics/doge-staff-list.html) that Elez held positions at the **U.S. Customs and Border Protection** and the **Immigration and Customs Enforcement** (ICE) bureaus, as well as the Department of Homeland Security. **The Washington Post** later [reported](https://www.washingtonpost.com/immigration/2025/04/21/doge-ecas-justice-immigration-courts-trump/) that Elez, while serving as a DOGE advisor at the **Department of Justice**, had gained access to the Executive Office for Immigration Review’s Courts and Appeals System (EACS).

Elez is not the first DOGE worker to publish internal API keys for xAI: In May, KrebsOnSecurity [detailed](https://krebsonsecurity.com/2025/05/xai-dev-leaks-api-key-for-private-spacex-tesla-llms/) how another DOGE employee leaked a private xAI key on GitHub for two months, exposing LLMs that were custom made for working with internal data from Musk’s companies, including SpaceX, Tesla and Twitter/X.

Caturegli said it’s difficult to trust someone with access to confidential government systems when they can’t even manage the basics of operational security.

“One leak is a mistake,” he said. “But when the same type of sensitive key gets exposed again and again, it’s not just bad luck, it’s a sign of deeper negligence and a broken security culture.”

*This entry was posted on Monday 14th of July 2025 09:23 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [DOGE](https://krebsonsecurity.com/category/doge/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Business Insider](https://krebsonsecurity.com/tag/business-insider/) [DOGE](https://krebsonsecurity.com/tag/doge/) [GitGuardian](https://krebsonsecurity.com/tag/gitguardian/) [GitHub](https://krebsonsecurity.com/tag/github/) [Grok](https://krebsonsecurity.com/tag/grok/) [Marko Elez](https://krebsonsecurity.com/tag/marko-elez/) [Philippe Caturegli](https://krebsonsecurity.com/tag/philippe-caturegli/) [President Trump](https://krebsonsecurity.com/tag/president-trump/) [Seralys](https://krebsonsecurity.com/tag/seralys/) [Techcrunch](https://krebsonsecurity.com/tag/techcrunch/) [The New York Times](https://krebsonsecurity.com/tag/the-new-york-times/) [The Wall Street Journal](https://krebsonsecurity.com/tag/the-wall-street-journal/) [The Washington Post](https://krebsonsecurity.com/tag/the-washington-post/) [twitter](https://krebsonsecurity.com/tag/twitter/) [Vice President J.D. Vance](https://krebsonsecurity.com/tag/vice-president-j-d-vance/) [X](https://krebsonsecurity.com/tag/x/) [xAI](https://krebsonsecurity.com/tag/xai/)

Post navigation

[← UK Arrests Four in ‘Scattered Spider’ Ransom Group](https://krebsonsecurity.com/2025/07/uk-charges-four-in-scattered-spider-ransom-group/)
[Poor Passwords Tattle on AI Hiring Bot Maker Paradox.ai →](https://krebsonsecurity.com/2025/07/poor-passwords-tattle-on-ai-hiring-bot-maker-paradox-ai/)

## 61 ...