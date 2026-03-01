---
title: Using the Jamf Pro API to delete computers from Jamf Pro
url: https://derflounder.wordpress.com/2026/02/28/using-the-jamf-pro-api-to-delete-computers-from-jamf-pro/
source: Der Flounder
date: 2026-02-28
fetch_date: 2026-03-01T04:26:53.558787
---

# Using the Jamf Pro API to delete computers from Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using the Jamf Pro API to delete computers from Jamf Pro

## Using the Jamf Pro API to delete computers from Jamf Pro

February 28, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Every so often, I need to delete one or multiple computers from a Jamf Pro server. [This can be accomplished in the Jamf Pro admin console](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Deleting_a_Computer_from_Jamf_Pro.html), but it can also be accomplished via the Jamf Pro API’s [computers-inventory API endpoint](https://developer.jamf.com/jamf-pro/reference/delete_v3-computers-inventory-id). For more details, please see below the jump.

The API command to delete a computer inventory record from a Jamf Pro server should look similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl –header "Authorization: Bearer api\_token\_goes\_here" -X DELETE "[https://jamf.pro.server.here/api/v1/computers-inventory/jamf\_pro\_computer\_ID\_goes\_here&quot](https://jamf.pro.server.here/api/v1/computers-inventory/jamf_pro_computer_ID_goes_here%26quot); |

[view raw](https://gist.github.com/rtrouton/7c9682e41a3c74c010d32fc6c7a6b1df/raw/4fd6d9d7a73584d6525d6ddcee5cfa521d2887b1/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7c9682e41a3c74c010d32fc6c7a6b1df#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

I was able to use the API information discussed above to create a script which:

1. Deletes specified computer inventory records.
2. Generates a report of the Macs whose computer inventory records were deleted.

The script is named **Delete\_Computers\_From\_Jamf\_Pro.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Delete_Computers_From_Jamf_Pro>

The script is designed to take in a set of Jamf Pro ID numbers in a plaintext file, where the Jamf Pro ID numbers correspond the Macs you want to delete. The script can also accept one Jamf Pro ID number as input, if a plaintext file containing Jamf Pro ID numbers is not available.

Three items are required to use these scripts:

* The URL of the appropriate Jamf Pro server.
* The username of an account on the Jamf Pro server with sufficient privileges to delete computers from the Jamf Pro server.
* The password for the relevant account on the Jamf Pro server.

Jamf Pro account privileges required by the Jamf Pro server account referenced above:

**Jamf Pro Server Objects**:

* Computers: **Read**, **Delete**

If you want to delete multiple computers at once from Jamf Pro, you will also need to provide a plaintext file containing the Jamf Pro IDs of the computer you wish to delete. The plaintext file should look similar to this:

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

Once the specified items are available, the scripts can be run using the following commands:

To use **Delete\_Computers\_From\_Jamf\_Pro.sh** to delete one computer:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /path/to/Delete\_Computers\_From\_Jamf\_Pro.sh |

[view raw](https://gist.github.com/rtrouton/6f838bfa1a75c2691c11b76992a9e78f/raw/a43929419b9b62f408b0eb914630d0aee8c5ef7e/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/6f838bfa1a75c2691c11b76992a9e78f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To use **Delete\_Computers\_From\_Jamf\_Pro.sh** to delete multiple computers:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /path/to/Delete\_Computers\_From\_Jamf\_Pro.sh /path/to/plaintext\_filename\_here.txt |

[view raw](https://gist.github.com/rtrouton/8080ec130c71a6112faa206cdc876403/raw/e5ae58d637ef9f347bbf9c5de49172c0749877f8/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8080ec130c71a6112faa206cdc876403#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

When using **Delete\_Computers\_From\_Jamf\_Pro.sh** to delete one computer, you should see output that looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/Shared/Delete\_Computers\_From\_Jamf\_Pro/Delete\_Computers\_From\_Jamf\_Pro\_Status.sh |
|  | Please enter the relevant Jamf Pro ID number : 416462 |
|  | Please enter your Jamf Pro server URL : <https://jamf.pro.server.here> |
|  | Please enter your Jamf Pro user account : username\_goes\_here |
|  | Please enter the password for the username\_goes\_here account: |
|  | Requested computers are being deleted from <https://jamf.pro.server.here> |
|  | Report on deleted computers is being generated. File location will appear below once ready. |
|  | curl -X DELETE <https://jamf.pro.server.here/api/v1/computers-inventory/416462> |
|  | Deleted the computer inventory record for <https://jamf.pro.server.here/computers.html?id=416462>. |
|  |  |
|  | Report on deleted Macs available here: /var/folders/ps/2\_yw29gj711c9d7c5w5jhyv80000gp/T/tmp.rxRIIKNmx0.tsv |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/63e6c5c7096a393354f807b3e5fae217/raw/8126a84332922dfab6a44dbfd97450883324d597/deleting_individual_Jamf_Pro_ID_number.txt)
 [deleting\_individual\_Jamf\_Pro\_ID\_number.txt](https://gist.github.com/rtrouton/63e6c5c7096a393354f807b3e5fae217#file-deleting_individual_jamf_pro_id_number-txt)
hosted with ❤ by [GitHub](https://github.com)

As part of t...