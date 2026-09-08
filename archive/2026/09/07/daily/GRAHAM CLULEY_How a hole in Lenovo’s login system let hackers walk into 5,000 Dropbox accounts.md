---
title: How a hole in Lenovo’s login system let hackers walk into 5,000 Dropbox accounts
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/lenovo-login-system-hackers-dropbox
source: GRAHAM CLULEY
date: 2026-09-07
fetch_date: 2026-09-08T06:42:33.918141
---

# How a hole in Lenovo’s login system let hackers walk into 5,000 Dropbox accounts

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

2 min read

# How a hole in Lenovo's login system let hackers walk into 5,000 Dropbox accounts

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

September 07, 2026

  ![How a hole in Lenovo's login system let hackers walk into 5,000 Dropbox accounts](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/09/dropbox-lenovo.jpeg "How a hole in Lenovo's login system let hackers walk into 5,000 Dropbox accounts")

If you ever linked your Dropbox account to a Lenovo ID - perhaps to make life easier when logging in via a Lenovo laptop - you might want to take heed.

Dropbox has confirmed that approximately 5,000 customer accounts were [accessed](https://www.theregister.com/security/2026/09/02/legacy-lenovo-login-opens-5000-dropbox-accounts-to-attackers/5293924) between 4-21 August, after hackers exploited a legacy login integration between Dropbox and Lenovo's own identity system, Lenovo ID.

Dropbox sent a warning to affected users about what it described as "an issue with Lenovo's email verification process," which saw attackers registering a brand new Lenovo ID with someone else's email address but never verified that the user registering the ID had ownership of the email inbox.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2026/09/dropbox-email.jpeg)

That clearly is sloppy, but what made things much worse was that due to a legacy integration between Lenovo and Dropbox, a Lenovo ID registered against your email address could then be used to log straight into your Dropbox account - no questions asked, no Dropbox password requested.

So, anyone wanting to access your Dropbox account just had to sign up for a Lenovo account using your email address.

Lenovo [told *Bleeping Computer*](https://www.bleepingcomputer.com/news/security/dropbox-accounts-breached-through-lenovo-email-verification-flaw/) that its own customers and systems were unaffected, and that "upon identifying the issue, Dropbox and Lenovo worked collaboratively to promptly mitigate the risk."

Dropbox attempted to put a good spin on things, telling [*Reuters*](https://www.reuters.com/technology/dropbox-says-about-5000-accounts-compromised-august-hack-2026-09-02/) that less than a third of affected accounts had had their files accessed in the breach.

Frankly, that would be cold comfort to me if I owned one of the Dropbox accounts that was compromised, and I would also feel disappointed that it had taken weeks to receive warning of the security breach (which was not apparently caught by monitoring at the time, but only spotted during a later investigation).

Dropbox says it has terminated all sessions authenticated through a Lenovo ID, and now requires a user's actual Dropbox password to be entered - even when signing in through Lenovo ID, which should close the loophole.

Affected users have also been told to reset their Dropbox and email passwords, and enable two-factor authentication (2FA).

Regardless of whether you have received a warning from Dropbox or not, it only takes a few minutes to enable 2FA. Don't just turn it on for your Dropbox account, enable it everywhere it is made available. It isn't a 100% solution, but it can provide a higher level of protection that will defeat many attempts to compromise accounts.

This hack of 5000 Dropbox accounts was not sophisticated. It did not rely upon advanced malware, or exploit a complex zero-day vulnerability. This was simply the case of an attacker finding a glaring loophole in the security of one company's identity system, and that it was being implicitly trusted by another's.

One can only be grateful that the problem was discovered after only 5000 Dropbox accounts were accessed. Things could have been much much worse.

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