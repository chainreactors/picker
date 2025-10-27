---
title: Global Microsoft Meltdown Tied to Bad Crowdstrike Update
url: https://krebsonsecurity.com/2024/07/global-microsoft-meltdown-tied-to-bad-crowstrike-update/
source: Krebs on Security
date: 2024-07-20
fetch_date: 2025-10-06T17:45:07.204573
---

# Global Microsoft Meltdown Tied to Bad Crowdstrike Update

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Global Microsoft Meltdown Tied to Bad Crowdstrike Update

July 19, 2024

[95 Comments](https://krebsonsecurity.com/2024/07/global-microsoft-meltdown-tied-to-bad-crowstrike-update/#comments)

A faulty software update from cybersecurity vendor **Crowdstrike** crippled countless **Microsoft Windows** computers across the globe today, disrupting everything from airline travel and financial institutions to hospitals and businesses online. Crowdstrike said a fix has been deployed, but experts say the recovery from this outage could take some time, as Crowdstrike’s solution needs to be applied manually on a per-machine basis.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/crowdstrike-bsod.png)

Earlier today, an errant update shipped by Crowdstrike began causing Windows machines running the software to display the dreaded “Blue Screen of Death,” rendering those systems temporarily unusable. Like most security software, Crowdstrike requires deep hooks into the Windows operating system to fend off digital intruders, and in that environment a tiny coding error can quickly lead to catastrophic outcomes.

In a post on Twitter/X, Crowdstrike CEO **George Kurtz** said an update to correct the coding mistake has been shipped, and that Mac and Linux systems are not affected.

“This is not a security incident or cyberattack,” Kurtz said on Twitter, echoing [a written statement by Crowdstrike](https://www.crowdstrike.com/blog/statement-on-windows-sensor-update/). “The issue has been identified, isolated and a fix has been deployed.”

Posting to Twitter/X, the director of Crowdstrike’s threat hunting operations [said](https://x.com/brody_n77/status/1814185935476863321) the fix involves booting Windows into Safe Mode or the Windows Recovery Environment (Windows RE), deleting the file “C-00000291\*.sys” and then restarting the machine.

The software snafu may have been compounded by a recent series of outages involving Microsoft’s **Azure** cloud services, *The New York Times* [reports](https://www.nytimes.com/2024/07/19/business/microsoft-outage-cause-azure-crowdstrike.html), although it remains unclear whether those Azure problems are at all related to the bad Crowdstrike update. **Update, 4:03 p.m. ET:** Microsoft [reports](https://azure.status.microsoft/en-us/status) the Azure problems today were unrelated to the bad Crowdstrike update.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/den-msbsod.png)

**Matt Burgess** at *Wired* [writes](https://www.wired.com/story/microsoft-windows-outage-crowdstrike-global-it-probems/) that within health care and emergency services, various medical providers around the world have reported issues with their Windows-linked systems, sharing news on social media or their own websites.

“The US Emergency Alert System, which issues hurricane warnings, said that there had been various 911 outages in a number of states,” Burgess wrote. “Germany’s University Hospital Schleswig-Holstein said it was canceling some nonurgent surgeries at two locations. In Israel, more than a dozen hospitals have been impacted, as well as pharmacies, with reports saying ambulances have been rerouted to nonimpacted medical organizations.”

In the United Kingdom, NHS England has confirmed that appointment and patient record systems have been impacted by the outages.

“One hospital has declared a ‘critical’ incident after a third-party IT system it used was impacted,” Wired reports. “Also in the country, train operators have said there are delays across the network, with multiple companies being impacted.”

Reactions to today’s outage were swift and brutal on social media, which was flooded with images of people at airports surrounded by computer screens displaying the Microsoft blue screen error. Many Twitter/X users chided the Crowdstrike CEO for failing to apologize for the massively disruptive event, while others noted that doing so could expose the company to lawsuits.

Meanwhile, the international Windows outage quickly became the most talked-about subject on Twitter/X, whose artificial intelligence bots collated a series of parody posts from cybersecurity professionals pretending to be on their first week of work at Crowdstrike. Incredibly,Twitter/X’s AI summarized these sarcastic posts into a sunny, can-do story about Crowdstrike that was promoted as the top discussion on Twitter this morning.

“Several individuals have recently started working at the cybersecurity firm Crowdstrike and have expressed their excitement and pride in their new roles,” the AI summary read. “They have shared their experiences of pushing code to production on their first day and are looking forward to positive outcomes in their work.”

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/x-react-csms.png)

This is an evolving story. Stay tuned for updates.

*This entry was posted on Friday 19th of July 2024 10:24 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[blue screen of death](https://krebsonsecurity.com/tag/blue-screen-of-death/) [CrowdStrike](https://krebsonsecurity.com/tag/crowdstrike/) [George Kurtz](https://krebsonsecurity.com/tag/george-kurtz/) [microsoft](https://krebsonsecurity.com/tag/microsoft/)

Post navigation

[← Researchers: Weak Security Defaults Enabled Squarespace Domains Hijacks](https://krebsonsecurity.com/2024/07/researchers-weak-security-defaults-enabled-squarespace-domains-hijacks/)
[Phish-Friendly Domain Registry “.top” Put on Notice →](https://krebsonsecurity.com/2024/07/phish-friendly-domain-registry-top-put-on-notice/)

## 95 thoughts on “Global Microsoft Meltdown Tied to Bad Crowdstrike Update”

1. J [July 19, 2024](https://krebsonsecurity.com/2024/07/global-microsoft-meltdown-tied-to-bad-crowstrike-update/comment-page-2/#comment-612109)

   Just call it X
2. Spencer H., CHCIO, FACHE [July 19, 2024](https://krebsonsecurity.com/2024/07/global-microsoft-meltdown-tied-to-bad-crowstrike-update/comment-page-2/#comment-612114)

   I am a Certified Healthcare CIO, so I have years of background working in this field. There is a lot of friction between the “new” generation of IT Leaders and my generation of IT leaders. My generation has always focused much effort on testing and regression testing of code and patches, the result being longer patch cycles. New DevOps teams want to patch more often with less testing. Both approaches have their pros and cons. This is an example of the “old” way of testing being more appropriate. In my world, if we had 10 variants of Windows Operating Systems (Windows 10, release xxxxxx, Windows 11, release xxxxxx), I would require 1000 tests to be run, 100 on each variant, before we released to PROD. In todays DevOps world, it is common to minimize testing, and just fix “whatever breaks” on the backend, after-the-fact. The reality is that we need to meet in the middle between these two processes and come up with something that prevents this from happening.

   There is truly no excuse for this. IMO, the CIO, CTO, and the CEO needs to be held accountable for...