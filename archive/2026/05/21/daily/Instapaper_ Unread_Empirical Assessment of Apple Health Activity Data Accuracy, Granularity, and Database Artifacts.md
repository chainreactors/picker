---
title: Empirical Assessment of Apple Health Activity Data Accuracy, Granularity, and Database Artifacts
url: https://metadataperspective.com/2026/05/19/empirical-assessment-of-apple-health-activity-data-accuracy-granularity-and-database-artifacts/
source: Instapaper: Unread
date: 2026-05-21
fetch_date: 2026-05-22T06:08:38.632494
---

# Empirical Assessment of Apple Health Activity Data Accuracy, Granularity, and Database Artifacts

[Skip to content](#wp--skip-link--target)

![](https://metadataforensics.files.wordpress.com/2023/06/largebanner.png?w=1024)

***Behind the Bytes: Exploring the World of Digital Forensics Incident Response***

May 19, 2026

## Empirical Assessment of Apple Health Activity Data: Accuracy, Granularity, and Database Artifacts

**Synopsis:**

For nearly ten years, Apple Health data has played a role in significant criminal investigations, prompting ongoing and crucial discussions about its dependability and precision. One of the earliest documented instances of Apple Health data as evidence was during the 2018 trial of Hussein Khavari, accused of the rape and murder of Maria Ladenburger in 2016. Investigators noted Flights Climbed activity from Khavari’s Apple Health app, correlating it with the movement needed to ascend the riverbank after allegedly disposing of the victim’s body in the Dreisam River. Police later corroborated this finding by replicating the activity, reviewing the Apple Health data, and correlating the data with geolocation and timeline evidence from the case (BBC News, 2018). More recently, in the 2023 Alex Murdaugh double-murder trial, prosecutors presented data from Maggie Murdaugh’s iPhone Health app, which recorded 38 steps between 8:17:41 and 8:18:29 p.m. on June 7, 2021, shortly after her phone was disconnected from a charger (The Trial Channel, 2025). In the Karen Read murder retrial, defense attorneys pointed to 36 steps (approximately 25.46 meters) logged on victim John O’Keefe’s iPhone after he was reportedly left outside the Albert residence (Czajkowski, 2026). These examples illustrate how Apple Health data can powerfully reconstruct timelines and physical activity and aid in building a fuller, more reliable forensic picture when combined with additional case evidence and details. This article will detail the location of Apple Health application database files within Apple iPhone extractions, evaluate Apple Health data against established benchmarks (including direct comparisons of the healthdb\_secure.sqlite and cache\_encryptedC.db databases), and present the findings regarding its reliability and accuracy.

**Forensic Questions:**

In relation to Apple Health data, the cache\_encryptedC.db is said to be far more granular than the healthdb\_secure.sqlite for Steps, Walking + Running Distance, and Flights Climbed. What additional data can be obtained from these databases and how accurate is the data from either database in relation to Steps, Walking + Running Distance, and Flights Climbed (or stairs ascended / descended)?

**Apple iPhone Model / OS Version:**

Apple iPhone 8, iOS 15.0.2

Apple iPhone SE (2nd Gen), iOS 26.0

**Tools:**

DB Browser for SQLite Version 3.13.1 on Windows 11 Pro, 25H2, referred to as “DB Browser” within this work.

**Location of Health Database Files:**

Within this article, we will be reviewing data from two databases. The first is the healthdb\_secure.sqlite, located at /private/var/mobile/Library/Health/ within a Full File System Extraction. The Health folder stores both the healthdb\_secure.sqlite database as well as the healthdb.sqlite. The healthdb.sqlite holds additional beneficial data for the current OS version, product type name, and other paired source devices. Notably, both databases can also be obtained through an Advanced Logical File System Extraction (Encrypted) or even an Apple iTunes Encrypted Backup, though both means require decryption for data review.

The second database we will be reviewing is the cache\_encryptedC.db, located at /private/var/root/Library/Caches/locationd/ within a Full File System Extraction. This database is not obtained through other extraction means beyond the Full File System Extraction or an After First Unlock Extraction.

**Review of Data Storage:**

The healthdb\_secure.sqlite stores data for Steps, Walking + Running Distance, and Flights Climbed within two tables: samples and quantity\_samples. Joining these tables by the data\_id and using the appropriate WHERE clause provides the beginning timestamp, ending timestamp, and the quantity of the measurement, i.e., 23 steps. *Note: This article will not cover SQL queries.*

**Steps:**

![](https://metadataperspective.com/wp-content/uploads/2026/05/image.png?w=621)

Figure 1: Example of Steps data stored in the healthdb\_secure.sqlite database on an Apple iPhone running iOS 26.0, displayed using DB Browser. The figure illustrates the use of start\_date and end\_date timestamps and the associated quantity value representing the number of recorded Steps.

Timestamp values, start\_date and end\_date are Apple Cocoa Core Data timestamps, or Mac Absolute Time, and are the number of seconds since January 1, 2001. Steps are data\_type 7 and our quantity value is the number of steps recorded, or 23 as depicted in Figure 1. Apple defines Steps as “the number of steps you take throughout the day. Pedometers and digital activity trackers can help you determine your step count. These devices count steps for any activity that involves step-like movement, including walking, running, stair-climbing, cross-country skiing, and even movement as you go about your daily chores” (Apple Inc., n.d.).

**Walking + Running Distance:**

![](https://metadataperspective.com/wp-content/uploads/2026/05/image-2.png?w=622)

Figure 2: Example of Walking + Running Distance data stored in the healthdb\_secure.sqlite database on an Apple iPhone running iOS 26.0, displayed using DB Browser. The figure shows corresponding start\_date and end\_date timestamps and the recorded distance value expressed in meters.

Consistent with Steps data, start\_date and end\_date values are present. Walking + Running Distance is data\_type 8 and our quantity value is the distance in meters, or 13.7593427104875 m as depicted in Figure 2. Apple does not define Walking + Running Distance in the same manner they define Steps; however, it does define a related metric, distanceWalkingRunning, as “A quantity sample type that measures the distance the user has moved by walking or running” (Apple Inc., n.d.).

Using a simple SQL query, we can review the beginning and ending timestamps for our Steps and Walking + Running Distance together:

![](https://metadataperspective.com/wp-content/uploads/2026/05/image-1.png?w=540)

Figure 3: Example of the results of a SQL query combining Steps and Walking + Running Distance records from the healthdb\_secure.sqlite database, illustrating the aligned start\_date and end\_date timestamps for these activities. This figure is displayed using DB Browser.

**Flights Climbed:**

![](https://metadataperspective.com/wp-content/uploads/2026/05/image-4.png?w=623)

Figure 4: Example of Flights Climbed data stored in the healthdb\_secure.sqlite database on an Apple iPhone running iOS 26.0, displayed using DB Browser. The figure displays the start\_date and end\_date timestamps associated with a recorded flight of stairs climbed, with the corresponding quantity value.

Again, start\_date and end\_date values are present. Flights Climbed is data\_type 12 and the quantity value is the number of flights climbed, or 1 flight climbed as depicted in Figure 4. Apple defines Flights Climbed as “A flight of stairs is counted as approximately 10 feet (3 meters) of elevation gain (approximately 16 steps)” (Apple Inc., n.d.).

Using a simple SQL query, we can review the beginning and ending timestamps for our Flights Climbed:

![](https://metadataperspective.com/wp-content/uploads/2026/05/image-2-2.png?w=412)

Figure 5: Example of the results of a SQL query for Flights Climbed data from the healthdb\_secure.sqlite database, showing the left and right limit time bounds and the number of recorded flights climbed. This figure is displayed using DB Browser.

While the healthdb\_secure.sqlite stores data for Steps, Walking + Running Distance, and Flights Climbed in a clearcut manner, obtained through basic SQL queries, the cache\_encryptedC.db data st...