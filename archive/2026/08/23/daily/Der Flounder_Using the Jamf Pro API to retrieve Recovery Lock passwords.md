---
title: Using the Jamf Pro API to retrieve Recovery Lock passwords
url: https://derflounder.wordpress.com/2026/08/23/using-the-jamf-pro-api-to-retrieve-recovery-lock-passwords/
source: Der Flounder
date: 2026-08-23
fetch_date: 2026-08-24T02:58:52.385566
---

# Using the Jamf Pro API to retrieve Recovery Lock passwords

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/) > Using the Jamf Pro API to retrieve Recovery Lock passwords

## Using the Jamf Pro API to retrieve Recovery Lock passwords

August 23, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

A while back, [I wrote a script which uses Jamf Pro’s Classic and Jamf Pro API to retrieve FileVault recovery keys](https://derflounder.wordpress.com/2023/01/25/using-the-jamf-pro-api-to-retrieve-filevault-personal-recovery-keys/). As part of assisting with a recent issue, I decided to develop a similar one for retrieving [Recovery Lock passwords](https://support.apple.com/guide/deployment/startup-security-dep5810e849c/web) (these are alternatively referred to in Apple’s documentation as **recoveryOS passwords**.) The resulting script uses the Jamf Pro API to take a list of Jamf Pro computer IDs from a plaintext file, retrieve the associated Macs’ Recovery Lock passwords (if one is set) and generate a report in [TSV format](https://en.wikipedia.org/wiki/Tab-separated_values).

For more details, please see below the jump.

**Pre-requisites:**

If setting up an API client for this purpose with limited rights, here are the required API Role privileges for the API client on the Jamf Pro server:

* **Read Computers**
* **View Recovery Lock**

For authentication, the script can accept manual input or values stored in a **~/Library/Preferences/com.github.jamfpro-info.plist** file.

The plist file can be created by running the following commands and substituting your own values where appropriate:

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

To store the API Client ID in the plist file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | defaults write com.github.jamfpro-info jamfpro\_api\_client\_id api\_client\_id\_information\_goes\_here |

[view raw](https://gist.github.com/rtrouton/77a8e5d6ad182d7395a4e44f49b41459/raw/351f942cac39582eb3db541c7932abd860fe336f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/77a8e5d6ad182d7395a4e44f49b41459#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To store the API Client Secret in the plist file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | defaults write com.github.jamfpro-info jamfpro\_api\_client\_secret api\_client\_secret\_information\_goes\_here |

[view raw](https://gist.github.com/rtrouton/29c97e6c736513fb0a6669d1fc7549a1/raw/971858ee6e055c169aeab4d063b95af1bd143c57/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/29c97e6c736513fb0a6669d1fc7549a1#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This script imports a list of Jamf Pro computer ID numbers from a plaintext file and uses that information to generate a report about the Recovery Lock passwords associated with those computers. The plaintext file format should look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 19 |
|  | 55 |
|  | 72 |
|  | 93 |

[view raw](https://gist.github.com/rtrouton/b06733deb944207e7ca924058f55bb69/raw/4f06ed4b6d26ea9f7fcd8163c168ccf70ff0f410/jamf_pro_id_numbers.txt)
 [jamf\_pro\_id\_numbers.txt](https://gist.github.com/rtrouton/b06733deb944207e7ca924058f55bb69#file-jamf_pro_id_numbers-txt)
hosted with ❤ by [GitHub](https://github.com)

**Usage:**

**/path/to/generate\_filevault\_recovery\_key\_report\_from\_jamf\_pro\_id\_numbers /path/to/jamf\_pro\_id\_numbers.txt**

Once the Jamf Pro computer ID numbers are read from in from the plaintext file, the script takes the following actions:

1. Uses the Jamf Pro API to download all information about the matching computer inventory record.
2. Pulls the following information out of the inventory entry:

* Jamf Pro ID
* Manufacturer
* Model
* Serial Number
* Hardware UDID

3. Runs a separate API call to retrieve the following:

* Recovery Lock Password

4. Create a report in tab-separated value (.tsv) format which contains the following information about the deleted Macs

* Jamf Pro ID
* Manufacturer
* Model
* Serial Number
* Hardware UDID
* Recovery Lock Password Available
* Recovery Lock Password (if no password is set, **NA** is reported for the **Recovery Lock Password** column.)
* Jamf Pro URL for the computer inventory record

The script should display output similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/Shared/Generate\_Recovery\_Lock\_Password\_Report\_From\_Jamf\_Pro\_ID\_Numbers.sh jamf\_pro\_id\_numbers.txt |
|  | Please enter your Jamf Pro server URL : <https://jamf.pro.server.here> |
|  | Please enter your Jamf Pro API client ID : 52d62208-4eb8-45f9-af54-5aa2e4273029 |
|  | Please enter the API client secret for the 52d62208-4eb8-45f9-af54-5aa2e4273029 API ID client: |
|  | Report being generated. File location will appear below once ready. |
|  | Report on Recovery Lock passwords available here: /var/folders/ps/2\_yw29gj711c9d7c5w5jhyv80000gp/T/tmp.6YgzNdcgqV.tsv |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/31f533cff4316dd6da96173fc5d57509/raw/47c223647ef7f6f2214a7b3e9a5a4cccac755068/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/31f533cff4316dd6da96173fc5d57509#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The resulting report in [TSV format](https://en.wikipedia.org/wiki/Tab-separated_values) will contain information similar to what’s shown below:

This file contains hidden or bidirec...