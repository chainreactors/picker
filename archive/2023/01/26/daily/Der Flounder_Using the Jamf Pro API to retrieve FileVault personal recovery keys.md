---
title: Using the Jamf Pro API to retrieve FileVault personal recovery keys
url: https://derflounder.wordpress.com/2023/01/25/using-the-jamf-pro-api-to-retrieve-filevault-personal-recovery-keys/
source: Der Flounder
date: 2023-01-26
fetch_date: 2025-10-04T04:51:23.732723
---

# Using the Jamf Pro API to retrieve FileVault personal recovery keys

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using the Jamf Pro API to retrieve FileVault personal recovery keys

## Using the Jamf Pro API to retrieve FileVault personal recovery keys

January 25, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Jamf Pro 10.43’s release, Jamf has added the ability to access and retrieve FileVault personal recovery keys via the Jamf Pro API:

* **Return FileVault information for a specific computer**: [https://developer.jamf.com/jamf-pro/reference/get\_v1-computers-inventory-id-filevault](https://developer.jamf.com/jamf-pro/reference/get_v1-computers-inventory-filevault)
* **Return paginated FileVault information for all computers**: <https://developer.jamf.com/jamf-pro/reference/get_v1-computers-inventory-filevault>

For those who want to use this new capability, I’ve written a script which uses the Jamf Pro Classic API and Jamf Pro API to take a list of Jamf Pro computer IDs from a plaintext file, retrieve the associated Macs’ FileVault personal recovery keys and generate a report in .tsv format.

For more details, please see below the jump.

**Pre-requisites:**

If setting up a specific Jamf Pro user account for this purpose with limited rights, here are the required API privileges for the account on the Jamf Pro server:

**Jamf Pro Server Objects:**

* Computers: **Read**

**Jamf Pro Server Actions:**

* **View Disk Encryption Recovery Key**

For authentication, the script can accept manual input or values stored in a **~/Library/Preferences/com.github.jamfpro-info.plist** file. The plist file can be created by running the following commands and substituting your own values where appropriate:

To store the Jamf Pro URL in the plist file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | defaults write com.github.jamfpro-info jamfpro\_url <https://jamf.pro.server.goes.here:port_number_goes_here> |

[view raw](https://gist.github.com/rtrouton/aef7088969297b4c788caa2b009c4a4d/raw/6e7f9d3c0f766a41e9d9b6eade016291a498c7b2/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/aef7088969297b4c788caa2b009c4a4d#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To store the account username in the plist file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | defaults write com.github.jamfpro-info jamfpro\_user account\_username\_goes\_here |

[view raw](https://gist.github.com/rtrouton/9951d9af0b9bdacddd89c2502f34f694/raw/0a7ed6fa8ef76b2414ba3fde5a4ed8599ee587a3/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9951d9af0b9bdacddd89c2502f34f694#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To store the account password in the plist file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | defaults write com.github.jamfpro-info jamfpro\_password account\_password\_goes\_here |

[view raw](https://gist.github.com/rtrouton/358d9b52bcb9915fdfe5e0b4994f7e7a/raw/56d029ec5e697aff7a066573a57ad74e60212632/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/358d9b52bcb9915fdfe5e0b4994f7e7a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This script imports a list of Jamf Pro computer ID numbers from a plaintext file and uses that information to generate a report about the FileVault personal recovery keys associated with those computers. The plaintext file format should look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 13 |
|  | 86 |
|  | 87 |
|  | 85 |

[view raw](https://gist.github.com/rtrouton/1733ab8ee0b9eb8add3ad64b92da6b24/raw/e0da6313daf0aabab7d72df610717fb9b21c3865/jamf_pro_id_numbers.txt)
 [jamf\_pro\_id\_numbers.txt](https://gist.github.com/rtrouton/1733ab8ee0b9eb8add3ad64b92da6b24#file-jamf_pro_id_numbers-txt)
hosted with ❤ by [GitHub](https://github.com)

**Usage:**

**/path/to/generate\_filevault\_recovery\_key\_report\_from\_jamf\_pro\_id\_numbers /path/to/jamf\_pro\_id\_numbers.txt**

![Screenshot 2023 01 25 at 4 27 23 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/01/screenshot-2023-01-25-at-4.27.23-pm.png?w=595 "Screenshot 2023-01-25 at 4.27.23 PM.png")

Once the Jamf Pro computer ID numbers are read from in from the plaintext file, the script takes the following actions:

1. Uses the Jamf Pro API to download all information about the matching computer inventory record in XML format.

2. Pulls the following information out of the inventory entry:

* Manufacturer
* Model
* Serial Number
* Hardware UDID

3. Runs a separate API call to retrieve the following in JSON format.

* FileVault personal recovery key

4. Create a report in tab-separated value (.tsv) format which contains the following information about the deleted Macs

* Jamf Pro ID
* Manufacturer
* Model
* Serial Number
* Hardware UDID
* FileVault personal recovery key if available
* Jamf Pro URL for the computer inventory record

The resulting report in .tsv format will contain information similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Jamf Pro ID Number | Make | Model | Serial Number | UDID | FileVault Recovery Key Available | FileVault Recovery Key | Jamf Pro URL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 13 | Apple | Mac mini (Mid 2011) | C07GM01TDJD0 | 00BC7701-6791-573D-B461-470B44D16DF6 | No | NA | <https://jamfpro.pretendco.com:8443/computers.html?id=13> |
|  | 86 | Apple | iMac Pro Intel (Retina 5k, 27-inch, Late 2017) | VM0N0WRc4EjC | 564D33BC-AF4C-86CF-1DFB-AF6EDFC395A3 | Yes | 3CZZ-OB8K-...