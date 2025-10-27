---
title: Using the Jamf Pro API to download IPA files from a JCDS2 distribution point
url: https://derflounder.wordpress.com/2025/05/08/using-the-jamf-pro-api-to-download-ipa-files-from-a-jcds2-distribution-point/
source: Der Flounder
date: 2025-05-09
fetch_date: 2025-10-06T22:26:25.540055
---

# Using the Jamf Pro API to download IPA files from a JCDS2 distribution point

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Cloud Distribution Service](https://derflounder.wordpress.com/category/jamf-cloud-distribution-service/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using the Jamf Pro API to download IPA files from a JCDS2 distribution point

## Using the Jamf Pro API to download IPA files from a JCDS2 distribution point

May 8, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A while back, I wrote about how [you could use the Jamf Pro API to download installer packages from a JCDS2 distribution point](https://derflounder.wordpress.com/2024/02/24/using-the-jamf-pro-api-to-download-installer-packages-from-a-jcds2-distribution-point/).

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-08-at-3.40.png?w=595 "Screenshot 2025-05-08 at 3.40.png")

However, installer packages are not the only items which may be stored on a JCDS2 distribution point. The [IPA files](https://en.wikipedia.org/wiki/.ipa) used by [in-house iOS, iPadOS and tvOS devices](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/In-House_Apps.html) may also be stored for distribution on a JCDS2 distribution point. IPA files stored on a JCDS2 distribution point can be accessed for download in the same way that installer packages can.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-08-at-3.41.png?w=595 "Screenshot 2025-05-08 at 3.41.png")

For those who want to use this capability, I’ve written a script which uses the Jamf Pro Classic API and Jamf Pro API to get the list of IPA files on a Jamf Pro server, retrieve the associated download links and download the IPA files to a directory on my Mac. For more details, please see below the jump.

**Pre-requisites:**

If setting up a specific Jamf Pro user account for this purpose with limited rights, here are the required API privileges for the account on the Jamf Pro server:

**Jamf Pro Server Objects:**

* Mobile Device Apps: **Read**
* Jamf Content Distribution Server Files: **Read**

For authentication, the script can accept manual input or values stored in a **~/Library/Preferences/com.github.jamfpro-info.plist** file. The plist file can be created by running the following commands and substituting your own values where appropriate:

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

**Usage:**

**/path/to/Jamf\_Pro\_JCDS\_Mobile\_InHouseIPA\_Download.sh**

The script takes the following actions:

1. Creates a download directory if none has been specified in the script.
2. Uses the Jamf Pro Classic API to download the list of mobile device applications from the Jamf Pro server.
3. Gets the Jamf Pro ID numbers for the individual IPA files.
4. Uses the Jamf Pro Classic API to get the names of the individual IPA files.
5. Uses the Jamf Pro API to get the MD5 hash of the individual IPA files.
6. Checks to see if a file with a matching name and MD5 hash exists in the download directory.
7. If a file with a matching name and MD5 hash exists in the download directory, display a message that the file exists in the download directory.
8. If a file with a matching name and MD5 hash does not exist in the download directory, use the Jamf Pro API to query the JCDS2 distribution point for the download URL of the IPA file and download the IPA file.

The script should provide output similar to this:

**Downloading new copies of the IPA files where no copies currently exist**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/username/Jamf\_Pro\_JCDS\_Mobile\_InHouseIPA\_Download.sh |
|  | A location to store downloaded IPA files has not been specified. |
|  | Downloaded IPA files will be stored in /var/folders/zh/5bw3hvb93kdb3nwmwfjkhgsw0000gp/T/tmp.MAKKW8O0oo. |
|  | Please enter your Jamf Pro server URL : <https://jamfpro.server.here> |
|  | Please enter your Jamf Pro user account : apiuser |
|  | Please enter the password for the apiuser account: |
|  | /var/folders/zh/5bw3hvb93kdb3nwmwfjkhgsw0000gp/T/tmp.MAKKW8O0oo exists but is empty. Using existing directory for downloading IPA files. |
|  |  |
|  | Downloading AIM 1.0.ipa to /var/folders/zh/5bw3hvb93kdb3nwmwfjkhgsw0000gp/T/tmp.MAKKW8O0oo. |
|  | ######################################################################################################## 100.0% |
|  | AIM 1.0.ipa is available in /var/folders/zh/5bw3hvb93kdb3nwmwfjkhgsw0000gp/T/tmp.MAKKW8O0oo. |
|  |  |
|  | Downloading AMP 2.3.ipa to /var/folders/zh/5bw3hvb93kdb3nwmwfjkhgsw0000gp/T/tmp.MAKKW8O0oo. |
|  | ######################################################################################################## 100.0% |
|  | AMP 2.3.ipa is available in /var/folders/zh/5bw...