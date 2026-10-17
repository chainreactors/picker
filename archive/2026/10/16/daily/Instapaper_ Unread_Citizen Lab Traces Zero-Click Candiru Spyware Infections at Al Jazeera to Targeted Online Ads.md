---
title: Citizen Lab Traces Zero-Click Candiru Spyware Infections at Al Jazeera to Targeted Online Ads
url: https://thehackernews.com/2026/10/citizen-lab-traces-zero-click-candiru.html
source: Instapaper: Unread
date: 2026-10-16
fetch_date: 2026-10-17T06:37:58.084850
---

# Citizen Lab Traces Zero-Click Candiru Spyware Infections at Al Jazeera to Targeted Online Ads

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Citizen Lab Traces Zero-Click Candiru Spyware Infections at Al Jazeera to Targeted Online Ads](https://thehackernews.com/2026/10/citizen-lab-traces-zero-click-candiru.html)

**Swati Khandelwal**Oct 15, 2026Spyware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgE0PuxlZklu67SsXNfh_vZefiytkMx159npHL_6Ln3dNT0yxzyYE55zZU5SMOFGk39ZqhfWzXpYQfXdoZB0gGYdkoPu3cNactAPL9ZuCWdb_v4Hp4ZkoBLtEnzBovntpudGiQZvIwTucBgDRwNzfVR5SNybyZvTANvdqsDPjHVoUQcV3hrBNm0-YMvZK0/s1700-nu-rw-lo-l85-e365/spyware-ads.jpg)

Candiru, an Israeli maker of spyware sold to governments, infected devices at the news network Al Jazeera through ordinary online ads, in attacks that needed no click or other action from the user, researchers at [the Citizen Lab](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) said Thursday.

The hidden attack code ran the moment an ad loaded on the screen, and in some cases the ad loaded out of sight, in the background.

The Citizen Lab, a research group at the University of Toronto, said this is the first public, technical confirmation that mercenary spyware, meaning hacking tools sold to governments, has reached real devices through targeted ads. The method had been described before from leaked company documents, but not shown in a live attack.

The researchers recovered the spyware itself from one device, but not the exploit that breaks into the browser or app to install it. That first break-in step is described from how the attack was set up, not from captured code.

### How the Attack Worked

The ads were placed by Discover-Tech, an Israeli company that presents itself as a normal digital advertising firm. Each ad carried a small piece of code that, when the ad loaded, quietly sent the device's advertising ID and internet address back to a Discover-Tech server, the researchers found.

That server decided whether the device belonged to a target. If it did, the server sent back attack code for the browser or app to run. If it did not, the server sent nothing. Because the ad itself carried no attack code, the ad networks that delivered it had nothing harmful to detect.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

At Al Jazeera, at least 45 devices were targeted in 2024 and 2025, the Citizen Lab said, and it linked the attacks to Candiru with high confidence. The researchers did not say which government was behind the operation.

The network gave the researchers its traffic logs. On infected devices, the logs showed the same order each time: first contact with a Discover-Tech ad server, then a Candiru server that screens the device, then a command-and-control server that runs the spyware.

Al Jazeera also pulled one Windows program file off a compromised device. Its code used the same distinctive techniques as a [Candiru tool the Citizen Lab took apart in 2021](https://citizenlab.ca/research/hooking-candiru-another-mercenary-spyware-vendor-comes-into-focus/), which is the basis for the high-confidence link.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAe611JDMe2g8H2mp0QZPo3BstTcdFVDjQC-JlVnP8YZflTl6Fs9HcIDxe1cld9EjMcCcJcJ6MRqV1iweB52hNzw0_RdCgSEK99Cw65-4SYnz6CTBHb5cNQ8bK0IKiE0n7EoEigEwzcrsnHK4bCjkP5YpND9aTTFF31LQhmva6mSX9eHij4zqa3SzWhQ4/s1700-nu-rw-lo-l85-e365/ads.png)

Al Jazeera staff were targeted once before. In 2020, dozens of its journalists' [iPhones were hacked with NSO Group's Pegasus spyware](https://thehackernews.com/2020/12/iphones-of-36-journalists-hacked-using.html), in a different operation that used a different method.

### Who Discover-Tech and Candiru Are

Google and the advertising trade group IAB Europe had both listed Discover-Tech as an approved ad vendor from 2020 until this month. The company was registered in Israel in 2020 and is led by its chief executive, Dekel Boni.

Candiru is one of the better-known names in the spyware trade. The United States [put it on a trade blacklist in 2021](https://www.commerce.gov/news/press-releases/2021/11/commerce-adds-nso-group-and-other-foreign-companies-entity-list) over spyware used to target government officials, journalists, and activists. In 2025, its assets were [bought by a U.S. investment firm, Integrity Partners](https://www.calcalistech.com/ctechnews/article/r1er11mi61e), and moved into a new company, [reported to be Integrity Labs](https://assets.recordedfuture.com/content/dam/insikt-report-pdfs/2025/cta-2025-0805.pdf), that the sanctions do not cover.

### What the Platforms Did

After the researchers shared their findings, Google and IAB Europe removed Discover-Tech from their vendor lists in early October, the Citizen Lab said. Google cut off the company's access to its ad exchanges, Beeswax removed it, Vungle paused its access for a review, and Eskimi blocked its accounts.

Google [told Reuters](https://www.arabnews.com/media/israeli-firm-used-online-ads-to-run-vast-spy-operation-researchers-say-3006492) it had worked with the researchers and removed Discover-Tech "for systematically violating our policies." IAB Europe said it suspended the company after an audit found policy violations. Comcast, which owns Beeswax, said it acted "following recent activity."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1-gisbWdbwwmZK-X7z-8r9JPTzT6Ixie2U-r2caA92IUKixmV8qjjOsG5i039LwDNa_4e6dUjjfOkGZjVHj_DoaSqu0WpQrYzkD16O294PnFAzxc39VMEQL5xqCPM2l59LwUcrR7r3asa4FDim0r17TPyB_nFsO_DK6gfHCymCDu7PzrNhBNdTZEZy10/s1700-nu-rw-lo-l85-e365/events.png)

Discover-Tech, Candiru's owners, Al Jazeera, and the Russian ad network Yandex did not respond to Reuters. Discover-Tech's website was still online on Thursday and said nothing about the findings.

### How Far the Ads Reached

Discover-Tech's reach went far beyond Al Jazeera. On one of its platforms, the company placed near...