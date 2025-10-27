---
title: Server-Side Prototype Pollution Scanner
url: https://portswigger.net/blog/server-side-prototype-pollution-scanner
source: PortSwigger Blog
date: 2023-03-14
fetch_date: 2025-10-04T09:30:22.541234
---

# Server-Side Prototype Pollution Scanner

[**Your agentic AI partner in Burp Suite - Discover Burp AI now**

**Read more**](https://portswigger.net/burp/ai)

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# Server-Side Prototype Pollution Scanner

[ ]

Gareth Heyes |
13 March 2023 at 15:00 UTC

[server-side prototype pollution](/blog/server-side-prototype-pollution)
[scanning](/blog/scanning)
[black-box](/blog/black-box)

![An illustration of a guy in a suit with a gadget to detect pollution and some water with prototype pollution vectors in](/cms/images/65/4c/b758-article-prototype_pollution_hunting_blog-article.png)

We recently published some research on [server-side prototype pollution](https://portswigger.net/research/server-side-prototype-pollution) where we went into detail on techniques for detecting this vulnerability black-box. To make your life easier, we've integrated these techniques into an automated, open source tool called [Server-Side Prototype Pollution Scanner](https://portswigger.net/bappstore/c1d4bd60626d4178a54d36ee802cf7e8). In this post, we'll walk you through how to use this tool to exploit the Web Security Academy lab [privilege escalation via server-side prototype pollution](https://portswigger.net/web-security/prototype-pollution/server-side/lab-privilege-escalation-via-server-side-prototype-pollution).

## Installation

To install the Server-Side [Prototype Pollution](/web-security/prototype-pollution) Scanner:

1. In Burp, go to the  **Extensions > BApp Store**  tab.
2. From the list of extensions, select Server-Side Prototype Pollution Scanner.
3. Click Install.

The Server-Side Prototype Pollution Scanner now appears on the **Extensions > Installed** tab, where you can enable and disable it as needed.

![Screenshot showing the BApp store with the prototype pollution scanner selected](/cms/images/09/fc/dbf9-article-bapp-store-prototype-pollution-scanner-install.png)

## Using the Server-Side Prototype Pollution Scanner

Now that we've got the BApp installed we need something to test it on. Let's walk through the process using one of the deliberately vulnerable labs from the Web Security Academy.

To follow this tutorial, you need to create a free account on [portswigger.net](https://portswigger.net/users/register).

### Launch the lab

1. In Burp, go to the **Proxy > Intercept** tab.
2. Click **Open browser** to launch Burp's built-in browser.
3. In Burp's browser, go to the following URL:
 <https://portswigger.net/web-security/prototype-pollution/server-side/lab-privilege-escalation-via-server-side-prototype-pollution>
4. Click **Access the lab**, then log in if prompted. After a short pause, the deliberately vulnerable online store opens.

### Map the target

1. In Burp, go to the **Target > Site map** tab.
2. From the list of hosts, right-click on the top-level entry for the lab and select **Add to scope**.
3. In the browser, go back to the lab and click **My account**.
4. When prompted, log in using the following credentials:

Username: **wiener**
Password: **peter**

5. Manually explore the lab. In particular, investigate the function for changing your delivery address. This accumulates a log of HTTP interactions in Burp, which we'll later use to scan for prototype pollution.

### Scan for server-side prototype pollution

1. In Burp, go to the **Proxy > HTTP history** tab.
2. Above the list of HTTP interactions, click the **Filter:** bar to open the filter settings.
3. In the filter settings, select **Show only in-scope items** then click **Apply**.
4. Select all of the items in the proxy history. Due to the filter we applied, this should only contain HTTP interactions with the lab. This is important to ensure that we don't accidentally scan any unrelated sites that are out of scope.
5. Right-click on the selected interactions and select **Extensions > Server-Side Prototype Pollution Scanner > Server-Side Prototype Pollution > Body scan**.

![Context menu showing the various scan options](/cms/images/0a/2c/45c0-article-scan-context-menu.png)

6. When prompted, click **OK** to accept the default settings. The scan begins probing for prototype pollution using any request that contains a JSON body.

### Check the results

The results of the scan are reported in different locations depending on whether you're using [Burp Suite Professional](/burp/pro) or [Burp Suite Community Edition](/burp/communitydownload). The following steps assume you're using Burp Suite Professional.

1. On the **Dashboard** tab, go to the **Issue Activity** tab.
2. Notice that this contains three new issues related to server-side prototype pollution.
3. Select the issue **Server-side prototype pollution via JSON spacing**.
4. Observe that the issue provides several requests and responses as evidence:

* The first request is the unmodified base request where the vulnerability was found.
* In the second request, notice that the scanner attempted ...