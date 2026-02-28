---
title: Malicious Go Crypto Module Steals Passwords, Deploys Rekoobe Backdoor
url: https://thehackernews.com/2026/02/malicious-go-crypto-module-steals.html
source: The Hacker News
date: 2026-02-27
fetch_date: 2026-02-28T04:01:40.404850
---

# Malicious Go Crypto Module Steals Passwords, Deploys Rekoobe Backdoor

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Malicious Go Crypto Module Steals Passwords, Deploys Rekoobe Backdoor](https://thehackernews.com/2026/02/malicious-go-crypto-module-steals.html)

**Ravie Lakshmanan**Feb 27, 2026Malware / Linux Security

[![Rekoobe Backdoor](data:image/png;base64... "Rekoobe Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdXNmYRKw13_BHE7B7MMtqTTpJXBkgDzl2sH31t0L0_VCl9uJbWPS2yg0j0jz0XJovSYryM4NcSCAZdtTDsoRa2d6y3U84K9TDQYJSObLgaJXXh8juWmP6liqj_uirhZvKjR0dqYZ-J2mwTnmEIYIKfAoC9BY3yL2xhfLD_NbwVKzekKwoI3u4iSzU44Xn/s1700-e365/hackers.jpg)

Cybersecurity researchers have disclosed details of a malicious Go module that's designed to harvest passwords, create persistent access via SSH, and deliver a Linux backdoor named Rekoobe.

The Go module, github[.]com/xinfeisoft/crypto, impersonates the legitimate "golang.org/x/crypto" codebase, but injects malicious code that's responsible for exfiltrating secrets entered via terminal password prompts to a remote endpoint, fetches a shell script in response, and executes it.

"This activity fits namespace confusion and impersonation of the legitimate golang.org/x/crypto subrepository (and its GitHub mirror github.com/golang/crypto)," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-go-crypto-module-steals-passwords-and-deploys-rekoobe-backdoor). "The legitimate project identifies go.googlesource.com/crypto as canonical and treats GitHub as a mirror, a distinction the threat actor abuses to make github.com/xinfeisoft/crypto look routine in dependency graphs."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Specifically, the backdoor has been placed within the "ssh/terminal/terminal.go" file, so that every time a victim application invokes ReadPassword() – a function supposedly meant to read input like passwords from a terminal – it causes that information to capture interactive secrets.

The main responsibility of the downloaded script is to function as a Linux stager, appending a threat actor's SSH key to the "/home/ubuntu/.ssh/authorized\_keys" file, set iptables default policies to ACCEPT in an attempt to loosen firewall restrictions, and retrieve additional payloads from an external server while disguising them with the .mp5 extension.

Of the two payloads, one is a helper that tests internet connectivity and attempts to communicate with an IP address ("154.84.63[.]184") over TCP port 443. The program likely functions as a recon or loader, Socket noted.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNfof5SVhlSVWgulcCtH4nVuXC9oVyXj97l_qJOhch8piParafaTuHDI6OlLyiHuQgIyvthX7Y716raMMFIdCk4H7PT1LMWYLa_weutNtuSSt2QWYOch1e7F8ZXt3xMk7aqj1_cnbqSvilyuM4TwdL_9-77Qx-U-I7LVd4Sul770WUhHXEToy152qlnCHp/s1700-e365/git.jpg)

The second downloaded payload has been assessed to be Rekoobe, a [known](https://thehackernews.com/2022/06/new-syslogk-linux-rootkit-lets.html) [Linux trojan](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html) that has been detected in the wild [since at least 2015](https://vms.drweb.com/virus/?i=7754026&lng=en). The [backdoor](https://intezer.com/blog/linux-rekoobe-operating-with-new-undetected-malware-samples/) is [capable](https://blog.techevo.uk/analysis/linux/2024/11/30/rekoobe-apt31-linux-backdoor.html) of receiving commands from an attacker-controlled server to download more payloads, steal files, and execute a reverse shell. As recently as August 2023, Rekoobe has been put to use by Chinese nation-state groups like [APT31](https://thehackernews.com/2023/08/chinas-apt31-suspected-in-attacks-on.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

While the package [still remains listed](https://pkg.go.dev/github.com/xinfeisoft/crypto) on pkg.go.dev, the Go security team has taken steps to block the package as malicious.

"This campaign will likely repeat because the pattern is low-effort and high-impact: a lookalike module that hooks a high-value boundary (ReadPassword), uses GitHub Raw as a rotating pointer, then pivots into curl | sh staging and Linux payload delivery," Boychenko said.

"Defenders should anticipate similar supply chain attacks targeting other 'credential edge' libraries (SSH helpers, CLI auth prompts, database connectors) and more indirection through hosting surfaces to rotate infrastructure without republishing code."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Backdoor](https://thehackernews.com/search/label/Backdoor), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Go Programming](https://thehackernews.com/search/label/Go%20Programming), [Linux security](https://thehackernews.com/search/label/Linux%20security), [Malware](https://thehackernews.com/search/label/Malware), [Open Source](https://thehackernews.com/search/label/Open%20Source), [SSH](https://thehackernews.com/search/label/SSH), [supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![Resea...