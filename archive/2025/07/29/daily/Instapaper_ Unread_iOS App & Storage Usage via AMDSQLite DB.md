---
title: iOS App & Storage Usage via AMDSQLite DB
url: https://www.stark4n6.com/2025/07/ios-app-storage-usage-via-amdsqlite-db.html
source: Instapaper: Unread
date: 2025-07-29
fetch_date: 2025-10-06T23:58:15.818272
---

# iOS App & Storage Usage via AMDSQLite DB

[Skip to main content](#main)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKbEuDpbWt2h4R7y02WrWiCmAG90SxVmMkXsEXZE0k3gAACuFYgfUVuTHkKpfowS3WWbkh6XGjqMXh77QkxuZv0osjeusHJnR_ehrMU9r8RaAa3a2R61zmMgl3wLsGpQxSh7rCRX4oQEM/s1600/1947245.png)

Search

### Search This Blog

### iOS App & Storage Usage via AMDSQLite DB

Posted by

[Kevin Pagano](https://www.blogger.com/profile/13417965550116928863 "author profile")

[July 22, 2025](https://www.stark4n6.com/2025/07/ios-app-storage-usage-via-amdsqlite-db.html "permanent link")

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjCgWAU9HxTey6mh2eJ9Za8H9cGPT0_83eZ4OqZMFYKAsEt6MskZg0XX8E4kF3DZ3C_IoFpC-wQ0O9ShWM9jx8CPYAz-kLkqzWJN6acwYdyX50QkI7HH-2qpbOiLRtGyKpKsBXfvD0K6fFFEwCiSRHzBOEaDHdPvYpPtENEp8nt-M2PxTBqIrSMovO7EJ8=w640-h591)](https://blogger.googleusercontent.com/img/a/AVvXsEjCgWAU9HxTey6mh2eJ9Za8H9cGPT0_83eZ4OqZMFYKAsEt6MskZg0XX8E4kF3DZ3C_IoFpC-wQ0O9ShWM9jx8CPYAz-kLkqzWJN6acwYdyX50QkI7HH-2qpbOiLRtGyKpKsBXfvD0K6fFFEwCiSRHzBOEaDHdPvYpPtENEp8nt-M2PxTBqIrSMovO7EJ8)

I came across a short [research paper](https://www.researchgate.net/publication/393005242_Validity_of_foreground_application_in_AMDAppStoreUsageEvents_from_AMDSQLitedb0) that was recently published on ResearchGate from Ruud Schramp of the Netherlands Forensic Institute. He found a new possible evidence source in a SQLite database on iOS devices at path:

/private/var/mobile/Containers/Data/PluginKitPlugin/<GUID>/Documents/AMDSQLite.db.0\*

The tables of interest are:

* **AMDAppStoreUsageEvents** - app install/update dates and app foreground usage
* **DeviceStorageUsage** - shows free storage capacity at certain intervals
* **AMDAppStoreAnalyticsData** - app info and feeds via the App Store app

## **AMDAppStoreUsageEvents**

This is the meat of what Ruud's paper looks at. This table records app events that show when an app was installed or updated as well as when the app was opened to the foreground and for how long.

* time - timestamp of the event
* creationTime - another timestamp which I thought calculated duration but still needs more research
* type - type of event occurring,

+ 0 = Install/Update,
+ 1 = Uninstall
+ 2 = Open or run
+ 3 = TBD

* adamId - Apple store identifier for an application
* appVersion - version number of the application
* foregroundDuration - how long the app was in the foreground in seconds
* userId - unique identifier to the user opening the apps

We don't directly get the app names here but we do get adamIDs which I've seen before in the [storeUser.db](https://www.stark4n6.com/2025/04/tracking-ios-app-installs-and-purchase.html). If we pull in an attach that database here we can get bundle names to correlate with the adamIDs. We can also match the userId to an Apple ID found in storeUser as well.gm

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhIQhZAPQJTQrLIeHyHK1yWHHZo4Bb-OC-XSRyWicP_9IsbvvmBWElUyVWUnMK0DtyaB4iujEgIGAZp3WVC7ICNG1AEJ5CRHKQd5hhCxboB8jgm0Ou53Zdlajexd5DhWNO7mnMQ1M1vTnzNBiLkuF8V0Vkm6YpH8gZzkPLU6P6rivWypnDx5_lQ6EIpJ7E=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhIQhZAPQJTQrLIeHyHK1yWHHZo4Bb-OC-XSRyWicP_9IsbvvmBWElUyVWUnMK0DtyaB4iujEgIGAZp3WVC7ICNG1AEJ5CRHKQd5hhCxboB8jgm0Ou53Zdlajexd5DhWNO7mnMQ1M1vTnzNBiLkuF8V0Vkm6YpH8gZzkPLU6P6rivWypnDx5_lQ6EIpJ7E)

***Figure 1: AMDAppStoreUsageEvents query in DB Browser***

From Josh Hickman's iOS 17 image we can see a sample of Signal activity lines up almost exactly (given local to UTC offset conversion).

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjp0D-sLzM3VmZeHl_oTwsb6aFipHp39091dfb2tLeZr6y3PRhaP6e5Ma5Iucj4olkcyqTy57xWJwTcbJSyKEaNo_fBw8jjkCF3ZV_ZhuJxYcShwFAN5SO_2zPHBHQspXQn2mjgqITzPnfPaFrfi5yqGniI3Z5B3Xyb8pGlhEL8IaoPrJ6dTtYzTCA55XM=w640-h520)](https://blogger.googleusercontent.com/img/a/AVvXsEjp0D-sLzM3VmZeHl_oTwsb6aFipHp39091dfb2tLeZr6y3PRhaP6e5Ma5Iucj4olkcyqTy57xWJwTcbJSyKEaNo_fBw8jjkCF3ZV_ZhuJxYcShwFAN5SO_2zPHBHQspXQn2mjgqITzPnfPaFrfi5yqGniI3Z5B3Xyb8pGlhEL8IaoPrJ6dTtYzTCA55XM)

***Figure 2: iOS 17 image creation documentation from Josh Hickman***

## **DeviceStorageUsage**

In this simple table we get some indicators of capacity used for the phone itself.

* time - timestamp of the event
* creationTime - appears to be duplicative of time in this table instance
* availableDeviceCapacityGB - amount of GB free space
* totalDeviceCapacityGB - total amount of GB on the device

Maybe this would be helpful to have for an examiner to show usage over time.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj_P7bkTCSA0MC95Uard-VAqqmV8mL8IiO-8D0rLjg2T_mVALkKc4EEsFIZvqYUbQU6ITsYVdo55vE21xWbQmzKlWreQTHJ6rZDrQx90XTky1WbOOKKEDKmtC56Q3sd9_O_CT_9onWYEUPudpaVb2WO6n1BMjiHzmOgZwiqsLcphhyFrbCoNu3NrMDdGRo=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEj_P7bkTCSA0MC95Uard-VAqqmV8mL8IiO-8D0rLjg2T_mVALkKc4EEsFIZvqYUbQU6ITsYVdo55vE21xWbQmzKlWreQTHJ6rZDrQx90XTky1WbOOKKEDKmtC56Q3sd9_O_CT_9onWYEUPudpaVb2WO6n1BMjiHzmOgZwiqsLcphhyFrbCoNu3NrMDdGRo)

***Figure 3: Device capacity over time in DB Browser***

## AMDAppStoreAnalyticsData

This table shows information and suggested content straight from the Apple App Store application such as the Today page and trending apps. In my limited testing there appears to be some information related to searches and download/redownload events of apps.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjDhIqTxTrKPJ9ERQ9YlpcOcsZLO3svQhw6e_Icbe2kdwBaVHEz3ZkDXgrtCmvERUhreOgw08RusTSVJHPkmNj4KlDZFcOsB3B8d1_7ZhjBsXm5ZH-qJCV8a3ZjqQM1nO9gCaWZJKnHopbN5HVDYty6Ok2Bbommw99QDxXYG6-H_h-ukwXN1IsdY_jee8Y=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEjDhIqTxTrKPJ9ERQ9YlpcOcsZLO3svQhw6e_Icbe2kdwBaVHEz3ZkDXgrtCmvERUhreOgw08RusTSVJHPkmNj4KlDZFcOsB3B8d1_7ZhjBsXm5ZH-qJCV8a3ZjqQM1nO9gCaWZJKnHopbN5HVDYty6Ok2Bbommw99QDxXYG6-H_h-ukwXN1IsdY_jee8Y)

