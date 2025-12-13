---
title: Updating management status in Jamf Pro computer inventory records using the Jamf Pro API
url: https://derflounder.wordpress.com/2025/12/12/13154/
source: Der Flounder
date: 2025-12-12
fetch_date: 2025-12-13T03:14:25.880193
---

# Updating management status in Jamf Pro computer inventory records using the Jamf Pro API

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Updating management status in Jamf Pro computer inventory records using the Jamf Pro API

## Updating management status in Jamf Pro computer inventory records using the Jamf Pro API

December 12, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A while back, I wrote a post on [how to set Jamf Pro computer inventory records to be managed using a script](https://derflounder.wordpress.com/2023/08/15/updating-management-status-in-jamf-pro-computer-inventory-records-on-jamf-pro-10-49-0-and-later/). I recently revisited this script as part of a general effort on my part to update scripts which have been using the [now-deprecated computers Classic API endpoint](https://derflounder.wordpress.com/2025/03/21/jamf-pro-classic-api-computer-inventory-endpoint-deprecated-as-of-jamf-pro-11-15-0/), to now use the Jamf Pro API’s [computers-inventory-detail API endpoint](https://developer.jamf.com/jamf-pro/reference/get_v1-computers-inventory-detail-id).

As part of this effort, I decided to not only update my existing script for setting the management status in Jamf Pro computer inventory records to be managed but also write a second script for setting the management status to be unmanaged. For more details, please see below the jump.

You can set the management status in a Jamf Pro computer inventory record using the [computers-inventory-detail endpoint](https://developer.jamf.com/jamf-pro/reference/patch_v1-computers-inventory-detail-id) for the Jamf Pro API. The API command to change the management status in a Jamf Pro computer inventory record to **Managed** should look similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -H "Content-Type: application/json" "[https://jamf.pro.server.here/api/v3/computers-inventory-detail/jamf\_pro\_computer\_ID\_goes\_here&quot](https://jamf.pro.server.here/api/v3/computers-inventory-detail/jamf_pro_computer_ID_goes_here%26quot); –header "Authorization: Bearer api\_token\_goes\_here" -X PATCH -d '{"general":{"managed":"true"}}' |

[view raw](https://gist.github.com/rtrouton/28c5b4e14ad50eb6d160e2301fe485ed/raw/b55e3d00b38c30a7714696250badad3b42fa2384/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/28c5b4e14ad50eb6d160e2301fe485ed#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

It’s sending the following JSON block to update the relevant computer inventory record and make the management change:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | { |
|  | "general": { |
|  | "managed": "true" |
|  | } |
|  | } |

[view raw](https://gist.github.com/rtrouton/1ba2d810bee6e4d112648fd46b88ab1e/raw/18e2d4e0419cd127a3e431e87f12e8033fdaf818/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/1ba2d810bee6e4d112648fd46b88ab1e#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The API command to change the management status in a Jamf Pro computer inventory record to **Not Managed** should look similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -H "Content-Type: application/json" "[https://jamf.pro.server.here/api/v3/computers-inventory-detail/jamf\_pro\_computer\_ID\_goes\_here&quot](https://jamf.pro.server.here/api/v3/computers-inventory-detail/jamf_pro_computer_ID_goes_here%26quot); –header "Authorization: Bearer api\_token\_goes\_here" -X PATCH -d '{"general":{"managed":"false"}}' |

[view raw](https://gist.github.com/rtrouton/cb6146215072663bb6af5d584fcc9d10/raw/cc13212efb42872e26366ae3d3416652f395561e/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/cb6146215072663bb6af5d584fcc9d10#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

It’s sending the following JSON block to update the relevant computer inventory record and make the management change:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | { |
|  | "general": { |
|  | "managed": "false" |
|  | } |
|  | } |

[view raw](https://gist.github.com/rtrouton/2a07e5f21f2644d4b38344e29424ddf1/raw/7f461c084990f0c1288099225e56330c2ebf57bb/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/2a07e5f21f2644d4b38344e29424ddf1#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

I was able to use the API information discussed above to create a couple of scripts which a) update the management status in specified computer inventory records and b) generates a report of the Macs whose computer inventory records were updated.

The scripts are named **Set\_Jamf\_Pro\_Computers\_To\_Managed\_Status.sh** and **Set\_Jamf\_Pro\_Computers\_To\_Unmanaged\_Status.sh** and are available via the links below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Set_Jamf_Pro_Computers_To_Managed>
<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Set_Jamf_Pro_Computers_To_Unmanaged>

Both scripts are designed to take in a set of Jamf Pro ID numbers in a plaintext file, where the Jamf Pro ID numbers correspond the Macs where you want to change the management status in their Jamf Pro computer inventory records. The plaintext file should look similar to this:

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

Four items are required to use these scripts:

* A text file containing the Jamf Pro IDs of the computer(s) you wish to delete.
* The URL of the appropriate Jamf Pr...