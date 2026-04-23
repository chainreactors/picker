---
title: Mustang Panda’s New LOTUSLITE Variant Targets India Banks, South Korea Policy Circles
url: https://thehackernews.com/2026/04/mustang-pandas-new-lotuslite-variant.html
source: The Hacker News
date: 2026-04-22
fetch_date: 2026-04-23T04:45:14.931380
---

# Mustang Panda’s New LOTUSLITE Variant Targets India Banks, South Korea Policy Circles

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Mustang Panda’s New LOTUSLITE Variant Targets India Banks, South Korea Policy Circles](https://thehackernews.com/2026/04/mustang-pandas-new-lotuslite-variant.html)

**Ravie Lakshmanan**Apr 22, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQHPkb7rlS_ueovJaV3s5KxgSQFfHhuZhvW8R8L9wG8j-trZvnmusj4EGvkOPah_XSqgJDLIiRWozv7RtA3o_1VaHYWnaH77PH2kOg2FYkc60uIc6WTf6frjbUp3IwhtB038_wojAl7G5OxcC4aSy5kLF48ssz_3xqLCD7bDbg6_i-RdY8tLvjxlj4Xc0o/s1700-e365/indian-banks.jpg)

Cybersecurity researchers have discovered a new variant of a known malware called **LOTUSLITE** that's distributed via a theme related to India's banking sector.

"The backdoor communicates with a dynamic DNS-based command-and-control server over HTTPS and supports remote shell access, file operations, and session management, indicating a continued espionage-focused capability set rather than financially motivated objectives," Acronis researchers Subhajeet Singha and Santiago Pontiroli [said](https://www.acronis.com/en/tru/posts/same-packet-different-magic-mustang-panda-hits-indias-banking-sector-and-korea-geopolitics/) in an analysis.

The use of LOTUSLITE was [previously observed](https://thehackernews.com/2026/01/lotuslite-backdoor-targets-us-policy.html) in spear-phishing attacks targeting U.S. government and policy entities using decoys associated with the geopolitical developments between the U.S. and Venezuela. The activity was attributed with medium confidence to a Chinese nation-state group tracked as Mustang Panda.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeSnuZMsTn46viNI6XBVImY0eE_omV9JpDiEMw4MyRp4OMy7q7NX1C1Nal98_REvwDll7c3zUCB7XaJEiiFPsP5eh0G_T7HABh4PAhuc0R92NED5-MUaTn4lCjLi9o9J21UnWx9JQrU0-MEvooL1P-mdu1EfeFumDu3GopyyS_3YHopnj8c6iqlxisYyLK/s1700-e365/chain.jpg)

The latest activity flagged by Acronis involves deploying an evolved version of LOTUSLITE that demonstrates "incremental improvements" over its predecessor, indicating that the malware is being actively maintained and refined by its operators.

The deviation from the prior attack wave relates to a geographic pivot that focuses mainly on the banking sector of India, while keeping the rest of the operational playbook mostly intact. The starting point of the attack is a Compiled HTML (CHM) file embedding the malicious payloads – a legitimate executable and a rogue DLL – along with an HTML page that contains a pop-up which prompts the user to click "Yes."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

This step is designed to silently retrieve and execute a JavaScript malware from a remote server ("cosmosmusic[.]com"), whose primary responsibility is to extract and run the malware contained inside the CHM file using [DLL side-loading](https://techzone.bitdefender.com/en/tech-explainers/what-is-dll-sideloading.html). The DLL ("dnx.onecore.dll") is an updated version of LOTUSLITE that communicates with the domain "editor.gleeze[.]com" to receive commands and exfiltrate data of interest.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGQcAv2nc7ZwtvHU_Io-3unyJEpC-eeMDcgI1hWeIfoaQmOCPOYdLNWLG73LxehOJWBHseUd3WC_wEEpSpbuEcCT8vwcOK9pJBB1iirRJd_qQi3RWuBr1EdVfkZCtqbr_mGN-rQq3u8trKBGcCzTSRvOHTjUGUfcII-pbBW_hORi5sq_hqUPlRvhbcnDz-/s1700-e365/ssl.jpg)

Further analysis of the campaign has uncovered similar artifacts designed to target South Korean entities, specifically individuals within the policy and diplomatic community.

"We believe that the group had been targeting certain entities belonging to the South Korean and U.S. diplomatic and policy communities, specifically those involved in Korean peninsula affairs, North Korea policy discussions and Indo-Pacific security dialogues," Acronis said.

"What stands out is the broadening of the group's targeting, from U.S. government entities with geopolitical lures, to India's banking sector through implants embedded with HDFC Bank references and pop-ups masquerading as legitimate banking software, and now to South Korean and U.S. policy circles through the impersonation of a prominent figure in Korean peninsula diplomacy, delivered via spoofed Gmail accounts and Google Drive staging."

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

[Acronis](https://thehackernews.com/search/label/Acronis), [banking security](https://thehackernews.com/search/label/banking%20security), [cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DLL side-loading](https://thehackernews.com/search/label/DLL%20side-loading), [Malware](https://thehackernews.com/search/label/Malware), [Phishing](https://thehackernews.com/search/label/Phishing), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;base64... "Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reach...