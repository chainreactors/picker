---
title: 100+ Fake Chrome Extensions Found Hijacking Sessions, Stealing Credentials, Injecting Ads
url: https://thehackernews.com/2025/05/100-fake-chrome-extensions-found.html
source: The Hacker News
date: 2025-05-21
fetch_date: 2025-10-06T22:29:42.134200
---

# 100+ Fake Chrome Extensions Found Hijacking Sessions, Stealing Credentials, Injecting Ads

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

# [100+ Fake Chrome Extensions Found Hijacking Sessions, Stealing Credentials, Injecting Ads](https://thehackernews.com/2025/05/100-fake-chrome-extensions-found.html)

**May 20, 2025**Ravie LakshmananCredential Theft / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9-Oa58jl3Hg4GUlsgHZkt5tqF9PiDnEig_pnfkc_yRkawR4ksZLkQazxJJ4aZbarymldktl-cR3DaclZpwCGdsz4ca0269Jbrx4tbLJ9rIkxlcKNbH1HWg6Clx3phGstaZdMmtIOlEiFwixXu1RJ4hdtAygJimqJwfJBGe-17yShFpcHEWnMMB98rXROE/s790-rw-e365/chrome-malware.jpg)

An unknown threat actor has been attributed to creating [several malicious Chrome Browser extensions](https://github.com/DomainTools/SecuritySnacks/blob/main/2025/DualFunction-Malware-Chrome-Extensions) since February 2024 that masquerade as seemingly benign utilities but incorporate covert functionality to exfiltrate data, receive commands, and execute arbitrary code.

"The actor creates websites that masquerade as legitimate services, productivity tools, ad and media creation or analysis assistants, VPN services, crypto, banking and more to direct users to install corresponding malicious extensions on Google's Chrome Web Store (CWS)," the DomainTools Intelligence (DTI) team [said](https://dti.domaintools.com/dual-function-malware-chrome-extensions/) in a report shared with The Hacker News.

While the browser add-ons appear to offer the advertised features, they also enable credential and cookie theft, session hijacking, ad injection, malicious redirects, traffic manipulation, and phishing via DOM manipulation.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Another factor that works in the extensions' favor is that they are configured to grant themselves excessive permissions via the manifest.json file, allowing them to interact with every site visited on the browser, execute arbitrary code retrieved from an attacker-controlled domain, perform malicious redirects, and even inject ads.

The extensions have also been found to rely on the "[onreset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/reset_event)" event handler on a temporary document object model (DOM) element to execute code, likely in an attempt to bypass content security policy (CSP).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWe8d6t8ulIDr9JgJp57eeM_OC2MF8Fx56v5tSy1kUdUajxysUyRoofM3zRk5cN4nMNiWyT08YpwIiINfxyXv9HEpwoCYjWPaG8sNE5UHCovNydvweGHL1GAzydJ7mcyweEwwBgX6IsyxZ4OQMW3AOsGxCC4cVlZX9-f3SPOtV7lLDgUBvxHMwOO3byN9h/s790-rw-e365/chrome.jpg)

Some of the identified lure websites impersonate legitimate products and services like DeepSeek, Manus, DeBank, FortiVPN, and Site Stats to entice users into downloading and installing the extensions. The add-ons then proceed to harvest browser cookies, fetch arbitrary scripts from a remote server, and set up a WebSocket connection to act as a network proxy for traffic routing.

There is currently no visibility into how victims are redirected to the bogus sites, but DomainTools told the publication that it could involve usual methods like phishing and social media.

"Because they appear in both Chrome Web Store and have adjacent websites, they can return from as results in normal web searches and for searches within the Chrome store," the company said. "Many of the lure websites used Facebook tracking IDs, which strongly suggests they are leveraging Facebook / Meta apps in some way to attract site visitors. Possibly through Facebook pages, groups, and even ads."

As of writing, it's not known who is behind the campaign, although the threat actors have set up over 100 fake websites and malicious Chrome extensions. Google, for its part, has taken down the extensions.

To mitigate risks, users are advised to stick with verified developers before downloading extensions, review requested permissions, scrutinize reviews, and refrain from using lookalike extensions.

That said, it's also worth keeping in mind that ratings could be manipulated and artificially inflated by filtering negative user feedback.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

DomainTools, in an analysis published late last month, [found](https://dti.domaintools.com/deceptive-browser-extensions-google-store-ai-slop/) evidence of extensions impersonating DeepSeek that redirected users providing low ratings (1-3 stars) to a private feedback form on the ai-chat-bot[.]pro domain, while sending those providing high ratings (4-5 stars) to the official Chrome Web Store review page.

### Update

In a follow-up analysis, LayerX said it identified over 40 malicious browser extensions that are part of three distinct phishing campaigns, many of which it said are still available for download from the Chrome Web Store.

The extensions, the browser security company said, are designed to impersonate popular tools/brands and exhibit similar structure, formatting, and language, raising the possibility that they may have been auto-generated using AI tools.

"This tactic enabled threat actors to rapidly scale their efforts across dozens of fake tools with minimal manual effort," LayerX said. "These extensions grant attackers persistent access to user sessions, allowing for data theft, impersonation, and potential entry into corporate environments."

Or Eshed, CEO of LayerX Security, noted that removing the add-ons from the Chrome Web Store does not automatically uninstall them from end users' devices, requiring users to manually get rid of them. The complete list of extensions can be accessed [here](https://layerxsecurity.com/blog/layerx-reveals-40malicious-browser-extensions/).

"This is especially a problem in organizations, where even a single compromised endpoint or corporate account can lead to exposure at the organizational level," Eshed said. "Our best practice recommendation to organizations is to check each of these extensions individually to make sure they are removed ...