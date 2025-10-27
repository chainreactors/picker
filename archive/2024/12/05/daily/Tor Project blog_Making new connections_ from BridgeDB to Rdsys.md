---
title: Making new connections: from BridgeDB to Rdsys
url: https://blog.torproject.org/making-connections-from-bridgedb-to-rdsys/
source: Tor Project blog
date: 2024-12-05
fetch_date: 2025-10-06T19:42:04.355769
---

# Making new connections: from BridgeDB to Rdsys

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Making new connections: from BridgeDB to Rdsys

by [meskio](/author/meskio) and [pavel](/author/pavel)
| December 4, 2024

![](/making-connections-from-bridgedb-to-rdsys/lead.png)

For over a decade, BridgeDB was the reluctant champion helping users bypass censorship and connect to the open web. [Released more than 11 years ago as a prototype](https://gitlab.torproject.org/tpo/anti-censorship/bridgedb/-/tags/bridgedb-0.0.1), the bridge distribution mechanism surpassed its original lifespan, honorably serving the Tor community. However, as censorship techniques evolved, BridgeDB became overburdened with the many updates necessary to adapt to these new challenges. Over time, this led to an accumulation of technical debt and outdated code which made further improvements and maintenance increasingly difficult. It became clear that to keep up with the dynamic nature of anti-censorship work, Tor needed a more robust, flexible and easier to maintain solution.

**Enter Rdsys:** the next-generation bridge distribution system. Developed from the ground up, it incorporates the learnings from over 15 years of anti-censorship work to overcome the limitations of its predecessor. In October 2024, Tor completed the migration to Rdsys, retiring Bridge DB. This transition ensures a more flexible, maintainable, and user-friendly approach to bridge distribution, strengthening Tor's ability to counter censorship and making the web more accessible to those who need it most.

## Learning from the past

When Tor was first adopted by people circumventing censorship, it quickly became a target for censors. Blocking the public list of Tor relays was an easy way to cut off access. The solution? Bridges---relays that aren't listed publicly to make it harder for censors to block access to Tor. But as soon as bridges were introduced, two challenges emerged: how to disguise bridge traffic and how to distribute bridges securely without exposing them to censors.

While the former was addressed with different [bridge types](https://youtu.be/8mdtSgHWhXY), BridgeDB addressed the latter: It needed to give legitimate users access to bridges while making it difficult for censors to obtain the entire list. So, it employed several distribution mechanisms, including web-based or email requests, and a Tor Browser API called MOAT. Users could either obtain bridge addresses through a website and by requesting them via email, or by solving captchas.

These approaches allowed for some degree of censorship protection, but they weren't foolproof. Censors could still attempt to scrape websites, flood the email system to collect bridges, or bypass them by leveraging human CAPTCHA-solving services.

As censorship tactics became more sophisticated, we kept adding to its original code base, resulting in an accumulation of technical debt. While it was a great solution at the time, BridgeDB grew increasingly difficult to maintain.

## Pathing towards the future

Recognizing BridgeDB's limitations, we began developing Rdsys as a replacement four years ago. Unlike its predecessor, Rdsys is built as a modular system, dividing responsibilities into separate components--such as distribution logic and communication methods (e.g., email, Telegram)--that work together seamlessly. This architecture lets us experiment with new ideas and, eventually, adapt to emerging threats without overhauling the entire system:

### Exploring new distribution channels

Rdsys enabled us to explore bridge distribution channels by leveraging platforms widely used in censored regions. For example, in response to increasing censorship in Russia, we successfully distributed bridges through Telegram. This approach takes advantage of account history, distinguishing between old and new accounts to ensure bridges are given to real users, not bots or censors creating accounts en masse.

### Adding new tools

The modular design allows us to test and deploy new anti-censorship tools more rapidly to stay ahead of evolving tactics. [Lox](https://gitlab.torproject.org/tpo/anti-censorship/lox), for instance, is a bridge distribution mechanism that detects blocked bridges and uses a reputation-based approach rewarding users whose bridges remain unblocked.

### Eliminating the hassle of captchas

For many, captchas are frustratingly inaccessible, presenting challenges for users with disabilities, those who rely on screen readers, or individuals using older devices with limited capabilities. For some users, solving captchas can even be impossible due to language barriers or overly complex visual puzzles, creating a bottleneck in their efforts to connect to the open web.Â

Beyond user experience, captchas have also become increasingly ineffective as a security measure. Censors have adapted to them, employing automated tools or other methods to bypass these obstacles. This renders captchas less of a deterrent for those aiming to restrict access while maintaining their burden on legitimate users.

By shifting away from captchas, Rdsys improves the accessibility and reliability of Tor bridges, ensuring that more users--particularly those in regions facing heavy censorship--can connect without unnecessary roadblocks.Â

## What's next?

Looking ahead, the goal is not just to maintain access to the internet, but to expand it. This is where you, dear reader, come in!

Earlier this year, [we launched Webtunnel](https://blog.torproject.org/introducing-webtunnel-evading-censorship-by-hiding-in-plain-sight/), a new bridge type that blends itself into other web traffic. This was made possible in part through new systems like Rdsys, but mostly by the power of thousands of volunteers, contributors, and [alpha testers](https://community.torproject.org/user-research/become-tester/) who are committed to empowering internet users worldwide to reclaim their right to [speak, browse, and search anonymously](https://blog.torproject.org/2024-fundraiser-donations-matched/).

Now, [we are calling on the Tor and Internet freedom community once again to help us scale Tor's anti-censorship efforts.](https://blog.torproject.org/call-for-webtunnel-bridges/) If you've ever thought about contributing to [Tor's development](https://torproject.org/donate/donate-fb-2024) or of [running a Tor bridge](https://community.torproject.org/relay/setup/webtunnel/), today is the day. Together, we can ensure that everyone, everywhere has access to a free and open internet.

[![Donate Button](/making-connections-from-bridgedb-to-rdsys/donate-button.png)](https://torproject.org/donate/donate-bp5-yec2024)

* [circumvention](/category/circumvention)
* [community](/category/community)
* [releases](/category/releases)
* [human rights](/category/human-rights)
* [announcements](/category/announcements)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/making-connections-from-bridgedb-to-rdsys/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/making-connections-from-bridgedb-to-rdsys/&text=Introducing%20Rdsys%3A%20the%20next-generation%20bridge%20distribution%20system%2C%20designed%20from%20the%20ground%20up%20for%20a%20more%20flexible%2C%20maintainable%2C%20and%20user-friendly%20approach%20to%20bridge%20distribution.%20As%20of%20October%202024%2C%20the%20Tor%20Project%20has%20retired%20its%20predecessor%2C%20Bridge%20DB.%20Find%20out%20more%20about%20why%20and%20the%20lessons%20learned%20from%20over%2015%20years%20of%20anti-censorship%20work.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/making-connections-from-bridgedb-to-rdsys/&text=Introducing%20Rdsys%3A%20the%20next-generation%20bridge%20distribution%20sys...