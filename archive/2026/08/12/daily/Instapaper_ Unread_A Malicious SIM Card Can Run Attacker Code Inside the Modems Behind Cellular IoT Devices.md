---
title: A Malicious SIM Card Can Run Attacker Code Inside the Modems Behind Cellular IoT Devices
url: https://thehackernews.com/2026/08/a-malicious-sim-card-can-run-attacker.html
source: Instapaper: Unread
date: 2026-08-12
fetch_date: 2026-08-13T04:05:27.510080
---

# A Malicious SIM Card Can Run Attacker Code Inside the Modems Behind Cellular IoT Devices

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

![cybersecurity](data:image/svg+xml;base64...)

# [A Malicious SIM Card Can Run Attacker Code Inside the Modems Behind Cellular IoT Devices](https://thehackernews.com/2026/08/a-malicious-sim-card-can-run-attacker.html)

**Swati Khandelwal**Aug 11, 2026IoT Security / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-_ftAONA3vSU_pho_96pouqt_n3CXa1PRfS2fhilG7JBshSuPpKNZzKVFvPRASkzNSVrDj-U4sISWf8TN9fuNqgAr4g07OYcRzZ7ecqVlAkd_C1EBL2bJZBCKMA90CLSrWN_s3I2-dhBLDGuH3juBdciPUruhDBkC2826KaVwB41tr122SnxgBeWw3VM/s1700-e365/malware-sim.jpg)

A malicious SIM card can order the device it sits in to run commands of the attacker's choosing. On the cellular modules built into electric-vehicle chargers, industrial routers, and car telematics units, that is enough to take the whole device over.

Researchers at the University of Birmingham and the security firm Fuzzware tested 26 phones and cellular modules for the capability, found it switched on in 9 of them, and used it to run their own code on a commercial EV charger.

Six of the [eight cellular modules they tested](https://www.usenix.org/system/files/woot26-lisowski.pdf) accepted the command. Only 3 of 18 phones did: the OPPO Find X5, the OPPO Reno 14 F 5G, and the ASUS Zenfone 9. No iPhone or Pixel was among them.

The exposure is in machine-to-machine hardware. Five of the six were Quectel parts, three of them pulled from an EV charger, an industrial router, and a car's telematics control unit.

Knowing the victim's number is not enough: every attack starts with a hostile card already in the slot, swapped by hand, slipped in as a thin interposer, pushed out by a compromised operator, or subverted in software or on the production line. Unattended IoT gear with an accessible SIM tray and few other exposed interfaces is exactly where that trade is worth making.

There is no single patch. Every one of the nine devices that accepted the command runs a Qualcomm communication processor. Five other Qualcomm-based handsets in the survey did not accept it, which the paper suggests is down to vendor customisation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Qualcomm told the researchers it has built a hardened configuration that switches the interface off by default. Quectel says it has mitigated the file-access flaw and is still working on the interface itself. Neither has published an advisory, and the module maker's vulnerability portal requires a login to see anything at all.

The researchers' own position is that the interface should be hardened, deprecated, or disabled outright. That hardened configuration will be the default on future devices, the researchers told The Hacker News, and fixes will also reach affected modules as updates, though the team has not checked whether the RUN AT code paths are removed or only switched off. For anyone running cellular IoT fleets, the step available today is to ask the module supplier whether RUN AT is enabled in the firmware they shipped and whether it can be disabled. No attacks using the interface have been reported.

The command in question is [a proactive command](https://thehackernews.com/2019/09/simjacker-mobile-hacking.html), part of the standardised set a SIM can push back at the modem instead of waiting to be read. RUN AT asks the modem to execute an AT command, the modem control language that dates to the 1981 Hayes Smartmodem and that every vendor extends with its own additions. Supporting it therefore hands the card a general-purpose console.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmiqMmxlZmhqPzf3_fVcaZc6wsgfjXcuEmbaNzQbKYoCfKd49JhUY7dUjDBj4BiKfXLFFtd8phpL7Vn4ITBIQ0cjObISp52Bhwe_D3Nen8Ci_DJyQZVQcwidLPwJda0AvKhSOAFAGQJEGx-lr57AE8Kjt7LklpsNsTPURyD77ii6FJe3SxysYNX3cjqBU/s1700-e365/sim-1.jpg)

Marius Muench, assistant professor in computer science at the University of Birmingham, said in the university's announcement of the work that the SIM's proactive capability and the attack surface it opens are "explicitly defined in the technical specifications for cellular communication", which is why he frames the result as compliant with the standard rather than a break from it.

That framing matters for what a fix looks like. The individual flaws are ordinary bugs and can be patched; the interface that exposes them is a documented capability, and switching it off is a decision each vendor makes for its own products.

Architecture is what makes the IoT side worse. Nearly every module the team examined runs a small application processor alongside the radio, usually Android on an ARM Cortex-A7, and passes up any AT command the radio does not handle itself. The card ends up talking to a little Linux computer, which [their paper](https://www.usenix.org/conference/woot26/presentation/lisowski), presented this week at USENIX WOOT in Baltimore, calls "a rich attack surface to hostile SIMs."

The charger is a commercial Autel unit that the paper identifies by the model code MAXI US AC W12-L-4G. Inside it, the Quectel EC25AFXDGA module's atfwd\_daemon passes attacker-controlled text into a shell call through an unsafe format string. A character blocklist was supposed to stop shell escapes. A newline got past it. Two stages later, the team had code execution, driven entirely by commands the SIM issued. Autel is not among the companies the write-up says were notified; the flawed code belongs to the module. Muench told The Hacker News the team disclosed to Quectel as the module vendor, which then notified its own customers.

On an OPPO Reno 14 F 5G, one of the three handsets that accepted RUN AT, the command AT+COPS=0,,,0 pinned the phone to 2G. The owner cannot undo it. Not by toggling airplane mode, not by switching to manual network selection, not by toggling mobile data, not by disabling the SIM, not by changing the preferred network generation in settings. 2G has no mutual authentication, so a downgrade the victim cannot reverse hands an attacker the conditions for [a fake base station](https://thehackernews.com/2024/10/android-14-adds-new-security-features.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Two further commands powered the handset down and shut off the mo...