---
title: Listing and downloading available macOS installers using Apple’s softwareupdate tool
url: https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/
source: Der Flounder
date: 2023-07-01
fetch_date: 2025-10-04T11:50:56.745742
---

# Listing and downloading available macOS installers using Apple’s softwareupdate tool

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Listing and downloading available macOS installers using Apple’s softwareupdate tool

## Listing and downloading available macOS installers using Apple’s softwareupdate tool

June 30, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As of macOS Catalina and Big Sur, Apple added some useful functionality to the [softwareupdate](https://ss64.com/osx/softwareupdate.html) tool which allows you to [list the macOS installers](https://derflounder.wordpress.com/2021/03/03/listing-the-full-os-installers-available-from-apples-software-update-feed-on-macos-big-sur/) (starting on macOS Big Sur) available to a particular Mac and then to [download them](https://scriptingosx.com/2019/10/download-a-full-install-macos-app-with-softwareupdate-in-catalina/) (starting on macOS Catalina.)

I’ve used both functions frequently when I needed to identify and download new macOS installers, so I decided to write a script which makes the task easier. For more details, please see below the jump.

The script uses the **softwareupdate** tool to list all macOS installers that are available to the Mac you’re running the script on, along with the version number information you would need to provide to the **softwareupdate** tool in order to download that macOS version’s installer.

![Screen Shot 2023 06 30 at 4 43 04 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/06/screen-shot-2023-06-30-at-4.43.04-pm.png?w=595&h=278 "Screen Shot 2023-06-30 at 4.43.04 PM.png")

If you enter version information when prompted, the script will download the specified macOS installer and install the corresponding macOS installer application into **/Applications**.

![Screen Shot 2023 06 30 at 4 56 57 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/06/screen-shot-2023-06-30-at-4.56.57-pm.png?w=595&h=325 "Screen Shot 2023-06-30 at 4.56.57 PM.png")

![Screen Shot 2023 06 30 at 4 35 48 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/06/screen-shot-2023-06-30-at-4.35.48-pm.png?w=595&h=302 "Screen Shot 2023-06-30 at 4.35.48 PM.png")

This script is available below and also from GitHub at the following location:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/download_macos_installers>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # This script uses the softwareupdate command to display all available macOS |
|  | # installers for a particular Mac and then offers the option to download a |
|  | # selected OS installer. |
|  |  |
|  | available\_os\_installers=$(mktemp) |
|  |  |
|  | # Set exit status |
|  | error=0 |
|  |  |
|  | #Check for available macOS installers |
|  |  |
|  | /usr/sbin/softwareupdate –list-full-installers > "$available\_os\_installers" |
|  |  |
|  | clear |
|  |  |
|  | echo "The following macOS installers are available for this Mac:" |
|  | echo "" |
|  | cat "$available\_os\_installers" | tail -n +3 | awk -F ': |, |KiB' '($1 == "\* Title") { print $2" "$4" Build "$9 ": "(int((($6 \* 1024) / 1000000000) \* 10 + 0.5) / 10) " GB" }' |
|  | echo "" |
|  | echo "Version numbers:" |
|  | grep -oE '\d+\.(\d|\.)\*\d' "$available\_os\_installers" |
|  | echo "" |
|  | read -p "Please enter the version number of the macOS installer you wish to download: " macos\_version |
|  |  |
|  | # Verify that data entered contains only numbers and periods by extracting all the numbers and |
|  | # periods and seeing if there's anything left over. If there is, not a valid version number. |
|  |  |
|  | macos\_version\_check=$(echo "$macos\_version" | sed 's/[0-9]//g' | tr -d '.') |
|  |  |
|  | # If the version check returns no data, a version number containing only numbers and periods was entered. |
|  |  |
|  | if [[ -z "$macos\_version\_check" ]]; then |
|  | echo "Downloading installer…" |
|  | /usr/sbin/softwareupdate –fetch-full-installer –full-installer-version ${macos\_version} |
|  | else |
|  | echo "$macos\_version is not a valid version number. Exiting…" |
|  | error=1 |
|  | fi |
|  |  |
|  | exit $error |

[view raw](https://gist.github.com/rtrouton/57e84706ca8e2217aa4f6a7aca46d50e/raw/4e73a07af005b6b73df43829ddd1a795ca3917d7/download_macos_installers.sh)
 [download\_macos\_installers.sh](https://gist.github.com/rtrouton/57e84706ca8e2217aa4f6a7aca46d50e#file-download_macos_installers-sh)
hosted with ❤ by [GitHub](https://github.com)

Thanks to the folks in the **#bash** channel in the Mac Admins Slack for helping improve various parts of this script.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/)

Comments (6)
[Leave a comment](#respond)

1. ![plstrtfrd's avatar](https://0.gravatar.com/avatar/6af5ef1ffd9d4e881f6168c5f2321f711dc6ee8d8852eeaa03cd7e59b1a28c8e?s=32&d=identicon&r=G)

   plstrtfrd

   June 30, 2023 at 9:22 pm

   [Reply](https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/?replytocom=71312#respond)

   I think the “–” on line 13 in the script window has been automagically transmogrified into an “–”

   * ![rtrouton's avatar](https://0.gravatar.com/avatar/fb809...