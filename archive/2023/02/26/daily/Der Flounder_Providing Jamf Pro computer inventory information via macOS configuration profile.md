---
title: Providing Jamf Pro computer inventory information via macOS configuration profile
url: https://derflounder.wordpress.com/2023/02/25/providing-jamf-pro-computer-inventory-information-via-macos-configuration-profile/
source: Der Flounder
date: 2023-02-26
fetch_date: 2025-10-04T08:08:00.715229
---

# Providing Jamf Pro computer inventory information via macOS configuration profile

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Providing Jamf Pro computer inventory information via macOS configuration profile

## Providing Jamf Pro computer inventory information via macOS configuration profile

February 25, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Jamf Pro can store and make available a lot of information about a particular computer and who is using it as part of the computer’s inventory record, but it can be challenging to access that information from the computer itself.

![Screenshot 2023-02-25 at 1.59.32 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-1.59.32-pm-1.png?w=595)

It is possible to use an API call to access this information, using either the [Jamf Pro API](https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview) or Jamf Pro’s [Classic API](https://developer.jamf.com/jamf-pro/docs/getting-started-2), but that means providing a way to [authenticate to the API](https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview#authentication-and-authorization). This may pose some security issues as you will need to both:

* Provide a way for the computer to access those authentication credentials
* Protect the authentication credentials from potentially malicious third parties

Fortunately, there is an alternative way to provide at least some inventory information without needing to make an API call. Jamf Pro provides [a number of variables which can be used in macOS configuration profiles](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/Computer_Configuration_Profiles.html) and it’s possible to leverage those variables to build a profile whose task is providing information from the computer’s inventory record in Jamf Pro in a way which can be accessed from the managed computer. For more details, please see below the jump.

The variables which are available to macOS configuration profiles as of Jamf Pro 10.44.0 are listed in the table shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Variable | Inventory Information |
| --- | --- | --- |
|  | $MANAGEMENTID | Device management ID assigned by Jamf Pro |
|  | $COMPUTERNAME | Computer Name |
|  | $SITENAME | Site Name |
|  | $SITEID | Site ID |
|  | $UDID | Computer UDID |
|  | $SERIALNUMBER | Computer Serial Number |
|  | $USERNAME | Username associated with the computer in Jamf Pro (computer-level profiles only)  Username of the user logging in to the computer (user-level profiles only) |
|  | $FULLNAME or $REALNAME | Full Name |
|  | $EMAIL | Email Address |
|  | $PHONE | Phone Number |
|  | $POSITION | Position |
|  | $DEPARTMENTNAME | Department Name |
|  | $DEPARTMENTID | Department ID |
|  | $BUILDINGNAME | Building Name |
|  | $BUILDINGID | Building ID |
|  | $ROOM | Room |
|  | $MACADDRESS | MAC Address |
|  | $JSSID | Jamf Pro ID |
|  | $PROFILEJSSID | Jamf Pro ID of the Configuration Profile |
|  | $EXTENSIONATTRIBUTE\_# | Extension Attribute ID Number  Note: The ID number is found in the extension attribute URL. In the example URL below,"id=2" indicates the extension attribute ID number:  <https://JAMF_PRO_URL.jamfcloud.com/computerExtensionAttributes.html?id=2&o=r> |

[view raw](https://gist.github.com/rtrouton/8e0e369605d0256afebd5da4afdca4f3/raw/d53833ce5ae6c5be8a15d3569897499cfeace355/jamf_pro_profile_variables.csv)
 [jamf\_pro\_profile\_variables.csv](https://gist.github.com/rtrouton/8e0e369605d0256afebd5da4afdca4f3#file-jamf_pro_profile_variables-csv)
hosted with ❤ by [GitHub](https://github.com)

I’ve used them to build a profile which will pull the information associated with the variables below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | $JSSID |
|  | $COMPUTERNAME |
|  | $MACADDRESS |
|  | $SERIALNUMBER |
|  | $UDID |
|  | $EMAIL |
|  | $REALNAME |
|  | $BUILDINGID |
|  | $BUILDINGNAME |
|  | $DEPARTMENTNAME |
|  | $DEPARTMENTID |
|  | $POSITION |
|  | $ROOM |
|  | $PHONE |
|  | $USERNAME |
|  | $SITENAME |
|  | $SITEID |

[view raw](https://gist.github.com/rtrouton/f1f2dd3e88246fb5719935e2b46f81bc/raw/8e3e058e1778c373339b09c80e34865eeb900ba8/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/f1f2dd3e88246fb5719935e2b46f81bc#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

When deployed, the profile will pull the relevant information from the computer record in Jamf Pro and store it as part of the profile.

![Screenshot 2023-02-25 at 2.06.24 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-2.06.24-pm-1.png?w=595)

![Screenshot 2023-02-25 at 2.06.25 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-2.06.25-pm-1.png?w=595)

This information in turn can be read from a plist file which should appear in the **/Library/Managed Preferences** directory on the managed Macs which the profile is being deployed to. In this case, the profile is managing the **com.company.information** domain, which means that a file named **com.company.information.plist** should appear in **/Library/Managed Preferences**.

![Screenshot 2023-02-25 at 2.01.05 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-2.01.05-pm-1.png?w=595)

This information can then be read out of the **/Library/Managed Preferences/com.company.information.plist** file by either the [defaults command](https://support.apple.com/guide/terminal/edit-property-lists-apda49a1bb2-577e-4721-8f25-ffc0836f6997/mac) or an alternate tool which can parse a plist file for information.

![Screenshot 2023-02-25 at 2.09.39 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-2.09.39-pm-1.png?w=595)

![Screenshot 2023-02-25 at 2.09.38 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-2.09.38-pm-1.png?w=595)

![Screenshot 2023-02-25 at 2.09.37 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-25-at-2.09.37-pm-1.png?w=595)

The example profile I’ve written is available below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1"> |
|  | <dict> |
|  | <key>PayloadUUID</key> |
|  | <string>6D198024...