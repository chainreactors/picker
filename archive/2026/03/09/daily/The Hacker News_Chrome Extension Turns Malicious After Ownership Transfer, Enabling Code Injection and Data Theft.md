---
title: Chrome Extension Turns Malicious After Ownership Transfer, Enabling Code Injection and Data Theft
url: https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html
source: The Hacker News
date: 2026-03-09
fetch_date: 2026-03-10T04:04:05.717807
---

# Chrome Extension Turns Malicious After Ownership Transfer, Enabling Code Injection and Data Theft

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Chrome Extension Turns Malicious After Ownership Transfer, Enabling Code Injection and Data Theft](https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html)

**Ravie Lakshmanan**Mar 09, 2026Browser Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgH49NW0X18R8bc0fzFm6aPt92f15pxPq-HLMfyFmsApiXvZEsCn4z9qNQErHHvW34SFXKUPWy7mK70hM06Ld6Cxa4DioW7xjV9jnMamMF3DDKIQ39VwJhvq7l4bO79yzGp8huA6ewRk-XdWvJSeYT8fs16PdOa9BSxdbzw0hIwC1PVxh9uY5L0Wx3nNMAL/s1700-e365/chrome-malware.jpg)

Two Google Chrome extensions have turned malicious after what appears to be a case of [ownership transfer](https://x.com/tuckner/status/2027416172442853830), offering attackers a way to push malware to downstream customers, inject arbitrary code, and harvest sensitive data.

The extensions in question, both originally associated with a developer named "akshayanuonline@gmail.com" (BuildMelon), are listed below -

* QuickLens - Search Screen with Google Lens (ID: kdenlnncndfnhkognokgfpabgkgehodd) - 7,000 users
* ShotBird - Scrolling Screenshots, Tweet Images & Editor (ID: gengfhhkjekmlejbhmmopegofnoifnjp) - 800 users

While QuickLens is no longer available for download from the Chrome Web Store, ShotBird remains accessible as of writing. ShotBird was [originally launched](https://www.reddit.com/r/chrome_extensions/comments/1gkv28r/free_say_hello_to_shotbird_make_better/) in November 2024, with its developer, Akshay Anu S (@AkshayAnuOnline), [claiming](https://x.com/AkshayAnuOnline/status/1854777234541642035) on X that the extension is suitable for "creating professional, studio-like visuals," and that all processing happens locally.

According to [research](https://monxresearch-sec.github.io/shotbird-extension-malware-report/) published by monxresearch-sec, the browser add-on received a "Featured" flag in January 2025, before it was passed on to a different developer ("loraprice198865@gmail.com") sometime last month.

In a similar vein, QuickLens was listed for sale on ExtensionHub on October 11, 2025, by "akshayanuonline@gmail.com" merely two days after it was published, Annex Security's John Tuckner [said](https://annex.security/blog/pixel-perfect/). On February 1, 2026, the extension's owner changed to "support@doodlebuggle.top" on the Chrome Web Store listing page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The malicious update introduced to QuickLens on February 17, 2026, kept the original functionality but introduced capacities to strip security headers (e.g., X-Frame-Options) from every HTTP response, allowing malicious scripts injected into a web page to make arbitrary requests to other domains, bypassing Content Security Policy ([CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)) protections.

In addition, the extension contained code to fingerprint the user's country, detect the browser and operating system, and polls an external server every five minutes to receive JavaScript, which is stored in the browser's local storage and executed on every page load by adding a hidden 1×1 GIF <img> element and setting the JavaScript string as its "onload" attribute. This, in turn, causes the malicious code to be executed once the image is loaded.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtbNVFQArInH_tIqk1dHv8QtD4RMtEkzUjgiEzaxf4z0lmK6RcYoKLyd9KlMLtR3pXGvE4vJEaO046ysdQwH7zP0-1R9WqRMYBEsTgTbDk6tINfKUZ4R9W7Klf38B5DvTduvDARTerx7w9IEZ8PCu0ytRoPVr9nu6Vxzngv2PrndHNlMz5f6C28dfZCaya/s1700-e365/short.png)

"The actual malicious code never appears in the extension's source files," Tuckner explained. "Static analysis shows a function that creates image elements. That's it. The payloads are delivered from the C2 and stored in local storage -- they only exist at runtime."

A similar analysis of the ShotBird extension by monxresearch-sec has uncovered the use of direct callbacks to deliver JavaScript code instead of creating a 1x1 pixel image to trigger the execution. The JavaScript is engineered to display a bogus Google Chrome browser update prompt, clicking which users are served a ClickFix-style page to open the Windows Run dialog, launch "cmd.exe," and paste a PowerShell command, resulting in the download of an executable named "googleupdate.exe" on Windows hosts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghw5aOSEwX7E3oTaco23HX_tRAaOQWXAv5il2MoG38psjlOR7Nct0E4393oLqMRE9snrm60Cl1laVyqL9MTgnH3R1sBPaq1CQuLW4yPoOALBlZ2NVLFZC3UF9HNUsuylPVxzf2QBeM00bRKoHSaNs0zVXbhibhq68M3zfgaGamUcTuIuQv66gfyVEA7i8z/s1700-e365/supply.png)

The malware then proceeds to hook input, textarea, select HTML elements, and capture any data entered by the victim. This could include credentials, PIN, card details, tokens, and government identifiers. It's also equipped to siphon data stored in the Chrome web browser, such as passwords, browsing history, and extension-related information.

"This is a two-stage abuse chain: extension-side remote browser control plus host-level execution pivot via fake updates," the researcher said. "The result is high-risk data exposure in-browser and confirmed host-side script execution on at least one affected system. In practical terms, this elevates the impact from browser-only abuse to likely credential theft and broader endpoint compromise."

It's assessed that the same threat actor is behind the compromise of the two extensions and is operating them in parallel, given the use of an identical command-and-control (C2) architecture pattern, ClickFix lures injected into the browsing context, and ownership transfer as an infection vector.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPooBnA_BkLKvWR7VnMPD1tAnk4ionaZ-EEKjpOlhyphenhyphenU9htgxvrnhocDSplm6DYEjgCRD6ouBSDJr_0kn61JnHfrCBaZRD3-fwDqcHgLwpaXsJdTAdAhJhjjrYXVRGrwdib54XE-...