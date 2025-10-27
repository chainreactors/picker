---
title: Unleash the Power of JS Link Finder: Hunt Hidden Endpoints Like a Pro
url: https://infosecwriteups.com/unleash-the-power-of-js-link-finder-hunt-hidden-endpoints-like-a-pro-deb77530155f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-03
fetch_date: 2025-10-02T19:33:18.329713
---

# Unleash the Power of JS Link Finder: Hunt Hidden Endpoints Like a Pro

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdeb77530155f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funleash-the-power-of-js-link-finder-hunt-hidden-endpoints-like-a-pro-deb77530155f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funleash-the-power-of-js-link-finder-hunt-hidden-endpoints-like-a-pro-deb77530155f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-deb77530155f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-deb77530155f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unleash the Power of JS Link Finder: Hunt Hidden Endpoints Like a Pro

## **Finding JavaScript URLs and Secret Endpoints with Burp Suite’s JS Link Finder Extension**

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--deb77530155f---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--deb77530155f---------------------------------------)

9 min read

·

Sep 2, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

Bug bounty hunting is like being a digital detective, searching for security flaws in websites to keep them safe and earn rewards. One of the most powerful tools in a bug hunter’s toolkit is Burp Suite, and its extensions can supercharge your efforts. Among these, the **JS Link Finder** extension stands out as a game-changer. It scans JavaScript files for URLs and hidden endpoints that could lead to vulnerabilities like exposed APIs, open redirects, or even account takeovers. Whether you’re a beginner or a seasoned hunter, this extension can help you uncover “fishy” endpoints that developers might have overlooked. In this article, we’ll walk you through the full process: from setting up a target in Burp Suite to using JS Link Finder to extract JavaScript URLs and hidden endpoints, and finally checking those endpoints for bugs. Let’s dive into this powerful tool and start hunting like a pro!

## Why JS Link Finder Is a Must-Have for Bug Hunters

Modern websites rely heavily on JavaScript for features like dynamic content, API calls, and user interactions. These JavaScript files often contain URLs or endpoints that aren’t visible on the website’s front end. For example, a file like `service-worker.js` might include API paths or redirect URLs that, if misconfigured, could lead to serious vulnerabilities. Manually searching through these files is time-consuming and easy to miss. That’s where **JS Link Finder**, a Burp Suite extension, shines. It automatically scans JavaScript files for links, endpoints, and parameters, saving you hours of work and helping you find hidden gems like `/api/users` or `/admin` endpoints that could be exploitable.

Here’s why JS Link Finder is so powerful:

* **Passive Scanning**: It analyzes JavaScript files as you browse, without sending extra requests, keeping your testing stealthy.
* **Endpoint Discovery**: Finds URLs and paths (e.g., `/api/v1/config`) that might expose sensitive data or logic.
* **Bug Bounty Friendly**: Helps uncover vulnerabilities like open redirects, broken authentication, or information disclosure, which can lead to big rewards.
* **Beginner-Friendly**: Easy to set up and use, even if you’re new to Burp Suite.

In this guide, we’ll show you how to use JS Link Finder to find these hidden endpoints, step by step, with practical examples inspired by real-world bug bounty reports.

## Prerequisites: What You Need to Get Started

Before we begin, make sure you have the following:

* **Burp Suite Community or Professional Edition**: The free Community Edition works for manual testing, but Professional is better for passive scanning with extensions. Download it from [portswigger.net](https://portswigger.net/burp).
* **JPython Environment**: JS Link Finder requires JPython to run. Download the JPython JAR file from [jython.org](https://www.jython.org/) and set it up in Burp Suite.
* **A Target Website**: Choose a website with a bug bounty program (e.g., on HackerOne or Bugcrowd) and check its scope to ensure subdomains and JavaScript files are included.
* **A Browser**: Configure your browser (e.g., Chrome or Firefox) to use Burp Suite as a proxy.
* **Basic Tools**: A text editor to review findings and a notebook to track your progress.

If you’re new, practice on safe environments like [PortSwigger’s Web Security Academy](https://portswigger.net/web-security) to avoid legal issues.

## Step-by-Step Process: Using JS Link Finder in Burp Suite

Let’s break down the process into clear steps, from setting up your target to finding and testing hidden endpoints with JS Link Finder.

## Step 1: Set Up Your Target in Burp Suite

To use JS Link Finder, you first need to configure Burp Suite to capture traffic from your target website. Here’s how:

1. **Open Burp Suite**: Launch Burp Suite (Community or Professional).
2. **Configure Your Browser**:

* Set your browser to use Burp as a proxy. In Chrome, go to **Settings > System > Open your computer’s proxy settings**, and set the proxy to `127.0.0.1:8080`.
* Install the Burp Suite CA certificate in your browser to avoid SSL errors. In Burp, go to **Proxy > Options > Import/Export CA Certificate** and follow the instructions.

**3. Add the Target to Scope**:

* Go to the **Target > Scope** tab in Burp Suite.
* Click **Add** under the **Target Scope** section.
* Enter the target’s domain (e.g., `example.com`) or specific subdomains (e.g., `dev.example.com`, `api.example.com`). Include `https://` or `http://` as needed.
* For bug bounties, check the program’s scope on HackerOne or Bugcrowd to include only allowed domains.

**4. Turn on Proxy**: In the **Proxy > Proxy Settings** tab, ensure the proxy is running on `127.0.0.1:8080`. Enable **Intercept is on** to capture requests (you can turn it off later for passive scanning).

**5. Browse the Target**: Visit the target website in your browser and interact with it (e.g., log in, click links, submit forms). This populates the **Target > Site map** with URLs and JavaScript files.

## Step 2: Install JS Link Finder Extension

JS Link Finder is available in Burp Suite’s BApp Store. Here’s how to install it:

1. **Open the BApp Store**:

* In Burp Suite, go to the **Extender > BApp Store** tab.

**2. Search for JS Link Finder**:

* Type “JS Link Finder” in the search bar. You’ll see the extensio...