---
title: Burp Suite Cheatsheet
url: https://www.blackhillsinfosec.com/burp-suite-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:17.650647
---

# Burp Suite Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Brian King](https://www.blackhillsinfosec.com/category/author/brian-king/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Burp Suite](https://www.blackhillsinfosec.com/tag/burp-suite/), [Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [Burp Suite Cheatsheet](https://www.blackhillsinfosec.com/burp-suite-cheatsheet/)

Written by [BB King](https://www.linkedin.com/in/bbhacking) || Reviewed by [Chris Traynor](https://ridgebackinfosec.com/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_4.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**Burp Suite Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_Burp-Suite.pdf)

Find the tool here: <https://portswigger.net/burp>

---

Burp Suite is an intercepting HTTP proxy that can also scan a web-based service for vulnerabilities. A tool like this is indispensable for testing web applications. Burp Suite is written in Java and comes bundled with a JVM, so it works on any operating system you’re likely to use. It comes in a free Community version and a paid-for Professional version. Pro offers more automation and more powerful filters, but Community is enough for CTFs and a good chunk of penetration testing, too.

The “**proxy**” part means that it acts as a pass-through system for network traffic between an HTTP client and an HTTP server. Requests from the client pass through Burp Suite—which usually runs on the same host as the client—before hitting the network, and responses from the server pass through Burp Suite before going to the browser (or any other user agent).

The “**intercepting**” part means that it allows you to hold on to a request (or a response) and inspect or modify it before releasing it on its way.

The “**suite**” part means it does a whole lot more than just intercept HTTP traffic. Burp Suite is made up of a half-dozen or so built-in tools and also supports extensions, of which more than 300 are available for one-click installation via the BApp Store in the Extensions tab.

## Getting Started

The first thing to do with Burp Suite is to just look at some HTTP traffic and see what you can learn by reading what you see. To do this:

* Go to the “Proxy” tab
* Open the “Intercept” sub-tab
* Click “Open browser”

This will launch an embedded Chromium-based browser that is pre-configured to use Burp Suite as its proxy.

In that browser, visit https://example.com/ then come back to Burp Suite and click on the HTTP History tab of the Proxy. Among a few other requests your browser does on its own, you’ll see a “Host” of “https://example.com” and a “Method” of “GET” and a “URL” of “/”. When you select that row, you’ll see the HTTP request and response in the panes below.

Right-click on any request and choose “Send to Repeater” then send the request again from within Repeater. Now modify the request in some way and send it again to see how the server handles different inputs. Start deleting headers until you get an error or a timeout, then try to figure out what caused the difference.

### **Right Click on Everything**

A lot of Burp Suite’s functionality is in the context menus, so it pays to right-click on everything. You may be surprised at what you find. Now, on to the tools in the Suite…

## Proxy

The Proxy History shows all of the traffic that has gone through Burp Suite so far.

* Click on any heading here to sort by that heading. Click again to sort in reverse. Click a third time to go back to unsorted.

* Click and drag the column headings to put them in a different order.

* Scroll all the way to the right to see all the columns and understand what they’re showing you.

* Click on the dark bar above the headings to see the filters available. Better filtering is one of the key benefits of Burp Pro over Community.

* Right-click on any request you see here and choose “Send to Repeater” (or any other tool) and see what you can do with it in that other tool.

* The Inspector shows you information about the request, includin...