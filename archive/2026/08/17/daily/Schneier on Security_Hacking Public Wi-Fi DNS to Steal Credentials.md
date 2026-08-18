---
title: Hacking Public Wi-Fi DNS to Steal Credentials
url: https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html
source: Schneier on Security
date: 2026-08-17
fetch_date: 2026-08-18T02:53:48.303649
---

# Hacking Public Wi-Fi DNS to Steal Credentials

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

## Hacking Public Wi-Fi DNS to Steal Credentials

Criminals are [hacking](https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/) into public Wi-Fi devices—at hotels, conference centers, and so on—around the world and changing their DNS settings. The goal is to redirect users to fake login pages and steal their credentials.

Tags: [credentials](https://www.schneier.com/tag/credentials/), [DNS](https://www.schneier.com/tag/dns/), [hacking](https://www.schneier.com/tag/hacking/), [phishing](https://www.schneier.com/tag/phishing/), [theft](https://www.schneier.com/tag/theft/)

[Posted on August 17, 2026 at 7:18 AM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html) •
[10 Comments](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html#comments)

### Comments

[Carl Fink](https://reasonablyliterate.com) •
[August 17, 2026 8:10 AM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456937)

Would that be compatible with https? Would the fake login page not have the wrong cert, if it even had SSL enabled? Or is the user meant not to notice a redirect from att.net to att.someotherdomain.net or something?

Andrew Olpin •
[August 17, 2026 9:32 AM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456938)

Yes, the DNS would direct them to the wrong server, and the attacker could HTTPS encrypt the traffic. The trouble is that no reputable cert issuer will issue some rando a cert for “google.com,” so it’s very likely the certificate won’t be trusted by the browser.

My guess is the attackers will go for HTTP and hope the user doesn’t notice.

Privacy •
[August 17, 2026 11:22 AM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456939)

DNS translates every user request such as for google.com to an IP address.
A hacker in control of DNS can redirect a request to anyplace they choose, not only Microsoft 365.
The router used in public WiFi may not be configured securely or may have a vuln.
That’s why a travel router is a must when using public WiFi.
A travel router sits between a user PC and public WiFi (or hotel WiFi), providing NAT and DNS.
The PC user needs to set encrypted DNS in their browser and router, to avoid revealing which sites they request.
DNSSEC gives the PC user assurance the site they connect to is the genuine site, instead of a site a hacker controls.
A travel router running OpenWRT firmware is a good bet. OpenWRT is open-source.
GL-iNet is a company I have no connection to except being a user of their routers.
My routers run OpenWRT and I use an anti-malware encrypted DNS service that performs DNSSEC.
Hacking is rampant these days, for stealing information, stealing money, setting up a botnet, etc. Good cybersecurity has become an absolute necessity.

rando •
[August 17, 2026 11:27 AM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456940)

@Andrew Olpin,
“My guess is the attackers will go for HTTP and hope the user doesn’t notice.”

Yup, exactly that. All browsers should completely eliminate the HTTP option(completely remove the option)… plus, man, this .js crap is just about everywhere. Like some self-destruct feature when it comes to security and privacy.

[mark](https://mrw.5-cent.us) •
[August 17, 2026 12:51 PM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456943)

Wonderful. So if I want to check my email while I’m, say, at Worldcon in LA, what should I do – edit my android hosts file to use 8.8.8.8 to get DNS? Aim my browser at the IP address of my hosting provider?

Not Really Anonymous •
[August 17, 2026 1:34 PM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456944)

You don’t need to use public resolvers to do DNS lookups. Your device can do lookups starting at the root (which will get cached, so it won’t need that for every request) and work it’s way down.

lurker •
[August 17, 2026 1:42 PM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456945)

@Andrew Olpin
“My guess is the attackers will go for HTTP and hope the user doesn’t notice.”

Uhuh. When my local library dropped WPA2 for an “open” system, three of the five browsers on my laptop complained that www[dot]schneier[dot]com was insecure, and somebody might be spoofing it. I have to keep a copy of the highly recommended Firefox just so i can register with their proxy, then the TLS seems to work OK. (I know, telling you’re being MITMed isn’t that simple)

@mark
It’s tough when you’re forced to use webmail because the (say Worldcon) proxy has blocked the IMAP ports. And pdnsd is great to have for those weekends away.

RedLight •
[August 17, 2026 6:54 PM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456948)

Uhhh. Wait a sec…

* I go to foo.com on my computer’s web-browswer.
* DNS lookup is redirected and goes to a the wrong 1.2.3.4 ip address.
* As long as that IP address has a security cert, and can handle HTTPS traffic, everything is fine. I see nothing out of the ordinary.
* The 1.2.3.4 machine now does a man-in-the-middle attack, sitting between me & foo.com. It can read everything! And I see nothing out of the ordinary!

Seems like there’s an awful lot of HTTPS-capable websites out there. It can’t be that hard to get a security cert. It doesn’t have to be foo.com’s security cert. Any sercurity cert will do!

Problem is, my web browswer can’t tell whether I’m talking directly to foo.com’s IP address or to the 1.2.3.4 ip address. It only knows the destination has a security cert and can connect over HTTPS.

That’s a problem. Suddenly Firefox’s secure-DNS seems like a godsend!

Mr D •
[August 17, 2026 8:35 PM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456949)

@RedLight it absolutely matters that it’s a security cert for the correct site – the cert is tied to the DNS name of the site. This is a non-trivial attack if limited to https only – and a bunch of security measures in browsers make forcing http much harder than it was.

The number of phone apps that don’t validate certs properly probably gives easier attacks than the browser, though getting a fake cert has been done a few times

[Carl Fink](https://reasonablyliterate.com) •
[August 17, 2026 10:09 PM](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html/#comment-456951)

@mark, have you considered a proxy service? With a proxy enabled, all your t...