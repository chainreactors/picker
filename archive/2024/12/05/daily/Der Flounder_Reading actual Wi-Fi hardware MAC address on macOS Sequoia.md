---
title: Reading actual Wi-Fi hardware MAC address on macOS Sequoia
url: https://derflounder.wordpress.com/2024/12/04/reading-actual-wi-fi-hardware-mac-address-on-macos-sequoia/
source: Der Flounder
date: 2024-12-05
fetch_date: 2025-10-06T19:36:44.656198
---

# Reading actual Wi-Fi hardware MAC address on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Reading actual Wi-Fi hardware MAC address on macOS Sequoia

## Reading actual Wi-Fi hardware MAC address on macOS Sequoia

December 4, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the privacy protections Apple introduced for macOS as part of macOS Sequoia is [MAC address randomization](https://support.apple.com/guide/security/wi-fi-privacy-secb9cb3140c/web). This address randomization is a privacy feature which Apple first introduced for mobile devices in iOS / iPadOS 14 and later, as well as watchOS 7 and later, which enables a unique randomly generated [MAC address](https://en.wikipedia.org/wiki/MAC_address) to be provided to Wi-Fi networks when an Apple device connects via Wi-Fi to the Wi-Fi network. The reason for doing this is to [prevent the Apple device from being tracked as it connects to public Wi-Fi networks](https://macadmin.fraserhess.com/2024/09/16/handling-mac-address-randomization-in-macos-15), as each Wi-Fi network will receive a new MAC address from the Apple device every time it connects to the Wi-Fi network in question.

For shops which want to disable the MAC address randomization for their own Wi-Fi networks, Apple has provided a [DisableAssociationMACRandomization management setting](https://developer.apple.com/documentation/devicemanagement/wifi) which is available for use in iOS 14 and later, macOS 15 and later, and watchOS 7 and later. However, for shops which don’t want to disable this privacy protection but still want to be able to find out what the actual MAC address of the Wi-Fi network interface on Macs running macOS Sequoia and later, it’s possible to use the [networksetup](https://ss64.com/mac/networksetup.html) tool to do so. (Hat tip to everyone in the Mac Admins Slack who helped with figuring this out.) For more information, please see below the jump.

Assuming the Wi-Fi network interface on your Mac has been assigned the display name of **Wi-Fi**, you can get the actual MAC address using the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/networksetup -getmacaddress Wi-Fi |

[view raw](https://gist.github.com/rtrouton/ef82035e919fb4ec1c9f37811a322cef/raw/9632ec0cc5b97646ee0f63c50558386491796ace/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/ef82035e919fb4ec1c9f37811a322cef#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/networksetup -getmacaddress Wi-Fi |
|  | Ethernet Address: 6c:ce:2e:d3:6b:bd (Hardware Port: Wi-Fi) |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/bf1eca30c5b82fba180bb3605272a117/raw/ddbb015b90ccce24c24e421b85a412efe68090c8/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/bf1eca30c5b82fba180bb3605272a117#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If you want only the MAC address returned, you can use the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/networksetup -getmacaddress $(/usr/sbin/networksetup -listallhardwareports | awk '/Hardware Port: Wi-Fi/{getline; print $2}') | awk '{print $3}' |

[view raw](https://gist.github.com/rtrouton/8b82f9b359fcd042d499603074626d9d/raw/7b4551ad538f4d52829f04f33a30128d266367e2/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8b82f9b359fcd042d499603074626d9d#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/networksetup -getmacaddress $(/usr/sbin/networksetup -listallhardwareports | awk '/Hardware Port: Wi-Fi/{getline; print $2}') | awk '{print $3}' |
|  | 6c:ce:2e:d3:6b:bd |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/410d6876ae897057a1bc90244e0cc3a4/raw/197e5c490233756455c28375d93bef35d1a1c3b6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/410d6876ae897057a1bc90244e0cc3a4#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If you want only the MAC address returned with all the colons ( **:** ) removed, you can use the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/networksetup -getmacaddress $(/usr/sbin/networksetup -listallhardwareports | awk '/Hardware Port: Wi-Fi/{getline; print $2}') | awk '{print $3}' | tr -d ':' |

[view raw](https://gist.github.com/rtrouton/7684610fbb75ede8ca2e47d32af017fe/raw/5c062dcf9bc49c6593f84f1faccce39c6fe14444/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7684610fbb75ede8ca2e47d32af017fe#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/networksetup -getmacaddress $(/usr/sbin/networksetup -listallhardwareports | awk '/Hardware Port: Wi-Fi/{getline; print $2}') | awk '{print $3}' | tr -d ':' |
|  | 6cce2ed36bbd |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/1dcef83c130c0ee34308e166265a8180/raw/31fcebcd7e3074f6632116bc90b40577dd5edef9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/1dcef83c130c0ee34308e166265a8180#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in n...