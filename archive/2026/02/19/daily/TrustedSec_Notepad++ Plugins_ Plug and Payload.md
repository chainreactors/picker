---
title: Notepad++ Plugins: Plug and Payload
url: https://trustedsec.com/blog/notepad-plugins-plug-and-payload
source: TrustedSec
date: 2026-02-19
fetch_date: 2026-02-20T04:07:51.649325
---

# Notepad++ Plugins: Plug and Payload

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

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
* [Notepad++ Plugins: Plug and Payload](https://trustedsec.com/blog/notepad-plugins-plug-and-payload)

February 19, 2026

# Notepad++ Plugins: Plug and Payload

Written by
Kevin Clark

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/NotepadPluginsPlugPayload_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1771427092&s=6639c582d8b2209431a2f3078b6a64b4)

Table of contents

* [Revisiting Notepad++ Plugins](#Revisiting)
* [A Simple Example](#Simple)
* [A More Complicated Example](#Complicated)
* [Notepad++ Plugin Store](#Plugin)
* [Upgrading PythonScript to Version 3](#PythonScript)
* [The Pip Problem](#Problem)
* [Defensive Measures](#Defensive)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#09367a7c6b636c6a7d344a616c6a622c3b39667c7d2c3b397d61607a2c3b39687b7d606a656c2c3b396f7b66642c3b395d7b7c7a7d6c6d5a6c6a2c3b382f686479326b666d703447667d6c79686d2c3b4b2c3b4b2c3b3959657c6e60677a2c3a482c3b3959657c6e2c3b3968676d2c3b395968706566686d2c3a482c3b39617d7d797a2c3a482c3b4f2c3b4f7d7b7c7a7d6c6d7a6c6a276a66642c3b4f6b65666e2c3b4f67667d6c79686d2479657c6e60677a2479657c6e2468676d247968706566686d "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fnotepad-plugins-plug-and-payload "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Notepad%2B%2B%20Plugins%3A%20Plug%20and%20Payload%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fnotepad-plugins-plug-and-payload "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fnotepad-plugins-plug-and-payload&mini=true "Share on LinkedIn")

Notepad++ has been in the [news recently for a breach](https://notepad-plus-plus.org/news/hijacked-incident-info-update/) of infrastructure associated with the Notepad++ updater. This attack may have allowed an adversary to deliver backdoored updates which could allow arbitrary code execution inside of existing Notepad++ installations. If you have read my other blog posts on [Meterpreter BOFLoader](https://trustedsec.com/blog/operators-guide-to-the-meterpreter-bofloader) and [Offensive Python](https://trustedsec.com/blog/operating-inside-the-interpreted-offensive-python), you will realize I have a fondness for old techniques. Code execution inside of Notepad++ is not new, but many of our clients are either not looking for it or have misguided assumptions about what malicious Notepad++ execution looks like. For these reasons, it seemed fitting to talk about some of the ways we on the Targeted Operations team use Notepad++ during our assessments.

## Revisiting Notepad++ Plugins

Let's go over the basics of Notepad++ plugins. Plugins are simply Windows DLL files stored in a folder inside the Plugins directory. If you used the standard Notepad++ installer, it would be located inside C:\Program Files\Notepad++.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/NotepadPlugins_Clark/Fig01_Clark_NotepadPlug.png?w=320&q=90&auto=format&fit=max&dm=1771360028&s=9e90052164e9e1edab7f821158ce4a48)

Notepad++ in Program Files From Installer

This is important because low-privileged users cannot create files inside of Program Files, including the Notepad++ plugins folder. If not running as administrator, an attacker can do one of two (2) things:

1. Use the portable Notepad++ installer
2. Copy existing Program Files Notepad++ folder to a writable location

For the rest of this blog, I'll be using the portable Notepad++ version. This will allow us to edit plugins just by modifying files inside the plugins folder. First, open the plugins folder to view the currently installed plugins. Notepad++ comes with a few by default.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/NotepadPlugins_Clark/Fig02_Clark_NotepadPlug.png?w=320&q=90&auto=format&fit=max&dm=1771360028&s=f8ecac3364a11aac0f1cf15614986731)

Plugins Folder in Notepad++ Portable Directory

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/NotepadPlugins_Clark/Fig03_Clark_NotepadPlug.png?w=320&q=90&auto=format&fit=max&dm=1771360029&s=6172fc149cfe6f6f1e28466246ab5dd3)

Viewing Default Notepad++ Plugins in Plugins Folder

When started, Notepad++ loads each of the plugins listed in these folders. Functionality is accessible in the plugins tab on the top bar.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/NotepadPlugins_Clark/Fig04_Clark_NotepadPlug.png?w=320&q=90&auto=format&fit=max&dm=1771360030&s=a3b41ce872a16179fd0113b3...