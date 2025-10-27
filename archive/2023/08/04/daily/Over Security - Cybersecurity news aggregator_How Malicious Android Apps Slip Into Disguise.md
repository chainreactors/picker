---
title: How Malicious Android Apps Slip Into Disguise
url: https://krebsonsecurity.com/2023/08/how-malicious-android-apps-slip-into-disguise/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-04
fetch_date: 2025-10-04T12:03:40.109881
---

# How Malicious Android Apps Slip Into Disguise

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# How Malicious Android Apps Slip Into Disguise

August 3, 2023

[15 Comments](https://krebsonsecurity.com/2023/08/how-malicious-android-apps-slip-into-disguise/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/grandroidude.png)

Researchers say mobile malware purveyors have been abusing a bug in the **Google Android** platform that lets them sneak malicious code into mobile apps and evade security scanning tools. Google says it has updated its app malware detection mechanisms in response to the new research.

At issue is a mobile malware obfuscation method identified by researchers at [ThreatFabric](https://www.threatfabric.com), a security firm based in Amsterdam. **Aleksandr Eremin**, a senior malware analyst at the company, told KrebsOnSecurity they recently encountered a number of mobile banking trojans abusing a bug present in all Android OS versions that involves corrupting components of an app so that its new evil bits will be ignored as invalid by popular mobile security scanning tools, while the app as a whole gets accepted as valid by Android OS and successfully installed.

“There is malware that is patching the .apk file [the app installation file], so that the platform is still treating it as valid and runs all the malicious actions it’s designed to do, while at the same time a lot of tools designed to unpack and decompile these apps fail to process the code,” Eremin explained.

Eremin said ThreatFabric has seen this malware obfuscation method used a few times in the past, but in April 2023 it started finding many more variants of known mobile malware families leveraging it for stealth. The company has since attributed this increase to a semi-automated malware-as-a-service offering in the cybercrime underground that will obfuscate or “crypt” malicious mobile apps for a fee.

Eremin said Google flagged their initial May 9, 2023 report as “high” severity. More recently, Google awarded them a $5,000 bug bounty, even though it did not technically classify their finding as a security vulnerability.

“This was a unique situation in which the reported issue was not classified as a vulnerability and did not impact the Android Open Source Project (AOSP), but did result in an update to our malware detection mechanisms for apps that might try to abuse this issue,” Google said in a written statement.

Google also acknowledged that some of the tools it makes available to developers — including [APK Analyzer](https://developer.android.com/tools/apkanalyzer) — currently fail to parse such malicious applications and treat them as invalid, while still allowing them to be installed on user devices.

“We are investigating possible fixes for developer tools and plan to update our documentation accordingly,” Google’s statement continued.

![](https://krebsonsecurity.com/wp-content/uploads/2023/08/tf-apk.png)

According to ThreatFabric, there are a few telltale signs that app analyzers can look for that may indicate a malicious app is abusing the weakness to masquerade as benign. For starters, they found that apps modified in this way have [Android Manifest files](https://maldr0id.blogspot.com/2014/09/having-fun-with-androidmanifestxml.html) that contain newer timestamps than the rest of the files in the software package.

More critically, the Manifest file itself will be changed so that the number of “strings” — plain text in the code, such as comments — specified as present in the app does match the actual number of strings in the software.

One of the mobile malware families known to be abusing this obfuscation method has been dubbed **Anatsa**, which is a sophisticated Android-based banking trojan that typically is disguised as a harmless application for managing files. Last month, ThreatFabric [detailed](https://www.threatfabric.com/blogs/anatsa-hits-uk-and-dach-with-new-campaign) how the crooks behind Anatsa will purchase older, abandoned file managing apps, or create their own and let the apps build up a considerable user base before updating them with malicious components.

ThreatFabric says Anatsa poses as PDF viewers and other file managing applications because these types of apps already have advanced permissions to remove or modify other files on the host device. The company estimates the people behind Anatsa have delivered more than 30,000 installations of their banking trojan via ongoing Google Play Store malware campaigns.

Google has come under fire in recent months for failing to more proactively police its Play Store for malicious apps, or for once-legitimate applications that later go rogue. [This May 2023 story](https://arstechnica.com/information-technology/2023/05/app-with-50000-google-play-installs-sent-attackers-mic-recordings-every-15-minutes/) from *Ars Technica* about a formerly benign screen recording app that turned malicious after garnering 50,000 users notes that Google doesn’t comment when malware is discovered on its platform, beyond thanking the outside researchers who found it and saying the company removes malware as soon as it learns of it.

“The company has never explained what causes its own researchers and automated scanning process to miss malicious apps discovered by outsiders,” Ars’ **Dan Goodin** wrote. “Google has also been reluctant to actively notify Play users once it learns they were infected by apps promoted and made available by its own service.”

The Ars story mentions one potentially positive change by Google of late: A preventive measure available in Android versions 11 and higher that implements “app hibernation,” which puts apps that have been dormant into a hibernation state that removes their previously granted runtime permissions.

*This entry was posted on Thursday 3rd of August 2023 07:22 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Aleksandr Eremin](https://krebsonsecurity.com/tag/aleksandr-eremin/) [Anatsa](https://krebsonsecurity.com/tag/anatsa/) [Android malware](https://krebsonsecurity.com/tag/android-malware/) [Ars Technica](https://krebsonsecurity.com/tag/ars-technica/) [Google Play](https://krebsonsecurity.com/tag/google-play/) [ThreatFabric](https://krebsonsecurity.com/tag/threatfabric/)

Post navigation

[← Russia Sends Cybersecurity CEO to Jail for 14 Years](https://krebsonsecurity.com/2023/07/russia-sends-cybersecurity-ceo-to-jail-for-14-years/)
[Teach a Man to Phish and He’s Set for Life →](https://krebsonsecurity.com/2023/08/teach-a-man-to-phish-and-hes-set-for-life/)

## 15 thoughts on “How Malicious Android Apps Slip Into Disguise”

1. Steven Hebert [August 3, 2023](https://krebsonsecurity.com/2023/08/how-malicious-android-apps-slip-into-disguise/#comment-589150)

   Are there any recommendations for current Android users?

   Was this bug patched in the July security update?

   I just checked my Android and was still on the June 2023 security update and July 2023 was available.

   1. Tim Cook [August 3, 2023](https://krebsonsecurity.com/2023/08/how-malicious-android-apps-slip-in...