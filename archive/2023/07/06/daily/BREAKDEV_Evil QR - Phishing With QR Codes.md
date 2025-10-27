---
title: Evil QR - Phishing With QR Codes
url: https://breakdev.org/evilqr-phishing/
source: BREAKDEV
date: 2023-07-06
fetch_date: 2025-10-04T11:52:49.616522
---

# Evil QR - Phishing With QR Codes

[![BREAKDEV](https://breakdev.org/content/images/2022/08/breakdev_logo_with_title.png)](https://breakdev.org)

* [Home](https://breakdev.org/)
* [Evilginx Pro](https://evilginx.com)
* [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery)
* [Tools](https://github.com/kgretzky)
* [Contact](https://breakdev.org/contact/)

[phishing](/tag/phishing/)

# Evil QR - Phishing With QR Codes

Evil QR is a spin-off of a QRLJacking attack, demonstrating how attackers could take over accounts by convincing users to scan supplied QR codes, through phishing.

* [![Kuba Gretzky](/content/images/size/w100/2022/08/avatar512.png)](/author/kuba/)

#### [Kuba Gretzky](/author/kuba/)

Jul 5, 2023
• 7 min read

![Evil QR - Phishing With QR Codes](/content/images/size/w2000/2023/07/evilqr-blog-cover2.png)

Today I'm publishing the research I started to work on last year, but I was too busy with the [Evilginx Mastery](https://academy.breakdev.org/evilginx-mastery) course, to publish it, at the time.

If you want a quick TL;DR rundown of what this blog post is about, check out the demo video I prepared:

# Background

In recent years, I've noticed that more and more web applications begin to offer a new way to sign in - through QR code scanning. This method is especially convenient if you have a mobile app, on your phone, corresponding to the web application you are trying to sign into, in your web browser.

Here are the most popular websites, you can sign into, in any web browser, by scanning a QR code within the mobile application.

![](https://breakdev.org/content/images/2023/07/chrome_MjsPYYQP9L.png)

Discord

![](https://breakdev.org/content/images/2023/07/chrome_KNrCzWXZJY.png)

Telegram

![](https://breakdev.org/content/images/2023/07/chrome_oT6hs4i5n9.png)

Whatsapp

![](https://breakdev.org/content/images/2023/07/chrome_jaxSIkFFVQ.png)

Steam

![](https://breakdev.org/content/images/2023/07/chrome_XeZrh4q1a8.png)

TikTok

![](https://breakdev.org/content/images/2023/07/chrome_jt9fNtReWm.png)

Binance

To sign in, you open the mobile application, navigate to "Scan QR code", usually residing somewhere within your profile settings, in the mobile application, and scan the QR with your phone camera.

The QR code, displayed on every sign-in page, is nothing more than a dynamically generated session token, which you can authorize with your mobile application, to pair it with your account.

Try to scan any of these QR codes with your phone's camera and you'll see the code translates into a unique string, usually presented in URL format. Here are several examples:

Discord:

```
https://discord.com/ra/GLt61XsN_fuakToqeSMV25pd3G-uwSbdScI1Zc9iwT8
```

Whatsapp:

```
2@o7Ugs+XwUVXgG2f8stGluhiItwCxbZJNLkpkeKEhz65GmPh6+/N1lp3fXpaSjxeARrE2JGXi3ikIFA==,it98cjNOA3qvp4i/TidKTeWZTrGkFUTnqsOzPPxFEzI=,AMV+jQ0gSnoFFKbuYzKdrDSPT7BVZ4R5iFxIGEbCqQI=,nVAlyqnDJiYfW/S1LzZoaVNsDm+pNaB1mGm8pGC0+/E=,1
```

Steam:

```
https://s.team/q/1/1711614348354244891
```

TikTok:

```
https://www.tiktok.com/t/ZGJXCraU8/
```

Binance:

```
https://www.binance.com/en/qr/93bd2ead7e504488bda81bf50deab7e8
```

Now let's imagine if there is any potential way, attackers could convince users to scan the QR code with the session token they control.

# Meet Evil QR Phishing aka QRLJacking

One day you receive an email, telling you that you've been granted exclusive access to a private Discord server, where highly valuable information will be shared, among the participants. All you need to do is open the attached link and scan the QR code with your Discord application.

You click the link and the following website shows up in your web browser:

![](https://breakdev.org/content/images/2023/07/chrome_ZDBusl819X.png)

Phishing page deployed and hosted by the attacker

Since you are pretty excited to join, you open your Discord application and scan the QR code, showing up on the screen of your PC. Discord asks you to confirm if you want to sign in, using the scanned QR code. You think that it makes sense that you need to be signed in to join the Discord server, so you agree without hesitation.

Once you approve the login attempt, the website redirects you to the Discord server page. You lose interest and go back to your other activities. All this without realizing, you've just given the attacker full access to your account.

## What happened?

Here is the step-by-step process of what the attacker did to pull off this phishing attack, using the [Evil QR](https://github.com/kgretzky/evilqr) toolkit.

1. The attacker opens the official [Discord login page](https://discord.com/login) within their web browser to generate the sign-in QR code.
2. Using the [Evil QR](https://github.com/kgretzky/evilqr) browser extension, the attacker is able to extract the sign-in QR code from the login page and upload it to the [Evil QR](https://github.com/kgretzky/evilqr) server, where the phishing page is hosted.
3. The phishing page, hosted by the attacker, dynamically displays the most recent sign-in QR code controlled by the attacker.

Once the target successfully scans the QR code, the attacker takes over the phished account.

The concept of phishing users with sign-in QR codes is not new and it has been [broadly documented](https://seekurity.com/blog/2016/11/04/admin/phishing-analysis/qrljacking-your-qr-based-session-belongs-to-us) by [Mohamed Abdelbasset Elnouby (@SymbianSyMoh)](https://twitter.com/SymbianSyMoh) from [Seekurity](https://seekurity.com/) in 2016! I highly recommend you read this post as it covers a lot of information about the potential attack vectors, which could be used to pull off such attacks.

The technique was later officially recognized as [QRLJacking](https://owasp.org/www-community/attacks/Qrljacking) and [@SymbianSyMoh](https://twitter.com/SymbianSyMoh/status/1675895436870139904) also released a [QRLJacker](https://github.com/OWASP/QRLJacking) tool in 2020 to demonstrate how such attacks can be executed. Evil QR idea is just a spin-off of the same idea.

# Evil QR Toolkit

To demonstrate this interesting phishing technique, I've developed a set of proof-of-concept tools for demonstration purposes.

You can find the open-sourced [Evil QR](https://github.com/kgretzky/evilqr) toolkit on my [GitHub](https://github.com/kgretzky/evilqr) if you're interested in trying it out yourself.

As you can see below, the Evil QR attack can be customized using personalized phishing pre-text, with dynamic updates, for every website separately. Evil QR browser extension can detect and extract QR codes, within websites, no matter how they are rendered.

The extension supports extracting QR codes rendered as `CANVAS`, `IMG`, `SVG` or even `DIV` (by taking a screenshot with [html2canvas](https://html2canvas.hertzen.com/) library).

![](https://breakdev.org/content/images/2023/07/evilqr-phishing.gif)

### Evil QR Server

The server is developed in GO and its main purpose is to expose REST API for the browser extension and run an HTTP server to host the phishing page.

It awaits authenticated communication from the browser extension including QR code image with metadata in JSON format on `/qrcode/[qr_uuid]` endpoint:

```
{
    "id": "11111111-1111-1111-1111-111111111111",
    "source": "data:image/png;base64,iVBORw0K...",
    "host": "discord.com"
}
```

The retrieved QR code is then stored and is available for retrieval by the JavaScript, running on the phishing page. The phishing page is using [HTTP Long Polling](https://www.pubnub.com/blog/http-long-polling/) to be able to retrieve QR code updates with minimal delays, without having to use Websockets.

The phishing page automatically detects which hostname the QR code was retrieved from and can dynamically adjust its CSS and text content to change the phishing pre-text, for social engineering purposes.

### Evil QR Browser Extension

![](https://breakdev.org/content/images/2023/07/image.png)

The extension is used solely by the attacker and it needs to be enabled on the s...