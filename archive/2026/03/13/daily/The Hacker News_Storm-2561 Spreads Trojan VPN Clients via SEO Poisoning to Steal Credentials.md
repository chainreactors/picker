---
title: Storm-2561 Spreads Trojan VPN Clients via SEO Poisoning to Steal Credentials
url: https://thehackernews.com/2026/03/storm-2561-spreads-trojan-vpn-clients.html
source: The Hacker News
date: 2026-03-13
fetch_date: 2026-03-14T04:14:27.136008
---

# Storm-2561 Spreads Trojan VPN Clients via SEO Poisoning to Steal Credentials

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

# [Storm-2561 Spreads Trojan VPN Clients via SEO Poisoning to Steal Credentials](https://thehackernews.com/2026/03/storm-2561-spreads-trojan-vpn-clients.html)

**Ravie Lakshmanan**Mar 13, 2026VPN Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIHmOuzh2pt4Kd3D5FVJ3ryojQF5XMf6q51cdyxus7nMy4suicQ1RNW3_sjRA6OgE3H-JXTOoxz9wwMqEZQbJb9SXS7DOYTVUBK1MszgQoAR6rGGTgunHDAKM7NfOTkK-W2U9_5rT0Un6xn-cwMnGipbokPav0UoDL7eyQkKIrrKwa2h0BgCFqwuZe598R/s1700-e365/vpn-download.jpg)

Microsoft has disclosed details of a credential theft campaign that employs fake virtual private network (VPN) clients distributed through search engine optimization (SEO) poisoning techniques.

"The campaign redirects users searching for legitimate enterprise software to malicious ZIP files on attacker-controlled websites to deploy digitally signed trojans that masquerade as trusted VPN clients while harvesting VPN credentials," the Microsoft Threat Intelligence and Microsoft Defender Experts teams [said](https://www.microsoft.com/en-us/security/blog/2026/03/12/storm-2561-uses-seo-poisoning-to-distribute-fake-vpn-clients-for-credential-theft/).

The Windows maker, which observed the activity in mid-January 2026, has attributed it to **Storm-2561**, a threat activity cluster known for propagating malware through SEO poisoning and impersonating popular software vendors since May 2025.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The threat actor's campaigns were [first documented](https://www.cyjax.com/resources/blog/a-sting-on-bing-bumblebee-delivered-through-bing-seo-poisoning-campaign) by Cyjax, highlighting the use of SEO poisoning to redirect users searching for software programs from companies like SonicWall, Hanwha Vision, and Pulse Secure (now Ivanti Secure Access) on Bing to fake sites and trick them into downloading MSI installers that deploy the [Bumblebee loader](https://thehackernews.com/2022/04/cybercriminals-using-new-malware-loader.html).

A subsequent iteration of the attack was [disclosed](https://thehackernews.com/2025/10/weekly-recap-f5-breached-linux-rootkits.html#:~:text=SEO%20Campaign%20Uses%20Fake%20Ivanti%20Installers%20to%20Steal%20Credentials) by Zscaler in October 2025. The campaign was observed taking advantage of users searching for legitimate software on Bing to propagate a trojanized Ivanti Pulse Secure VPN client via bogus websites ("ivanti-vpn[.]org") that ultimately stole VPN credentials from the victim's machine.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEKes-WCkV0lnkhG_Aue7xnrFicdmAsQDu3TNLJIMvgBIR3ewSJKlqj_Uw-kdzkaptZAe4tfbOLOBZMOH0VoDOk10AonXsGRn0oekUw-dhAUYhaFNzE_R_GpX7QMxSiSPfu_6a9FLh09h0bPsrnXfZ800h5gU3BCqPQ1XWkxFHqwOfgQdIyxNWTHMsnhmP/s1700-e365/fort.jpg)

Microsoft said the activity highlights how threat actors exploit trust in search engine rankings and software branding as a social engineering tactic to steal data from users looking for enterprise VPN software. Compounding matters is the abuse of trusted platforms like GitHub to host the installer files.

Specifically, the GitHub repository hosts a ZIP file containing an MSI installer file that masquerades as legitimate VPN software, but sideloads malicious DLL files during installation. The end goal, as before, is to collect and exfiltrate VPN credentials using a variant of an information stealer called Hyrax.

A fake, yet convincing, VPN sign-in dialog is displayed to the user to capture the credentials. Once the information is entered by the victim, they are displayed an error message and are instructed to download the legitimate VPN client this time. In some cases, they are redirected to the legitimate VPN website.

The malware makes use of the [Windows RunOnce registry key](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys) to set up persistence, so that it's executed automatically every time following a system reboot.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

"This campaign exhibits characteristics consistent with financially motivated cybercrime operations employed by Storm-2561," Microsoft said. "The malicious components are digitally signed by 'Taiyuan Lihua Near Information Technology Co., Ltd.'"

The tech giant has since taken down the attacker-controlled GitHub repositories and revoked the legitimate certificate to neutralize the operation.

To counter such threats, organizations and users are advised to implement multi-factor authentication (MFA) on all accounts, exercise caution when downloading software from websites, and make sure that they are authentic.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Information Stealer](https://thehackernews.com/search/label/Information%20Stealer), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Phishing](https://thehackernews.com/search/label/Phishing), [SEO poisoning](https://thehackernews.c...