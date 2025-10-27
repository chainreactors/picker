---
title: Recon
url: https://infosecwriteups.com/recon-98cf42e60eff?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-11
fetch_date: 2025-10-04T01:12:11.670005
---

# Recon

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F98cf42e60eff&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-98cf42e60eff&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-98cf42e60eff&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-98cf42e60eff---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-98cf42e60eff---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Recon

## The Art of Gathering Information

[![Mukilan Baskaran](https://miro.medium.com/v2/resize:fill:64:64/1*tif1c7lTx883WhLR92OsxA.jpeg)](https://mukibas37.medium.com/?source=post_page---byline--98cf42e60eff---------------------------------------)

[Mukilan Baskaran](https://mukibas37.medium.com/?source=post_page---byline--98cf42e60eff---------------------------------------)

4 min read

·

Nov 29, 2022

--

Listen

Share

The motive of recon is the more you know about your target and the possibility of attack is more.

Press enter or click to view image in full size

![]()

In red team operation, you must know what company you going to gather information from. To gather information there are 2 types of recon one is passive recon and active recon. Passive reconnaissance is about finding information available on the internet. Tools for passive reconnaissance are Google, Shodan, and Wireshark. Active reconnaissance is about finding hidden details by gathering network information. Network information can be gathered through Nmap (Network Mapper). Some of the tools for active recon are Nessus, OpenVas, Nikto, and Metasploit.

### **Objectives of Recon:**

1. Gathering subdomains related target company
2. Collecting public information on the internet such as the hostname and IP address.
3. Finding target email address.
4. Gathering pwned email and passwords
5. Identifying exposed documents and spreadsheets.

### **Types of Recon:**

Let’s discuss the type of recon in detail.

Press enter or click to view image in full size

![]()

Reconnaissance can categorized into 2 types one is passive recon and another is active.

Passive recon doesn’t interact with the target directly. So these don't create much noise.

The best source of passive recon is **google.com.**

**Google Dorks** are the best source of gathering information passively.

**Google Dorks** have queries that can be typed into a google search engine to fine-tune searched results better.

Active recon requires interaction from the target by sending packets to the target and analyzing the packets and how they respond.

### Active recon can be classified into 2 types:

> 1. External Recon - Recon conducted outside the target network.
>
> 2. Internal Recon - Recon conducted within the target network.

### Built-in tools:

Built-in tools such as **whois, dig, nslookup, host, traceroute/tracert.**

The domain registrar is responsible for holding the whois record for domain names it’s leasing.

**Whois command** collects the information and displays the details such as Registrar WHOIS server, Registrar URL, record creation date, record updation date, Registrant contact info, and address. Admin contact info and address. Tech contact info and address.

**The nslookup command** gathers A and AAAA records related to the domain.

**Dig command** gathers information by retrieving DNS server information.

Press enter or click to view image in full size

![]()

**Recon-ng** is a framework that helps in the automation of OSINT work.

Press enter or click to view image in full size

![]()

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

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

**Recon-ng marketplace:**

For marketplace usage, some useful commands are used :

**marketplace search keyword**

**marketplace info module**

**marketplace install module**

**marketplace remove module**

Press enter or click to view image in full size

![]()

You will many subcategories under recon which are **domain companies, domain-contacts, and domain credentials.**

Domain-host provides a module related to hosting that provides a domain.

**Working with installed modules:**

> **marketplace install module**

After the modules get installed we have to set up the modules to load.

![]()

![]()

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

And here is my new blog page which contains tips of cybersecurity

[## @ethicalhacktech8 | YoFan

### Learn to secure and how to safe from attacks.

yo.fan](https://yo.fan/ethicalhacktech8?source=post_page-----98cf42e60eff---------------------------------------)

Support me there also by viewing content

[Recon](https://medium.com/tag/recon?source=post_page-----98cf42e60eff---------------------------------------)

[Information](https://medium.com/tag/information?source=post_page-----98cf42e60eff---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----98cf42e60eff---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----98cf42e60eff---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----98cf42e60eff---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page--...