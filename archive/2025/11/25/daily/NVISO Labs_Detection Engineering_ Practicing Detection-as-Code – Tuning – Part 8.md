---
title: Detection Engineering: Practicing Detection-as-Code – Tuning – Part 8
url: https://blog.nviso.eu/2025/11/25/detection-engineering-practicing-detection-as-code-tuning-part-8/
source: NVISO Labs
date: 2025-11-25
fetch_date: 2025-11-26T03:15:37.808445
---

# Detection Engineering: Practicing Detection-as-Code – Tuning – Part 8

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Detection Engineering: Practicing Detection-as-Code – Tuning – Part 8

[Kristof Baute](https://blog.nviso.eu/author/kristof-baute/ "Posts by Kristof Baute")

[Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

November 25, 2025November 25, 2025
28 Minutes

This entry is part 8 in the series [Detection Engineering: Practicing Detection-as-Code](https://blog.nviso.eu/series/detection-engineering-practicing-detection-as-code/ "Detection Engineering: Practicing Detection-as-Code")

---

Detections should adapt to changes in the monitored environments. As organizations modify their infrastructure, through migrations, network reconfigurations, new systems or software, or deprecation of existing ones, detections require constant refinement to remain effective and maintain the alert queue at a manageable levels. Creating new detection rules involves researching, learning and understanding new tactics and techniques, problem-solving, and creative thinking to address the never-ending emerging threats. In contrast, tuning detections is a repetitive process that can feel mundane and less engaging by comparison.

![](https://blog.nviso.eu/wp-content/uploads/2025/09/image-16.png)

In Part 7, we showcased how we can leverage automation to continuously monitor the performance and trigger rate of our deployed detections. In this part, we are going to investigate how we can introduce automation and utilize continuous deployment pipelines to streamline the tedious task of tuning our detections. We’ll provide examples from Microsoft Sentinel, particularly its Watchlists functionality, but the concepts provided here apply to other SIEM platforms as well, since most of them come with similar features.

## Watchlists

Watchlists are custom data sets you can upload and use to enrich your detections, hunting, and investigations. For instance: if you have lists of high-privileged accounts, computer assets, IOCs, … you can upload them as a CSV file and reference them in your hunting rules or analytics. In this blog we will show how they can be used for tuning and filter-outs.

Under the hood, watchlist items are JSON objects that are added to a special Sentinel table “Watchlist”. The table is cached for query performance. You retrieve the elements in the watchlist by use of the *\_GetWatchlist()* function.

There are some limitations you need to be aware of. Watchlists are not intended for large data volumes. The maximum number of active watchlist items (all watchlists combined) is 10 million, and file uploads (a single watchlist) are limited to 3.8 MB. Think about this: if you have a watchlist of network ranges, one item would be about 40 bytes (an IP address in CIDR notation and a range name), meaning you can store 100K network ranges – that is a lot of ranges. For our tuning detections, these limits are sufficient. If you need bigger files, you can upload your files to Azure Storage, but this is outside the scope of this blog. Refer to the MS documentation if you need this.[1](#8ec8c6c9-2fcd-4046-bb37-739f62698ca4)

There is a retention period of 28 days. This can be confusing – it does not mean your watchlist items are deleted after 28 days. It means *deleted* items will be purged after 28 days. To keep the other items active, there is an automatic refresh interval of 12 days.

## Watchlist Management

Creating watchlists can be done via the Sentinel web interface. This process is straightforward: you provide a name, an alias and a search key, and you point to the CSV file containing the data. The alias is the name you will use in your queries to reference the watchlist. The name can be something else. We keep them identical but we can think of scenarios where they have different names. For instance, if you are an MSSP, you will deal with multiple watchlists, so it can be convenient to have specific names for the watchlist, e.g. Servers\_CustomerA, Servers\_CustomersB, … but in the rules you need a general reference, which then would be “Servers”.

![](https://blog.nviso.eu/wp-content/uploads/2025/09/image-51-1024x698.png)

Creation of Servers watchlist in Sentinel

The SearchKey is the name of the column that you intend to use in joins or lookups. It is designed for that use, to make the query more performant. Think about this when defining a watchlist. Most of the time, it will be the value that you want to use in your query.

Editing watchlists can also be done via the web interface; this is a straightforward process.

As this blog is about Detection-as-Code, we manage our watchlists programmatically. There are two APIs. There is an API to create and edit watchlists[2](#dc52eb66-2693-401b-b0fc-5a3d2666716d), and there is an API to create and edit watchlist items[3](#b84ee4b8-a078-4c32-8f3c-47fe22a07686).

A small warning here – It might be tempting to go for an approach where you just delete and re-upload a watchlist, after it has been changed. That seems simple indeed: you do not have to care about the different possible operations (update, delete or create) and it makes your integration very straightforward. However, Microsoft advises against this because there is a 5-minute SLA for data ingestion. This means that when you delete a watchlist and you recreate it, you might see both versions active, but more importantly: it is also possible there is no watchlist item at all during that time window. As a consequence, any rule running during that window will fail: it will miss bad stuff (if you use it for blocklisting) or it will generate false positives (if you use it for allowlisting).

![](https://blog.nviso.eu/wp-content/uploads/2025/09/image-48.png)

A possible workaround is to “hack” the *\_GetWatchlist()* function, so that it also retrieves items that have been deleted in the last 5 minutes, but we did not go that route. Instead, to sync the watchlists stored in our repository with the watchlists on Sentinel, we built a script (watchlist\_mgmt.py) that leverages Sentinel’s watchlist API to sync the watchlist items, without the need to delete and re-create watchlists or modify the *\_GetWatchlist()* function. We will be using that script later in an Azure DevOps pipeline to introduce some automation to the tuning process, but for now we will go through its functionality.

A screenshot of the API consumer code is provided below:

![](https...