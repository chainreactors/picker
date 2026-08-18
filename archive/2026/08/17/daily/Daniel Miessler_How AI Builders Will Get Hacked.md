---
title: How AI Builders Will Get Hacked
url: https://danielmiessler.com/blog/how-ai-builders-get-hacked?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-08-17
fetch_date: 2026-08-18T02:54:03.743305
---

# How AI Builders Will Get Hacked

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# How AI Builders Will Get Hacked

Keep a live list of everything you've deployed and let AI test it before someone else does

August 17, 2026

[#cybersecurity](/archives/?tag=cybersecurity) [#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology)

 PPO-clipping…

[![How AI Builders Will Get Hacked](/images/how-ai-builders-get-hacked.webp)](/images/how-ai-builders-get-hacked.webp)

If you are building stuff with AI I have a critical security recommendation for you.

Create a continuously-running security testing system that:

1. Maintains a list of all the public stuff you have deployed online
2. Constantly probes those properties with basic security testing

[![The security loop: everything public feeds a living asset inventory, tested continuously](/images/how-ai-builders-diagram-1.webp)](/images/how-ai-builders-diagram-1.webp)

What I mean here is ensuring that:

* The application's stack is not running on known-vulnerable tech
* Your authentication is in place, and working properly
* You don't have any glaring security issues in your application

[![What to check on every public asset: stack, authentication, and glaring holes](/images/how-ai-builders-diagram-2.webp)](/images/how-ai-builders-diagram-2.webp)

For your most important applications you can add full testing to your [harness](https://github.com/danielmiessler/LifeOS/blob/main/LifeOS/install/LIFEOS/DOCUMENTATION/Bunker/BunkerSystem.md) as well. Or you could do it constantly for all applications if you have the funds to do that.

But the most important thing to do, especially as AI gets more and more competent at security testing, is to MAKE SURE YOU HAVE A LIST OF EVERYTHING YOU HAVE PUBLIC.

Never let that list get stale.

And then use AI to continuously ensure you're not leaving something broken out there.

[![Keep the list fresh: every deploy and teardown updates the inventory, and anything public not on it is your dangling risk](/images/how-ai-builders-diagram-3.webp)](/images/how-ai-builders-diagram-3.webp)

I think the main way personal AI builders (and companies) will get hacked in the coming years will be building too fast and leaving stuff dangling on the internet.

It's so easy to build now that many people are building, tearing down, and building something else within the period of minutes or hours. And this raises the chances that you have something facing the internet that is vulnerable.

And [the better general AI gets](/blog/how-easy-to-hack-you), the faster your internet-facing mistakes will get compromised.

Building such a system with AI today is much easier than it was just a year ago, and here's a prompt you could use to do so.

> I am deeply concerned that we have built infrastructure since we've been building with AI that can lead to our systems being hacked, resulting in the loss of infrastructure and/or data. Especially anything customer-related. I need you to do a comprehensive review of everything that we have built and construct an asset management system that maintains a current list of everything we have deployed online. For anything that requires authentication and is therefore sensitive, I need you to build a basic set of security checks that we can run consistently against those assets. Most importantly, ensuring that the authentication is actually working the way it is supposed to. But even outside the authentication and for all assets that are publicly deployed, a comprehensive set of basic security testing should run continuously against all assets to ensure that the software stack is up to date and not vulnerable to known vulnerabilities. I need you to come up with the asset management system's basic functionality, as well as the security testing set of checks. I need you to ensure that these will run continuously from the cloud in a robust and secure way, which needs to itself be secured, along with an alerting system that lets us know if there's ever an issue.

This will get you going, and you can continue improving on it.

Stay safe out there.

#### Notes

1. 🤖 **AIL 1:** Daniel wrote this post. I (Kai, his AI assistant) helped with formatting, the subtitle, the three diagrams, and the header image, and added the links. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).

## Related Reading

* [How Easy It Would Be to Hack You](/blog/how-easy-to-hack-you)

♥

## Reader-supported

For roughly 29.8 years I've written here, ad-free—3,093 essays and tutorials and counting. If it's useful to you, a monthly or one-time donation keeps it going. 🫶🏼

### Monthly

[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)

### One-Time

[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fhow-ai-builders-get-hacked&title=How%20AI%20Builders%20Will%20Get%20Hacked)

Search

This post was tagged with:

cybersecurityaitechnology

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2026 Daniel Miessler. All rights reserved.