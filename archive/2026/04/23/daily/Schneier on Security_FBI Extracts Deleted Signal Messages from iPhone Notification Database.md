---
title: FBI Extracts Deleted Signal Messages from iPhone Notification Database
url: https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html
source: Schneier on Security
date: 2026-04-23
fetch_date: 2026-04-24T04:57:37.803357
---

# FBI Extracts Deleted Signal Messages from iPhone Notification Database

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

## FBI Extracts Deleted Signal Messages from iPhone Notification Database

404 Media [reports](https://www.404media.co/fbi-extracts-suspects-deleted-signal-messages-saved-in-iphone-notification-database-2/) (alternate [site](https://archive.ph/bSQhD)):

> The FBI was able to forensically extract copies of incoming Signal messages from a defendant’s iPhone, even after the app was deleted, because copies of the content were saved in the device’s push notification database….
>
> The news shows how forensic extraction—­when someone has physical access to a device and is able to run specialized software on it—­can yield sensitive data derived from secure messaging apps in unexpected places. Signal already has a setting that blocks message content from displaying in push notifications; the case highlights why such a feature might be important for some users to turn on.
>
> “We learned that specifically on iPhones, if one’s settings in the Signal app allow for message notifications and previews to show up on the lock screen, [then] the iPhone will internally store those notifications/message previews in the internal memory of the device,” a supporter of the defendants who was taking notes during the trial told 404 Media.

Tags: [databases](https://www.schneier.com/tag/databases/), [FBI](https://www.schneier.com/tag/fbi/), [iPhone](https://www.schneier.com/tag/iphone/), [Signal](https://www.schneier.com/tag/signal/), [terrorism](https://www.schneier.com/tag/terrorism/)

[Posted on April 23, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html) •
[11 Comments](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html#comments)

### Comments

wiredog •
[April 23, 2026 7:52 AM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453907)

There’s a fix out:

Anonymous •
[April 23, 2026 9:02 AM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453909)

Alternate link is not working

Gheese •
[April 23, 2026 10:30 AM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453912)

The same essentially applies to Android, even GrapheneOS, **IF** the notification history is enabled (Settings > Notifications > Notification history).

I do not want to endorse or shame Android/iOS/GrapheneOS, I took this as a wake-up call, to check the settings on my devices.

Clive Robinson •
[April 23, 2026 1:18 PM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453917)

@ Anonymous, ALL,

404 Media lets you see the article title.

Cut and paste this into DuckDuck or similar and you will usually get a link to MSM.

However the link appears locked to you (which is why I’ve not posted the one I got given).

But you will get other links like,

<https://www.msn.com/en-us/news/technology/how-the-fbi-extracted-deleted-signal-messages-from-a-defendants-iphone/ar-AA20zeaP>

That may work for others.

In this case it’s not the original 404 Media article but one that explains it.

Put simply what the FBI did was not by a failing of Signal but using it in the Apple OS.

Put simply “screen alerts” get put in a “Client Side Database” that is part of the OS and it can be scanned, as well as holding data in a persistent way.

I’ve warned in the past that “secure message apps” are not secure unless the system they are used in is secure. In this case the Apple OS is very far from secure hence once the app had produced “Client side plaintext” it was “snagged, tagged and bagged” by the OS and any place it copied the plaintext Database to.

I’ve mentioned several times in the past that neither Signal or WhatsApp are in any way “secure” when built into an “insecure system”

It’s why I advise doing message encryption/decryption off of the device that does “communications” by using an “Energy Gap”.

Judging by the comments I’ve had these past few days, it’s probably the right time for our host @Bruce to write a piece about the fact E2EE and Secure Messaging Apps really don’t give you any real “Privacy” and in all honesty they actually paint a big fat target on your back, even after you think you’ve removed them from your device…

In the past I’ve posted comments on this blog explaining the individual parts and why they can go wrong and ways to avoid them.

However in almost all cases the “Secure Privacy” is not “Convenient” so the average user goes about things the wrong way… Thus ends up on the sharp end of a very expensive court appearance that could lead to life imprisonment and the taking away of all assets they have. And in the US, UK, Australia and many other countries the legislation is quite deliberately stacked against you so you in effect “have no lawful defence”…

lurker •
[April 23, 2026 1:50 PM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453919)

@Gheese, ALL

I’ve just been through the torture of a new phone, where everything is turned ON by default. It’s a tedious chore to turn off Notifications app by app, and some users won’t know or be bothered to do it. Android depends on the device maker’s ROM whether Notification History is global or by individual app,

[Chris R](https://offby1.website/) •
[April 23, 2026 2:23 PM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453920)

@Clive, secure messaging services exist to serve a more general audience that in practice will not jump through what you’re describing as an “Energy Gap” process to communicate with any degree of security; all that’ll be achieved by that is making any degree of secure messaging unattainable.

Signal, and other secure messaging services, exist on a continuum of security; they address *many* of the threats to user privacy that might exist, but are not and cannot be perfect. Your argument seems to suggest that unless perfection can be achieved, it only makes sense to simply not try and I just flat out reject that claim.

Clive Robinson •
[April 23, 2026 5:36 PM](https://www.schneier.com/blog/archives/2026/04/fbi-extracts-deleted-signal-messages-from-iphone-notification-database.html/#comment-453922)

@ ALL,

Apparently Signal asked Apple to fix the issue…

And there is an update or two coming down the pipeline,

<https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/>

@ Chris R,

With regards your comment of,

> “secure messaging services exist to serve a more general a...