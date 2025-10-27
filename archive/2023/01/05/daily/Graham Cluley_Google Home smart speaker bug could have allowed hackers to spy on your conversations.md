---
title: Google Home smart speaker bug could have allowed hackers to spy on your conversations
url: https://www.bitdefender.com/blog/hotforsecurity/oogle-home-smart-speaker-bug-could-have-allowed-hackers-to-spy-on-your-conversations/
source: Graham Cluley
date: 2023-01-05
fetch_date: 2025-10-04T03:06:11.680579
---

# Google Home smart speaker bug could have allowed hackers to spy on your conversations

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

min read

# Google Home smart speaker bug could have allowed hackers to spy on your conversations

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

January 04, 2023

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![Google Home smart speaker bug could have allowed hackers to spy on your conversations](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2023/01/google-home.jpeg "Google Home smart speaker bug could have allowed hackers to spy on your conversations")

A security researcher has won a $107,500 bug bounty after discovering a way in which hackers could install a backdoor on Google Home devices to seize control of their microphones, and secretly spy upon their owners' conversations.

Vulnerability hunter Matt Kunze initially reported the problem to Google in early 2021, after experiments with his own Google Home smart speaker noticed the ease with which it added new users via the Google Home app.

Kunze discovered that connected users could send commands remotely to paired Google Home devices via its cloud API.

In a [technical blog post](https://downrightnifty.me/blog/2022/12/26/hacking-google-home.html), Kunze described a possible attack scenario:

1. Attacker wishes to spy on victim. Attacker can get within wireless proximity of the Google Home (but does NOT have the victim’s Wi-Fi password).
2. Attacker discovers victim’s Google Home by listening for MAC addresses with prefixes associated with Google Inc. (e.g. `E4:F0:42`).
3. Attacker sends deauth packets to disconnect the device from its network and make it enter setup mode.
4. Attacker connects to the device’s setup network and requests its device info.
5. Attacker connects to the internet and uses the obtained device info to link their account to the victim’s device.
6. Attacker can now spy on the victim through their Google Home over the internet (no need to be within proximity of the device anymore).

According to Kunze, a malicious hacker who has successfully linked his account to the targeted Google Home device can now execute commands remotely: controlling smart switches, making purchases online, remotely unlock doors and vehicles, or opening smart locks by brute-forcing a user's PIN.

Kunze even determined that he could exploit a Google Home speaker's "call <phone number>" command, effectively transmitting everything picked up by its microphone to a phone number of the hacker's choice.

Thankfully, Kunze's responsible disclosure of the vulnerabilities to Google mean that none of the security flaws should be possible to exploit any more.  Google fixed the security holes in April 2021, although details have only been made public now.

Of course, that does mean that for some years millions of people were purchasing vulnerable Google Home smart speakers unaware that they could be putting their privacy and security in danger.

Voice-activated devices have been proven to be vulnerable to covert snooping in the past due to vulnerabilities, and it would be a brave person who bet that they won't be again.  The widespread adoption of smart speakers in both the home and office has made them a potential headache for those who prioritise their privacy and security over convenience.

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

## Right now Top posts

[![Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/06/header-1.jpg "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")](/en-us/blog/hotforsecurity/beyond-free-antivirus-5-reasons-full-strength-protection "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")[Digital Privacy](/en-us/blog/hotforsecurity/tag/digital-privacy "Digital Privacy")[Tips and Tricks](/en-us/blog/hotforsecurity/tag/tips-and-tricks "Tips and Tricks")[How to](/en-us/blog/hotforsecurity/tag/how-to "How to")

[### Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices](/en-us/blog/hotforsecurity/beyond-free-antivirus-5-reasons-full-strength-protection "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")

June 12, 2025

min read

[![Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/05/movie-theater-2093264_1920.jpg "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")](/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")

[Threats](/en-us/blog/hotforsecurity/tag/threats "Threats")

[### Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer](/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")

May 23, 2025

min read

[![Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/05/interior-design-8922413_1920--1-.jpg "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")](/en-us/blog/hotforsecurity/scammers-sell-steam-accounts-games "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")

[Scam](/en-us/blog/hotforsecurity/tag/scam "Scam")

[### Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](/en-us/blog/hotforsecurity/scammers-sell-steam-accounts-games "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")

May 16, 2025

min read

[![How to Protect Your WhatsApp from Hackers and Scammers – 8 Key Settings and Best Practices](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/04/How-to-Protect-Your-WhatsApp-from-Hackers-and-Scammers--header-.jpg "How to Protect Your WhatsApp from Hackers and Scammers – 8 Key Settings and Best Practices")](/en-us/blog/hotforsecurity/how-to-protect-whatsapp-hackers-scammers-8-key-settings "How to Protect Your WhatsApp from Hackers and Scammers – 8 Key Settings and Best Practices")

[How to](/en-us/blog/hotforsecurity/tag/how-to "How to")[Tips and Tricks](/en-us/blog/hotforsecurity/tag/tips-and-tricks "Tips and Tricks")

[### How to Protect Your WhatsApp from Hackers and Scammers – 8 Key Settings and Best Practices](/en-us/blog/hotforsecurity/how-to-protect-whatsapp-hackers-s...