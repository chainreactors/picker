---
title: A hacker group is poisoning open source code at an unprecedented scale
url: https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/
source: Instapaper: Unread
date: 2026-05-27
fetch_date: 2026-05-28T06:03:53.138381
---

# A hacker group is poisoning open source code at an unprecedented scale

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

[Andy Greenberg](/author/andy-greenberg/) [Lily Hay Newman](/author/lily-hay-newman/)

[Security](/category/security)

May 21, 2026 5:00 AM

# A Hacker Group Is Poisoning Open Source Code at an Unprecedented Scale

GitHub is just the latest victim of TeamPCP, a gang that has carried out a spree of software supply chain attacks that has impacted hundreds of organizations.

![Collage of a burglar and a supply chain](https://media.wired.com/photos/6a0e3f41387ce528c0f138b0/master/w_2560%2Cc_limit/security_teampcp_supply_chain_hack.jpg)

Photo-illustration: WIRED Staff; Getty Images

Comment

Loader

Save StorySave this story

Comment

Loader

Save StorySave this story

A so-called software [supply chain attack](https://www.wired.com/story/the-untold-story-of-solarwinds-the-boldest-supply-chain-hack-ever/), in which hackers corrupt a legitimate piece of software to hide their own malicious code, was once a relatively rare event but one that haunted the cybersecurity world with its insidious threat of turning any innocent application into a dangerous foothold in a victim’s network. Now [one group of cybercriminals](https://www.wired.com/story/meta-pauses-work-with-mercor-after-data-breach-puts-ai-industry-secrets-at-risk/) has turned that occasional nightmare into a near-weekly episode, corrupting hundreds of open source tools, extorting victims for profit, and sowing a new level of distrust in an entire ecosystem used to create the world’s software.

On Tuesday night, open source code platform GitHub announced that it had been breached by hackers in one such software supply chain attack: A GitHub developer had installed a “poisoned” extension for VSCode, a plug-in for a commonly used code editor that, like GitHub itself, is owned by Microsoft. As a result, the hackers behind the breach, an increasingly notorious group called TeamPCP, claim to have accessed around 4,000 of GitHub’s code repositories. GitHub’s statement confirmed that it had found at least 3,800 compromised repositories while noting that, based on its findings so far, they all contained GitHub’s own code, not that of customers.

“We are here today to advertise GitHub’s source code and internal orgs for sale,” TeamPCP wrote on BreachForums, a forum and marketplace for cybercriminals. “Everything for the main platform is there and I very am happy to send samples to interested buyers to verify absolute authenticity.”

The GitHub breach is just the latest incident in what has become the longest-running spree of software supply chain attacks ever, with no end in sight. According to cybersecurity firm Socket, which focuses on software supply chains, TeamPCP has, in just the last few months, carried out 20 “waves” of supply chain attacks that have hidden malware in more than 500 distinct pieces of software, or well over a thousand counting all of the various versions of the code that TeamPCP has hijacked.

Those tainted pieces of code have allowed TeamPCP’s hackers to breach hundreds of companies that installed the software, says Ben Read, who leads strategic threat intelligence at the cloud security firm Wiz. GitHub is only the latest on the group’s long list of victims, which has also included AI firm OpenAI and the data contracting firm Mercor. “It may be their biggest one," Read says of the GitHub breach. “But each one of these is a big deal for the company that it happens to. It's not qualitatively different from the 14 breaches that happened last week.”

TeamPCP’s core tactic has become a kind of cyclical exploitation of software developers: The hackers gain access to a network where an open source tool commonly used by coders is being developed—for example, the VSCode extension that led to the GitHub breach or the data visualization software AntV that TeamPCP hijacked earlier this week. The hackers plant malware in the tool that ends up on other software developers’ machines, including some who are writing other tools intended to be used by coders.

The malware allows TeamPCP’s hackers to steal credentials that let them publish malicious versions of *those* software development tools, too. The cycle repeats, and TeamPCP’s collection of breached networks grows. “It’s a flywheel of supply chain compromises,” says Read. “It’s self-perpetuating, and it’s been a hugely successful way to get access to networks and steal stuff.”

Most recently, the group appears to have automated many of its software supply chain attacks with a self-spreading worm that’s come to be known as Mini Shai-Hulud. The name comes from GitHub repositories the worm creates that include encrypted credentials stolen from victims, each of which includes the phrase “A Mini Shai-Hulud Has Appeared” along with a handful of other references to the sci-fi novel *Dune*. That message in turn appears to be a reference not just to *Dune*’s sandworms but to a similar [supply chain compromise worm known as Shai-Hulud that appeared in September](https://www.wired.com/story/a-dangerous-worm-is-eating-its-way-through-software-packages/), though there’s no evidence TeamPCP was behind that earlier self-spreading malware.

“They’re definitely going for big exposure. They really care about getting big attention,” says Philipp Burckhardt, who leads research at Socket and has tracked TeamPCP for months. “They like to toot their own horn.” A dark-web site for the group, which links to “business contacts” likely used to carry out ransom negotiations, features *Matrix*-style cascading ones and zeros, a reggae fusion soundtrack, and the words “TEAMPCP: The Cats Hijacking Your Supply Chains.”

Before landing on its current strategy for supply chain attacks, TeamPCP emerged in late 2025 exploiting cloud misconfigurations and a vulnerability in the web app development tool Next.js to deploy a botnet for attacks like credential theft and cryptocurrency mining. The group’s reliance on worms emerged during this time with increasing success grabbing static credentials and authentication tokens to bore deeper into victims’ systems.

“It’s been like wildfire; it’s gone very fast,” says Nathaniel Quist, manager of the Cortex Cloud intelligence team at Palo Alto Networks. “They find credentials, personal access tokens, and then it’s just how far can one credential go. I think we will continue to see these techniques. Threat actors know they work, and they’re running with it.”

TeamPCP appears to be financially motivated and often deploys ransomware or data extortion campaigns against its targets, though it also appears willing to sell victims’ data to any buyer. In the most recent case of GitHub, for instance, it wrote on its BreachForums site that “this is not a ransom. We do not care about extorting GitHub, 1 buyer and we shred the data on our end.”

It added what appeared to be a veiled threat to GitHub, perhaps intended to coerce the company to pay: “It looks like our retirement is soon so if no buyer is found we will leak it free.”

The picture has become increasingly complex, Quist says, since Te...