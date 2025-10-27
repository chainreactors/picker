---
title: Making authentication faster than ever: passkeys vs. passwords
url: http://security.googleblog.com/2023/05/making-authentication-faster-than-ever.html
source: Google Online Security Blog
date: 2023-05-06
fetch_date: 2025-10-04T11:38:24.085875
---

# Making authentication faster than ever: passkeys vs. passwords

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Making authentication faster than ever: passkeys vs. passwords](https://security.googleblog.com/2023/05/making-authentication-faster-than-ever.html "Making authentication faster than ever: passkeys vs. passwords")

May 5, 2023

Silvia Convento, Senior UX Researcher, Court Jacinic, Senior UX Content Designer, Becca Shareff, User Experience Researcher

In recognition of World Password Day 2023, [Google announced](https://blog.google/technology/safety-security/the-beginning-of-the-end-of-the-password/) its next step toward a passwordless future: passkeys.

Passkeys are a [new, passwordless authentication method](https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html) that offer a convenient authentication experience for sites and apps, using just a fingerprint, face scan or other screen lock. They are designed to enhance online security for users. Because they are based on the public key cryptographic protocols that underpin security keys, they are resistant to phishing and other online attacks, making them more secure than SMS, app based one-time passwords and other forms of multi-factor authentication (MFA). And since passkeys are standardized, a single implementation enables a passwordless experience across browsers and operating systems.

Passkeys can be used in two different ways: on the same device or from a different device. For example, if you need to sign in to a website on an Android device and you have a passkey stored on that same device, then using it only involves unlocking the phone. On the other hand, if you need to sign in to that website on the Chrome browser on your computer, you simply scan a QR code to connect the phone and computer to use the passkey.

The technology behind the former (“same device passkey”) is not new: it was originally developed within [the FIDO Alliance](https://fidoalliance.org/) and first implemented by [Google in August 2019](https://security.googleblog.com/2019/08/making-authentication-even-easier-with_12.html) in select flows. Google and other FIDO members have been working together on enhancing the underlying technology of passkeys over the last few years to improve their usability and convenience. This technology behind passkeys allows users to log in to their account using any form of device-based user verification, such as biometrics or a PIN code. A credential is only registered once on a user’s personal device, and then the device proves possession of the registered credential to the remote server by asking the user to use their device’s screen lock.

The user’s biometric, or other screen lock data, is never sent to Google’s servers - it stays securely stored on the device, and only cryptographic proof that the user has correctly provided it is sent to Google. Passkeys are also created and stored on your devices and are not sent to websites or apps. If you create a passkey on one device the Google Password Manager can make it available on your other devices that are signed into the same system account.

Learn more on how passkey works under the hood in our [Google Security Blog](https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html).

Emerging Google data shows promise for a passwordless future with passkeys

Passkeys were originally designed to provide simpler and more secure authentication experiences for users, and so far, the technology has proven to be simpler and faster than passwords. Google data (March-April 2023) shows how the percentage of users successfully authenticating through same device passkeys is 4x higher than the success rate typically achieved with passwords: average authentication success rate with passwords is 13.8%, while local passkey success rate is 63.8% (see figure 1 below).

Passkeys are not just easier to use, but also significantly faster than passwords. On average, a user can successfully sign in within 14.9 seconds, while it typically takes twice as long to sign in with passwords (30.4 seconds, as seen in Figure 2 below). Preliminary, qualitative data collected from user research also indicates that  users already perceive this convenience as the key value of passkeys.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5baUsvUIh27iTBqgxPjF2U4h-IDJz8WGdBFB7wviRgq-dxIrggZnDbVo7RqeSh3ew0OQ4jy0UfjOhpBNMQhtnjV9_MNlbzoL-f2sOkZZaRrcThguOsJ1fS8bdWnkIfSdYM3Sqqx_LaXois1SzTPZpkAO2fXArn9u2G4ROBdKknAkGJs-RryvAs4O6lA/w549-h261/Screenshot%202023-05-05%20at%2010.10.43%20AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5baUsvUIh27iTBqgxPjF2U4h-IDJz8WGdBFB7wviRgq-dxIrggZnDbVo7RqeSh3ew0OQ4jy0UfjOhpBNMQhtnjV9_MNlbzoL-f2sOkZZaRrcThguOsJ1fS8bdWnkIfSdYM3Sqqx_LaXois1SzTPZpkAO2fXArn9u2G4ROBdKknAkGJs-RryvAs4O6lA/s1366/Screenshot%202023-05-05%20at%2010.10.43%20AM.png)

Figure 1: authentication success rate with passkey vs password. Data from March-April 2023 (n≈100M)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh9dhP_BTIs8qA16d0PEUbbnPDE8YUL0MM-5riLGhbekttYWFv1YI30sS6HsT6aAILdS1BTF4IbAfFD8fksfy7Uqys5sfiZgb5u3UGhVPeCKgv8I357J3zjrnVEJUOP25-KaIx1j7nIyrVNQH7VgYCeujpGyA4tZHEOW8QWl8wsXAfkOqA0D5ZYJX6xA/w586-h295/Screenshot%202023-05-05%20at%2010.07.51%20AM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh9dhP_BTIs8qA16d0PEUbbnPDE8YUL0MM-5riLGhbekttYWFv1YI30sS6HsT6aAILdS1BTF4IbAfFD8fksfy7Uqys5sfiZgb5u3UGhVPeCKgv8I357J3zjrnVEJUOP25-KaIx1j7nIyrVNQH7VgYCeujpGyA4tZHEOW8QWl8wsXAfkOqA0D5ZYJX6xA/s1408/Screenshot%202023-05-05%20at%2010.07.51%20AM.png)

Figure 2: time spent authenticating with passkey vs password (data from March-April 2023). Dashed, vertical lines indicate average duration for each authentication method (n≈100M)

We are excited to share this data following our launch of passkeys for Google Accounts. Passkeys are faster, more secure, and more convenient than passwords and MFA, making them a desirable alternative to passwords and a promising development in the journey to a more secure future. To learn more about passkeys and how to turn a basic form-based username and password sign-in system into one that supports passkeys, check out the documentation on [developers.google.com/identity/passkeys](http://developers.google.com/identity/passkeys).

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/5571181486321078716)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/05/io-2023-android-security-and-privacy.html.html "Newer Post")

[**](https://security.googleblog.com/2023/05/introducing-rulesoci.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackh...