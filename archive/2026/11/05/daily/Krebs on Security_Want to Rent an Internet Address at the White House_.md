---
title: Want to Rent an Internet Address at the White House?
url: https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/
source: Krebs on Security
date: 2026-11-05
fetch_date: 2026-11-06T08:41:48.566969
---

# Want to Rent an Internet Address at the White House?

Advertisement

[![](/b-doppel/17.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

[![](/b-doppel/18.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Want to Rent an Internet Address at the White House?

November 4, 2026

[23 Comments](https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/#comments)

Several staffers at the White House are using computers or mobile devices equipped with residential proxy services that render their internet address available for others to rent, security experts warned today. One of the proxy services is a Russian company whose founder’s web hosting business was ground zero for cyberattacks against election systems in Arizona and Illinois in 2016.

The security firm **Layer3 Intel** said it detected multiple residential proxy nodes beaconing out from the internet address network reserved for the Executive Office of the President ([AS2650](https://ipgeolocation.io/browse/asn/AS2650)). Layer3 said the proxy activity was relatively persistent between October 5 to November 3, and that a review of the proxies available from AS2650 showed they exited from the White House network 236 times during that period.

The proxy tracking company **Synthient** [said](https://x.com/synthient/status/2118115310922518777) on Twitter/X that the activity it saw coming from AS2650 was related to multiple Windows 11 installations of a service called **Infatica**, a proxy program that is often integrated into “free” [mobile and desktop applications](https://krebsonsecurity.com/2021/03/is-your-browser-extension-a-botnet-backdoor/). Infatica’s founder **Vladimir Fomenko** is a Russian man whose hosting firm **King Servers** was home to six of the eight internet addresses used by Russia’s state security services to [compromise databases for election systems](https://edition.cnn.com/2016/08/29/politics/hackers-breach-illinois-arizona-election-systems/) in Arizona and Illinois in 2016.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/11/synthient-whitehouse.png)](https://krebsonsecurity.com/wp-content/uploads/2026/11/synthient-whitehouse.png)

Synthient’s depiction of the frequency of outgoing proxy traffic from the dedicated White House network (AS2650). Click to enlarge.

There are dozens of residential proxy providers with varying degrees of legitimacy, many of them based in China or Russia. But at a minimum, they all make it simple for customers to rent someone else’s internet address as a way to anonymize their web traffic or spoof their true location. From a website’s perspective, the traffic from a proxy network user appears to originate from the rented IP address, not from the proxy service customer.

Layer3 Intel said the proxy exit nodes at the White House came from six internet addresses, on 26 of the 30 days, and that most of the activity happens in the evening, between 5 p.m. and midnight.

Incredibly, Infatica was not the only proxy service that reportedly has been reselling access to White House internet addresses: Layer3 Intel *said it found 28 separate residential proxy services were able to exit through this network*.

“This is public access,” the Layer3 Intel team [wrote](https://layer3intel.com/blog/residential-proxies-white-house-network). “Anybody can obtain it by signing up to a public residential proxy service, paying a few dollars and sending requests through it. We did not selectively target this network or try to make our probes exit from it. We caught this by chance, simply by requesting global rotating access through these services.”

The White House did not immediately respond to a request for comment.

As detailed in several stories here over the past year, residential proxy services are a major source of unwanted and often malicious traffic, including account takeover and other cybercrime activity, advertising fraud, and mass content scraping for AI projects.

They can also introduce serious security risks. In late 2025, it was discovered that cybercriminals were mass exploiting a widespread vulnerability in these services that allowed them to probe each proxy endpoint’s local network for vulnerable systems to infect with malware. In January 2026, dozens of proxy services were forced to patch their networks after Synthient Founder **Ben Brundage** showed how cybercriminals were [abusing a vulnerability](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) in these residential proxy services to seize control over devices inside the local networks of unsuspecting users.

“Some of these resellers sell bandwidth for as low as 60 cents a Gigabyte, that means for less than a dollar you can gain access into some of the most confidential and trusted networks,” Brundage told KrebsOnSecurity. “The reseller ecosystem further enables this with any criminal able to buy access while skipping KYC [Know Your Customer] processes.”

All too often, these proxy services are beaconing out from employee devices brought into the workplace. App developers can embed software development kits (SDKs) provided by the residential proxy networks to monetize their software, allowing them to receive a small amount of money on each installation.

As risky as residential proxies can be for unsuspecting end users, they are all too commonly found on government and corporate networks. In a webinar in January 2026, the proxy tracking service **Spur** found residential proxies in nearly 300 government owned and operated networks, 318 utility companies, 166 healthcare companies or hospitals, and 141 companies in banking and finance. In a blog post earlier this year, the security firm **Infoblox** said it discovered that fully 65% of its customer base was querying one or more residential proxy related domains.

*This entry was posted on Wednesday 4th of November 2026 11:36 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/)

[AS2650](https://krebsonsecurity.com/tag/as2650/) [Ben Brundage](https://krebsonsecurity.com/tag/ben-brundage/) [Infoblox](https://krebsonsecurity.com/tag/infoblox/) [King Servers](https://krebsonsecurity.com/tag/king-servers/) [Layer3 Intel](https://krebsonsecurity.com/tag/layer3-intel/) [residential proxies](https://krebsonsecurity.com/tag/residential-proxies/) [Spur](https://krebsonsecurity.com/tag/spur/) [Synthient](https://krebsonsecurity.com/tag/synthient/) [Vladimir Fomenko](https://krebsonsecurity.com/tag/vladimir-fomenko/)

Post navigation

[← Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies](https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/)

## 23 thoughts on “Want to Rent an Internet Address at the White House?”

1. Hc [November 5, 2026](https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/#comment-661638)

   Incredible things happening in america rn

   [Reply](https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/?replytocom=661638#respond) →
2. E.W. [November 5, 2026](https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/#comment-661640)

   We may never know but I think that there are some staffers who forced the IT department to give them admin rights.
   I’ve experienced that in a county courthouse. All of the judges had admin rights and the compu...