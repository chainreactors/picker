---
title: What Is Flipper Zero The Hacker Tool Going Viral on TikTok, Explained
url: https://www.wired.com/story/what-is-flipper-zero-tiktok/
source: Instapaper: Unread
date: 2022-12-25
fetch_date: 2025-10-04T02:30:03.009487
---

# What Is Flipper Zero The Hacker Tool Going Viral on TikTok, Explained

[Skip to main content](#main-content)

Menu

[![Wired](/verso/static/wired-us/assets/logo.svg)](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[![Wired](/verso/static/wired-us/assets/logo.svg)](/)

Account

Account

[Newsletters](/newsletter?sourceCode=navbar)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=navbar)

[Podcasts](/podcasts/)

[Video](/video/)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Fwhat-is-flipper-zero-tiktok%2F&source=VERSO_NAVIGATION)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Fwhat-is-flipper-zero-tiktok%2F&source=VERSO_NAVIGATION)

[Dhruv Mehrotra](/author/dhruv-mehrotra/)

[Security](/category/security)

Dec 22, 2022 7:00 AM

# Hands On With Flipper Zero, the Hacker Tool Blowing Up on TikTok

Don’t be fooled by its fun name and Tamagotchi-like interface—this do-everything gadget is trouble waiting to happen and a whole lot more.

![Colorful illustration featuring a person's hand holding a FlipperZero device.](https://media.wired.com/photos/639a3cfa97910e7b896daef8/3:2/w_2560%2Cc_limit/YearEndReview_FlipperZero.jpg)

ILLUSTRATION: YAZ BUTCHER; Cameron Getty; FlipperZero

Save StorySave this story

Save StorySave this story

Across the US, countless buildings, from government offices to your next hotel room door, are protected by RFID-controlled locks. On a recent trek through Manhattan, I passed nearly 20 of these keyless entry systems, which are among the most pervasive in the world. But a playful palm-sized gadget with a Tamagotchi-like interface can likely thwart the locks on many of these doors.

The $200 device is called Flipper Zero, and it’s a portable pen-testing tool designed for hackers of all levels of technical expertise. The tool is smaller than a phone, easily concealable, and is stuffed with a range of radios and sensors that allow you to intercept and replay signals from keyless entry systems, Internet of Things sensors, garage doors, NFC cards, and virtually any other device that communicates wirelessly in short ranges. For example, in just seconds, I used the Flipper Zero to seamlessly clone the signal of an RFID-enable card tucked safely inside my wallet.

If you had only heard about Flipper Zero through TikTok, where the tool has gone viral, you might think that it was a toy that could [make ATMs spit out money, cars unlock themselves, and gas spill out of pumps for free](https://www.tiktok.com/%40b_turner50/video/7167461902950419717?is_from_webapp=v1&item_id=7167461902950419717). I spent the last week testing one to determine whether the world was as vulnerable to Flipper Zero as social media made it out to be. What I found was mixed: Many of the most dramatic videos posted to TikTok are likely staged—most modern wireless devices are not susceptible to simple replay attacks—but the Flipper Zero is still undeniably powerful, giving aspiring hackers and seasoned pen-testers a convenient new tool to probe the security of the world’s most ubiquitous wireless devices.

In reviews, people liken Flipper Zero to [a Swiss Army knife](https://www.theverge.com/23433594/flipper-zero-hacking-gadget-wireless-pentesting-open-source-antenna) for physical penetration testing. But in my week testing Flipper Zero, it felt more like a blacklight—something I could literally hold up to a device that would reveal information, invisible to the human eye, about how it worked, what data it was emitting, and how often it was doing so.

Here’s a brief list of some things I’ve learned with the help of Flipper Zero this week: Some animal microchips will tell you the body temperature of your pet. My neighbor’s car tire pressure sensor leaks data to anyone in range of the signal. My iPhone blasts my face with infrared signals every few seconds. My home security system has built-in signal-jamming detection. Some hotel and office bathrooms have soap dispensers that broadcast whether they need to be refilled.

When I told Alex Kulagin, one of Flipper Zero’s co-creators, about my experiences using his tool to make these kinds of mundane observations, he explained that this is exactly what the device is meant for. “We want to help you understand something deeply, explore how it works, and explore the wireless world that’s all around you but difficult to understand,” he says.

Kulagin and his business partner, Pavel Zhovner, first came up with the idea for Flipper Zero in 2019. Since then, their company has sold 150,000 devices and they’ve grown their team to nearly 50 people. But as they’ve grown, they’ve encountered some resistance. This summer, [payments of more than $1.3 million were held up by PayPal,](https://www.dailydot.com/debug/flipper-zero-paypal/) and in September, US Customs and Border Patrol seized a shipment of devices. According to Kulagin, CBP released the shipment after a month but has yet to tell the company why it held the shipment. CBP declined WIRED’s request to comment about the seized Flipper Zeros.

Bob Zahreddine is a lieutenant for the Glendale Police Department and executive officer with the High Tech Crime Cops, an industry group made up of law enforcement officials that, according to its website, “connects cyber cops and investigators.” Zahreddine says that he isn’t necessarily surprised that CBP has taken an interest in Flipper Zero. “Because Flipper Zero is so customizable, the potential is there for it to be used in all sorts of crime,” he says.

Zahreddine’s organization maintains a listserv where investigators will often solicit advice from their peers and share news or information about developments in the latest law enforcement technology. He told WIRED that while he hasn’t heard any chatter about Flipper Zero being used in any crimes on his listserv, investigators there are aware of the tool and have been following its development since Kulagin and Zhovner began fundraising on Kickstarter.

Indeed, it’s easy to imagine how someone could break the law or even just get up to some petty mischief with this device. For instance, not only was I able to clone a building-entry card with Flipper Zero, I was able to record the signal that my neighbor’s garage door opener makes when he pulls into his driveway. Older cars that don’t use rolling code encryption are likely unlockable with the device, and my Flipper Zero was able to read my credit card number through my wallet and pants.

But Kulagin isn’t particularly concerned about his tool’s potential for criminal mischief. “Obviously, there are old cars that are vulnerable to Flipper. But they aren’t secure by definition—that is not Flipper’s fault,” he says. “There are bad people out there, and they can do bad stuff with any computer. We aren’t intending to break laws.”

To that end, Flipper Zero’s firmware, by default, prevents individuals from transmitting on frequencies that are banned in the country the device is in, and Flipper Zero’s Discord server explicitly forbids discussions about alternative firmware with illegal features. (However, because the project is open source, a savvy Flipper user could adjust the firmware to enable additional, perhaps malicious, functionality.) The tool also isn’t able to copy or replay any encrypted signals. For instance, while I was able to read the signal from my credit and debit cards, I was unable to use that signal to actually pay for anything with contactless p...