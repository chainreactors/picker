---
title: aCropalypse now! Cropped and redacted images suffer privacy fail on Google Pixel smartphones
url: https://www.bitdefender.com/blog/hotforsecurity/acropalypse-now-cropped-and-redacted-images-suffer-privacy-fail-on-google-pixel-smartphones/
source: Graham Cluley
date: 2023-03-23
fetch_date: 2025-10-04T10:25:27.030942
---

# aCropalypse now! Cropped and redacted images suffer privacy fail on Google Pixel smartphones

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

min read

# aCropalypse now! Cropped and redacted images suffer privacy fail on Google Pixel smartphones

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

March 22, 2023

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![aCropalypse now! Cropped and redacted images suffer privacy fail on Google Pixel smartphones](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2023/03/acropalypse.jpeg "aCropalypse now! Cropped and redacted images suffer privacy fail on Google Pixel smartphones")

Have you ever shared a photograph where you've redacted some sensitive information?

Perhaps you've cropped out part of the image you didn't want others to see?

Well, users of Google's Pixel Android smartphone might be alarmed to learn that pictures they've shared in the past may have been less discreet than they imagined.

Security experts Simon Aarons and David Buchanan have revealed that the Markup editing app included on Pixel smartphones to allow users to crop, add text, and draw on images has a serious vulnerability that puts their privacy at risk.

You might imagine that you have placed an opaque black bar over your address or a credit card number in an image, blurred out part of your anatomy, or simply cropped out of the image something that you would rather remain private... but the so-called "aCropalypse" flaw means that edited screenshots were only overwriting the start of PNG files, but not truncating them.

In short, all screenshots edited by Markup from Pixel phones that have been shared for the past five-or-so years might have additional image data recoverable from them.

Researcher Simon Aarons [posted an example on Twitter](http://twitter.com/ItsSimonTime/status/1636857478263750656) of how the technique was used to restore a photo of credit card uploaded to a Discord channel, whose number was originally redacted using the black marker feature of the Markup tool.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2023/03/acropalyse-example.jpeg)

Clearly this is a serious problem.

In the past, we've explained the problem of how weak redaction (by blurring or pixelating text) may be insufficient to keep sensitive information secure, and how [tools have been created](https://www.bitdefender.com/blog/hotforsecurity/stop-pixelating-new-tool-reveals-the-secrets-of-redacted-documents/) which can effectively "undo" the redaction to reveal secrets.

For that reason, I've previously recommended that you shouldn't really blur or "swirl" text if you want to hide part of an image - replace the section of the picture with randomly generated noise, or covering the text with an opaque black bar works better.

But the aCropalypse flaw means that sensitive details can still be exposed if you go to that effort.

The flaw in Google Pixel's Markup tool has made the seemingly impossible to be possible.  And to prove their point, the researchers who found the vulnerability have created a [demo website](https://acropalypse.app/) where Pixel images can upload their past images to see what might be lurking within.

There is, thankfully, some good news.

Firstly, some social media sites perform their own processing on uploaded images (typically for compression purposes and the stripping of meta data) and this may remove the extraneous information that the creator of the image never imagined was still included.

Furthermore, Google has reportedly fixed the Markup app in its [latest Pixel security update](https://source.android.com/docs/security/bulletin/pixel/2023-03-01).

But, and it's a big but, this does nothing to *unshare* vulnerable screenshots created and distributed in the last five years. Quite how Google plans to help with that problems remains something of a mystery...

Oh, and before Windows users start to feel a little too smug about the misfortune of their Android-using friends, researcher David Buchanan has [just warned](https://twitter.com/David3141593/status/1638222624084951040) that the Snipping Tool and Snip & Sketch cropping tool in Windows 11 and Windows 10 respectively also leak image data in a similar fashion to how aCropalypse occurs on Pixel phones.

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

[### Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](/en-us/blog/hotforsecurity/scammers-sell-steam-...