---
title: Downloading macOS IPSW files for use with Mac virtual machines on Apple Silicon Macs
url: https://derflounder.wordpress.com/2022/11/17/downloading-macos-ipsw-files-for-use-with-mac-virtual-machines-on-apple-silicon-macs/
source: Der Flounder
date: 2022-11-18
fetch_date: 2025-10-03T23:05:11.284784
---

# Downloading macOS IPSW files for use with Mac virtual machines on Apple Silicon Macs

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/), [Virtualization](https://derflounder.wordpress.com/category/virtualization/) > Downloading macOS IPSW files for use with Mac virtual machines on Apple Silicon Macs

## Downloading macOS IPSW files for use with Mac virtual machines on Apple Silicon Macs

November 17, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A change between creating Mac virtual machines on Intel Macs and creating them on Apple Silicon Macs is that virtualization on Apple Silicon Macs often assumes that the [virtual machine is built using a macOS restore image](https://developer.apple.com/documentation/virtualization/running_macos_in_a_virtual_machine_on_apple_silicon_macs) . These restore images are files with an **.ipsw** file extension and are commonly referred to as IPSW files.

Apple publishes the download links for macOS restore images via the following URL:

<https://mesu.apple.com/assets/macos/com_apple_macOSIPSW/com_apple_macOSIPSW.xml>

If you look at the XML file from the link above, it provides download links for the current version of macOS for the various Mac models which support running that version of macOS.

Among the various models listed is the model identifier for Mac virtual machines (**VirtualMac2,1**) created [using Apple’s Virtualization framework](https://developer.apple.com/documentation/virtualization/running_macos_in_a_virtual_machine_on_apple_silicon_macs). This means that we should be able to identify and download the appropriate IPSW file for use when building Mac virtual machines.

![Screenshot 2022-11-16 at 7.33.48 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-16-at-7.33.48-pm.png?w=595)

Using this information, I’ve written a script to download the appropriate IPSW file for building macOS virtual machines by checking the file linked above for the download URL associated with the **VirtualMac2,1** Mac model. For more details, please see below the jump.

The script checks Apple’s IPSW feed to get the appropriate IPSW file for the current release of macOS used by the **VirtualMac2,1** Mac model. If it finds a matching IPSW download URL, it will take the following actions:

1. Download the IPSW file to a temp directory.
2. If the download succeeds, a message is displayed notifying the user that the download has completed and where the IPSW file is stored.
3. If the download fails, a message is displayed notifying the user that the download failed and the script exits with an error.

**Usage:**

**./download\_latest\_macOS\_ipsw\_for\_virtualization.sh**

![Screenshot 2022 11 16 at 10 39 10 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-16-at-10.39.10-pm.png?w=595 "Screenshot 2022-11-16 at 10.39.10 PM.png")

![Screenshot 2022 11 16 at 10 42 14 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-16-at-10.42.14-pm.png?w=595 "Screenshot 2022-11-16 at 10.42.14 PM.png")

This script is available below and also from GitHub at the following location:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/download_latest_macOS_ipsw_for_virtualization>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # This script checks Apple's IPSW feed to get the appropriate IPSW file |
|  | # for the current release of macOS used by the VirtualMac2,1 virtualization |
|  | # Mac model. |
|  |  |
|  | clear |
|  |  |
|  | exitCode=0 |
|  | Apple\_macOS\_IPSW\_Download\_Directory=$(mktemp -d) |
|  | Apple\_macOS\_IPSW\_Feed="[https://mesu.apple.com/assets/macos/com\_apple\_macOSIPSW/com\_apple\_macOSIPSW.xml&quot](https://mesu.apple.com/assets/macos/com_apple_macOSIPSW/com_apple_macOSIPSW.xml%26quot); |
|  | Apple\_macOS\_IPSW\_XML=$(/usr/bin/curl -s "$Apple\_macOS\_IPSW\_Feed" | xmllint –format -) |
|  | Apple\_macOS\_IPSW\_Download\_URL=$(/usr/libexec/PlistBuddy -c 'print ":MobileDeviceSoftwareVersionsByVersion:1:MobileDeviceSoftwareVersions:VirtualMac2,1"' /dev/stdin <<< "$Apple\_macOS\_IPSW\_XML" | awk '/FirmwareURL/ {print $3}') |
|  | Apple\_macOS\_IPSW\_Filename=$(echo "$Apple\_macOS\_IPSW\_Download\_URL" | awk -F / '{print $NF}') |
|  |  |
|  | # Verify that the IPSW download URL contains a filename which ends in .ipsw |
|  |  |
|  | if [[ -n $(echo "$Apple\_macOS\_IPSW\_Download\_URL" | grep -o ".ipsw") ]]; then |
|  |  |
|  | # If the IPSW download URL contains a filename which ends in .ipsw, |
|  | # download the IPSW file and store it in a temp directory. |
|  |  |
|  | echo "Downloading $Apple\_macOS\_IPSW\_Filename …" |
|  | echo "From: $Apple\_macOS\_IPSW\_Download\_URL" |
|  | echo "To: $Apple\_macOS\_IPSW\_Download\_Directory/$Apple\_macOS\_IPSW\_Filename" |
|  | echo "" |
|  |  |
|  | /usr/bin/curl -L "$Apple\_macOS\_IPSW\_Download\_URL" -o "$Apple\_macOS\_IPSW\_Download\_Directory"/"$Apple\_macOS\_IPSW\_Filename" && download\_success=1 |
|  |  |
|  | # If the download succeeds, display a message notifying the user that the |
|  | # download has completed and where the IPSW file is stored. |
|  | # |
|  | # If the download fails, display a message notifying the user that the download failed |
|  | # and exit with an error. |
|  |  |
|  | if [[ -n "$download\_success" ]] && [[ -f "$Apple\_macOS\_IPSW\_Download\_Directory"/"$Apple\_macOS\_IPSW\_Filename" ]]; then |
|  | echo "" |
|  | echo "$Apple\_macOS\_IPSW\_Filename has been downloaded to the following location:" |
|  | echo "$Apple\_macOS\_IPSW\_Download\_Directory/$Apple\_macOS\_IPSW\_Filename" |
|  | else |
|  | echo "Download of $Apple\_macOS\_IPSW\_Filename from $Apple\_macOS\_IPSW\_Download\_URL has failed. Exiting." |
|  | exitCode=1 |
|  | fi |
|  | else |
|  |  |
|  | # If the IPSW download URL does not contain a filename which ends in .ipsw, |
|  | # display a message notifying the user that an IPSW file was not found and |
|  | # exit with an error. |
|  |  |
|  | echo "Unable to detect macOS IPSW file to download. Exiting." |
|  | exitCode=1 |
|  | fi |
|  |  |
|  | exit "$exitCode" |

[view raw](https://gist.github.com/rtrouton/268691f551be4115afa0520c3ec0cd1c/raw/9d6669c4cfa7f87efd66e25d49d1c7b0defb9dfa/download_latest_macOS_ipsw_for_virtualization.sh)
 [download\_latest\_macOS\_ipsw\_for\_virtualization.sh](https://gist.github.com/rtrouton/268691f551be4115afa0520c3ec0cd1c#file-download_latest_macos_ipsw_for_virtualization-sh)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2022/11/17/downloading-macos-ipsw-files-for-use-with-mac-virtual-machines-on-apple-silicon-macs/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2022/11/17/downloading-macos-ipsw-files-for-use-with-mac-virtual-machines-on-apple-silicon-macs/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2022/11/17/downloading-macos-ipsw-files-for-use-with-mac-virtual-machines-on-apple-silicon-macs/?share=linkedin)
* [Clic...