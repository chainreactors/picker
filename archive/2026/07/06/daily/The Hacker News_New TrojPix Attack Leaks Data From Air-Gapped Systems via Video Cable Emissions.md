---
title: New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions
url: https://thehackernews.com/2026/07/new-trojpix-attack-leaks-data-from-air.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:05.802708
---

# New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions](https://thehackernews.com/2026/07/new-trojpix-attack-leaks-data-from-air.html)

**Swati Khandelwal**Jul 06, 2026Cyber Espionage / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLYJDaMKVJEwbsJA1eYJaguihQzJv2dpnIl512z5xBuWojpidgE7mvbGWz27QN-Dnwx74qvCYOYGQNY4h2K00TzF_hz8D6M9gNxWALh2f2bz6jrzwuKvTuuLsb6kwU1O72qPUIjQYHtRwGPCCUYt-TDFJEZ7frhvxvsQa4vWP7HkLRPtXCi0ovIACzurMP/s1700-e365/TrojPix-attack.jpg)

Researchers at [Shandong University](https://view.sdu.edu.cn/info/1101/210020.htm) have shown a fast new way to pull data off computers that are cut off from every network. The technique, called [TrojPix](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-guoming), tweaks on-screen pixels in ways the eye cannot see, so that the video cable carrying them radiates a faint radio signal a nearby receiver can decode.

But TrojPix works only once malware is already on the target machine, so it is a way for stolen data to get out, not a way in. In the researchers' tests, TrojPix hit a peak throughput of 8.1 Mbps and reached as far as 208 meters, the two measured separately rather than together.

Most air-gap covert channels crawl along at bits or kilobits per second; at 8.1 megabits, roughly a megabyte a second, TrojPix could move a 100 MB file in under two minutes. That turns the threat from leaking a password into moving whole files while the monitor looks switched off.

Real-world range is another matter: a receiver still has to fight through walls, shielding, and noise.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The method, which the researchers call **imperceptible pixel modulation**, needs no administrator rights and no hardware changes, they say; user-level malware that can draw to the screen is enough.

They describe two ways to hide the traffic. One fakes a powered-off display, keeping the screen dark while it transmits. The other buries the signal in whatever is already on screen, so ordinary-looking content carries the payload.

The team reports it is working across nine monitor brands and fifteen video cables, so the result is not tied to one setup.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_gDx3-Rndtv271gcj_26jpPiCBt66V9_dbIQG4d_6fTJT5O8yyy6Mr629G2q57AD_Ja7DzFmihGLtwGwu-pdbUZ31TJ23XhReE7-mQWASE-Acn1imLkdY2PmUIyU4ElEp4nOy1EQwCJpFPF2hzGdDl3sTCxLe_sL5zq6X4_pgGTtM4GfFC7JnsNs51xtT/s1700-e365/trojpix.jpg)

Turning a video cable into a covert transmitter is not new. It traces back to the decades-old study of compromising emanations, known as TEMPEST, and more recently to work like [TEMPEST-LoRa](https://arxiv.org/abs/2506.21069) (CCS 2025), which used the same trick to reach off-the-shelf LoRa radios, a common long-range wireless standard.

That one topped out at 87.5 meters, or 21.6 kbps. TrojPix's peak throughput is hundreds of times higher, though the two use different receivers under different conditions, so the numbers are not a head-to-head comparison.

These emission channels remain lab work. The air-gap attacks that have surfaced in the wild, from Stuxnet to Agent.BTZ, crossed the gap on USB drives, not over radio; TrojPix and its kind show what is possible, not what has been caught.

Another screen-based channel, PIXHELL, which [The Hacker News covered in 2024](https://thehackernews.com/2024/09/new-pixhell-attack-exploits-screen.html), made the display itself emit sound to leak data from an air-gapped PC.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

Others have pulled data off Ethernet with a planted [hardware implant](https://arxiv.org/abs/2605.02702), the kind of hardware change TrojPix avoids.

You cannot patch away the emission itself. The countermeasures are physical and preventive: run video over fiber-optic links, which carry no such signal, rather than copper; shield cables and rooms where the data warrants it, as TEMPEST-rated facilities already do; and above all, keep malware off the machine in the first place, since without that foothold, TrojPix has nothing to send.

Once an attacker is inside, a channel this fast can move the data out in the time the screen sits dark.

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

[Covert Channel](https://thehackernews.com/search/label/Covert%20Channel), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [data exfiltration](https://thehackernews.com/search/label/data%20exfiltration), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [hardware security](https://thehackernews.com/search/label/hardware%20security), [Malware](https://thehackernews.com/search/label/Malware), [Physical Security](https://thehackernews.com/search/label/Physica...