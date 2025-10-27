---
title: WebDAV-as-a-Service: Uncovering the infrastructure behind Emmenhtal loader distribution
url: https://blog.sekoia.io/webdav-as-a-service-uncovering-the-infrastructure-behind-emmenhtal-loader-distribution/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-20
fetch_date: 2025-10-06T18:30:05.657847
---

# WebDAV-as-a-Service: Uncovering the infrastructure behind Emmenhtal loader distribution

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# WebDAV-as-a-Service: Uncovering the infrastructure behind Emmenhtal loader distribution

This blogpost examines the use of WebDAV technology in hosting malicious files related to the Emmenhtal loader, then analyses the various final payloads delivered through this infrastructure, and concludes by exploring the possibility that...

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Marc N. and Sekoia TDR](#molongui-disabled-link)
September 19 2024

0

6 minutes reading

*This report was originally published for our customers on 30 August 2024.*

## Table of contents

* [Introduction](#h-introduction)
* [Use of WebDAV technology for malicious file hosting](#h-use-of-webdav-technology-for-malicious-file-hosting)
* [Detailed analysis of malware delivered via WebDAV](#h-detailed-analysis-of-malware-delivered-via-webdav)
* [Infrastructure assumptions and observations](#h-infrastructure-assumptions-and-observations)
* [Conclusion](#h-conclusion)
* [IOCs](#h-iocs)

## **Introduction**

Since December 2023, Sekoia TDR team monitored a specific infrastructure involved in the distribution of the Emmenhtal loader. Emmenhtal is a stealthy malware loader known for its effectiveness in distributing various commodity infostealers worldwide. This loader has attracted attention from cybersecurity researchers, with detailed analyses provided by [Orange Cyberdefense](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide) and [Google Cloud’s Threat Intelligence team](https://cloud.google.com/blog/topics/threat-intelligence/peaklight-decoding-stealthy-memory-only-malware?hl=en).

The Emmenhtal loader, also known as PeakLight, operates in a memory-only manner, making it difficult to detect and analyse. It is primarily used to distribute other malicious payloads, including well-known infostealers that target sensitive information.

This blogpost begins by examining the use of WebDAV technology in hosting malicious files related to the Emmenhtal loader, then analyses the various final payloads delivered through this infrastructure, and concludes by exploring the possibility that the infrastructure is being offered as-a-service to multiple threat actors.

## **Use of WebDAV technology for malicious file hosting**

In our investigation of the infrastructure distributing the Emmenhtal loader, TDR analysts identified the use of WebDAV (Web Distributed Authoring and Versioning) technology to host malicious files. WebDAV, an extension of the HTTP protocol, allows for the management of files on web servers, including uploading, editing, and deleting files remotely. Even though WebDAV has legitimate applications in collaborative environments, threat actors have increasingly leveraged this technology to facilitate malicious activities.

The Emmenhtal loader, first detailed by Orange Cyberdefense for its role in distributing commodity infostealers, was later analysed by Google Cloud’s Threat Intelligence team, which uncovered its sophisticated memory-only execution strategy under the name PeakLight. These analyses underscore the significant and evolving threat posed by Emmenhtal as it continues to deliver new infostealers.

In one of the infection chains described by Orange Cyberdefense and Google, the user is initially redirected to the WebDAV server through a drive-by compromise while visiting some websites. This process results in a preview of an *explorer.exe* window connected to the WebDAV server, where the malicious files are hosted. Since the end of 2023, **Sekoia.io identified more than 100 malicious WebDAV servers from this infrastructure**.

In the infrastructure Sekoia analysed, the malicious files were hosted within the “/Downloads” directory on a WebDAV server, an open directory where all files are accessible. The files predominantly consisted of “*.lnk*” files, which were weaponised to download further malicious payloads using the “*mshta.exe*” binary, a legitimate Microsoft executable designed to execute Microsoft HTML Application (HTA) files.

The use of “mshta.exe” to download and execute malicious payloads is a known technique among cybercriminals. By utilising a trusted system binary like “mshta.exe”, threat actors can bypass certain security controls and achieve a higher degree of stealth in their operations. Once the “*.lnk*” file is executed, “*mshta.exe*” is invoked to retrieve the Emmenhtal loader, which is most often hosted on separate infrastructure, adding complexity to the attack chain.

This method of using WebDAV to host malicious “.lnk” files that trigger the download of Emmenhtal via “*mshta.exe*” represents an evasive tactic. The separation of the hosting server for the initial “*.lnk*” files and the payload server hinder detection and attribution efforts, making it a preferred strategy among advanced threat actors.

## **Detailed analysis of malware delivered** via WebDAV

Our analysis uncovered a wider range of malware distributed via this infrastructure than previously reported. The malware families identified, such as SelfAU3, DarkGate, and Amadey, demonstrate the infrastructure’s versatility. Each payload was identified as being delivered through WebDAV-hosted “.lnk” files, with the malicious URLs adjusted to avoid direct exposure. Below is a table of the identified malware families and the corresponding URLs:

| Malware family | URL |
| --- | --- |
| SelfAU3 | ``` 91[.]92[.]251[.]35/Downloads/solaris-docs[.]lnk ``` |
| DarkGate | ``` 206[.]188[.]196[.]28/Downloads/example[.]lnk ``` |
| Amadey | ``` 147[.]45[.]79[.]82/Downloads/qqeng[.]pdf[.]lnk ``` |
| Lumma | ``` 91[.]92[.]243[.]198:81/Downloads/test[.]lnk ``` |
| Remcos | ``` 89[.]23[.]107[.]244/Downloads/Test[.]lnk ```...