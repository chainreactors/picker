---
title: An undercover Google analyst infiltrated a notorious supply-chain hacking gang
url: https://www.wired.com/story/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/
source: Instapaper: Unread
date: 2026-09-20
fetch_date: 2026-09-21T07:27:39.967292
---

# An undercover Google analyst infiltrated a notorious supply-chain hacking gang

[Skip to main content](#main-content)

[THE WIRED APP IS HERE](https://www.wired.com/app?utm_id=site_ribbon)

[DOWNLOAD NOW »](https://www.wired.com/app?utm_id=site_ribbon)

Menu

[WIRED](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[WIRED](/)

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

[WIRED Store](https://shop.wired.com/)

[SearchSearch](/search/)

[Andy Greenberg](/author/andy-greenberg/)

[Security](/category/security)

Sep 18, 2026 12:00 PM

# An Undercover Google Analyst Infiltrated a Notorious Supply-Chain Hacking Gang

TeamPCP pulled off the worst-ever software supply-chain hacking spree and breached thousands of companies. Now Google’s threat intelligence group has revealed it had a mole inside the hackers’ inner circle.

![An Undercover Google Analyst Infiltrated a Notorious SupplyChain Hacking Gang](https://media.wired.com/photos/6aac35420820a9282b5f1721/master/w_2560%2Cc_limit/Security_An%2520Undercover%2520Google%2520Researcher%2520Infiltrated%2520the%2520Gang%2520Behind%2520the%2520Worst-Ever%2520Supply%2520Chain%2520Hacking%2520Spree_v1.jpg)

Photo-Illustration: Jobanny Cabrera; Getty Images

Comment

Loader

Save StorySave this story

Comment

Loader

Save StorySave this story

Before two of its alleged members were arrested and charged in Australia last month, the hacker group known as TeamPCP [carried out a hacking spree](https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/) unlike any other in history. It tainted hundreds of open-source programs with its malware, stole developer accounts to perpetuate that software supply-chain hacking, and even released a [*Dune*-themed self-spreading worm](https://www.wired.com/story/a-dangerous-worm-is-eating-its-way-through-software-packages/) to automate the process, ultimately breaching more than a thousand companies.

Now Google’s threat intelligence group has revealed that during a key moment of TeamPCP’s rampage, the company’s own undercover researcher had infiltrated the group—allowing Google to monitor the hacking spree from the inside, warn breach targets, and even help disrupt the group’s attempts to exploit those victims.

In a talk at security firm SentinelOne's LABScon research conference today, Google Threat Intelligence Group researcher Austin Larsen will present details on the company’s investigation—and infiltration—of TeamPCP amidst the group’s unprecedented, chaotic supply-chain hacking campaign. According to Larsen, Google eventually followed a trail of operational security mistakes allegedly made by one of the two Australians now accused of being leading members of the hacker group and passed on key identifying details to law enforcement. The company also received intelligence from ShinyHunters, another infamous cybercriminal group that TeamPCP partnered with, but which later turned on the supply-chain hackers. And perhaps most surprisingly, Larsen says that Google’s security subsidiary Mandiant had an undercover analyst—not himself—within the group’s inner circle from almost the beginning of TeamPCP’s time in the spotlight.

“One of our personas had been working for many months to build trust with one of the actors that was invited to join TeamPCP, and so was added to the group,” Larsen told WIRED in an interview ahead of his LABScon talk. “So essentially, almost day one, Mandiant was watching everything behind the scenes.”

## The TeamPCP Mole

Late last month, Ruben Ian Thomson and Louis Michael Gaebler, both Australians in their early twenties, were arrested by Australian police in a joint investigation with assistance from the FBI, charged with hacking crimes, and described by the Australian Federal Police (AFP)—in a press release that, due to Australian privacy laws, did not name them—as “principal participants” in TeamPCP. The hacker group, which seems to have first appeared online in late 2025, had made headlines with a [brazen string of cascading supply-chain attacks](https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/): It repeatedly compromised open-source software to hide its malware, which then allowed it to hijack the credentials of software developers and plant its malicious code in yet another widely used tool, in a repeating cycle.

Starting this spring, for instance, TeamPCP compromised the open-source security scanner Trivy, the AI application programming interface tool LiteLLM, infrastructure of the web application security firm Checkmarx, the web app library TanStack, and the enterprise AI platform Mistral AI. Those repeated supply-chain attacks, with each enabling the group to cast its net again for more victims, ultimately allowed the hackers to breach open-source code repository Github, data contracting firm Mercor, and employee devices at OpenAI, the European Commission, and many others who have remained unnamed in public reporting. At times, the group deployed a worm known as Mini Shai-Hulud, named after the sandworms in *Dune*, to automate its hacking and scale up to even more victims. (The name also seemed to refer to an earlier Shai-Hulud worm that hackers designed to try a similar approach in September 2025, though it’s still not clear if TeamPCP or any of its alleged members were involved in that earlier intrusion campaign.)

Larsen now says that in March, just as TeamPCP was beginning its frenzied supply-chain hacking, Google’s own undercover analyst was invited to join the hackers’ inner circle. That inside source, whose name Larsen declined to reveal, was one of about 12 members of the group given access to a core chat that TeamPCP called CanisterWorm.

“You guys should understand that we pulled off the biggest supplychain [sic] maybe ever recorded in modern history,” one TeamPCP member wrote in the leaked chats.

Michael Fletcher, a former AFP analyst who now works in the threat research division of an Australian telecom firm, says he approached Larsen around that time about methods for monitoring the group’s members and activities. He says that Larsen responded by asking Fletcher to approach the hackers with caution because one of them was a “friendly,” Fletcher remembers. “I thought, damn, you all have been inside this *early*,” he says.

Google’s undercover analyst, Larsen says, gained access to a server where TeamPCP was storing its trove of credentials stolen from its many victims: the usernames, passwords, and access tokens it had obtained through its hacking and seemingly planned to use to extort target companies. So Google’s team decided to take action to warn victims and prevent TeamPCP’s ransom scheme. “My thought was: How can we, as quickly as possible, disrupt their campaign before more compromises can happen?” Larsen says. “Let's go mess up what they're doing. That was my goal.”

Rather than focus on alerting the owners of the stolen credentials at victim companies directly, which Larsen says would have taken too long given the sheer number of breached companies, Google first reached out to providers where those credentials could be used, like Amazon Web Services and Microsoft, to have the credentials revoked and prevent the hackers from exploiting them. Larsen and his team sent out hundreds of notifi...