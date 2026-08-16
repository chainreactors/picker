---
title: The New Blog
url: https://inteltechniques.com/blog/index.html#the-new-blog-content
source: IntelTechniques by Michael Bazzell
date: 2026-08-15
fetch_date: 2026-08-16T02:57:53.194243
---

# The New Blog

[# IntelTechniques](../index.html)

* [Training](../training.html)
* [Services](../services.html)
* [Resources](../links.html)
* [Tools](../tools/index.html)
* [Blog](../blog/)
* [Magazine](https://unredactedmagazine.com)
* [Books](../books.html)
* [Contact](../contact.html)

#### IntelTechniques Blog

---

## The New Blog

August 15, 2026

+

I have hosted a WordPress blog on this site for almost 20 years. I don't any more.

WordPress was great. Type what you want to say; click a few buttons; and poof, your post is available to the world while your RSS feed is auto generated. It was so easy. It also brought a lot of trouble.

Even though we self-hosted the blog, WordPress continued to add various tracking capabilities. We would remove them as they emerged, but tracking was still possible. We try to prevent us from knowing the IP addresses of our visitors whenever possible. This gives you more privacy and us deniability if we were to receive a court order for traffic. The feds were not knocking down our door, but we like to practice what we preach.

We use Cloudflare as our CDN and full caching prevented our web host from receiving the requests for pages. This eliminated both our host and us from seeing your specific traffic and IP address. However, searches on the blog would generate a direct hit to the host and bypass the protection. We disabled search but that did not stop all logging when an un-cached page was accessed.

My main beef with having WordPress on our site was the attacks. Thousands of bots brute-force and scrape WordPress installations looking for content and vulnerabilities. This can result in hundreds of thousands of page loads every day, sometimes millions. Our CDN stops some of it, but most gets by.

I also just don’t like having a large amount of code and a database on my site just to deliver text content and a few images. WordPress is very excessive for our needs. So we killed it. Doing this left us with an entire site existing of only HTML and JS. This allowed us to stop using our web host (Namecheap) and simply cache the static pages on a Cloudflare worker. The entire site is under 100 MB and our old host is no longer logging your activity. Cloudflare is now the only server which can see the data and traffic, and they do not share IP address or traffic logs with us, outside of temporary security logs when attacked. That is not to say THEY don't store the data, but they could do that as our CDN anyway. We have just eliminated one of two middle-men (Namecheap). We updated our Privacy Policy to reflect these new benefits at <https://inteltechniques.com/privacy>.

Today, we offer a pure HTML with Javacript Blog at <https://inteltechniques.com/blog/>. There is no database and all of the content is on a single HTML page. Images only load if you expand a post in order to keep bandwidth down for you and us. We created an RSS feed to continue supplying updates to those who rely on RSS readers for content. We even forward the old feed to the new so that your existing configurations should just work.

We have already posted new content and pruned the old and outdated material so be sure to take a look and subscribe to the RSS feed. We have many big things planned.

## New Firewall Guide

August 15, 2026

+

We have released a brand new Firewall Guide at <https://inteltechniques.com/firewall/>. This guide walks through every step of creating your own pfSense firewall with [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1519) and Wireguard.

## OSINT Tools Update

August 15, 2026

+

We have update our online OSINT Tools at <https://inteltechniques.com/tools/>. They now allow automated query of an X (Twitter) username across XCancel for data retrieval without being logged into a X (Twitter) account including filtration by year.

![](images/xcancel.png)

## Online Training: Updates & Membership Discounts

July 14, 2026

+

Periodically, we like to share some of the tactics, tools, and topics that we’ve been tackling recently in our online training program. If it has been a while since you last visited the training, the summary below will bring you up to speed on what has been added recently. We continue to add new lessons every month, along with the tools, templates, and resources that you have come to expect from your IntelTechniques membership.

We also wanted to remind former training members that, although training costs have risen in recent years, you are always welcome to renew your membership at your original discounted price point. Contact Jason at **[[email protected]](/cdn-cgi/l/email-protection)** directly to reactivate your account or if you have any questions. No chatbots, no AI agents, and no call centers. Laura or I will assist you directly because we think you deserve proper support from real humans.

#### **New Lessons & Updates**

The training currently includes more than 130 hours of video content, 1,000+ pages of digital guides, a custom OSINT virtual machine, specialized scripts, and report templates, with new content added every month. Below is a sample of recent lessons, tools, and resources added to the program and you can view the full curriculum at [inteltechniques.net](https://www.inteltechniques.net/courses/open-source-intelligence).

**Triaging Leads**
Best practices for deciding which leads to pursue early in an investigation, with an optional real-world practical exercise.

**Event Threat Assessments**
A scenario-based lesson on researching events, related issues, and online discussions to support safety planning and tactical decision-making.

**Privacy Assessments**
A workflow for conducting vulnerability assessments on cooperating targets. New Excel and Obsidian templates are provided.

**Developer Tools: Removing Page Elements**
A demonstration on using browser developer tools to remove overlays and reveal hidden page content during online investigations.

**Cultural Intelligence**
Guidance on interpreting interests, beliefs, online behavior, photos, videos, usernames, and cultural context to improve investigative analysis.

**Investigating a Scam Email – Exercise & Demo**
A practical attribution exercise using a real-world scam email, followed by a walkthrough of the investigative workflow.

**Domains, IP Addresses, & DNS**
A foundational overview of how domains, IP addresses, and DNS work in the context of web traffic.

**How Packets Work**
A companion write-up to the Domains, IP Addresses, and DNS lesson, explaining what happens at the packet level when a browser requests a website.

**APIs**
An overview of application programming interfaces appropriate for OSINT work and how to add them to your workflow.

**Due Diligence Reports**
An overview of core components, templates, and best practices for professional due diligence reporting.

**Updated Tools Dashboard**
An updated set of custom OSINT tools available only to training members, including hosted and self-hosted options.

**Client Expectations: Bug Sweep Scenario**
A real-world counter-surveillance scenario used to discuss best practices for managing challenging client expectations.

**Sanctions Evasion Report & Resources**
A sample report and resources focused on business-entity research in the context of a sanctions-evasion investigation.

**Address Verification Demo**
A demonstration combining search engines, people-search results, and government databases to locate and verify a target residential address.

**Premium Breach Data Services**
A comparison spreadsheet covering popular premium breach-data services. This supplements our lesson series on building and self-hosting your own breach-data collections.

**Triaging a Personal Data Security Incident**
Actionable steps to take in the first 24 hours after a cyber incident to stop the bleeding and mitigate damage.

**OSINT Case Study: “Call to Arms”**
This case study was shared by one of our members and walks through their approach to an OSINT investigation.

**Investigative Pivots*...