---
title: Experts Flag Security, Privacy Risks in DeepSeek AI App
url: https://krebsonsecurity.com/2025/02/experts-flag-security-privacy-risks-in-deepseek-ai-app/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-07
fetch_date: 2025-10-06T20:38:23.814314
---

# Experts Flag Security, Privacy Risks in DeepSeek AI App

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Experts Flag Security, Privacy Risks in DeepSeek AI App

February 6, 2025

[35 Comments](https://krebsonsecurity.com/2025/02/experts-flag-security-privacy-risks-in-deepseek-ai-app/#comments)

New mobile apps from the Chinese artificial intelligence (AI) company **DeepSeek** have remained among the top three “free” downloads for Apple and Google devices since their debut on Jan. 25, 2025. But experts caution that many of DeepSeek’s design choices — such as using hard-coded encryption keys, and sending unencrypted user and device data to Chinese companies — introduce a number of glaring security and privacy risks.

![](https://krebsonsecurity.com/wp-content/uploads/2025/02/deepseek.png)

Public interest in the DeepSeek AI chat apps swelled following widespread [media](https://www.nytimes.com/2025/01/27/business/us-stock-market-deepseek-ai-sp500-nvidia.html) reports that the upstart Chinese AI firm had managed to match the abilities of cutting-edge chatbots while using a fraction of the specialized computer chips that leading AI companies rely on. As of this writing, DeepSeek is the third most-downloaded “free” app on the Apple store, and #1 on Google Play.

DeepSeek’s rapid rise caught the attention of the mobile security firm **NowSecure**, a Chicago-based company that helps clients screen mobile apps for security and privacy threats. In [a teardown](https://www.nowsecure.com/blog/2025/02/06/nowsecure-uncovers-multiple-security-and-privacy-flaws-in-deepseek-ios-mobile-app/) of the DeepSeek app published today, NowSecure urged organizations to remove the DeepSeek iOS mobile app from their environments, citing security concerns.

NowSecure founder **Andrew Hoog** said they haven’t yet concluded an in-depth analysis of the DeepSeek app for **Android** devices, but that there is little reason to believe its basic design would be functionally much different.

Hoog told KrebsOnSecurity there were a number of qualities about the DeepSeek iOS app that suggest the presence of deep-seated security and privacy risks. For starters, he said, the app collects an awful lot of data about the user’s device.

“They are doing some very interesting things that are on the edge of advanced device fingerprinting,” Hoog said, noting that one property of the app tracks the device’s name — which for many iOS devices defaults to the customer’s name followed by the type of iOS device.

The device information shared, combined with the user’s Internet address and [data gathered from mobile advertising companies](https://krebsonsecurity.com/2024/10/the-global-surveillance-free-for-all-in-mobile-ad-data/), could be used to deanonymize users of the DeepSeek iOS app, NowSecure warned. The report notes that DeepSeek communicates with **Volcengine**, a cloud platform developed by **ByteDance** (the makers of **TikTok**), although NowSecure said it wasn’t clear if the data is just leveraging ByteDance’s digital transformation cloud service or if the declared information share extends further between the two companies.

[![](https://krebsonsecurity.com/wp-content/uploads/2025/02/deepseek-graphic.png)](https://krebsonsecurity.com/wp-content/uploads/2025/02/deepseek-graphic.png)

Image: NowSecure.

Perhaps more concerning, NowSecure said the iOS app transmits device information “in the clear,” without any encryption to encapsulate the data. This means the data being handled by the app could be intercepted, read, and even modified by anyone who has access to any of the networks that carry the app’s traffic.

“The DeepSeek iOS app globally disables App Transport Security (ATS) which is an iOS platform level protection that prevents sensitive data from being sent over unencrypted channels,” the report observed. “Since this protection is disabled, the app can (and does) send unencrypted data over the internet.”

Hoog said the app does selectively encrypt portions of the responses coming from DeepSeek servers. But they also found it uses an insecure and now deprecated encryption algorithm called 3DES (aka [Triple DES](https://en.wikipedia.org/wiki/Triple_DES)), and that the developers had hard-coded the encryption key. That means the cryptographic key needed to decipher those data fields can be extracted from the app itself.

There were other, less alarming security and privacy issues highlighted in the report, but Hoog said he’s confident there are additional, unseen security concerns lurking within the app’s code.

“When we see people exhibit really simplistic coding errors, as you dig deeper there are usually a lot more issues,” Hoog said. “There is virtually no priority around security or privacy. Whether cultural, or mandated by China, or a witting choice, taken together they point to significant lapse in security and privacy controls, and that puts companies at risk.”

Apparently, plenty of others share this view. *Axios* [reported](https://www.axios.com/2025/01/30/house-congress-bans-deepseek-ai) on January 30 that U.S. congressional offices are being warned not to use the app.

“[T]hreat actors are already exploiting DeepSeek to deliver malicious software and infect devices,” read the notice from the chief administrative officer for the House of Representatives. “To mitigate these risks, the House has taken security measures to restrict DeepSeek’s functionality on all House-issued devices.”

*TechCrunch* [reports](https://techcrunch.com/2025/02/03/deepseek-the-countries-and-agencies-that-have-banned-the-ai-companys-tech/) that Italy and Taiwan have already moved to ban DeepSeek over security concerns. *Bloomberg* [writes](https://www.bloomberg.com/news/articles/2025-01-30/pentagon-workers-used-deepseek-s-chatbot-for-days-before-block) that **The Pentagon** has blocked access to DeepSeek. *CNBC* [says](https://www.cnbc.com/2025/01/31/nasa-becomes-latest-federal-agency-to-block-chinas-deepseek.html) **NASA** also banned employees from using the service, as did the **U.S. Navy**.

Beyond security concerns tied to the DeepSeek iOS app, there are indications the Chinese AI company may be playing fast and loose with the data that it collects from and about users. On January 29, researchers at **Wiz** [said](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) they discovered a publicly accessible database linked to DeepSeek that exposed “a significant volume of chat history, backend data and sensitive information, including log streams, API secrets, and operational details.”

“More critically, the exposure allowed for full database control and potential privilege escalation within the DeepSeek environment, without any authentication or defense mechanism to the outside world,” Wiz wrote. [Full disclosure: Wiz is currently an advertiser on this website.]

KrebsOnSecurity sought comment on the report from DeepSeek and from Apple. This story will be updated with any substantive replies.

*This entry was posted on Thursday 6th of February 2025 04:12 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Andrew Hoog](https://krebsons...