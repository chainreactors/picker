---
title: SAP HANA Cloud – Unlocking Performance Classes
url: https://blogs.sap.com/2023/07/28/sap-hana-cloud-unlocking-performance-classes/
source: SAP Blogs
date: 2023-07-29
fetch_date: 2025-10-04T11:52:55.649693
---

# SAP HANA Cloud – Unlocking Performance Classes

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP HANA Cloud - Unlocking Performance Classes

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164343&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP HANA Cloud - Unlocking Performance Classes](/t5/technology-blog-posts-by-sap/sap-hana-cloud-unlocking-performance-classes/ba-p/13569871)

![rittyjoseph](https://avatars.profile.sap.com/c/1/idc1f6db0e615886bc982f290a7c3fed009172ba334ecf63308c77bcb37d95eb7f_small.jpeg "rittyjoseph")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[rittyjoseph](https://community.sap.com/t5/user/viewprofilepage/user-id/152526)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164343)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164343)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569871)

‎2023 Jul 28
7:09 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164343/tab/all-users "Click here to see who gave kudos to this post.")

2,884

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520SAP%2520HANA%2520database/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP HANA Cloud, SAP HANA database

  Additional Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2BSAP%2BHANA%2Bdatabase/pd-p/ada66f4e-5d7f-4e6d-a599-6b9a78023d84)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (3)

**Introduction**

In the realm of cloud computing, the seamless delivery of services and applications relies heavily on maintaining an optimal balance between processing power and memory resources. Striking the right balance between these two components is crucial for achieving peak performance and cost-effectiveness. In this blog, we will delve into the flavors of the SAP HANA Cloud performance class offerings and it's significance on SAP HANA Cloud.

**Performance Classes and Core to Memory Ratios**

SAP HANA Cloud offers 4 performance classes with different core to memory ratios, each tailored to specific use case, which lets you allocate either more memory or more processing power to an SAP HANA Cloud instance.

The following performance classes are available on SAP HANA Cloud:

+ **Memory (Default)**: Default configuration, which is suitable for most workloads.

+ **High Memory**: Optimized to support the processing of large data sets that require a lot of memory.

+ **Compute:** Optimized to support compute-intensive workloads

+ **High Compute:** Optimized to support compute-intensive workloads that require less memory resources.

The core to memory ratio represents the relationship between the number of vCPUs and the size of the (compressed) in-memory data in your SAP HANA database which is allocated to an SAP HANA Cloud instance. Essentially, it measures the ratio of processing power to available memory, and it serves as a fundamental determinant of a system's capacity to handle workloads efficiently.

The maximum amount of memory depends on the hyperscaler and the region in which the instance is created. For more information, see [Memory and Storage Sizes Supported by SAP HANA Database](https://help.sap.com/docs/hana-cloud/sap-hana-cloud-administration-guide/memory-and-storage-sizes-supported-by-sap-hana-database).

The number of vCPUs cannot be set manually. It is allocated according to the size chosen at the time of provisioning the SAP HANA database instance.

For each hyperscaler the following tables show the different step sizes in which the memory is increased depending on the selected performance class.

**Memory (Default)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Hyperscaler** | **1 vCPU per 16 GB / 15 GB / 16 GB** | **4 vCPU per 64 GB / 60 GB / 64 GB** | **412 vCPUs / 440 vCPUs / 412 vCPUs** |
| Microsoft Azure | up to 960 GB | 960 GB – 1920 GB | 5600 GB |
| Amazon Web Services | up to 900 GB | 960 GB – 1800 GB | 5970 GB |
| Google Cloud | up to 1024GB | 1024 GB – 1344 GB | n/a |

**High Memory**

|  |  |  |
| --- | --- | --- |
| **Hyperscaler** | **120 vCPUs / 156 vCPUs** | **204 vCPUs** |
| Microsoft Azure | 3776 GB | 5955 GB |
| Amazon Web Services | 3600 GB | - |
| Google Cloud | 3700 GB | 5750 GB |

**Compute**

|  |  |
| --- | --- |
| **Hyperscaler** | **1 vCPU per 8 GB** |
| Microsoft Azure | 32 GB – 480 GB |
| Amazon Web Services | 32 GB – 912 GB |
| Google Cloud | 32 GB – 608 GB |

**High Compute**

|  |  |
| --- | --- |
| **Hyperscaler** | **120 vCPUs / 156 vCPUs** |
| Microsoft Azure | 32 GB – 360 GB |
| Amazon Web Services | 32 GB – 360 GB |
| Google Cloud | 32 GB – 296 GB |

The performance class of an already existing or new *SAP HANA Cloud, SAP HANA database* instance can be adjusted via self-service in the SAP HANA Cloud Central. Use the Performance Class slider to choose one of the four configurations that range from High Memory to High Compute.

![](/legacyfs/online/storage/blog_attachments/2023/07/DB.png)

*Adjusting Performance Class in SAP HANA Cloud Central*

**Conclusion**

The performance class is a critical factor in determining the performance and cost-efficiency of SAP HANA Cloud instances. Understanding the specific demands of your application workload and selecting the appropriate performance class with the right core to memory balance is essential for unlocking the full potential of SAP HANA Cloud.

As we continue to evolve, new optimizations may be introduced, offering even more tailored solutions for different workloads. Stay updated with [SAP HANA Cloud documentation](https://help.sap.com/docs/hana-cloud/sap-hana-cloud-administration-guide/sap-hana-database-size?q=max%20Instance%20sizes) and best practices to make informed decisions and ensure your SAP HANA cloud based applications thrive in the dynamic world of cloud computing.

**Please note**, that specifying or changing the performance class of an SAP HANA database instance is only supported via the new [Multi-Environment tooling](https://blogs.sap.com/2022/09/21/sap-hana-cloud-goes-multi-environment-part-2-getting-started/) of SAP HANA Cloud.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [Cloud](/t5/tag/Cloud/tg-p/board-id/technology-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fsap-hana-cloud-unlocking-performance-classes%2Fba-p%2F13569871%23comment-on-this)
...