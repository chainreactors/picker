---
title: How Pixel and Android are bringing a new level of trust to your images with C2PA Content Credentials
url: http://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html
source: Google Online Security Blog
date: 2025-09-11
fetch_date: 2025-10-02T19:57:25.771952
---

# How Pixel and Android are bringing a new level of trust to your images with C2PA Content Credentials

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [How Pixel and Android are bringing a new level of trust to your images with C2PA Content Credentials](https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html "How Pixel and Android are bringing a new level of trust to your images with C2PA Content Credentials")

September 10, 2025

Posted by Eric Lynch, Senior Product Manager, Android Security, and Sherif Hanna, Group Product Manager, Google C2PA Core

At Made by Google 2025, we announced that the new Google Pixel 10 phones will support C2PA [Content Credentials](contentcredentials.org) in [Pixel Camera](https://blog.google/products/pixel/pixel-10-camera-features) and [Google Photos](https://blog.google/products/photos/ai-photo-editing-google-photos). This announcement represents a series of steps towards greater digital media transparency:

* The Pixel 10 lineup is the first to have Content Credentials built inacross every photo created by Pixel Camera.
* The Pixel Camera app **[achieved Assurance Level 2](https://github.com/c2pa-org/conformance-public/blob/main/conforming-products/conforming-products-list.json)**, the highest security rating [currently defined](https://github.com/c2pa-org/conformance-public/blob/main/docs/current/C2PA%20Generator%20Product%20Security%20Requirements.pdf) by the C2PA Conformance Program. Assurance Level 2 for a mobile app is currently **only possible on the Android platform**.
* **A private-by-design** approach to C2PA certificate management, where no image or group of images can be related to one another or the person who created them.
* Pixel 10 phones support **on-device trusted time-stamps,** which ensures images captured with your native camera app can be trusted after the certificate expires, even if they were captured when your device was offline.

These capabilities are [powered by Google Tensor G5](https://blog.google/products/pixel/tensor-G5-pixel-10), Titan M2 security chip, the advanced hardware-backed security features of the Android platform, and Pixel engineering expertise.

In this post, we’ll break down our architectural blueprint for bringing a new level of trust to digital media, and how developers can apply this model to their own apps on Android.

## A New Approach to Content Credentials

Generative AI can help us all to be more creative, productive, and innovative. But it can be hard to tell the difference between content that’s been AI-generated, and content created without AI. The ability to verify the source and history—or provenance—of digital content is more important than ever.

Content Credentials convey a rich set of information about how media such as images, videos, or audio files were made, protected by the same digital signature technology that has secured online transactions and mobile apps for decades. It empowers users to identify AI-generated (or altered) content, helping to foster transparency and trust in generative AI. It can be complemented by watermarking technologies such as [SynthID](https://deepmind.google/science/synthid/).

Content Credentials are an [industry standard backed by a broad coalition of leading companies](https://c2pa.org/membership/) for securely conveying the origin and history of media files. The standard is developed by the Coalition for Content Provenance and Authenticity (C2PA), of which Google is a steering committee member.

The traditional approach to classifying digital image content has focused on categorizing content as “AI” vs. “not AI”. This has been the basis for many [legislative efforts](https://artificialintelligenceact.eu/article/50/), which have required the labeling of synthetic media. This traditional approach has drawbacks, as described in Chapter 5 of [this seminal report](http://publicpolicy.google/resources/determining_trustworthiness_en.pdf) by Google. Research shows that if only synthetic content is labeled as “AI”, then users falsely believe unlabeled content is “not AI”, a phenomenon called “the implied truth effect”. This is why Google is taking a different approach to applying C2PA Content Credentials.

Instead of categorizing digital content into a simplistic “AI” vs. “not AI”, Pixel 10 takes the first steps toward implementing our vision of categorizing digital content as either i) media that comes with verifiable proof of how it was made or ii) media that doesn't.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn37sHTBDdvDNieYBDEQwQhZi9rGDruWptlSomDIXQYpY1smY0zvs_Cu9S6h39fEFTQFNRuW2oxwUGtu8EC6nv_KyutlwMPQE4h1YWSOuOD5JU-A7iMJcRyZ9-CMet_ejzorqxvq9zBCIPG36LGW-yBcBgmTEZ23YVsirTBLAKMFF0XBgtzVL-cBCEoN5w/s1600/Blog%20image%20C2PA.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn37sHTBDdvDNieYBDEQwQhZi9rGDruWptlSomDIXQYpY1smY0zvs_Cu9S6h39fEFTQFNRuW2oxwUGtu8EC6nv_KyutlwMPQE4h1YWSOuOD5JU-A7iMJcRyZ9-CMet_ejzorqxvq9zBCIPG36LGW-yBcBgmTEZ23YVsirTBLAKMFF0XBgtzVL-cBCEoN5w/s1600/Blog%20image%20C2PA.png)

* **Pixel Camera** attaches Content Credentials to any JPEG photo capture, with the appropriate description as defined by the Content Credentials specification for each capture mode.
* **Google Photos** attaches Content Credentials to JPEG images that already have Content Credentials and are edited using AI or non-AI tools, and also to any images that are edited using AI tools. It will validate and display Content Credentials under a new section in the About panel, if the JPEG image being viewed contains this data. Learn more about it in [Google Photos Help](https://support.google.com/photos/answer/16496549?hl=en&sjid=12306603808317880081-NC#zippy=%2Chow-content-credentials-help-you-make-informed-decisions).

Given the broad range of scenarios in which Content Credentials are attached by these apps, we designed our C2PA implementation architecture from the onset to be:

1. **Secure from silicon to applications**
2. **Verifiable, not personally identifiable**
3. **Useable offline**

## Secure from Silicon to Applications

Good actors in the C2PA ecosystem are motivated to ensure that provenance data is trustworthy. C2PA Certification Authorities (CAs), such as Google, are incentivized to only issue certificates to genuine instances of apps from trusted developers in order to prevent bad actors from undermining the system. Similarly, app developers want to protect their C2PA claim signing keys from unauthorized use. And of course, users want assurance that the media files they rely on come from where they claim. For these reasons, the C2PA defined the Conformance Program.

The Pixel Camera application on the Pixel 10 lineup has **[achieved Assurance Level 2](https://github.com/c2pa-org/conformance-public/blob/main/conforming-products/conforming-products-list.json)**, the highest security rating [currently defined](https://github.com/c2pa-org/conformance-public/blob/main/docs/current/C2PA%20Generator%20Product%20Security%20Requirements.pdf) by the C2PA Conformance Program. This was made possible by a strong set of hardware-backed technologies, including Tensor G5 and the certified Titan M2 security chip, along with Android’s hardware-backed security APIs. Only mobile apps running on devices that have the necessary silicon features and Android APIs can be designed to achieve this assurance level. We are working with C2PA to help define future assurance levels that will push protections even deeper into hardware.

Achieving Assurance Level 2 requires verifiable, difficult-to-forge evidence. Google has built an end-to-end system on Pixel 10 devices that verifies several key attributes. However, the security of any claim is fundamentally dependent on the integrity of the application and the OS, an inte...