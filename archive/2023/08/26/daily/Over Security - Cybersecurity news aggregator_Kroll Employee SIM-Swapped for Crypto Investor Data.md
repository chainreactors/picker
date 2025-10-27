---
title: Kroll Employee SIM-Swapped for Crypto Investor Data
url: https://krebsonsecurity.com/2023/08/kroll-employee-sim-swapped-for-crypto-investor-data/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-26
fetch_date: 2025-10-04T12:02:36.272100
---

# Kroll Employee SIM-Swapped for Crypto Investor Data

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Kroll Employee SIM-Swapped for Crypto Investor Data

August 25, 2023

[32 Comments](https://krebsonsecurity.com/2023/08/kroll-employee-sim-swapped-for-crypto-investor-data/#comments)

Security consulting giant **Kroll** disclosed today that a SIM-swapping attack against one of its employees led to the theft of user information for multiple cryptocurrency platforms that are relying on Kroll services in their ongoing bankruptcy proceedings. And there are indications that fraudsters may already be exploiting the stolen data in phishing attacks.

Cryptocurrency lender **BlockFi** and the now-collapsed crypto trading platform **FTX** each disclosed data breaches this week thanks to a recent SIM-swapping attack targeting an employee of **Kroll** — the company handling both firms’ bankruptcy restructuring.

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/kroll.png)

In a statement released today, New York City-based Kroll said it was informed that on Aug. 19, 2023, someone targeted a **T-Mobile** phone number belonging to a Kroll employee “in a highly sophisticated ‘SIM swapping’ attack.”

“Specifically, T-Mobile, without any authority from or contact with Kroll or its employees, transferred that employee’s phone number to the threat actor’s phone at their request,” the [statement](https://www.kroll.com/en/about-us/news/security-incident) continues. “As a result, it appears the threat actor gained access to certain files containing personal information of bankruptcy claimants in the matters of BlockFi, FTX and **Genesis**.”

T-Mobile has not yet responded to requests for comment.

Countless websites and online services use SMS text messages for both password resets and multi-factor authentication. This means that stealing someone’s phone number often can let cybercriminals hijack the target’s entire digital life in short order — including access to any financial, email and social media accounts tied to that phone number.

SIM-swapping groups will often call employees on their mobile devices, pretend to be someone from the company’s IT department, and then try to get the employee to visit a phishing website that mimics the company’s login page.

Multiple SIM-swapping gangs have had great success using this method to target T-Mobile employees for the purposes of reselling a cybercrime service that can be hired to divert any T-Mobile user’s text messages and phone calls to another device.

In February 2023, KrebsOnSecurity chronicled SIM-swapping attacks claimed by these groups against T-Mobile employees [in more than 100 separate incidents in the second half of 2022](https://krebsonsecurity.com/2023/02/hackers-claim-they-breached-t-mobile-more-than-100-times-in-2022/). The average cost to SIM swap any T-Mobile phone number was approximately $1,500.

The unfortunate result of the SIM-swap against the Kroll employee is that people who had financial ties to BlockFi, FTX, or Genesis now face increased risk of becoming targets of SIM-swapping and phishing attacks themselves.

And there is some indication this is already happening. Multiple readers who said they got breach notices from Kroll today also shared phishing emails they received this morning that spoofed FTX and claimed, “You have been identified as an eligible client to begin withdrawing digital assets from your FTX account.”

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/ftx-phish.png)

A major portion of Kroll’s business comes from helping organizations [manage cyber risk](https://www.kroll.com/en/services/cyber-risk). Kroll is often called in to investigate data breaches, and it also sells identity protection services to companies that recently experienced a breach and are grasping at ways to demonstrate that they doing *something* to protect their customers from further harm.

Kroll did not respond to questions. But it’s a good bet that BlockFi, FTX and Genesis customers will soon enjoy yet another offering of free credit monitoring as a result of the T-Mobile SIM swap.

Kroll’s website says it employs “elite cyber risk leaders uniquely positioned to deliver end-to-end cyber security services worldwide.” Apparently, these elite cyber risk leaders did not consider the increased attack surface presented by their employees using T-Mobile for wireless service.

The SIM-swapping attack against Kroll is a timely reminder that *you should do whatever you can to minimize your reliance on mobile phone companies for your security*. For example, many online services require you to provide a phone number upon registering an account, but that number can often be removed from your profile afterwards.

Why do I suggest this? *Many online services allow users to reset their passwords just by clicking a link sent via SMS*, and this unfortunately widespread practice has turned mobile phone numbers into de facto identity documents. Which means losing control over your phone number thanks to an unauthorized SIM swap or mobile number port-out, divorce, job termination or financial crisis can be devastating.

If you haven’t done so lately, take a moment to inventory your most important online accounts, and see how many of them can still have their password reset by receiving an SMS at the phone number on file. This may require stepping through the website’s account recovery or lost password flow.

If the account that stores your mobile phone number does not allow you to delete your number, check to see whether there is an option to disallow SMS or phone calls for authentication and account recovery. If more secure options are available, such as a security key or a one-time code from a mobile authentication app, please take advantage of those instead. The website [2fa.directory](https://www.2fa.directory) is a good starting point for this analysis.

Now, you might think that the mobile providers would share some culpability when a customer suffers a financial loss because a mobile store employee got tricked into transferring that customer’s phone number to criminals. But earlier this year, a California judge [dismissed a lawsuit against AT&T](https://blockworks.co/news/att-crypto-sim-swap-lawsuit) that stemmed from [a 2017 SIM-swapping attack](https://krebsonsecurity.com/2021/12/ny-man-pleads-guilty-in-20-million-sim-swap-theft/) which netted the thieves more than $24 million in cryptocurrency.

*This entry was posted on Friday 25th of August 2023 02:05 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/)

[BlockFi](https://krebsonsecurity.com/tag/blockfi/) [FTX](https://krebsonsecurity.com/tag/ftx/) [Kroll breach](https://krebsonsecurity.com/tag/kroll-breach/) [SIM swapping](https://krebsonsecurity.com/tag/sim-swapping/) [T-Mobile](https://krebsonsecurity.com/tag/t-mobile/)

Post navigation

[← Tourists Give Themselves Away by Looking Up. So Do Most Network Intruders.](https://krebsonsecurity.com/2023/08/tourists-give-themselves-away-by-looking-up-so-do-most-network-intruders/)
[U.S. Hacks QakBot, Quietly Removes Botnet Infections →](https://krebsonsecurity....