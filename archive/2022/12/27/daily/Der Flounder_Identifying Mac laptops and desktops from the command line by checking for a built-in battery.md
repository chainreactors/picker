---
title: Identifying Mac laptops and desktops from the command line by checking for a built-in battery
url: https://derflounder.wordpress.com/2022/12/26/identifying-mac-laptops-and-desktops-from-the-command-line-by-checking-for-a-built-in-battery/
source: Der Flounder
date: 2022-12-27
fetch_date: 2025-10-04T02:31:50.334025
---

# Identifying Mac laptops and desktops from the command line by checking for a built-in battery

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Identifying Mac laptops and desktops from the command line by checking for a built-in battery

## Identifying Mac laptops and desktops from the command line by checking for a built-in battery

December 26, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Every so often, it may be necessary for Mac admins to deploy a script that can apply different settings to Mac desktops and laptops. A good example may be using the [pmset command](https://ss64.com/osx/pmset.html) to apply Energy Saver settings, where you may want to apply one set of power management settings to laptops and a different set to desktops.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # Set separate power management settings for desktops and laptops |
|  | # If it's a laptop, the power management settings for "Battery" are set to have the computer sleep in 15 minutes, |
|  | # disk will spin down in 10 minutes, the display will sleep in 5 minutes and the display itself will dim to |
|  | # half-brightness before sleeping. While plugged into the AC adapter, the power management settings for "Charger" |
|  | # are set to have the computer never sleep, the disk doesn't spin down, the display sleeps after 30 minutes and |
|  | # the display dims before sleeping. |
|  | # |
|  | # If it's not a laptop (i.e. a desktop), the power management settings are set to have the computer never sleep, |
|  | # the disk doesn't spin down, the display sleeps after 30 minutes and the display dims before sleeping. |
|  | # |
|  |  |
|  | # Detects if this Mac is a laptop or not by checking the model ID for the word "Book" in the name. |
|  | IS\_LAPTOP=$(/usr/sbin/system\_profiler SPHardwareDataType | grep "Model Identifier" | grep "Book") |
|  |  |
|  | if [[ -n "$IS\_LAPTOP" ]]; then |
|  | /usr/bin/pmset -b sleep 15 disksleep 10 displaysleep 5 halfdim 1 |
|  | /usr/bin/pmset -c sleep 0 disksleep 0 displaysleep 30 halfdim 1 |
|  | else |
|  | /usr/bin/pmset sleep 0 disksleep 0 displaysleep 30 halfdim 1 |
|  | fi |

[view raw](https://gist.github.com/rtrouton/b3d734830eea981b27fb11b25c3c0ba2/raw/31c54217e9c3499777ff729cda80868ee062f9d0/powersetings.sh)
 [powersetings.sh](https://gist.github.com/rtrouton/b3d734830eea981b27fb11b25c3c0ba2#file-powersetings-sh)
hosted with ❤ by [GitHub](https://github.com)

In the example above, the **Model Identifier** information from the [system\_profiler command](https://ss64.com/osx/system_profiler.html) is used to help identify if the Mac is a desktop or laptop. In this case, the **Model Identifier** information is checked to see if the model identifier contains “Book”.

![Screenshot 2022 12 23 at 5 51 44 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-23-at-5.51.44-pm.png?w=595 "Screenshot 2022-12-23 at 5.51.44 PM.png")

If it does, it’s a laptop. Otherwise, it’s a desktop:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/system\_profiler SPHardwareDataType | grep "Model Identifier" | grep "Book" |

[view raw](https://gist.github.com/rtrouton/92d8a729c6188b28785d205a83627de7/raw/6550e04e37a78b07afcbec93d235659bb553f207/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/92d8a729c6188b28785d205a83627de7#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, [the latest Mac laptops’ model identifier does not contain “Book”](https://support.apple.com/HT201300). This means that this identification method should no longer be considered reliable.

![Screenshot 2022 12 23 at 5 40 48 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-23-at-5.40.48-pm.png?w=595 "Screenshot 2022-12-23 at 5.40.48 PM.png")

What’s an alternative way to check? One way is to use the [ioreg command](https://www.manpagez.com/man/8/ioreg/) to see if the Mac in question has a built-in battery or not. Laptops will have a built-in battery and desktops will not. For more details, please see below the jump.

---

**Update – 12-29-2022**: It appears my original choice of detection criteria of using **built-in** with the **ioreg** command was not universally returning no output data for desktops, as I hadn’t tested against Apple Silicon Mac desktops. Apple Silicon Mac desktops share a number of characteristics with Apple Silicon laptops, including having the following command respond with the following output:

**Yes**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/ioreg -c AppleSmartBattery -r | awk '/built-in/ {print $3}' |
|  | Yes |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/1f16d1af1a2621d474ce6cbc54c09401/raw/cb8e7cd80f266b506c5deac370c1e8ce21d07331/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/1f16d1af1a2621d474ce6cbc54c09401#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, there is another criteria we can search for which should provide better results, which is to use **BatteryInstalled** in place of **built-in** as criteria when running the **ioreg** command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/ioreg -c AppleSmartBattery -r | awk '/BatteryInstalled/ {print $3}' |

[view raw](https://gist.github.com/rtrouton/05cb2137a3321b88c411d4b7c7d5f8f6/raw/976b57dd82cff1702ec7371068669daa61d23960/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/05cb2137a3321b88c411d4b7c7d5f8f6#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

On a laptop, the following output should be returned:

**Yes**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/sbin/ioreg -c AppleSmartBattery -r | awk '/BatteryInstalled/ {print $3}' |
|  | Yes |
|  ...