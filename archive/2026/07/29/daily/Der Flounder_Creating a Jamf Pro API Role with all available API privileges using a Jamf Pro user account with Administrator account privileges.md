---
title: Creating a Jamf Pro API Role with all available API privileges using a Jamf Pro user account with Administrator account privileges
url: https://derflounder.wordpress.com/2026/07/29/creating-a-jamf-pro-api-role-with-all-available-api-privileges-using-a-jamf-pro-user-account-with-administrator-account-privileges/
source: Der Flounder
date: 2026-07-29
fetch_date: 2026-07-30T04:47:14.440738
---

# Creating a Jamf Pro API Role with all available API privileges using a Jamf Pro user account with Administrator account privileges

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/) > Creating a Jamf Pro API Role with all available API privileges using a Jamf Pro user account with Administrator account privileges

## Creating a Jamf Pro API Role with all available API privileges using a Jamf Pro user account with Administrator account privileges

July 29, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

I’ve been doing some work with API clients on Jamf Pro, which use [API Roles to assign API privileges to the API client](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/API_Roles_and_Clients). One difference between assigning API privileges to an API Role as opposed to assigning API privileges to a Jamf Pro user account is that API privileges associated with a Jamf Pro user account are on a one to one basis with the Jamf Pro user account’s assigned account privileges. This means that API privileges associated with a user account can be assigned using the following [Jamf Pro account privilege sets](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/Jamf_Pro_User_Accounts_and_Groups):

* **Administrator**: Grants all account privileges
* **Auditor**: Grants all account read privileges
* **Enrollment Only**: Grants all account privileges required to enroll computers and mobile devices

API Roles do not have a corresponding set of API privilege sets, so each privilege assigned to an API Role must be set individually.

The reason why this matters is that Jamf Pro enforces a privilege-escalation guard, where an API Client can’t be used to authenticate an API call which creates a API Role and assigns API privileges to that Role which the API Client does not already hold itself. If you’re trying to set up an API Role which is assigned all API privileges, this means you would have manually assign all available API Role privileges in the Jamf Pro admin console at least one time.

However, in the event that you do need to create an API role that has all available API privileges assigned to it, there’s a way to sidestep the need to manually assign all available API privileges to an API Role. This method uses a Jamf Pro user account which has been assigned the **Administrator** account privileges set. The same privilege-holding rule still applies, but a Jamf Pro user account with the **Administrator** privileges set assigned to it has been granted all available API privileges. This enables an Jamf Pro account to be set up, assigned the **Administrator** account privileges set and subsequently be able to grant all available API privileges to an API Role via an API call.

To assist with this task, I’ve developed a script which uses a Jamf Pro user account with the **Administrator** account privileges assigned to perform the following actions:

* Create a new API role on a Jamf Pro server.
* Assign all available API privileges to that newly-created API role.

For more details, please below the jump.

The script is named **create\_jamf\_pro\_api\_role\_with\_all\_available\_privileges.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/create_jamf_pro_api_role_with_all_available_privileges>

This script connects to the Jamf Pro API on a Jamf Pro server and creates a new Jamf Pro API Role which is then granted every available API privilege.

Three items are required to use this script:

* The URL of the appropriate Jamf Pro server.
* The username for a Jamf Pro user account with the **Administrator** privileges set assigned to it.
* The password for that account.

For this example, I want to create a new API role named **All API Privileges Granted** and use a Jamf Pro user account named **apiadmin** which has been assigned the **Administrator** privileges set to create the new **All API Privileges Granted** API Role.

With the example conditions, you should see similar output to what’s shown below when using the script to create the new **All API Privileges Granted** API Role:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/Shared/create\_jamf\_pro\_api\_role\_with\_all\_available\_privileges.sh |
|  | Please enter your Jamf Pro server URL : <https://jamfpro.server.here> |
|  | Please enter your Jamf Pro user account : apiadmin |
|  | Please enter the password for the apiadmin account: |
|  | Retrieving the list of available API Role privileges … |
|  | Found 524 total API Role privileges on this server. |
|  | Verifying the 'apiadmin' account holds every privilege in the catalog … |
|  | Account holds every privilege in the catalog. Proceeding … |
|  | Name for the new all-privileges API Role: All API Privileges Granted |
|  | Creating API Role 'All API Privileges Granted' with all 524 privileges … |
|  |  |
|  | API Role created successfully: |
|  | ID: 15 |
|  | Display Name: All API Privileges Granted |
|  | Privileges: 524 (every privilege in the API Role catalog) |
|  |  |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/8a0b83dda64ddcb50b04d6af0e081ef7/raw/622c69d1aeec170825af2b41d960125f3e32ac24/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8a0b83dda64ddcb50b04d6af0e081ef7#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should then be able to check on the Jamf Pro server and verify that the API Role has been created and that it has all available permissions assigned to it.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/07/screenshot-2026-07-29-at-12.13.png?w=595 "Screenshot 2026-07-29 at 12.13.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2026/07/screenshot-2026-07-29-at-12.13-1.png?w=595 "Screenshot 2026-07-29 at 12.13.png")

As part of its run, the script will verify if the account being used to create the API Role itself has all available API privileges assigned to it. If the account does not have all available API privileges assigned to it, it will stop and display warnings similar to what is shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/Shared/create\_jamf\_pro\_api\_role\_with\_all\_available\_privileges.sh |
|  | Please enter your Jamf Pro server URL : <https://jamfpro.server.here> |
|  | Please enter your Jamf Pro user account : apiadmin |
|  | Please enter the password for the apiadmin account: |
|  | Retrieving the list of available API Role privileges … |
|  | ERROR: Failed to retrieve API Role privileges. Please try again using a Jamf Pro account which has been assigned the Administrator privileges set. Response from Jamf Pro server: { |
|  | "httpStatus" : 403, |
|  | "errors" : [ { |
|  | "code" : "INVALID\_PRIVILEGE", |
|  | "description" : "Forbidden", |
|  | "id" : "0", |
|  | "field" : null |
|  | } ] |
|  | } |
|  | username@computername ~ % |

[view raw](...