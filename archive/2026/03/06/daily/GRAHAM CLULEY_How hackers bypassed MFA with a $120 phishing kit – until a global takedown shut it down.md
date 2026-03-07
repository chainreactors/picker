---
title: How hackers bypassed MFA with a $120 phishing kit – until a global takedown shut it down
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/hackers-bypassed-mfa-120-phishing-kit-global-takedown-shut-down
source: GRAHAM CLULEY
date: 2026-03-06
fetch_date: 2026-03-07T03:57:09.706641
---

# How hackers bypassed MFA with a $120 phishing kit – until a global takedown shut it down

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

3 min read

# How hackers bypassed MFA with a $120 phishing kit - until a global takedown shut it down

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

March 06, 2026

  ![How hackers bypassed MFA with a $120 phishing kit - until a global takedown shut it down](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/03/tycoon-seized.jpeg "How hackers bypassed MFA with a $120 phishing kit - until a global takedown shut it down")

In a co-ordinated public-private operation between law enforcement agencies and cybersecurity industry partners one of the world's most prolific phishing-as-a-service platforms has been dismantled.

First appearing in August 2023, Tycoon 2FA was designed specifically to help fraudsters hack into accounts defended by multi-factor authentication and steal session cookies, and was responsible for tens of millions of fraudulent emails and almost tens of thousands of confirmed victims around the world.

What many computer users do not realise is that although enabling multi-factor authentication (MFA) on their Microsoft 365 or Gmail accounts is recommended and hardens their security against hackers, it does not make it impossible for them to be breached.

Tycoon 2FA's key trick was how it could bypass MFA by sitting between the victim and the legitimate service. A fake website that looked identical to the real one doesn't just collect a victim's login credentials - it immediately forwards them to the real site in real time, acting as a transparent proxy. When the victim enters their one-time-password on the fake site, it is forwarded to the real site before it expires, and the attack gains a fully-authenticated session.

For a starting price of roughly US $120 per month, Tycoon 2FA's customers gained access via private Telegram channels to an off-the-shelf phishing kit, allowing even those with limited technical expertise to run sophisticated account-takeover campaigns at scale.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2026/03/tycoon-login.jpeg)

By mid-2025, Tycoon 2FA is said to have accounted for approximately 62% of all phishing attempts blocked by Microsoft, including more than 30 million emails in a single month.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2026/03/phishing-email.jpeg)

According to reports, healthcare and education organisations were hit hard with more than 100 members of threat-sharing group Health-ISAC were targeted. In New York alone, at least two hospitals, six municipal schools, and three universities faced attempted or successful compromised — causing disruption and delays to patient care and operations.

Acting under a US. court order, Microsoft [seized](https://blogs.microsoft.com/on-the-issues/2026/03/04/how-a-global-coalition-disrupted-tycoon/) 330 active domains powering Tycoon 2FA's core infrastructure. Meanwhile, law enforcement authorities in Latvia, Lithuania, Portugal, Poland, Spain, and the UK also [seized](https://www.europol.europa.eu/media-press/newsroom/news/global-phishing-service-platform-taken-down-in-coordinated-public-private-action) infrastructure used by the criminal operation.

Tech firm Cloudflare went further, [announcing](https://www.cloudflare.com/en-gb/threat-intelligence/research/report/tycoon-2fa-takedown/) that it has banned thousands of domains and Workers projects, suspended related accounts, and erased all associated Workers scripts — blocking the kit's proxy functionality at the edge. For domains that could not be legally seized as local law enforcement agencies were non-cooperative, Cloudflare deployed warning pages to block victims attempting to access phishing links.

Obviously it's a good thing that one of the most dangerous phishing platforms in existence has been taken offline. But it must be remembered that the cybercrime industry abhors a vacuum, and chances are that other criminal operators are likely to fill the void quickly.

One lesson to learn is that not all MFA is created equal. We have in the past encouraged users to not rely upon SMS-based multi-factor authentication because of the problem of SIM-swapping attackers where fraudsters divert login codes to phones under their own control. Tycoon-style proxy attacks, meanwhile, are much more difficult for fraudsters to successfully pull off if users have protected their accounts with hardware security keys or passkeys.

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