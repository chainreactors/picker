---
title: Managing Safari extensions on macOS Sequoia using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/09/06/managing-safari-extensions-on-macos-sequoia-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-09-07
fetch_date: 2025-10-02T19:46:42.249149
---

# Managing Safari extensions on macOS Sequoia using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Safari](https://derflounder.wordpress.com/category/safari/) > Managing Safari extensions on macOS Sequoia using Blueprints in Jamf Pro

## Managing Safari extensions on macOS Sequoia using Blueprints in Jamf Pro

September 6, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro now provides with Blueprints is using DDM declarations to manage the [extensions](https://developer.apple.com/safari/extensions/) which can used by Apple’s [Safari web browser](https://www.apple.com/safari/). Let’s see how this works using the [Internet Archive](https://archive.org)‘s **Wayback Machine** Safari extension, which is available in the Mac App Store via the link below:

<https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12>

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-06-at-6.27.png?w=595 "Screenshot 2025-09-06 at 6.27.png")

For more details, please see below the jump.

Safari extensions can be managed using DDM declarations at the user level, which like with user-level MDM profiles, means that [they can be applied only to MDM-managed users](https://derflounder.wordpress.com/2025/04/04/identifying-mdm-managed-user-accounts-on-macos-sequoia/). When dealing with local accounts, this means that only the local user account which installs the MDM enrollment profile becomes the MDM-managed user. For our purposes here, this means that Safari extension management declarations can only be applied to the MDM-managed user and any other local accounts on the Mac cannot have their Safari extensions managed.

The following options are available for [Safari extension management](https://developer.apple.com/documentation/devicemanagement/safariextensionsettingsextensiondictionaryobject):

* **Allowed Domains**
* **Denied Domains**
* **Private Browsing**
* **State**

* **Allowed Domains**:
  + Controls the DNS domain(s) and sub-domain(s) that the extension is allowed to access.
* **Denied Domains**:
  + Controls the DNS domain(s) and sub-domain(s) that the extension is blocked from accessing.
* **Private Browsing**:
  + Controls whether or not the extension is allowed for use when using private browsing.
    - Options:
      * **Allowed**: The extension can be turned on or off when using private browsing.
      * **AlwaysOn**: The extension is always enabled when using private browsing if the extension is also enabled outside of private browsing.
      * **AlwaysOff**: The extension is never enabled when using private browsing, even if the extension is enabled outside of private browsing.
* **State**:
  + Controls whether an extension is allowed for use in general.
    - Options:
      * **Allowed**: The extension can be turned on or off.
      * **AlwaysOn**: The extension is always enabled.
      * **AlwaysOff**: The extension is never enabled.

**Note:**

For **Allowed Domains** and **Denied Domains**, [the following values are supported](https://developer.apple.com/documentation/devicemanagement/safariextensionsettings):

* Specific domain: Using a specific DNS domain name.
  + Example: **company.com** or **subdomain.company.com**
* Wildcard domain: Using a wildcard domain which uses a single asterix character ( **\*** ) as a prefix for the domain. This wildcard will allow both the top-level domain to be matched, as well as matching any sub-domains, with a wildcard domain entry like **\*company.com** being used to match against **company.com** as well as **subdomain.company.com**.
  + Example:  **\*company.com**
* Global wildcard: Uses a single asterix character ( **\*** ). This will match any DNS domain.
  + Example: **\***

You can also allow an extension to be specifically used on a specific or wildcarded domain, while blocking it for use on all other domains. For example, if you wanted to allow an extension to be used on the top-level **company.com** domain and all **company.com** subdomains, but block it on all others, you could define **Allowed Domains** and **Denied Domains** like this:

* Allowed Domains: **\*company.com**
* Denied Domains: **\***

For this example, we’re going to set the [Wayback Machine Safari extension](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12) to use [the following settings](https://support.apple.com/guide/deployment/safari-extensions-management-declarative-depff7fad9d8/web):

* Allowed Domains: **\***
* Private Browsing: **AlwaysOff**
* State: **Allowed**

This setting will do the following for the [Wayback Machine Safari extension](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12):

* Allow the extension to be used.
* Allow the extension to be used with all domains.
* Block the extension from being used with Safari’s [private browsing](https://support.apple.com/guide/safari/browse-privately-ibrw1069/mac) option, even when the extension is enabled outside of private browsing.

I can set up a Blueprint in Jamf Pro to deploy this Safari extension management configuration using the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Manage Safari extensions** box.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-06-at-6.28.png?w=595 "Screenshot 2025-09-06 at 6.28.png")

4. Give it a name when prompted. For this example, I’m using **Manage Wayback Machine Extension**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-06-at-6.28-1.png?w=595 "Screenshot 2025-09-06 at 6.28.png")

5. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Safari Extension Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-06-at-6.29.png?w=595 "Screenshot 2025-09-06 at 6.29.png")

6. At the following screen, we need to provide the identifier of the extension along with our settings.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-06-at-6.29-1.png?w=595 "Screenshot 2025-09-06 at 6.29.png")

To do this, we need to get the code signature of the Safari extension file. To obtain the code signature, once you have the extension’s file location, you will need to use the [codesign command line tool](https://ss64.com/mac/codesign.html) to run a command similar to the one below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | codesign -dv /path/to/extension\_goes\_here.appex |

[view raw](https://gist.github.com/rtrouton/6ab0d4da901cdd2fd93c34d9aaf00a48/raw/d47a34832f958cfc5dab065c25955458b309f833/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/6ab0d4da901cdd2fd93c34d9aaf00a48#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In the case of the **Wayback Machine** extension, the extension’s file is available in the following location:

**/Applications/Wayback Machine.app/Contents/PlugIns/Wayback Machine Extension.appex**

![...