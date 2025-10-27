---
title: Pwn2Own Returns to Miami Beach for 2023
url: https://buaq.net/go-138130.html
source: unSafe.sh - 不安全
date: 2022-12-02
fetch_date: 2025-10-04T00:15:46.302117
---

# Pwn2Own Returns to Miami Beach for 2023

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

Pwn2Own Returns to Miami Beach for 2023

¡Bienvenidos de nuevo a Miami!Even as we make our final preparations for our consumer-focused cont
*2022-12-1 22:32:46
Author: [www.thezdi.com(查看原文)](/jump-138130.htm)
阅读量:22
收藏*

---

¡Bienvenidos de nuevo a Miami!

Even as we make our final preparations for our consumer-focused contest in [Toronto](https://www.zerodayinitiative.com/blog/2022/8/29/announcing-pwn2own-toronto-2022-and-introducing-the-soho-smashup), we’re already looking ahead to warmer climes and returning to the [S4 Conference](https://s4xevents.com/) in Miami for our ICS/SCADA-themed event. Pwn2Own returns to South Beach on February 14-16, 2023, and for this year’s event, we’ve refined our target list to include the latest trends in the ICS world. As we did last year, we’ll have contestants both ***in person*** and around the world demonstrating the latest exploits on OPC Unified Architecture (OPC UA) Servers, OPC UA Clients, Data Gateways, and Edge systems.

Our inaugural Pwn2Own Miami was held back in January 2020 at the S4 Conference, and we had a fantastic time as we awarded over $280,000 USD in cash and prizes for 24 unique 0-day vulnerabilities. [Last year](https://www.zerodayinitiative.com/blog/2022/4/14/pwn2own-miami-2022-results), we awarded $400,000 for 26 unique 0-days (plus a few bug collisions). At that event, we crowned Daan Keuper ([@daankeuper](https://www.twitter.com/daankeuper)) and Thijs Alkemade ([@xnyhps](https://www.twitter.com/xnyhps)) from Computest Sector 7 ([@sector7\_nl](https://www.twitter.com/sector7_nl)) Master of Pwn for their multiple successful exploits. We’ll see if they return in 2023 to defend their crown.

This contest is not possible without the participation and help of our partners within the ICS community, and we would like to especially thank the folks at the OPC Foundation and AVEVA for their expertise and guidance. The cooperation of those within the ICS/SCADA community is essential in ensuring we have the right categories and targets. Pwn2Own Miami seeks to harden these platforms by revealing vulnerabilities and providing that research to the vendors. The goal is always to get these bugs fixed before they’re actively exploited by attackers. ICS vendors have been instrumental in making that goal a reality.

The 2023 edition of Pwn2Own Miami has four categories:

·      OPC Unified Architecture (OPC UA) Server

You’ll notice these are different categories from previous years. These differences reflect the changing state of the ICS industry and better reflect current threats to SCADA systems. Let’s look at the details of each category.

**OPC UA Server Category**

The [OPC Unified Architecture (UA)](https://opcfoundation.org/about/opc-technologies/opc-ua/) is a platform-independent, service-oriented architecture that integrates all the functionality of the individual OPC Classic specifications into one extensible framework. OPC UA serves as the universal translator protocol in the ICS world. It is used by almost all ICS products to send data between disparate vendor systems. While we’ve had OPC UA targets in the past, for this event, we’ve set up distinct Server and Client categories.

An attempt in this category must be launched against the target’s exposed network services from the contestant’s laptop within the contest network. An entry in the category must result in either a denial-of-service condition, arbitrary code execution, credential theft, or a bypass of the trusted application check.

The Credential Theft target should prove interesting. For this scenario, the contestant must create a session with a trusted certificate but use credentials acquired by either decrypting a password from an ongoing session or by abusing a vulnerability that allows for the retrieval of the stored password from the server. The server will be configured with an ‘admin’ account with a random password that is 12-16 characters long. A successful entry must log in using a legitimate client after the password is retrieved by some means. Brute force attacks won’t be allowed.

For the “bypass trusted application check” scenario, the contestant must bypass the trusted application check that occurs after the creation of a secure channel. Entries that bypass the check by manipulating the server security configuration are out of scope. There are additional requirements for this target, so definitely read the rules carefully if you want to enter.

Here is the full list of targets for the OPC UA Server category:

**OPC UA Client Category**

Similar to the Server category, we’ll have specific OPA UA Clients available to target. Again, the “bypass trusted application check” scenario must meet specific criteria, so you should check out the rules for a full description.

Here is the full list of targets for the OPC US Client category:

**Data Gateway Category**

This category focuses on devices that connect other devices of varying protocols. There are two products in this category. The first is the [Triangle Microworks SCADA Data Gateway](https://products.trianglemicroworks.com/) product. Triangle Microworks makes the most widely used DNP3 protocol stack.  The other is the [Softing Secure Integration Server](https://industrial.softing.com/products/opc-opc-ua-software-platform/integration-platform/secure-integration-server.html). According to their website, “Secure Integration Server covers the full range of OPC UA security features and enables the implementation of state-of-the-art security solutions.” We’ll see if that holds true throughout the contest.

A successful entry in this category must result in arbitrary code execution.

**Edge Category**

This category is new for 2023 and reflects how edge devices are often used in ICS/SCADA networks to manage and maintain systems. For this year’s event, we’ll have the [AVEVA Edge Data Store](https://www.aveva.com/en/products/aveva-edge-data-store/) as our sole target in this category. Edge Data Store collects, stores, and provides data from remote and uncrewed assets. This is an exciting addition to the contest, and we look forward to seeing what exploits researchers demonstrate against this target.

A successful entry in this category must result in arbitrary code execution.

**Master of Pwn**

No Pwn2Own contest would be complete without crowning a Master of Pwn, and Pwn2Own Miami is no exception. Earning the title comes with a slick trophy and  65,000 ZDI reward points (instant [Platinum](https://www.zerodayinitiative.com/about/benefits/) status in 2024, which includes a one-time bonus estimated at $25,000).

For those not familiar with how it works, Master of Pwn points are accumulated for each successful attempt. While only the first demonstration in a category wins the full cash award, each successful entry claims the full number of Master of Pwn points. Since the order of attempts is determined by a random draw, those who receive later slots can still claim the Master of Pwn title – even if they earn a lower cash payout.

To add to the excitement, there are penalties for withdrawing from an attempt once you register for it. If a contestant decides to withdraw from the registered attempt before the actual attempt, the Master of Pwn points for that attempt will be divided by 2 and deducted from the contestant's point total for the contest. Since Pwn2Own is now often a team competition, along with the initial deduction of points, the same number of Master of Pwn points will also be deducted from all contestant teams from the same company.

**The Complete Details**

The full set of rules for Pwn2Own Miami 2023 can be found [h...