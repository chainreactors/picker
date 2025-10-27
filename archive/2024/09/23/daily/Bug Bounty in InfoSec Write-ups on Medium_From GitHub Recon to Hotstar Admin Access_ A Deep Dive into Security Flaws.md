---
title: From GitHub Recon to Hotstar Admin Access: A Deep Dive into Security Flaws
url: https://infosecwriteups.com/from-github-recon-to-hotstar-admin-access-a-deep-dive-into-security-flaws-2e4ae0ec937e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-23
fetch_date: 2025-10-06T18:22:26.184669
---

# From GitHub Recon to Hotstar Admin Access: A Deep Dive into Security Flaws

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2e4ae0ec937e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-github-recon-to-hotstar-admin-access-a-deep-dive-into-security-flaws-2e4ae0ec937e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-github-recon-to-hotstar-admin-access-a-deep-dive-into-security-flaws-2e4ae0ec937e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2e4ae0ec937e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2e4ae0ec937e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From GitHub Recon to Hotstar Admin Access: A Deep Dive into Security Flaws

## Explore how a basic GitHub search revealed significant security issues in Hotstar’s admin panel. This write-up outlines the flaws discovered and offers guidance on how to address and prevent similar vulnerabilities.

[![Vishal Vishwakarma](https://miro.medium.com/v2/resize:fill:64:64/1*qLGqC7edjHddqB3_NaetRA.jpeg)](https://medium.com/%40rootxvishal?source=post_page---byline--2e4ae0ec937e---------------------------------------)

[Vishal Vishwakarma](https://medium.com/%40rootxvishal?source=post_page---byline--2e4ae0ec937e---------------------------------------)

5 min read

·

Sep 17, 2024

--

3

Listen

Share

Hello Everyone I am Vishal Vishwakarma [@rootxvishal] I hope you enjoy it and learn something new from it.

## **Introduction**

Hotstar, one of India’s leading streaming platforms, has gained immense popularity for its extensive library of movies, TV shows, and live sports. As with many large-scale online services, securing sensitive areas such as admin panels is critical. Recently, I discovered a vulnerability that allowed me to gain unauthorized access to Hotstar’s admin panel using a GitHub dork. In this article, I will guide you through the process of how I identified this vulnerability, from initial reconnaissance to the exploitation phase.

Press enter or click to view image in full size

![]()

## **Subdomain Enumeration**

The first step in my reconnaissance was subdomain enumeration. I used various tools to gather all the subdomains associated with the target website. Subdomain enumeration is crucial for discovering hidden parts of a website that might not be immediately visible.

Here’s a rundown of the tools and commands I used:

1. **Subdomain Discovery Tools**:

* **Subfinder**: A powerful subdomain discovery tool that performs passive reconnaissance.
* **Amass**: A tool designed for advanced network mapping and subdomain enumeration.

Example commands:

```
subfinder -d example.com -o subdomains.txt
amass enum -d example.com -o subdomains.txt
```

2. **Filtering Live Domains**: Once I had a list of subdomains, the next step was to filter out the live domains. I used the following commands to achieve this:

```
cat subdomains.txt | httpx -o urls.txt
cat subdomains.txt | httprobe | sort -u >> list.txt
```

3. **Extracting Useful Information**: With a large number of URLs, I wanted to avoid manually inspecting each one. Instead, I used `httpx` to fetch the titles and status codes of the URLs, which helped me quickly identify interesting targets.

```
cat list.txt | httpx -title -status-code -fr -o result.txt
```

> The result file contained valuable information, such as page titles and HTTP status codes, which made it easier to spot potential login panels or other interesting areas.

## Finding the Admin Panel

Among the various URLs, one page title stood out: “Admin — Log In”. This was a strong indication of an admin panel that could be a potential target. I attempted to bypass the login panel but was met with no success.

Determined, I moved on to fuzzing directories using `ffuf`, but this approach did not uncover any new directories or endpoints. Not ready to give up, I decided to delve into the JavaScript files of the admin panel, searching for hidden secrets or configurations. I utilized tools like TruffleHog and SecretFinder but found nothing of interest.

**Dorking for Hidden Information**

With traditional methods exhausted, I turned to dorking — using specific queries to find hidden information. I used both GitHub and Google dorks, searching for mentions of the admin panel and related data. Some example dorks included:

* org:target
* \*.target.\*
* “site.com” password

These queries led me to several repositories and directories on GitHub where the URL appeared. In one repository, I discovered source code that included development credentials. These credentials were in Base64 encoding, which I decoded using a Base64 decoder tool online.

**Exploiting the Credentials**

With the decoded credentials, which included an email address and password, I attempted to log in to the admin panel. To my astonishment, the login was successful. I found myself in the admin panel, where I had access to various critical functionalities

* **User Management**: Adding and removing users from the platform.
* **Ad Creatives**: Creating, modifying, and deleting advertising content.
* **Billing Details**: Viewing and modifying billing information, including advertiser names.
* **Request Approvals**: Approving or rejecting requests and invoices.

This level of access provided me with complete control over Hotstar’s advertising operations and billing processes, highlighting the critical nature of securing administrative interfaces.

## Impact of the Vulnerability

The impact of this vulnerability is substantial and multifaceted:

1. **Unauthorized Administrative Control:** Attackers gaining admin access can manipulate and control critical aspects of the Hotstar platform, including user accounts and advertising content. This could lead to unauthorized changes that disrupt service and undermine user trust.
2. **Financial Risk:** With access to billing details and financial information, attackers could commit fraud, alter financial records, or mismanage funds, posing a serious financial threat to the company.
3. **Operational Disruption:** The ability to approve or reject requests and invoices without authorization could disrupt business operations, causing delays and potentially affecting revenue streams. This could also harm the company’s operational efficiency.
4. **Data Exposure:** Sensitive data about advertisers and financial transactions could be exposed, risking privacy violations and compromising data integrity. This could damage the company’s reputation and erode customer trust if confidential information is leaked....