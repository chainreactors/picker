---
title: Hundreds of companies’ internal data exposed: The Confluence Cloud misconfiguration
url: https://infosecwriteups.com/hundreds-of-companies-internal-data-exposed-the-confluence-cloud-misconfiguration-63cbc143caea?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-04-22
fetch_date: 2025-10-04T11:33:19.708523
---

# Hundreds of companies’ internal data exposed: The Confluence Cloud misconfiguration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F63cbc143caea&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhundreds-of-companies-internal-data-exposed-the-confluence-cloud-misconfiguration-63cbc143caea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhundreds-of-companies-internal-data-exposed-the-confluence-cloud-misconfiguration-63cbc143caea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-63cbc143caea---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-63cbc143caea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hundreds of companies’ internal data exposed: The Confluence Cloud misconfiguration

## One misconfiguration, hundreds of companies, thousands of dollars in bounties

[![Mohammed Moiz Pasha](https://miro.medium.com/v2/resize:fill:64:64/1*qgO3IH-DSXxALEOyJg_caw.png)](https://mopasha17.medium.com/?source=post_page---byline--63cbc143caea---------------------------------------)

[Mohammed Moiz Pasha](https://mopasha17.medium.com/?source=post_page---byline--63cbc143caea---------------------------------------)

5 min read

·

Apr 9, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

Atlassian Confluence is a web-based software application that allows teams to collaborate and share knowledge in a centralized platform. It is used by thousands of organizations for creating, organizing, and sharing documents, meeting notes, project plans, and other types of content.

In this article, I will describe how a misconfiguration in Confluence Cloud caused (and is still causing) the exposure of internal and sensitive information of various organizations and companies. I will also be sharing the results of my research, which uncovered hundreds of companies with the same misconfiguration.

## **The misconfiguration**

Within Confluence, content is organized into spaces. A space is a container for content and collaboration in Confluence. It’s a way to organize related pages, blogs, and other types of content into one location, making it easier to manage and navigate. This allows members to share information, track progress, collaborate on tasks, etc.

Since the information in such spaces can be confidential, each space has permissions which can be assigned and revoked for access control.

Press enter or click to view image in full size

![]()

Source: <https://confluence.atlassian.com/doc/assign-space-permissions-139460.html>

**Here is where the misconfiguration exists.**

For any space, by going to **Space tools** > **Permissions > Edit Permissions** you can choose to allow anonymous users access to the space. This is usually done in order to make the space public (for example, some companies create spaces with support articles which are meant to be available to everyone).

However, in some cases, spaces containing internal information are unintentionally set in such a way that they give anonymous users access to view or edit, making the information public.

**The only thing an attacker needs to do is to visit this URL:**

```
https://<companyname>.atlassian.net/wiki/spaces
```

If there are any spaces open to the public, they will be visible on the landing page.

## Recon

After finding this misconfiguration on one target, I wanted to see just how many companies were affected by this misconfiguration. I created a script in order to automate this process. I also used a few Google dorks for the same:

```
site:"*.atlassian.net" inurl:"/wiki"
```

Press enter or click to view image in full size

![]()

Google dorking

Most of the Google dorks yield false positives (spaces that are intended to be public), but there are a few results which are clearly not meant to be exposed to the public.

## Impact

I combined all the data from my automation and then sifted through it manually.

**The results? Hundreds of companies, from small businesses to MNCs and international organizations, exposing internal information** such as:

* Passwords and working authentication tokens
* Ongoing project data (Project schedules, teams, links to other collaboration tools such as Miro and Figma)
* Employee PII (Names, email addresses, phone numbers)
* Meeting recordings, schedules and timetables
* Employee onboarding and hiring procedures
* Security incident reports
* Personal employee notes
* Detailed description of different protocols (i.e. procedures to be followed during security breaches, etc.)
* …

This misconfiguration was even present in some of the oldest public bug bounty programs on Hackerone, and numerous private programs across different platforms.

Press enter or click to view image in full size

![]()

Confluence spaces exposed on a real target

The results greatly varied. Some of the affected instances leaked information with minimal impact, while others contained access tokens and private keys for organization-wide services. One instance even gave me access to edit and create spaces, which could have caused huge problems if found by an attacker.

Press enter or click to view image in full size

![]()

Pages in a space on a real target

Press enter or click to view image in full size

![]()

Username and password exposed. I also found API tokens, private keys and AWS access keys among others

## Results

After checking if the spaces were not meant to be public, I reported as many findings as I could. **Sadly, many organizations affected do not have a responsible disclosure program.**

I also found this misconfiguration affecting organizations having public or private bug bounty programs. Most of these reports were acknowledged and fixed quickly.

The impact ranged from *Low* to *Critical,* based on the information being disclosed. **Almost all the bug bounty programs I submitted this to were happy to provide a monetary reward, ranging from $250 to $3000 per report.**

There are still hundreds of instances unknowingly being exposed to the public. Like

[Inti De Ceukelaire](https://medium.com/u/f9e27197ffb5?source=post_page---user_mention--63cbc143caea---------------------------------------)

 mentioned in his article about [a similar vulnerability](https://medium.com/%40intideceukelaire/hundreds-of-internal-servicedesks-exposed-due-to-covid-19-ecd0baec87bd),

“Whether you offer rewards for security bugs or not, every company should have a policy and contact for individuals to report security vulnerabilities to them.”

Even something as simple as “security.txt” can help an organization unc...