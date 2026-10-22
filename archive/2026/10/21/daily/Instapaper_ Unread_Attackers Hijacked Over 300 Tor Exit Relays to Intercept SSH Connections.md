---
title: Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections
url: https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
source: Instapaper: Unread
date: 2026-10-21
fetch_date: 2026-10-22T06:46:42.378163
---

# Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections](https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html)

**Swati Khandelwal**Oct 21, 2026Network Security / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-PokIxnQKc5RkxwrgRCR7Aaw8sjbkT1F4TQWCIG2V_rhQVKp8CJgtivgF5Zns45rObi0Tf-e9FDBXdX0L7OUshol00GvpiQhAi3SUAa72DV-bjeDu2oNzET9uV_cIQV2U9jSXGC2qiWWOr00M1ZYPAtcaWJNSn2_IH_BwPWVaUEqqjpmUSgfhIvRUdbY/s1700-nu-rw-lo-l85-e365/tor-ssh.jpg)

Attackers took control of more than 300 Tor exit relays in early October and used them to redirect SSH connections to servers that stole login passwords, a researcher found.

Exit relays are the last hop in a Tor circuit, where traffic leaves the network for its destination. Only a password login to an SSH server made through Tor between October 1 and 5, after accepting the interception server's host key, could have been captured.

The Tor Project began flagging relays on October 4, and by October 5, none remained in the consensus, the list of relays that Tor clients use. At the peak on October 4, the relays carrying the attacker's exit policy made up 7.46% of Tor's exit capacity, measured by consensus weight, according to an [analysis of public Tor directory data](https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays%40lists.torproject.org/message/Z2B6XYKJZBBQADU77MSNL6FJP7MHZHIV/) posted to the tor-relays mailing list.

The researcher, who publishes as kaba, [scanned](https://kaba.cx/posts/20261020_Tor/) all of Tor's roughly 3,000 exits on October 2 and found 333 redirecting SSH to the same 12 interception servers. The directory-data analysis counts 377 relays run by 59 operators that switched to the attacker's exit policy between October 1 and 4, which it calls "a policy match, not proof of compromise."

### How the Hijacked Exits Intercepted SSH

An exit relay only carries traffic to the ports its exit policy allows. The attackers rewrote that policy in the relays' torrc configuration files to allow port 22 (the SSH port), enabling SSH on 342 relays that had blocked it. Another 24 relays that had not been exits at all became exits.

"It seems the attacker is gaining access to Linux based hosts and when these machines are running non-exits they are editing the torrc file and turning them into exits to be able to carry out the SSH attack," the Tor Project's network health team wrote in its [October 5 notice](https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays%40lists.torproject.org/thread/WOHPLKCSHYXFTBRZXDENDKJZMBMPLMG5/) to relay operators. Most of the affected relays were already exits, the directory data shows.

The same change closed the encrypted mail ports, IMAPS and POP3S, and on most relays opened the plaintext-capable ones, POP3 and IMAP.

A Tor client only picks an exit that allows the destination port, so these relays stopped carrying encrypted mail and started carrying SSH, Telnet, and, on most of them, plaintext mail. Why the encrypted mail ports were closed is not visible in the data, the analysis says.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

With port 22 open, an SSH connection through one of these exits went to one of 12 interception servers instead of its destination, kaba found. When a server intercepted the connection, it presented its own host key. A user who already knew the real server's key saw OpenSSH's warning that the remote host identification had changed, and a user connecting for the first time saw the usual prompt to accept a new key.

In the October 2 scan, about a dozen exits were serving a fake host key, and the other 300 or so redirected through the same servers without altering the key.

A user who accepted the key and typed a password handed it to the interceptor. The interceptor connected to the real server, so the session worked, and every command could be watched and separately logged in with the stolen password to check for sudo and run a base64-encoded Perl installer. In kaba's honeypot, the installer took the same form as the command that put Ebury, a backdoor that hides inside OpenSSH, on one of a relay operator's servers, as described below.

A key-based SSH login could not be relayed this way. Under the [SSH authentication protocol](https://datatracker.ietf.org/doc/rfc4252/), , the client's signature includes an identifier unique to each session, so a signature made for the interceptor's session is useless against the real server. The interceptor could still accept a key login itself and show a fake shell, but it could not reach the real server with it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3VO8MBwoszoHUKXrQqE-LK-3HcolJ5Sfsw3joGhJ_Bblgz3m5ljQUmO9u0u0MPDWvK5XV1x-a0ugag9vALws8IRkgvFd-ryXY_utkD5AM7cEzJDvFKairXa0RsgfgtK8W7864FyDkIJt6r-4yIDPWBupF0YX0WDgMB4PRM-_IB93ZgmUX-y6J1hz__8M/s1700-nu-rw-lo-l85-e365/tor-ssh-incident.png)

A password, by contrast, travels inside the encrypted session and can be read by the server at the other end, which here was the interceptor.

### Who Was Exposed, and What to Do If You Were

To be exposed, someone had to connect to an SSH server over Tor between October 1 and the afternoon of October 5, land on one of the hijacked exits, have the connection intercepted rather than passed through, accept the interceptor's host key, and log in with a password. No count of victims exists.

If you accepted an unfamiliar or changed host key over Tor in that window, treat the password you typed as stolen, change it, and check that server for the Ebury signs listed below. An OpenSSH client that accepted the key saved it in known\_hosts.

The server that intercepted kaba's connection used an ED25519 key with the fingerprint SHA256:6baCZCPsl+AfQuujUS81fMEE/C7UeJ+AwjrImqmDB3E, though the other interception servers may have used different keys.

### How It Was Found and Stopped...