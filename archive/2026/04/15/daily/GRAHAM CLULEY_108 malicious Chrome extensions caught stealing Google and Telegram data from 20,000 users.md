---
title: 108 malicious Chrome extensions caught stealing Google and Telegram data from 20,000 users
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/malicious-chrome-extensions-steal-google-telegram-data
source: GRAHAM CLULEY
date: 2026-04-15
fetch_date: 2026-04-16T04:54:27.537727
---

# 108 malicious Chrome extensions caught stealing Google and Telegram data from 20,000 users

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

2 min read

# 108 malicious Chrome extensions caught stealing Google and Telegram data from 20,000 users

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

April 15, 2026

  ![108 malicious Chrome extensions caught stealing Google and Telegram data from 20,000 users](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/04/extensions.jpeg "108 malicious Chrome extensions caught stealing Google and Telegram data from 20,000 users")

Cybersecurity researchers have revealed that 108 malicious Google Chrome extensions have been quietly stealing user credentials, hijacking Telegram sessions, and injecting unwanted ads and scripts into browsers - all reporting back to the same central point.

The [discovery](https://socket.dev/blog/108-chrome-ext-linked-to-data-exfil-session-theft-shared-c2) by researchers at Socket, found that all 108 extensions were communicating with a single command-and-control server, strongly suggesting they are the work of one group of hackers.

Between them, before being identified, the extensions had racked up approximately 20,000 installs from the Chrome Web Store.

The malicious add-ons were published under five different publisher identities (Yana Project, GameGen, SideGames, Rodeo Games, and InterAlt) in an apparent attempt to avoid detection.

And to further disguise the reality of what was going on, each malicious Google Chrome extension adopted differing disguises - including posing as a Telegram sidebar client, slot machine games, tools to enhance YouTube and TikTok, or translation tools.

Behind the scenes, according to researchers, all 108 extensions were transferring stolen credentials, user identities, and browsing data to remote servers under the control of the hackers.

Specific malicious behaviours included:

* 54 extensions that stole Google account details - including email addresses, full names, profile pictures, and Google account IDs
* 45 extensions that contained a backdoor which could open arbitrary URLs upon browser startup
* Privacy-busting extensions that exfiltrated Telegram Web sessions every 15 seconds, and in some cases even replacing the victim's active session with of the hackers' choosing
* Extensions that stripped security headers from YouTube and TikTok, and injected gambling ads.

Although the identity of those behind the campaign remains unknown, it is perhaps telling that Russian-language comments were found in the source code of several of the add-ons.

If you're a regular reader of *Hot for Security* then you will know that browser extension security has been a significant problem over the years.

Back in 2018, for instance, the Mega.nz Chrome extension was [compromised via a malicious update](https://grahamcluley.com/rogue-browser-extension/), leading to the scooping-up of login credentials and cryptocurrency private keys belonging to silently harvesting login credentials and cryptocurrency private keys from web surfers.

In 2020, researchers found [49 browser extensions targeting cryptocurrency wallets](https://www.bitdefender.com/en-us/blog/hotforsecurity/49-crypto-wallet-pickpocketing-browser-extensions-booted-from-the-chrome-web-store), which had been promoted via Google Ads and lauded with fake five-star reviews to appear trustworthy.

More recently, in 2023, a rogue "ChatGPT for Google" extension [stole Facebook session cookies from over 9,000 users](https://www.bitdefender.com/en-us/blog/hotforsecurity/crooks-spread-rogue-chatgpt-chrome-extension-to-hijack-facebook-accounts), and used them to spread malvertising.

And just this January, [16 more fake ChatGPT-themed extensions](https://www.bitdefender.com/en-us/blog/hotforsecurity/beware-fake-chatgpt-browser-extensions-are-stealing-your-login-credentials) were found to be stealing authentication tokens.

Arguably the most alarming incident of all though occurred at Christmas in 2024, when a phishing email tricked a worker into granting a malicious app access to Cyberhaven's Chrome Web Store account. That allowed attackers to [push a poisoned update to hundreds of thousands of users](https://arstechnica.com/security/2025/01/dozens-of-backdoored-chrome-extensions-discovered-on-2-6-million-devices/). That attack was believed to be part of a broader campaign that compromised over 35 extensions and affected an estimated 2.6 million people.

If you have installed any of the 108 extensions identified in this latest malicious campaign, your best course of action is to remove them immediately.

Furthermore, anyone who installed a dodgy Telegram-related extension should also log out of all Telegram Web sessions via the Telegram mobile app, as attackers may have already hijacked them.

More generally, don't you think it's high time you did a spring clean of your Chrome extensions? Do you actually use each one? Do the permissions they request seem proportionate for what they do? If in doubt, remove it.

After all, a lean browser with less extensions is inevitably a safer browser.

tags

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

---

### Author

---

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=150&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[## Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s.

[View all posts](/en-us/blog/hotforsecurity/author/gcluley)

---

## You might also like

#### Bookmarks

---

![loader](https://download.bitdefender.com/resources/themes/draco/images/lite_v2/blog-images/loader-white.svg "loader")

[Legal Information](https://www.bitdefender.com/site/view/legal-terms.html "Legal Information") | [Privacy Policy](https://www.bitdefender.com/site/view/legal-privacy-policy-for-bitdefender-websites.html "Privacy Policy") | [Contact Us](https://www.bitdefender.com/site/Main/contact/1 "Contact Us")

Copyright © 1997 - 2026 Bitdefender.