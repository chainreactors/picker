---
title: Reviewing the Cryptography Used by Signal
url: https://soatok.blog/2025/02/18/reviewing-the-cryptography-used-by-signal/
source: Dhole Moments
date: 2025-02-19
fetch_date: 2025-10-06T20:47:24.058309
---

# Reviewing the Cryptography Used by Signal

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/) [Open Source](https://soatok.blog/category/technology/open-source/) [Software Security](https://soatok.blog/category/technology/software-security/)

# Reviewing the Cryptography Used by Signal

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [February 18, 2025](https://soatok.blog/2025/02/18/reviewing-the-cryptography-used-by-signal/)

![Reviewing the Cryptography Used by Signal](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/02/BlogHeader-2025-Signal.png?fit=1200%2C675&ssl=1)

Last year, I [urged furries to stop using Telegram](https://soatok.blog/2024/05/14/its-time-for-furries-to-stop-using-telegram/) because it doesn’t actually provide them with any of the privacy guarantees they *think* it gives them. Instead of improving Telegram’s cryptography to be actually secure, the CEO started spreading misleading bullshit about Signal[®](#trademark).

Since then, I’ve been flooded with people asking me about [various other encrypted messaging apps](https://soatok.blog/encrypted-messaging-apps/) and accused by Internet reply-guys of having malicious intentions. Some of the more egregiously stupid accusations were that I was somehow being paid to promote Signal.

> Not only am I not being paid to promote Signal, I refuse to ever be paid to promote *anything* ever! **I’ve been [extremely](https://soatok.blog/2024/07/02/my-furry-blog-is-not-an-opportunity-to-develop-your-brand/) [vocal](https://soatok.blog/2021/05/18/avoiding-the-frigid-hellscape-of-online-marketing/) [about](https://soatok.blog/2024/12/26/roasted-christmas-spam-from-muhu-ai/) [this](https://soatok.blog/2021/12/29/for-your-infurmation/#:~:text=Ad%20revenue%3A%20Still%20%240)**.

To be clear, being accused of being a paid shill for recommending Signal isn’t exactly unique to Signal, it also happens with other technologies.

For example: Have you ever wondered by influencers (streamers, vloggers, etc.) always promote “[VPN services](https://gist.github.com/joepie91/5a9909939e6ce7d09e29)” instead of Tor (which is free)?

It’s not just “today’s sponsor”, either.

Bad security advice, usually [marketed as infosec advice for activists](https://web.archive.org/web/20250207173047/https%3A//infosecforactivists.org/), absolutely *loves* to recommend specific VPN companies. Interestingly, they frequently make no mention of Tor. When you point this out, the same crowd will [try to weasel in FUD about Tor](https://ghostarchive.org/archive/25M1U).

> **Soatok**: That they recommend a VPN and not Tor in their first table immediately makes me suspicious.
>
> [Archive.org mirror](https://web.archive.org/web/20250211092400/https%3A//news.ycombinator.com/item?id=42941848)

> **First Reply:** Why? I’ve personally seen more news articles about Tor users getting de-anonymized than I have VPN users. […]

The rhetorical sleight-of-hand here isn’t particularly clever.

* Tor uses onion-routing to provide anonymity to Internet traffic.
* VPNs just provide an encrypted tunnel to another ISP, and therefore do not offer anonymity.
* You can’t *deanonymize* VPN users because they were never *anonymized* to begin with!
* [VPN providers that lied about “no logs”](https://www.theregister.com/2011/09/26/hidemyass_lulzsec_controversy/) never faced any meaningful consequences.

Tor is at least as private as any VPN. If you’re worried about exit nodes, only use Tor to access Onion Services or websites that use HTTPS.

![Drakeposting No Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-07.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

As a security engineer that specializes in applied cryptography, I’m generally not interested in the “Tor vs VPN” debate.

I’m *much* more interested in the “WireGuard vs OpenVPN” debate (on the side of WireGuard), and what lessons about software security the rest of the industry could learn from WireGuard.

In fact: If someone is promoting a VPN service in 2025 and that service doesn’t use WireGuard as its underlying protocol, they are almost certainly LARPing at security expertise rather than offering valuable advice.

> EDIT: I don’t currently have an opinion on [MASQUE](https://blog.cloudflare.com/masque-building-a-new-protocol-into-cloudflare-warp/).
>
> I don’t really keep up with everything Cloudflare does, unless it involves post-quantum cryptography.

But I digress.

Like Tor, Signal doesn’t cost you anything to use. Nobody makes money by telling you to use either of those things.

Despite having no financial incentive for doing so, security and privacy experts (including [the EFF’s director of cybersecurity, Eva Galperin](https://www.cnn.com/2025/02/09/tech/secure-chat-apps-signal-tor-browser/index.html)) constantly stake their reputation by recommending Tor and Signal.

And therein lies the question: Is Signal’s cryptography *actually* good? And how can we be sure of that?

To know this, we first need to discuss cryptography audits.

![Soatok pointing at a blackboard.](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/10/SoatokLecture.png?resize=512%2C402&ssl=1)

[AJ](https://bsky.app/profile/ajlovesdinos.bsky.social)

## Audits For Normies

Audits are a type of engagement between a vendor and a team of security consultants with specific expertise in the technologies involved.

How an audit works is, loosely:

* The vendor (or a third party, such as [OSTIF](https://ostif.org/)) hires the consultants for a timeboxed assessment of the security of the product or service in question.
* The consultants (ideally with the source code in hand) will then try to find any way to subvert the normal operation of the product/service, especially in a way that’s useful for an attacker.
* Any findings that result from the consultants’ work are compiled together into an Audit Report, with specific recommendations for remediating the issues they identified.
* The vendor responds by either fixing each issue, or documenting them as known limitations if a fix is impractical.
* Optional: The Audit Report is made public.

Regardless of the expertise of the consultants, every audit suffers from the same limitations:

1. The engagement has a specific timebox, which means that coverage will be finite.
2. The engagement is performed over a finite number of snapshots of the source code (typically, one commit hash), so each subsequent commit to the codebase erodes the relevance of the audit.
3. The consultants are human beings, and therefore imperfect.

Furthermore, performing an audit of a product or service without a clear threat model can lead to a lot of disagreement about the relevance or severity of any findings.

This cuts both ways: High-severity issues could actually be nothingburgers to the users of the app, or “informational” findings could be a dealbreaker to your users. Lacking clarity about the security goals and assumptions can hamstring any efforts to providing security assurance.

Unfortunately, sometimes you will see encrypted messaging apps proudly proclaim, “We were audited” when facing criticism, except:

* Their last audit was 5+ years (and/or over 1000 commits) ago.
* They only have the one public audit report.
* The company and/or person that did the audit has no other online footprint, including other audits, and only seemed to pop up to opine about this one vendor.
* The audit report [reads more like sales copy](https://soatok.blog/2021/09/28/the-bi-...