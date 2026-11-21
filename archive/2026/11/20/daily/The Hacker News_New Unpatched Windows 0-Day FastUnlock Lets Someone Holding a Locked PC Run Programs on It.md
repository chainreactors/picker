---
title: New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It
url: https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html
source: The Hacker News
date: 2026-11-20
fetch_date: 2026-11-21T09:02:36.026931
---

# New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It](https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html)

**Swati Khandelwal**Nov 20, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRnUdcazdCteyaE1EC_aLit8CioDaJ5yvsWnawFVWQrJvYFktNRJXlW9MOJLimG_-aS1IZChVHJbjPI4CXjIbNFLjn5W686xynepfC0oWyEG81NX5CxdS-9ayumfRljgy32e2bYXDD72T6VpIFFzeCcPKwG48RDKiZExwNdF-4XDFicISSaaRtT3W2dt0/s1700-nu-rw-lo-l85-e365/windows-lockscreen.jpg)

A newly disclosed unpatched zero-day technique called **FastUnlock** lets someone with physical access to a locked Windows computer start programs without signing in. Whoever uses it gets only a limited account, not administrator control of the machine.

The method was posted yesterday by a researcher who uses the handles **MSNightmare** and **Nightmare Eclipse**, and the endpoint-security firm ThreatLocker tested it the same day and found it works.

There is no fix from Microsoft yet, and nothing shows the method has been used in a real attack.

The technique does not work on every machine. It requires physical access to the computer and a Microsoft account accessible through the lock screen's recovery options, and it uses Windows' built-in screen reader, Narrator, to navigate the locked screen.

In its test, the firm reached a point where it could run a program from the lock screen in a limited account that ThreatLocker identified as WSIAccount and said is "not an administrator account."

The researcher's [GitHub disclosure](https://github.com/MSNightmare/FastUnlock) is a short post with a video and little written detail, so the clearest account of what the flaw does comes from the firm's [independent test](https://www.threatlocker.com/blog/proof-of-concept-for-fastunlock-windows-lock-screen-bypass-from-nightmare-eclipse).

Many Windows computers encrypt their drives with **BitLocker**, but in a common setup, that does not make them immune to this technique. A chip called the TPM unlocks the drive automatically when the computer starts, so by the time the lock screen appears, the files are already readable, and the bypass runs at that point. Microsoft's own [TPM documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/how-windows-uses-the-tpm) describes this mode, in which the drive unlocks "without having to enter a PIN."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

FastUnlock does not break that encryption or recover the key. It runs on a computer that has already unlocked its own drive in the normal way, which is a smaller problem than cracking an encrypted disk, though still a real one for a machine someone else is holding.

The conditions above, physical access and a reachable Microsoft account, are what put a machine at risk. No official list of affected Windows versions has been published, so treat any machine that meets those conditions as possibly affected until one is.

### What You Can Do Now

With no patch available, the useful steps are about physical control and startup protection.

* Keep machines that can go missing out of the wrong hands. Lock away or closely manage laptops, shared desks, and front-counter computers that a stranger could reach.
* On sensitive machines, add a startup PIN to BitLocker instead of letting the drive unlock on its own.
* Shut down or hibernate devices when they leave someone's control. A startup PIN protects only a machine that has not yet started, not one already on the lock screen.
* Do not treat a locked screen on its own as enough.

Microsoft's [countermeasures guidance](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/countermeasures) recommends using a startup PIN, along with shutting down or hibernating machines when faced with determined, hands-on attackers. Until an official fix or advisory appears, watch for one and apply it when it comes.

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

[data protection](https://thehackernews.com/search/label/data%20protection), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [operating system security](https://thehackernews.com/search/label/operating%20system%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Default 'admin:admin' Server Password Helps Researchers Hack Two Automakers, Unlock and Start Cars](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)

[![The Hacker News](data:image/svg+xml;base64...)

PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html)

[![The Hacker News](data:image/svg+xml;base64...)

New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs](https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html)

...