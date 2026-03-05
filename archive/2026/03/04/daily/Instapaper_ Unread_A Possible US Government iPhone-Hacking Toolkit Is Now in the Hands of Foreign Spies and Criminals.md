---
title: A Possible US Government iPhone-Hacking Toolkit Is Now in the Hands of Foreign Spies and Criminals
url: https://www.wired.com/story/coruna-iphone-hacking-toolkit-us-government/
source: Instapaper: Unread
date: 2026-03-04
fetch_date: 2026-03-05T04:07:42.861927
---

# A Possible US Government iPhone-Hacking Toolkit Is Now in the Hands of Foreign Spies and Criminals

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

Mar 3, 2026 2:01 PM

# A Possible US Government iPhone-Hacking Toolkit Is Now in the Hands of Foreign Spies and Criminals

A highly sophisticated set of iPhone hijacking techniques has likely infected tens of thousands of phones or more. Clues suggest it was originally built for the US government.

![Image may contain Light Person Computer Electronics Laptop and Pc](https://media.wired.com/photos/69a5fee53552f3bcbc80c606/1:1/w_2560%2Cc_limit/sec-phone-hacking-2252317890.jpg)

Photo-Illustration: Wired Staff; QI YANG/Getty Images

Save StorySave this story

Save StorySave this story

An iPhone-hacking technique used in the wild to indiscriminately hijack the devices of any [iOS](https://www.wired.com/tag/ios/) user who merely visits a website represents a rare and shocking event in the cybersecurity world. Now one powerful hacking toolkit at the center of multiple mass [iPhone](https://www.wired.com/story/the-untold-story-of-the-birth-of-the-iphone-david-pogue-book-excerpt/) exploitation campaigns has taken an even rarer and more disturbing path: It appears to have traveled from the hands of Russian spies who used it to target Ukrainians to a cybercriminal operation designed to steal cryptocurrency from Chinese-speaking victims—and some clues suggest it may have been originally created by a US contractor and sold to the American government.

Security researchers at Google on Tuesday [released a report](https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit) describing what they're calling “Coruna,” a highly sophisticated iPhone hacking toolkit that includes five complete hacking techniques capable of bypassing all the defenses of an iPhone to silently install malware on a device when it visits a website containing the exploitation code. In total, Coruna takes advantage of 23 distinct vulnerabilities in iOS, a rare collection of hacking components that suggests it was created by a well-resourced, likely state-sponsored group of hackers.

In fact, Google traces components of Coruna to hacking techniques it spotted in use in February of last year and attributed to what it describes only as a “customer of a surveillance company.” Then, five months later, Google says a more complete version of Coruna reappeared in what appears to have been an espionage campaign carried out by a suspected Russian spy group, which hid the hacking code in a common visitor-counting component of Ukrainian websites. Finally, Google spotted Coruna in use yet again in what seems to have been a purely profit-focused hacking campaign, infecting Chinese-language crypto and gambling sites to deliver malware that steals victims’ cryptocurrency.

Conspicuously absent from Google's report is any mention of who the original surveillance company “customer” that deployed Coruna may have been. But the mobile security company iVerify, which also analyzed a version of Coruna it obtained from one of the infected Chinese sites, suggests the code may well have started life as a hacking kit built for or purchased by the US government. Google and iVerify both note that Coruna contains multiple components previously used in a [hacking operation known as “Triangulation”](https://www.wired.com/story/kaspersky-apple-ios-zero-day-intrusion/) that was discovered targeting Russian cybersecurity firm Kaspersky in 2023, which the Russian government claimed was the work of the NSA. (The US government didn’t respond to Russia’s claim.)

Coruna's code also appears to have been originally written by English-speaking coders, notes iVerify's cofounder Rocky Cole. “It's highly sophisticated, took millions of dollars to develop, and it bears the hallmarks of other modules that have been publicly attributed to the US government," Cole tells WIRED. “This is the first example we’ve seen of very likely US government tools—based on what the code is telling us—spinning out of control and being used by both our adversaries and cybercriminal groups.”

An “EternalBlue Moment”

Regardless of Coruna's origin, Google warns that a highly valuable and rare hacking toolkit appears to have traveled through a series of unlikely hands, and now exists in the wild where it could still be adopted—or adapted—by any hacker group seeking to target iPhone users.

“How this proliferation occurred is unclear, but suggests an active market for ‘second hand’ zero-day exploits,” Google's report reads, using the term zero-day to refer to secret hacking techniques that exploit unpatched vulnerabilities. “Beyond these identified exploits, multiple threat actors have now acquired advanced exploitation techniques that can be reused and modified with newly identified vulnerabilities.”

iVerify's Cole notes that if Coruna actually began life as a tool intended for the US government, though, it also raises questions about the security of mobile devices in a world where highly sophisticated hacking tools created for or sold to the American government can leak to adversaries. “This is the EternalBlue moment for mobile malware,” says Cole. [EternalBlue](https://www.wired.com/story/eternalblue-leaked-nsa-spy-tool-hacked-world/) is the Windows-hacking tool stolen from the National Security Agency and leaked in 2017, leading to its use in catastrophic cyberattacks, including North Korea's [WannaCry](https://www.wired.com/tag/wannacry/) worm and Russia's [NotPetya](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/) attack.

Google notes that Apple patched vulnerabilities used by Coruna in the latest versions of its mobile operating system, [iOS 26](https://www.wired.com/story/apple-iphone-ios-18-ipados-18-new-features/), so its exploitation techniques are only confirmed to work against iOS 13 through 17.2.1. It targets vulnerabilities in Apple's Webkit framework for browsers, so Safari users on those older versions of iOS would be vulnerable, but there's no confirmed techniques in the toolkit for targeting Chrome users. Google also notes that Coruna checks if an iOS devices has Apple's most stringent security setting, known as [Lockdown Mode](https://www.wired.com/story/apple-lockdown-mode-hands-on/), enabled, and doesn’t attempt to hack it if so.

Despite those limitations, iVerify says Coruna likely infected tens of thousands of phones. The company consulted with a partner that has access to network traffic and counted visits to a command-and-control server for the cybercriminal version of Coruna infecting Chinese-language websites. The volume of those connections suggest, iVerify says, that roughly 42,000 devices may have already been hacked with the toolkit in the for-profit campaign alone.

Just how many other victims Coruna may have hit, including Ukrainians who visited websites infected with the code by the suspected Russian espionage operation, remains unclear. Google declined to comment beyond its published report. Apple did not immediately provid...