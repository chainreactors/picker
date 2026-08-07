---
title: The Art of Hunting Azure Cloud Secrets
url: https://trustedsec.com/blog/the-art-of-hunting-azure-cloud-secrets
source: TrustedSec
date: 2026-08-06
fetch_date: 2026-08-07T04:27:08.839527
---

# The Art of Hunting Azure Cloud Secrets

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [The Art of Hunting Azure Cloud Secrets](https://trustedsec.com/blog/the-art-of-hunting-azure-cloud-secrets)

August 06, 2026

# The Art of Hunting Azure Cloud Secrets

Written by
Edwin David

Cloud Penetration Testing
Demo

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/TheArtOfHuntingAzureCloudSecrets_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1785349177&s=58ca3c71586569380e3c1025c4b4eba4)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#67581412050d0204135a240f02040c425557081213425557130f0e144255570615130e040b024255570115080a4255573315121413020334020442555641060a175c0508031e5a330f0242555726151342555708014255572f1209130e0900425557261d121502425557240b081203425557340204150213144254264255570f13131714425426425521425521131512141302031402044904080a425521050b0800425521130f024a0615134a08014a0f1209130e09004a061d1215024a040b0812034a14020415021314 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-art-of-hunting-azure-cloud-secrets "Share on Facebook")
* [Share on X](https://twitter.com/share?text=The%20Art%20of%20Hunting%20Azure%20Cloud%20Secrets%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-art-of-hunting-azure-cloud-secrets "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-art-of-hunting-azure-cloud-secrets&mini=true "Share on LinkedIn")

Finding secrets in the cloud is what can turn a normal cloud test into a privilege escalation game changer. The approach to finding secrets is what may separate your next cloud penetration test from a finding expedition into a subscription or global administrative takeover.

In this blog, I am going to introduce two tools that I am making public. The purpose of each tool is to minimize your time looking for secrets in Azure that probably should not be there.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingAzure_Edwin/FigA_Edwin_HuntingAzure.jpg?w=320&q=90&auto=format&fit=max&dm=1785512902&s=252f518719906114afcc089f6fb36b9a)

Microburst, a public tool made by NetSPI, allows you to enumerate Azure Assets using an authenticated account in Azure. To get the maximum benefit out of tools such as Microburst, subscription reader access is normally recommended prior to running. Microburst can be found at the following GitHub URL: <https://github.com/Netspi/Microburst>

Once collection is finished, penetration testers will typically pivot to the data and pull secrets that may be stored in logic applications, VM extensions, automation accounts, and Azure resource deployment logs. The downside is that these actions require time and, in larger environments, you could inadvertently miss some secrets that could gain you privilege escalation in the cloud.

I had AI assist me into building a fully functional toolset that would search for secrets collected by Microburst. You don’t need something powerful like Claude Mythos to come up with these actions. You just need to plan how you want to build it, ask the right questions, do code review, and ensure you are not introducing a tool that may produce several false positives. Microburst Secrets Hunter is meant to be a companion post exploitation tool to Microburst collection. It is done entirely offline using the data that was collected during Microburst enumeration. I have also included actional reporting with redactions that you can easily import into reporting tools with very little effort.

Microburst Secrets Hunter can be downloaded at the following GitHub URL: <https://github.com/rootsecdev/MicroburstSecretsHunter>

This blog would not be complete without a demonstration. To protect any guilty cloud environments, I have made a sample pack of tests that are comparable to output produced by Microburst. This will give basic command use syntax and how the sample output looks.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HuntingAzure_Edwin/FigB_Edwin_HuntingAzure.jpg?w=320&q=90&auto=format&fit=max&dm=1785512986&s=0d3f7c3d937ef06db1c2fcdc369bec1a)

I have added two separate options for usage depending on the environment you are operating in and how paranoid you are when importing modules versus running PowerShell directly.

Sample usage:

```
# Clone / copy this folder, then from a PowerShell prompt:
.\Scan-MicroBurst.ps1 -Path .\MicroBurst-2026 -Verbose
```

```
#Import Module and use cmdlet directly
Import-Module .\MicroBurstSecretsHunter.psd1 -Force
Invoke-MBSecretScan -Path .\MicroBurst-2026
```

By default, all scans are redacted for reporting purposes. There is a switch you can use that will export full unredacted secrets data if you choose to do so.

Sample Syntax to export redacted secrets:

```
.\Scan-...