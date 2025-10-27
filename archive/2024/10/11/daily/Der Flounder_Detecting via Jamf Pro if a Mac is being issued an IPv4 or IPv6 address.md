---
title: Detecting via Jamf Pro if a Mac is being issued an IPv4 or IPv6 address
url: https://derflounder.wordpress.com/2024/10/10/detecting-via-jamf-pro-if-a-mac-is-being-issued-an-ipv4-or-ipv6-address/
source: Der Flounder
date: 2024-10-11
fetch_date: 2025-10-06T18:46:16.101602
---

# Detecting via Jamf Pro if a Mac is being issued an IPv4 or IPv6 address

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Detecting via Jamf Pro if a Mac is being issued an IPv4 or IPv6 address

## Detecting via Jamf Pro if a Mac is being issued an IPv4 or IPv6 address

October 10, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

I assisted a colleague recently with an interesting request – how to detect if a Mac is only being issued an [IPv6 address](https://en.wikipedia.org/wiki/IPv6)? In this instance, the use case was for when a Mac is on a network where only IPv6 addresses are being issued by DHCP (so no [IPv4 addresses](https://en.wikipedia.org/wiki/IPv4) are available.)

The idea was to get a **Yes** or **No** answer for whether any of the Mac’s network interfaces were being issued an IPv4 address, where **Yes** meant that at least one network interface had an IPv4 IP address and **No** if none of the network interfaces had an IPv4 IP address.

After some research and discussion with colleagues in the Mac Admins Slack, this information was available via the [system\_profiler command line tool](https://ss64.com/mac/system_profiler.html), using the **SPNetworkDataType** datatype. You can parse the output from the **system\_profiler** tool using the following command to get a count of how many IPv4 addresses are in use by the various network interfaces on a Mac:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/system\_profiler SPNetworkDataType | /usr/bin/grep -c "IPv4 Addresses:" |

[view raw](https://gist.github.com/rtrouton/715c2477803fc0ce73c4c0581305c472/raw/39fffedcf85e7de3ae4b2230e0ecaf71ed090194/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/715c2477803fc0ce73c4c0581305c472#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For example, if your Mac has IPv4 IP addresses assigned to both Ethernet and Wi-Fi, you should see output like this to show that your Mac has two assigned IPv4 addresses (one for Ethernet and one for Wi-Fi):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/system\_profiler SPNetworkDataType | /usr/bin/grep -c "IPv4 Addresses:" |
|  | 2 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/9b3892bc801b35353118b1842e2fc5f7/raw/07e58f3e474da30759fb765a9b02b16e7871f143/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9b3892bc801b35353118b1842e2fc5f7#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This same approach works for IPv6 addresses, where you can parse the output from system\_profiler using the following command to get a count of how many IPv6 addresses are in use by the various network interfaces on a Mac:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/system\_profiler SPNetworkDataType | /usr/bin/grep -c "IPv6 Addresses:" |

[view raw](https://gist.github.com/rtrouton/be8616822f51e0a993b89d7a041ef1b6/raw/8ff8754acbf881d395078a1b58c1cfed7d6d4288/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/be8616822f51e0a993b89d7a041ef1b6#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For example, if your Mac has no IPv6 IP addresses assigned to any network interfaces, you should see output like this to show that your Mac has no assigned IPv6 addresses:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/system\_profiler SPNetworkDataType | /usr/bin/grep -c "IPv6 Addresses:" |
|  | 0 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/4fb61cd3d407ad31488d0dfb443814fb/raw/d0c1b7de254de24a667d2f5d21576e80188f0c54/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/4fb61cd3d407ad31488d0dfb443814fb#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

I’ve used this technique to create Jamf Pro Extension Attributes which can help figure out if a particular Mac has IPv4 or IPv6 addresses assigned to it, which can help in the use case I discussed earlier to help figure out if no IPv4 or no IPv6 addresses are available to a particular Mac. For more details, please see below the jump.

I’ve written two Extension Attributes, one for detecting IPv4 addresses and the other for IPv6 addresses. Here’s how they work:

Detects if an IPv4 / IPv6 network address is being used on a Mac. It returns the value below if one or more IPv4 / IPv6 addresses are detected on the Mac’s various network interfaces.

**1**

In all other cases, the value below is returned:

**0**

The Extension Attribute’s returned value ( **1** or **0** ) can then be used as Jamf Pro smart group criteria.

IPv4 version of the Extension Attribute:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Extension_Attributes/check_for_IPv4_address_used_on_Mac>

![IPv4 Jamf Pro Extension Attribute Setup.](https://derflounder.wordpress.com/wp-content/uploads/2024/10/ipv4_jamf_pro_extension_attribute_setup.png?w=595 "IPv4_Jamf_Pro_Extension_Attribute_Setup.png")

IPv6 version of the extension attribute:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Extension_Attributes/check_for_IPv6_address_used_on_Mac>

![IPv6 Jamf Pro Extension Attribute Setup.](https://derflounder.wordpress.com/wp-content/uploads/2024/10/ipv6_jamf_pro_extension_attribute_setup.png?w=595 "IPv6_Jamf_Pro_Extension_Attribute_Setup.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/10/10/detecting-via-jamf-pro-if-a-mac-is-being-issued-an-ipv4-or-ipv6-address/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/10/10/detecting-via-jamf-pro-if-a-mac-is-being-issued-an-ipv4-or-ipv6-address/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/10/10/detecting-via-jamf-pro-if-a-mac-is-being-issued-an-ipv4-or-ipv6-address/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounde...