---
title: ShimCache and AmCache Forensic Analysis 2025
url: https://www.cybertriage.com/blog/shimcache-and-amcache-forensic-analysis-2025/
source: Instapaper: Unread
date: 2025-05-08
fetch_date: 2025-10-06T22:39:04.378856
---

# ShimCache and AmCache Forensic Analysis 2025

[Skip to content](#primary)

[cyber-triage-logo](https://www.cybertriage.com/)

Primary Menu

* [Platform](https://www.cybertriage.com/features/)
  + - * [Workflow](https://www.cybertriage.com/how-cyber-triage-works/)
      * [Benefits](https://www.cybertriage.com/benefits/)
      * [Why Cyber Triage](https://www.cybertriage.com/why-cyber-triage-digital-forensics-tool/)
      * [Compare Versions](https://www.cybertriage.com/features/versions/)
      * [Cyber Triage for Teams](https://www.cybertriage.com/team-version/)
    - * #### Key Features
      * [The Collector](https://www.cybertriage.com/cyber-triage-dfir-collector/)
      * [Artifact Scoring](https://www.cybertriage.com/features/prioritize-with-cyber-triage/)
      * [Malware Detection](https://www.cybertriage.com/malware-forensics-tool/)
      * [Ransomware Detection](https://www.cybertriage.com/features/ransomware/)
      * [Server API](https://www.cybertriage.com/team-rest-api/)
    - * #### EDR
      * [EDR + Cyber Triage](https://www.cybertriage.com/edr/)
      * [EDR Evasion 101](https://www.cybertriage.com/blog/how-edr-evasion-works-attacker-tactics/)
    - * #### Integrations
      * [EDR Powershell Script](https://www.cybertriage.com/deployer-script/)
      * [Integrated Capabilities](https://www.cybertriage.com/features/integrations/)
      * [Malware Scanner for Autopsy](https://www.cybertriage.com/autopsy-malware-module/)
* [Use Cases](https://www.cybertriage.com/benefits/)
  + [SOC Endpoint Investigation](https://www.cybertriage.com/soc-alert-investigation/)
  + [Consultants](https://www.cybertriage.com/benefits/consultants/)
  + [SOC DFIR Teams](https://www.cybertriage.com/benefits/internal-incident-responders/)
  + [Law Enforcement - Intrusions](https://www.cybertriage.com/benefits/law-enforcement/)
  + [Law Enforcement - ICAC (Trojan Defense)](https://www.cybertriage.com/detect-remote-access-for-icac-and-trojan-defense/)
* [Pricing](https://www.cybertriage.com/pricing/)
  + [Buy Cyber Triage](https://www.cybertriage.com/pricing/)
  + [Buy Malware Scanning Boosts](https://www.cybertriage.com/boost-checkout/)
  + [Buy Autopsy Malware Scanner Module](https://www.cybertriage.com/autopsy-checkout/)
  + [Buy Rapid Endpoint Triage Service](https://www.sleuthkitlabs.com/rapid_checkout/)
* [Resources](https://www.cybertriage.com/online-response-training/)
  + - * [Blog](https://www.cybertriage.com/blog/)
      * [Webinars](https://www.cybertriage.com/events/)
      * [Videos](https://www.cybertriage.com/videos/)
      * [Intro to DFIR Blog Series](https://www.cybertriage.com/intro-to-cyber-incident-response/)
      * [Cyber RespondIR Newsletter](https://www.cybertriage.com/sign-up-for-the-cyber-respondir/)
    - * [Rapid Endpoint Triage Service](https://www.cybertriage.com/services/#rapid)
      * [Training](https://www.cybertriage.com/training/)
    - * #### Recent Releases
      * [3.15 (Defender Telemetry, Access Control, IRIS)](https://www.cybertriage.com/blog/cyber-triage-3-15-import-defender-telemetry-more-soc-features/)
      * [3.14 (Tactics, Hayabusa, Baselining)](https://www.cybertriage.com/blog/3-14-release-brings-new-uis-hayabusa-baselining-and-much-more/)
      * [3.13 (MemProcFS, S3 Reading)](https://www.cybertriage.com/blog/releases/3-13-adds-memprocfs-and-extends-the-s3-and-recorded-future-sandbox-integrations/)
      * [3.12 (Data Exfil, USB, Validation)](https://www.cybertriage.com/blog/releases/3-12-adds-data-exfiltration-detection-usb-devices-and-easier-validation/)
* [About](https://www.cybertriage.com/about/)
  + [About](https://www.cybertriage.com/about/)
  + [Team](https://www.cybertriage.com/team/)
  + [Contact](https://www.cybertriage.com/contact/)
* [Start Free Trial](https://www.cybertriage.com/download-eval/)

# ShimCache and AmCache Forensic Analysis 2025

* May 2, 2025
* **[Chris Ray](https://www.cybertriage.com/team/chris-ray/)**

ShimCache and AmCache have lots to offer investigators.

But they’re tricky, too.

Learn the ins and outs of these artifacts from DFIR expert Chris Ray.

Let’s get to it!

**Jump to…**
[Intro to ShimCache and AmCache](#Intro to ShimCache and AmCache)
[Understanding AmCache](#Understanding AmCache)
[Understanding ShimCache](#Understanding AmCache)
[Data Captured by AmCache](#Data Captured by AmCache)
[Data Captured by ShimCache](#Data Captured by ShimCache)
[AmCache vs. ShimCache](#AmCache vs. ShimCache)
[Tools for Analysis](#Tools for Analysis)
[Other Application Compatibility Artifacts](#Other Application Compatibility Artifacts)

## **Intro to ShimCache and AmCache**

The [Windows Application Compatibility](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-7/dd837644%28v%3Dws.10%29) (Shim) Infrastructure is a complex and powerful feature that enables older applications to run on newer systems using a form of API hooking.

Metadata is stored on PE files of interest (executed, viewed by user, etc.) and installed applications to allow the shimming infrastructure to work smoothly. As a result, the locations where Windows stores this metadata became key forensic artifacts.

**2 most notable:**

* ShimCache
* AmCache

From an investigator’s perspective, these artifacts provide a trove of information available by default on all modern systems. This is in contrast to other high-value artifacts like Prefetch (disabled by default on servers) and process auditing (disabled by default), which may not be available.

We will dive into each of these artifacts in the following section below.

But, at a high level, **both artifacts provide the following:**

| **Evidence** | **Notes** |
| --- | --- |
| **Existence** | All entries can prove file once existed at recorded location. |
| **Execution** | Due to the complex nature of these artifacts, it’s best to think of this data under evidence of existence rather than evidence of execution. In certain scenarios you can show a file executed with a high degree of confidence, but should never be the definitive proof that something ran. |
| **App install** | AmCache only. |

## **Understanding AmCache**

AmCache is part of the Windows shimming infrastructure and was designed to enhance the application compatibility experience. The data is stored in a registry hive ([REGF](https://github.com/libyal/libregf/blob/main/documentation/Windows%20NT%20Registry%20File%20%28REGF%29%20format.asciidoc) formatted file), which is not part of the Windows Registry. Amcache logs extensive metadata related to installed applications, programs that exist or have been executed, drivers loaded, and much more.

| **Location** | |
| --- | --- |
| **Newer location** | ``` C:\Windows\AppCompat\Programs\Amcache.hve ``` |
| **Older location\*** | ``` C:\AppCompat\Programs\RecentFileCache.bcf ``` |

| **Limitations to Keep in Mind** |
| --- |
| * SHA1 hash isn’t always a full file hash (only up to 30 MBs). * Doesn’t contain process arguments, user associated with execution, or execution times. * Due to the artifact’s complexity, entries should generally not be used to prove program execution. Safer to interpret data as evidence of existence.\*\* * Artifact is complex and has changed numerous times since its inception, making it difficult to understand and leverage all the data it has to offer. |

| **Forensic Utility** |
| --- |
| * Data can prove files existed on disk even after file deletion. * Provides insight into installed applications, along with how it was installed. * SHA1 hash for PE files and drivers allows for file reputation checks to be done even after files have been deleted. * Stores comprehensive metadata for PE files and DLLs such as file size, SHA1, and PE header info like CompanyName, FileVersion, etc. |

| **Learn More about AmCache** |
| --- |
| * **Blanche Lagny**: [Analysis of the AmCache](https://cyber.gouv.fr/sites/default/files/2019/01/anssi-coriin_2019-analysis_amcache.pdf) * **binary foray**: [(Am)cache still rules everything around me (part 2 of 1)](https://binaryforay.blogs...