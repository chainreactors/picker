---
title: Hacked Russian CRMs Being Used in Phishing Attacks
url: https://pixmsecurity.com/blog/phish/hacked-russian-crms-being-used-in-phishing-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-31
fetch_date: 2025-10-04T11:16:23.313125
---

# Hacked Russian CRMs Being Used in Phishing Attacks

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# Hacked Russian CRMs Being Used in Phishing Attacks

# Introduction

For many years, Customer Relationship Management (CRM) software has allowed businesses to automate sales outreach and prospecting data collection at scale. A core feature of CRM suites is the ability to automate customer interactions. This is done through the creation of campaigns with custom landing pages or emails that the platform will distribute to your intended audience. For example, campaigns allow users to send email blasts and customer experience surveys to large customer groups. Cyber criminals are now increasingly leveraging the impressive scale, ease of use and trustworthiness of CRMs to their advantage.

Bitrix is a popular CRM and CMS that has the largest market share of any CRM in Russia. Its software was recently identified as the source of vulnerability CVE-2022-27228. The ‘Bitrix Site Manager’ application was affected with a vulnerability that allows unauthenticated attackers to execute arbitrary code. The CMS is widely adopted in a variety of industries in Russia, the most notable affected being Industrial Organizations, whose ICS devices have been targeted after their organization’s Bitrix tenant was compromised ([source](https://www.securityweek.com/exploitation-of-bitrix-cms-vulnerability-drives-ics-attack-surge-in-russia/)). In this blog, we will dive into the anatomy of a phishing attack detected by PIXM’s AI browser extension and explore the advantages hackers reap from compromised CRM tenants.

# The CRM Based Attack

By purchasing or compromising CRM credentials belonging to a corporate tenant, cyber criminals can login to a company’s tenant in a CRM platform and access a tool designed to send blast emails to large numbers of people. Within the CRM’s email campaign feature, hackers can craft a phishing email, deploy a phishing page in the CRM or on their own infrastructure, and send that email to as many contacts as are saved in the CRM suite, often tens or hundreds of thousands. This approach not only provides an advantage in terms of scale. The phishing parent domain, either the company or CRM website, also leverages the trust of a third party. The trust of that domain allows the phishing attack to bypass email gateways, spam filters, and reputation engines.

On February 2nd, 2023, a PIXM extension detected a Microsoft corporate spear phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2023/03/p1.png)

*Fig 1. The phishing page PIXM detected.*

Follow up investigations showed that the user opened the link in Office 365 and had Microsoft Advanced Threat Protection setup and multiple security extensions in their browser. The phishing email contained a link that was hosted on a compromised tenant of a CRM platform.

![](https://pixmsecurity.com/wp-content/uploads/2023/03/p2.png)

Fig 2. Link and redirects from original phishing email.

The example (in Fig 2) is spoofing an Office 365 email notification that a user has reached their storage limit. The email had field inputs to match the recipient’s first name and email (as were likely present in the compromised CRM). The compromised tenant domain (anonymized above in the ‘Clear Cache’ button) is a real estate business in Perm, Russia. We can see the CRM platform as well in the path, ‘bitrix’, so that the URL leverages the 3rd party reputation of both a legitimate business and a widely used CRM platform. When clicked, the link would redirect to any number of phishing domains hosting the phishing payload.

![](https://pixmsecurity.com/wp-content/uploads/2023/03/p3.png)

Fig 3. The Bitrix RU landing page.

The above (Fig 3) is the Russian language landing pages (translated to English) for the Bitrix CRM, listing its offerings. The company whose CRM was compromised in this example was a Russian real estate rental business in Perm, Russia. It is likely they leveraged the CRM to manage contacts of existing renters in the region, along with batches of leads for potential would-be renters. The destination phishing pages contain the target email in both the URL and page itself, further adding to the legitimacy.

![](https://pixmsecurity.com/wp-content/uploads/2023/03/p4.png)

Fig 4. Target email as an argument, to prepopulate the targets email as the account logging in.

# Campaign Ease and Success

The adversary may choose to use the database system built into the CRM for the collection of collected credentials, allowing for exporting all entered credentials in a few clicks (as is an intended level of convenience for the sales and/or marketing teams typically using the CRM). Alternatively, they can go the traditional route and have the credentials sent to their own infrastructure outside of the CRM.

The success rate of these campaigns is likely going to be higher than if the phishing email was sending the user to a recently registered domain with an atypical TLD. CRM companies place a high value on helping their customers’ emails land in their intended audiences inbox, without getting filtered by an email security gateway or spam/content filtering rules. In our observation of these attacks in the wild, the use of the CRM generated URLs, and sending the emails via the compromised CRM, has the desired result. The emails we observed landed as intended in the customers inbox, and all tested domain reputation engines (tested using Virustotal) returned a clean verdict on the phishing domains.

# Prevention

Preventing these types of attacks requires innovative solutions to be employed by the targets, and hopefully increased security by the CRM providers. PIXM was able to detect these attacks by way of our novel computer vision technology, which analyzes pages as they populate in the browser. These pages, which were all deemed clean by domain reputation engines, were detected by PIXM when they loaded in the target’s browser, preventing them from entering their credentials. We observe adversaries employing a variety of techniques to avoid blocking by domain reputation engines, which do not succeed against our approach.

Aside from using [our free browser extension](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en), CRM platforms should employ analysis of the URLs its clients are generating to detect potential phishing pages, as well as analyzing user login activity to detect potential anomalies.

# Conclusion

The technique observed in this attack points to the continually increasing use of legitimate third party tools in the modern adversaries phishing playbook. As we have published in previous research articles, the use of legitimate third party suites–application deployment services, sales software, and now CRMs–offer cyber criminals a variety of benefits. These benefits include a curated list of targets (no more stealing or buying email addresses in bulk), a parent domain which has inherent trust with domain reputation services, and no servers or email infrastructure to ...