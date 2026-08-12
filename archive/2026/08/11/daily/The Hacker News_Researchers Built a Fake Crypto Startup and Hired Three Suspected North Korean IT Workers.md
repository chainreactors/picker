---
title: Researchers Built a Fake Crypto Startup and Hired Three Suspected North Korean IT Workers
url: https://thehackernews.com/2026/08/researchers-built-fake-crypto-startup.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:49.979243
---

# Researchers Built a Fake Crypto Startup and Hired Three Suspected North Korean IT Workers

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

# [Researchers Built a Fake Crypto Startup and Hired Three Suspected North Korean IT Workers](https://thehackernews.com/2026/08/researchers-built-fake-crypto-startup.html)

**Swati Khandelwal**Aug 11, 2026Insider Threat / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIGgelUshBcG56Nc5uWqBbhQwtUxWtNgSIRTCiJXZoJtkuTWeXEV0KiWRje-UhGGnrvf6wNOmmBGQ7yAxKNigAuJE00RicY4ris0k02Dd_1ch7_RcSM2aJtGvgf4miSazvFMNEqTmVDY3nlDT1zPwg5vkafqzMwbkFRZ1kO4xU2mzZgfxAEUTM0zObjGE/s1700-e365/nk.jpg)

Security researchers invented a cryptocurrency startup, advertised developer jobs, and hired three people they believe were North Korean operatives. Every virtual machine the company issued was recording.

The onboarding paperwork is the part hiring teams can use. The first hire claimed to live in Pasadena, Texas, then sent a California driver's license and a New York bank account.

The researchers said the image metadata showed it had been processed with Google Gemini. They also reported a SynthID watermark, the invisible marker Google embeds in images its AI tools create or edit.

The second supplied a Texas license, a valid Social Security number, and a bank account in Kansas City. The third sent a New York license belonging to someone else, a genuine iPhone 15 photograph with the GPS coordinates stripped.

A successful placement gives the operative a real employee account and real access to source code and internal systems. The July 31 joint alert says North Korean IT workers seek contracts with the intent of remitting their salaries to parent North Korean agencies. It also names documents "forged or altered using image editing software" among the signals employers should watch for.

In April, the [Justice Department](https://www.justice.gov/opa/pr/two-us-nationals-sentenced-facilitating-fraudulent-remote-information-technology-worker) sentenced two US facilitators over a separate scheme that placed workers at more than 100 US companies on at least 80 stolen identities and earned North Korea more than $5 million. Google's Gemini app can check an image for a SynthID watermark, but it only detects content created or edited by Google's AI models. A negative result does not rule out AI editing by other tools.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The operation was a sequel. A joint investigation by Mauro Eldritch of BCA LTD, Heiner García of NorthScan, and [ANY.RUN](https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/), a provider of interactive malware analysis and threat intelligence, spent late 2025 posing as a facilitator willing to rent out his identity. The Hacker News [covered that operation](https://thehackernews.com/2025/12/researchers-capture-lazarus-apts-remote.html) in December.

This time they became the employer, building a fake DeFi protocol called **Ballena Azul**. A recruiter trawling GitHub for facilitators delivered the first developer. That developer vouched for a friend, who vouched for a third.

Nobody exploited anything.

Each operative came in through the hiring process, cleared an interview, signed a contract, and was given access to a work VM. The researchers write that these schemes are "not only a hiring risk" because once a placement holds, the worker's access is also authorized and expected.

Day one was reconnaissance. All three ran dxdiag, systeminfo, and wmic to profile their machines, then checked what country their connection appeared to originate from. One then installed Chrome Remote Desktop and synced his personal Google account to the sandbox, handing over his browsing history, saved passwords and installed extensions. He logged into GitHub on the same machine.

The tooling observed in this engagement differed from December. The researchers saw 2fa.cn used for passing two-factor codes between operators; the December operation had used authenticator.cc and otp.ee. Outlook.com appeared where only Gmail had before.

Their browsers carried AI job-application and interview-assistance extensions: AIApply, Final Round AI, Simplify Copilot and a saved-prompts tool for ChatGPT. The report places infrastructure on Vultr and Gorilla Servers and says [AstrillVPN exit nodes](https://thehackernews.com/2026/03/ofac-sanctions-dprk-it-worker-network.html) ran throughout.

[Silent Push has separately tracked](https://www.silentpush.com/blog/astrill-vpn/) Astrill as a fixture of North Korean operations.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The researchers advise periodic identity checks rather than one at hire, in-person verification for remote-first companies, recruiter training, and blocking AstrillVPN. The [July 31 advisory](https://www.ic3.gov/CSA/2026/260731.pdf) further notes a single account reached from many addresses in a short window and profile text that reads like machine translation.

The report presents the Gemini-processing metadata and the SynthID watermark as separate findings but does not explain how the watermark itself was detected.

Attribution rests with the researchers, who presented the work at DEF CON 34 in Las Vegas this month. They describe the three as suspected [Famous Chollima](https://thehackernews.com/2025/08/us-treasury-sanctions-dprk-it-worker.html) operatives. CrowdStrike uses that name for North Korea's IT worker operation, while the team places it under the wider Lazarus umbrella.

The eleven-government alert names no vendor actor cluster at all. As of August 11, no government source reviewed for this article had confirmed that identification. The real names behind the three personas are unknown, and the report gives no dates for how long the fake company ran.

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
[**Share...