***Figure 4: AMDAppStoreAnalyticsData table***

One of the original motivations why [I created ASP](https://github.com/stark4n6/ASP-Search) is to look up these adamIDs here. I am in the process of implementing possible code to this parser but work is ongoing. More research to follow for this table.

For now, parsers for the App Usage and Storage capacity events have been implemented into [iLEAPP](https://github.com/abrignoni/iLEAPP).

[AMDSQLite](https://www.stark4n6.com/search/label/AMDSQLite)
[Apple](https://www.stark4n6.com/search/label/Apple)
[Apple Store](https://www.stark4n6.com/search/label/Apple%20Store)
[iOS](https://www.stark4n6.com/search/label/iOS)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_rv98XOSpQWTx_-D_OwQHINXes6_8Q4J2QRmauiB7JMXfh6dp50JzZY1zhNlD0O0yYr01eKAj2jcAFv1S06jcx2ifxvmj1Pm18gESACkCmMdSldHhX_EO_prxaQJoeQ6FuCjeXLNkb0g/s150/FullColor_1024x1024_300dpi.jpg)

### Archive

* [September 20251](https://www.stark4n6.com/2025/09/)
* [August 20251](https://www.stark4n6.com/2025/08/)
* [July 20254](https://www.stark4n6.com/2025/07/)
* [June 20252](https://www.stark4n6.com/2025/06/)
* [April 20252](https://www.stark4n6.com/2025/04/)
* [March 20259](https://www.stark4n6.com/2025/03/)
* [February 20251](https://www.stark4n6.com/2025/02/)
* [January 20252](https://www.stark4n6.com/2025/01/)
* [December 20242](https://www.stark4n6.com/2024/12/)
* [October 20241](https://www.stark4n6.com/2024/10/)

* [May 20241](https://www.stark4n6.com/2024/05/)
* [April 20242](https://www.stark4n6.com/2024/04/)
* [March 20244](https://www.stark4n6.com/2024/03/)
* [February 20241](https://www.stark4n6.com/2024/02/)
* [January 20243](https://www.stark4n6.com/2024/01/)
* [December 20231](https://www.stark4n6.com/2023/12/)
* [October 20233](https://www.stark4n6.com/2023/10/)
* [September 20232](https://www.stark4n6.com/2023/09/)
* [August 20232](https://www.stark4n6.com/2023/08/)
* [July 20231](https://www.stark4n6.com/2023/07/)
* [June 20232](https://www.stark4n6.com/2023/06/)
* [May 20235](https://www.stark4n6.com/2023/05...