---
title: How I Found a Data Deletion Bypass via Subdomain Synchronization
url: https://infosecwriteups.com/how-i-found-a-data-deletion-bypass-via-subdomain-synchronization-7f5a43079983?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-06
fetch_date: 2026-07-07T06:03:29.426091
---

# How I Found a Data Deletion Bypass via Subdomain Synchronization

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-data-deletion-bypass-via-subdomain-synchronization-7f5a43079983&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-data-deletion-bypass-via-subdomain-synchronization-7f5a43079983&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7f5a43079983---------------------------------------)

·

1. [🙌🏻Introduction](/?source=post_page-----7f5a43079983---------------------------------------#a850 "🙌🏻Introduction")
2. [🏗️ Architecture & Application Flow](/?source=post_page-----7f5a43079983---------------------------------------#2248 "🏗️ Architecture & Application Flow")
3. [🧑‍🏫Understanding the target (account.redacted.com)](/?source=post_page-----7f5a43079983---------------------------------------#090b "🧑‍🏫Understanding the target (account.redacted.com)")
4. [🧑‍🏫Understanding the target (todo.redacted.com)](/?source=post_page-----7f5a43079983---------------------------------------#fb94 "🧑‍🏫Understanding the target (todo.redacted.com)")
5. [🧠 The Thought That Led to the Bug](/?source=post_page-----7f5a43079983---------------------------------------#9cc7 "🧠 The Thought That Led to the Bug")
6. [🔍 What I Found in the Real Case](/?source=post_page-----7f5a43079983---------------------------------------#9ccb "🔍 What I Found in the Real Case")
7. [💥 Impact](/?source=post_page-----7f5a43079983---------------------------------------#cd0c "💥 Impact")
8. [🤔What I Expected vs What Happened](/?source=post_page-----7f5a43079983---------------------------------------#dcbe "🤔What I Expected vs What Happened")
9. [Expected](/?source=post_page-----7f5a43079983---------------------------------------#f696 "Expected")
10. [Actual](/?source=post_page-----7f5a43079983---------------------------------------#ec44 "Actual")
11. [🕛Timeline](/?source=post_page-----7f5a43079983---------------------------------------#bbb3 "🕛Timeline")
12. [🤔Root Cause](/?source=post_page-----7f5a43079983---------------------------------------#3e31 "🤔Root Cause")
13. [🔚Conclusion](/?source=post_page-----7f5a43079983---------------------------------------#ee89 "🔚Conclusion")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7f5a43079983---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Found a Data Deletion Bypass via Subdomain Synchronization

[![Viperblitzz](https://miro.medium.com/v2/resize:fill:64:64/1*C0LbRx6HoqGgkKyUmc2osw.jpeg)](https://medium.com/%40viperblitzz?source=post_page---byline--7f5a43079983---------------------------------------)

[Viperblitzz](https://medium.com/%40viperblitzz?source=post_page---byline--7f5a43079983---------------------------------------)

4 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D7f5a43079983&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-data-deletion-bypass-via-subdomain-synchronization-7f5a43079983&source=---header_actions--7f5a43079983---------------------post_audio_button------------------)

Share

This is what I did after my lunch break and immediately got enough cash to buy stuff in the premium store

Press enter or click to view image in full size

![]()

## 🙌🏻Introduction

Hello everyone! Shortly after my lunch break one afternoon, I accidentally discovered a quite serious business logic errors vulnerability. This flaw enabled a user with a **Moderator** role to delete an entire organizational group simply by visiting the group settings. Naturally, such a destructive action should strictly be restricted to users with **Admin** or **Owner** privileges.

In appreciation of the report, the security team provided a a fairly attractive cash reward. To give you an idea, if you live in a major capital city, the bounty is more than enough to fund a premium retail shopping spree.

Interestingly, this finding did not involve any advanced hacking techniques, sophisticated tools, or magical payloads.

**There is only one key**

> High curiosity supported by a deep understanding of how the application workflow operates.

## 🏗️ Architecture & Application Flow

I discovered this vulnerability in a *self-hosted* bug bounty program with a fairly broad scope. After thoroughly reviewing the program rules, my first step was to perform subdomain enumeration using a mix of online tools and command-line utilities like [VirusTotal](https://www.virustotal.com/gui/home/search) , [Subfinder](https://subdomainfinder.c99.nl/), [redlimit](https://tools.redlimit.id/) and similar asset discovery tools.

After filtering the *scanning* results, one particular subdomain caught my attention`todo.redacted.com`. The application functions as an activity scheduler designed to boost daily user productivity. Without hesitation, I decided to dive deep into it mapping out the application flow and studying the developer documentation to understand all the available features.

The authentication architecture had an interesting twist. To use `todo.redacted.com`, new users had to sign up first. However, the registration process redirected users to a completely separate subdomain `account.redacted.com`. Only after successfully creating an account on the ***account*** subdomain could a user log back in and access the ***todo***platform.

**Looking at this architectural setup, a hypothesis immediately came to my mind:**

> These two subdomains exchange data in the same database without any process isolation (separation). This means that any configuration errors in the account subdomain will affect the todo subdomain.

**So, how did I confirm it?**

It was surprisingly simple. When a primary user creates an organization and invites a second user via the `account.redacted.com` dashboard, the changes automatically sync the moment the primary user opens `todo.redacted.com`. The newly created organization and its invited members instantly populate on the *todo* subdomain.

## 🧑‍🏫Understanding the target (account.redacted.com)

The `account.redacted.com` subdomain serves specifically as the **central hub** for account setting, group creation, and member management.

The most interesting component to audit here was the **group member management feature**. Within this feature, the system implements a Role-Based Access Control (RBAC) model with three distinct privilege levels:

* **Owner / Admin (Full Access):** Holds the highest level of control. They can create groups, invite new members, edit group profiles, remove members, ...