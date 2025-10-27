---
title: South Korea’s banking security: Intermediate conclusions
url: https://palant.info/2023/02/20/south-koreas-banking-security-intermediate-conclusions/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:22:04.804462
---

# South Korea’s banking security: Intermediate conclusions

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# South Koreaâs banking security: Intermediate conclusions

2023-02-20
 [Korea](/categories/korea/)/[Security](/categories/security/)/[Privacy](/categories/privacy/)
 8 mins
 [3 comments](/2023/02/20/south-koreas-banking-security-intermediate-conclusions/#comments)

*Note*: This article is also available [in Korean](https://github.com/alanleedev/KoreaSecurityApps/blob/main/04_intermediate_conclusions.md).

A while back I wrote [my first overview of South Koreaâs unusual approach to online security](/2023/01/02/south-koreas-online-security-dead-end/). After that I published two articles on [specific](/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/) [applications](/2023/01/25/ipinside-koreas-mandatory-spyware/). While Iâm not done yet, this is enough information to draw some intermediate conclusions.

The most important question is: all the security issues and bad practices aside, does this approach to banking security make sense? Do these applications have the potential to make people more secure when rolled out mandatorily nation-wide?

![Message on www.citibank.co.kr stating: [IP Logger] program needs to be installed to ensure safe use of the service. Do you want to move to the installation page?](/2023/02/20/south-koreas-banking-security-intermediate-conclusions/message.png)

TL;DR: I think that the question above can be answered with a clear âno.â The approaches make little sense given actual attack scenarios, they tend to produce security theater rather than actual security. And while security theater can sometimes be useful, the issues in question have proper solutions.

#### Contents

* [Endpoint protection](#endpoint-protection)
* [Keyboard protection](#keyboard-protection)
* [IP address detection](#ip-address-detection)
* [Certificate-based logins](#certificate-based-logins)
* [Software distribution](#software-distribution)

## Endpoint protection

The probably least controversial point here is: usersâ devices need protection, ideally preventing them from being compromised. So when a user accesses their bank, their computer should really be theirs, with nobody secretly watching over their shoulder. Over time, two types of applications emerged with the promise to deliver that: antivirus and firewall.

But Microsoft has you covered there. Starting with Windows 7, there is a very effective built-in firewall (Windows Firewall) and a decent built-in antivirus (Windows Defender). So you are protected out of the box, and installing a third-party antivirus application will not necessarily make you safer. In fact, these antivirus applications way too often [end](/2019/10/28/avast-online-security-and-avast-secure-browser-are-spying-on-you/) [up](/2020/06/22/exploiting-bitdefender-antivirus-rce-from-any-website/) [weakening](/2019/08/19/kaspersky-in-the-middle--what-could-possibly-go-wrong/) [the](/2020/01/13/pwning-avast-secure-browser-for-fun-and-profit/) [protection](/2020/02/25/mcafee-webadvisor-from-xss-in-a-sandboxed-browser-extension-to-administrator-privileges/).

Of course, I have no idea how good AhnLabâs antivirus is. Maybe it is really good, way better than Windows Defender. Does it mean that it makes sense for South Korean banking websites to force installation of AhnLab Safe Transaction?

Well, most of the time AhnLab Safe Transaction sits idly in the background. It only activates when you are on a banking website. In other words: it will not prevent your computer from being compromised, as a malware infection doesnât usually happen on a banking website. It will merely attempt to save the day when it is already too late.

## Keyboard protection

And speaking of âtoo late,â I see a number of âsecurityâ applications in South Korea attempting to protect keyboard input. The idea here is: yes, the computer is already compromised. But weâll encrypt keyboard input between the keyboard and the website, so that the malicious application cannot see it.

I took [a closer look at TouchEn nxKey](/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/), which is one such solution. The conclusion here was:

> So whatever protection nxKey might provide, it relies on attackers who are unaware of nxKey and its functionality. Generic attacks may be thwarted, but it is unlikely to be effective against any attacks targeting specifically South Korean banks or government organizations.

And this isnât because they did such a bad job (even though they did). As a general rule, you cannot add software to magically fix a compromised environment. Whatever you do, the malicious software active in this environment can always implement countermeasures.

Weâve already seen this two decades ago when banking trojans became a thing and would steal passwords. Some websites decided to use on-screen keyboards, so that the password would not be entered via a physical keyboard.

The banking trojans adapted quickly: in addition to merely recording the keys pressed, they started recording mouse clicks along with a screenshot of the area around the mouse cursor. And at that point on-screen keyboards became essentially useless. Yet they are still common in South Korea.

Just to state this again: once a computer is compromised, it cannot be helped. The only solution is [multi-factor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication). In banking context this means that the transaction details always need to be confirmed on a separate and hopefully unaffected device.

## IP address detection

Two decades ago I was a moderator of an online chat. Most chat visitors would behave, but some were trolls only looking to annoy other people. I would ban the trollsâ IP address, but they would soon come back with a different IP address.

Twenty years later I see South Korean banks still struggling with the same inadequate protection measures. Rather than finding new ways, they continue fighting anonymous proxies and VPNs. As a result, they demand that customers [install IPinside, a privacy-invasive de-anonymization tool](/2023/01/25/ipinside-koreas-mandatory-spyware/).

Quite frankly, Iâm not even certain which exact threat this addresses. Assuming that it addresses a threat at all rather than merely serving as an excuse to collect more data about their customers.

Banks generally donât care about IP addresses when limiting login attempts. After three unsuccessful login attempts the account is locked, this is common practice ensuring that guessing login credentials is impracticable.

Is the goal maybe recognizing someone using stolen login credentials? But thatâs also something which is best addressed by [multi-factor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication). Banking trojans learned avoiding such geo-blocking a long time ago, they simply use the victimâs compromised computer both to exfiltrate login credentials and to apply them for a malicious transaction. As far as the bank can see, the transaction comes from the computer belonging to the legitimate owner of the account.

Or is the goal actually preventing attacks against vulnerabilities of the banking website itself, allowing to recognize the source of the attack and to block it? But accessing banking websites prior to login doesnât require IPinside, so it has no effect here. And once the malicious actors are logged in, the bank can recognize and lock the compromised account.

## Certificate-based logins

One specific of the South Korean market is the prevalence of certificate-based logins, something that was apparently mandated for online banking at a certain point but no longer is. There are still applications to manage these certificates and to transfer them between devices.

Now certificate-based logins are something that browsers supported out of the box for a long time (âclient-...