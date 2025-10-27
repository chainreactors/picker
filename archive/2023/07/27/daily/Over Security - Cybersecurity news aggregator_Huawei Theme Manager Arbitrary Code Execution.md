---
title: Huawei Theme Manager Arbitrary Code Execution
url: https://blog.doyensec.com//2023/07/26/huawei-theme-arbitrary-code-exec.html
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:56:30.276727
---

# Huawei Theme Manager Arbitrary Code Execution

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Huawei Theme Manager Arbitrary Code Execution

26 Jul 2023 - Posted by Luca Carettoni

Back in 2019, we were lucky enough to take part in the newly-launched [Huawei mobile bug bounty](https://techcrunch.com/2019/11/05/huawei-secret-bug-bounty-meeting/). For that, we decided to research [Huaweiâs Themes](https://consumer.huawei.com/en/mobileservices/themes/).

The Themes Manager allows custom themes on EMUI devices to stylize preferences, and the customization of lock screens, wallpapers and icons. Processes capable of making these types of system-wide changes need to have elevated privileges, making them valuable targets for research as well as exploitation.

### Background

When it comes to implementing a lockscreen on EMUI, there were three possible engines used:

* *com.ibimuyu.lockscreen*
* *com.vlife.huawei.emuilock*
* *com.huawei.ucdlockscreen*

When installing a theme, the `SystemUI.apk` verifies the signature of the application attempting to make these changes against a hardcoded list of trusted ones. From what we observed, this process seems to have been implemented properly, with no clear way to bypass the signature checks.

That said, we discovered that when `com.huawei.ucdlockscreen` was used, it loaded additional classes at runtime. The signatures of these classes were not validated properly, nor were they even checked. This presented an opportunity for us to introduce our own code.

Taking a look at the structure of the theme archive files (`.hwt`), we see that the unlock screen elements are packaged as follows:

![Archive Structure](../../../public/images/huawei_image_01.png)

Looking in the unlock directory, we saw the `theme.xml` file, which is a manifest specifying several properties. These settings included the dynamic unlock engine to use (`ucdscreenlock` in our case) and an `ext.properties` file, which allows for dynamic Java code loading from within the theme file.

Letâs look at the file content:

![Archive Structure](../../../public/images/huawei_image_02.png)

This instructs the dynamic engine (`com.huawei.ucdlockscreen`) to load `com.huawei.nova.ExtensionJarImpl` at runtime from the `NOVA6`LockScreen`2019120501.apk`. Since this class is not validated, we can introduce our own code to achieve arbitrary code execution. What makes this even more interesting is that our code will run within a process of a highly privileged application (`com.huawei.android.thememanager`), as shown below.

![Privileged Application List](../../../public/images/huawei_image_03.png)

Utilizing the logcat utility, we can see the dynamic loading process:

![Process Logs](../../../public/images/huawei_image_04.png)

This vulnerability was confirmed via direct testing on EMUI 9.1 and 10, but appears to impact the current version of EMUI with [some limitations\*](#exploitability).

![Theme in foreground with logcat in back](../../../public/images/huawei_image_05.png)

### Impact

As previously mentioned, this results in **arbitrary code execution** using the PID of a highly privileged application. In our testing, exploitation resulted in obtaining around 200 Android and Huawei custom permissions. Among those were the permissions listed below which could result in total compromise of the deviceâs user data, sensitive system data, any credentials entered into the system and the integrity of the systemâs environment.

![Permissions List](../../../public/images/huawei_image_06.png)

Considering that the application can send intents requiring the `huawei.android.permission.HW_SIGNATURE_OR_SYSTEM` permission, we believe it is possible to leverage existing system functionalities to obtain system level code execution. Once achieved, this vulnerability has great potential as part of a rooting chain.

### Exploitability

This issue can be reliably exploited with no technical impediments. That said, exploitation requires installing a custom theme. To accomplish this remotely, user interaction is required. We can conceive of several plausible social engineering scenarios which could be effective or perhaps use a second vulnerability to force the download and installation of themes.
Firstly, it is possible to gift themes to other users, so a compromised trusted contact could be leveraged (or spoofed) to convince a victim to accept and install the malicious theme.
As an example, the following URL will open the theme gift page: `hwt://www.huawei.com/themes?type=33&id=0&from=AAAA&channelId=BBB`

![Theme gifting attack flow](../../../public/images/huawei_image_07.png)

Secondly, an attacker could publish a link or QR code pointing to the malicious theme online, then convince a victim into triggering the `HwThemeManager` application via a deep link using the `hwt://` scheme.

To be fair, we must acknowledge that Huawei has a review process in place for new themes and wallpapers, which might limit the use of live themes exploiting this vulnerability.

### Partial fix

Huawei released an update for HwThemeManager on February 24, 2022 (internally tracked as HWPSIRT-2019-12158) stating this was resolved. Despite this, we believe the issue was actually resolved in `ucdlockscreen.apk` (`com.huawei.ucdlockscreen` version 3 and later).

This is an important distinction, because the latest version of the `ucdlockscreen.apk` is installed at runtime by HwThemeManager, after applying a theme that requires such an engine. Even on a stock phone (both EMUI 9,10 and latest 12.0.0.149), an attacker with physical access can uninstall the latest version and install the old vulnerable version since it is properly signed by Huawei.

Without further mitigations from Huawei, an attacker with physical access to the device can still leverage this vulnerability to gain system privileged access on even the latest devices.

### Further discovery

After a few hours of reverse engineering the fix introduced in the latest version of `com.huawei.ucdlockscreen` (version 4.6), we discovered an additional bypass impacting the EMUI 9.1 release. This issue doesnât require physical access and can again trigger the same exploitable condition.

During theme loading, the latest version of `com.huawei.ucdlockscreen` checks for the presence of a `/data/themes/0/unlock/ucdscreenlock/error` file. Since all of the files within `/data/themes/0/` are copied from the provided theme (`.hwt`) file they can all be attacker-controlled.

This file is used to check the specific version of the theme. An attacker can simply embed an error file referencing an older version, forcing legacy theme support. When doing so, an attacker would also specify a fictitious package name in the `ext.properties` file. This combination of changes in the malicious `.hwt` file bypasses all the required checks - making the issue exploitable again on the latest EMUI9.1, with no physical access required. At the time of our investigation, the other EMUI major versions appear to implement signature validation mechanisms to mitigate this.

### Disclosure

This issue was disclosed on Dec 31, 2019 according to the terms of the Huawei Mobile Bug Bounty, and it was addressed by Huawei as described above. Additional research results were reported to Huawei on Sep 1, 2021. Given the time that has elapsed from the original fix and the fact that we believe the issue is no longer remotely exploitable, we have decided to release the details of the vulnerability.

At the time of writing this post (April 28th...