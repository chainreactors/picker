---
title: New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs in Days, Not Years
url: https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html
source: The Hacker News
date: 2026-11-18
fetch_date: 2026-11-19T09:47:35.069907
---

# New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs in Days, Not Years

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

# [New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs in Days, Not Years](https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html)

**Swati Khandelwal**Nov 18, 2026Hardware Security / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpsv4GxAUbzCsIV1umrxZs6VxfD1eFwAeCgRHQQG_dNbP1fLiYe48hM-Wbd_8w5IxlacAwoidLqyQgBmG7YD7qKo0_XcqW2GhggfXshuK1uXz8BOma2H0Jjs8fabCO4IxHBfRopEUFDd0xHRRv43gMeog852Usv40sfcTwnO_9coyxtIMmteJxeJI_oPA/s1700-nu-rw-lo-l85-e365/bitlocker.jpg)

On AMD-based PCs and some Intel PCs, the TPM lockout for **Windows Hello** and **BitLocker** PINs can be reset by someone who opens the PC's case, researchers at Technische Universität Berlin say.

That leaves short PINs open to guessing. In lab tests, the researchers found a four-digit Hello PIN on an AMD laptop and a 6-digit BitLocker PIN on an Intel laptop this way.

Both PINs were set by the researchers and found within 236 tries. From the speeds they measured, they calculate a worst-case of 40 hours for a four-digit Hello PIN, compared to 69 days with the lockout working as documented. For a default six-digit BitLocker PIN, the worst-case time drops from 19 years to 20 days.

AMD confirmed yesterday that its processor firmware has a flaw that allows the attack on some PCs with its chips. It plans fixes for most of those chips between November and February 2027. For now, the researchers advise adding at least two digits to Hello and BitLocker PINs.

The TPM in these PCs is a firmware TPM, built into the processor. Unlike a separate TPM chip, it has no secure storage of its own, according to the [research paper](https://arxiv.org/abs/2611.18126v1) the researchers posted late last week. So it keeps its saved state, including the count of wrong guesses, encrypted on the mainboard's flash chip.

If someone copies that saved state and later writes the old copy back, the count goes back too, unless the PC detects it. Newer PCs try to catch this with counters inside the flash chip, called RPMC, that can only go up.

On AMD PCs that use these counters, the processor's firmware never verifies that a counter actually increased. A small board placed between the processor and the flash chip can block the update and report success, causing the PC to accept the old state.

RPMC chips from flash maker Winbond have a different weakness, the researchers found. A brief drop in the chip's power supply, called a voltage glitch, can cause the chip to reveal the secret key that signs its counter values. With that key, which took about a second to extract with their best settings, the board can forge any counter value.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

On the Intel laptop they tested, one glitch was enough: the laptop's firmware feeds the chip the same value at every boot, so the leaked key kept working after each restart.

For the Hello test, the researchers attacked a locked HP OmniBook 3 with an AMD Ryzen AI 5 330 processor and a BitLocker-encrypted drive. Their setup typed PINs from 1000 upward and reached the correct one, 1235, after 236 tries in 57 minutes.

Windows still forced a restart after every 5 incorrect PIN attempts on that laptop, but no lockout delay was applied. Microsoft's [lockout defaults](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/tpm-fundamentals) lock the TPM after 32 wrong tries and forget one failure every 10 minutes.

The BitLocker test ran on a Framework Laptop 13 with an Intel Core Ultra 5 125H processor and Winbond flash. BitLocker's startup prompt adds no limit of its own, so each reset gave a fresh 32 tries. The setup found the PIN, 123457, after 236 tries in 6 minutes and 55 seconds.

In both tests, the researchers took the flash chip off the mainboard and wired in their own board. A script read the screen, typed PINs, and restarted the laptop through a KVM switch. They also changed firmware settings to slow each laptop's link to the flash chip, because their board could not keep up at full speed.

The researchers make two further claims that their tests did not cover. Either method could be used against either PIN. A recovered Hello PIN can also unlock keys tied to the device and enable Hello-based single sign-on at work, and, in some configurations, pass a multi-factor check.

The researchers have published their attack firmware, board designs, and scripts. They say reproducing the RPMC attacks is not plug-and-play and needs one of their boards. Neither the paper nor the vendor notices published so far describe attacks outside the lab.

### Which PCs the Attack Works On and What Vendors Say

Whether the attack works depends on the processor and the flash chip:

* **AMD-based PCs with RPMC flash:** open to the board that blocks counter updates. The chipmaker has confirmed the firmware flaw behind this and plans to fix it.
* **AMD-based PCs without RPMC flash:** on two AMD desktops in the researchers' tests, writing an old copy back with an ordinary flash programmer reset the count, requiring no board. They conclude that AMD processors likely have no other protection against this, though two desktops may not be representative of all AMD systems.
* **PCs that rely on Winbond RPMC flash:** the researchers say these are open to the leaked-key method whatever the processor, and that only a new chip design can fix it.
* **Intel PCs without RPMC-like flash:** three Intel systems detected the same write-back in those tests.

The researchers expect the AMD firmware flaw to affect AMD PCs that use the Microsoft Pluton security core as their TPM, but did not show this.

On an AMD PC, the owner can boot Linux, for example from a live USB stick, and run the command grep . /sys/bus/pci/drivers/ccp/\*/rpmc\_\* from the researchers' [exposure check](https://github.com/mattifinder/rpmc_attacks). The output indicates whether RPMC flash is present and enabled...