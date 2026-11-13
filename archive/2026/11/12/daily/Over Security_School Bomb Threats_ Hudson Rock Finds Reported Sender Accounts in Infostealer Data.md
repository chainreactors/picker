---
title: School Bomb Threats: Hudson Rock Finds Reported Sender Accounts in Infostealer Data
url: https://www.infostealers.com/article/school-bomb-threats-hudson-rock-finds-reported-sender-accounts-in-infostealer-data/
source: Over Security
date: 2026-11-12
fetch_date: 2026-11-13T09:07:23.752276
---

# School Bomb Threats: Hudson Rock Finds Reported Sender Accounts in Infostealer Data

[Skip to content](#site-main)

[![](https://www.infostealers.com/wp-content/themes/infostealers-sage/resources/images/infostealers-icon-black.png)
![](https://www.infostealers.com/wp-content/themes/infostealers-sage/resources/images/infostealers-icon-white.png)

INFOSTEALERS

By HudsonRock](https://www.infostealers.com/)

[Home](https://www.infostealers.com/)
[Blog](https://www.infostealers.com/learn-info-stealers/)
[Reports](https://www.infostealers.com/info-stealers-reports/)
[Threat Feeds](https://www.infostealers.com/threat-feeds/)
[Victims](https://www.infostealers.com/infostealer-victims/)

Resources

* [Infostealer Index
  Intelligence vendors ranked and compared](https://www.infostealers.com/infostealer-index/)
* [Techniques
  MITRE ATT&CK mapped by stealer family](https://www.infostealers.com/info-stealers-techniques/)
* [Glossary
  Cybercrime terms in plain language](https://www.infostealers.com/glossary/)

[About](https://www.infostealers.com/about-info-stealers/)

Search
`⌘K`

Free Individual Protection

![](https://www.infostealers.com/wp-content/uploads/2026/11/bomb_header.png)

1. [Home](https://www.infostealers.com/)/
2. [Blog](https://www.infostealers.com/learn-info-stealers/)/
3. School Bomb Threats: Hudson Rock Finds Reported Sender Accounts in Infostealer Data

Blog Post

# School Bomb Threats: Hudson Rock Finds Reported Sender Accounts in Infostealer Data

![](https://secure.gravatar.com/avatar/a917127d480b5b9fb3257b42447749cf299758c29d41b3c7cb28c470ecc8cbff?s=28&d=mm&r=g) InfoStealers

Nov 12, 2026

11 min read

![](https://www.infostealers.com/wp-content/uploads/2026/11/bomb_header.png)

Hudson Rock Research   /   Credential Exposure

# School Bomb Threats: Hudson Rock Finds Reported Sender Accounts in Infostealer Data

Two university email addresses associated with the threats appear in Hudson Rock’s stolen-credential holdings. The Egyptian record dates to a 2021 Vidar infection; the Taiwanese credentials were found in the historical AlienTXTBASE collection.

By Hudson RockNovember 12, 2026Investigation & analysis

The bomb-threat emails that disrupted Italian schools on November 11 have a significant credential-exposure connection. Hudson Rock identified records for both university email addresses highlighted in threat-related material: `[[email protected]](/cdn-cgi/l/email-protection)` and `[[email protected]](/cdn-cgi/l/email-protection)`.

The Egyptian address is associated with a detailed infostealer record containing passwords extracted from an infected computer, including credentials saved against Microsoft authentication pages. Hudson Rock located the Taiwanese credentials in **AlienTXTBASE**, a credential collection containing aggregated infostealer data. Hudson Rock assesses the matching record as infostealer-derived and dates the reviewed data to more than a year before the threats.

**Both findings place credential exposure well before the disruption, creating a substantial window in which exposed access could have been investigated and secured.** Authentication and mail-delivery records from the providers are needed to determine whether these credentials were used to send the threats.

What Hudson Rock found

* **Egyptian university address:** a Vidar-associated machine record dated October 1, 2021, with saved Microsoft credentials and a broader collection of browser passwords.
* **Taiwanese university address:** a matching Microsoft credential entry in AlienTXTBASE, in data that Hudson Rock dates to more than a year before the threats. The university subsequently reported abnormal bulk sending and suspended the account.
* **The security implication:** verified credential theft should trigger containment and closer scrutiny before an account can be repurposed for abuse.

## The threats that disrupted schools across Europe

Reporting published and updated on November 12 followed a wave of threatening emails sent the previous day. [ANSA reported that approximately 6,000 Italian schools received the messages](https://www.ansa.it/sito/notizie/cronaca/2026/11/11/vi-annienteremo-lallarme-bomba-in-6.000-scuole-italiane.-meloni-strategia-per-il-caos_870b0024-72d2-4b15-bab5-0c74dcc1d653.html), citing the Education Ministry. Some schools evacuated; others continued lessons after consulting police. The recipient count should not be read as an evacuation count.

The messages claimed to be from “Mikhail Andropov,” included threats against pupils and staff, and referred to an alleged bomb targeting the prime minister. The name and organizational labels in those emails are claims made by the sender, not verified attribution.

Prime Minister Giorgia Meloni addressed the disruption on November 11. She said searches had found no bombs and described an attempt to generate fear and chaos. In a video statement reported by [ANSA](https://www.ansa.it/sito/notizie/topnews/2026/11/11/meloni-non-permetteremo-a-una-mail-anonima-di-decidere-il-calendario-scolastico_6a6809dc-f12f-48b8-9a16-a7376e58ac05.html), she said:

> “We will not allow an anonymous email to decide our children’s school calendar.”
>
> Giorgia Meloni, November 11, 2026. Translated from Italian.

[![Screenshot of Giorgia Meloni’s November 11 post responding to the school bomb threats, showing translated text and a still from her video statement.](https://www.infostealers.com/wp-content/uploads/2026/11/bomb5.png)](https://www.infostealers.com/wp-content/uploads/2026/11/bomb5.png)

**Figure 1.** Prime Minister Giorgia Meloni’s [November 11 post on X](https://x.com/GiorgiaMeloni/status/2120596347271188849), shown with the platform’s English translation. Her response underscores the national disruption caused by the threatening emails.

The disruption extended beyond Italy. [Police in Northern Ireland](https://www.psni.police.uk/latest-news/threatening-emails-over-300-schools-being-treated-hoax) said more than 300 schools reported the same threatening message. [Police Scotland](https://www.scotland.police.uk/what-s-happening/news/2026/november/statement-after-threatening-messages-sent-to-a-number-of-schools-in-scotland/) also investigated school threats and assessed them as hoaxes.

In Ireland, [The Journal reported threats to schools and newsrooms](https://www.thejournal.ie/bomb-threats-schools-media-thejournal-7222128-Nov2026/?jrnl_lg=1), including its own. It specifically said different addresses were used for the school and media messages. Hudson Rock’s findings here concern the two addresses examined below; they do not establish a common operator or an infostealer connection for every contemporaneous threat.

## Two university accounts with historical credential exposure

Egyptian university address
`[[email protected]](/cdn-cgi/l/email-protection)`

**Threat connection:** the reported address appears in an annotated newspaper screenshot and a public post reviewed in this investigation.

**Hudson Rock evidence:** a Vidar-associated machine profile, system information, and extracted browser credentials.

Taiwanese university address
`[[email protected]](/cdn-cgi/l/email-protection)`

**Threat connection:** independently published by a recipient school; the university reported apparent account compromise.

**Hudson Rock evidence:** a Microsoft URL–login–password entry recovered from the historical AlienTXTBASE collection.

## The Egyptian account: inside a documented infostealer exposure

A photograph used in [la Repubblica’s coverage](https://www.repubblica.it/cronaca/2026/11/11/news/mail_scuole_mikhail_andropov_chi_e-425715611/) shows the display name “Mosaad Khalifa” and the beginning of a matching email address above the threatening text. The annotated reproduction below identifies the full reported address as `[[email protected]](/cdn-cgi/l/email-protection)`.

[![Annotated screenshot of la Repubblica’s bomb-threat coverage, highlighting the apparent Egyptian university sender identity.](https://www.infostealers.com/wp-content/uploads/2026/11/bomb3.png)](https://www.i...