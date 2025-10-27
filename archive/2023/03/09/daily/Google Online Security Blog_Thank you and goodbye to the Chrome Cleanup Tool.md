---
title: Thank you and goodbye to the Chrome Cleanup Tool
url: http://security.googleblog.com/2023/03/thank-you-and-goodbye-to-chrome-cleanup.html
source: Google Online Security Blog
date: 2023-03-09
fetch_date: 2025-10-04T08:59:11.587412
---

# Thank you and goodbye to the Chrome Cleanup Tool

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Thank you and goodbye to the Chrome Cleanup Tool](https://security.googleblog.com/2023/03/thank-you-and-goodbye-to-chrome-cleanup.html "Thank you and goodbye to the Chrome Cleanup Tool")

March 8, 2023

Posted by Jasika Bawa, Chrome Security Team

Starting in Chrome 111 we will begin to turn down the Chrome Cleanup Tool, an application distributed to Chrome users on Windows to help find and remove unwanted software (UwS).

## Origin story

The Chrome Cleanup Tool was introduced in 2015 to help users recover from unexpected settings changes, and to detect and remove unwanted software. To date, it has performed more than 80 million cleanups, helping to pave the way for a cleaner, safer web.

## A changing landscape

In recent years, several factors have led us to reevaluate the need for this application to keep Chrome users on Windows safe.

First, the user perspective – Chrome user complaints about UwS have continued to fall over the years, averaging out to around 3% of total complaints in the past year. Commensurate with this, we have observed a steady decline in UwS findings on users' machines. For example, last month just 0.06% of Chrome Cleanup Tool scans run by users detected known UwS.

Next, several positive changes in the platform ecosystem have contributed to a more proactive safety stance than a reactive one. For example, [Google Safe Browsing](https://safebrowsing.google.com/) as well as antivirus software both block file-based UwS more effectively now, which was originally the goal of the Chrome Cleanup Tool. Where file-based UwS migrated over to extensions, our substantial investments in the Chrome Web Store [review process](https://developer.chrome.com/docs/webstore/review-process/) have helped catch malicious extensions that violate the Chrome Web Store's policies.

Finally, we've observed changing trends in the malware space with techniques such as [Cookie Theft](https://blog.google/threat-analysis-group/phishing-campaign-targets-youtube-creators-cookie-theft-malware/) on the rise – as such, we've doubled down on defenses against such malware via a variety of improvements including hardened authentication workflows and advanced heuristics for blocking phishing and social engineering emails, malware landing pages, and downloads.

## What to expect

Starting in Chrome 111, users will no longer be able to request a Chrome Cleanup Tool scan through Safety Check or leverage the "Reset settings and cleanup" option offered in chrome://settings on Windows. Chrome will also remove the component that periodically scans Windows machines and prompts users for cleanup should it find anything suspicious.

Even without the Chrome Cleanup Tool, users are automatically protected by [Safe Browsing in Chrome](https://support.google.com/chrome/answer/9890866?hl=en&co=GENIE.Platform%3DDesktop&oco=0). Users also have the option to turn on [Enhanced protection](https://security.googleblog.com/2022/12/enhanced-protection-strongest-level-of.html) by navigating to chrome://settings/security – this mode substantially increases protection from dangerous websites and downloads by sharing real-time data with Safe Browsing.

While we'll miss the Chrome Cleanup Tool, we wanted to take this opportunity to acknowledge its role in combating UwS for the past 8 years. We'll continue to monitor user feedback and trends in the malware ecosystem, and when adversaries adapt their techniques again – which they will – we'll be at the ready.

As always, please feel free to send us [feedback](https://bugs.chromium.org/p/chromium/issues/list) or find us on Twitter [@googlechrome](https://twitter.com/googlechrome).

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

Labels:

[chrome](https://security.googleblog.com/search/label/chrome)
,
[chrome security](https://security.googleblog.com/search/label/chrome%20security)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/1446278575177326265)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/03/osv-and-vulnerability-life-cycle.html "Newer Post")

[**](https://security.googleblog.com/2023/03/google-trust-services-now-offers-tls.html "Older Post")

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
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security](https://security.googleblog.com/search/label/chrome%20security)
* [connected devices](https://security.googleblog.com/search/label/connected%20devices)
* [CTF](https://security.googleblog.com/search/label/CTF)
* [diversity](https://security.googleblog.com/search/label/diversity)
* [encryption](https://security.googleblog.com/search/label/encryption)
* [federated learning](https://security.googleblog.com/search/label/federated%20learning)
* [fuzzing](https://security.googleblog.com/search/label/fuzzing)
* [Gboard](https://security.googleblog.com/search/label/Gboard)
* [google play](https://security.googleblog.com/search/label/google%20play)
* [google play protect](https://security.googleblog.com/search/label/google%20play%20protect)
* [hacking](https://security.googleblog.com/search/label/hacking)
* [interoperability](https://security.googleblog.com/search/label/interoperability)
* [iot security](https://security.googleblog.com/search/label/iot%20security)
* [kubernetes](https://security.googleblog.com/search/label/kubernetes)
* [linux kernel](https://security.googleblog.com/search/label/linux%20kernel)
* [memory safety](https://security.googleblog.com/search/label/memory%20safety)
* [Open Source](https://security.googleblog.com/search/label/Open%20Source)
* [pha family highlights](https://security.googleblog.com/search/label/pha%20family%20highlights)
* [pixel](https://security.googleblog.com/search/label/pixel)
* [privacy](https://security.googleblog.com/search/label/privacy)
* [private compute core](https://security.googleblog.com/search/label/private%20compute%20core)
* [Rowhammer](https://security.googleblog.com/search/label/Rowhammer)
* [rust](https://security.googleblog.com/search/label/rust)
* [Security](https://security.googleblog.com/search/label/Security)
* [security rewards program](https://security.googleblog.com/search/label/security%20rewards%20program)
* [sigstore](https://security.googleblog.com/search/label/sigstore)
* [spyware](https://security.googleblog.com/search/label/spyware)
* [supply chain](https://security.googleblog.com/search/label/supply%20chain)
* [targeted spyware](https:...