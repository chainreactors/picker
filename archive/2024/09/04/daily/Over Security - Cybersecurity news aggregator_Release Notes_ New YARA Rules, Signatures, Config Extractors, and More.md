---
title: Release Notes: New YARA Rules, Signatures, Config Extractors, and More
url: https://any.run/cybersecurity-blog/release-notes-august-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-04
fetch_date: 2025-10-06T18:30:42.838148
---

# Release Notes: New YARA Rules, Signatures, Config Extractors, and More

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![Release Notes: New YARA Rules, Signatures, Config Extractors, and More ](/cybersecurity-blog/wp-content/uploads/2024/04/new_updates_blog.jpg)

[Service Updates](/cybersecurity-blog/category/service-updates/)

# Release Notes: New YARA Rules, Signatures, Config Extractors, and More

September 3, 2024

[Add comment](#comments-8756)
2320 views
3 min read

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: New YARA Rules, Signatures, Config Extractors, and More

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1381
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3018
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3025
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Service Updates](/cybersecurity-blog/category/service-updates/)

Release Notes: New YARA Rules, Signatures, Config Extractors, and More

Welcome to [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktolanding/)‘s monthly update, where we share what our team has been working on.

In August, we focused on enhancing our detection tools and improving your experience. We added the new XOR-URL extractor, updated YARA rules, added new signatures, and improved [network detection rules](https://any.run/cybersecurity-blog/detection-with-suricata-ids/).

Here’s a closer look at what we’ve done in August:

## New YARA rules

Our YARA rules have been refined and updated to improve detection accuracy for various malware families.

The newly added and updated rules now cover a broader spectrum of threats, including:

* [GoInjector](https://app.any.run/tasks/79ca0a73-24e4-4460-ae7a-e91db02cf4d9?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Luder](https://app.any.run/tasks/2dc53220-7d5a-4e16-b367-fa29ffed07f8?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Xdspyloader](https://app.any.run/tasks/878edf29-ddcd-4ca2-a257-09d325da4b09?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Guloader](https://app.any.run/tasks/581f2cff-6e83-494b-8541-55b296eb331f?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice) (with fixes)
* [DarkRoad](https://app.any.run/tasks/86ccc0dc-9a8c-4220-a57a-9a91cf2b9c09?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [PyInstaller](https://app.any.run/tasks/e6f43ed1-0561-4f8a-8cba-cdeb0a02dbd6/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [WannaCry](https://app.any.run/tasks/80d8884e-6a1d-4b02-8aea-fc830f9615ff/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice) (take a look at [WannaCry](https://any.run/malware-trends/wannacry) ransomware in our Malware Trends Tracker to get more IOCs)
* [MuddyRot](https://app.any.run/tasks/e3612b97-00ba-426b-a5e9-519e3c84f02a/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Phorpiex](https://app.any.run/tasks/9fea1c5a-3099-416c-bca0-6eca8240c342/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Onlineclipper](https://app.any.run/tasks/3754d88b-a40d-4304-9049-328cce88faad/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [MeshAgent](https://app.any.run/tasks/bf3439d9-614a-4cb9-ab7b-e25bbea6a898/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Prince](https://app.any.run/tasks/1e15e2f8-0a03-47ec-934f-7e502f582347/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Razr](https://app.any.run/tasks/6a4be23d-0c71-49c5-be9f-0cda10a83894/?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)
* [Snake Keylogger](https://app.any.run/tasks/34ef8bdb-f642-4808-b551-fe87df07d0f7?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice)  (updated)
* [Zusy](https://app.any.run/tasks/7f9431a5-dde4-42bf-b06c-207f24834eda?utm_source=anyrunblog&utm_medium=article&utm_campaign=release_notes_august24&utm_term=030924&utm_content=linktoservice) Ransomware
* [Luke](https://app.any.run/tasks/...