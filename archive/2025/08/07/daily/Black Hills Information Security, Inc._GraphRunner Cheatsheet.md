---
title: GraphRunner Cheatsheet
url: https://www.blackhillsinfosec.com/graphrunner-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:16.668403
---

# GraphRunner Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Beau Bullock](https://www.blackhillsinfosec.com/category/author/beau-bullock/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Kaitlyn Wimberley](https://www.blackhillsinfosec.com/category/author/kaitlyn-wimberley/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [GraphRunner](https://www.blackhillsinfosec.com/tag/graphrunner/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [GraphRunner Cheatsheet](https://www.blackhillsinfosec.com/graphrunner-cheatsheet/)

Written by [Kaitlyn Wimberley](https://www.blackhillsinfosec.com/team/kaitlyn-wimberley/) || Reviewed by [Beau Bullock](https://x.com/dafthack?lang=en)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_5.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**GraphRunner Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_GraphRunner-.pdf)

Find the tool here: <https://github.com/dafthack/GraphRunner>

---

GraphRunner is a collection of post-exploitation PowerShell modules for interacting with the Microsoft Graph API. It provides modules for enumeration, exfiltration, persistence, and more!

## Installation

```
git clone https://github.com/dafthack/GraphRunner
cd GraphRunner
Import-Module .\GraphRunner.ps1
```

List all of the available GraphRunner modules:

```
List-GraphrunnerModules
```

## Obtaining Tokens

Obtain tokens with the Device Code authentication flow:

```
Get-GraphTokens
```

*(Requests tokens for the Microsoft Office client, graph.microsoft.com resource, and Chrome on macOS user agent)*

–

Specify the Client, Resource, and User Agent used in the token request:

```
Get-GraphTokens -Client AzureManagement -Resource https://graph.windows.net -Browser Android -Device Mac
```

*Conditional Access policies can often be subverted by choosing the right values here.*

–

Specify a custom Client by Client ID:

```
Get-GraphTokens -Client Custom -ClientID "e9c51622-460d-4d3d-952d-966a5b1da34c"
```

–

Tokens will automatically be written to the variable `$tokens`.

–

Already have tokens? Import them with `Invoke-ImportTokens -AccessToken "eyJ..." -RefreshToken "0.A...”`

–

By default, access tokens expire between 60-90 minutes after issue.

Refresh an expired access token with `Invoke-RefreshGraphTokens` OR use `Invoke-AutoTokenRefresh` to automatically refresh the token periodically.

```
Invoke-AutoTokenRefresh -RefreshToken $tokens.refresh_token -tenantid "example.com" -RefreshInterval 42
```

## Enumerate Permissions

Different actions within the Graph API (and therefore GraphRunner) require different scopes. Enumerate the permissions associated with multiple client applications to determine which ones will give you the permissions you need:

```
Invoke-BruteClientIDAccess -domain example.com -refreshToken $tokens.refresh_token
```

*Great reference for Graph permissions:* [*https://graphpermissions.merill.net/permission/*](https://graphpermissions.merill.net/permission/)

## GraphRun All the Things

```
Invoke-GraphRunner -Tokens $tokens
```

This module is a wrapper that runs:

* **Invoke-GraphRecon** – Gathers various reconnaissance data such as authorization policies, main contact information, and user settings.
* **Get-AzureADUsers** – Gathers all users from the directory.
* **Get-SecurityGroups** – Lists all security groups and their members.
* **Invoke-DumpCAPS** – Gathers conditional access policies.
  + *Review these to identify restrictions you’ll need to work around or exceptions you can take advantage of*.
* **Invoke-DumpApps** – Gathers tenant’s registered applications, with permission scopes and consented users, and external applications that users consented to.
* **Invoke-SearchMailbox**, **Invoke-SearchSharePointAndOneDrive**, and **Invoke-SearchTeams** – Search the user’s mailbox as well as accessible SharePoint sites, OneDrives, and Teams channels/messages for interesting content using the GraphRunner default\_detectors.json rules

## Groups, Groups, and More Groups

Find groups that your user has the ability to update:

```
Get-UpdatableGroups...