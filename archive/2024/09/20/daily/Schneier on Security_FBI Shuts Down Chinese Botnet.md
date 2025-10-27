---
title: FBI Shuts Down Chinese Botnet
url: https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html
source: Schneier on Security
date: 2024-09-20
fetch_date: 2025-10-06T18:32:23.671272
---

# FBI Shuts Down Chinese Botnet

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

## FBI Shuts Down Chinese Botnet

The FBI has [shut down](https://gizmodo.com/fbi-shuts-down-botnet-run-by-beijing-backed-hackers-that-hijacked-over-200000-devices-2000500627) a botnet run by Chinese hackers:

> The botnet malware infected a number of different types of internet-connected devices around the world, including home routers, cameras, digital video recorders, and NAS drives. Those devices were used to help infiltrate sensitive networks related to universities, government agencies, telecommunications providers, and media organizations…. The botnet was launched in mid-2021, according to the FBI, and infected roughly 260,000 devices as of June 2024.
>
> The operation to dismantle the botnet was coordinated by the FBI, the NSA, and the Cyber National Mission Force (CNMF), according to a press release dated [Wednesday](https://www.ic3.gov/Media/News/2024/240918.pdf). The U.S. Department of Justice received a court order to take control of the botnet infrastructure by sending disabling commands to the malware on infected devices. The hackers tried to counterattack by hitting FBI infrastructure but were “ultimately unsuccessful,” according to the law enforcement agency.

Tags: [botnets](https://www.schneier.com/tag/botnets/), [China](https://www.schneier.com/tag/china/), [hacking](https://www.schneier.com/tag/hacking/)

[Posted on September 19, 2024 at 11:40 AM](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html) •
[5 Comments](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html#comments)

### Comments

Clive Robinson •
[September 19, 2024 7:57 PM](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html/#comment-440648)

@ All,

Does anyone else immediately see the funny side of the FBI activities the article calls out with,

> *“The government’s malware disabling commands, which interacted with the malware’s native functionality…”*

It’s proof if required that,

**“If you put a backdoor in a product then anybody can use it.”**

The “botnet operators” had put in what was a “backdoor control channel” for their own use. However analysis of the code by others, enabled those others to use the backdoor to lock the botnet operators out.

Remember this next time you hear some WASP Nation politician wittering on about “mandatory access” such as recently happened in Australia.

Clive Robinson •
[September 22, 2024 6:27 PM](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html/#comment-440695)

@ ALL,

Re : In other shutdown news.

It appears that the “Ghost Communications Network” setup around 2015 on stripped down mobile phones has been taken down by various world wide Guard Labour agencies,

<https://www.pcmag.com/news/encrypted-phones-used-by-mafia-drug-traffickers-face-police-crackdown>

Apparently like EncroChat etc the system lacked certain types of “Security Protection” thus it was possible for the phones to be backdoored,

> *“Authorities apparently exploited the phones’ update process. Police in Australia were able to hijack access to the servers and send out a modified update, giving law enforcement a way to backdoor the Ghost devices.*

As I’ve indicated before all of these supposed secure message applications are anything but “secure” even for message content privacy, for a number of reasons.

But people need to realise, that for any communications system to stand a chance of being secure as a first step,

“The ‘Security End Point’ has to be verifiably beyond the reach of the ‘Communications End Point’.”

If not then the communications system will be insecure in many ways. Not least as attackers do an ‘end run’ or ‘reach around’ attack through other parts of the system to the ‘Plaintext user interface’.

But there is another issue I’ve mentioned repeatedly in the past, over and above “message content” security you also need “traffic movement” security.

That is you need to deal with not just “Meta-Data” but also “Meta-Meta-Data” that are part of “traffic analysis” of various types.

This is really quite hard for most people to do with any kind of radio based communications as recent news events have shown.

But most people can not do the required “OpSec” either, and lets be honest neither could the CIA agents that ended up being executed in both China and Iran.

ResearcherZero •
[September 26, 2024 4:26 AM](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html/#comment-440766)

Quite a few updates rolled out from various router manufacturers in the last month.
Command injection and other vulnerabilities got patched. D-Link, Zyxel and others…

*(ASUS quietly updated a similar critical vulnerability)*

‘https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-os-command-injection-vulnerability-in-aps-and-security-router-devices-09-03-2024

CVE-2024-45696 allowed enabling D-Link’s telnet and then using the default credentials.

‘https://www.twcert.org.tw/en/cp-139-8081-3fb39-2.html

ResearchZero •
[September 26, 2024 5:02 AM](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html/#comment-440771)

@Clive Robinson

Re: FBI activities

Don’t have to worry about “mandatory access” anymore since their is a special lab for hardware level access to defeat any of the encrypted communications running on device.

cough, cough (because I have a cold)

Hence why the ISP should update the router remotely so I do not have to drive to work.
Or put on shoes, or get out of my chair, or walk to the door, open door and get in car.

Clive Robinson •
[September 27, 2024 2:30 PM](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html/#comment-440799)

@ ResearchZero,

Re : Sheriff’s chairs and doughnuts give heart failure an easy target.

As you indicate, they want to make G-men “more productive”… So if they make it so they,

“do not have to drive to work.
Or put on shoes, or get out of a chair, or walk to the door, open door and get in car.”

They can nurd-harder at a computer and not waste time or the government dime going somewhere (oh and think of the retirment benefit savings 😉

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2024/09/fbi-shuts-down-chinese-botnet.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2024%2F09%2Ffbi-shuts-down-chinese-botnet.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_...