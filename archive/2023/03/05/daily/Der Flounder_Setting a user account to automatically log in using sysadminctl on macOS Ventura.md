---
title: Setting a user account to automatically log in using sysadminctl on macOS Ventura
url: https://derflounder.wordpress.com/2023/03/04/setting-a-user-account-to-automatically-log-in-using-sysadminctl-on-macos-ventura/
source: Der Flounder
date: 2023-03-05
fetch_date: 2025-10-04T08:43:06.519263
---

# Setting a user account to automatically log in using sysadminctl on macOS Ventura

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Setting a user account to automatically log in using sysadminctl on macOS Ventura

## Setting a user account to automatically log in using sysadminctl on macOS Ventura

March 4, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

On macOS, [it’s possible to set an account to automatically log in](https://support.apple.com/HT201476). However, up until macOS Ventura, there hasn’t been an Apple command line tool available which will do the following:

* Set the desired account to automatically log in
* Create the **/etc/kcpassword** file

Setting the desired account to log in could be accomplished by running the following command with root privileges:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write /Library/Preferences/com.apple.loginwindow autoLoginUser -string username\_goes\_here |

[view raw](https://gist.github.com/rtrouton/f31e4210990360ca63d3a77ba630d39f/raw/c057d9a19538668f4b039d11020a02c80527b4c6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/f31e4210990360ca63d3a77ba630d39f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The hard part was correctly creating the **/etc/kcpassword** file, which stores an obfuscated copy of the password used by the account which is being set for auto-login. Without that file properly created and available in the specified location, the automatic login process would fail. For those interested in how the **kcpassword** file is set up, please see the link below:

<https://www.offsec.com/offsec/in-the-hunt-for-the-auto-login-setup-process/>

There have been [several](https://github.com/xfreebird/kcpassword/blob/master/kcpassword) tools [built](https://web.archive.org/web/20111001040218/http%3A//www.brock-family.org/gavin/perl/kcpassword.html) by the [community](https://www.brunerd.com/blog/2021/08/24/automating-automatic-login-for-macos/) which successfully create the **kcpassword** file, but Apple themselves hadn’t provided a way to do this in macOS Monterey or earlier, outside of using the GUI for **Users & Groups** in System Preferences.

![Screen Shot 2023 03 04 at 12 49 59 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screen-shot-2023-03-04-at-12.49.59-pm.png?w=595 "Screen Shot 2023-03-04 at 12.49.59 PM.png")

As of macOS Ventura, the [sysadminctl command line tool](https://ss64.com/osx/sysadminctl.html) has been updated with functionality to enable and disable auto-login for specified accounts. For more details, please see below the jump.

As of macOS Ventura 13.2.1, the help output for the **sysadminctl** tool includes the following options:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 2023-03-03 15:25:06.223 sysadminctl[35718:252330] Usage: sysadminctl |
|  | -deleteUser <user name> [-secure || -keepHome] (interactive || -adminUser <administrator user name> -adminPassword <administrator password>) |
|  | -newPassword <new password> -oldPassword <old password> [-passwordHint <password hint>] |
|  | -resetPasswordFor <local user name> -newPassword <new password> [-passwordHint <password hint>] (interactive] || -adminUser <administrator user name> -adminPassword <administrator password>) |
|  | -addUser <user name> [-fullName <full name>] [-UID <user ID>] [-GID <group ID>] [-shell <path to shell>] [-password <user password>] [-hint <user hint>] [-home <full path to home>] [-admin] [-roleAccount] [-picture <full path to user image>] (interactive] || -adminUser <administrator user name> -adminPassword <administrator password>) |
|  | -secureTokenStatus <user name> |
|  | -secureTokenOn <user name> -password <password> (interactive || -adminUser <administrator user name> -adminPassword <administrator password>) |
|  | -secureTokenOff <user name> -password <password> (interactive || -adminUser <administrator user name> -adminPassword <administrator password>) |
|  | -autologin set -userName <user name> [-password <user password>] || off || status (interactive || -adminUser <administrator user name> -adminPassword <administrator password>) |
|  | -guestAccount <on || off || status> |
|  | -afpGuestAccess <on || off || status> |
|  | -smbGuestAccess <on || off || status> |
|  | -automaticTime <on || off || status> |
|  | -filesystem status |
|  | -screenLock <status || immediate || off || seconds> -password <password> |
|  |  |
|  | Pass '-' instead of password in commands above to request prompt. |
|  | '-adminPassword' used mostly for scripted operation. Use '-' or 'interactive' to get the authentication string interactively. This preferred for security reasons |
|  |  |
|  | \*Role accounts require name starting with \_ and UID in 200-400 range. |

[view raw](https://gist.github.com/rtrouton/98081860705ec8391bed01a80d14c720/raw/a3c0d718df524e84580757e35b07922e3bfc0c5c/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/98081860705ec8391bed01a80d14c720#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

One of the options is the new-as-of-Ventura **-autologin** option. To set an account to auto-login, you will need to have the following:

* The username of the account you want to have auto-login
* The password to that account
* Some way to run the **sysadminctl** tool using root privileges

Once you have all conditions satisfied, you can set the desired account to auto-login by running the following command with root privileges:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | sysadminctl -autologin set -userName username\_goes\_here -password password\_goes\_here |

[view raw](https://gist.github.com/rtrouton/a391d93633a03bcb4833e8661dc6e07f/raw/3b3c59a07e4fd257de1ea7da3b38227bbbbc4fbf/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/a391d93633a03bcb4833e8661dc6e07f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![Screenshot 2023 03 04 at 11 58 32 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-04-at-11.58.32-am.png?w=595 "Screenshot 2023-03-04 at 11.58.32 AM.png")

If you want to be prompted for the desired account’s password, enter a dash ( **–** ) where you would otherwise enter the desired account’s password when running the following command with root privileges:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional U...