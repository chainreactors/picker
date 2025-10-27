---
title: Clearing failed MDM commands from members of Jamf Pro smart or static groups
url: https://derflounder.wordpress.com/2024/11/15/clearing-failed-mdm-commands-from-members-of-jamf-pro-smart-or-static-groups/
source: Der Flounder
date: 2024-11-16
fetch_date: 2025-10-06T19:13:38.270121
---

# Clearing failed MDM commands from members of Jamf Pro smart or static groups

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/) > Clearing failed MDM commands from members of Jamf Pro smart or static groups

## Clearing failed MDM commands from members of Jamf Pro smart or static groups

November 15, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A while back, I had posted about a solution for [clearing failed MDM commands on a per-computer basis](https://derflounder.wordpress.com/2020/09/25/clearing-failed-mdm-commands-on-jamf-pro/). I recently learned it’s also possible to clear them by using an API command which clears failed MDM commands from all members of a specified Jamf Pro smart or static group. This approach works for both computer groups and mobile device groups. For example, if you wanted to clear all failed MDM commands for members of a mobile device group, you could use a command like the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -sf –header "Authorization: Bearer bearer\_token\_goes\_here" "[https://jamf.pro.server.goes.here/JSSResource/commandflush/mobiledevicegroups/id/group\_Jamf\_Pro\_ID\_number\_goes\_here/status/Failed&quot](https://jamf.pro.server.goes.here/JSSResource/commandflush/mobiledevicegroups/id/group_Jamf_Pro_ID_number_goes_here/status/Failed%26quot); -X DELETE |

[view raw](https://gist.github.com/rtrouton/66df04165c82deaed903538269dbb371/raw/3e918011f069a01e12741d4af519e0921e3b81df/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/66df04165c82deaed903538269dbb371#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If you wanted to clear all failed MDM commands for members of a computer group, you could use a command like the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -sf –header "Authorization: Bearer bearer\_token\_goes\_here" "[https://jamf.pro.server.goes.here/JSSResource/commandflush/computergroups/id/group\_Jamf\_Pro\_ID\_number\_goes\_here/status/Failed&quot](https://jamf.pro.server.goes.here/JSSResource/commandflush/computergroups/id/group_Jamf_Pro_ID_number_goes_here/status/Failed%26quot); -X DELETE |

[view raw](https://gist.github.com/rtrouton/bfa48db63697618dad239ac64d3c3402/raw/a6b13c25cda4c966a5f642af2dc9de711bdd9390/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/bfa48db63697618dad239ac64d3c3402#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In both cases, the following API permission would be required:

**Flush MDM Commands**

If using a user account to authenticate to the API, this permission would be set in **Jamf Pro Server Actions**:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-15-at-9.05.png?w=595 "Screenshot 2024-11-15 at 9.05.png")

If using an API client to authenticate to the API, this permission would be set in an API role:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-15-at-9.06.png?w=595 "Screenshot 2024-11-15 at 9.06.png")

For folks who want to use this method to clear failed API commands, I’ve written a couple of scripts to assist with this. For more details, please see below the jump.

I’ve posted both scripts to the following location:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/clear_failed_Jamf_Pro_mdm_commands_from_groups>

* **clear\_failed\_Jamf\_Pro\_mdm\_commands\_from\_computer\_group.sh** – clears failed MDM commands from Jamf Pro smart or static computer groups
* **clear\_failed\_Jamf\_Pro\_mdm\_commands\_from\_mobile\_device\_group.sh** – clears failed MDM commands from Jamf Pro smart or static mobile device groups

Both scripts are designed to use API client authentication, with the following permissions assigned:

**clear\_failed\_Jamf\_Pro\_mdm\_commands\_from\_computer\_group.sh**

* **Flush MDM Commands**
* **Read Smart Computer Groups**
* **Read Static Computer Groups**

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-15-at-9.07-1.png?w=595 "Screenshot 2024-11-15 at 9.07.png")

**clear\_failed\_Jamf\_Pro\_mdm\_commands\_from\_mobile\_device\_group.sh**

* **Flush MDM Commands**
* **Read Smart Mobile Device Groups**
* **Read Static Mobile Device Groups**

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-15-at-9.07.png?w=595 "Screenshot 2024-11-15 at 9.07.png")

Both scripts are designed to use the Jamf Pro ID number for a specified Jamf Pro smart or static group to do the following:

1. Verify that the provided Jamf Pro ID is a positive number, as Jamf Pro IDs should only be only numbers which are not negative.
2. If the provided Jamf Pro ID is a positive number, look up the display name of the specified Jamf Pro smart or static group via the Jamf Pro Classic API using the Jamf Pro ID number.
3. If the lookup succeeds, send a command to clear all failed MDM commands associated with the members of the specified group.
4. If the MDM command clearing succeeds, display a message that all failed MDM commands associated with the members of the specified group have been cleared.

The scripts will produce errors in the following cases:

1. The provided Jamf Pro ID is not a positive number.
2. The lookup of the display name of the specified Jamf Pro smart or static group fails.
3. The MDM command clearing fails.

Successful output should look like this for the following scripts:

**clear\_failed\_Jamf\_Pro\_mdm\_commands\_from\_computer\_group.sh**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /path/to/clear\_failed\_Jamf\_Pro\_mdm\_commands\_from\_computer\_group.sh |
|  | Please enter your Jamf Pro server URL : <https://jamf.pro.server.goes.here> |
|  | Please enter your Jamf Pro API client ID : 7eda98e3-12ea-469c-8c45-4e070b5003cb |
|  | Please enter the API client secret for the 7eda98e3-12ea-469c-8c45-4e070b5003cb API ID client: |
|  |  |
|  | The smart or static computer group you want to clear failed MDM commands from has not been specified. |
|  |  |
|  | Please enter the Jamf Pro ID of the smart or static computer group : 1 |
|  |  |
|  | Clearing failed MDM commmands from members of the following group: All Managed Clients |
|  | <?xml version="1.0" encoding="UTF-8"?><commandflush><status>+failed</status><computer\_groups>[1]</computer\_groups></commandflush> |
|  | Failed MDM commands successfully cleared from members of ...