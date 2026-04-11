---
title: Detecting installed Intel-based applications on macOS Tahoe
url: https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/
source: Der Flounder
date: 2026-04-10
fetch_date: 2026-04-11T04:20:58.645689
---

# Detecting installed Intel-based applications on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Rosetta 2](https://derflounder.wordpress.com/category/rosetta-2/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Detecting installed Intel-based applications on macOS Tahoe

## Detecting installed Intel-based applications on macOS Tahoe

April 10, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

On macOS Tahoe 26.4.x and later, launching an Intel-based app on an Apple Silicon Mac will periodically result in [a message similar to the following](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/) being displayed by the OS.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-10-at-9.25.28am.png?w=372&h=139 "Screenshot 2026-04-10 at 9.25.28 AM.png")

This message is part of Apple’s transition strategy for Intel-based apps over the course of macOS 26 and macOS 27. The Rosetta 2 support used to run Intel-based apps will continue in its current form on both macOS 26 and macOS 27, but there will be as-yet unspecified changes occurring beyond macOS 27. For more information on this transition, please see the Apple KBase article linked below:

**Using Intel-based apps on a Mac with Apple silicon**
<https://support.apple.com/102527>

To help identify if and where Intel-based applications have been installed on Apple Silicon Macs, you can use **System Information.app**‘s list of installed software to identify which installed applications show up with the following status:

* **Kind: Intel**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-10-at-9.35.20am.png?w=598&h=290 "Screenshot 2026-04-10 at 9.35.20 AM.png")

To assist with automating this task, a script is available which uses the [/usr/sbin/system\_profiler](https://ss64.com/mac/system_profiler.html) command line tool to detect all Intel-based apps installed in **/Applications**, **/Library** or **/usr/local** and output the list to a logfile named **intel\_apps\_installed.log** which is stored in the **/var/log** directory. For more details, please see below the jump.

The script does the following:

1. Checks to see if the script is being run as root.
2. Checks to see if the designated log file is present and creates it if it isn’t.
3. Uses the **/usr/sbin/system\_profiler** command line tool to pull the complete list of installed applications
4. Filters all applications that are not Intel-based applications.
5. Excludes all Intel-based applications that are not stored in one of the following locations or their included directories:

* **/Applications**
* **/Library**
* **/usr/local**

6. Outputs the following output to the log:

If any Intel-based applications are found in **/Applications**, **/Library** or **/usr/local**, the path to the delected Intel-based application or applications are listed in the log:

**/path/to/Intel\_based\_application\_name\_here.app**

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-10-at-9.24.38am.png?w=600&h=265 "Screenshot 2026-04-10 at 9.24.38 AM.png")

If no Intel-based applications are found in /Applications, /Library or /usr/local, the following is output to the log:

**No Intel-based applications found in /Applications, /Library or /usr/local.**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-10-at-9.22.23am.png?w=600&h=265 "Screenshot 2026-04-10 at 9.22.23 AM.png")**

The script is available below and also on GitHub at the following address:

<https://github.com/rtrouton/rtrouton_scripts/tree/master/rtrouton_scripts/detect_installed_intel_based_apps>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # Detect all Intel apps installed in /Applications, /Library |
|  | # or /usr/local and output list to logfile stored in /var/log. |
|  |  |
|  | intel\_app\_logfile="/var/log/intel\_apps\_installed.log" |
|  | ERROR=0 |
|  |  |
|  | # this script must be run with root privileges |
|  | if [[ "$(/usr/bin/id -u)" -eq 0 ]]; then |
|  |  |
|  | # Create log file if not present |
|  | if [[ -f "$intel\_app\_logfile" ]]; then |
|  | echo "$intel\_app\_logfile found. Proceeding…" |
|  | else |
|  | echo "Creating $intel\_app\_logfile log. Proceeding…" |
|  | touch "$intel\_app\_logfile" |
|  | fi |
|  |  |
|  | # Get a list of all installed applications |
|  | intel\_app\_list=$(/usr/sbin/system\_profiler SPApplicationsDataType) |
|  |  |
|  | if [[ -n "$intel\_app\_list" ]]; then |
|  |  |
|  | # get all non-64 Bit applications from the initial list |
|  | intel\_app\_list=$(echo "$intel\_app\_list" | /usr/bin/grep -A3 "Intel") |
|  |  |
|  | # filter out all applications in /Applications, /Library and /usr/local |
|  | intel\_app\_list=$(echo "$intel\_app\_list" | /usr/bin/grep -E "Location:[^/]\*/(Applications|Library|usr/local)/") |
|  |  |
|  | # remove everything except the path |
|  | intel\_app\_list=$(echo "$intel\_app\_list" | /usr/bin/sed -n 's/.\*Location:[[:space:]]\*\(.\*\)/\1/p') |
|  |  |
|  | if [[ -n "$intel\_app\_list" ]]; then |
|  | echo "$intel\_app\_list" > "$intel\_app\_logfile" |
|  | echo "List of detected Intel-based applications available in $intel\_app\_logfile" |
|  | else |
|  | echo "No Intel-based applications found in /Applications, /Library or /usr/local." > "$intel\_app\_logfile" |
|  | fi |
|  | fi |
|  |  |
|  | else |
|  | log "ERROR! You must be root in order to run this script!" |
|  | ERROR=1 |
|  | fi |
|  |  |
|  | exit $ERROR |

[view raw](https://gist.github.com/rtrouton/9182239b44190bfb6bfec9785f31ea4f/raw/9ee4b1a6a5f850f54762516bb5888b1c5581f12c/detect_installed_intel_based_apps.sh)
 [detect\_installed\_intel\_based\_apps.sh](https://gist.github.com/rtrouton/9182239b44190bfb6bfec9785f31ea4f#file-detect_installed_intel_based_apps-sh)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/04/10/detecting-installed-intel-based-applications-on-macos-tahoe/?share=tu...