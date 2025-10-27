---
title: What is device code phishing, and why are Russian spies so successful at it
url: https://arstechnica.com/information-technology/2025/02/russian-spies-use-device-code-phishing-to-hijack-microsoft-accounts/
source: Instapaper: Unread
date: 2025-02-20
fetch_date: 2025-10-06T20:52:21.629448
---

# What is device code phishing, and why are Russian spies so successful at it

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

SPEAR PHISHING

# What is device code phishing, and why are Russian spies so successful at it?

Overlooked attack method has been used since last August in a rash of account takeovers.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Feb 14, 2025 4:16 pm
| [27](https://arstechnica.com/information-technology/2025/02/russian-spies-use-device-code-phishing-to-hijack-microsoft-accounts/#comments "27 comments")

[![](https://cdn.arstechnica.net/wp-content/uploads/2022/03/phishing-300x161.jpeg)
![](https://cdn.arstechnica.net/wp-content/uploads/2022/03/phishing.jpeg)](https://cdn.arstechnica.net/wp-content/uploads/2022/03/phishing.jpeg)

Credit:
Getty Images

Credit:
Getty Images

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

Researchers have uncovered a sustained and ongoing campaign by Russian spies that uses a clever phishing technique to hijack Microsoft 365 accounts belonging to a wide range of targets, researchers warned.

The technique is known as device code phishing. It exploits “device code flow,” a form of authentication formalized in the industry-wide [OAuth standard](https://tools.ietf.org/html/draft-ietf-oauth-device-flow-07#section-3.4). Authentication through device code flow is designed for logging printers, smart TVs, and similar devices into accounts. These devices typically don’t support browsers, making it difficult to sign in using more standard forms of authentication, such as entering user names, passwords, and two-factor mechanisms.

Rather than authenticating the user directly, the input-constrained device displays an alphabetic or alphanumeric device code along with a link associated with the user account. The user opens the link on a computer or other device that’s easier to sign in with and enters the code. The remote server then sends a token to the input-constrained device that logs it into the account.

Device authorization relies on two paths: one from an app or code running on the input-constrained device seeking permission to log in and the other from the browser of the device the user normally uses for signing in.

## A concerted effort

Advisories from both security firm [Volexity](https://www.volexity.com/blog/2025/02/13/multiple-russian-threat-actors-targeting-microsoft-device-code-authentication/) and [Microsoft](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/) are warning that threat actors working on behalf of the Russian government have been abusing this flow since at least last August to take over Microsoft 365 accounts. The threat actors masquerade as trusted, high-ranking officials and initiate conversations with a targeted user on a messenger app such as Signal, WhatsApp, and Microsoft Teams. Organizations impersonated include:

> * United States Department of State
> * Ukrainian Ministry of Defence
> * European Union Parliament
> * Prominent research institutions

![](https://cdn.arstechnica.net/wp-content/uploads/2025/02/impersonation-messages.webp)

Messages sent by threat actors impersonating high-profile organizations.
Credit:
Microsoft

After building a rapport, the attackers ask the user to join a Microsoft Teams meeting, give access to applications and data as an external Microsoft 365 user, or join a chatroom on a secure chat application. The request includes a link to and an access code, which the threat actor generated using a device they control.

![](https://cdn.arstechnica.net/wp-content/uploads/2025/02/phishing-lure.webp)

A phishing lure that requests target click a link and enter a device authorization code.
Credit:
Microsoft

When the target visits the link with a browser authorized to access the Microsoft 365 account and enters the code, the attacker device gains access that will last as long as the authentication tokens remain valid.

![](https://cdn.arstechnica.net/wp-content/uploads/2025/02/Device-code-phishing-attack-chain.webp)

Attack chain of the device authorization phishing campaign.
Credit:
Microsoft

“While Device Code Authentication attacks are not new, they appear to have been rarely leveraged by nation-state threat actors,” Volexity CEO Steven Adair wrote Thursday afternoon. He said that “this particular method has been far more effective than the combined effort of years of other social-engineering and spear-phishing attacks conducted by the same (or similar) threat actors. It appears that these Russian threat actors have made a concerted effort to launch several campaigns against organizations with a goal of simultaneously abusing this method before the targets catch on and implement countermeasures.”

The effectiveness of the attacks is, in large part, the result of the ambiguity in the user interface of the device code authorization process. That means it's important for people to pay close attention to links and the pages they lead to. Microsoft Azure prompts users to confirm they're signing into the app they expect. People should look for it and be suspicious of messages where this option is missing.

[Microsoft](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/) and [Volexity](https://www.volexity.com/blog/2025/02/13/multiple-russian-threat-actors-targeting-microsoft-device-code-authentication/) provide various other steps people can take to avoid falling prey to this campaign.

[![Photo of Dan Goodin](https://cdn.arstechnica.net/wp-content/uploads/2018/10/Dang.jpg)](https://arstechnica.com/author/dan-goodin/)

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
Senior Security Editor

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
Senior Security Editor

Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at [here](https://infosec.exchange/%40dangoodin) on Mastodon and [here](https://bsky.app/profile/dangoodin.bsky.social) on Bluesky. Contact him on Signal at DanArs.82.

[27 Comments](https://arstechnica.com/information-technology/2025/02/russian-spies-use-device-code-phishing-to-hijack-microsoft-accounts/#comments "27 comments")

Comments

[Forum view](https://arst...