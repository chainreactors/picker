---
title: Forcing a DDM sync on a Jamf Pro-managed device via the Jamf Pro API
url: https://derflounder.wordpress.com/2025/05/14/forcing-a-ddm-sync-on-a-jamf-pro-managed-device-via-the-jamf-pro-api/
source: Der Flounder
date: 2025-05-15
fetch_date: 2025-10-06T22:24:49.351752
---

# Forcing a DDM sync on a Jamf Pro-managed device via the Jamf Pro API

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Forcing a DDM sync on a Jamf Pro-managed device via the Jamf Pro API

## Forcing a DDM sync on a Jamf Pro-managed device via the Jamf Pro API

May 14, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

[As part of Jamf Pro 10.48.0](https://learn.jamf.com/en-US/bundle/jamf-pro-release-notes-10.48.0/page/New_Features_and_Enhancements.html), Jamf changed the behavior of the **Send Blank Push** MDM command to send a [DeclarativeManagementRequest](https://developer.apple.com/documentation/devicemanagement/declarativemanagementrequest) MDM command (aka **DeclarativeManagement**) in place of the previous blank push MDM command, which was a blank push notification via APNS to the device to prompt the device to check in the Apple Push Notification Service (APNS). Changing the behavior to now send a **DeclarativeManagement** MDM command allows a DDM status report to be sent to the MDM server along with the APNS check-in.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-14-at-1.00.png?w=595 "Screenshot 2025-05-14 at 1.00.png")

However, I’ve observed that sending a blank push command does not always cause a **DeclarativeManagement** command to be queued up for Jamf Pro-managed devices if a previous **DeclarativeManagement** command was recently sent. If you want to make sure a **DeclarativeManagement** MDM command is being sent to your Jamf Pro-managed device, the [declarative-device-management](https://developer.jamf.com/jamf-pro/reference/post_v1-ddm-clientmanagementid-sync) endpoint for the Jamf Pro API can be used to force a DDM status report to be sent to your Jamf Pro server. For more details, please see below the jump.

---

Update: June 6, 2025 – For those who want to use least privileged permissions for running this API command, here’s the permissions needed:

API client permissions:

* **View MDM command information in Jamf Pro API**
* **Send Declarative Management Command**

User account permissions:

**Jamf Pro Server Actions**:

* **View MDM command information in Jamf Pro API**
* **Send Declarative Management Command**

---

The **declarative-device-management** endpoint uses what’s referred to as the client management ID to identify the managed device in question. The client management ID is included as part of the computer inventory record. If you have the Jamf Pro ID of the Mac in question, you can get the client management ID using the following API command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -s <https://jamf.pro.server.here/api/v1/computers-inventory-detail/jamf_pro_id_goes_here> -H 'accept: application/json' -H 'Authorization: Bearer bearer\_token\_goes\_here' | plutil -extract general.managementId raw – |

[view raw](https://gist.github.com/rtrouton/2e9753c350ed947d14a96d5e0ffe52ab/raw/63ede855d35d182b5a631a29ebfe6a16a1d748d4/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/2e9753c350ed947d14a96d5e0ffe52ab#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

That should produce output which looks similar to this, where the output is the client management ID:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/bin/curl -s <https://jamf.pro.server.here/api/v1/computers-inventory-detail/22> -H 'accept: application/json' -H 'Authorization: Bearer bearer\_token\_goes\_here' | plutil -extract general.managementId raw – |
|  | c8bbd450-dbad-44ac-bc46-4024a08ce061 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/7191635a243fccc1767d8f86412b8ae9/raw/92a7e209f73022a8361e7c4cd0e1d489307965d0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7191635a243fccc1767d8f86412b8ae9#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Once you have the client management ID, you should be able to use it to force a DDM sync and cause a **DeclarativeManagement** MDM command to be sent to your managed device:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -s <https://jamf.pro.server.here/api/v1/ddm/client_management_id_goes_here/sync> -H 'accept: application/json' -H 'Authorization: Bearer bearer\_token\_goes\_here' -X POST |

[view raw](https://gist.github.com/rtrouton/76da84e0e322160d3a58704341526c1b/raw/27eb818d8b6fd238bc18e3a6601aca1d16b7618f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/76da84e0e322160d3a58704341526c1b#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Once sent, the **DeclarativeManagement** MDM command should appear in the device’s inventory record as part of the management history.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-14-at-12.59.png?w=595 "Screenshot 2025-05-14 at 12.59.png")

Once the device has sent in an updated DDM status report, you can also use the Jamf Pro API to query the status report’s information. For more information about doing that, please see the link shown below for a previous post on this topic:

<https://derflounder.wordpress.com/2025/03/27/using-the-jamf-pro-api-to-query-ddm-status-information-for-macos/>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/05/14/forcing-a-ddm-sync-on-a-jamf-pro-managed-device-via-the-jamf-pro-api/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/05/14/forcing-a-ddm-sync-on-a-jamf-pro-managed-device-via-the-jamf-pro-api/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/05/14/forcing-a-ddm-sync-on-a-jamf-pro-managed-device-via-the-jamf-pro-api/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/05/14/forcing-a-ddm-sync-on-a-jamf-pro-managed-device-via-the-jamf-pro-api/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/05/14/forcing-a-ddm-sync-on-a-jamf-pro-managed-device-via-the-jamf-pro-api/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/20...