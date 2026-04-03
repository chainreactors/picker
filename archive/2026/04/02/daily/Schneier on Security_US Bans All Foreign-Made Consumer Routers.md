---
title: US Bans All Foreign-Made Consumer Routers
url: https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html
source: Schneier on Security
date: 2026-04-02
fetch_date: 2026-04-03T04:29:00.509722
---

# US Bans All Foreign-Made Consumer Routers

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## US Bans All Foreign-Made Consumer Routers

This is for [new routers](https://docs.fcc.gov/public/attachments/DOC-420034A1.pdf); you don’t have to throw away your existing ones:

> The Executive Branch determination noted that foreign-produced routers (1) introduce “a supply chain vulnerability that could disrupt the U.S. economy, critical infrastructure, and national defense” and (2) pose “a severe cybersecurity risk that could be leveraged to immediately and severely disrupt U.S. critical infrastructure and directly harm U.S. persons.”

More [information](https://www.bbc.com/news/articles/c74787w149zo):

> Any new router made outside the US will now need to be approved by the FCC before it can be imported, marketed, or sold in the country.
>
> In order to get that approval, companies manufacturing routers outside the US must apply for conditional approval in a process that will require the disclosure of the firm’s foreign investors or influence, as well as a plan to bring the manufacturing of the routers to the US.
>
> Certain routers may be exempted from the list if they are deemed acceptable by the Department of Defense or the Department of Homeland Security, the FCC said. Neither agency has yet added any specific routers to its list of equipment exceptions.
>
> […]
>
> Popular brands of router in the US include Netgear, a US company, which manufactures all of its products abroad.
>
> One exception to the general absence of US-made routers is the newer Starlink WiFi router. Starlink is part of Elon Musk’s company SpaceX.

Presumably US companies will start making home routers, if they think this policy is stable enough to plan around. But they will be more expensive than routers made in China or Taiwan. Security is never free, but policy determines who pays for it.

Tags: [China](https://www.schneier.com/tag/china/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [hardware](https://www.schneier.com/tag/hardware/), [national security policy](https://www.schneier.com/tag/national-security-policy/)

[Posted on April 2, 2026 at 1:28 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html) •
[10 Comments](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html#comments)

### Comments

Who? •
[April 2, 2026 1:32 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453316)

Right now, I am not really sure US-manufactured devices are the most clever choice… better using open-source devices whose firmware has been written by an international team of qualified developers.

US has become an odd player in the international playground.

Who? •
[April 2, 2026 1:38 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453317)

U.S. corporations have a long history of bad practices, including installing backdoors on their own devices (Cisco, Juniper, Fortinet…); these ones are certainly not the devices I would consider for a secure environment.

Who? •
[April 2, 2026 1:49 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453318)

For consumer routers, I would choose a small open-source device with a suitable ONT, compatible with the service provider network, and operating system—either OpenWrt, for less technically savvy customers, or an OpenBSD-based design.

Chris •
[April 2, 2026 2:25 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453319)

Sounds like a great opportunity for the cartel…er, I mean administration…to set the stage for government surveillance.

KathyRo •
[April 2, 2026 3:16 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453320)

Security is never free.. and in this case it’s not even secure.

I wouldn’t trust the US government to keep their mitts off those routers under any administration but especially the current one.

Dumb questions •
[April 2, 2026 3:18 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453321)

Former Can PM Steve Harper’s gov banned huawei equipment years ago … I think security was the reason.

Who certifies that chinese made equipment doesnt have backdoors?

Who certifies that open source equipment doesnt have backdoors?

Arent all of these vulnerable to side channel attacks?

Arent any of these vulnerable if theyre unpatched, which they are likely unpatched because youre supposed to buy a new one rather than maintain the existing one?

i ask because honestly i dont know

You’d think monitoring your outbound traffic would be more important.

Felix •
[April 2, 2026 3:38 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#comment-453322)

So, my router was made in Taiwan for a Swedish company. I bought it directly, then loaded pfsense onto it for a few years, before switching to OPNSense.

It has been running great (limited only by the BSD Intel GigE support) for over a decade. Still, the up/down performance is faster than my internet connection, so I’m not planning to upgrade.

OPNsense seems to patch every 2 weeks. Not exactly consumer friendly, so I don’t see grandma changing. What will end up happening is that ISPs will get their rental routers approved, so they can charge $10/month rental fees and non-technical people will end up renting those.

A few companies will get a few models, no doubt the $300 models, through the Govt’s certification stuff. The $70 models won’t be available in the USA, so expect Canada and Mexico to have new profitable list of equipment for sale to US residents. It won’t just be Tylenol-3, but the $70 Asus routers too.

Asus has 9 more years on the FTC settlement which requires them to follow security best practices. I’ve been using an Asus wifi router as an AP for about 3 yrs. The older TP-Link router had support/pathes about 1 yr from TP-link. That taught me a huge lesson.

“Beware cheap network/computing devices made in China without a non-Chinese brand backing it up with a reputation at risk.” Chinese companies don’t seem to care much about their reputation. Companies that put their branding on Chinese-made equipment primarily to be sold in the USA definitely do care about their reputation. I’ve some some excellent customer service from those brands.

I’ve had issues with my wifi devices connecting to Netgear equipment. At the specific location with this issue, it was an issue for anyone not using MS-Windows or a iPhone. Everyone else had problems – so we replaced the wifi part of the netgear with Ubiquiti APs – which fixed everything.

TimH •
[April 2, 2026 4:06 PM](https://www.schneier.com/blog/archives/2026/04/us-bans-all-foreign-made-consumer-routers.html/#c...