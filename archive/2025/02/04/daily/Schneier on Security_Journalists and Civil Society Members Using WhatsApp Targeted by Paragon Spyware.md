---
title: Journalists and Civil Society Members Using WhatsApp Targeted by Paragon Spyware
url: https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html
source: Schneier on Security
date: 2025-02-04
fetch_date: 2025-10-06T20:39:33.831979
---

# Journalists and Civil Society Members Using WhatsApp Targeted by Paragon Spyware

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

## Journalists and Civil Society Members Using WhatsApp Targeted by Paragon Spyware

This is yet another story of commercial spyware being [used against](https://www.theguardian.com/technology/2025/jan/31/whatsapp-israel-spyware) journalists and civil society members.

> The journalists and other civil society members were being alerted of a possible breach of their devices, with WhatsApp telling the Guardian it had “high confidence” that the 90 users in question had been targeted and “possibly compromised.”
>
> It is not clear who was behind the attack. Like other spyware makers, Paragon’s hacking software is used by government clients and WhatsApp said it had not been able to identify the clients who ordered the alleged attacks.
>
> Experts said the targeting was a “zero-click” attack, which means targets would not have had to click on any malicious links to be infected.

Tags: [spyware](https://www.schneier.com/tag/spyware/), [WhatsApp](https://www.schneier.com/tag/whatsapp/)

[Posted on February 3, 2025 at 7:05 AM](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html) •
[16 Comments](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html#comments)

### Comments

Clive Robinson •
[February 3, 2025 8:33 AM](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html/#comment-442750)

**Zero-Click, the modern curtain twitching.**

From the article we see,

> *“Experts said the targeting was a “zero-click” attack, which means targets would not have had to click on any malicious links to be infected.”*

It’s a bit more complicated than just telling users **Do Not** “click on any malicious links”…

Without going into lots of details, it’s possible to send somebody a message where the users “Smart Device” phone does something really “Dumb” like “pre fetch” images and the like thus do the equivalent of a user clicking…

But the other thing which really annoys me about people talking glibly about “malicious links” is that even Security Experts can not actually “Positively identify” them as being “malicious links” untill they follow them… So,

“How the heck do we expect ordinary users to be able to magically know every time what links are malicious or not?”

Personally I blame the likes of Microsoft, Google, and other major software developers in the industry. Because they talk a lot about “User Security” and then do just about everything they can to destroy user security in the name of “User Convenience” or some other “Marketing Nonsense”.

Further we know that they can not find vulnerability exploits in code despite their special teams…

Just ask yourself how many times have you heard about “malicious exploits” in the software they say is OK to go in their “Walled Garden” App Stores and similar.

As long as this nonsense goes on then the likes of “Paragon Spyware” will be continued to be developed and made available to be used by all sorts of undesirables and criminals.

If we want to reduce it we have to treat Microsoft abd Google etc like those who “grow or manufacture” drugs. That is send in the military with flame throwers etc. Because if the War-On-Drugs has taught us one thing, “as long as their is product, then a market will exist to trade it”. It’s the same with vulnerabilities lock up the producers and burn the product, then others might learn there “Individual Rights” to push bad product for profit is capped by “Societal Responsability”.

TimH •
[February 3, 2025 1:28 PM](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html/#comment-442751)

@Clive…also the reporting “WhatsApp said it believed the so-called vector, or means by which the infection was delivered to users, was through a malicious pdf file that was sent to individuals who were added to group chats.” provides no help at all to avoid infection, apart from not have WA installed.

What is the group chat vector? Does the attack use javascipt which can be disabled in Safari?

MDK •
[February 3, 2025 3:57 PM](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html/#comment-442753)

WebRTC is not your friend.

lurker •
[February 3, 2025 6:25 PM](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html/#comment-442756)

@TimH

attaching a PDF to a chat message is stupidity,

There seems to be no shortage of stupidity.

BTW a recent “update” to Android means that all PDF reading apps now require permissions to “access all files on device”. The fine print in the dialog box says the when the permission is granted the app “can read, write, or delete any file on the device. Access to files may occurr without any notification to the user.”

ResearcherZero •
[February 3, 2025 11:51 PM](https://www.schneier.com/blog/archives/2025/02/journalists-and-civil-society-members-using-whatsapp-targeted-by-paragon-spyware.html/#comment-442758)

There are no regulations that providers have to inform subscribers about the flaws in their networks. Most people do not realise that voice call ‘metadata’ and ordinary text messages are not encrypted. The **plain text** messages can be read by anyone (including the IMSI which can be monitored by an IMSI Cathcher). All of this data is sent **unencrypted** over-the-air in 2G, 3G and 4G. Much of the network will contain a mix of these technologies, and providers may use other network providers’ base stations for roaming and other features where they do not themselves have coverage. An attacker can easily see a lot of this information.

No special skill or knowledge is needed to conduct such attacks. It’s dead easy and cheap.

Particularly vulnerable are new customers activating a new SIM or registering a new device on the network. A scammer can see the new activation attempt, who the mobile provider is and the subscriber details, then **Cold Call** the unsuspecting customer while impersonating the customer support of the mobile provider. Next the scammer will ask the customer for their password and take control of their account/s. These attacks are cheap.

A more advanced attacker can operate their own base station or network equipment and conduct far more advanced attacks. While there are laws allowing governments to use contractors to install ‘lawful intercept’ equipment and middleboxes which allow Deep Packet Inspection or the ability to inject malicious packets, there are **no regulations** ensuring that network providers must protect and secure all your data passing over their networks.

Vulnerabilities used by spyware operators might be available six...