---
title: Burp Suite Android Emulator
url: https://infosecwriteups.com/burp-suite-android-emulator-5c030d420394?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:57:52.192294
---

# Burp Suite Android Emulator

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5c030d420394&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-suite-android-emulator-5c030d420394&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-suite-android-emulator-5c030d420394&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5c030d420394---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5c030d420394---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Burp Suite Android Emulator Setup

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:64:64/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---byline--5c030d420394---------------------------------------)

[Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---byline--5c030d420394---------------------------------------)

3 min read

·

Dec 18, 2022

--

2

Share

Guide to setup Burp Suite on your Android Emulator

Burp Suite has a [great guide](https://blog.ropnop.com/configuring-burp-suite-with-android-nougat) for setting this up, which I’ll be referencing, but it’s not for emulators, and I’ve found no complete guide online, so I’ll make one here. If you like it follow my [Twitter](https://twitter.com/AdamJSturge) and medium for more guides and tips

Install [Android Studio](https://developer.android.com/studio)

Run this command in your terminal to allow you to make changes to your emulator’s system

```
launchctl setenv studio.emu.params -writable-system
```

Install [adb](https://developer.android.com/studio/command-line/adb): `adb devices` will let you know if it’s installed

Go to the "Proxy Tab" in Burp and select "Options." In the ‘Proxy listeners’ export your cert in der format. I called it `cacert.der`

Press enter or click to view image in full size

![]()

Run these 3 commands to change the cert to a pem and it’s name to it’s `hash value` appended with `.0` (Replace <hash> with the hash printed from the second command)

```
openssl x509 -inform DER -in cacert.der -out cacert.pem
openssl x509 -inform PEM -subject_hash_old -in cacert.pem |head -1
mv cacert.pem <hash>.0
```

We need to start the emulator on android studio, so open an empty project and hit the start button that’s highlighted in my photo

Once the emulator is up we are going to adb push the cert to the device

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5c030d420394---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5c030d420394---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5c030d420394---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5c030d420394---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--5c030d420394---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:96:96/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--5c030d420394---------------------------------------)

[![Adam J Sturge](https://miro.medium.com/v2/resize:fill:128:128/1*AX1cAqP11mihW4R-ONoVTA.png)](https://adamjsturge.medium.com/?source=post_page---post_author_info--5c030d420394---------------------------------------)

[## Written by Adam J Sturge](https://adamjsturge.medium.com/?source=post_page---post_author_info--5c030d420394---------------------------------------)

[369 followers](https://adamjsturge.medium.com/followers?source=post_page---post_author_info--5c030d420394---------------------------------------)

·[21 following](https://medium.com/%40adamjsturge/following?source=post_page---post_author_info--5c030d420394---------------------------------------)

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----5c030d420394---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----5c030d420394---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5c030d420394---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5c030d420394---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----5c030d420394---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5c030d420394---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----5c030d420394---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5c030d420394---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5c030d420394---------------------------------------)