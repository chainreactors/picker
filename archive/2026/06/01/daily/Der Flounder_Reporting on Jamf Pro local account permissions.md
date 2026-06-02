---
title: Reporting on Jamf Pro local account permissions
url: https://derflounder.wordpress.com/2026/06/01/reporting-on-jamf-pro-local-account-permissions/
source: Der Flounder
date: 2026-06-01
fetch_date: 2026-06-02T06:31:15.245053
---

# Reporting on Jamf Pro local account permissions

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Reporting on Jamf Pro local account permissions

## Reporting on Jamf Pro local account permissions

June 1, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to my previous post on [reporting on Jamf Pro API clients and assigned API roles](https://derflounder.wordpress.com/2026/05/22/13403/), I decided to see if I could write a similar script for [reporting on the permissions assigned to Jamf Pro local user accounts](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/Jamf_Pro_User_Accounts_and_Groups). With this in mind, I’ve written a script which reports the following:

• The current list of the Jamf Pro user accounts on a Jamf Pro server
• The permissions assigned to those user accounts
• Whether those permissions are assigned directly to the account, or if they are permissions assigned to the account because it is a member of a Jamf Pro user group.

For more details, please see below the jump.

The script is named **Jamf\_Pro\_Local\_Account\_Permissions\_Report.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Jamf_Pro_Local_Account_Permissions_Report>

This script connects to the Jamf Pro Classic API on a Jamf Pro server and reports which Jamf Pro user accounts have which permissions assigned, along with how those permissions are assigned (direct assignment to the user account, or via membership in a user group.)

Three items are required to use this script:

* The URL of the appropriate Jamf Pro server.
* An API client on the Jamf Pro server with sufficient privileges to read the necessary information from the Jamf Pro Classic API.
* The client secret for the relevant API client on the Jamf Pro server.

If setting up an API client with limited rights, here are the required API role privileges for the API client on the Jamf Pro server:

* **Read Accounts**

The report should include the following information:

* Account Name
* Account ID
* Account Enabled / Disabled
* Privilege Category
* Privilege Name
* Assignment Type

In this example, I have the following Jamf Pro user accounts set up on a Jamf Pro server:

* **backup\_admin\_user\_failover**
* **computer\_deletion\_service\_account**
* **it\_audit\_service\_account**
* **jamfpro-enroll**

How permissions are assigned to the user accounts:

* **backup\_admin\_user\_failover**: Member of the **Administrator Permissions Group**, which has the **Administrator** privileges set assigned to the group.
* **computer\_deletion\_service\_account**: Permissions are directly assigned to the user account.
* **it\_audit\_service\_account**: Member of the **Auditor Permissions Group**, which has the **Auditor** privileges set assigned to the group.
* **jamfpro-enroll**: Member of the **Enrollment Permissions Group**, which has the **Enrollment** privileges set assigned to the group.

With the example conditions, you should see similar output to what’s shown below when using the **Jamf\_Pro\_Local\_Account\_Permissions\_Report.sh** script to generate a report:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /path/to/Jamf\_Pro\_Local\_Account\_Permissions\_Report.sh |
|  | Please enter your Jamf Pro server URL : <https://jamf.pro.server.here> |
|  | Please enter your Jamf Pro API client ID : 685a71d5-e08d-460b-af81-8763d30559f5 |
|  | Please enter the API client secret for the 685a71d5-e08d-460b-af81-8763d30559f5 API client ID: |
|  | Report being generated. File location will appear below once ready. |
|  | Account Name Account ID Account Enabled Privilege Category Privilege Name Assignment Type |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Create Cloud Distribution Point Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Read Cloud Distribution Point Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Update Cloud Distribution Point Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Create Custom Paths Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Read Custom Paths Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Update Custom Paths Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Delete Custom Paths Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Create Jamf Cloud Distribution Service Files Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Read Jamf Cloud Distribution Service Files Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Delete Jamf Cloud Distribution Service Files Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Create API Integrations Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Read API Integrations Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Update API Integrations Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Delete API Integrations Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects blueprints create Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects blueprints read Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects blueprints update Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects blueprints delete Permission assigned via membership in Jamf Pro group: Administrator Permissions Group |
|  | backup\_admin\_user\_failover 7 Enabled Jamf Pro Server Objects Create API Roles Permission assigned via m...