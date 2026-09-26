---
title: Doubts grow over claims OpenAI agent hacked Australian Medicare portal
url: https://therecord.media/openai-australia-breach-cyber
source: Over Security
date: 2026-09-25
fetch_date: 2026-09-26T06:51:45.196111
---

# Doubts grow over claims OpenAI agent hacked Australian Medicare portal

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![OpenAI](https://cms.therecord.media/uploads/large_Open_Ai_logo_7782b15323.jpg)

[Alexander Martin](/author/alexander-martin)September 25th, 2026

# Doubts grow over claims OpenAI agent hacked Australian Medicare portal

Security researchers are questioning whether an OpenAI agent needed to hack an Australian government health portal to access it, after a review of the website’s archived code found it explicitly directed visitors to an unauthenticated endpoint.

Prime Minister Anthony Albanese [said](https://therecord.media/openai-australia-health-breach) Wednesday that an OpenAI agent had gained “unauthorized access” to “non-public files” on a Medicare statistics portal after finding a way around blocks that repeatedly refused its requests. He did not describe the specific technique used.

In response to his criticism, OpenAI said its models “took actions we did not intend” but did not identify what those actions were. Neither party has released the agent’s activity logs.

A review by Recorded Future News of archived versions of the website found the agent may not have needed to find a workaround at all. The portal’s own code explicitly directed the statistics service to an unauthenticated endpoint, meaning the agent may have done exactly what the site told it to do.

If the archive evidence holds, the Australian government’s response — a task force, a parliamentary inquiry and a potential referral to the Australian Federal Police — may rest on a misconfigured website that was directing visitors to data the government now describes as non-public.

“It’s still unclear if what's happened would constitute a hack in the normal sense of the term,”said Ciaran Martin, the former chief executive of Britain’s National Cyber Security Centre and now a professor at Oxford University’s Blavatnik School of Government.

“I cannot, for the life of me, figure out why so much attention is being paid to an AI agent reading a website at a time when the FBI [appears](https://www.reuters.com/world/hacked-fbi-data-has-sensitive-information-about-employees-intelligence-roles-2026-09-23/) to have suffered one of the most consequential data breaches in history,” he said.

## Archival evidence

According to Albanese, the affected site was the Medicare Statistics Reporting Service portal, a public tool for generating reports on Medicare item usage and pharmaceutical spending.

A reconstruction of the incident [published](https://x.com/EastMelbGroupie/status/2102960384777040285) on social media suggested the agent had found its way to an open guest endpoint. The analysis, which as of Friday morning has received more than 60,000 views, has been reposted dozens of times by Australian security researchers particularly critical of Albanese’s claims.

Recorded Future News independently verified that reconstruction from JavaScript [archived](https://web.archive.org/web/20250404063401id_/https%3A//medicarestatistics.humanservices.gov.au/VEA0032/SAS.Web/MCACommon/SetupEnvironment.js) by the Internet Archive’s Wayback Machine and additionally found that the agent would not have simply “found its way,” but that the portal’s own code actively directed visitors to the open guest endpoint.

The portal had required no login for over a decade, according to the Wayback Machine. Although a March 2025 upgrade added a login page, it also enabled guest access — which signs any visitor in automatically without credentials — and published a JavaScript file, SetupEnvironment.js, containing the following logic:

```
if (ENV_PROJECT == 'statistics' && ENV_SYSTEM == 'prod') {
    var WEBSTATS_STORED_PROCESS_DO = "/SASStoredProcess/guest";
} else {
    var WEBSTATS_STORED_PROCESS_DO = "/SASStoredProcess/do";
}
```

The logic states that if a visitor is accessing the statistics project on the production server — exactly what someone querying Medicare data would be doing — then the site should send them to the guest endpoint, which requires no credentials.

The archive provides mundane explanations for Albanese’s claims. The “internal file names” he mentioned were potentially published in full by the same JavaScript file, which also exposed the complete internal server path structure to any visitor. The files “written to the internal server” are potentially chart images as the portal had generated date-stamped GIFs in a temporary folder on every chart request since at least 2018.

In response to detailed questions about the technique the agent used, the nature of the blocks, and what files were written to the server, OpenAI said it had nothing to add beyond its earlier statement.

Services Australia did not respond to a request for comment. The affected website is currently offline.

## Other agents, other techniques

The archive evidence shows the Medicare portal could have been accessed without any exploit. Separate analysis [published](https://transluce.org/agent-activity) Wednesday by researchers at Transluce, a nonprofit research lab, found the same agent swarms were using genuine attack techniques against other targets in the same period as the Medicare incident.

Transluce cited public records from urlquery.net which it said showed the agents were probing the Australian Institute of Health and Welfare, the University of New Mexico Digital Library and Data USA in May and June of this year.

The techniques used by these agents included SQL injection, path traversal and command injection. The lab linked the activity to swarms previously attributed to OpenAI, and said the “agents did this while attempting mundane data retrieval tasks which were not cyber-related.”

A spokesperson for OpenAI said: “Our initial review suggests that much of the activity described in Transluce’s report overlaps with cases at varying stages of investigation in our ongoing review of misaligned model activity.

The company has reached out to the two affected American entities and has been “in communication with the Australian government about affected government websites.”

“In our broader review, we’re continuing to prioritize the most serious incidents while expanding our work to lower-severity activity, including agents spamming websites,” the spokesperson said. “Given the scale of this work and the need to verify each case, we expect the review to take months.”

* [News](/russia-internet-shutdowns-disrupt-warnings-about-drone-attacks)
* [Government](/news/government)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Alexander Martin](https://cms.therecord.media/uploads/headshot_79eb085f87.jpeg)](/author/alexander-martin)

[Alexander Martin](/author/alexander-martin)

is the UK Editor for Recorded Future News. He was previously a technology reporter for Sky News and a fellow at the European Cyber Conflict Research Initiative, now Virtual Routes. He can be reached securely using Signal on: AlexanderMartin.79

## Briefs

* [Cyberattack hits Welsh police force, may have affected staff dataSeptember 25th, 2026](/wales-cyberattack-police-breach)
* [Astrana latest healthcare tech firm to report data breach to SECSept...