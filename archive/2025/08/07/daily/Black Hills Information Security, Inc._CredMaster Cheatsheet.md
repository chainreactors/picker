---
title: CredMaster Cheatsheet
url: https://www.blackhillsinfosec.com/credmaster-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:15.825755
---

# CredMaster Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [CredMaster](https://www.blackhillsinfosec.com/tag/credmaster/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [CredMaster Cheatsheet](https://www.blackhillsinfosec.com/credmaster-cheatsheet/)

Collaborated on by: [Adam Rose](https://www.blackhillsinfosec.com/team/adam-rose/) & Martin Pearson || Reviewed by: [Alyssa Snow](https://www.linkedin.com/in/alyssa-snow-2b8437169)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_6.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**TAKE NOTE!** **Update 8/13:** After this article was published, BHIS was made aware that the use of API Gateway for penetration testing was prohibited by AWS’s Customer Service Policy for Penetration Testing (<https://aws.amazon.com/security/penetration-testing/>). CredMaster uses API Gateway extensively for IP address rotation.
Using CredMaster, even for authorized penetration testing activities, may get your AWS account banned or result in legal proceedings against you. BHIS accepts no responsibility for violations of Amazon policies or repercussions of using CredMaster.
Use at your own risk!

**CredMaster Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/09/CheetSheet_credmaster-Update.pdf)

Find the tool here: <https://github.com/knavesec/CredMaster>

---

CredMaster is a tool that facilitates password guessing attacks against common targets. It is designed with evasion and anti-detection capabilities and uses AWS APIs to rotate IP addresses for each guess.

## Prerequisites

1. CredMaster requires an AWS subscription. Create an account and create an AWS access key and secret access key (this requires a credit card and can cost money).
   * <https://aws.amazon.com/blogs/security/how-to-find-update-access-keys-password-mfa-aws-management-console/>
2. For security and ease-of-use, export the keys as environment variables so you don’t have to copy and paste multiple times:

```
export AWS_KEY=<Your Key> && export AWS_SECRET_KEY=<Your Secret Key>
```

3. Now you can reference those keys as environment variables by prepending a dollar sign ($) to the variables’ names:

```
echo $AWS_KEY
```

## Installation

1. Ensure Python 3 is installed:

```
python3 --version
```

2. Clone the repository:

```
git clone https://github.com/knavesec/CredMaster.git
```

3. Set up and activate a Python virtual environment and install dependencies:

```
cd CredMaster/ && python3 -m venv credmaster-env &&  source ./credmaster-env/bin/activate &&  pip install -r requirements.txt
```

## Plugins

CredMaster supports password guessing attacks against a variety of different authentication providers and targets via plugins. This is a brief overview of some of the plugins we commonly use on engagements:

| Plugin Name | Description |
| --- | --- |
| `o365enum` | Enumerates valid O365/Microsoft Online users from a list of potential emails/usernames. Does not make an authentication attempt. |
| `msgraph` | Authenticates to Microsoft Online instances via the Graph API. Can sometimes be used as an Entra ID conditional access bypass. |
| `azuresso` | Authenticates to Entra ID (Microsoft Azure Active Directory). Requires the tenant domain to be passed in with **`--domain`**. |
| `msol` | Authenticates to Microsoft Online and managed O365 instances. Basically, this is the same thing as using `login.microsoftonline.com`. |
| `okta` | Authenticates to a target organization’s Okta login portal. Requires the `--url` flag. |
| `gmailenum` | Enumerates valid GSuite users from a list of potential emails/usernames. Does not make an authentication attempt. |
| `fortinetvpn` | Authenticates to Fortinet VPN instances. Requires the `--url` flag to specify the targeted login portal. |

## Tradecraft

No two organizations are the same, and different targets require different operational considerations. CredMaster has a lot of customization capabilities to allow for the unique goals of each engagement. Here’s a few of the mos...