---
title: Warming Up Your IP Addresses Automatically
url: https://luxsci.com/blog/warming-up-ip-address-automatically.html
source: LuxSci
date: 2023-02-14
fetch_date: 2025-10-04T06:33:13.589284
---

# Warming Up Your IP Addresses Automatically

[![](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2024/06/19153212/Horizontal-Logo-Dark.svg)](/)
[![LUXSCI](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2024/06/19153212/Horizontal-Logo-Dark.svg)](/)

[Contact Us](/contact-us)

[« blog index](/blog)

# Warming Up Your IP Addresses Automatically

February 13th, 2023

There are many best practices for ensuring optimal deliverability when sending email messages. One critical factor in deliverability is IP reputation. However, how can you build a good reputation when using a brand-new server and IP address? This article will explain how to warm up an IP address to build a good reputation and improve [email deliverability](https://luxsci.com/email-deliverability/ "email deliverability").

[![warm up ip address](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2018/06/02160358/LuxSci_Sep2021_Blog-image_How-to-Warm-Up-An-IP-Address-Automatically.jpeg)](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2018/06/02160358/LuxSci_Sep2021_Blog-image_How-to-Warm-Up-An-IP-Address-Automatically.jpeg)

## **What Is IP Reputation?**

**Good reputation**: If a server is known to send lots of good quality emails (messages people do not consider spam-like), then the server’s IP address is looked at favorably by ISPs (such as Yahoo!, Google, Microsoft, etc.). A good reputation allows organizations to send large quantities of good emails that will be delivered to recipients. A server with a good reputation has an IP address that we call “warm” (think *warmed up and humming along*).

**Bad reputation**: If a server is known to send junk or malicious emails (according to the email recipients), ISPs will throttle the emails, accepting only a few messages at a time. They may even flag emails as spam and not deliver them at all. A server with a poor reputation will need work to repair it.

**No reputation**: A new server may not have a recent history of sending emails. As a result, the IP address may have “no reputation.” ISPs are very skeptical about emails from servers with no reputation or evidence of good email sending. A typical sign of a spammer is when a server with little or no reputation suddenly starts sending large quantities of emails. ISPs will detect this and quickly throttle or block such servers, *moving them from “no reputation” to “bad reputation.”*

## **Warm Up an IP Address from No Reputation**

So, you have a new dedicated server and want to start sending a lot of emails. The new dedicated server’s IP address will likely have no reputation, so what can you do to warm it up? More importantly, **how do you go from having “no reputation” to a “good reputation?”**

The IP address must be warmed up to achieve a good reputation. This process involves the following steps:

1. Start by sending *slowly*. Send less than 50 email messages per hour in the beginning.
2. Each day, send more messages.
3. Over the course of a month, ramp up to the full sending rate.
4. Start sending to clean email lists that have opted into receiving emails. This helps ensure that the recipients will not mark it as spam or flag it as unwanted.
5. Follow all the other best practices for good email deliveryÂ (e.g., good content, good lists, SPF and DKIM records in place, etc.)

Following this warmup process makes it possible to reach a full sending rate in a reasonable amount of time without being penalized for sending too much too soon.

Many people are anxious to get that first huge email blast off ASAP, but unless the IP address is adequately warmed up, those messages won’t land in the recipients’ inboxes. Furthermore, the server’s reputation will be damaged and will take longer to recover and properly warm up.

### Email throttling and Manual IP Warmup

If the email sending program has sending rate throttling built-in, it can be used to ramp up sending slowly. However, many sending systems do not know how to limit email sending correctly. For these cases, LuxSci has an email throttling feature in the server status and configuration page (Existing customers can go to the servers page, click on your server, and scroll down to the “Email Queues” section of the Server Vital Signs widget).

When “email throttling” is enabled:

* Emails can be sent to the server as often as desired.
* The server will queue these messages.
* The server will send them out based on a specified “email throttling” rate.

For example, if the rate is 1,000 messages/hour and 24,000 messages are sent, they will be queued and sent out evenly over 24 hours. The first messages received are the first ones sent out.

The throttling rate can be changed to manually warm up an IP address and fix problems with tarnished IP reputation.

Note:

1. The actual maximum rate at which a server can send email is a function of many factors, including the power of the server and the nature of the messages sent. See Sending Rates for more details.
2. No matter the configured maximum sending rate, the excess messages will be rejected if emails are sent to more recipients in a month than the monthly recipient limit.

### Automatic IP Warmup

LuxSci’s Automatic IP Warmup is usually a good alternative for new servers as it eliminates all manual work and decision-making and takes care of the warm up process. Customers can go to the server status and configuration page, enable “Automatic IP Warmup,” and leave “Email Throttling” set to “0” or “-1” (the default, which means “no specific throttling”). Then:

1. LuxSci enables email throttling and sets the rate limit for today to be very small: 20 messages/hour.
2. Each night, LuxSci increases the allowed sending rate (see the table below for the schedule) once the current rate for the entire day is met.

Customers going through the automatic IP warmup process need to:

1. **Actually send messages.** If emails are not being sent, the warm up will not impact IP reputation, and the rate limit will not automatically increase.
2. **Send enough messages**. It’s essential to send enough email, so the server sends at close to its maximum allowed rate during the first weeks. This way, ISPs see the server progressively sending more and more emails. We usually recommend sending a good size email blast in the beginning that will slowly work its way through the recipients as the IP warms up and the sending rate increases.
3. **Use best practices.** As we have said before, the messages must have good content, do not look spammy, and are sent to recipients who want to receive emails (i.e., they are unlikely to mark it as spam). The goal is to validate the server’s reputation by *sending more good emails to willing recipients*. By not following this advice, the warm up process may leave you with a bad reputation.

### Automatic IP Warmup Schedule

Customers must warm up the IP address of their email server to achieve a good sender reputation. The following schedule sets the server’s sending rate during the automatic IP warmup period. If less than 90% of a given day’s rate-allowed messages are sent within 24 hours, the rate will not automatically increase to the next level. This requirement helps make sure that the IP warmup is effective.

| DAY | Rate: Messages/Hour | Maximum Messages/Day | Cumulative Messages |
| --- | --- | --- | --- |
| 1 (Week 1) | 20 | 480 | 480 |
| 2 | 30 | 720 | 1,200 |
| 3 | 40 | 960 | 2,160 |
| 4 | 55 | 1,320 | 3,480 |
| 5 | 80 | 1,920 | 5,400 |
| 6 | 160 | 3,840 | 9,240 |
| 7 | 320 | 7,680 | 16,920 |
| 8 (Week 2) | 640 | 15,360 | 32,280 |
| 9 | 1,000 | 24,000 | 56,280 |
| 10 | 1,400 | 33,600 | 89,880 |
| 11 | 2,000 | 48,000 | 137,880 |
| 12 | 3,000 | 72,000 | 209,880 |
| 13 | 4,000 | 96,000 | 305,880 |
| 14 | 6,000 | 144,000 | 449,880 |
| 15 (Week 3) | 8,000 | 192,000 | 641,880 |
| 16 | 11,000 | 264,000 | 905,880 |
| 17 | 15,000 | 360,000 | 1,265,880 |
| 18 | 20,000 | 480,000 | 1,745,880 |
| 19 | 26,000 | 624,000 | 2,369,880 |
| 20 | 33,000 | 729,000 | 3,161,880 |
| 21 | 40,000 | 960,000 | 4,121...