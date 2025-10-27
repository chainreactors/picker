---
title: Recon
url: https://buaq.net/go-139488.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:35.892525
---

# Recon

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Recon

The Art of Gathering InformationThe motive of recon is the more you know about your target and the p
*2022-12-11 01:16:34
Author: [infosecwriteups.com(查看原文)](/jump-139488.htm)
阅读量:17
收藏*

---

## The Art of Gathering Information

The motive of recon is the more you know about your target and the possibility of attack is more.

In red team operation, you must know what company you going to gather information from. To gather information there are 2 types of recon one is passive recon and active recon. Passive reconnaissance is about finding information available on the internet. Tools for passive reconnaissance are Google, Shodan, and Wireshark. Active reconnaissance is about finding hidden details by gathering network information. Network information can be gathered through Nmap (Network Mapper). Some of the tools for active recon are Nessus, OpenVas, Nikto, and Metasploit.

## **Objectives of Recon:**

1. Gathering subdomains related target company
2. Collecting public information on the internet such as the hostname and IP address.
3. Finding target email address.
4. Gathering pwned email and passwords
5. Identifying exposed documents and spreadsheets.

## **Types of Recon:**

Let’s discuss the type of recon in detail.

Reconnaissance can categorized into 2 types one is passive recon and another is active.

Passive recon doesn’t interact with the target directly. So these don't create much noise.

The best source of passive recon is **google.com.**

**Google Dorks** are the best source of gathering information passively.

**Google Dorks** have queries that can be typed into a google search engine to fine-tune searched results better.

Active recon requires interaction from the target by sending packets to the target and analyzing the packets and how they respond.

## Active recon can be classified into 2 types:

> 1. External Recon - Recon conducted outside the target network.
>
> 2. Internal Recon - Recon conducted within the target network.

## Built-in tools:

Built-in tools such as **whois, dig, nslookup, host, traceroute/tracert.**

The domain registrar is responsible for holding the whois record for domain names it’s leasing.

**Whois command** collects the information and displays the details such as Registrar WHOIS server, Registrar URL, record creation date, record updation date, Registrant contact info, and address. Admin contact info and address. Tech contact info and address.

**The nslookup command** gathers A and AAAA records related to the domain.

**Dig command** gathers information by retrieving DNS server information.

**Recon-ng** is a framework that helps in the automation of OSINT work.

All data collected or gathered will automatically be saved in the database.

To get started in **Recon-ng,** just type recon-ng in the terminal.

In order to run the scan you need to install the module

The workflow is required to install the module.

1. Create a workspace for your project.
2. Insert the starting information into the database.
3. Search the marketplace for a module and learn about it before installing it.
4. List the installed module and load one
5. Run the loaded one.

**Creating Workspace:**

Run **workspaces create WORKSPACE\_NAME (workspaces create threatteam)** to create a new workspace for your investigation. For example,

> **workspace create threatteam**

will create a workspace named **threatteam**.

To perform recon-ng against the workspace type

**recon-ng -w threatteam** which starts recon-ng with specified workspace.

**Recon-ng marketplace:**

For marketplace usage, some useful commands are used :

**marketplace search keyword**

**marketplace info module**

**marketplace install module**

**marketplace remove module**

You will many subcategories under recon which are **domain companies, domain-contacts, and domain credentials.**

Domain-host provides a module related to hosting that provides a domain.

**Working with installed modules:**

> **marketplace install module**

After the modules get installed we have to set up the modules to load.

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/recon-98cf42e60eff?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)