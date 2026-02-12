---
title: On Discord Alternatives
url: https://soatok.blog/2026/02/11/on-discord-alternatives/
source: Dhole Moments
date: 2026-02-11
fetch_date: 2026-02-12T04:21:32.882258
---

# On Discord Alternatives

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

[(Anti-)Social Media](https://soatok.blog/category/social-media/) [Open Source](https://soatok.blog/category/technology/open-source/)

# On Discord Alternatives

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [February 11, 2026](https://soatok.blog/2026/02/11/on-discord-alternatives/)

![On Discord Alternatives](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/02/BlogHeader-2026-Discord-Alternatives.png?fit=1200%2C675&ssl=1)

Next month, [Discord is going to start requiring age verification](https://www.gamingonlinux.com/2026/02/discord-is-about-to-require-age-verification-for-everyone/). The backlash from gamers everywhere has been predictable and justified. I guess their company name checks out.

<https://www.youtube.com/watch?v=D-s6HuzZRNg>

I’ve had a few people reach out to me because of [my prior vulnerability disclosures and criticism of encrypted messaging apps](https://soatok.blog/encrypted-messaging-apps/).

(Thanks, [Toggart](https://taggart-tech.com/discord-alternatives/).)

Unfortunately, asking a cryptography-focused security engineer for app recommendations is like asking a rocket scientist to recommend a car dealership in Nebraska: If you somehow get a good answer, it’ll be by sheer coincidence rather than a reasonable expectation.

That might sound weird. Let me explain.

![Soatok pointing at a blackboard.](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/10/SoatokLecture.png?resize=512%2C402&ssl=1)

Art by [AJ](https://bsky.app/profile/ajlovesdinos.bsky.social)

## Discord is Different Things to Different People

Gamers made Discord popular, but Discord isn’t just one tool to people.

Discord is simultaneously:

1. The main way normal people do voice chat (often with strangers) without automatically doxing themselves
2. A place to share memes and multimedia content
3. The software that facilitates family group chats
4. A support forum with Q&A sections and bug trackers
5. Live event hosting (AMAs, podcasts)
6. Activism and political organizing
7. Casual gaming coordination
8. A platform for mental health support circles
9. Collaboration hubs between artists and other creative workers
10. Educational spaces for tutoring or code reviews with screen shares
11. A rather poor substitute for wikis and personal websites
12. A point-and-click adventure game to get bots to give you permission to access the actual channels you need in order to solve a problem

And this is just the use cases I’m acutely aware of from scrolling through public invites I can find on the Fediverse and the “servers” I’m already on.

*Actually, I need to add one more thing Discord is*:

13. Solely responsible for muddying the waters for most people on what a fucking “server” is.

My point is: Asking *anyone* to recommend a one-size-fits-all replacement for every use case (which may have wildly different user experience requirements) is setting yourself up for disappointment.

But asking a cryptography nerd might be even worse, because we tend to care about how products and services actually achieve privacy and security, where most people simply do not.

## Which Apps Are Good for Privacy?

Currently, the only messaging app I’ve [evaluated](https://soatok.blog/2025/02/18/reviewing-the-cryptography-used-by-signal/) that actually meets the bar for privacy (i.e., end-to-end encryption) is, unfortunately, **Signal**.

* WhatsApp is owned by Meta, so I won’t even look at it.
* Matrix knowingly shipped vulnerable cryptography for many years and then admitted that fact only after [I disclosed vulnerabilities in said cryptography code](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/).
* [XMPP (Jabber, etc.) is plaintext-by-default](https://soatok.blog/2024/08/04/against-xmppomemo/), which disqualifies it. Private messaging apps shouldn’t even *have* a plaintext mode to fallback onto.
  + Aside: There are some Fediverse users that have claimed this post has been “debunked” simply because some person [disagreed with it, concluding that Signal doesn’t meet their personal threat model](https://web.archive.org/web/20240809132745/https%3A//www.moparisthebest.com/against-silos-signal/) which prioritizes [where data is stored over how it’s encrypted](https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/).

    The author of the other blog post and I can disagree respectfully, but anyone who calls their post a “debunk” [needs to consult a dictionary](https://www.youtube.com/watch?v=dTRKCXC0JFg).
* Session [forked Signal and removed forward secrecy](https://soatok.blog/2025/01/14/dont-use-session-signal-fork/). They recently announced [plans to undo this mistake](https://web.archive.org/web/20260000000000%2A/https%3A//getsession.org/blog/session-protocol-v2). Time will tell if they fuck that up, too.
* [Telegram sucks](https://soatok.blog/2024/05/14/its-time-for-furries-to-stop-using-telegram/) and the less furries use Telegram, the better.

As for Twitter’s “X Chat” feature, well…

> Why was this code ever shipped?!This is from the second vuln, where keys' signatures aren't checked before they're stored in the trusted key store.Why would you ever ship a "TODO, actually validate signatures lol" in your secure messenger?!
>
> — [Andrew Lilley Brinker (@alilleybrinker.com)](https://bsky.app/profile/did%3Aplc%3Ageozyv62fx63m7jhr4eraubc?ref_src=embed) [2026-01-28T18:38:08.957Z](https://bsky.app/profile/did%3Aplc%3Ageozyv62fx63m7jhr4eraubc/post/3mdiw7ejdks26?ref_src=embed)

<https://bsky.app/profile/alilleybrinker.com/post/3mdiw7ejdks26>

> **Note**: If you’re curious about some product that isn’t included in the above list, please don’t ask me about it.
>
> I was needled for most of 2024 and 2025 with random queries to assess the security of random chat apps and I don’t want these kinds of questions anymore.
>
> Many of the products I get asked about have had public pentest reports. Go read those reports instead of asking Internet furries to do free labor.

### Signal Isn’t Perfect

That said, Signal has its faults:

1. You still need a phone number to sign up.
   * You do not, however, need to give your phone number to strangers to communicate with them. Signal rolled out usernames *years ago*, and it’s no longer a requirement.

     Some people missed the memo and still gripe about this. They are simply wrong.
2. Group moderation tools are nonexistent.
   * As a group admin, I cannot delete abusive messages sent to a group chat and have it be removed from other people’s devices.
3. Signal is largely under the jurisdiction of the United States.
   * If your threat model includes “nation state forces them to release a backdoor that targets *your account in particular*“, this might be a dealbreaker for you.

     However, Signal historically has not had [any data to provide authorities even under subpoena](https://signal.org/bigbrother/santaclara/).
4. Signal is largely hosted by cloud providers, and is generally considered Centralized.
   * This has some upsides: A large k-anonymity provides advantages against a passive adversary trying to do traffic analysis on network-level metadata will only see that you and your friends are using Signal, and cannot generally learn who is talking to whom.

     This has some obvious downsides: An active attacker that has compromised Signal’s infrastructure might be able to discern which messages are sent to which profile (via [96-bit “delivery tokens”](...