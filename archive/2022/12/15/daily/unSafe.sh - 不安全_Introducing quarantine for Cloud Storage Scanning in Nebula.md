---
title: Introducing quarantine for Cloud Storage Scanning in Nebula
url: https://buaq.net/go-140062.html
source: unSafe.sh - 不安全
date: 2022-12-15
fetch_date: 2025-10-04T01:29:36.247104
---

# Introducing quarantine for Cloud Storage Scanning in Nebula

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/cdb6e203ddf2d31de335c524a8655a72.jpg)

Introducing quarantine for Cloud Storage Scanning in Nebula

We’re excited to announce quarantine for Malwarebytes Cloud Storage Sca
*2022-12-14 21:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-140062.htm)
阅读量:19
收藏*

---

We’re excited to announce quarantine for [Malwarebytes Cloud Storage Scanning (CSS)](https://www.malwarebytes.com/business/cloud-storage-scanning), a new feature which allows you to automatically quarantine threats found in your cloud storage repositories.

Malwarebytes Cloud Storage Scanning is an add-on service in Nebula that scans for malware on cloud storage repositories across supported cloud storage providers, using multiple anti-malware engines to monitor and protect the health of all your enterprise data.

By toggling on **Enable Quarantine** toggle in the Cloud Storage Scan configuration, malicious files are automatically quarantined to the configured folder. You can manage these detections from the **Storage Quarantine** page. For more information, see [Manage Cloud Storage Scanning quarantine in Nebula.](https://service.malwarebytes.com/hc/en-us/articles/10379213970067-Manage-Cloud-Storage-Scanning-quarantine-in-Nebula)

Let’s dive to learn more about how quarantine for Cloud Storage Scanning works.

## Configuring quarantine in a new Cloud Storage Scan

In Nebula, go to “**Settings**” and click “**Cloud Storage Scans**”. Here you can see existing scans and the providers being checked. Click “Add a Scan” to create a new scan. For our full article on how to configure Cloud Storage Scans in Nebula, [check our previous blog post](https://www.malwarebytes.com/blog/business/2022/08/introducing-malwarebytes-cloud-storage-scanning-how-to-scan-for-malware-in-cloud-file-storage-repositories).

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file18403_252202_e.png)

In the **Quarantine** tab, toggle **Enable Quarantine** on to automatically move detected malware to a selected user’s storage.

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file4328_252202_e.png)

Select a user to transfer all quarantined files to. A quarantine folder will be created in their cloud storage location.

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file45576_252202_e.png)

Quarantined files will no longer be accessible to original owners, collaborators, or others with access.

Select the default tombstone message or customize it. A **tombstone file** is created and replaces the original file when it is quarantined. The tombstone file is designed to provide information or instructions for users.

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file13797_252202_e.png)

## Manage Cloud Storage Scanning quarantine in Nebula

The **Cloud Storage Quarantine** page displays quarantined files from your cloud storage providers and allows you to manage them. Review the files detected by Cloud Storage Scans and moved to quarantine here.**![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file57778_252202_e.png)**

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file20266_252202_e.png)

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file38858_252202_e.png)

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file39789_252202_e.png)

To delete the file from quarantine, go to **Actions > Delete**. The file is sent to the administrator's trash in the cloud storage provider.

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file74912_252202_e.png)

![](https://www.malwarebytes.com/blog/business/2022/12/easset_upload_file20087_252202_e.png)

## Reduce risk from cloud-based malware, without slowing down your business.

Malwarebytes Cloud Storage Scanning (CSS) service enables Malwarebytes [IR/EP/EDR](https://www.malwarebytes.com/business/edr) customers to use our cloud-native Nebula console to detect (and now quarantine) threats across multi-vendor cloud storage repositories, such as Box and OneDrive.

With Malwarebytes CSS, customers gain centralized visibility across cloud storage repositories and the ability to generate reports to confirm the security of their cloud-stored data.

Learn more about CSS: <https://www.malwarebytes.com/business/cloud-storage-scanning>

### Further resources

#### [5 SaaS security best practices](https://www.malwarebytes.com/blog/business/2022/12/5-saas-security-best-practices)

#### [Cloud data breaches: 4 biggest threats to cloud storage security](https://www.malwarebytes.com/blog/business/2022/06/cloud-data-breaches-4-biggest-threats-to-cloud-storage-security)

#### [Benefits of a malware scanner for cloud storage](https://www.malwarebytes.com/cybersecurity/business/benefits-of-a-malware-scanner-for-cloud-storage)

#### [Cloud-based malware is on the rise. How can you secure your business?](https://www.malwarebytes.com/blog/business/2022/07/cloud-based-malware-is-on-the-rise-how-can-you-secure-your-business)

文章来源: https://www.malwarebytes.com/blog/business/2022/12/introducing-quarantine-for-cloud-storage-scanning-in-nebula
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)