---
title: Hackers Claim They Breached T-Mobile More Than 100 Times in 2022
url: https://krebsonsecurity.com/2023/02/hackers-claim-they-breached-t-mobile-more-than-100-times-in-2022/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:27.438307
---

# Hackers Claim They Breached T-Mobile More Than 100 Times in 2022

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Hackers Claim They Breached T-Mobile More Than 100 Times in 2022

February 28, 2023

[36 Comments](https://krebsonsecurity.com/2023/02/hackers-claim-they-breached-t-mobile-more-than-100-times-in-2022/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2023/02/tmoblog.png)

Three different cybercriminal groups claimed access to internal networks at communications giant **T-Mobile** in more than 100 separate incidents throughout 2022, new data suggests. In each case, the goal of the attackers was the same: Phish T-Mobile employees for access to internal company tools, and then convert that access into a cybercrime service that could be hired to divert *any* T-Mobile user’s text messages and phone calls to another device.

The conclusions above are based on an extensive analysis of **Telegram** chat logs from three distinct cybercrime groups or actors that have been identified by security researchers as particularly active in and effective at “**SIM-swapping**,” which involves temporarily seizing control over a target’s mobile phone number.

Countless websites and online services use SMS text messages for both password resets and multi-factor authentication. This means that stealing someone’s phone number often can let cybercriminals hijack the target’s entire digital life in short order — including access to any financial, email and social media accounts tied to that phone number.

All three SIM-swapping entities that were tracked for this story remain active in 2023, and they all conduct business in open channels on the instant messaging platform Telegram. KrebsOnSecurity is not naming those channels or groups here because they will simply migrate to more private servers if exposed publicly, and for now those servers remain a useful source of intelligence about their activities.

Each advertises their claimed access to T-Mobile systems in a similar way. At a minimum, every SIM-swapping opportunity is announced with a brief “*Tmobile up!”* or “*Tmo up!*” message to channel participants. Other information in the announcements includes the price for a single SIM-swap request, and the handle of the person who takes the payment and information about the targeted subscriber.

The information required from the customer of the SIM-swapping service includes the target’s phone number, and [the serial number](https://www.hologram.io/blog/whats-an-iccid-number-and-why-does-it-matter-for-cellular-iot/) tied to the new SIM card that will be used to receive text messages and phone calls from the hijacked phone number.

Initially, the goal of this project was to count how many times each entity claimed access to T-Mobile throughout 2022, by cataloging the various “Tmo up!” posts from each day and working backwards from Dec. 31, 2022.

But by the time we got to claims made in the middle of May 2022, completing the rest of the year’s timeline seemed unnecessary. The tally shows that in the last seven-and-a-half months of 2022, these groups collectively made SIM-swapping claims against T-Mobile on 104 separate days — often with multiple groups claiming access on the same days.

[![](https://krebsonsecurity.com/wp-content/uploads/2023/02/tmodates.png)](https://krebsonsecurity.com/wp-content/uploads/2023/02/tmodates.png)

The 104 days in the latter half of 2022 in which different known SIM-swapping groups claimed access to T-Mobile employee tools.

KrebsOnSecurity shared a large amount of data gathered for this story with T-Mobile. The company declined to confirm or deny any of these claimed intrusions. But in a written statement, T-Mobile said this type of activity affects the entire wireless industry.

“And we are constantly working to fight against it,” the statement reads. “We have continued to drive enhancements that further protect against unauthorized access, including enhancing multi-factor authentication controls, hardening environments, limiting access to data, apps or services, and more. We are also focused on gathering threat intelligence data, like what you have shared, to help further strengthen these ongoing efforts.”

## TMO UP!

While it is true that each of these cybercriminal actors periodically offer SIM-swapping services for other mobile phone providers — including **AT&T**, **Verizon** and smaller carriers — those solicitations appear *far* less frequently in these group chats than T-Mobile swap offers. And when those offers do materialize, they are considerably more expensive.

The prices advertised for a SIM-swap against T-Mobile customers in the latter half of 2022 ranged between USD $1,000 and $1,500, while SIM-swaps offered against AT&T and Verizon customers often cost well more than twice that amount.

![](https://krebsonsecurity.com/wp-content/uploads/2023/02/mobiletheft.png)

To be clear, KrebsOnSecurity is not aware of specific SIM-swapping incidents tied to any of these breach claims. However, the vast majority of advertisements for SIM-swapping claims against T-Mobile tracked in this story had two things in common that set them apart from random SIM-swapping ads on Telegram.

First, they included an offer to use a mutually trusted “middleman” or escrow provider for the transaction (to protect either party from getting scammed). More importantly, the cybercriminal handles that were posting ads for SIM-swapping opportunities from these groups generally did so on a daily or near-daily basis — often teasing their upcoming swap events in the hours before posting a “Tmo up!” message announcement.

In other words, if the crooks offering these SIM-swapping services were ripping off their customers or claiming to have access that they didn’t, this would be almost immediately obvious from the responses of the more seasoned and serious cybercriminals in the same chat channel.

There are plenty of people on Telegram claiming to have SIM-swap access at major telecommunications firms, but a great many such offers are simply four-figure scams, and any pretenders on this front are soon identified and banned ([if not worse](https://krebsonsecurity.com/2022/09/violence-as-a-service-brickings-firebombings-shootings-for-hire/)).

One of the groups that reliably posted “Tmo up!” messages to announce SIM-swap availability against T-Mobile customers also reliably posted “Tmo down!” follow-up messages announcing exactly when their claimed access to T-Mobile employee tools was discovered and revoked by the mobile giant.

A review of the timestamps associated with this group’s incessant “Tmo up” and “Tmo down” posts indicates that while their claimed access to employee tools usually lasted less than an hour, in some cases that access apparently went undiscovered for several hours or even days.

## TMO TOOLS

How could these SIM-swapping groups be gaining access to T-Mobile’s network as frequently as they claim? Peppered throughout the daily chit-chat on their Telegram channels are solicitations for people urgently needed to serve as “callers,” or those who can be hired to social engineer employees over the phone into navigating to a phishing website and entering their employee credentials.

**Allison Nixon** is chief research officer for the New York City-based cybersecuri...