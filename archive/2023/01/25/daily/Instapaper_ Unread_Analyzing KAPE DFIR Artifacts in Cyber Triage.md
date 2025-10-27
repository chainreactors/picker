---
title: Analyzing KAPE DFIR Artifacts in Cyber Triage
url: https://www.cybertriage.com/blog/analyzing-kape-dfir-artifacts-in-cyber-triage/
source: Instapaper: Unread
date: 2023-01-25
fetch_date: 2025-10-04T04:48:44.278396
---

# Analyzing KAPE DFIR Artifacts in Cyber Triage

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

# Analyzing KAPE DFIR Artifacts in Cyber Triage

* January 23, 2023
* **[Dr. Brian Carrier](https://www.cybertriage.com/team/dr-brian-carrier/)**

[KAPE](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape) is a popular tool for collecting files from a suspect system. In this blog post, we’re going to show you how to use Cyber Triage to efficiently analyze your KAPE outputs. Cyber Triage will score the artifacts and highlight ones you should focus on first.

We’ll also talk about how our collection tool is different from KAPE so that you can decide which one you want to use.

This blog is also useful if you use [Velociraptor](https://www.rapid7.com/products/velociraptor/) and output data in the “KAPE Format”. That too can be imported into Cyber Triage.

## KAPE Basics

The Kroll Artifact Parser and Extractor (KAPE) is a set of command line tools and scripts that allow an incident responder to collect artifacts from a target system. It’s development has been led by Eric Zimmerman and is taught in several SANS courses.

From their website:

> “With KAPE, you can find and prioritize the most critical systems to your case and collect key artifacts before imaging. This means no longer having to wait until full system images are gathered and then wading through data where typically less than 10% will have any forensic value.”

There are two primary methods that KAPE uses to collect data:

* A set of files and directories are collected based on paths in configuration files (called targets)
* Command line tools are run that can extract or parse additional data. For example, [PsList](https://learn.microsoft.com/en-us/sysinternals/downloads/pslist) from SysInternals could be called to collect information about running processes.

The results are all saved to a single location and bundled into a container:

* Logical folder structure
* ZIP file
* VHD file

KAPE can be used for free for internal corporate, law enforcement, and academic use. A commercial license is required for consultants.

Here’s an example of running KAPE:

![](https://www.cybertriage.com/wp-content/uploads/2023/01/kape_cli-2-800x183.png)

## KAPE vs Cyber Triage Collector

As you may know, our Cyber Triage application has a program called the [Collector](https://www.cybertriage.com/features/digital-forensics-data-collection/) that runs on target systems and it also collects files and artifacts. So, you may be wondering how KAPE and the Collector are different.

The two tools have similar goals and overlap, but there are a few key differences and each has its own strengths:

The Cyber Triage Collector strengths include:

* The Collector collects more executables. We call it a [adaptive collection tool](https://www.cybertriage.com/blog/adaptive-vs-static-file-collections-for-dfir/) because both collects files based on static rules and it parses data to identify additional files to collect. It parses registry keys and other files so that it can collect the corresponding executable, dll, or referenced file. For example, it will collect the  “AutoRuns” executables for malware analysis. KAPE can run the AutoRuns program and show the list of paths and it will copy the entire registry hive, but it will not copy the specific executables that are run when the system starts.
* The Collector is a single executable with minimal dependencies that is easy to move around and launch. KAPE has several files and requires .NET.

KAPE strengths include:

* The KAPE output is easy to use in other post-processing tools because the output is a logical file set. Any tool that can take in logical files, a ZIP, or VHD can process the results. With Cyber Triage, you have to use a report module to convert to such a folder-based structure. The Collector output is a JSON file.
* KAPE is more user-extensible. KAPE uses a set of text-based configuration files to specify what other programs should get run. The Collector can use custom file collection rules, but cannot run other programs.

While not the point of this article, we are working on adding similar extensibility into the Cyber Triage Collector.

## Cyber Triage Adds Analytics to KAPE

While we think ...