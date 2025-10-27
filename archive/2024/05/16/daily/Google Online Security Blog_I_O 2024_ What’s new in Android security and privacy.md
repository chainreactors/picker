---
title: I/O 2024: What’s new in Android security and privacy
url: http://security.googleblog.com/2024/05/io-2024-whats-new-in-android-security.html
source: Google Online Security Blog
date: 2024-05-16
fetch_date: 2025-10-06T17:15:28.955688
---

# I/O 2024: What’s new in Android security and privacy

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [I/O 2024: What’s new in Android security and privacy](https://security.googleblog.com/2024/05/io-2024-whats-new-in-android-security.html "I/O 2024: What’s new in Android security and privacy")

May 15, 2024

Posted by Dave Kleidermacher, VP Engineering, Android Security and Privacy

Our commitment to user safety is a top priority for Android. We’ve been consistently working to stay ahead of the world’s scammers, fraudsters and bad actors. And as their tactics evolve in sophistication and scale, we continually adapt and enhance our advanced security features and AI-powered protections to help keep Android users safe.

In addition to our new suite of advanced [theft protection features](https://blog.google/products/android/android-theft-protection) to help keep your device and data safe in the case of theft, we’re also focusing increasingly on providing additional protections against mobile financial fraud and scams.

Today, we’re announcing more new fraud and scam protection features coming in Android 15 and Google Play services updates later this year to help better protect users around the world. We’re also sharing new tools and policies to help developers build safer apps and keep their users safe.

**Google Play Protect live threat detection**

Google Play Protect now scans 200 billion Android apps daily, helping keep more than 3 billion users safe from malware. We are expanding Play Protect’s on-device AI capabilities with Google Play Protect live threat detection to improve fraud and abuse detection against apps that try to cloak their actions.

With live threat detection, Google Play Protect’s on-device AI will analyze additional behavioral signals related to the use of sensitive permissions and interactions with other apps and services. If suspicious behavior is discovered, Google Play Protect can send the app to Google for additional review and then warn users or disable the app if malicious behavior is confirmed. The detection of suspicious behavior is done on device in a privacy preserving way through Private Compute Core, which allows us to [protect users without collecting data](https://security.googleblog.com/2022/12/trust-in-transparency-private-compute.html). Google Pixel, Honor, Lenovo, Nothing, OnePlus, Oppo, Sharp, Transsion, and other manufacturers are deploying live threat detection later this year.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHu3KjsnNfmKKg1Ao5pch2rYyGOJYR5TbJ5dsYKstsVh84orcjM_l6E20ASbRLZtNEK-_UxysLMa7HUUyrlBVbv3QDjzSBUQaHLK3vQlWzH9XekwTB5G_GWEQ_6vqQAZqSjj5jIEnTMCStKtJQuL05p_ACE2WqFgRolKWvGR8NR91JJtO27BsGrntLtTHC/s400/Google%20Play%20Protect%20live%20threat%20detection.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHu3KjsnNfmKKg1Ao5pch2rYyGOJYR5TbJ5dsYKstsVh84orcjM_l6E20ASbRLZtNEK-_UxysLMa7HUUyrlBVbv3QDjzSBUQaHLK3vQlWzH9XekwTB5G_GWEQ_6vqQAZqSjj5jIEnTMCStKtJQuL05p_ACE2WqFgRolKWvGR8NR91JJtO27BsGrntLtTHC/s3816/Google%20Play%20Protect%20live%20threat%20detection.png)

**Stronger protections against fraud and scams**

We’re also bringing additional protections to fight fraud and scams in Android 15 with two key enhancements to safeguard your information and privacy from bad apps:

* **Protecting One-time Passwords from Malware:** With the exception of a few types of apps, such as wearable companion apps, one-time passwords are now hidden from notifications, closing a common attack vector for fraud and spyware.* **Expanded Restricted Settings**: To help protect more sensitive permissions that are commonly abused by fraudsters, we’re expanding Android 13’s [restricted settings](https://support.google.com/android/answer/12623953?hl=en), which require additional user approval to enable permissions when installing an app from an Internet-sideloading source (web browsers, messaging apps or file managers).

We are continuing to develop new, AI-powered protections, like the [scam call detection capability](https://blog.google/products/android/google-ai-android-update-io-2024) that we’re testing, which uses on-device Gemini-Nano AI to warn users in real-time when it detects conversation patterns commonly associated with fraud and scams.

**Protecting against screen-sharing social engineering attacks**
We’re also tightening controls for screen sharing in Android 15 to limit social engineering attacks that try to view your screen and steal information, while introducing new safeguards to further shield your sensitive information:

* **Automatically Hidden Notifications and One-time Passwords (OTPs):** During screen sharing, private notification content will be hidden, preventing remote viewers from seeing details in a user's notifications. Apps that post OTPs in notifications will be automatically protected from remote viewers when you’re screen sharing, helping thwart attempts to steal sensitive data.* **Safer Logins:** Your screen will be hidden when you enter credentials like usernames, passwords and credit card numbers during a screen-share session.* **Choose What You Share:** Currently available on Pixel, other Android devices will also have the ability to share just one app's content rather than your whole screen to help preserve your screen privacy.

Having clear content sharing indicators is important for users to understand when their data is visible. A new, more prominent screen indicator coming to Android devices later this year will always let you know when screen sharing is active, and you can stop sharing with a simple tap.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiF9sSXpP5qJ8i6XEv7mky1cmZhVsDEhzku1rovY4GDAsJS7wx5BmxrHKzaE496UMlUYEklG7BBtz331up3hhCvV5h-2jSHUbUiqHrsxqW8nh-62dxTydtJpqK_i-CX3YoQWDSfuL-l3t_B_ILflRaEPhytzFcF-7OaQJOkFJzpW55rwjIXJwkGs6IDgt-j/s400/Hide%20notifications%20and%20OTPs.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiF9sSXpP5qJ8i6XEv7mky1cmZhVsDEhzku1rovY4GDAsJS7wx5BmxrHKzaE496UMlUYEklG7BBtz331up3hhCvV5h-2jSHUbUiqHrsxqW8nh-62dxTydtJpqK_i-CX3YoQWDSfuL-l3t_B_ILflRaEPhytzFcF-7OaQJOkFJzpW55rwjIXJwkGs6IDgt-j/s3816/Hide%20notifications%20and%20OTPs.png)

**Advanced cellular security to fight fraud and surveillance**

We’re adding new advanced cellular protections in Android 15 to defend against abuse by criminals using cell site simulators to snoop on users or send them SMS-based fraud messages.

* **Cellular Cipher Transparency:** We’ll notify you if your cellular network connection is unencrypted, potentially exposing voice and SMS traffic to radio interception, and potentially visible to others. This can help warn users if they’re being targeted by criminals who are trying to intercept their traffic or inject a fraud SMS message.* **Identifier Disclosure Transparency:** We’ll help at risk-users like journalists or dissidents by alerting them if a potential false cellular base station or surveillance tool is recording their location using a device identifier.

These features require device OEM integration and compatible hardware. We are working with the Android ecosystem to bring these features to users. We expect OEM adoption to progress over the next couple of years.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhvuLLtMUwGfLTp4gmw6f_2_UuhR3KmVAm-2tlwHexRs8qNlntBWGXo9bwggAONKocQXVqB09MoIATqqwwjmpUG5QtgGfgFz-Lc7nVdLgvf3vGPCNN1UlJoF72Bzfy0_-UwfMON2FbMUfPq75ABmlc8JER42jl3xL46J4Xc3kOkArWgDvvSBkn3tqJ5Uv4/s400/Cellular%20security%20encryption%20warning%20blog.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhvuLLtMUwGfLTp4gmw6f_2_UuhR3KmVAm-2tlwHexRs8qNlntBWGXo9bwggAONKocQXVqB09MoIATqqwwjmpUG5QtgGfgFz-Lc7nVdLgvf3vGPCNN1UlJoF72Bzfy0_-UwfMON2FbMUfPq75ABmlc8JER42jl3xL46J4Xc3...