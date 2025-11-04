---
title: Researchers Uncover BankBot-YNRK and DeliveryRAT Android Trojans Stealing Financial Data
url: https://thehackernews.com/2025/11/researchers-uncover-bankbot-ynrk-and.html
source: The Hacker News
date: 2025-11-03
fetch_date: 2025-11-04T03:11:35.226920
---

# Researchers Uncover BankBot-YNRK and DeliveryRAT Android Trojans Stealing Financial Data

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Uncover BankBot-YNRK and DeliveryRAT Android Trojans Stealing Financial Data](https://thehackernews.com/2025/11/researchers-uncover-bankbot-ynrk-and.html)

**Nov 03, 2025**Ravie LakshmananMalware / Mobile Security

[![Android](data:image/png;base64... "Android")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4Tt56UVzOmPmMb8bx8CdK2PZTnThikELcwApmVlEElJPqMdbGur-t2k_JEGRXo_sWqNkLG6TVRUUWKlMnhS_xQ4Tpzwp-CPqaEpn_n8PIEn11MyTpBmpsDDI8nEKBAeZ_NjWQ_hVPRjJHuSsc4xoZiG9II5fpf9mWE80YZd_-5-SDbHKtgoocG8I6qiBx/s790-rw-e365/android.jpg)

Cybersecurity researchers have shed light on two different Android trojans called **BankBot-YNRK** and **DeliveryRAT** that are capable of harvesting sensitive data from compromised devices.

According to CYFIRMA, which [analyzed](https://www.cyfirma.com/research/investigation-report-android-bankbot-ynrk-mobile-banking-trojan/) three different samples of BankBot-YNRK, the malware incorporates features to sidestep analysis efforts by first checking its running within a virtualized or emulated environment, and then extracting device details such as the manufacturer and model name to ascertain if it's being executed on a real device.

BankBot-YNRK also checks if the device is manufactured by Oppo, or is running on ColorOS, a version of the Android operating system that's used on devices made by the Chinese original equipment manufacturer (OEM).

"The malware also includes logic to identify specific devices," CYFIRMA said. "It verifies whether the device is a Google Pixel or a Samsung device and checks if its model is included in a predefined list of recognized or supported models. This allows the malware to apply device-specific functionality or optimizations only on targeted devices while avoiding execution on unrecognized models."

The names of the APK packages distributing the malware are listed below. All three apps go by the name "IdentitasKependudukanDigital.apk," which likely appears to be an attempt to impersonate a [legitimate Indonesian government app](https://play.google.com/store/apps/details?id=gov.dukcapil.mobile_id&hl=en-US) called "Identitas Kependudukan Digital."

* com.westpacb4a.payqingynrk1b4a
* com.westpacf78.payqingynrk1f78
* com.westpac91a.payqingynrk191a

Once installed, the malicious apps are designed to harvest device information and set the volume of various audio streams, such as music, ringtone, and notifications, to zero to prevent the affected victim from being alerted to incoming calls, messages, and other in-app notifications.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

It also establishes communication with a remote server ("ping.ynrkone[.]top"), and upon receiving the "OPEN\_ACCESSIBILITY" command, it urges the user to enable [accessibility services](https://thehackernews.com/2024/09/trickmo-android-trojan-exploits.html) so as to realize its goals, including gaining elevated privileges and performing malicious actions.

The malware, however, is capable of targeting only Android devices running versions 13 and below, as Android 14, launched in late 2023, introduced a new security feature that prevents the use of accessibility services to automatically request or grant app additional permissions.

"Until Android 13, apps could bypass permission requests through accessibility features; however, with Android 14, this behavior is no longer possible, and users must grant permissions directly through the system interface," CYFIRMA said.

BankBot-YNRK leverages Android's JobScheduler service to establish persistence on the device and ensure it's launched after a reboot. It also supports a wide range of commands to gain device administrator privileges, manage apps, interact with the device, redirect incoming calls using MMI codes, take photos, perform file operations, and harvest contacts, SMS messages, locations, lists of installed apps, and clipboard content.

Some of the other features of the malware are as follows -

* Impersonating Google News by programmatically replacing the apps's name and icons, as well as launching "news.google[.]com" via a WebView
* Capture screen content to reconstruct a "skeleton UI" of application screens such as banking apps to facilitate credential theft
* Abusing accessibility services to open cryptocurrency wallet apps from a predefined list and automating UI actions to gather sensitive data and initiate unauthorized transactions
* Retrieving a list of 62 financial apps to target
* Displaying an overlay message claiming their personal information is being verified, while the malicious actions are carried out, including requesting itself extra permissions and adding itself as a device administrator app

"BankBot-YNRK exhibits a comprehensive feature set aimed at maintaining long-term access, stealing financial data, and executing fraudulent transactions on compromised Android devices," CYFIRMA said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj58um41ybJcBY39DuWC1DJUh_vSWz8jUBbIXl9eFDqLFhJEPm49KTir2HQggJnXYp6IOV6EcjKLjoZ6J_CG66KTgR9EoGs2CGgweT4ZuXPaBiOSUiRnidPRvNt_6SYVv52q9yOmmC2yq5U_VVY3cf-Vx-kRf6nNJB_CME0ao3fNNJnrJYNOG0lcZuTN8O9/s790-rw-e365/wallets.jpg)

The disclosure comes as F6 [revealed](https://www.f6.ru/blog/android-deliveryrat-research/) that threat actors are distributing an updated version of DeliveryRAT targeting Russian Android device owners under the guise of food delivery services, marketplaces, banking services, as well as parcel tracking applications. The mobile threat is assessed to be active since mid-2024.

According to the Russian cybersecurity company, the malware is [advertised](https://www.f6.ru/blog/android-troyan-deliveryrat/) under a malware-as-a-service (MaaS) model through a Telegram bot named Bonvi Team, allowing users to either get access to an APK file or links to phishing pages distributing the malware.

Victims are then approached on messaging apps like Telegram, where they are asked to download the malicious...