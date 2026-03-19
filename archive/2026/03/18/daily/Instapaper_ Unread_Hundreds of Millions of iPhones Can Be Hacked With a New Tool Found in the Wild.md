---
title: Hundreds of Millions of iPhones Can Be Hacked With a New Tool Found in the Wild
url: https://www.wired.com/story/hundreds-of-millions-of-iphones-can-be-hacked-with-a-new-tool-found-in-the-wild/
source: Instapaper: Unread
date: 2026-03-18
fetch_date: 2026-03-19T04:20:59.606594
---

# Hundreds of Millions of iPhones Can Be Hacked With a New Tool Found in the Wild

[Skip to main content](#main-content)

Menu

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

Account

Account

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Podcasts](/podcasts/)

[Video](/video/)

[Livestreams](https://www.wired.com/livestreams)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Andy Greenberg](/author/andy-greenberg/)

[Security](/category/security)

Mar 18, 2026 10:00 AM

# Hundreds of Millions of iPhones Can Be Hacked With a New Tool Found in the Wild

A powerful iPhone-hacking technique known as DarkSword has been discovered in use by Russian hackers. It can take over devices running iOS 18 that simply visit infected websites.

![Image may contain Electronics Phone Mobile Phone Blade Razor Weapon Texting and Computer](https://media.wired.com/photos/69b86b74be9e27104c501c7c/3:2/w_2560%2Cc_limit/security_iphone_Getty.jpg)

Photo Illustration: WIRED Staff; Getty Images

Comment

Loader

Save StorySave this story

Comment

Loader

Save StorySave this story

iPhone hacking techniques have sometimes been described almost like rare and elusive animals: Hackers have used them so stealthily and carefully against such a small number of hand-picked targets that they're only rarely seen in the wild. Now a recent spate of [espionage and cybercriminal campaigns](https://www.wired.com/story/coruna-iphone-hacking-toolkit-us-government/) has instead deployed those same phone-takeover tools, embedded in infected websites, to indiscriminately hack phones by the thousands. And one new technique in particular—capable of taking over any of hundreds of millions of [iOS devices](https://www.wired.com/story/apple-ios-26-and-ipados-26-top-new-features/)—has appeared on the web in an easily reusable form, putting a significant fraction of the world's [iPhone](https://www.wired.com/gallery/iphone-buying-guide/) users at risk.

Researchers at Google and cybersecurity firms iVerify and Lookout on Wednesday [jointly](https://iverify.io/blog/darksword-ios-exploit-kit-explained) [revealed](https://www.lookout.com/threat-intelligence/article/darksword) the [discovery](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain) of a sophisticated iPhone hacking technique known as DarkSword that they've seen in use on infected websites, capable of instantly and silently hacking iOS devices that visit those sites. While the technique doesn't affect the latest, updated versions of iOS, it does work against iOS devices running versions of Apple's previous operating system release, iOS 18, which as of last month still accounted for close to a quarter of iPhones, [according to Apple's own count](https://developer.apple.com/support/app-store/).

“A vast number of iOS users could have all of their personal data stolen simply for visiting a popular website,” says Rocky Cole, iVerify's cofounder and CEO. “Hundreds of millions of people who are still using older Apple devices or older operating system versions remain vulnerable.”

The iPhone-hacking campaign that used DarkSword has come to light just two weeks after the revelation of another, even more sophisticated and fully featured [hacking toolkit known as Coruna](https://www.wired.com/story/coruna-iphone-hacking-toolkit-us-government/) was found in use by what Google describes as a Russian state-sponsored espionage group and other hacker groups. Although DarkSword appears to have been created by different developers from Coruna, the researchers found that it was used by those same Russian spies. Like Coruna, it too was embedded in components of otherwise legitimate Ukrainian websites, including online news outlets and a government agency site, to harvest data from visitors' phones.

Beyond this Russian spy campaign, according to Google, DarkSword was spotted earlier when hackers used it to compromise the phones of victims in Saudi Arabia, Turkey, and Malaysia. In the case of the Turkish and Malaysian targets, Google writes in its blog post that customers of the Turkish security and surveillance firm PARS Defense appear to have used the intrusion tool. All of that suggests that DarkSword has already proliferated to several different hacking groups, Google says, and more are likely to adopt it.

In fact, iVerify cofounder and researcher Matthias Frielingsdorf notes that the Russian hackers who most recently used DarkSword in their espionage campaign left the full, unobscured DarkSword code—complete with explanatory comments in English that describe each component and include the “DarkSword" name for the tool—available on those sites for anyone to access and reuse. That carelessness, he says, practically invites other hackers to pick up the tool and target other iPhone users. “Anyone who manually grabbed all the different parts of the exploit could put them onto their own web server and start infecting phones. It's as simple as that,” says Frielingsdorf. “It's all nicely documented, also. It's really too easy.”

An Apple spokesperson told WIRED in a statement that “every day Apple's security teams around the world work tirelessly to protect users' devices and data,” and noted that Apple had released security updates that would protect users from both Coruna and DarkSword, including emergency updates released last week for older devices that can't run iOS 26. “Keeping software up to date remains the single most important thing users can do to maintain the high security of their Apple devices,” the statement reads. Users who enable iOS's strictest security setting known as [Lockdown Mode](https://www.wired.com/story/apple-lockdown-mode-hands-on/) are also protected, the company added.

Google declined to comment beyond the blog post it released about its DarkSword findings. WIRED also reached out to PARS Defense via its X account but didn't immediately receive a response.

According to Lookout, DarkSword is designed to steal data from vulnerable iPhones that include passwords and photos; logs from iMessage, WhatsApp, and Telegram; browser history; Calendar and Notes data; and even data from Apple's Health app. Despite the apparent espionage focus of the hacking campaign, DarkSword also steals users' cryptocurrency wallet credentials, suggesting the hackers may have carried out a possible side business in for-profit cybercrime.

Rather than install spyware that persists on users' phones, DarkSword uses stealthier techniques that are more often seen in “fileless” malware that typically target Windows devices, hijacking the legitimate processes in an iPhone's operating system to steal data. “Instead of using a spyware payload to brute force your way through the file system—which leaves tons of artifacts of exploitation that are pretty easy to detect—this just uses system processes the way they're meant to be used,” iVerify's Cole says. “And it leaves far fewer traces.”

That fileless technique also means that a DarkSword infection doesn't persist on a phone after it reboots, Cole says. Instead, it steals data from the phone within the first few minutes after it's hacked—what he calls a “smash-and-grab” approach.

While the Coruna iOS hacking toolkit exposed earlier this month works against iOS versions 13 through 17, DarkSword works against most versions of iOS 18, the previous version of Apple's mobile operating system before the co...