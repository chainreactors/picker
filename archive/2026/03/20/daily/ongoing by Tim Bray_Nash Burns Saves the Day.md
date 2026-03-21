---
title: Nash Burns Saves the Day
url: https://www.tbray.org/ongoing/When/202x/2026/03/20/Nash-Burns
source: ongoing by Tim Bray
date: 2026-03-20
fetch_date: 2026-03-21T04:06:37.324010
---

# Nash Burns Saves the Day

# Nash Burns Saves the Day

![Opens, and navigates to, search input field](/ongoing/misc/smallmag.png)

What happened was, soon after New Year’s, friends and colleagues in the UK and Germany started letting us know that their
emails to us were bouncing.
Our “textuality.com” family domain is a Google Workspace (or whatever they call it this year) for email and docs and so on.
Its Web presence, including DNS, has for many years been handled by a local outfit I’ll call “CWH” for some absurdly low monthly
price, and has been trouble-free.

So, what could be wrong? We investigated and discovered that Google was offering a new-and-improved MX-record option,
although they emphasized that the old setup should still work. Anyhow, we installed the New Thing and it didn’t help.

So, we filed a ticket with CWH tech support and somebody got back to us pretty quick, saying they’d changed a firewall
setting that was blocking connections to Germany. I detect the scent of GDPR, but whatever.
Euro-email: Bounce, bounce.

CWH: Probably an MX-record issue, and we should wait for DNS propagation. Several days passed and
bounce, bounce, bounce.
Us: “Not DNS propagation.”
CWH: “Still could be.”

So we VPN’ed to Germany and discovered we couldn’t ping
Textuality’s IP address. Smells like a firewall to me. We told CWH that.

CWH: We have made some changes to firewall settings.

EMail: bounce, bounce, bounce.

VPN+Ping: Request timeout, request timeout, request timeout.

CWH: Try traceroute?

VPN+Traceroute: 14 hops, no joy.

CWH: Your VPN settings must be wrong. Here are instructions to use Windows PC VPN correctly.
Us: Thanks but no.

CWH: Your MX records are configured incorrectly.
Us: No, they are correct per Google guidance. We sent an email beginning
“Please believe us.”

CWH: It must be DNSSEC. Check to see if your registrar implements DNSSEC.
Us: We are using your DNS servers.

CWH: Perhaps your registrar is broadcasting an old record?
Us: Our registrar doesn’t do DNSSEC.

At this point we consulted a friend who’s an expert on DNS and Email and even DNSSEC. He verified that not only could
you not ping
Textuality from Germany, you also couldn’t ping CWH or its name servers. Firewall firewall firewall!

CWH: “I did test the site access using a 3rd party application, and it seems to be accessible on all parts.”
Us: Look at the
output, it shows we can’t be reached from anywhere in Germany.

Also, for all the remaining messages in the email trail, we prefixed our input with bold face extra-large text reading:
**Systems located in Germany cannot ping Textuality.com’s IP address, nor can they ping the IP addresses of textuality.com’s
designated name servers. This is the problem.**

CWH: Let’s try migrating you to a different server; try pinging these hostnames.
VPN+Ping: Nope.

CWH: Are you sure it’s not your VPN settings?
Us: Are you sure it’s not your GDPR settings?
CWH: Raising your issue to Tier 3.

20 hours pass, then we get email from:

Nash Burns! ·
…who said “This has been fixed.” It was.
Nash’s email signature was “Nash(Rajaneesh) B”. What a great name, though. Thanks, Nash.

Am we mad? ·
Not really. Consumer-facing tech support is hard. None of their suggestions were unreasonable.
Doing GDPR correctly is hard.
They’ve been just fine for years and were having a bad week.
Could we expect better from any of CWH’s local competitors? Probably not.

It wasn’t funny at the time, but looking back, it kind
of is.

---

**Updated: 2026/03/20**

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/ongoing/misc/Tim) ·
[Dad](http://www.textuality.com/BillBray/)
[colophon](/ongoing/misc/Colophon) ·
[rights](/ongoing/misc/Copyright)

[![picture of the day](/ongoing/potd.png)](/ongoing/goto-potd/)

[March](/ongoing/When/202x/2026/03/) [20](/ongoing/When/202x/2026/03/20/), [2026](/ongoing/When/202x/2026/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [Web](/ongoing/What/Technology/Web) (399 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!