---
title: Malicious Go Module Poses as SSH Brute-Force Tool, Steals Credentials via Telegram Bot
url: https://thehackernews.com/2025/08/malicious-go-module-poses-as-ssh-brute.html
source: The Hacker News
date: 2025-08-25
fetch_date: 2025-10-07T00:17:48.663422
---

# Malicious Go Module Poses as SSH Brute-Force Tool, Steals Credentials via Telegram Bot

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Malicious Go Module Poses as SSH Brute-Force Tool, Steals Credentials via Telegram Bot](https://thehackernews.com/2025/08/malicious-go-module-poses-as-ssh-brute.html)

**Aug 24, 2025**Ravie LakshmananMalware / Supply Chain Security

[![SSH Brute-Force Tool](data:image/png;base64... "SSH Brute-Force Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_MS2EnkJx0smfkh9jPgVCwzAVD9zpIkpEoYP8Z30l20DYhHW2USZrRxJeP56Q62VenfhR02Iq0QO3wH12F-n2YjipfM5yHArlYlRiimnghudGACbXklxwbxAO-TDWHD_9rG4cXDlK7VpHNUf8MWejLdNn6th5n17jPbzPCoy5pzJjQ7tATwsTR-PgI1AU/s790-rw-e365/ssh-tool.jpg)

Cybersecurity researchers have discovered a malicious Go module that presents itself as a brute-force tool for SSH but actually contains functionality to discreetly exfiltrate credentials to its creator.

"On the first successful login, the package sends the target IP address, username, and password to a hard-coded Telegram bot controlled by the threat actor," Socket researcher Kirill Boychenko [said](https://socket.dev/blog/malicious-go-module-disguised-as-ssh-brute-forcer-exfiltrates-credentials).

The deceptive package, named "golang-random-ip-ssh-bruteforce," has been linked to a GitHub account called [IllDieAnyway](https://github.com/illdieanyway) (G3TT), which is currently no longer accessible. However, it [continues to be available](https://pkg.go.dev/github.com/illdieanyway/golang-random-ip-ssh-bruteforce%40v0.0.0-20220624110449-9d819518d4fc) on pkg.go[.]dev. It was published on June 24, 2022.

The software supply chain security company said the Go module works by scanning random IPv4 addresses for exposed SSH services on TCP port 22, then attempting to brute-force the service using an embedded username-password list and exfiltrating the successful credentials to the attacker.

A notable aspect of the malware is that it deliberately disables host key verification by setting "[ssh.InsecureIgnoreHostKey](https://pkg.go.dev/golang.org/x/crypto/ssh#InsecureIgnoreHostKey)" as a HostKeyCallback, thereby allowing the SSH client to accept connections from any server regardless of their identity.

The wordlist is fairly straightforward, including only two usernames root and admin, and pairing them against weak passwords like root, test, password, admin, 12345678, 1234, qwerty, webadmin, webmaster, techsupport, letmein, and Passw@rd.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The malicious code runs in an infinite loop to generate the IPv4 addresses, with the package attempting concurrent SSH logins from the wordlist.

The details are transmitted to a threat actor-controlled Telegram bot named "@sshZXC\_bot" (ssh\_bot) via the API, which then acknowledges the receipt of the credentials. The messages are sent through the bot to an account with the handle "@io\_ping" (Gett).

[![SSH Brute-Force Tool](data:image/png;base64... "SSH Brute-Force Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdPvGfOX4Abfle8aEVfLZ-G7TJQHUy3vBXXY7Fdzc4RcOQtzQ4SrOX1WsubqvWXvCKm1sX4I-xMaUYtorMM5V7lqQ34Mt5kCPcYt6PexwbS3xkZ-UESQ2Yozm1lrIe5RQ0U7OTpUFfoQGDH2ioaji0KL_0GYOWz-CdVnIITNSKVyC592YQTwAwfiBufuQu/s790-rw-e365/g3tt.jpg)

An [Internet Archive snapshot](https://web.archive.org/web/20250609090051/https%3A//github.com/illdieanyway) of the now-removed GitHub account shows that IllDieAnyway's software portfolio, included an IP port scanner, an Instagram profile info and media parser, and even a PHP-based command-and-control (C2) botnet called Selica-C2.

Their [YouTube channel](https://www.youtube.com/%40AngelsTogether/videos), which remains accessible, hosts various short-form videos on "How to hack a Telegram bot" and what they claim to be the "most powerful SMS bomber for the Russian Federation," which can send spam SMS texts and messages to VK users using a Telegram bot. It's assessed that the threat actor is of Russian origin.

"The package offloads scanning and password guessing to unwitting operators, spreads risk across their IPs, and funnels the successes to a single threat actor-controlled Telegram bot," Boychenko said.

"It disables host key verification, drives high concurrency, and exits after the first valid login to prioritize quick capture. Because the Telegram Bot API uses HTTPS, the traffic looks like normal web requests and can slip past coarse egress controls."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub](https://thehackernews.com/search/label/GitHub)[Go Programming](https://thehackernews.com/search/label/Go%20Programming)[Malware](https://thehackernews.com/search/label/Malware)[password](https://thehackernews.com/search/label/password)[Russian hackers](https://thehackernews.com/search/label/Russian%20hackers)[ssh security](https://thehackernews.com/search/label/ssh%20security)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)[Telegram](https://thehackernews.com/search/label/Telegram)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "St...