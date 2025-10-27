---
title: New Qilin Ransomware Attack Uses VPN Credentials, Steals Chrome Data
url: https://thehackernews.com/2024/08/new-qilin-ransomware-attack-uses-vpn.html
source: The Hacker News
date: 2024-08-24
fetch_date: 2025-10-06T18:07:28.004354
---

# New Qilin Ransomware Attack Uses VPN Credentials, Steals Chrome Data

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

# [New Qilin Ransomware Attack Uses VPN Credentials, Steals Chrome Data](https://thehackernews.com/2024/08/new-qilin-ransomware-attack-uses-vpn.html)

**Aug 23, 2024**Ravie LakshmananRansomware / Data Breach

[![Qilin Ransomware Attack](data:image/png;base64... "Qilin Ransomware Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim6dV6h2dVU_94IVAKtyaL17vKHQQ6Ie8ljr3oBylLNLt5X9byIO_gL45RliOkbvwVkLacPNU_E3T2XoL2w2RWRrFn6o9vbaeo2k5ckOk6rcK-Vsr21886N7PbC3AqVnsdWgsxL04VIx7loCM68A5ef6fh4oDhtri095YqQoUFUbCDA1tnt_cYjRE_rZj9/s790-rw-e365/chrome.png)

The threat actors behind a recently observed Qilin ransomware attack have stolen credentials stored in Google Chrome browsers on a small set of compromised endpoints.

The use of credential harvesting in connection with a ransomware infection marks an unusual twist, and one that could have cascading consequences, cybersecurity firm Sophos said in a Thursday report.

The attack, detected in July 2024, involved infiltrating the target network via compromised credentials for a VPN portal that lacked multi-factor authentication (MFA), with the threat actors conducting post-exploitation actions 18 days after initial access took place.

"Once the attacker reached the domain controller in question, they edited the default domain policy to introduce a logon-based Group Policy Object (GPO) containing two items," researchers Lee Kirkpatrick, Paul Jacobs, Harshal Gosalia, and Robert Weiland [said](https://news.sophos.com/en-us/2024/08/22/qilin-ransomware-caught-stealing-credentials-stored-in-google-chrome/).

The first of them is a PowerShell script named "IPScanner.ps1" that's designed to harvest credential data stored within the Chrome browser. The second item is a batch script ("logon.bat") contacting commands to execute the first script.

"The attacker left this GPO active on the network for over three days," the researchers added.

"This provided ample opportunity for users to log on to their devices and, unbeknownst to them, trigger the credential-harvesting script on their systems. Again, since this was all done using a logon GPO, each user would experience this credential-scarfing each time they logged in."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attackers then exfiltrated the stolen credentials and took steps to erase evidence of the activity before encrypting the files and dropping the ransom note in every directory on the system.

The theft of credentials stored in the Chrome browser means that affected users are now required to change their username-password combinations for every third-party site.

"Predictably, ransomware groups continue to change tactics and expand their repertoire of techniques," the researchers said.

"If they, or other attackers, have decided to also mine for endpoint-stored credentials – which could provide a foot in the door at a subsequent target, or troves of information about high-value targets to be exploited by other means – a dark new chapter may have opened in the ongoing story of cybercrime."

## Ever-evolving Trends in Ransomware

The development comes as ransomware groups like [Mad Liberator](https://news.sophos.com/en-us/2024/08/13/dont-get-mad-get-wise/) and [Mimic](https://news.sophos.com/en-us/2024/08/07/sophos-mdr-hunt-tracks-mimic-ransomware-campaign-against-organizations-in-india/) have been observed using unsolicited AnyDesk requests for data exfiltration and leveraging internet-exposed Microsoft SQL servers for initial access, respectively.

The Mad Liberator attacks are further characterized by the threat actors abusing the access to transfer and launch a binary called "Microsoft Windows Update" that displays a bogus Windows Update splash screen to the victim to give the impression that software updates are being installed on the machine while the data is being plundered.

The [abuse of legitimate remote desktop tools](https://www.reliaquest.com/blog/rmm-tool-abuse/), as opposed to custom-made malware, offers attackers the perfect disguise to camouflage their malicious activities in plain sight, allowing them to blend in with normal network traffic and evade detection.

[![Ransomware Attack](data:image/png;base64... "Ransomware Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNXYOTGnZMh7TsyFAe-sfkOtdVUn0pb62V-GkELcer7PWm88HHCz75gHRAj_9MsZZP-ZlC3knmpMIX7xASGoJxkJEiPBHOE_IeH7l7gc2gyRitrfJpkPPiAgp8nBtMmIv2Ml9do5o63ReD4A-FVqO_M72WqCJyW5S7ytjkLNqZZCWvL7vz59-lfOHYckzl/s790-rw-e365/square.png)

Ransomware continues to be a profitable venture for cybercriminals despite a series of law enforcement actions, with 2024 set to be the highest-grossing year yet. The year also saw the [largest ransomware payment](https://www.zscaler.com/blogs/security-research/threatlabz-ransomware-report-unveiling-75m-ransom-payout-amid-rising) ever recorded at approximately $75 million to the [Dark Angels](https://thehackernews.com/2023/11/us-treasury-targets-russian-money.html) ransomware group.

"The median ransom payment to the most severe ransomware strains has spiked from just under $200,000 in early 2023 to $1.5 million in mid-June 2024, suggesting that these strains are prioritizing targeting larger businesses and critical infrastructure providers that may be more likely to pay high ransoms due to their deep pockets and systemic importance," blockchain analytics firm Chainalysis [said](https://www.chainalysis.com/blog/2024-crypto-crime-mid-year-update-part-1/).

Ransomware victims are estimated to have paid $459.8 million to cybercriminals in the first half of the year, up from $449.1 million year-over-year. However, total ransomware payment events as measured on-chain have declined YoY by 27.29%, indicating a drop in payment rates.

What's more, Russian-speaking threat groups [accounted](https://www.trmlabs.com/post/new-trm-report-reveals-russian-speaking-groups-dominate-ransomware) for at least 69% of all cryptocurrency proceeds linked to ransomware throughout the pr...