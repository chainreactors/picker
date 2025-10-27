---
title: Anatsa Targets North America; Uses Proven Mobile Campaign Process
url: https://www.threatfabric.com/blogs/anatsa-targets-north-america-uses-proven-mobile-campaign-process
source: Over Security - Cybersecurity news aggregator
date: 2025-07-09
fetch_date: 2025-10-06T23:54:47.046570
---

# Anatsa Targets North America; Uses Proven Mobile Campaign Process

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## Anatsa Targets North America; Uses Proven Mobile Campaign Process

08 July 2025

![](https://www.threatfabric.com/hubfs/TF_Anatsa_BlogUSA.jpg)

### Jump to

ThreatFabric researchers have identified a new campaign involving the Anatsa Android banking trojan, which is now targeting users in North America. This marks at least the third instance of Anatsa focusing its operations on mobile banking customers in the United States and Canada. As with previous campaigns, Anatsa is being distributed via the official Google Play Store.

## What is Anatsa?

Anatsa is a sophisticated device-takeover trojan designed to provide its operators with extensive capabilities. These include stealing credentials through overlay and keylogging attacks, as well as executing fraudulent transactions directly from infected devices via remote control functionalities.

ThreatFabric has been monitoring Anatsa's activity since 2020 and recognises the group as one of the most prolific operators in the mobile crimeware landscape. Their campaigns have consistently demonstrated a high level of success. This latest campaign is particularly notable due to its intensified focus on North American targets.

## How Does Anatsa Operate?

Anatsa campaigns typically follow a consistent and methodical process:

* A developer establishes a profile on an app store.
* They upload a new application – such as a PDF reader, phone cleaner, file manager, or another generic tool. Initially, the application is entirely legitimate and functions as advertised.
* Once the application gains a substantial user base – often in the thousands or tens of thousands of downloads – an update is deployed, embedding malicious code into the app.
* This embedded code downloads and installs Anatsa on the device as a separate application.
* Anatsa receives targets from its command-and-control server, which can be updated at any time. These targets are primarily financial institutions and banking applications. Depending on the target, Anatsa can perform credential theft for account takeover, keylogging, or even fully automated fraudulent transactions.
* Users may report issues with their banking applications as these malicious actions are carried out.

Anatsa is known for its cyclical activity, alternating between periods of active distribution and dormancy. These waves allow the malware operators to evade detection while maintaining a high success rate.

## North America Campaign Specifics

The latest Anatsa campaign in North America demonstrates the group’s geographical ambition. The malicious payload was deployed under the guise of a “PDF Update” within a file reader dropper application. The dropper app achieved significant visibility, ranking among the top three in the “Top Free Tools” category on the official US Google Play Store. By the time it was removed, the app had amassed over 50,000 downloads.

This dropper followed Anatsa’s established modus operandi: initially launched as a legitimate app, it was transformed into a malicious one approximately six weeks after release. The distribution window for this campaign was short yet impactful, running from 24 to 30 June.

A key characteristic of this operation was its broadened target list, which included a wider range of mobile banking applications in the United States. This targeted approach highlights Anatsa’s increasing focus on exploiting North American financial institutions.

![A screenshot of a computer  AI-generated content may be incorrect., Picture](https://www.threatfabric.com/hs-fs/hubfs/undefined-3.png?width=1376&height=1277&name=undefined-3.png)

Our analysis of the latest campaign reveals that Anatsa employs a technique where a deceptive overlay message is displayed when users attempt to access their banking applications. The overlay typically reads:

*Scheduled Maintenance**We are currently enhancing our services and will have everything back up and running shortly. Thank you for your patience.*

This tactic serves two purposes:

* To obscure the malicious activity occurring within the targeted application.
* To prevent users from contacting the banking application's customer support, thereby delaying detection of the fraudulent operations.

## Conclusion

The Anatsa malware campaigns continue to show a growing focus on North American targets, particularly mobile banking applications. The latest operation not only broadened its reach but also relied on well-established tactics aimed at financial institutions in the region. Organisations in the financial sector are encouraged to review the provided intelligence and assess any potential risks or impacts on their customers and systems.

---

### Further Reading

As the technical workings of the Anatsa malware remain consistent with previous campaigns, further insights can be found in our earlier analyses. For a comprehensive technical overview, refer to our previous blogs on Anatsa, such as this one:

[Anatsa hits UK and DACH with new campaign](https://www.threatfabric.com/blogs/anatsa-hits-uk-and-dach-with-new-campaign)

## Questions or demo?

[CONTACT US](https://www.threatfabric.com/contact)

![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg)

* [JOBS](https://www.threatfabric.com/jobs)
* [PRIVACY](https://www.threatfabric.com/privacy)
* [INTEL/PGP](https://www.threatfabric.com/contact)
* [VULNERABILITY DISCLOSURE](https://www.threatfabric.com/vulnerability-disclosure-policy)

![40185](https://www.threatfabric.com/hubfs/40185.png)

![](https://px.ads.linkedin.com/collect/?pid=3969834&fmt=gif)