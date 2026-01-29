---
title: Beware! Fake ChatGPT browser extensions are stealing your login credentials
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/beware-fake-chatgpt-browser-extensions-are-stealing-your-login-credentials
source: GRAHAM CLULEY
date: 2026-01-28
fetch_date: 2026-01-29T04:06:01.044859
---

# Beware! Fake ChatGPT browser extensions are stealing your login credentials

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

2 min read

# Beware! Fake ChatGPT browser extensions are stealing your login credentials

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

January 28, 2026

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![Beware! Fake ChatGPT browser extensions are stealing your login credentials](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/01/chatgpt-extension.jpeg "Beware! Fake ChatGPT browser extensions are stealing your login credentials")

If you've installed a browser extension to enhance your ChatGPT experience, you might want to think again.

Security researchers have uncovered at least 16 malicious Chrome extensions masquerading as handy ChatGPT productivity tools. Their real purpose? To steal your account credentials and hijack your sessions.

The extensions, which at the time of writing remain available on the Chrome Web Store, promise helpful features like folder organisation, voice downloads, prompt management, and chat history search.

However, in reality they are quietly stealing users' authentication tokens and sending them to a remote server controlled by the attackers.

According to researchers at LayerX who [discovered the campaign](https://layerxsecurity.com/blog/how-we-discovered-a-campaign-of-16-malicious-extensions-chatgpt/), all of the malicious extensions appear to be the work of one person or group, using multiple identities in an attempt to distribute them as widely as possible.

The offending extensions do not deploy traditional malware or attempt to exploit flaws in ChatGPT itself. Instead, they hook into the Chrome browser, and intercept outgoing data that contains users' authentication details.

That means that if you are logged into ChatGPT and the extension detects a request which contains an authorisation header, it will extract your session token and send it to the attackers. A cybercriminal with that token can effectively pose as you - accessing your entire ChatGPT chat history, any connected services like Slack or GitHub, and any potentially sensitive information you have shared with the AI.

The good news is that the malware campaign has not yet gained massive traction. Researchers say that at the time of discovery, the Google Chrome web store indicated a mere 900 downloads acros the 16 malicious extensions.

However, that could - of course - change very quickly if one or more of the extensions suddenly became popular.

So, what should you do if you use Google Chrome and ChatGPT?

My advice is to check if you have installed any ChatGPT-related browser extensions recently, and remove any that you have concerns over.

The security researchers who uncovered the malware campaign have listed the names of the extensions that have been identified so far (although, of course, it is possible that more have been used - or could still be):

* ChatGPT folder, voice download, prompt manager - ChatGPT Mods
* ChatGPT voice download, TTS download - ChatGPT Mods
* ChatGPT pin chat, bookmark - ChatGPT Mods
* ChatGPT message navigator, history scroller - ChatGPT Mods
* ChatGPT model switch - ChatGPT Mods
* ChatGPT export - ChatGPT Mods
* ChatGPT Timestamp Display - ChatGPT Mods
* ChatGPT bulk delete, Chat manager - ChatGPT Mods
* ChatGPT search history - ChatGPT Mods
* ChatGPT prompt optimization - ChatGPT Mods
* Collapsed message - ChatGPT Mods
* Multi-Profile Management & Switching - ChatGPT Mods
* Search with ChatGPT - ChatGPT Mods
* ChatGPT Token counter - ChatGPT Mods
* ChatGPT Prompt Manager, Folder, Library, Auto Send - ChatGPT Mods

If you spot any of these extensions are being used by your browser, remove them immediately. You would also probably be wise to change your OpenAI password for good measure, and review your computer security.

In general it is important to be cautious about browser extensions - and in particular those which offer to enhance AI services. The rapid adoption of AI tools makes them an increasingly attractive target for cybercriminals.

Before installing any extension, check the publisher's reputation, read reviews, and ask yourself whether you really need yet another add-on cluttering up your browser.

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

[![Streaming Subscription Scams: What Users Need to Know](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/12/51ae8402-f997-41c2-8867-1c932eaada64.png "Streaming Subscription Scams: What Users Need to Know")](/en-us/blog/hotforsecurity/streaming-subscription-scams-dark-net "Streaming Subscription Scams: What Users Need to Know")

[Scam](/en-us/blog/hotforsecurity/tag/scam "Scam")

[### Streaming Subscription Scams: What Users Need to Know](/en-us/blog/hotforsecurity/streaming-subscription-scams-dark-net "Streaming Subscription Scams: What Users Need to Know")

December 18, 2025

3 min read

[![How Do You Manage Your Passwords? We Ask Netizens](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/12/header-1.jpg "How Do You Manage Your Passwords? We Ask Netizens")](/en-us/blog/hotforsecurity/how-to-manage-passwords-we-ask-netizens-survey "How Do You Manage Your Passwords? We Ask Netizens")

[Tips and Tricks](/en-us/blog/hotforsecurity/tag/tips-and-tricks "Tips and Tricks")[How to](/en-us/blog/hotforsecurity/tag/how-to "How to")

[### How Do You Manage Your Passwords? We Ask Netizens](/en-us/blog/hotforsecurity/how-to-manage-passwords-we-ask-netizens-survey "How Do You Manage Your Passwords? We Ask Netizens")

December 18, 2025

2 min read

[![Cybercriminals Use Fake Leonardo DiCaprio Film Torrent to Spread Agent Tesla Malware](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/12/90cbbfab-b875-4654-a654-df248f9c8a73.png "Cybercriminals Use Fake Leonardo DiCaprio Film Torrent to Spread Agent Tesla Malware")](/en-us/blog/hotforsecurity/fake-leonardo-dicaprio-film-torrent-agent-tesla-malware "Cybercriminals Use Fake Leonardo DiCaprio Film Torrent to Spread Agent Tesla Malware")

[Threats](/en-us/blog/hotforsecurity/tag/threats "Threats")

[### Cybercriminals Use Fake Leonardo DiCaprio Film Torrent to Spread Agent Tesla Malware](/en-us/blog/hotforsecurity/fake-leonardo-dicaprio-film-torrent-agent-tesla-malware "Cybercriminals Use Fake Leonardo DiCaprio Film Torrent to Spread Agent Tesla Malware")

December 11, 2025

2 min read

[![What Scares You Most About AI? We Ask Netizens](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/12/header.png "What Scares You Most About AI? We Ask Netizens")](/en-us/blog/hotforsecurity/what-scares-you-most-about-ai-we-ask-netizens "What Scares You Most About AI? We Ask Netizens")

[Scam](/en-us/blog/hotforsecurity/tag/scam "Scam")[Tips and Tricks](/en-us...