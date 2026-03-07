---
title: Open source is dying.
url: https://breakdev.org/open-source-is-dying/
source: BREAKDEV
date: 2026-03-06
fetch_date: 2026-03-07T03:55:02.892737
---

# Open source is dying.

[![BREAKDEV](https://breakdev.org/content/images/2022/08/breakdev_logo_with_title.png)](https://breakdev.org)

* [Home](https://breakdev.org/)
* [Evilginx Pro](https://evilginx.com)
* [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery)
* [Tools](https://github.com/kgretzky)
* [Contact](https://breakdev.org/contact/)

[evilginx](/tag/evilginx/)

# Open source is dying.

* [![Kuba Gretzky](/content/images/size/w100/2022/08/avatar512.png)](/author/kuba/)

#### [Kuba Gretzky](/author/kuba/)

Mar 6, 2026
• 4 min read

![Open source is dying.](/content/images/size/w2000/2026/03/opensource-dead2.png)

## Open source is dying a slow, painful death.

For the time being, the AI-related issues in the open-source space have been largely attributed to the flood of AI-slop-generated code contributions, which human project maintainers were unable to process because the effort required to validate each contribution far exceeded the quality of those contributions.

Now Cloudflare, by slop-forking Next.js, has just validated that it's okay to take an open-source project, shove it into an LLM, and have it vibe-code a completely new product based on the source code the engine was fed.

The question arises: if AI regenerates the source code of an open-source project entirely, does the original open-source license still apply?

We're approaching the Slop Ages, where protecting your IP from AI heists becomes virtually impossible. We've seen it in the music industry, and the time has come for the software industry.

I am a software developer myself, and Evilginx has been open-sourced for over 8 years. That's why this news story rubs me the wrong way on a personal level.

Evilginx is an offensive security tool - a phishing framework focused on bypassing MFA. Due to its dual-use nature, it can be used either by the good guys to demonstrate the weaknesses of the company's MFA implementation or by the bad guys for malicious purposes, mainly to harm others.

I had countless second thoughts since the release of the open-source version, whether it was a good idea to put it out there, and later update it with new features, knowing that on one hand it will popularise the problems around weak MFA, and on the other hand give the bad guys a jump-start to expand their criminal enterprise.

It was no surprise to me to learn later that APT groups like Scattered Spider or Void Blizzard reportedly created their own phishing toolkits, based on publicly exposed Evilginx source code.

The main reason I launched Evilginx Pro as a closed-source, paid product last year was a combination of wanting to aid the good guys while gatekeeping the tool from the bad guys (and, of course, building a business out of it).

It has always been important to me to make the community version of the tool accessible to everyone. Still, I was not a fan of the collateral; this decision also carried.

Getting back to my original point.

We now live in a world where a threat actor can feed the GitHub source code of any offensive security tool into an AI and prompt it to create something completely different from scratch, with more features and easier to use. Security issues arising from vibe-coding become a secondary concern in this scenario and can be largely disregarded.

Over the last 2 years, I've been making significant improvements to the Evilginx proxy engine. The majority of these changes have now been implemented in Evilginx Pro. One of the upcoming major updates is the introduction of the new Phishlets 2.0 format.

The plan is to release Phishlets 2.0, together with the proxy engine improvements, as part of the major update to the Evilginx community edition and make it accessible to everyone. As you may've guessed by now, my main concern is whether to release it as open-source or closed-source.

Going the open-source route, I risk threat actors spending a few hundred bucks on a Claude subscription to create their own derivatives of Evilginx, which they can later rebrand and sell on the dark web.

The closed-source route allows me to still release the tool to the public, with proper guardrails to prevent misuse, while keeping it accessible to people who want to use Evilginx to learn hands-on how MFA is bypassed in phishing engagements.

I don't feel that open source is the proper delivery method for offensive security tooling anymore.

The AI has completely reshaped the open-source ecosystem. Writing code is no longer dark magic; it is more accessible than ever, but it has also introduced the cancer we will have to learn to live with.

I use AI to generate small helper libraries, while the rest of the Evilginx code is written by hand. Not because I reject the new AI-oriented reality we live in, but because I really enjoy programming. My love of programming brought me to this point in life.

I also enjoy the concept of ownership. By releasing your work into the world, you let everyone know that you made it, that you personally vouch for its quality, and that you own any mistakes you make. This is what builds trust and reputation.

With AI-generated software, there is neither.

*- Kuba*

*P.S. I refrained from using an LLM to correct this post to avoid adding to the irony of the matter.*

---

### References:

[How we rebuilt Next.js with AI in one week

One engineer used AI to rebuild Next.js on Vite in a week. vinext builds up to 4x faster, produces 57% smaller bundles, and deploys to Cloudflare Workers with a single command.

![](https://blog.cloudflare.com/images/favicon-32x32.png)The Cloudflare BlogSteve Faulkner

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/720QQcrdICiSJXrr9VoixA/4934fffd05d1ca10cc661238b381308e/BLOG-3194_OG.png)](https://blog.cloudflare.com/vinext/)[New Russia-affiliated actor Void Blizzard targets critical sectors for espionage | Microsoft Security Blog

Microsoft Threat Intelligence has discovered a cluster of worldwide cloud abuse activity conducted by a threat actor we track as Void Blizzard, who we assess with high confidence is Russia-affiliated and has been active since at least April 2024. Void Blizzard’s cyberespionage operations tend to be…

![](https://www.microsoft.com/favicon.ico)Microsoft Security BlogMicrosoft Threat Intelligence

![](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2025/05/Void-Blizzard-social.png)](https://www.microsoft.com/en-us/security/blog/2025/05/27/new-russia-affiliated-actor-void-blizzard-targets-critical-sectors-for-espionage/)

<https://x.com/lcamtuf/status/2029771844975501382>

[![Evilginx Pro 4.3 - Event Notifications & Proxies Overhaul](/content/images/size/w600/2025/11/evilginx-pro-43-update.png)](/evilginx-pro-4-3/)

[Featured

## Evilginx Pro 4.3 - Event Notifications & Proxies Overhaul

The newest 4.3 update delivers real-time event notifications, an overhaul of the tunnelling proxy system and a new CSS canary token evasion.](/evilginx-pro-4-3/)

Nov 26, 2025
—
4 min read

[![Evilginx Pro 4.2 - Anti-phishing evasions and more!](/content/images/size/w600/2025/08/evilginx-pro-42-update.png)](/evilginx-pro-4-2/)

[Featured

## Evilginx Pro 4.2 - Anti-phishing evasions and more!

The latest update includes a complete proxy engine rewrite, new anti-phishing evasions, added support for new DNS providers, custom hostnames for lure URLs, better Gophish integration and more!](/evilginx-pro-4-2/)

Aug 14, 2025
—
17 min read

[![Evilginx Pro is finally here!](/content/images/size/w600/2025/03/evilginx_pro_release_cover.png)](/evilginx-pro-release/)

[Featured

## Evilginx Pro is finally here!

After over two years of development, Evilginx Pro reverse proxy phishing framework for red teams is finally live!](/evilginx-pro-release/)

Mar 12, 2025
—
9 min read

[BREAKDEV](https://breakdev.org) © 2026

* E-mail
* [Evilginx Pro](https://evilginx.com)
* [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery)
* [GitHub](https://github.com/kgretzky)
* [Twitter](https://twitter.com/mrgretzky)
* [LinkedIn](http...