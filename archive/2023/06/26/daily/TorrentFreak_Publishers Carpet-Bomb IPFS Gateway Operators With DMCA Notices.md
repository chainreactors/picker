---
title: Publishers Carpet-Bomb IPFS Gateway Operators With DMCA Notices
url: https://torrentfreak.com/publishers-carpet-bomb-ipfs-gateway-operators-with-dmca-notices-230625/
source: TorrentFreak
date: 2023-06-26
fetch_date: 2025-10-04T11:47:58.207364
---

# Publishers Carpet-Bomb IPFS Gateway Operators With DMCA Notices

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# Publishers Carpet-Bomb IPFS Gateway Operators With DMCA Notices

June 25, 2023 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [DMCA](https://torrentfreak.com/category/anti-piracy/dmca/ "Go to the DMCA category archives.") >

The Interplanetary File System provides technical resilience against censorship but, for those who offer IPFS gateways, pressure to self-censor is mounting. Reports indicate that major publishing companies are carpet-bombing these volunteers with tens of thousands of DMCA notices, despite being fully aware that they are not responsible for the content in question and cannot take it down. One gateway operator has already called it quits.

[![ipfs-l](https://torrentfreak.com/images/ipfs-l.png)](https://torrentfreak.com/images/ipfs-l.png)[IPFS](https://ipfs.tech/#install) is a decentralized network that makes it possible to efficiently distribute high volumes of data between peers while avoiding downtime associated with regular hosting outages.

The IPFS project describes the system as a *peer-to-peer hypermedia protocol designed to preserve and grow humanity’s knowledge by making the web upgradeable, resilient, and more open*. Anyone who values these qualities is invited to come along for the ride [using free, open source tools](https://ipfs.tech/#install).

## IPFS Gateways

For those who prefer not to install software but would still like to access content stored on IPFS, web gateways provide streamlined access to IPFS with zero fuss. IPFS gateways tend to be run by supporters and enthusiasts who charge nothing for their time and usually pay all of the bills.

Examples can be [found here](https://ipfs-public-gateway-checker.on.fleek.co/) but in broad terms, public gateways aren’t particularly numerous. [As reported in March](https://torrentfreak.com/cloudflare-disables-access-to-pirated-content-on-its-ipfs-gateway-230324/), Cloudflare offers a free IPFS gateway yet despite having nothing to do with the content hosted in the network, still received over 1,000 copyright complaints in the first half of 2022.

Figures for the second half are yet to be published but if recent events are anything to go by, those numbers could be significantly higher in the next report.

## Avalanche of Copyright Complaints

UK-based programmer James Stanley has a [project page](https://incoherency.co.uk/blog/pages/projects.html) to make any geek smile. It begins with SCAMP, a homemade 16-bit CPU with a homemade programming language, before moving on to a robotic chessboard (accessible via API), and a footwear-based chess computer that allows Stanley to cheat at chess “hands-free and without any third-party assistance.”

Stanley is also the brains behind [Hardbin.com](https://github.com/jes/hardbin/), an encrypted pastebin-type service that utilizes IPFS. Unfortunately, Stanley took Hardbin down this week after being targeted by an anti-piracy entity demanding the removal of thousands of allegedly-infringing URLs.

“I received 3 DMCA takedown emails today, covering 7350 URLs on my hardbin.com IPFS gateway. The URLs were allegedly serving infringing copies of books,” his [blog post](https://incoherency.co.uk/blog/stories/hardbin-fake-takedowns.html) reads.

Heavily truncated sample notice[![ciu-online-complaint](https://torrentfreak.com/images/ciu-online-complaint.png)](https://torrentfreak.com/images/ciu-online-complaint.png)

Stanley posted the complaints to GitHub, with all three following a similar format; a demand for the immediate takedown of thousands of pieces of content that have nothing to do with the programmer, that he has no ability to take down, even if he wanted to.

## Who’s Behind The Takedown Demands?

All three complaints ([1](https://gist.github.com/jes/51496baaa48610f1b59a39804fd28df9),[2](https://gist.github.com/jes/597cf1fa84067586c906ac1d8c605f20),[3](https://gist.github.com/jes/f32147236874ef736be6190c2cce4a3d)) were sent from “[[email protected]](/cdn-cgi/l/email-protection)” but as Stanley points out, it’s hard to say who is behind the notices.

Each notice claims to have been sent by ‘Gareth Young – Internet Investigator’ but where Young works isn’t made clear. Instead, the notices carry the names and addresses of three publishing companies; Wolters Kluwer Health (New York), Knovel, a subsidiary of Elsevier, Inc. (New York), and IEEE (new Jersey).

Stanley’s research turned up a ‘Gareth Young’ who apparently worked for law firm Covington & Burling LLP. Young is also the author of a [slideshow](https://documents.pub/document/gareth-young-creating-a-global-internet-anti-piracy-strategy.html?page=11) that describes methods and tactics for taking infringing content down and making people’s lives more difficult.

[![ipfs-hard-work](https://torrentfreak.com/images/ipfs-hard-work.png)](https://torrentfreak.com/images/ipfs-hard-work.png)

The page above contains numerous options, and just as Mr Young suggested, the 5th option did indeed prove effective.

“I have now taken hardbin.com down completely because dealing with this sort of thing makes it less fun to run and more like hard work,” Stanley says.

## IPFS: *Technical* Resilience Against Censorship

That Stanley’s work on Hardbin can’t be enjoyed by him or anyone else shows that it’s still possible to have a chilling effect on IPFS, despite its technical resilience to censorship.

It’s also worth noting that the DMCA takedown notices were sent directly to abuse addresses at the programmer’s host, rather than to him directly. It’s the kind of tactic that’s easily justified when dealing with an uncooperative pirate site but entirely unhelpful when dealing with innocent parties.

And then there’s the interesting evidence uncovered by Stanley when cross-referencing the 7,350 URLs against his reverse proxy logs.

“I did some bash-fu to extract the IPFS hashes from the emails and grep for them in my nginx logs, and was surprised to find not a single match,” Stanley explains. “None of them have ever been accessed, and of the ones that I checked, none even worked.”

## Other IPFS Users Targeted

Sean Lang has been [keeping records](https://github.com/notslang/ipfs-gateway-dmca-requests) on the DMCA notices he’s received related to his gateway since February 2022.

“I currently operate an IPFS gateway on ipfs.slang.cx. I don’t publish or pin any content there, it’s only a resolver for content that’s available on the rest of the IPFS network,” Lang writes on GitHub.

“I get a lot of DMCA requests from running this. Currently I’m blocking 12367 files. They’re almost all books, although I don’t have nearly enough time to go through them manually.”

Lang says that the takedown notices are usually sent by a guy called Gareth Young and have at least one familiar quality.

“The weird thing is, [the system used] doesn’t actually verify that a given file is available through my server before sending a DMCA request. I’ve looked through the traffic logs, and the vast majority of the files listed in these takedown requests have never been requested in the history of my gateway....