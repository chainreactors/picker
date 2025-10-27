---
title: Removing Oracle Java from macOS
url: https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/
source: Der Flounder
date: 2023-08-12
fetch_date: 2025-10-04T12:00:32.891803
---

# Removing Oracle Java from macOS

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Java](https://derflounder.wordpress.com/category/java/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Removing Oracle Java from macOS

## Removing Oracle Java from macOS

August 11, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As of January 23, 2023, Oracle made a change to how they’ve licensed Oracle’s Java (which is a separate license from the ones used for open source Java distributions like [OpenJDK](https://openjdk.org/).) [The new license terms are described here in Oracle’s FAQ](https://www.oracle.com/java/technologies/java-se-subscription-faq.html), but to summarize the main difference between the old licensing and the current licensing is that [Oracle introduced a new employee-based metric](https://www.theregister.com/2023/01/27/oracle_java_licensing_change/).

* Old license: License costs were based on how many employees your company has which used Oracle’s Java.
* Current license: License costs are based on how many employees your company has.

See the difference? Previously, if your company had 1000 employees and 2 used Oracle’s Java for purposes which required payment under the old license, the company paid for 2 licenses. Under the current license, if your company has 1000 employees and 2 use Oracle’s Java, Oracle may say that now the company needs to pay for 1000 licenses.

There’s more to it and I am not the person to turn to when needing explanation of complex legal and financial questions, but the operational consequence for Mac admins is that companies which had previously been OK with Oracle Java being installed on their Macs may now be coming to their Mac admins, asking how Oracle Java can be removed and kept off.

To assist with this, I’ve written a script which should remove Oracle Java JREs and JDKs on macOS. For more details, please see below the jump.

The script will check the following directories for Oracle Java JREs and JDKs:

* JRE: **/Library/Internet Plug-Ins**
* JDK: **/Library/Java/JavaVirtualMachines**

The script will check those directories for the following conditions:

1. Is the directory in question empty? If yes, nothing to do and the script moves on.
2. If the directory is not empty, it checks to see if there are JRE or JDKs installed.
3. If there are JREs or JDKs installed, check if the JRE or JDK in question is from Oracle.
4. If a JRE or JDK is from Oracle, remove the Oracle Java JRE or JDK installation.

This script should leave all non-Oracle Java installs that you may have on the Mac intact and untouched. However, I strongly recommend testing in your own environment before any deployment to make sure it is not removing anything you don’t want to have removed.

The script is available below and also from GitHub at the following location:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/uninstallers/oracle_java_uninstall>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # Checks for Oracle Java JRE and JDK installs and removes all |
|  | # identified installations. |
|  |  |
|  | installedJREs="/Library/Internet Plug-Ins" |
|  | installedJDKs="/Library/Java/JavaVirtualMachines" |
|  |  |
|  | # Check to see if /Library/Internet Plug-Ins is empty. |
|  |  |
|  | if [[ -n $(ls -A "$installedJREs") ]]; then |
|  |  |
|  | # If it's not empty, check for installed JREs. If an installed JRE |
|  | # is detected, check to see if it's from Oracle. |
|  |  |
|  | if [[ -x "${installedJREs}/JavaAppletPlugin.plugin" ]]; then |
|  | jreVendor=$(/usr/bin/defaults read "${installedJREs}/JavaAppletPlugin.plugin/Contents/Enabled.plist" CFBundleIdentifier | /usr/bin/grep -Eo "oracle") |
|  |  |
|  | # If it's from Oracle, remove the Java installation. |
|  |  |
|  | if [[ "$jreVendor" = "oracle" ]]; then |
|  | rm -rf "${installedJREs}/JavaAppletPlugin.plugin" |
|  | fi |
|  | fi |
|  | fi |
|  |  |
|  | # Check to see if /Library/Java/JavaVirtualMachines is empty. |
|  |  |
|  | if [[ -n $(ls -A "$installedJDKs") ]]; then |
|  |  |
|  | # If it's not empty, check for installed JDKs. |
|  |  |
|  | for aJDKPath in "${installedJDKs}"/\*; do |
|  |  |
|  | # If an installed JDK is detected, check to see if it's from Oracle |
|  |  |
|  | jdkVendor=$(/usr/bin/defaults read "${aJDKPath}/Contents/Info.plist" CFBundleIdentifier | /usr/bin/grep -Eo "oracle") |
|  |  |
|  | # If it's from Oracle, remove the Java installation. |
|  |  |
|  | if [[ "$jdkVendor" = "oracle" ]]; then |
|  | rm -rf "${aJDKPath}" |
|  | fi |
|  | done |
|  | fi |
|  |  |
|  | exit 0 |

[view raw](https://gist.github.com/rtrouton/006ced369bae2daceabc4ed81a05b586/raw/d6036da3cdfd65fdba245b2f8ff40df1599611ef/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/006ced369bae2daceabc4ed81a05b586#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?share=pocket)

Like Loading...

### *Related*

Categories: [Java](https://derflounder.wordpress.com/category/java/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/)

Comments (3)
[Leave a comment](#respond)

1. ![janothin63a41d48df's avatar](https://0.gravatar.com/avatar/c97ae82db837e7356c8e29f4545ddd75b2f38828871172d1c2ec147e8551c04f?s=32&d=identicon&r=G)

   janothin63a41d48df

   August 11, 2023 at 8:52 pm

   [Reply](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/?replytocom=71734#respond)

   Hi there, do you have an extension attribute that could determine computers running Oracle Java? Also, if another JDK such as the Microsoft OpenJDK is installed, would this script potentially remove it also?

   * ![rtrouton's avatar](https://0.gravatar.com/avatar/fb809ae7...