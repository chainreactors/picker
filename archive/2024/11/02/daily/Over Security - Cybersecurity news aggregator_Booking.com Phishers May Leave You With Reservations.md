---
title: Booking.com Phishers May Leave You With Reservations
url: https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-02
fetch_date: 2025-10-06T19:18:56.020198
---

# Booking.com Phishers May Leave You With Reservations

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Booking.com Phishers May Leave You With Reservations

November 1, 2024

[34 Comments](https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/#comments)

A number of cybercriminal innovations are making it easier for scammers to cash in on your upcoming travel plans. This story examines a recent spear-phishing campaign that ensued when a California hotel had its **booking.com** credentials stolen. We’ll also explore an array of cybercrime services aimed at phishers who target hotels that rely on the world’s most visited travel website.

According to the market share website **statista.com**, booking.com is by far the Internet’s busiest travel service, with nearly 550 million visits in September. KrebsOnSecurity last week heard from a reader whose close friend received a targeted phishing message within the Booking mobile app just minutes after making a reservation at a California hotel.

The missive bore the name of the hotel and referenced details from their reservation, claiming that booking.com’s anti-fraud system required additional information about the customer before the reservation could be finalized.

![](https://krebsonsecurity.com/wp-content/uploads/2024/11/bookingcomphish.png)

In an email to KrebsOnSecurity, booking.com confirmed one of its partners had suffered a security incident that allowed unauthorized access to customer booking information.

“Our security teams are currently investigating the incident you mentioned and can confirm that it was indeed a phishing attack targeting one of our accommodation partners, which unfortunately is not a new situation and quite common across industries,” booking.com replied. “Importantly, we want to clarify that there has been no compromise of Booking.com’s internal systems.”

![](https://krebsonsecurity.com/wp-content/uploads/2024/11/bookingdotcomphishingsite.png)

Booking.com said it now [requires 2FA](https://partner.booking.com/en-gb/help/legal-security/security/securing-your-account), which forces partners to provide a one-time passcode from a mobile authentication app (Pulse) in addition to a username and password.

“2FA is required and enforced, including for partners to access payment details from customers securely,” a booking.com spokesperson wrote. “That’s why the cybercriminals follow-up with messages to try and get customers to make payments outside of our platform.”

“That said, the phishing attacks stem from partners’ machines being compromised with malware, which has enabled them to also gain access to the partners’ accounts and to send the messages that your reader has flagged,” they continued.

It’s unclear, however, if the company’s 2FA requirement is enforced for all or just newer partners. Booking.com did not respond to questions about that, and its current [account security advice](https://www.booking.com/trust-and-safety/partners.en-gb.html#tns_partners_account_safe) urges customers to enable 2FA.

![](https://krebsonsecurity.com/wp-content/uploads/2024/11/whybooking.png)

A scan of social media networks showed this is not an uncommon scam.

In November 2023, the security firm **SecureWorks** [detailed](https://www.secureworks.com/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam) how scammers targeted booking.com hospitality partners with data-stealing malware. SecureWorks said these attacks had been going on since at least March 2023.

“The hotel did not enable multi-factor authentication (MFA) on its Booking.com access, so logging into the account with the stolen credentials was easy,” SecureWorks said of the booking.com partner it investigated.

In June 2024, booking.com [told the BBC](https://www.bbc.com/news/articles/c8003dd8jzeo) that phishing attacks targeting travelers had increased 900 percent, and that thieves taking advantage of new artificial intelligence (AI) tools were the primary driver of this trend.

Booking.com told the BCC the company had started using AI to fight AI-based phishing attacks. Booking.com’s statement said their investments in that arena “blocked 85 million fraudulent reservations over more than 1.5 million phishing attempts in 2023.”

The domain name in the phony booking.com website sent to our reader’s friend — **guestssecureverification[.]com** — was registered to the email address **ilotirabec207@gmail.com**. According to [DomainTools.com](https://www.domaintools.com), this email address was used to register more than 700 other phishing domains in the past month alone.

Many of the 700+ domains appear to target hospitality companies, including platforms like booking.com and **Airbnb**. Others seem crafted to phish users of **Shopify**, **Steam**, and a variety of financial platforms. A full, defanged list of domains is available [here](https://docs.google.com/spreadsheets/d/1k8c2d2XZLXIG9tFUaU6MGRK-puAKxoCuWuzB8GSqkAM/edit?usp=sharing).

A cursory review of recent posts across dozens of cybercrime forums monitored by the security firm [Intel 471](https://www.intel471.com) shows there is a great demand for compromised booking.com accounts belonging to hotels and other partners.

One post last month on the Russian-language hacking forum **BHF** offered up to $5,000 for each hotel account. This seller claims to help people monetize hacked booking.com partners, apparently by using the stolen credentials to set up fraudulent listings.

A service advertised on the English-language crime community **BreachForums** in October courts phishers who may need help with certain aspects of their phishing campaigns targeting booking.com partners. Those include more than two million hotel email addresses, and services designed to help phishers organize large volumes of phished records. Customers can interact with the service via an automated Telegram bot.

![](https://krebsonsecurity.com/wp-content/uploads/2024/11/airbnb-bf.png)

Some cybercriminals appear to have used compromised booking.com accounts to power their own travel agencies catering to fellow scammers, with up to 50 percent discounts on hotel reservations through booking.com. Others are selling ready-to-use “config” files designed to make it simple to conduct automated login attempts against booking.com administrator accounts.

SecureWorks found the phishers targeting booking.com partner hotels used malware to steal credentials. But today’s thieves can just as easily just visit crime bazaars online and purchase stolen credentials to cloud services that do not enforce 2FA for all accounts.

That is [exactly what transpired](https://www.wired.com/story/snowflake-breach-advanced-auto-parts-lendingtree/) over the past year with many customers of the cloud data storage giant **Snowflake**. In late 2023, cybercriminals figured out that while tons of companies had stashed enormous amounts of customer data at Snowflake, many of those customer accounts were not protected by 2FA.

Snowflake responded by making 2FA mandatory for all new customers. But that change came only after thieves used stolen credentials to siphon data from 160 companies — including **AT&T**, **Lending Tree** and **TicketMaster**.

*This entry was posted on Friday 1st of November 2024 05:12 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecu...