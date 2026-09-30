---
title: Using Device Linking to Eavesdrop on WhatsApp and Signal
url: https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html
source: Schneier on Security
date: 2026-09-29
fetch_date: 2026-09-30T07:42:57.646788
---

# Using Device Linking to Eavesdrop on WhatsApp and Signal

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Using Device Linking to Eavesdrop on WhatsApp and Signal

Modern messaging apps allow users to link their phone accounts to their computer desktop. Eavesdroppers are [taking advantage](https://cybernews.com/privacy/police-telegram-whatsapp-signal-surveillance-linked-devices/) of this capability:

> Apps such as WhatsApp Web and Signal Desktop allow people to use their accounts on other devices, such as laptops or desktop computers.
>
> Germany’s Customs Office has been using these features to connect a police-controlled computer to a suspect’s account.
>
> Once connected, messages can be delivered to that computer without the police having to crack the encryption protecting them.
>
> [Netzpoltik details](https://netzpolitik.org/2026/messenger-ueberwachung-immer-mehr-polizei-ueberwacht-messenger-wie-whatsapp/#2026-02-20_ZKA_Messenger-Ueberwachung) that police are able to gain access in this way either through physical access to someone’s phone or by intercepting verification codes via a state-sanctioned phishing attack or intercepting SMS messages via telephone surveillance.

That last paragraph is important. Making this work requires user consent.

What we want is a feature that displays connected devices, so users could notice if a new device gets connected to their account.

Tags: [eavesdropping](https://www.schneier.com/tag/eavesdropping/), [law enforcement](https://www.schneier.com/tag/law-enforcement/), [police](https://www.schneier.com/tag/police/), [Signal](https://www.schneier.com/tag/signal/), [WhatsApp](https://www.schneier.com/tag/whatsapp/)

[Posted on September 29, 2026 at 7:02 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html) •
[13 Comments](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html#comments)

### Comments

Billy Jack •
[September 29, 2026 7:50 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458492)

I know some people who are going to hate learning that Signal is not the ultimate in security.

Henrik •
[September 29, 2026 8:00 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458493)

Had to double check Signal and WhatsApp, and both have “a feature that displays connected devices”. At least on Android in Sweden.

It’s a complete list of linked devices with “last active” timestamp and the possibility to remove the link.

Matthias Urlichs •
[September 29, 2026 8:20 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458496)

Telegram has that feature too (yes I know, ugh Telegram, but still). So what’s the problem? Other than, you know, don’t hand an unlocked phone to *anybody* …

Clive Robinson •
[September 29, 2026 8:23 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458497)

@ Bruce, ALL,

If you step back a little you will realise this is an attack almost as old as telephones themselves (think intercepting telegraphy by clipping across the line to “tee off” the signal).

“Signaling System 7″(SS7) was shown to have a similar “tee off” weakness long before it was discussed on this blog back a decade ago in 2016.

The problem is one that has no easily resolvable solution, which is,

“How do more than two people communicate securely?”

At some point you have to “mix together” the messages as plaintext then send them on encrypted to the end users.

This “mix together” requires a high traffic node so is rarely done on a client device but some centralized server etc.

The only secure solution currently is,

“No group communications in real time.”

Which is not what most humans with money to spend want enforced on them…

It’s also something the “guard labour” at all levels do not want fixed either, because adding somebody to a “group” is often childishly simple and gets the person –or AI machine etc– onto the inside track.

It’s in part the reason why “Communications Assistance for Law Enforcement Act”(CALEA) and similar legislation is written the way it is.

And if French recent behaviour is to be believed something they will jail people for providing even minimal protection against Guard Labour and other evesdropping entities performing even in foreign countries (like silencing political discourse in other countries).

See the case of the arrest of Pavel Durov, the co-founder and CEO of Telegram, who was detained near Paris in August 2024 amid a clown crap show of cockerel posturing by French Authorities in Paris that the French courts have in part struck down,

<https://en.wikipedia.org/wiki/Arrest_and_indictment_of_Pavel_Durov>

(With the question arising that since France has jumped more right wing after the recent election will it all just get quietly dropped,

‘https://www.politico.eu/article/far-right-scores-historic-victory-in-french-senate-election/ )

Rontea •
[September 29, 2026 9:27 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458498)

WhatsApp for iOS also has a feature called linked devices which you can monitor. Not sure if you’ll receive an alert if things change in that list.

toilet licker •
[September 29, 2026 9:55 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458499)

i love to lick public toilet seats – especially if they’re still warm.

Q •
[September 29, 2026 10:07 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458500)

I avoided Signal and WhatsApp because they require a telephone number. The phone number is a weak point because I don’t control it, the telco controls it. And a telephone number is also useless when I travel to another country and get a “tourist sim” thing. And if I change my telephone number it gets reallocated to someone else later.

I use Session. <https://getsession.org/>

It’s free. It requires no user account, no email, no telephone number, no registration, no name. It can be used on any and all devices I choose. It can’t be intercepted by someone else by backdooring a telco.

KC •
[September 29, 2026 11:04 AM](https://www.schneier.com/blog/archives/2026/09/using-device-linking-to-eavesdrop-on-whatsapp-and-signal.html/#comment-458502)

re: the Order for messenger surveillance for Customs Investigation, ZKA

The direct link to this rather measured confidential order is in the OP.

A few informative excerpts:

> “Using messenger surveillance (MU), it may be possible to record data exchanged via instant messengers without having to infiltrate the information technology system with surveillance softwa...