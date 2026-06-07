---
title: Free Apps Are Quietly Turning Smart TVs Into Web-Scraping Proxies for AI
url: https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
source: The Hacker News
date: 2026-06-06
fetch_date: 2026-06-07T06:16:38.565944
---

# Free Apps Are Quietly Turning Smart TVs Into Web-Scraping Proxies for AI

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Free Apps Are Quietly Turning Smart TVs Into Web-Scraping Proxies for AI](https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html)

**Swati Khandelwal**Jun 06, 2026Network Security / IoT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKr3KoscB_oGLqU5_JV16DIaB7jXY1ko8PiJDTuwrxbHcZV2DYJpfkx8lqwNbscwTSTVQUMwd8vBf-nI13mQE7vzzmUzwKF3BF6q7s5Lnq7kG7CovDsKaHYlvKpEXo2cvNk4mA27BdJSI6buZLqtVCKhYQ31GOaozmEHQecUa9Zdt-jwFJIZ0OCvlF27_p/s1700-e365/smart-tv.jpg)

A researcher has reverse-engineered the iOS SDK that Bright Data embeds in consumer apps and documented how it turns devices, including always-on smart TVs, into exit nodes that relay web-scraping traffic for a data business Bright Data markets heavily to the AI industry.

The company, the successor to Luminati, operates what it calls the largest residential proxy network in the world, advertised at more than 400 million residential IPs. Part of that supply comes from this SDK, shipped inside free apps behind an opt-in screen and described as a consent-sourced pool of 150 million-plus IPs.

The findings, published June 5 by [Include Security](https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/) and independent researcher Buchodi, matter because the scraping comes from the user's home IP, not the customer's. The immediate risk is not a hacked account or stolen data; it is that a home connection and its bandwidth get used as someone else's scraping infrastructure.

A connected TV is close to ideal for that: usually plugged in, on a fast connection, effectively unmetered, and unwatched.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The deepest technical evidence is from the iOS SDK; the smart-TV reach rests on Bright Data's platform support, its public partner list, and earlier reporting. The research found the peer channel that carries scraping jobs has no real authentication, and on iOS, its traffic bypasses a configured VPN.

## Inside the peer tunnel

When the app opens, the SDK contacts one of Bright Data's servers, which hands over its instructions without really checking who is asking. From then on, the server can tell the device to go and fetch pages from other websites, using the user's home internet connection to do it.

The researcher found the channel that carries those jobs has none of the usual security checks, and described it as weaker than the controls built into most malware.

On iPhones, the researcher found that this traffic slips past a VPN, and that much of what the app does does not show up in the tools security teams normally use to monitor apps. The device can also keep relaying in the background while someone is watching the screen or on a call, as long as the battery is not low.

## The consent gap

The opt-in screen does not match what the SDK actually allows. In one Roku app, Petflix, the screen said it would use the device and its connection "occasionally."

The settings the SDK loads allow up to 200 GB of traffic a month. In a few countries, including Uzbekistan and Oman, the limits are set far higher, and the device is cleared to keep working almost until the battery runs flat. The SDK can also tie together a person's phone and computers that run the same company's apps, treating them as one user.

Bright Data publishes its list of app partners on a page anyone can open, and it includes makers of smart-TV apps such as PlayWorks Digital, CloudTV, and Longvision. The researcher is careful to note that being on the list only shows a company worked with Bright Data at some point, not that its app includes the SDK today. Each one would need to be checked on its own.

## An old model, pulled by AI demand

None of this is new in shape, only in scale. Bright Data is the successor to Luminati, the paid proxy service that grew out of Hola VPN. In 2015 Hola was [caught selling its free users' bandwidth](https://thehackernews.com/2015/05/hola-widely-popular-free-vpn-service.html) as exit nodes through Luminati, at $20 a gigabyte. The same model now runs on the always-on box in the living room.

What changed is the buyer. Anti-bot defenses from Cloudflare, DataDome, and others block scrapers coming from datacenter IPs, so AI scrapers route through residential connections instead.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Krebs [reported in October 2025](https://krebsonsecurity.com/2025/10/aisuru-botnet-shifts-from-ddos-to-residential-proxies/) that proxies from botnets like Aisuru are fueling large-scale AI data harvesting, and Google [dismantled the criminal IPIDEA proxy network](https://thehackernews.com/2026/01/google-disrupts-ipidea-one-of-worlds.html) in January. Those operations hijack consumer devices; Bright Data says its exit nodes opt in through a consent screen. That consent is the line between the two, and whether it is meaningful is the open question.

Lowpass, syndicated by The Verge, [first surfaced](https://www.lowpass.cc/p/smart-tv-web-scraping-ai-bright-data-proxy-networks) the smart-TV angle in February, and this is the technical teardown. Google, Amazon, and Roku have since restricted background proxy SDKs, and Bright Data dropped those platforms, though it still lists Samsung's Tizen and LG's webOS.

## What to do

The traffic is easy to spot and block. On a home network, the simplest step is to block the web addresses the SDK uses to connect, with a router-level tool like Pi-hole or NextDNS.

The main ones are proxyjs.brdtnet.com, proxyjs.luminatinet.com, proxyjs.bright-sdk.com, clientsdk.bright-sdk.com, and clientsdk.brdtnet.com. According to the research, blocking these stops the device from acting as a relay without affecting Bright Data's paid service, which runs on separate addresses.

Companies that manage staff phones can also scan for apps that carry the SDK. One catch: on a mobile connect...