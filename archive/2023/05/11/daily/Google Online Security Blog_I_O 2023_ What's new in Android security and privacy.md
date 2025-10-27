---
title: I/O 2023: What's new in Android security and privacy
url: http://security.googleblog.com/2023/05/io-2023-android-security-and-privacy.html.html
source: Google Online Security Blog
date: 2023-05-11
fetch_date: 2025-10-04T11:36:58.617883
---

# I/O 2023: What's new in Android security and privacy

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [I/O 2023: What's new in Android security and privacy](https://security.googleblog.com/2023/05/io-2023-android-security-and-privacy.html.html "I/O 2023: What's new in Android security and privacy")

May 10, 2023

Posted by Ronnie Falcon, Product Manager

Android is built with multiple layers of security and privacy protections to help keep you, your devices, and your data safe. Most importantly, we are committed to transparency, so you can see your device safety status and know how your data is being used.

Android uses the best of Google’s AI and machine learning expertise to proactively protect you and help keep you out of harm’s way. We also empower you with tools that help you take control of your privacy.

I/O is a great moment to show how we bring these features and protections all together to help you stay safe from threats like phishing attacks and password theft, while remaining in charge of your personal data.

**Safe Browsing: faster more intelligent protection**

Android uses Safe Browsing to protect billions of users from web-based threats, like deceptive phishing sites. This happens in the Chrome default browser and also in Android WebView, when you open web content from apps.

Safe Browsing is getting a big upgrade with a new real-time API that helps ensure you’re warned about fast-emerging malicious sites. With the newest version of Safe Browsing, devices will do real-time blocklist checks for low reputation sites. Our internal analysis has found that a significant number of phishing sites only exist for less than ten minutes to try and stay ahead of block-lists. With this real-time detection, we expect we’ll be able to block an additional 25 percent of phishing attempts every month in Chrome and Android[1](#fn1).

Safe Browsing isn’t just getting faster at warning users. We’ve also been building in more intelligence, leveraging Google’s advances in AI. Last year, Chrome browser on Android and desktop started utilizing a [new image-based phishing detection machine learning model](https://blog.google/products/chrome/building-a-more-helpful-browser-with-machine-learning/) to visually inspect fake sites that try to pass themselves off as legitimate log-in pages. By leveraging a TensorFlow Lite model, we’re able to find 3x more[2](#fn2) phishing sites compared to previous machine learning models and help warn you before you get tricked into signing in. This year, we're expanding the coverage of the model to detect hundreds of more phishing campaigns and leverage new ML technologies.

This is just one example of how we use our AI expertise to keep your data safe. Last year, Android used AI to protect users from 100 billion suspected spam messages and calls.[3](#fn3)

**Passkeys helps move users beyond passwords**

For many, passwords are the primary protection for their online life. In reality, they are frustrating to create, remember and are easily hacked. But cybercriminals can’t phish a password that doesn’t exist. Which is why we are excited to share another major step forward in our passwordless journey: Passkeys.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8sVka7rMRsIjOOmsQQtqe_0fcZZftD5puxtcKFTwrJgg4H7o-edQgZPu5YMxsPiKBYCK_HgONPHB_vzYWFwSTqYks3nvMtJxnJJKHxPRArXAmQxZSOzPGgNXB5hh3P7HrVIBxK4ot5rYzM4qcObaurFYX_RnFZjH_Wrtu12xsBUQcTXBeDh0qHBsIcQ/w320-h640/Passkey%20Screen%20(1).gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8sVka7rMRsIjOOmsQQtqe_0fcZZftD5puxtcKFTwrJgg4H7o-edQgZPu5YMxsPiKBYCK_HgONPHB_vzYWFwSTqYks3nvMtJxnJJKHxPRArXAmQxZSOzPGgNXB5hh3P7HrVIBxK4ot5rYzM4qcObaurFYX_RnFZjH_Wrtu12xsBUQcTXBeDh0qHBsIcQ/s1200/Passkey%20Screen%20%281%29.gif)

Passkeys combine the advanced security of 2-Step Verification with the convenience of simply unlocking your device — so signing in is as easy as glancing at your phone or scanning your fingerprint. And because they use cutting-edge cryptography to create a “key” that is unique between *you* and a specific app or website, passkeys can’t be stolen by hackers the way that passwords can.

Last week, we [announced](https://blog.google/technology/safety-security/the-beginning-of-the-end-of-the-password/) you can use a passkey to log in to your Google Account on all major platforms. We’re the first major tech company to simplify sign-in with passkeys across our own platform. You can also use passkeys on services like PayPal, Shopify, and Docusign, with many more on the way. Start saying goodbye to passwords and [try it](g.co/passkeys) today.

To help support developers as they incorporate passkeys, we’ve [launched a Credential Manager Jetpack API](https://android-developers.googleblog.com/2023/02/bringing-together-sign-in-solutions-and-passkeys-android-new-credential-manager.html) that brings together multiple sign-in methods, such as passkeys, passwords and federated sign in, into a unified interface for users and a single API for developers.

**Better protections for apps**

Accessibility services are helpful for people with disabilities but their broad powers can be used by malware and bad apps to read screen content. In Android 14, we’re introducing a new API that lets developers limit accessibility services from interacting with their apps. Now, with a new app attribute, developers can limit access to only apps that have declared and have been validated by Google Play Protect as accessibility tools. This adds more protection from side-loaded apps that may get installed and are trying to access sensitive data.

In Android 14, we’re preventing apps that target an SDK level lower than 23 from being installed. This is because malware often targets older levels to get around newer security and privacy protections. This won’t affect existing apps on your device, but new installs will have to meet this requirement.

Learn more about how we’re protecting apps and developers in the What’s New in Google Play [blog](https://android-developers.googleblog.com/2023/05/io-2023-whats-new-in-google-play.html).

**More transparency around how your data is used**

We [launched](https://blog.google/products/google-play/data-safety/) the Data safety section in Google Play last year to help you see how developers collect, share, and protect user data. Every day, millions of users use the Data Safety section information to evaluate an app’s safety before installing it.

In Android 14, we’re extending this transparency to permission dialogs, starting with location data usage. So every time an app asks for permission to use location data, you’ll be able to see right away if the app shares the location data with third parties.

And if an app changes its data sharing practices, for example, to start using it for ads purposes, we’ll notify you through a new monthly notification. As with the permissions dialogs, we’re starting with location data but will be expanding to other permission types in future releases.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiCum3-DZNow9FCvdADj2cdNwWP8-HAurgTKYVPRaXmHI5_Ld9BM08pVgunAin1-UY9AwLFm1svoGUZANYV9hERTsE_oMhpkgs4T4z5wx_579W6sW_qUmVZM9yMgMH0RckmPBs_UXLjbLLz3M42fKtfd5w5sA3xeWTJ68yDJKY1dA5Pya_ZGV9iEwMvg/w320-h640/PSL%20in%20permissions%20(1)%20(1).gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiCum3-DZNow9FCvdADj2cdNwWP8-HAurgTKYVPRaXmHI5_Ld9BM08pVgunAin1-UY9AwLFm1svoGUZANYV9hERTsE_oMhpkgs4T4z5wx_579W6sW_qUmVZM9yMgMH0RckmPBs_UXLjbLLz3M42fKtfd5w5sA3xeWTJ68yDJKY1dA5Pya_ZGV9iEwMvg/s1200/PSL%20in%20permissions%20%281%29%20%281%29.gif)

We’re also empowering you with greater clarity and control over your account data by making it easier to [delete accounts](https://android-developers.googleblog.com/...