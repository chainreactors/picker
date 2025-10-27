---
title: Sowing Chaos and Reaping Rewards in Confluence and Jira
url: https://posts.specterops.io/sowing-chaos-and-reaping-rewards-in-confluence-and-jira-7a90ba33bf62?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-06-29
fetch_date: 2025-10-04T11:49:18.310228
---

# Sowing Chaos and Reaping Rewards in Confluence and Jira

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7a90ba33bf62&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fsowing-chaos-and-reaping-rewards-in-confluence-and-jira-7a90ba33bf62&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fsowing-chaos-and-reaping-rewards-in-confluence-and-jira-7a90ba33bf62&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-7a90ba33bf62---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-7a90ba33bf62---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Sowing Chaos and Reaping Rewards in Confluence and Jira

[![Craig Wright](https://miro.medium.com/v2/resize:fill:64:64/1*PyhXJhWAcOy99oNLa-ALwQ.png)](https://medium.com/%40werdhaihai?source=post_page---byline--7a90ba33bf62---------------------------------------)

[Craig Wright](https://medium.com/%40werdhaihai?source=post_page---byline--7a90ba33bf62---------------------------------------)

9 min read

·

Jun 28, 2023

--

Listen

Share

## Introduction

Let me paint a picture for you. You’re on a red team operation, operating from your favorite C2, and have just landed on a user’s workstation. You decide to take a look at their DNS cache to get a list of internal resources the user has been browsing and as you look through the list, there are several that you recognize based on naming conventions. One in particular might be interesting: ***Atlassian***. What do you do next? Do you immediately sleep your Beacon down to 0 and SOCKS proxy in browser traffic? No way. You have options!

## TL;DR

I have created a new .NET tool named ***AtlasReaper*** that calls the Atlassian REST APIs for Confluence and Jira. It is designed to run in-memory from C2 agents, with the aim of minimizing the network overhead generated from a SOCKS proxy. This tool has several features, including listing spaces, pages, attachments, projects, issues (and comments), usernames, and emails, and has the ability to search by a provided keyword. I have also included some features for adding content to pages and issues.

<https://github.com/werdhaihai/AtlasReaper>

## Why??

As red teamers, we are often asked to perform the relatively mundane task of triaging local and remote file systems or other information systems such as Confluence and Jira. This can be both time-consuming and tedious. Why do we do boring stuff, then? Because it’s usually fruitful! If you create a system and it accepts files or text, people will put their passwords or sensitive customer information posthaste. This is something adversaries use to their advantage.

![]()

There are other tools, like [conf-thief](https://github.com/antman1p/Conf-Thief) and [jecretz](https://github.com/sahadnk72/jecretz), that solve the problem of searching through Confluence and Jira, but I couldn’t find a tool that did both or a tool that had all of the features I wanted. My aim was to build a tool that could quickly interact with Confluence and Jira via C2. I also wanted to make use of the very “fun” Confluence Query Language and Jira Query Language with “fuzzy” searching. I needed the ability to view spaces, pages, and issues individually, dump everything at once to the console, or save the output to a file. I also felt there could be value in attaching files, commenting, and mentioning other users on pages and issues.

## Overview of Confluence and Jira

A full explanation of all of the features of Confluence and Jira is outside the scope of this blog post; however, I wanted to briefly provide a breakdown of the structure of each of these applications.

Confluence is basically a wiki for companies. Confluence uses spaces to logically separate or group information. Spaces are often broken down by department (e.g. Finance, HR, IT, etc) and can contain pages. The latter is where users put text, tables, attachments, and so on. The breakdown in a tree structure looks something like this:

```
GLOBAL CORP CONFLUENCE INSTANCE
├───Finance (Space)
│   ├───2023 Annuals (Page)
│   └───SWIFT Account (Page)
├───HR (Space)
│   ├───Internal Systems (Page)
│   └───Training and Development (Page)
└───IT (Space)
    ├───Cloud Infrastructure (Page)
    ├───New-Hire Onboarding (Page)
    └───Software Licenses (Page)
```

Jira is an issue and project tracking software. Jira is broken down into projects, and projects are broken down further into issues. Issues can be used in various ways; for instance, I have seen them used as a way to track individual tasks, IT help tickets, and even findings and security issues discovered in past penetration test reports.😈

Jira breakdown:

```
GLOBAL CORP JIRA INSTANCE
├───Dev (Project)
│   ├───DEV30 - Convert All Codebases to COBOL (Issue)
│   └───DEV61 - Implement New Feature Request (Issue)
├───IT (Project)
│   ├───IT849 - Server Maintenance (Issue)
│   └───IT9999999 - Password Reset for David (Issue)
└───SEC (Project)
    ├───SEC105 - Security Incident Response (Issue)
    └───SEC99 - SQL Injection Everywhere! (Issue)
```

## Introducing AtlasReaper

Atlassian is pushing users from on-premises to cloud versions of these services; as such, the tool is designed to work with cloud versions. The cloud versions of these applications use the same session token, named ***cloud.session.token*** . Oftentimes, Confluence and Jira will be accessible to anonymous users (“It’s secure! They’d have to be on the VPN to access it”). Try running the tool without the ***-c*** or ***— cookie*** flag. Otherwise, you’ll need to dump the session token from the user’s browser.

AtlasReaper includes two commands, ***confluence*** and ***jira***:

```
.\AtlasReaper.exe

                                                   .@@@@
                                               @@@@@
                                            @@@@@   @@@@@@@
                                          @@@@@   @@@@@@@@@@@
                                         @@@@@  @@@@@@@@@@@@@@@
                                        @@@@,  @@@@        *@@@@
                                          @@@@ @@@  @@  @@@ .@@@
   _  _   _         ___                       @@@@@@@     @@@@@@
  /_\| |_| |__ _ __| _ \___ __ _ _ __  ___ _ _   @@   @@@@@@@@
 / _ \  _| / _` (_-<   / -_) _` | '_ \/ -_) '_|  @@   @@@@@@@@
/_/ \_\__|_\__,_/__/_|_\___\__,_| .__/\___|_|    @@@@@@@@   &@
                                |_|             @@@@@@@@@@  @@&
                                                @@@@@@@@@@@@@@@@@
                                               @@@@@@@@@@@@@@@@. @@
                                                  @werdhaihai

Available commands:

    confluence       - query confluence
    jira             - query jira
``...