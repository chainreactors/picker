---
title: Enrolling macOS Golden Gate 27.0.0 virtual machines with MDM servers does not work correctly
url: https://derflounder.wordpress.com/2026/09/15/enrolling-macos-golden-gate-27-0-0-virtual-machines-with-mdm-servers-does-not-work-correctly/
source: Der Flounder
date: 2026-09-15
fetch_date: 2026-09-16T06:58:14.896378
---

# Enrolling macOS Golden Gate 27.0.0 virtual machines with MDM servers does not work correctly

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Push Notification Service](https://derflounder.wordpress.com/category/apple-push-notification-service/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/), [Secure Enclave](https://derflounder.wordpress.com/category/secure-enclave/), [Virtualization](https://derflounder.wordpress.com/category/virtualization/) > Enrolling macOS Golden Gate 27.0.0 virtual machines with MDM servers does not work correctly

## Enrolling macOS Golden Gate 27.0.0 virtual machines with MDM servers does not work correctly

September 15, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of testing macOS Golden Gate, it was discovered by myself and others that MDM enrollment does not appear to completely work. In my testing, here’s what I did:

1. Create a macOS VM running macOS 27.0.0
2. Enroll it in an MDM (in my case, Jamf Pro) using profile-based device enrollment.
3. MDM enrollment profile is successfully installed.

Expected behavior following step #3:

* Additional configuration profiles and Jamf software components are installed on the macOS VM.

Actual behavior following step #3:

* No additional profiles or Jamf software components are installed. Only the MDM enrollment profile is visible in System Settings, in **General**: **Device Management**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-15-at-8.38.36am.png?w=595 "Screenshot 2026-09-15 at 8.38.36 AM.png")

What’s happening after step #3? For more details, please see below the jump.

To check on this issue, I ran the following command using the [log command line tool](https://ss64.com/mac/log.html) to see what was being logged within the last hour by **apsd**, the background system process on macOS responsible for maintaining macOS’s persistent connection to Apple’s Push Notification service (APNS):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | log show –info –debug –predicate 'process == "apsd" AND (eventMessage CONTAINS[c] "BAA" OR eventMessage CONTAINS[c] "unable to generate key" OR eventMessage CONTAINS[c] "server bag")' –last 1h |

[view raw](https://gist.github.com/rtrouton/e3bbce8ac12c4789ab9075b99b540d18/raw/2127f3831bad7edd0c0ae8b893f8f6f967b447b8/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e3bbce8ac12c4789ab9075b99b540d18#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

When I checked the logging, I saw the following logging repeatedly appear:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 2026-09-15 08:35:55.176162-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] <private>: Identity provider has processed server bag update, user courier finished processing config |
|  | 2026-09-15 08:35:55.176162-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] <private> user courier finished processing server bag (1/2) |
|  | 2026-09-15 08:35:55.176163-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] <private>: Identity provider has processed server bag update, user courier finished processing config |
|  | 2026-09-15 08:35:55.176164-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] <private> user courier finished processing server bag (2/2) |
|  | 2026-09-15 08:35:55.176164-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] <private> all couriers have finished processing server bag |
|  | 2026-09-15 08:35:55.176164-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:stream] <private>: Delegates have processed server bag update, checking if stream should connect |
|  | 2026-09-15 08:35:55.176582-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] APSBAAClientIdentityProvider attempting to fetch BAA certs |
|  | 2026-09-15 08:35:55.176632-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] APSBAAClientIdentityProvider fetching BAA cert |
|  | 2026-09-15 08:35:55.178997-0700 0x3e8 Error 0x176f 133 0 apsd: (CryptoTokenKit) [com.apple.CryptoTokenKit:sepkey] <sepk:\* kid=0000000000000000>: (apsd) unable to generate key: error e00002e2(-536870174) ACL=<SecAccessControlRef: dk;ock(true);odel(true);osgn(true);oa(true);okd(true)> params=<AKSp:{acmh:###,ag:[],ed:{acl:{ock:true,odel:true,osgn:true,oa:true,okd:true}}}> |
|  | 2026-09-15 08:35:55.179032-0700 0x3e8 Error 0x176e 133 0 apsd: (Security) [com.apple.security:seckey] SecKeyCreateRandomKey\_ios failed: Error Domain=NSOSStatusErrorDomain Code=-25308 "Failed to generate keypair" (errKCInteractionNotAllowed / errSecInteractionNotAllowed: / Interaction is not allowed with the Security Server.) UserInfo={numberOfErrorsDeep=0, NSDescription=Failed to generate keypair, NSUnderlyingError=0x7c56d55fe0 {Error Domain=NSOSStatusErrorDomain Code=-25308 "<sepk:\* kid=0000000000000000>: unable to generate key" UserInfo={NSDebugDescription=<sepk:\* kid=0000000000000000>: unable to generate key, AKSError=-536870174}}} |
|  | 2026-09-15 08:35:55.179085-0700 0x2b5 Default 0x0 133 0 apsd: (DeviceIdentity) Error Domain=com.apple.MobileActivation.ErrorDomain Code=-1 "Failed to create reference key." UserInfo={NSLocalizedDescription=Failed to create reference key., NSUnderlyingError=0x7c56d560d0 {Error Domain=com.apple.MobileActivation.ErrorDomain Code=-1 "Failed to create ref key." UserInfo={NSLocalizedDescription=Failed to create ref key., NSUnderlyingError=0x7c56c55350 {Error Domain=NSOSStatusErrorDomain Code=-25308 "Failed to generate keypair" (errKCInteractionNotAllowed / errSecInteractionNotAllowed: / Interaction is not allowed with the Security Server.) UserInfo={numberOfErrorsDeep=0, NSDescription=Failed to generate keypair, NSUnderlyingError=0x7c56d55fe0 {Error Domain=NSOSStatusErrorDomain Code=-25308 "<sepk:\* kid=0000000000000000>: unable to generate key" UserInfo=0x7c571c8860 (not displayed)}}}}}} |
|  | 2026-09-15 08:35:55.179108-0700 0x2b5 Default 0x0 133 0 apsd: [com.apple.apsd:courier] APSBAAClientIdentityProvider failed to obtain a BAA cert, error: Error Domain=com.apple.MobileActivation.ErrorDomain Code=-1 UserInfo={NSLocalizedDescription=<private>, NSUnderlyingError=0x7c56d560d0 {Error Domain=com.apple.MobileActivation.ErrorDomain Code=-1 UserInfo={NSLocalizedDescription=<private>, NSUnderlyingError=0x7c56c55350 {Error Domain=NSOSStatusErrorDomain Code=-25308 UserInfo={numberOfErrorsDeep=0, NSDescription=<private>, NSUnderlyingError=0x7c56d55fe0 {Error Domain=NSOSStatusErrorDomain Code=-25308 UserInfo=0x7c571c8860 (not displayed)}}}}}} |

[view raw](https://gist.github.com/rtrouton/6fdf84b55ab6ac38c793b35b0cb0335a/raw/b0f1bb895adbbaadf7be06b51a6d119e415e76b4/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/6fdf84b55ab6ac38c793b35b0cb0335a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Based on the information discussed in [this post in the Apple Developer Forums](https://developer.apple.com/forums/thread/840500), this logging appears...