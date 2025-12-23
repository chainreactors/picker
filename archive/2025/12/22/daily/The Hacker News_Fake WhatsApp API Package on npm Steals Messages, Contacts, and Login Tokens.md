---
title: Fake WhatsApp API Package on npm Steals Messages, Contacts, and Login Tokens
url: https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html
source: The Hacker News
date: 2025-12-22
fetch_date: 2025-12-23T03:25:46.712680
---

# Fake WhatsApp API Package on npm Steals Messages, Contacts, and Login Tokens

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Fake WhatsApp API Package on npm Steals Messages, Contacts, and Login Tokens](https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html)

**Dec 22, 2025**Ravie LakshmananMalware / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivmlgJ1Ik_0R32UVEqmVu8yRjzKyNEMijqN7ox6JMNp9RQFOtpeBhDHEcgQH6eL6SgRRF3z6pH4YHh2fanPXGIIyrMJIUZ72Nm4JOWYycoqFnvzyFcbuufQHdjxdde1_MIZ0SiSsG8EyrzC0KpF-pO4Nvzpg2OtpApM_F0pZizo46YpYmU6Jj0dA1YvHiz/s790-rw-e365/whatsapp-api.jpg)

Cybersecurity researchers have disclosed details of a new malicious package on the npm repository that works as a fully functional WhatsApp API, but also contains the ability to intercept every message and link the attacker's device to a victim's WhatsApp account.

The package, named "[lotusbail](https://www.npmjs.com/package/lotusbail)," has been downloaded [over 56,000 times](https://npm-stat.com/charts.html?package=lotusbail) since it was first uploaded to the registry by a user named "seiren\_primrose" in May 2025. Of these, 711 downloads took place over the last week. The library is still available for download as of writing.

Under the cover of a functional tool, the malware "steals your WhatsApp credentials, intercepts every message, harvests your contacts, installs a persistent backdoor, and encrypts everything before sending it to the threat actor's server," Koi Security researcher Tuval Admoni [said](https://www.koi.ai/blog/npm-package-with-56k-downloads-malware-stealing-whatsapp-messages) in a report published over the weekend.

Specifically, it's equipped to capture authentication tokens and session keys, message history, contact lists with phone numbers, as well as media files and documents. More significantly, the library is inspired by [@whiskeysockets/baileys](https://www.npmjs.com/package/%40whiskeysockets/baileys), a legitimate WebSockets-based TypeScript library for interacting with the WhatsApp Web API.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

This is accomplished by means of a malicious WebSocket wrapper through which authentication information and messages are routed, thereby allowing it to capture credentials and chats. The stolen data is transmitted to an attacker-controlled URL in encrypted form.

The attack doesn't stop there, for the package also harbors covert functionality to create persistent access to the victim's WhatsApp account by hijacking the [device linking process](https://thehackernews.com/2025/12/threatsday-bulletin-whatsapp-hijacks.html#whatsapp-hijack-campaign) by using a hard-coded pairing code.

"When you use this library to authenticate, you're not just linking your application -- you're also linking the threat actor's device," Admoni said. "They have complete, persistent access to your WhatsApp account, and you have no idea they're there."

By linking their device to the target's WhatsApp, it not only allows continued access to their contacts and conversations but also enables persistent access even after the package is uninstalled from the system, given the threat actor's device remains linked to the WhatsApp account until it's unlinked by navigating to the app's settings.

Koi Security's Idan Dardikman told The Hacker News that the malicious activity is triggered when the developer uses the library to connect to WhatsApp.

"The malware wraps the WebSocket client, so once you authenticate and start sending/receiving messages, the interception kicks in," Dardikman said. "No special function needed beyond normal usage of the API. The backdoor pairing code also activates during the authentication flow – so the attacker's device gets linked the moment you connect your app to WhatsApp."

Furthermore, "lotusbail" comes fitted with anti-debugging capabilities that cause it to enter into an infinite loop trap when debugging tools are detected, causing it to freeze execution.

"Supply chain attacks aren't slowing down – they're getting better," Koi said. "Traditional security doesn't catch this. Static analysis sees working WhatsApp code and approves it. Reputation systems have seen 56,000 downloads, and trust it. The malware hides in the gap between 'this code works' and 'this code only does what it claims.'"

### Malicious NuGet Packages Target the Crypto Ecosystem

The disclosure comes as ReversingLabs [shared](https://www.reversinglabs.com/blog/nuget-malware-crypto-oauth-tokens) details of 14 malicious NuGet packages that impersonate Nethereum, a .NET integration library for the Ethereum decentralized blockchain, and other cryptocurrency-related tools to redirect transaction funds to attacker-controlled wallets when the transfer amount exceeded $100 or exfiltrate private keys and seed phrases.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfqlLm0nO31cZsxBAe_qm4vXX5mLyCs1uPJmiULBZhIrfIorSjIz4VGeE8SHECXTt9tfJJyDOwUW8b37W5Qyie53QJ7FX2ctoAlMMjq5n8a0l7gf_W4zu4XDRZ_m9JBGNOHZzsQN7zCw6ZZysU7F_K3QbC7rZRw-xeAI2Y4UM7QUV9FIj6P80cSCUTteGt/s790-rw-e365/nuget.png)

The names of the packages, published from eight different accounts, are listed below -

* binance.csharp
* bitcoincore
* bybitapi.net
* coinbase.net.api
* googleads.api
* nbitcoin.unified
* nethereumnet
* nethereumunified
* netherеum.all
* solananet
* solnetall
* solnetall.net
* solnetplus
* solnetunified

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

The packages have leveraged several techniques to lull users into a false sense of trust in security, including inflating download counts and publishing dozens of new versions in a short amount of time to give the impression that it's being actively maintained. The campaign dates all the way back to July 2025.

The malicious functionality is injected such that it's only triggered when the packages are installed by developers and specific functions are embedded into other applications. Notable among the packages is GoogleAds.API, which focuses on stealing Google A...