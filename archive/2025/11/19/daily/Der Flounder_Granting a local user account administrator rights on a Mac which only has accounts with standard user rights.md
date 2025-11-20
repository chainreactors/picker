---
title: Granting a local user account administrator rights on a Mac which only has accounts with standard user rights
url: https://derflounder.wordpress.com/2025/11/19/granting-a-local-user-account-administrator-rights-on-a-mac-which-only-has-accounts-with-standard-user-rights/
source: Der Flounder
date: 2025-11-19
fetch_date: 2025-11-20T03:08:33.202984
---

# Granting a local user account administrator rights on a Mac which only has accounts with standard user rights

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [macOS Recovery](https://derflounder.wordpress.com/category/macos-recovery/) > Granting a local user account administrator rights on a Mac which only has accounts with standard user rights

## Granting a local user account administrator rights on a Mac which only has accounts with standard user rights

November 19, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

[I recently saw a post on LinkedIn](https://www.linkedin.com/posts/prakhar-jain-0710_apple-macos-security-activity-7396494243940298752-RQLO/) where the poster had apparently removed all accounts which were assigned administrator rights on the Mac from the local group named **admin** on macOS and then had difficulty recovering from this state.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-18-at-7.20.13pm.png?w=595 "Screenshot 2025-11-18 at 7.20.13 PM.png")

On macOS, membership in the **admin** group is what grants administrator rights, so now this meant that the Mac only had accounts which had [standard user rights](https://support.apple.com/en-is/guide/mac-help/mtusr001/mac).

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-18-at-8.20.13pm.png?w=595 "Screenshot 2025-11-18 at 8.20.13 PM.png")

There have been methods available in the past for fixing this from the [Recovery environment](https://support.apple.com/102518) which used the [chroot command line tool](https://ss64.com/bash/chroot.html) in the Recovery environment to change the active filesystem from the Recovery environment to the Mac’s regular boot drive, then run the [dseditgroup command line tool](https://ss64.com/mac/dseditgroup.html) to re-add one or more local user accounts to the **admin** group on the boot drive.

However, it looks like the **chroot** command does not work currently in the Recovery environment available to macOS Tahoe on Apple Silicon Macs. When launched, it reports an error and then exits.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-18-at-8.20.15pm.png?w=595 "Screenshot 2025-11-18 at 8.20.15 PM.png")

With the **chroot** command line tool no longer working in Recovery, that would seem to close off most avenues to re-adding users to the **admin** group for Apple Silicon Macs running macOS Tahoe. However, after some research, I’ve discovered an alternative method which uses the [sudo command line tool](https://ss64.com/mac/sudo.html). For more details, please see below the jump.

This method uses the ability on macOS for the **sudo** command line tool to use properly formatted configurations for the **sudo** tool, where those configuration files are stored as plaintext files in the **/private/etc/sudoers.d** directory. The following process will create a **sudo** configuration which is stored in a plaintext file named **fixadmin** which will be created from the Recovery environment and stored in the **/private/etc/sudoers.d** directory in the writeable part of the Mac’s boot drive.

What this configuration file will do is allow a user account which otherwise has standard user rights to run the **dseditgroup** command line tool with root privileges, which in turn will enable the user account to add itself (or another account) to the local group named **admin** using the **dseditgroup** command line tool. The end result of this process is that administrator rights will be granted to the account being added to the admin group.

**Pre-requisites:**

* Physical access to the Mac in question.
* The [account shortname](https://support.apple.com/en-is/guide/mac-help/mh35548/mac) of the account being used to run the **dseditgroup** command line tool with root privileges
* If Mac is encrypted using FileVault, you will need the [FileVault recovery key](https://support.apple.com/en-is/guide/mac-help/mh35880/mac) and the password to a [FileVault-enabled account](https://support.apple.com/en-is/guide/mac-help/flvlt001/26/mac/26).

Once the pre-requisites are handled, use the following process to create the configuration file for the **sudo** command line tool:

1. Boot to the [Recovery environment](https://support.apple.com/102518).
2. If required, enter the FileVault recovery key to access the Recovery environment.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.36.png?w=595 "Screenshot 2025-11-19 at 10.36.png")

3. If you needed to unlock using the FileVault recovery key, once unlocked choose the **Exit to Recovery** option.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.36-1.png?w=595 "Screenshot 2025-11-19 at 10.36.png")

4. From the Recovery window, click on Disk Utility.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.36-2.png?w=595 "Screenshot 2025-11-19 at 10.36.png")

5. Verify that the **Data** volume is mounted.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.37.png?w=595 "Screenshot 2025-11-19 at 10.37.png")

If the **Data** volume is not mounted, click the **Mount** button in Disk Utility to mount it.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.37-1.png?w=595 "Screenshot 2025-11-19 at 10.37.png")

If FileVault is enabled, you will need to enter the password of a FileVault-enabled account to mount the **Data** volume.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.37-2.png?w=595 "Screenshot 2025-11-19 at 10.37.png")

6. Quit out of Disk Utility.
7. Open Terminal using the **Utilities** menu.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-10.38.png?w=595 "Screenshot 2025-11-19 at 10.38.png")

8. Run the following command to create a file named **fixadmin** in the **/Volumes/Data/private/etc/sudoers.d** directory:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | touch /Volumes/Data/private/etc/sudoers.d/fixadmin |

[view raw](https://gist.github.com/rtrouton/0bb700f6094d1be3ca601fd014e5c94c/raw/451ee9d5774583381dbfcaf362ef3b9423adf708/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0bb700f6094d1be3ca601fd014e5c94c#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-19-at-11.55.png?w=595 "Screenshot 2025-11-19 at 11.55.png")

9. Run the following command to edit the **/Volumes/Data/private/etc/sudoers.d/fixadmin** file using the [nano command line text editor](https://support.apple.com/en-is/guide/terminal/apdb02f1133-25af-4c65-8976-159609f99817/mac):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /Volumes/Macintosh\ HD/usr/bin/nano /Volumes/Data/private/etc/s...