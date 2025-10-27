---
title: Can we block the addition of local Microsoft Defender Antivirus exclusions?
url: https://blog.nviso.eu/2022/12/02/can-we-block-the-addition-of-local-microsoft-defender-antivirus-exclusions/
source: NVISO Labs
date: 2022-12-03
fetch_date: 2025-10-04T00:23:08.551285
---

# Can we block the addition of local Microsoft Defender Antivirus exclusions?

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

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

# Can we block the addition of local Microsoft Defender Antivirus exclusions?

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Cloud Security](https://blog.nviso.eu/category/cloud-security/), [Microsoft 365 Defender](https://blog.nviso.eu/category/microsoft-365-defender/)

December 2, 2022December 2, 2022
6 Minutes

## **Introduction**

A few weeks ago, I got a question from a client to check how they could prevent administrators, including local administrators on their device, to add exclusions in Microsoft Defender Antivirus. I first thought it was going to be pretty easy by pushing some settings via Microsoft Endpoint Manager. However, after doing some research and tests in a lab environment, I discovered that it might not be as easy as I thought.

## **What capabilities in Microsoft Defender Antivirus can help us?**

Microsoft Defender Antivirus, which is part of the Microsoft Defender for Endpoint (MDE), is one component of the next-generation protection solution. Microsoft Defender Antivirus comes with different features that can be configured using Microsoft Endpoint Manager (MEM)/Intune, Group Policy, PowerShell, etc. These features include cloud-delivered and real-time protection with behavioral, heuristic and machine learning-based protection.

Because some business applications might be blocked by these capabilities, there is the possibility to create specific exclusions for files, processes and processed-opened files from Microsoft Defender Antivirus scans, real-time protection and monitoring. Although they can be useful to benefit from the protection capabilities while preventing any impact on end users and business flows, they represent a protection gap. Indeed, the more exclusions there are, the larger the attack surface is. Therefore, it is a best practice to keep them as limited as possible and to review them periodically.

Because these are protection gaps, you don’t want users from adding exclusions locally on their laptop. By default, standard users can’t change, add or remove exclusions. However, administrators can. This is where our problems start. Indeed, we want to prevent that users help themselves to install suspicious software and we don’t want attackers that would have gained sufficient privileges to add exclusions so that they can install and run their malicious payloads.

How can we prevent users from adding exclusions? We can? Right? We will go over different possibilities in Microsoft Defender for Endpoint to do so.

### Tamper Protection

First, let’s have a look at Tamper Protection. By searching on the Internet, I found a few posts mentioning that Tamper Protection could help us to solve this issue.

Tamper Protection is a feature that allows to protect specific protection settings against tampering as its name suggests. The main objective of Tamper Protection is to make sure attackers can’t disable security features to get easier access to your data, install malware or run exploits. In practice, Tamper Protection allows to prevent the following:

* Disabling virus and threat protection
* Disabling real-time protection
* Turning off behavior monitoring
* Disabling antivirus protection, such as IOfficeAntivirus (IOAV)
* Disabling cloud-delivered protection
* Removing security intelligence updates
* Disabling automatic actions on detected threats
* Suppressing notifications in the Windows Security app
* Disabling scanning of archives and network files

Therefore, we can already see that this is not going to help us here. I can also confirm this based on the tests that I have done. During the tests, Tamper Protection is enabled at the tenant level in the Microsoft 365 Defender portal and therefore applied to all devices by default.

### Local Admin Merge

Secondly, we have the Defender “local admin merge” feature. This capability looks more interesting. Indeed, it allows to control if exclusion list settings, which are configured by a local admin, will merge with managed settings from an Intune policy. We can use a Microsoft Defender Antivirus profile in Microsoft Endpoint Manager to configure it:

![Enforce "Disable Local Admin Merge" in an Antivirus profile in MEM](https://blog.nviso.eu/wp-content/uploads/2022/11/DisableLocalAdminMerge_Intune.png)

Enforce “Disable Local Admin Merge” in an Antivirus profile in MEM

Three values are supported for the *Disable Local Admin Merge*:

* **Not configured**: preference settings configured by local administrators will be merged into the resulting effective policy. If there are conflicts, settings from Intune will override local preference settings.
* **Enable Local Admin Merge**: same as *Not configured*.
* **Disable Local Admin Merge**: Intune-managed settings override preference settings that are configured by local administrators.

Theoretically, the *Disable Local Admin Merge* value would allow to prevent local admins from creating exclusions. We will test that in a moment, but let’s check first if this setting is correctly applied on my device. In the registry editor, I verify that the *DisableLocalAdminMerge* key is set to *1*:

![DisableLocalAdminMerge key set to 1 (enforced)](https://blog.nviso.eu/wp-content/uploads/2022/11/LocalAdminMerge_RegEdit.png)

DisableLocalAdminMerge key set to 1 (enforced)

It seems to be the case here, great! If we go to Windows Security on the local machine, we can see that exclusions already exists and that we can’t add or manage them. This is because these policies have been pushed through Intune:

![Existing exclusions configured via Intune](https://blog.nviso.eu/wp-content/uploads/2022/11/Exclusions.png)

Existing exclusions configured via Intune

We will now see if we can still add local exclusions to download and run malicious software. First, if we try to download *SharpHound* for example, it will end up in the user’s download folder and get removed automatically:

![Windows Security alert: Threat found](https://blog.nviso.eu/wp-content/uploads/2022/11/WindowsSecurity_alert.png)

Windows Security alert: Threat found

As mentioned before, exclusions can be managed in PowerShell. We will add an exclusion for our download folder using the `Add-MpPreference -ExclusionPath 'C:\Users\<USERNAME>\Downloads'` (make sure to replace *<USERNAME>*) PowerShell cmdlet. Moreover, we can verify the exclusions that currently apply using `Get-MpPref...