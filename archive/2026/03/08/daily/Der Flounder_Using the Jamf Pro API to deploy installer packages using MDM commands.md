---
title: Using the Jamf Pro API to deploy installer packages using MDM commands
url: https://derflounder.wordpress.com/2026/03/08/using-the-jamf-pro-api-to-deploy-installer-packages-using-mdm-commands/
source: Der Flounder
date: 2026-03-08
fetch_date: 2026-03-09T04:08:05.491059
---

# Using the Jamf Pro API to deploy installer packages using MDM commands

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Using the Jamf Pro API to deploy installer packages using MDM commands

## Using the Jamf Pro API to deploy installer packages using MDM commands

March 8, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the capabilities of mobile device management (MDM) on macOS is that you can use MDM commands to deploy installer packages, via the [InstallEnterpriseApplication](https://developer.apple.com/documentation/devicemanagement/installenterpriseapplicationcommand/command-data.dictionary) MDM command. If you’re using Jamf Pro for your MDM management, one of the capabilities of the Jamf Pro API is being able to leverage its ability to run MDM commands to send out InstallEnterpriseApplication commands to deploy installer packages. For more details, please see below the jump.

The relevant Jamf Pro API endpoint is the [v1/deploy-package endpoint](https://developer.jamf.com/jamf-pro/reference/post_v1-deploy-package). Here are the required API permissions for using it:

API permissions using user account authentication:

**Jamf Pro Server Objects**:

* Computers: **Read**, **Update**

**Jamf Pro Server Actions**:

* **Send Computer Remote Command to Install Package**
* **Send MDM command information in Jamf Pro API**
* **View MDM command information in Jamf Pro API**

API permissions using API client authentication:

* **Read Computers**
* **Update Computers**
* **Send Computer Remote Command to Install Package**
* **Send MDM command information in Jamf Pro API**
* **View MDM command information in Jamf Pro API**

Installer packages deployed using this method would need to be signed and built as a distribution-style package. I have a blog post describing the details available via the link below:

<https://derflounder.wordpress.com/2023/10/24/preparing-installer-packages-for-installation-using-mdm-commands/>

If you look at the Jamf Pro API documentation available with Jamf Pro, using the **v1/deploy-package** Jamf Pro API endpoint to successfully deploy a package requires sending a JSON block containing a manifest for the package along with some additional information on whether or not the package is set to be managed and which devices to install it on. Let’s take a look at the essential components of this block, using an example provided as part of the Jamf API documentation:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | { |
|  | "manifest": { |
|  | "url": "[https://example.jamf.com/this/package&quot](https://example.jamf.com/this/package%26quot);, |
|  | "hash": "dcb02a41cd6d842943459a88c96a5f72", |
|  | "hashType": "MD5", |
|  | "displayImageUrl": "[https://example.jamf.com/img/display/this/package.jpg&quot](https://example.jamf.com/img/display/this/package.jpg%26quot);, |
|  | "fullSizeImageUrl": "[https://example.jamf.com/img/full/this/package.jpg&quot](https://example.jamf.com/img/full/this/package.jpg%26quot);, |
|  | "bundleId": "com.jamf.example", |
|  | "bundleVersion": "0.1.0", |
|  | "subtitle": "Subtitle", |
|  | "title": "Title", |
|  | "sizeInBytes": 12345 |
|  | }, |
|  | "installAsManaged": false, |
|  | "devices": [ |
|  | 1, |
|  | 2, |
|  | 3 |
|  | ], |
|  | "groupId": "1" |
|  | } |

[view raw](https://gist.github.com/rtrouton/7e708d17a1e7fafe5f8b3ad0548446b9/raw/ce2205826990ebeb4fa348ff6597d11ddad0e671/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7e708d17a1e7fafe5f8b3ad0548446b9#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This has several parts, so let’s break it down by section:

Manifest:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | "manifest": { |
|  | "url": "[https://example.jamf.com/this/package&quot](https://example.jamf.com/this/package%26quot);, |
|  | "hash": "dcb02a41cd6d842943459a88c96a5f72", |
|  | "hashType": "MD5", |
|  | "displayImageUrl": "[https://example.jamf.com/img/display/this/package.jpg&quot](https://example.jamf.com/img/display/this/package.jpg%26quot);, |
|  | "fullSizeImageUrl": "[https://example.jamf.com/img/full/this/package.jpg&quot](https://example.jamf.com/img/full/this/package.jpg%26quot);, |
|  | "bundleId": "com.jamf.example", |
|  | "bundleVersion": "0.1.0", |
|  | "subtitle": "Subtitle", |
|  | "title": "Title", |
|  | "sizeInBytes": 12345 |
|  | }, |

[view raw](https://gist.github.com/rtrouton/41b9463889bd73261090f1d38453c18b/raw/a37333c52c8ca8d3f9d51ac6c458c485def319bd/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/41b9463889bd73261090f1d38453c18b#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This is providing the MDM command’s information about the package to be installed. Here are the essential parts you need to provide as part of the manifest:

* **URL**: The installer package will need to be hosted on an available location which allows anonymous HTTPS downloads (i.e. downloading via HTTPS without requiring authentication.)
* **Hash**: This is a unique, fixed-length string generated by running an file’s data (in this case an installer package) through a cryptographic algorithm like [MD5](https://en.wikipedia.org/wiki/MD5) or [SHA256](https://en.wikipedia.org/wiki/SHA-2).
* **Hash Type**: This is the cryptographic algorithm being used. Either MD5 or SHA256 is supported.

Note: The hash type description must use capitalization. No lowercase letters allowed in this use case.

* **Bundle ID**: For an installer package, this is the unique, reverse-DNS identifier (for example, **com.example.app**) used to identify macOS installer packages.
* **Bundle Version**: For an installer package, this is the version of the installer package. Packages with the same package identifier are compared using this version, to determine if the package is an upgrade or downgrade.
* **Title**: This is the title of the package being installed
* **Size in Bytes**: This is the size in bytes of the installer package.

For more information on the topic of creating a manifest for installer packages deployed using the **InstallEnterpriseApplication** MDM command, please see the link below:

<https://www.dersoldat.org/?p=1456>

Next, there’s the choice to install as managed or not:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | "installAsManaged": false, |

[view raw](h...