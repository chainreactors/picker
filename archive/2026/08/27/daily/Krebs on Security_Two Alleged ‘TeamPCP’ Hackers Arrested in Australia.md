---
title: Two Alleged ‘TeamPCP’ Hackers Arrested in Australia
url: https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/
source: Krebs on Security
date: 2026-08-27
fetch_date: 2026-08-28T13:38:09.846048
---

# Two Alleged ‘TeamPCP’ Hackers Arrested in Australia

Advertisement

[![](/b-cape/1.jpg)](https://www.cape.co/?utm_source=Krebs&utm_medium=Banner&utm_campaign=Krebs_Display_Footer_Desktop)

Advertisement

[![](/b-cape/2.jpg)](https://www.cape.co/?utm_source=Krebs&utm_medium=Banner&utm_campaign=Krebs_Display_Footer_Mobile)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Two Alleged ‘TeamPCP’ Hackers Arrested in Australia

August 27, 2026

[16 Comments](https://krebsonsecurity.com/2026/08/two-alleged-teampcp-hackers-arrested-in-australia/#comments)

Authorities in Australia have arrested two men believed to be members of **TeamPCP**, a prolific cybercrime and data extortion group blamed for perpetrating the longest running spree of software supply chain attacks ever.

In [a statement](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global) released today, the **Australian Federal Police** (AFP) said two men from Western Australia, aged 21 and 23, were arrested in connection with a “sophisticated cybercrime syndicate that allegedly created malicious open-source software to rob thousands of global businesses.”

The AFP did not name the defendants, but KrebsOnSecurity learned the 21-year-old suspect’s real identity in June, and has been communicating with him ever since. This story includes interviews with TeamPCP’s self-described spokesperson, and examines clues left behind by the TeamPCP leader that likely led to his undoing.

TeamPCP vaulted onto the cybercrime scene in late 2025, embedding malicious code in hundreds of open source software tools and extorting victims for profit. Members of the group made headlines by compromising corporate cloud environments using a self-propagating worm dubbed **Shai-Hulud**, which added malicious code to open source programs maintained by developers whose credentials at public code repositories like GitHub or NPM were phished or stolen.

Writing for *Wired*, journalist **Andy Greenberg** described TeamPCP’s core tactic as a kind of cyclical exploitation of software developers.

“The hackers gain access to a network where an open source tool commonly used by coders is being developed,” Greenberg [wrote in May](https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/). “The hackers plant malware in the tool that ends up on other software developers’ machines, including some who are writing other tools intended to be used by coders. The malware allows TeamPCP’s hackers to steal credentials that let them publish malicious versions of those software development tools, too. The cycle repeats, and TeamPCP’s collection of breached networks grows.”

TeamPCP also has practiced something akin to cyclical recruitment. In May, the source code for the third iteration of Shai-Hulud was published online, and TeamPCP soon after launched a contest offering $1,000 in virtual currency to whichever participant could conduct the largest supply chain operation using the worm’s code. According to the contest rules, participants were scored based on the number of weekly and monthly downloads of packages they compromised — directly incentivizing them to target the most popular code libraries.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/teampcp-shai-hulud.png)

A screenshot of a message from TeamPCP’s Telegram account, announcing the supply chain hacking contest. Image: dataminr.com.

“TeamPCP has stated the competition is a recruiting opportunity and they intend to purchase all meaningful access harvested from participants’ campaigns,” the security firm Dataminr [wrote](https://www.dataminr.com/resources/cyber-intel-deep-dive-teampcp-shai-hulud-3-0/). “The $1,000 XMR (Monero) prize is a recruitment floor and has been dismissed by the actor as ‘just like participation trophy,’ adding ‘if you find something good you will be paid way more,’ confirming the contest’s true function as talent identification and malicious access acquisition at scale.”

In March, TeamPCP executed a supply chain attack targeting AI infrastructure by compromising the code for **LiteLLM**, an open source AI gateway that connects users to more than 100 different large language models. A [recent analysis](https://www.cloudsek.com/blog/ai-supply-chain-breach-2500-companies-434000-cicd-pipelines) by the security firm **CloudSEK** found TeamPCPs attack on LiteLLM harvested cloud service keys and other secrets from more than 2,500 organizations, including many of the world’s top technology companies.

In May, TeamPCP claimed credit for compromising at least 3,800 code repositories at the Microsoft-owned **GitHub**, after a GitHub developer installed a code extension that was compromised by TeamPCP’s malware.

## MEET THE CYBERCATS

Security experts say TeamPCP is less of a hacker group than an amalgamation of threat actors from multiple cybercriminal gangs who sometimes work together toward similar goals.

“It is not a structured criminal crew with a single operator,” said **Austin Larsen**, a principal threat analyst with the **Google Threat Intelligence Group**. “It is a peer community of individually-skilled actors, with one clear center of gravity.”

That center of gravity is **George Prepakis**, an accomplished security researcher and self-described exploit developer who operates the Twitter/X profile [@kernelstub](https://x.com/kernelstub). Earlier this year, @kernelstub tweeted a public invite link to a Matrix chat server he created and dubbed “Cybercats,” and TeamPCP and several other cybercrime entities have been using this server to communicate daily for the past several months.

![](https://krebsonsecurity.com/wp-content/uploads/2026/08/matrix-tpcp-xpl0itrs.png)

A screenshot of the Matrix chat server “Cybercats,” whose members used hacker handles associated with multiple distinct cybercrime groups that have occasionally collaborated on a series of supply chain and data ransom attacks over the past nine months.

Kernelstub, like other administrators in the Cybercats chat, has been using his Twitter/X profile name as his handle in these Matrix communications, frequently tweeting references to other members and to conversations taking place in the Cybercats chat. In a number of cases, the corresponding X accounts for members of the Cybercats chat taunted cybercrime victims publicly before the incidents were reported in the news media.

The Cybercats administrator listed at the top of the screenshot above — “**Boxturtle**” — is a close associate of TeamPCP who has been tweeting about the group’s conquests under the name [@xpl0itrsturtle](https://x.com/xploitrsturtle2/). This handle corresponds to a data breach broker active on Breachforums and Darkforums who has been selling data stolen in a wave of recent breaches at automobile manufacturers, including **BMW Group**, **Audi**, **Honda**, **Mercedes-Benz**, **Volvo** and **Toyota**, as well as data allegedly taken from **Snapchat** and **SportRadar**.

![](https://krebsonsecurity.com/wp-content/uploads/2026/08/xpl0itrs-dls.png)

The data leak site for the extortion group or handle “xpl0itrs.”

The Cybercats administrator “**SeesawSec**” in the screenshot above is the alias of whoever is behind the cybercrime group known as **Fulcrumsec**, which recently claimed credit for data extortion attacks against the pharmaceutical giant **Novo Nordisk**, the data broker **LexisNexis**, and **Avnet**, a Fortune 500 distributor of electronic components.

![](https://krebsonsecurity.com/wp-content/uploads/2026/08/fulcrumsec-dls.png)

The data leak site of Fulcrum Security, a.k.a. Fulcrumsec.

The Cybercats administrator “**@pcpcasper**” also has been using a similar name on X to dis...