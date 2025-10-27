---
title: Sustaining Digital Certificate Security - Upcoming Changes to the Chrome Root Store
url: http://security.googleblog.com/2025/05/sustaining-digital-certificate-security-chrome-root-store-changes.html
source: Google Online Security Blog
date: 2025-05-31
fetch_date: 2025-10-06T22:24:59.029435
---

# Sustaining Digital Certificate Security - Upcoming Changes to the Chrome Root Store

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Sustaining Digital Certificate Security - Upcoming Changes to the Chrome Root Store](https://security.googleblog.com/2025/05/sustaining-digital-certificate-security-chrome-root-store-changes.html "Sustaining Digital Certificate Security - Upcoming Changes to the Chrome Root Store")

May 30, 2025

Posted by Chrome Root Program, Chrome Security Team

*Note: Google Chrome communicated its removal of default trust of Chunghwa Telecom and Netlock in the public forum on May 30, 2025.*

The [Chrome Root Program Policy](https://googlechrome.github.io/chromerootprogram/) states that Certification Authority (CA) certificates included in the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md) must provide value to Chrome end users that exceeds the risk of their continued inclusion. It also describes many of the [factors](https://googlechrome.github.io/chromerootprogram/#51-incident-reports) we consider significant when CA Owners disclose and respond to incidents. When things don’t go right, we expect CA Owners to commit to meaningful and demonstrable change resulting in evidenced continuous improvement.

Chrome's confidence in the reliability of Chunghwa Telecom and Netlock as CA Owners included in the Chrome Root Store has diminished due to patterns of concerning behavior observed over the past year. These patterns represent a loss of integrity and fall short of expectations, eroding trust in these CA Owners as publicly-trusted certificate issuers trusted by default in Chrome. To safeguard Chrome’s users, and preserve the integrity of the [Chrome Root Store](https://security.googleblog.com/2023/05/how-chrome-root-program-keeps-users-safe.html#:~:text=Chrome%20uses%20digital,the%20%E2%80%9CWeb%20PKI.%E2%80%9D), we are taking the following action.

Upcoming change in Chrome 139 and higher:

* Transport Layer Security (TLS) server authentication certificates validating to the following root CA certificates whose earliest Signed Certificate Timestamp (SCT) is dated after July 31, 2025 11:59:59 PM UTC, will no longer be trusted by default.

+ [OU=ePKI Root Certification Authority,O=Chunghwa Telecom Co., Ltd.,C=TW](https://crt.sh/?q=c0a6f4dc63a24bfdcf54ef2a6a082a0a72de35803e2ff5ff527ae5d87206dfd5)
+ [CN=HiPKI Root CA - G1,O=Chunghwa Telecom Co., Ltd.,C=TW](https://crt.sh/?q=f015ce3cc239bfef064be9f1d2c417e1a0264a0a94be1f0c8d121864eb6949cc)
+ [CN=NetLock Arany (Class Gold) Főtanúsítvány,OU=Tanúsítványkiadók (Certification Services),O=NetLock Kft.,L=Budapest,C=HU](https://crt.sh/?q=6c61dac3a2def031506be036d2a6fe401994fbd13df9c8d466599274c446ec98)

* TLS server authentication certificates validating to the above set of roots whose *earliest* SCT is on or before **July 31, 2025 11:59:59 PM UTC,** will be unaffected by this change.

This approach attempts to minimize disruption to existing subscribers using a previously announced Chrome [feature](https://source.chromium.org/chromium/chromium/src/%2B/main%3Anet/cert/root_store.proto;drc=a783c3bab474ff68e675e2753f91c92ca817e072;l=15?q=f:root_store.proto&ss=chromium) to remove default trust based on the SCTs in certificates.

Additionally, should a Chrome user or enterprise [explicitly trust](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/faq.md#How-does-the-Chrome-Certificate-Verifier-integrate-with-platform-trust-stores-for-local-trust-decisions) any of the above certificates on a platform and version of Chrome [relying](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/faq.md#when-did-these-features-land) on the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md) (e.g., explicit trust is conveyed through a Group Policy Object on Windows), the SCT-based constraints described above will be overridden and certificates will function as they do today.

To further minimize risk of disruption, website operators are encouraged to review the “Frequently Asked Questions" listed below.

### Why is Chrome taking action?

CAs serve a privileged and trusted role on the internet that underpin encrypted connections between browsers and websites. With this tremendous responsibility comes an expectation of adhering to reasonable and consensus-driven security and compliance expectations, including those defined by the [CA/Browser Forum TLS Baseline Requirements](https://cabforum.org/working-groups/server/baseline-requirements/requirements/).

Over the past several months and years, we have observed a pattern of compliance failures, unmet improvement commitments, and the absence of tangible, measurable progress in response to publicly disclosed incident reports. When these factors are considered in aggregate and considered against the inherent risk each publicly-trusted CA poses to the internet, continued public trust is no longer justified.

### When will this action happen?

The action of Chrome, by default, no longer trusting new TLS certificates issued by these CAs will begin on approximately August 1, 2025, affecting certificates issued at that point or later.

This action will occur in Versions of [Chrome 139](https://chromiumdash.appspot.com/schedule) and greater on Windows, macOS, ChromeOS, Android, and Linux. Apple policies prevent the Chrome Certificate Verifier and corresponding Chrome Root Store from being used on Chrome for iOS.

### What is the user impact of this action?

By default, Chrome users in the above populations who navigate to a website serving a certificate from Chunghwa Telecom or Netlock issued **after** July 31, 2025 will see a full page interstitial [similar to this one](https://untrusted-root.badssl.com/).

Certificates issued by other CAs are not impacted by this action.

### How can a website operator tell if their website is affected?

Website operators can determine if they are affected by this action by using the Chrome Certificate Viewer.

Use the Chrome Certificate Viewer

* Navigate to a website (e.g., <https://www.google.com>)
* Click the “Tune" icon
* Click “Connection is Secure"
* Click “Certificate is Valid" (the Chrome Certificate Viewer will open)

+ **Website owner action is not required**, if the “Organization (O)” field listed beneath the “Issued By" heading **does not** contain “Chunghwa Telecom" , “行政院” , “NETLOCK Ltd.”, or “NETLOCK Kft.”
+ **Website owner action is required**, if the “Organization (O)” field listed beneath the “Issued By" heading contains “Chunghwa Telecom" , “行政院” , “NETLOCK Ltd.”, or “NETLOCK Kft.”

### What does an affected website operator do?

We recommend that affected website operators transition to a new publicly-trusted CA Owner as soon as reasonably possible. To avoid adverse website user impact, action **must** be completed **before** the existing certificate(s) expire if expiry is planned to take place **after** July 31, 2025.

While website operators could delay the impact of blocking action by choosing to collect and install a new TLS certificate issued from Chunghwa Telecom or Netlock before Chrome’s blocking action begins on August 1, 2025, website operators will inevitably need to collect and install a new TLS certificate from one of the many other CAs included in the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md).

### Can I test these changes before they take effect?

Yes.

A command-line flag was added beginning in Chrome 128 that allows administrators and power users to simulate the effect of an SCTNotAfter distrust constraint as described in this blo...