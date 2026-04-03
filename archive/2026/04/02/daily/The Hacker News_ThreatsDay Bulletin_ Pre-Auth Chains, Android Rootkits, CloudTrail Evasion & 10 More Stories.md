---
title: ThreatsDay Bulletin: Pre-Auth Chains, Android Rootkits, CloudTrail Evasion & 10 More Stories
url: https://thehackernews.com/2026/04/threatsday-bulletin-pre-auth-chains.html
source: The Hacker News
date: 2026-04-02
fetch_date: 2026-04-03T04:29:26.696908
---

# ThreatsDay Bulletin: Pre-Auth Chains, Android Rootkits, CloudTrail Evasion & 10 More Stories

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [ThreatsDay Bulletin: Pre-Auth Chains, Android Rootkits, CloudTrail Evasion & 10 More Stories](https://thehackernews.com/2026/04/threatsday-bulletin-pre-auth-chains.html)

**Ravie Lakshmanan**Apr 02, 2026Cybersecurity / Hacking News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEht9hzOUmn8npVxC_AyWUe1DLsv1VkWHox2PmDxZnVuG_XnQt7R5l7CZHlYu9m9BcwAib4L0j0x877sDuCF2shmSH3ef0Me-m0sbKDtu-ZEw5RLqLGNsjGJ0o-b_CuKtFg86fMFb-GKVBud7S8PfpsoL4HCqEZypO1NcWfx6ljXcUhC5O4GIjRbhRcG-fIi/s1700-e365/threatsday.jpg)

The latest ThreatsDay Bulletin is basically a cheat sheet for everything breaking on the internet right now. No corporate fluff or boring lectures here, just a quick and honest look at the messy reality of keeping systems safe this week.

Things are moving fast. The list includes researchers chaining small bugs together to create massive backdoors, old software flaws coming back to haunt us, and some very clever new tricks that let attackers bypass security logs entirely without leaving a trace. We are also seeing sketchier traffic on the underground and the usual supply chain mess, where one bad piece of code threatens thousands of apps.

It is definitely worth a quick scan before you log off for the day, if only to make sure none of this is sitting in your own network. Let's get into it.

1. Pre-auth RCE chain exposed

   [Security Flaws in Progress ShareFile](https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/)

   watchTower Labs has [disclosed](https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/) two security flaws in Progress ShareFile (CVE-2026-2699 and CVE-2026-2701) that could be chained to achieve pre-authenticated remote code execution. While CVE-2026-2699 is an authentication bypass via the "/ConfigService/Admin.aspx" endpoint, CVE-2026-2701 refers to a case of post-authenticated remote code execution. An attacker could combine the two vulnerabilities to sidestep authentication and upload web shells. Progress released fixes for the vulnerabilities with Storage Zone Controller 5.12.4 released on March 10, 2026. There are about 30,000 internet-facing instances, making patching against the flaws crucial.

   [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioKTXaq7xM4Vt_WU85ZwiPlldNVEkHLGi8Sj9yuRHhcAgXYVi7N1XqOyerEZFy73AJvqAjuukO-oQnv6YGbBCGtYidicrPXY0cF9m_105jf5QEx3aIfS1jyFqMG1mk9eotWtJZ8XN1ozEsgx7HCYC3OwcOyrZCmuQ90k1h6S2i9zW6CO39l1_umedd_St4/s1700-e365/watch.png)
2. Rootkit spreads via 50+ apps

   [Operation Novoice Rootkit Campaign Targets Older Android Devices](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/new-research-operation-novoice-rootkit-malware-android/)

   A new Android malware named NoVoice has been distributed via more than 50 apps that were downloaded at least 2.3 million times. While apps masqueraded as utilities, image galleries, and games, and offered the advertised functionality, the malware attempted to obtain root access on the device by exploiting 22 Android vulnerabilities that received patches between 2016 and 2021. "If the exploits succeed, the malware gains full control of the device," McAfee Labs [said](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/new-research-operation-novoice-rootkit-malware-android/). "From that moment onward, every app that the user opens is injected with attacker-controlled code. This allows the operators to access any app data and exfiltrate it to their servers." The malware avoids infecting devices in certain regions, like Beijing and Shenzhen in China, and implements more than a dozen checks for emulators, debuggers, and VPNs. It then contacts a remote server to send device information and fetch appropriate exploits to gain root access and disable SELinux. Upon gaining elevated access, the rootkit modifies system libraries to facilitate the execution of malicious code when specific apps are opened, install arbitrary apps, and enable persistence. NoVoice has been found to share some level of overlap with [Triada](https://thehackernews.com/2025/04/triada-malware-preloaded-on-counterfeit.html). One of the targeted apps is WhatsApp, which enabled the malware to harvest data from the app as soon as it was launched. Google has since removed the apps. The highest concentration of infections has been reported in Nigeria, Ethiopia, Algeria, India, and Kenya.
3. FBI flags foreign app risks

   [FBI Warns of Risky Foreign-Developed Mobile Apps](https://www.ic3.gov/PSA/2026/PSA260331)

   The U.S. Federal Bureau of Investigation (FBI) is warning of the data security risks associated with foreign-developed mobile applications. "As of early 2026, many of the most downloaded and top-grossing apps in the United States are developed and maintained by foreign companies, particularly those based in China," the FBI [said](https://www.ic3.gov/PSA/2026/PSA260331). "The apps that maintain digital infrastructure in China are subject to China's extensive national security laws, enabling the Chinese government to potentially access mobile app users' data." The bureau also warned that these apps may harvest contact information under the pretext of inviting friends to use them, store personal data in Chinese servers, or contain malware that could collect data beyond what is authorized by the user. "This could include malicious code and hard-to-remove malware designed to exploit known vulnerabilities in various operating systems and insert a backdoor for escalated privileges, such as enabling the download and execution of additional malicious packages designed to provide unauthorized access to users' data," it added. The FBI did not name the apps, but TikTok, Shein, Temu, and DeepSeek fit the profile.
4. New bureau targets cyber threats

   [U.S. Activates Bureau of Emerging Thr...