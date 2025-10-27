---
title: Using AutoPkg to build installers for Palo Alto’s GlobalProtect VPN software
url: https://derflounder.wordpress.com/2022/12/11/using-autopkg-to-build-installers-for-palo-altos-globalprotect-vpn-software/
source: Der Flounder
date: 2022-12-12
fetch_date: 2025-10-04T01:14:20.773552
---

# Using AutoPkg to build installers for Palo Alto’s GlobalProtect VPN software

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [AutoPkg](https://derflounder.wordpress.com/category/autopkg/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Packaging](https://derflounder.wordpress.com/category/packaging/) > Using AutoPkg to build installers for Palo Alto’s GlobalProtect VPN software

## Using AutoPkg to build installers for Palo Alto’s GlobalProtect VPN software

December 11, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of some recent testing, I needed to do some work with Palo Alto’s GlobalProtect VPN software. Palo Alto provides an installer package for GlobalProtect, but it has some interesting characteristics as the installer includes three installation options. One is enabled by default and the other two are disabled by default.

The first configuration is the option to install GlobalProtect, the default enabled configuration:

![Screenshot 2022 12 08 at 3 47 44 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-08-at-3.47.44-pm.png?w=595 "Screenshot 2022-12-08 at 3.47.44 PM.png")

The second configuration is the option to uninstall GlobalProtect, which is disabled by default:

![Screenshot 2022 12 08 at 3 49 18 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-08-at-3.49.18-pm.png?w=595 "Screenshot 2022-12-08 at 3.49.18 PM.png")

The third configuration is the option to enable the System Extension for GlobalProtect, which is disabled by default:

![Screenshot 2022 12 08 at 3 50 35 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-08-at-3.50.35-pm.png?w=595 "Screenshot 2022-12-08 at 3.50.35 PM.png")

**Note:** *In the image above, I’ve done some photoshopping because checking the third option to enable the System Extension for GlobalProtect also enables the option to install GlobalProtect. I made the change to the image to hopefully make more clear which option I was discussing.*

The options to uninstall GlobalProtect and enable the System Extension for GlobalProtect can be managed by using an [installer choices XML file](https://sneakypockets.wordpress.com/2017/07/26/using-installer-choices-xml-to-modify-anyconnect-and-mcafee-deployments/) to selectively enable only the desired option. For example, here’s the installer choices XML file for enabling only the option to uninstall GlobalProtect:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <array> |
|  | <dict> |
|  | <key>attributeSetting</key> |
|  | <integer>1</integer> |
|  | <key>choiceAttribute</key> |
|  | <string>selected</string> |
|  | <key>choiceIdentifier</key> |
|  | <string>second</string> |
|  | </dict> |
|  | <dict> |
|  | <key>attributeSetting</key> |
|  | <integer>1</integer> |
|  | <key>choiceAttribute</key> |
|  | <string>selected</string> |
|  | <key>choiceIdentifier</key> |
|  | <string>com.paloaltonetworks.globalprotect.uninstall.pkg</string> |
|  | </dict> |
|  | </array> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/9dc481681656cafbbe513992f4f34696/raw/c5592d373aeeb1c74fadb1c9b76428dc05c8f31c/uninstall_global_protect.xml)
 [uninstall\_global\_protect.xml](https://gist.github.com/rtrouton/9dc481681656cafbbe513992f4f34696#file-uninstall_global_protect-xml)
hosted with ❤ by [GitHub](https://github.com)

Here’s the installer choices XML file for enabling only the option to enable the System Extension for GlobalProtect:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <array> |
|  | <dict> |
|  | <key>attributeSetting</key> |
|  | <integer>1</integer> |
|  | <key>choiceAttribute</key> |
|  | <string>selected</string> |
|  | <key>choiceIdentifier</key> |
|  | <string>third</string> |
|  | </dict> |
|  | <dict> |
|  | <key>attributeSetting</key> |
|  | <integer>1</integer> |
|  | <key>choiceAttribute</key> |
|  | <string>selected</string> |
|  | <key>choiceIdentifier</key> |
|  | <string>com.paloaltonetworks.globalprotect.systemext.pkg</string> |
|  | </dict> |
|  | </array> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/837a1107117a978c162928d0c014e88b/raw/1677e50fba564c7f67c4a4853ba17124ba5644f7/install_system_extensions.xml)
 [install\_system\_extensions.xml](https://gist.github.com/rtrouton/837a1107117a978c162928d0c014e88b#file-install_system_extensions-xml)
hosted with ❤ by [GitHub](https://github.com)

Using these options, I was able to build recipes for AutoPkg which would automatically build three installer packages:

* An installer which installs GlobalProtect.
* An installer which uninstalls GlobalProtect.
* An installer which enables the System Extension for GlobalProtect.

The reason I chose to do this is that using AutoPkg to create these additional installer packages should help ensure any changes that Palo Alto makes to GlobalProtect’s uninstall and System Extension enablement will automatically be available whenever a new version of GlobalProtect is picked up by AutoPkg. In turn, this should save work for those deploying GlobalProtect because now they don’t need to figure out what may have changed between GlobalProtect releases. For more details, please see below the jump.

There is an existing AutoPkg **.download** recipe for GlobalProtect, available via the link below:

<https://github.com/autopkg/peshay-recipes/blob/master/PaloAlto/GlobalProtect.download.recipe>

Since that part of the recipe setup is already done, I focused on building AutoPkg **.pkg** recipes. For the example recipe shown below which handles creating the installer which installs GlobalProtect, the recipe won’t make any changes to the downloaded installer package beyond renaming it. This is because by default, the GlobalProtect installer package installs GlobalProtect.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>Description</key> |
|  | <str...