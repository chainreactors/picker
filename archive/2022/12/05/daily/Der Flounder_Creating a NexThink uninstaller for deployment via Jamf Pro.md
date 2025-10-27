---
title: Creating a NexThink uninstaller for deployment via Jamf Pro
url: https://derflounder.wordpress.com/2022/12/04/creating-a-nexthink-uninstaller-for-deployment-via-jamf-pro/
source: Der Flounder
date: 2022-12-05
fetch_date: 2025-10-04T00:30:42.742512
---

# Creating a NexThink uninstaller for deployment via Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Packaging](https://derflounder.wordpress.com/category/packaging/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Creating a NexThink uninstaller for deployment via Jamf Pro

## Creating a NexThink uninstaller for deployment via Jamf Pro

December 4, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to [my previous post on building an installer for NexThink Collector](https://derflounder.wordpress.com/2022/12/03/creating-a-nexthink-installer-for-deployment-via-jamf-pro/) which could be deployed via Jamf Pro, I also needed to build an uninstaller for this software. Fortunately, NexThink ships an uninstaller script on the same disk image that it uses to ship its installer.

![Screenshot 2022 12 03 at 3 31 46 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-03-at-3.31.46-pm.png?w=595 "Screenshot 2022-12-03 at 3.31.46 PM.png")

[NexThink’s install documentation](https://docs.nexthink.com/platform/latest/installing-collector-on-macos) for the macOS version of the Collector software assumes that a human is doing the following to run the uninstall process:

A. Mounting the disk image
B. Opening the Terminal application
C. Using the uninstaller script to run the uninstallation process.

![Screenshot 2022 12 03 at 3 47 10 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-03-at-3.47.10-pm.png?w=595 "Screenshot 2022-12-03 at 3.47.10 PM.png")

In my case, I decided to do the following to deploy the uninstaller via Jamf Pro:

1. Wrap the disk image inside a separate installer package.
2. Use a **postinstall** script to perform the following actions:

A. Identify the location of the disk image stored inside the installer package.
B. Mount the disk image
C. Use the uninstall script to uninstall the NexThink Collector software.
D. Unmount the disk image.

For more details, please see below the jump.

**Pre-requisites:**

* [Packages](http://s.sudre.free.fr/Software/Packages/about.html)
* Vendor-provided NexThink disk image with the NexThink Collector uninstaller script

**Building the NexThink Collector uninstaller**

1. Set up a new Packages project and select **Raw Package**.

![Screenshot 2022 12 04 at 3 53 01 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.53.01-pm.png?w=595 "Screenshot 2022-12-04 at 3.53.01 PM.png")

2. In this case, I’m naming the project **NexThink Collector Uninstaller 22.9.1.14**.

![Screenshot 2022 12 04 at 3 53 24 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.53.24-pm.png?w=595 "Screenshot 2022-12-04 at 3.53.24 PM.png")

3. Once the Packages project opens, click on the **Project** tab. You’ll want to make sure that the your information is correctly set here (if you don’t know what to put in, check the **Help** menu for the Packages User Guide. The information you need is in **Chapter 4 – Configuring a project**.)

![Screenshot 2022 12 04 at 3 53 48 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.53.48-pm.png?w=595 "Screenshot 2022-12-04 at 3.53.48 PM.png")

In this example, I’m not changing any of the options from what is set by default.

4. Next, click on the **Settings** tab. In the case of my project, I want to install with root privileges and not require a logout, restart or shutdown.

To accomplish this, I’m choosing the following options in the **Settings** section:

In the **Tag** section:

* **Identifier:** set as appropriate (for my uninstaller, I’m using **com.nexthink.pkg.collector.uninstaller**.)
* **Version:** set as appropriate (for my uninstaller, I’m using **22.9.1.14**. )

In the **Post-installation Behavior** section:

**On Success**: should be set to **Do Nothing**.

In the **Options** section:

* **Require admin password for installation** should be checked
* **Relocatable** should be unchecked
* **Overwrite directory permissions** should be unchecked
* **Follow symbolic links** should be unchecked

![Screenshot 2022 12 04 at 3 54 48 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.54.48-pm.png?w=595 "Screenshot 2022-12-04 at 3.54.48 PM.png")

5. Select the **Payload** tab. Nothing here should be changed from the defaults.

![Screenshot 2022 12 04 at 3 54 58 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.54.58-pm.png?w=595 "Screenshot 2022-12-04 at 3.54.58 PM.png")

6. Select the **Scripts** tab.

Under the **Additional Resources** section, add the following file:

* The NexThink disk image

![Screenshot 2022 12 04 at 3 56 04 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.56.04-pm.png?w=595 "Screenshot 2022-12-04 at 3.56.04 PM.png")

![Screenshot 2022 12 04 at 3 56 08 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.56.08-pm.png?w=595 "Screenshot 2022-12-04 at 3.56.08 PM.png")

The last part is telling the NexThink uninstall script to run. For this, you’ll need a **postinstall** script.

Here’s the **postinstall** script being used for this example:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # Description: Script to uninstall NexThink Collector. |
|  |  |
|  | ERROR=0 |
|  |  |
|  | # File Paths |
|  |  |
|  | if [[ -f "$(/usr/bin/find $(dirname $0) -maxdepth 1 \( -iname \\*\.dmg \))" ]]; then |
|  | dmgFile="$(/usr/bin/find $(dirname $0) -maxdepth 1 \( -iname \\*\.dmg \))" |
|  | fi |
|  |  |
|  | dmgMount="$(/usr/bin/mktemp -d /tmp/NexThink\_Collector\_Uninstaller.XXXX)" |
|  |  |
|  | # Remove the trailing slash from the dmgMount variable if needed. |
|  | dmgMount=${dmgMount%%/} |
|  |  |
|  | # Mount the DMG |
|  | /usr/bin/hdiutil attach "$dmgFile" -mountpoint "$dmgMount" -nobrowse -noverify -noautoopen |
|  |  |
|  | # Uninstall the NexThink Collector software |
|  |  |
|  | "$dmgMount"/uninstaller |
|  |  |
|  | # Unmount the DMG |
|  | hdiutil detach $dmgMount -force |
|  |  |
|  | exit $ERROR |

[view raw](https://gist.github.com/rtrouton/8b53adb27a9c366365a7845a39cc072a/raw/d1eb4074a42bb909a7cfdf5d524f9148bbb4d5ac/postinstall)
 [postinstall](https://gist.github.com/rtrouton/8b53adb27a9c366365a7845a39cc072a#file-postinstall)
hosted with ❤ by [GitHub](https://github.com)

If not already selected, select the **postinstall** script and add it to the project.

![Screenshot 2022 12 04 at 3 56 20 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.56.20-pm.png?w=595 "Screenshot 2022-12-04 at 3.56.20 PM.png")

![Screenshot 2022 12 04 at 3 56 24 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-04-at-3.56.24-pm.png?w=595 "Screenshot 2022-12-04 at 3.56.24 PM.png")

7. Build the package. (If you don’t know to build, check the **Help** menu for the Packages User Guide. The information you need is in **Chapter 3 – Creating a raw package project** and **Chapter 10 ...