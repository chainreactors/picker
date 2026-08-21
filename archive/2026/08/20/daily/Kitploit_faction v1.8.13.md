---
title: faction v1.8.13
url: https://kitploit.com/en/posts/github-factionsecurity-faction-1813
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:02:44.633589
---

# faction v1.8.13

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/6545/3c68861944a65908816c4021a60ad058e35efc02221f72a9ca2994860691c91f.png)

New releaseAug 20, 2026

# faction v1.8.13

Pen Test Report Generation and Assessment Collaboration

Share

# OWASP - FACTION PenTesting Report Generation and Collaboration Framework

![GitHub last commit](https://img.shields.io/github/last-commit/factionsecurity/faction) ![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/factionsecurity/faction) [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10120/badge)](https://www.bestpractices.dev/projects/10120)

[![](https://img.shields.io/badge/null0perat0r-it?style=flat-square&logo=mastodon&labelColor=white&color=white&link=https://infosec.exchange/@null0perat0r)](https://infosec.exchange/%40null0perat0r)
[![Bluesky](https://img.shields.io/badge/Bluesky-0285FF?logo=bluesky&logoColor=fff)](https://bsky.app/profile/factionsecurity.com)

***Faction is now an OWASP Project! You can find more information [here](https://owasp.org/www-project-faction/)***

![image](https://assets.kitploit.com/production/public/readmes/6545/01ea3bf743672186dd6ffdc6daf406aa0d9efdac28d390dbab0a9f67158e7459.png)

## Sponsors

### Premium Sponsors

|  |  |
| --- | --- |
| [![](https://assets.kitploit.com/production/public/readmes/6545/bb9d82c0c6d375eb4776cdb24a3f4c433f1bb13ce65120f54998f6e3d499ff97.jpg)](https://www.otto-js.com) [otto-js - PCI and Client Side Security](https://www.otto-js.com) | [![SecNinjaz Technologies LLP](https://raw.githubusercontent.com/factionsecurity/faction/HEAD/backers/Secninjaz+Logo+with+outline+01.svg)](https://secninjaz.com/) [Secninjaz Technologies LLP](https://secninjaz.com/) |

### Become a Sponsor ❤️

If you like the project and would like to see it advance then consider being a sponsor. All sponsors get access to the Faction discord server and will have bug reports prioritized. Just click the sponsor links at the top of this repo or contact us at info[at]factionsecurity.com

### Community, Getting Involved, and Updates

[Join the OWASP Slack Community](https://owasp.org/slack/invite) and and follow #project-faction! Be sure to follow us on [BlueSky](https://bsky.app/profile/factionsecurity.com) and our [Blog](https://medium.com/%40we-are-faction) to get the latest updates.

### Contributing

Please see our [contributing guidelines](https://github.com/factionsecurity/faction/blob/HEAD/CONTRIBUTING.md) for details and standards on contributing before considering or submitting a pull request.

# Introduction

FACTION is your entire assessment workflow in a box. With FACTION you can:

1. Automate pen testing and security assessment Reports
2. Peer review and track changes for reports
3. Create customized DOCX templates for different assessment types and retests
4. Real-time collaboration with assessors via the web app and [Burp Suite Extensions](https://github.com/factionsecurity/Faction-Burp)
5. Customizable vulnerability templates with over 75 prepopulated
6. Easily manage assessment teams and track progress across your organization
7. Track vulnerability remediation efforts with custom SLA warnings and alerts
8. Full Rest API to integrate with other tools

Other Features:

1. LDAP Integration
2. OAUTH2.0 Integration
3. SMTP integration
4. Extendable with Custom Plugins similar to Burp Extender.
5. Custom Report Variables

**Want to see it in action?** -> [Faction YouTube Channel](https://www.youtube.com/%40factionsecurity/videos)

## Quick Setup

**Requirements**

* Java JDK11
* Maven (for building the project)
* (Optional for VM). Mongo DB requires a CPU with AVX support. You may run into this issue if using [Oracle Virtual](https://www.mongodb.com/community/forums/t/could-not-start-mongodb-5-0-running-oracle-linux-on-virtualbox/120524/10) Box or [Kubernetes](https://stackoverflow.com/questions/70818543/mongo-db-deployment-not-working-in-kubernetes-because-processor-doesnt-have-avx)

Run the following commands to build the war file and deploy it to the docker container.

root@kitploit:~

```
git clone [email protected]:factionsecurity/faction.git
cd faction
docker-compose up --build
```

Once the containers are up you can navigate to <http://127.0.0.1:8080> to access your FACTION instance.
On the first boot, it will ask you to create an admin account.

## Import the Vulnerability Templates

1. Navigate to Templates -> Default Vulnerabilities
2. Click Update from Faction.

## Customize reports

You can find out more information about creating your own custom report templates here:
[Custom Security Report Templates - Faction Security](https://docs.factionsecurity.com/Custom%20Security%20Report%20Templates/)

## Burp Suite Extension

[Burp Suite Extensions](https://github.com/factionsecurity/Faction-Burp)

## Manuals and Tutorials

[Manual](https://docs.factionsecurity.com/)

## Don't want to host it yourself?

We can provide hosting for your instance. All instances are single tenants so you don't have to worry about sharing infrastructure with untrusted parties. Navigate to [https://www.factionsecurity.com to learn more](https://www.factionsecurity.com).

## Screenshots

**Vulnerability Templates**
![image](https://assets.kitploit.com/production/public/readmes/6545/1257b669a02a4390e78227ece20c53ef1175076099050b5517a60aff40767f1e.png)

**Assessment Scheduling**
![image](https://assets.kitploit.com/production/public/readmes/6545/37579bdc2814228e98026c719a878fe2b83b18eed9c659e9484c58cc9e2efa9d.png)

**Peer Review and Track Changes**
![image](https://assets.kitploit.com/production/public/readmes/6545/c050ca3fe50dcaab00dd9b14bc7ec8a3babd75792f4d46b2a796a38c7f7bc4dc.png)

**Remediation/Retest Queue**
![image](https://assets.kitploit.com/production/public/readmes/6545/ab89d48e953a164d0eadb11b524a8065ef952114a22c27cfbbeb02d9b785cacf.png)

**Schedule Retests**
![image](https://assets.kitploit.com/production/public/readmes/6545/d693774fa01cd1d47b96be3ccc6be4e930bd10e96cf002c3d6e19ddb59125b0d.png)

**Assessor Retest Interface**
![image](https://assets.kitploit.com/production/public/readmes/6545/3c68861944a65908816c4021a60ad058e35efc02221f72a9ca2994860691c91f.png)

**Vulnerability Status Tracking**
![image](https://assets.kitploit.com/production/public/readmes/6545/106adae46dae56ede1bd1478cb357ab89e489a0fd5bbe2eaea9cfac368738a4e.png)

# 1.2 Release Updates

Faction 1.2 introduces the App Store! The Faction App Store will make it easier for developers to extend faction. Faction Extensions can be used to trigger custom code when certain events happen in your workflow like sending all vulnerbilities to Jira when the assessment is complete or update a tracking system when retests pass or fail. More information can be found in the [documentation site](https://docs.factionsecurity.com).

### ⭐️ Jira Integration and AppStore Dashboard

![image](https://assets.kitploit.com/production/public/readmes/6545/18fd2b24bde04ffdb05b1528519e5809b3dc047a0f99047d2b8a3c571587e5e5.png)

Note you can reorder extensions so that updates for one can affect updates to the next.

### ⭐️ Extensions for Custom Graphics

Extensions will also allow custom bar charts to your reports:
![image](https://assets.kitploit.com/production/public/readmes/6545/5ee9b6c403473ed1107c0a8e728d6d56ef3e149f939455aa616d4301875f4153.png)

Generated report with graphics:
![image](https://assets.kitploit.com/production/public/readmes/6545/2c03001c438622375418b5808d9d75c6a1bba87931869f8711cf82e7debc17a9.png)

[Read more](/en/tools/github/factionsecurity/faction?expand=1)

## Categories

[Penetration Testing Frameworks](/en/categories/penetration-testi...