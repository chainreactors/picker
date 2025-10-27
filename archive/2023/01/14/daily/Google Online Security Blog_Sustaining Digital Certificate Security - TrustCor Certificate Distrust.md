---
title: Sustaining Digital Certificate Security - TrustCor Certificate Distrust
url: http://security.googleblog.com/2023/01/sustaining-digital-certificate-security_13.html
source: Google Online Security Blog
date: 2023-01-14
fetch_date: 2025-10-04T03:49:57.955299
---

# Sustaining Digital Certificate Security - TrustCor Certificate Distrust

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Sustaining Digital Certificate Security - TrustCor Certificate Distrust](https://security.googleblog.com/2023/01/sustaining-digital-certificate-security_13.html "Sustaining Digital Certificate Security - TrustCor Certificate Distrust")

January 13, 2023

Posted by Chrome Root Program, Chrome Security Team

*Note: This post is a follow-up to discussions carried out on the Mozilla “[Dev Security Policy](https://groups.google.com/a/mozilla.org/g/dev-security-policy)” Web PKI public discussion forum Google Group in December 2022. Google Chrome communicated its distrust of TrustCor in the public forum on December 15, 2022.*

The Chrome Security Team prioritizes the security and privacy of Chrome’s users, and we are unwilling to compromise on these values.

Google includes or removes CA certificates within the [Chrome Root Store](https://blog.chromium.org/2022/09/announcing-launch-of-chrome-root-program.html) as it deems appropriate for user safety in accordance with our policies. The selection and ongoing inclusion of CA certificates is done to enhance the security of Chrome and promote interoperability.

Behavior that attempts to degrade or subvert security and privacy on the web is incompatible with organizations whose CA certificates are included in the Chrome Root Store. Due to a loss of confidence in its ability to uphold these fundamental principles and to protect and safeguard Chrome’s users, certificates issued by TrustCor Systems will no longer be recognized as trusted by:

* Chrome versions 111 (landing in Beta approximately February 9, 2023 and Stable approximately March 7, 2023) and greater; and* Older versions of Chrome capable of receiving [Component Updates](https://chromium.googlesource.com/chromium/src/%2B/lkgr/components/component_updater/README.md) after Chrome 111’s Stable release date.

This change was [first communicated](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/oxX69KFvsm4/m/PKpJf5W6AQAJ) in the Mozilla “Dev Security Policy” Web PKI public discussion forum Google Group on December 15, 2022.

This change will be implemented via our existing mechanisms to respond to CA incidents via:

* An integrated certificate blocklist, and* Removal of certificates included in the Chrome Root Store.

Beginning approximately March 7, 2023, navigations to websites that use a certificate that chains to one of the roots detailed below will be considered insecure and result in a full page certificate error interstitial.

Affected Certificates (SHA-256 fingerprint):

* [d40e9c86cd8fe468c1776959f49ea774fa548684b6c406f3909261f4dce2575c](https://crt.sh/?q=d40e9c86cd8fe468c1776959f49ea774fa548684b6c406f3909261f4dce2575c)* [0753e940378c1bd5e3836e395daea5cb839e5046f1bd0eae1951cf10fec7c965](https://crt.sh/?q=0753e940378c1bd5e3836e395daea5cb839e5046f1bd0eae1951cf10fec7c965)* [5a885db19c01d912c5759388938cafbbdf031ab2d48e91ee15589b42971d039c](https://crt.sh/?q=5a885db19c01d912c5759388938cafbbdf031ab2d48e91ee15589b42971d039c)

This change will be integrated into the Chromium open-source project as part of a default build. Questions about the expected behavior in specific Chromium-based browsers should be directed to their maintainers.

This change will be incorporated as part of the regular Chrome release process to ensure sufficient time for testing and replacing affected certificates by website operators. Information about release timetables and milestones is available at <https://chromiumdash.appspot.com/schedule>.

Beginning approximately February 9, 2023, website operators can preview these changes in Chrome 111 Beta. Website operators will also be able to preview the change sooner, using our Dev and Canary channels. The majority of users will not encounter behavior changes until the release of Chrome 111 to the Stable channel, approximately March 7, 2023.

Summarizing security response of other Google products:

* **Android** has removed TrustCor’s root CA certificates from the set of platform trusted certificates shipping with future operating system versions. Existing versions of Android will distrust TrustCor’s root CA certificates on a similar timeline as described above for Chrome.* **Gmail** is finalizing its action plan and updates will be made available in the future.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

Labels:

[chrome](https://security.googleblog.com/search/label/chrome)
,
[chrome security](https://security.googleblog.com/search/label/chrome%20security)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/976481015804218737)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/02/taking-next-step-oss-fuzz-in-2023.html "Newer Post")

[**](https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html "Older Post")

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
* [private compute co...