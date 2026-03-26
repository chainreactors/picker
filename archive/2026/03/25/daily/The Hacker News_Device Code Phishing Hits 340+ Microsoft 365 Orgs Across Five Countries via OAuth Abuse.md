---
title: Device Code Phishing Hits 340+ Microsoft 365 Orgs Across Five Countries via OAuth Abuse
url: https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html
source: The Hacker News
date: 2026-03-25
fetch_date: 2026-03-26T04:32:06.466978
---

# Device Code Phishing Hits 340+ Microsoft 365 Orgs Across Five Countries via OAuth Abuse

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

# [Device Code Phishing Hits 340+ Microsoft 365 Orgs Across Five Countries via OAuth Abuse](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html)

**The Hacker News**Mar 25, 2026Identity Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifvDHwUAT0Y5sILbpMYi15pftc8kD-oPKrtaUucJ0PLeFRnxKsA14uMC3zCpTPZwj0w7GBTqFQCMfmwzzy_tv-RYTVBijk_x2KWzKkS68n9QfolIhr2B3rSMTGJWg3qt9ZbTYWDiyHmKNT6yD47XPMyS2aj8DF_lyKGKKGWfIsohBlWJvjS_Z3j_XqMZQ/s1700-e365/ms-phish-kit.jpg)

Cybersecurity researchers are calling attention to an active device code phishing campaign that's targeting Microsoft 365 identities across more than 340 organizations in the U.S., Canada, Australia, New Zealand, and Germany.

The activity, per Huntress, was [first spotted](https://www.huntress.com/blog/railway-paas-m365-token-replay-campaign) on February 19, 2026, with subsequent cases appearing at an accelerated pace since then. Notably, the campaign leverages Cloudflare Workers redirects with captured sessions redirected to infrastructure hosted on a platform-as-a-service (PaaS) offering called Railway, effectively turning it into a credential harvesting engine.

Construction, non-profits, real estate, manufacturing, financial services, healthcare, legal, and government are some of the prominent sectors targeted as part of the campaign.

"What also makes this campaign unusual is not just the device code phishing techniques involved, but the variety of techniques observed," the company said. "Construction bid lures, landing page code generation, DocuSign impersonation, voicemail notifications, and abuse of Microsoft Forms pages are all hitting the same victim pool through the same Railway.com IP infrastructure."

[Device code phishing](https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html) refers to a technique that exploits the [OAuth device authorization flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code) to grant the attacker persistent access tokens, which can then be used to seize control of victim accounts. What's significant about this attack method is that the tokens remain valid even after the account's password is reset.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

At a high level, the [attack](https://www.huntress.com/blog/oh-auth-2-0-device-code-phishing-in-google-cloud-and-azure) works as follows -

* Threat actor requests a device code from the identity provider (e.g, Microsoft Entra ID) via the legitimate device code API.
* The service responds with a device code.
* Threat actor creates a persuasive email and sends it to the victim, urging them to visit a sign-in page ("microsoft[.]com/devicelogin") and enter the device code.
* After the victim enters the provided code, along with their credentials and two-factor authentication (2FA) code, the service creates an access token and a refresh token for the user.

"Once the user has fallen victim to the phish, their authentication generates a set of tokens that now live at the OAuth token API endpoint and can be retrieved by providing the correct device code," Huntress explained. "The attacker, of course, knows the device code because it was generated by the initial cURL request to the device code login API."

"And while that code is useless by itself, once the victim has been tricked into authenticating, the resulting tokens now belong to anyone who knows which device code was used in the original request."

The use of device code phishing was first observed by Microsoft and Volexity in February 2025, with subsequent waves documented by Amazon Threat Intelligence and Proofpoint. Multiple Russia-aligned groups tracked as Storm-2372, APT29, UTA0304, UTA0307, and UNK\_AcademicFlare, have been attributed to these attacks.

The technique is insidious, not least because it leverages legitimate Microsoft infrastructure to perform the device code authentication flow, thereby giving users no reason to suspect anything could be amiss.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuLn4vcy3nzM1vjAMcP7c_6MVrS7QlVg4yp_IRBiqYeTMmPU-dV_5K-l1s7y7CNsLoBn4RFX1VzGNhEvN6tIDGlYho3j2Nk6PxVipVh7j6XyK95P_IEDlbRQvohTRwm4Zka4WRRJB_el9nej0Vtet1HaFVKDLHid_h1noaszAVvKRmQ97x-CbYW83i0_E/s1700-e365/phish.jpg)

In the campaign detected by Huntress, the authentication abuse originates from a small cluster of Railway.com IP addresses, with three of them accounting for roughly 84% of observed events -

* 162.220.234[.]41
* 162.220.234[.]66
* 162.220.232[.]57
* 162.220.232[.]99
* 162.220.232[.]235

The starting point of the attack is a phishing email that wraps malicious URLs within legitimate [security vendor redirect services](https://www.levelblue.com/blogs/spiderlabs-blog/weaponizing-safe-links-abuse-of-multi-layered-url-rewriting-in-phishing-attacks) from Cisco, Trend Micro, and Mimecast so as to bypass spam filters and trigger a multi-hop redirect chain featuring a combination of compromised sites, Cloudflare Workers, and Vercel as intermediaries before taking the victim to the final destination.

"The observed landing sites prompt the victim to proceed to the legitimate Microsoft device code authentication endpoint and input a provided code in order to read some files," Huntress said. "The code is rendered directly on the page when the victim arrives."

"This is an interesting iteration of the tactic, as, normally, the adversary must produce and then provide the code to the victim. By rendering the code directly on the page, likely by some code generation automation, the victim is immediately provided with the code and pretext for the attack."

The landing page also comes with a "Continue to Microsoft" that, when clicked, spews a pop-up window rendering the legitimate Microsoft authentication endpoint ("microsoft[.]com/devicelogin").

[![Cybersecurit...