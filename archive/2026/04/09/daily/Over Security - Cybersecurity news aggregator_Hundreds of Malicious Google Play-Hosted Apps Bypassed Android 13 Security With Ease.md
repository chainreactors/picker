---
title: Hundreds of Malicious Google Play-Hosted Apps Bypassed Android 13 Security With Ease
url: https://www.bitdefender.com/en-us/blog/labs/malicious-google-play-apps-bypassed-android-security
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:50.771960
---

# Hundreds of Malicious Google Play-Hosted Apps Bypassed Android 13 Security With Ease

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

9 min read

# Hundreds of Malicious Google Play-Hosted Apps Bypassed Android 13 Security With Ease

[![Alecsandru Cătălin DAJ](https://blogapp.bitdefender.com/labs/content/images/size/w100/2025/03/1000016262.jpg "Alecsandru Cătălin DAJ")](/en-us/blog/labs/author/alecsandru-daj "Alecsandru Cătălin DAJ")[![Adina MATEESCU](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/11/admateescu.jpeg "Adina MATEESCU")](/en-us/blog/labs/author/admateescu "Adina MATEESCU")[![Albert ENDRE-LASZLO](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/08/IMG_20200529_155527.jpg "Albert ENDRE-LASZLO")](/en-us/blog/labs/author/aendre "Albert ENDRE-LASZLO")[![Alex BACIU](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/08/20220817_120008.jpg "Alex BACIU")](/en-us/blog/labs/author/albaciu "Alex BACIU")[![Elena FLONDOR](https://blogapp.bitdefender.com/labs/content/images/size/w100/2020/11/eflondor.jpg "Elena FLONDOR")](/en-us/blog/labs/author/eflondor "Elena FLONDOR")

[Alecsandru Cătălin DAJ](/en-us/blog/labs/author/alecsandru-daj "Alecsandru Cătălin DAJ")[Adina MATEESCU](/en-us/blog/labs/author/admateescu "Adina MATEESCU")[Albert ENDRE-LASZLO](/en-us/blog/labs/author/aendre "Albert ENDRE-LASZLO")[Alex BACIU](/en-us/blog/labs/author/albaciu "Alex BACIU")[Elena FLONDOR](/en-us/blog/labs/author/eflondor "Elena FLONDOR")

March 18, 2025

  ![Hundreds of Malicious Google Play-Hosted Apps Bypassed Android 13 Security With Ease](https://blogapp.bitdefender.com/labs/content/images/size/w600/2025/03/Hand-holding-phone--security-app-on-screen-522371570_7360x4912.jpg "Hundreds of Malicious Google Play-Hosted Apps Bypassed Android 13 Security With Ease")

*Bitdefender's security researchers have identified a large-scale ad fraud campaign that deployed hundreds of malicious apps in the Google Play Store, resulting in more than 60 million downloads total. The apps display out-of-context ads and even try to persuade victims to give away credentials and credit card information in phishing attacks.*

The Google Play Store is often targeted by cybercriminals trying to upload malicious apps by bypassing existing protections. Google purges the store of such apps, either on its own volition or after being notified by researchers but criminals adapt.

This is one of the main reasons why it's  not enough for users to rely solely on the protection available by default on Android devices and the Google Play Store and why  Bitdefender  has dedicated technologies to address this  issue..

The technology embedded in Bitdefender Mobile Security, App Anomaly Detection, observes the apps’ behavior after installation, which is critical in today’s threat landscape. In some cases, bad actors alter the functionality of previously benign apps that had already been cleared for the Google Play Store, turning them into dangerous software.

Security researchers from IAS Threat Lab [uncovered](https://integralads.com/insider/ias-threat-lab-fraud-scheme-fake-android-apps/) a part of this campaign, exceeding 180 apps. However, the campaign is much larger, as Bitdefender's security researchers learned, and the dangers extend past what we usually observe. Criminals have used their access to devices to direct users towards phishing websites, not just to show them annoying full-screen ads.

## **Key findings**

* The campaign features at least 331 apps that were available via the Google Play Store (15 were still online when the research was completed), gathering more than 60 million downloads.
* Attackers figured out a way to hide the apps’ icons from the launcher, which is restricted on newer Android iterations.
* The apps have some functionality in most cases, but they can show out-of-context ads over other applications in the foreground, bypassing restrictions without using specific permissions that allow this behavior.
* Some apps have tried to collect user credentials for online services, and even credit card data, via phishing attacks.
* The apps can start without user interaction, even though this should not be technically possible in Android 13.
* The campaign seems to either be the work of one actor, or multiple criminals using the same packaging tool sold on black markets.

## **Insights and overview**

The investigated applications bypass Android security restrictions to start activities even if they are not running in the foreground and, without required permissions to do so, spam the users with continuous, fullscreen ads. The same behavior is used to serve UI elements featuring phishing attempts.

Application mimicking simple utility apps like:

* QR scanners
* Expense tracking apps
* Health apps
* Wallpaper apps
* Many others...

![](https://blogapp.bitdefender.com/labs/content/images/2025/03/data-src-image-1f332819-993c-4f35-b26a-8003bd89d426.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/03/data-src-image-54aadada-6faa-4081-bb20-e37d70df4fe9.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/03/image.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/03/Picture3_1.jpg)![](https://blogapp.bitdefender.com/labs/content/images/2025/03/Picture1_4.jpg)

## **Distribution by countries**

![](https://blogapp.bitdefender.com/labs/content/images/2025/03/image-2.png)

Most applications first became active on Google Play in Q3 2024. After further analysis, we saw that older ones that had been published earlier were initially benign and did not contain malware components. The malicious behavior was added afterward, starting with versions from the beginning of Q3.

To be clear, this is an active campaign. The latest malware published in the Google Play Store went live in the first week of March, 2025. When we finished the investigation, a week later, 15 applications were still available for download on Google Play.

Here are a couple from the latest batch uploaded to the store. Both of them were uploaded on March 4.

![](https://blogapp.bitdefender.com/labs/content/images/2025/03/Screenshot-2025-03-18-122722.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/03/Screenshot-2025-03-18-122806.png)![](https://blogapp.bitdefender.com/labs/content/images/2025/03/image-5.png)

## **Technical Overview**

**Running without user interaction:**

The application declares a [contact content provider](https://developer.android.com/reference/android/provider/ContactsContract.Directory) that is automatically queried by the system after the installation has been completed and the application entry point is loaded.

![](https://blogapp.bitdefender.com/labs/content/images/2025/03/image-6.png)

In some of the more recent samples, we noticed an evolution in criminals' methods to evade detection techniques by adding that type of content provider referenced as a string in resources. In previous iterations, it was directly referenced in the app's manifest.

![](https://blogapp.bitdefender.com/labs/content/images/2025/03/image-7.png)

This is likely one reason why our analysis has revealed so many more apps involved in this massive fraudulent campaign. Attackers often find ways to adapt when their methods are discovered, and apps are removed from the store.

**Icon hiding techniques:**

One way to keep a malicious app hidden from the user is to hide the icon – a behavior that is no longer allowed in the Android OS.

We notice that attackers used multiple approaches to solve this problem. The most popular and interesting one is also likely the most efficient. The app comes...