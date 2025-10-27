---
title: Using the Jamf Pro agent to set computer name to match the Mac’s hardware serial number on macOS Sonoma
url: https://derflounder.wordpress.com/2024/08/07/using-the-jamf-pro-agent-to-set-computer-name-to-match-the-macs-hardware-serial-number-on-macos-sonoma/
source: Der Flounder
date: 2024-08-08
fetch_date: 2025-10-06T18:00:05.557245
---

# Using the Jamf Pro agent to set computer name to match the Mac’s hardware serial number on macOS Sonoma

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using the Jamf Pro agent to set computer name to match the Mac’s hardware serial number on macOS Sonoma

## Using the Jamf Pro agent to set computer name to match the Mac’s hardware serial number on macOS Sonoma

August 7, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

In a number of environments, Mac admins have chosen to use the Mac’s hardware serial number when naming the computer’s hostname (otherwise referred to as the computer name.) This is a task which the Jamf Pro agent includes built-in functionality for, using the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/local/jamf/bin/jamf setComputerName -useSerialNumber |

[view raw](https://gist.github.com/rtrouton/5a1192b59e9c9bbba2e5e69d231ec463/raw/3c273ee2a9bbff650da6729946117764ce1b76ff/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5a1192b59e9c9bbba2e5e69d231ec463#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For more information on this functionality, please run the following command on a Mac with the Jamf Pro agent installed:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | jamf help setComputerName |

[view raw](https://gist.github.com/rtrouton/3acaefd49fb8ee1ba97b280f1b42ba69/raw/602e6a40cdbf260a11a697c2fe77a23beba16972/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3acaefd49fb8ee1ba97b280f1b42ba69#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see the help information which is relevant to this command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % jamf help setComputerName |
|  |  |
|  | Usage: jamf setComputerName [-target <target volume>] [-name <name>] |
|  | [-useMACAddress] [-useSerialNumber] [-suffix <suffix>] |
|  | [-prefix <prefix>] [-fromFile <path to file>] |
|  |  |
|  |  |
|  | -target The target drive to set the name on |
|  |  |
|  | -name The new name for the computer |
|  |  |
|  | -useMACAddress Generate the name using the MAC Address |
|  |  |
|  | -useSerialNumber Generate the name using the Serial Number |
|  |  |
|  | -prefix Add this prefix to the MAC Address or Serial Number |
|  |  |
|  | -suffix Add this suffix to the MAC Address or Serial Number |
|  |  |
|  | -fromFile The path to a CSV file containing the computer's MAC Address or Serial Number followed by the desired name |
|  |  |
|  |  |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/891163ccfde3d1f8d8bc8c74d3a88034/raw/7ffd5a2c92a6fd441605c19188740ac8e1a1d127/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/891163ccfde3d1f8d8bc8c74d3a88034#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You can also use the [scutil command line tool](https://ss64.com/mac/scutil.html) for this task, if you don’t have the Jamf Pro agent installed. However, for the **scutil** tool, you would need to run the following commands to match the functionality as provided by the Jamf agent command listed above:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/scutil –set ComputerName serial\_number\_goes\_here |
|  | /usr/sbin/scutil –set LocalHostName serial\_number\_goes\_here |
|  | /usr/sbin/scutil –set HostName serial\_number\_goes\_here |

[view raw](https://gist.github.com/rtrouton/096fb6fb766b84574f5d154d7ae83ebf/raw/8ead16c917b6f6806cc309c5ab5976df472a436c/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/096fb6fb766b84574f5d154d7ae83ebf#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To have the serial number information be provided by the system, the following commands can be used:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/scutil –set ComputerName $(/usr/sbin/system\_profiler SPHardwareDataType | awk '/Serial Number/ { print $4; }') |
|  | /usr/sbin/scutil –set LocalHostName $(/usr/sbin/system\_profiler SPHardwareDataType | awk '/Serial Number/ { print $4; }') |
|  | /usr/sbin/scutil –set HostName $(/usr/sbin/system\_profiler SPHardwareDataType | awk '/Serial Number/ { print $4; }') |

[view raw](https://gist.github.com/rtrouton/b83b50289150faaeeb054a7bbcb7acc3/raw/a52d72290cdcdafaa8d30e6ebebf395b85d76ab4/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/b83b50289150faaeeb054a7bbcb7acc3#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For more information, please see below the jump.

To put all of what I discussed above together, I’ve written the following script which does the following:

1. Checks if the Jamf agent is installed and set as executable.
2. If the Jamf agent is installed and set as executable, the Jamf agent is used to set the hostname to match the Mac’s serial number.
3. If the Jamf agent is not installed or not set as executable, the **scutil** command line tool is used to set the hostname to match the Mac’s serial number.

This script is available below and also available on GitHub via the following link:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/set_computer_name_to_match_machine_serial_number>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # Sets the computer name to the machine's serial number. |
|  | # |
|  | # If the Jamf agent is installed, the script uses the Jamf agent to set |
|  | # the computer name to the machine's serial number. |
|  | # |
|  | # If the Jamf agent is not inst...