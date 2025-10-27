---
title: Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later
url: https://derflounder.wordpress.com/2023/08/15/updating-management-status-in-jamf-pro-computer-inventory-records-on-jamf-pro-10-49-0-and-later/
source: Der Flounder
date: 2023-08-16
fetch_date: 2025-10-04T11:58:47.225162
---

# Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

## Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

August 15, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As of Jamf Pro 10.49.0, the following mass action has been removed:

* **Edit the Management Account Information**

![Screen Shot 2021 09 28 at 10 39 53 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/08/screen-shot-2021-09-28-at-10.39.53-am.png?w=595 "Screen Shot 2021-09-28 at 10.39.53 AM.png")

I had been using this to update the status of unmanaged Macs to now be managed Macs, by editing the username and password assigned to the computer inventory record. As part of this, the remote management status of the computer inventory record would change from **Unmanaged** to **Managed**.

As of Jamf Pro 10.49.0, the management account information has been removed from the computer inventory record, with the resulting removal of the mass-action to edit the management account information. However, this has left me without a mass-action to change unmanaged Macs to managed Macs.

Fortunately, there’s a way to change this via the Jamf Pro Classic API. The relevant API command to change the management status in a Jamf Pro computer inventory record should look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -H "content-type: text/xml" "[https://jamf.pro.server.here/JSSResource/computers/id/jamf\_pro\_computer\_ID\_goes\_here&quot](https://jamf.pro.server.here/JSSResource/computers/id/jamf_pro_computer_ID_goes_here%26quot); –header "Authorization: Bearer api\_token\_goes\_here" -X PUT -d "<computer><general><remote\_management><managed>true</managed></remote\_management></general></computer>" |

[view raw](https://gist.github.com/rtrouton/892998de0fde83465f5f82c0b0b588c9/raw/19ac9fa1eb402f8a251856f8b1e7d2dbf765486c/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/892998de0fde83465f5f82c0b0b588c9#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

It’s sending the following XML block to update the relevant computer inventory record and make the management change:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <computer> |
|  | <general> |
|  | <remote\_management> |
|  | <managed>true</managed> |
|  | </remote\_management> |
|  | </general> |
|  | </computer> |

[view raw](https://gist.github.com/rtrouton/2918b7317b1c6810fb71a676b3235ab8/raw/3ac22cbe0027950282be4901ceb67b20c5dcb69f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/2918b7317b1c6810fb71a676b3235ab8#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Previously, you also needed to send along the management username and management password, but since those have been removed as of Jamf Pro 10.49.0, those are no longer needed.

I have filed a feature request with Jamf to get back an equivalent mass-action to update the management status. For those interested, it is the following:

**JN-I-27551**: <https://ideas.jamf.com/ideas/JN-I-27551>

While I wait to see what Jamf does with the feature request, I was able to use the API information discussed above to create a script which a) updates the management status in specified computer inventory records and b) generates a report of the Macs whose computer inventory records were updated. For more details, please see below the jump.

The script is named **Set\_Jamf\_Pro\_Computers\_To\_Managed\_Status.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Set_Jamf_Pro_Computers_To_Managed>

The script is designed to take in a set of Jamf Pro ID numbers in a plaintext file, where the Jamf Pro ID numbers correspond the Macs where you want to change the management status in their Jamf Pro computer inventory records. The plaintext file should look similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 416462 |
|  | 842736 |
|  | 434703 |
|  | 338517 |
|  | 481915 |
|  | 596669 |

[view raw](https://gist.github.com/rtrouton/cfed6b5d30fff51a44e46fbb832fa489/raw/f6c50ad2867d0a56ca1b39deb64f806cc043af41/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/cfed6b5d30fff51a44e46fbb832fa489#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Five items are required to use this script:

* Jamf Pro 10.49.0 or later
* A text file containing the Jamf Pro IDs of the computer(s) you wish to delete.
* The URL of the appropriate Jamf Pro server.
* The username of an account on the Jamf Pro server with sufficient privileges to delete computers from the Jamf Pro server.
* The password for the relevant account on the Jamf Pro server.

Jamf Pro account privileges required by the Jamf Pro server account referenced above:

**Jamf Pro Server Objects**:

Computers: **Read**, **Update**

Users: **Update**

Once the five specified items are available, the script can be run using the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /path/to/Set\_Jamf\_Pro\_Computers\_To\_Managed\_Status.sh /path/to/plaintext\_filename\_here.txt |

[view raw](https://gist.github.com/rtrouton/514ff2d01cce9284dad07e201858a6aa/raw/c801b7d0421320dd8e45c686096d93492147571f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/514ff2d01cce9284dad07e201858a6aa#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see output like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/Shared/Set\_Jamf\_Pro\_Computers\_To\_Managed/Set\_Jamf\_Pro\_Computers\_To\_Managed\_Status.sh /Users/Shared/jamfpro\_comput...