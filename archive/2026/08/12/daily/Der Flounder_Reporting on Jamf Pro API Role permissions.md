---
title: Reporting on Jamf Pro API Role permissions
url: https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/
source: Der Flounder
date: 2026-08-12
fetch_date: 2026-08-13T04:02:44.189552
---

# Reporting on Jamf Pro API Role permissions

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Reporting on Jamf Pro API Role permissions

## Reporting on Jamf Pro API Role permissions

August 12, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of [reporting on Jamf Pro API clients and assigned API roles](https://derflounder.wordpress.com/2026/05/22/13403/), I had [previously written a script](https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/API_Client_Role_Reporting) to report on the following information:

* The current list of the enabled and disabled API clients on a Jamf Pro server.
* Which API roles are being used by the API clients.

It later occurred to me that a more comprehensive report which includes the permissions assigned to the roles may be wanted, so I’ve now written a separate script which reports on the following:

* API Role Display Name
* API Role ID number
* API privileges assigned to the API Role.
* Which API Clients are assigned to each API Role and whether the API Client is enabled or disabled.

For more details, please see below the jump.

The script is named **Generate\_Jamf\_Pro\_API\_Role\_Privileges\_Report.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Generate_Jamf_Pro_API_Role_Privileges_Report>

This script connects to the Jamf Pro API on a Jamf Pro server and reports the API Roles, their assigned API privileges and which API clients (if any) are assigned to those API client roles.

Three items are required to use this script:

* The URL of the appropriate Jamf Pro server.
* An API client on the Jamf Pro server with sufficient privileges to read the necessary information from the Jamf Pro API.
* The client secret for the relevant API client on the Jamf Pro server.

If setting up an API client with limited rights, here are the required API role privileges for the API client on the Jamf Pro server:

* **Read API Integrations**
* **Read API Roles**

You should see similar output to what’s shown below when using the **Generate\_Jamf\_Pro\_API\_Role\_Privileges\_Report.sh** script to generate a report:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/Shared/Jamf\_Pro\_API\_Role\_Privileges\_Report/Jamf\_Pro\_API\_Role\_Privileges\_Report.sh |
|  | Please enter your Jamf Pro server URL : <https://jamf.pro.server.here> |
|  | Please enter your Jamf Pro API client ID : 88ab021a-6b2e-478e-ae57-7b2208664c7c |
|  | Please enter the API client secret for the 88ab021a-6b2e-478e-ae57-7b2208664c7c API client ID: |
|  | Report being generated. File location will appear below once ready. |
|  | Role Name Role ID Privilege Name Assigned API Client(s) |
|  | Create API Roles and Update API Roles 28 Create API Roles 125ed256-21e1-42b6-bb77-afe3c917a940 (Disabled) |
|  | Create API Roles and Update API Roles 28 Update API Roles 125ed256-21e1-42b6-bb77-afe3c917a940 (Disabled) |
|  | Read Computers API Role 29 Read Computers 47da63c0-1386-4c55-851b-cc0098621f26 (Enabled) |
|  | Read API Roles and API Integrations 30 Read API Integrations 88ab021a-6b2e-478e-ae57-7b2208664c7c (Enabled) |
|  | Read API Roles and API Integrations 30 Read API Roles 88ab021a-6b2e-478e-ae57-7b2208664c7c (Enabled) |
|  | Create Computers API Role 31 Create Computers (No API Client assigned) |
|  |  |
|  | Report available here: /var/folders/ps/2\_yw29gj711c9d7c5w5jhyv80000gp/T/tmp.OG0uCcS4CL.tsv |
|  |  |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/334564817ac2b1fbfc6403bf8c00de08/raw/b26c41d5a844e238f16856f4959724946d6b8dd2/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/334564817ac2b1fbfc6403bf8c00de08#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

As part of the script’s run, a report will be generated and you’ll be notified of where it is stored. The report will be in [TSV format](https://en.wikipedia.org/wiki/Tab-separated_values) and appear similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Role Name | Role ID | Privilege Name | Assigned API Clients |
| --- | --- | --- | --- | --- |
|  | Create API Roles and Update API Roles | 28 | Create API Roles | 125ed256-21e1-42b6-bb77-afe3c917a940 (Disabled) |
|  | Create API Roles and Update API Roles | 28 | Update API Roles | 125ed256-21e1-42b6-bb77-afe3c917a940 (Disabled) |
|  | Read Computers API Role | 29 | Read Computers | 47da63c0-1386-4c55-851b-cc0098621f26 (Enabled) |
|  | Read API Roles and API Integrations | 30 | Read API Integrations | 88ab021a-6b2e-478e-ae57-7b2208664c7c (Enabled) |
|  | Read API Roles and API Integrations | 30 | Read API Roles | 88ab021a-6b2e-478e-ae57-7b2208664c7c (Enabled) |
|  | Create Computers API Role | 31 | Create Computers | (No API Client assigned) |

[view raw](https://gist.github.com/rtrouton/79dbd5700316ebcc91d1ecf3d23f78ee/raw/c21d22fd7d0816d0c25b844bfe9b6a19d87f285b/tmp.OG0uCcS4CL.tsv)
 [tmp.OG0uCcS4CL.tsv](https://gist.github.com/rtrouton/79dbd5700316ebcc91d1ecf3d23f78ee#file-tmp-og0uccs4cl-tsv)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/08/12/reporting-on-jamf-pro-api-role-permissions/?share=tumblr)

Like Loading...

### *Related*

Categories: [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/08/12/reporting-on-jamf-pro-api-role-permissions/#respond)

Δ

[Validating FileVault recovery keys using a plist file to provide...