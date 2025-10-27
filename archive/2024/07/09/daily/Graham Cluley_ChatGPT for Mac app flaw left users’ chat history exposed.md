---
title: ChatGPT for Mac app flaw left users’ chat history exposed
url: https://www.bitdefender.com/blog/hotforsecurity/chatgpt-mac-app-flaw-left-users-history-exposed/
source: Graham Cluley
date: 2024-07-09
fetch_date: 2025-10-06T17:47:48.484481
---

# ChatGPT for Mac app flaw left users’ chat history exposed

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

min read

# ChatGPT for Mac app flaw left users' chat history exposed

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

July 08, 2024

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![ChatGPT for Mac app flaw left users' chat history exposed](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2024/07/chatgpt-mac.jpeg "ChatGPT for Mac app flaw left users' chat history exposed")

Is it only a few weeks since OpenAI announced its new app for macOS computers?

To much fanfare, the makers of ChatGPT revealed a desktop version that allowed Mac users to ask questions directly rather than via the web.

"ChatGPT seamlessly integrates with how you work, write, and create," bragged OpenAI.

What could possibly go wrong?

Well, anyone rushing to try out the software may have be rueing their impatience, because - as software engineer Pedro José Pereira Vieito [posted on Threads](https://www.threads.net/%40pvieito/post/C85NVV6hvF6?xmt=AQGz0o3JtBOwk1nfUgk8lvxQoIV8E92xz1vK1IP8VC6zhA) - OpenAI's ever-so-clever ChatGPT's software was doing something really-rather-stupid.

It was storing users' chats with ChatGPT for Mac in plaintext on their computer. In short, anyone who gained unauthorised use of your computer - whether it be a malicious remote hacker, a jealous partner, or rival in the office, would be able to easily read your conversations with ChatGPT and the data associated with them.

As Pereira Vieito described, OpenAI's app was not sandboxed, and stored all conversations, *unencrypted* in a folder accessible by any other running processes (including malware) on the computer.

"macOS has blocked access to any user private data since macOS Mojave 10.14 (6 years ago!). Any app accessing private user data (Calendar, Contacts, Mail, Photos, any third-party app sandbox, etc.) now requires explicit user access," explained Pereira Vieito. "OpenAI chose to opt-out of the sandbox and store the conversations in plain text in a non-protected location, disabling all of these built-in defenses."

Thankfully, the security goof has now been fixed.  *The Verge* [reports](https://www.theverge.com/2024/7/3/24191636/openai-chatgpt-mac-app-conversations-plain-text) that after it contacted OpenAI about the issue raised by Pereira Vieito, a new version of the ChatGPT macOS app was shipped, properly encrypting conversations.

But the incident acts as a salutary reminder.  Right now there is a "gold rush" mentality when it comes to artificial intelligence.  Firms are racing ahead with their AI developments, desperate to stay ahead of their competitors.  Inevitably that can lead to less care being taken with security and privacy as shortcuts are taken to push out developments at an ever-faster speed.

My advice to users is not to make the mistake of jumping onto every new development on the day of release. Let others be the first to investigate new AI features and developments. They can be the beta testers who try out AI software when it's most likely to contain bugs and vulnerabilities, and only when you are confident that the creases have been ironed out try it for yourself.

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

[### How to Protect Your WhatsApp from Hackers and Scammers – 8 Key Settings and Best Practices](/en-us/blog/hotforsecurity/how-to-protect-whatsapp-hackers-scammers-8-key-settings "How to Protect Your WhatsApp from Hackers and Scammers – 8 Key Settings and...