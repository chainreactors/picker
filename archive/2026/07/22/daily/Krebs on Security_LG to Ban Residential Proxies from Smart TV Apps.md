---
title: LG to Ban Residential Proxies from Smart TV Apps
url: https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/
source: Krebs on Security
date: 2026-07-22
fetch_date: 2026-07-23T05:11:51.295349
---

# LG to Ban Residential Proxies from Smart TV Apps

Advertisement

[![](/b-doppel/17.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

[![](/b-doppel/18.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# LG to Ban Residential Proxies from Smart TV Apps

July 21, 2026

[22 Comments](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/#comments)

The home appliance giant **LG Electronics USA** said this week it plans to suspend any apps built for its smart TVs that turn one’s television into an always-on residential proxy node. The move comes less than a month after researchers found that more than 42 percent of games and other apps available for download on LG’s webOS store allow unknown third-parties to route their Internet traffic through a user’s TV.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/smarttv-proxysdks.png)

Proxy SDK prevalence among smart TV apps for LG (webOS) and Samsung (Tizen OS) televisions. Image: Spur.us.

On July 2, we [featured research](https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/) by the security firm **Spur** that examined the prevalence of residential proxy software development kits (SDKs) in smart TV apps. Spur [found](https://spur.us/blog/smart-tv-apps-residential-proxy-sdks) more than 42 percent of apps available for download on LG smart TVs include SDKs that turn one’s television in a proxy node indefinitely, and that more than a quarter of the apps made for Samsung’s Tizen operating system had similar residential proxy components.

Responding to questions about Spur’s research, **LG Senior Vice President John Taylor** told KrebsOnSecurity the company was working with app developers to remove the residential proxy option from their apps on the webOS platform. Developers that fail to comply, he said, will find their apps suspended.

“A residential proxy network is not an intended use for LG smart TVs, and LG Electronics is working with developers to remove the residential proxy option from their apps on the webOS platform,” Taylor said. “If this option is not removed, these apps will be suspended.”

Taylor said LG is committed to keeping residential proxy networks out of its smart TV apps going forward, and that the company’s review of those apps is “well underway now.”

“As part of our ongoing efforts to enhance platform quality and the user experience, LG will continue to strengthen our evaluation process for developer-submitted apps, including those that incorporate residential proxy SDKs,” Taylor wrote in an emailed statement.

App makers looking for ways to monetize their creations can turn to residential proxy providers, which pay developers to include SDKs that turn the user’s device into a residential proxy node that is rented to paying customers. In the case of LG and Samsung smart TVs, Spur found residential proxy SDKs bundled with everything from simple games like Pac-Man to screensavers and file utilities.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/pac-man-brightdata.png)

A Pac-Man smart TV app from Bright Data offers users the choice between viewing ads in the game or agreeing to allow their TV to serve as a residential proxy node. Image: Spur.us.

Spur’s report found the residential proxy network **Bright Data** accounted for a majority of proxy SDKs across both Samsung and LG smart TVs. In a statement shared with KrebsOnSecurity, Bright Data said its network is built on consent and responsibility and operates by LG and Samsung terms.

“Every peer opts in through a dedicated screen and receives value in return; every customer is vetted, and our practices have now undergone a second independent audit by PwC,” the statement reads. “We remain committed to an open, transparent internet where legitimate businesses, researchers, and institutions can responsibly access data that lives in the public domain.”

Bright Data and other proxy providers named in Spur’s report all say they follow rigorous know-your-customer processes to validate legitimate uses of their services, which is often heavily tied to content-scraping activities by said customers. The proxy companies also say they incorporate technological countermeasures to prevent proxy service customers from being able to [interact with and control other devices on the proxy user’s local network](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/).

Spur argues the problem is not that residential proxy networks exist, but rather that they are being embedded at scale in devices that most consumers do not think of as computers and are not equipped to audit.

“A one-time consent prompt buried in a TV app is not a substitute for meaningful transparency, ongoing control, and platform oversight,” Spur’s **Trevor Sutter** wrote. “The risk is amplified when consent comes from individuals within the household who use the device but shouldn’t give consent, such as minors.”

LG’s announcement that it is culling residential proxy SDKs from its app store is welcome news, but the company recently came under fire for another questionable partnership: Pimping McAfee security products via software drivers included in its high-end LCD monitors.

Earlier this week, the Youtube channel [Gamers Nexus](https://www.youtube.com/watch?v=Q9uefFYe6bM) showed that certain LG LCD monitors will automatically install [an app](https://apps.microsoft.com/detail/9pm9n6f47jb8?hl=en-US&gl=US) that promotes paid McAfee antivirus subscriptions, and that the app arrives through Windows Update without an approval prompt.

**Update, July 22, 1:06 p.m. ET:** Added statement from Bright Data.

*This entry was posted on Tuesday 21st of July 2026 09:10 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Internet of Things (IoT)](https://krebsonsecurity.com/category/internet-of-things-iot/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Bright Data](https://krebsonsecurity.com/tag/bright-data/) [John Taylor](https://krebsonsecurity.com/tag/john-taylor/) [LG Electronics USA](https://krebsonsecurity.com/tag/lg-electronics-usa/) [residential proxies](https://krebsonsecurity.com/tag/residential-proxies/) [Samsung](https://krebsonsecurity.com/tag/samsung/) [Spur](https://krebsonsecurity.com/tag/spur/) [Tizen](https://krebsonsecurity.com/tag/tizen/) [Trevor Sutter](https://krebsonsecurity.com/tag/trevor-sutter/) [webOS](https://krebsonsecurity.com/tag/webos/)

Post navigation

[← Microsoft Patches a Record 570 Security Flaws](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)

## 22 thoughts on “LG to Ban Residential Proxies from Smart TV Apps”

1. Robert Lane [July 21, 2026](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/#comment-658289)

   Good – residential proxy providers are scum.

   [Reply](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/?replytocom=658289#respond) →
2. The\_Mess [July 22, 2026](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/#comment-658291)

   Now if only they’d also stock forcing McAfee on PC users of their monitors via stealth windows updates and kill off the spyware on their smart TV’s that records everything you say and watch etc.

   [Reply](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/?replytocom=658291#respond) →

   1. mealy [July 22,...