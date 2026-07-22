---
title: Ukraine warns fake CAPTCHAs are being used to make you hack yourself
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/ukraine-fake-captchas-hack-yourself
source: GRAHAM CLULEY
date: 2026-07-21
fetch_date: 2026-07-22T05:04:28.830507
---

# Ukraine warns fake CAPTCHAs are being used to make you hack yourself

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

2 min read

# Ukraine warns fake CAPTCHAs are being used to make you hack yourself

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

July 21, 2026

  ![Ukraine warns fake CAPTCHAs are being used to make you hack yourself](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/07/clickfix.jpeg "Ukraine warns fake CAPTCHAs are being used to make you hack yourself")

Ukraine's computer emergency response team, CERT-UA, has [warned](https://cert.gov.ua/article/6318437) that Russian hackers are using fake CAPTCHA checks to trick people into compromising their own PCs.

The Kremlin-backed Sandworm hacking group is [reportedly](https://therecord.media/ukraine-sandworm-hacks-captcha-powershell) leveraging fake CAPTCHA checks on compromised websites that persuade users to execute a PowerShell command on their computers - tricking them into running malicious code.

CERT-UA has attributed the attacks, which have surged this spring and summer against Ukrainian targets, to UAC-0145 - a branch of Sandworm, the hacking unit known for some of Russia's most destructive cyber attacks in the past 10+ years, including ones against Ukraine's power grid.

The latest attacks begin when a user visits a compromised webpage, where they're greeted by a fake CAPTCHA claiming they need to complete an extra step to prove that they are human.

But unlike normal CAPTCHAs it is not about picking out the traffic lights or ticking a box. Instead, the fake CAPTCHA instructs the user to copy and paste a PowerShell command into their Windows computer.

Of course, it's not worded quite like that.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2026/07/clickfix-captcha.jpeg)

The instructions tell the user to press a key sequence that opens the Windows Run dialog, pastes the contents of the clipboard, and hits Enter — all without the victim realising what they have just unleashed.

Because what they've just executed could:

* download malware
* run PowerShell scripts
* or install remote access software on their machine

A genuine CAPTCHA will never ask you to:

* press Windows + R
* open the Run dialog
* paste a command
* or press Enter to "verify you are human."

The downloaded code run on targeted computers runs a reconnaissance tool called ScoutCurl that collects information about the infected computer. This includes details about how the system is set up, what software is installed, files that are present, and browser data - all of which helps attackers determine whether the target is worth compromising further.

At least ten websites are estimated to have been compromised as part of the campaign since the beginning of June.

ClickFix attacks like this are not new, and we have written about the threat [many](https://www.bitdefender.com/en-gb/blog/businessinsights/how-clickfix-cyberattack-technique-works) [times](https://www.bitdefender.com/en-gb/blog/hotforsecurity/tiktok-free-photoshop-scam) in [past](https://www.bitdefender.com/en-gb/blog/hotforsecurity/supply-chain-captcha-attack-hits-over-100-car-dealerships) [articles](https://www.bitdefender.com/en-gb/blog/hotforsecurity/clickfix-victims-help-hackers).

The uncomfortable truth is that ClickFix attacks persist because cybercriminals have found that they are very effective. This is in part because they do not rely on users being tricked into clicking on malicious links, but instead guide the victim through the process of infecting their own computers.

Furthermore, the instructions are presented as "helpful" technical advice to resolve an issue, and can too easily be trusted by the unwary. Furthermore, they exploit the fact the widespread installation of legitimate tools like PowerShell which are trusted in many corporate environments.

ClickFix attacks are not just a problem for the people of Ukraine, already navigating a relentless barrage of cyberattacks from Russian hackers amid a long-lasting kinetic war. They are a problem for computer users worldwide.

As a result, all computer users should take Ukraine's warning about the rise in ClickFix attacks as a timely reminder that the most dangerous threats often do not arrive in the form of an exploit of a zero-day vulnerability.

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