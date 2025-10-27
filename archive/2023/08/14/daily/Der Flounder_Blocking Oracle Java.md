---
title: Blocking Oracle Java
url: https://derflounder.wordpress.com/2023/08/13/blocking-oracle-java/
source: Der Flounder
date: 2023-08-14
fetch_date: 2025-10-04T11:59:09.804638
---

# Blocking Oracle Java

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Java](https://derflounder.wordpress.com/category/java/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Blocking Oracle Java

## Blocking Oracle Java

August 13, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to [my previous post on removing Oracle Java](https://derflounder.wordpress.com/2023/08/11/removing-oracle-java-from-macos/), it’s possible that Mac admins may be requested to block Oracle Java in place of removing it. This may be challenging, but possible with the right information and tools. For more details, please see below the jump.

Normally, there’s three approaches on macOS that you can take when needing to block an app:

1. Block by process name
2. Block by code signature
3. Block with parental controls

**Block by process name**

Blocking by process name may be problematic in this case, since the process names for Oracle’s Java and any other non-Oracle Java are almost certainly going to be identical (for example, **java** as the process name.) Blocking Oracle’s Java by process name will mean that the non-Oracle Java you may be installing to replace Oracle’s Java will be caught by the same process-based block.

This is to say nothing of apps which may have embedded Java runtimes you’re not aware of; blocking Oracle’s Java by process may inadvertently also block the processes run by an app’s embedded Java runtime.

**Block by code signature**

This may be the best approach, as you may be able to use Oracle Java’s code signing signature and bundle identifier to block Oracle Java. Solutions which can do this include the following:

* Google’s [Santa](https://github.com/google/santa)
* [Jamf Protect](https://www.jamf.com/products/jamf-protect/)

These solutions should be able to block by the code signature’s Team Identifier and the java binaries’ bundle identifier(s). [You can find these by running the following command](https://support.addigy.com/hc/en-us/articles/4403542583187-How-To-Get-The-Team-ID-Bundle-ID-and-Code-Requirement):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | codesign -dv /path/to/java/binary |

[view raw](https://gist.github.com/rtrouton/0677268ea5c9d43026f2fb2ebc0302ba/raw/0097a7d271ab57d2d21f40d58035acc9ef75a7e3/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0677268ea5c9d43026f2fb2ebc0302ba#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Here’s an example of using the **codesign** command to get the code signature’s Team Identifier and the bundle identifier for the **java** binary in Oracle’s Java JDK 11.0.20:

* Bundle identifier: **Identifier**
* Team Identifier: **TeamIdentifier**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % codesign -dv /Library/Java/JavaVirtualMachines/jdk-11.jdk/Contents/Home/bin/java |
|  | Executable=/Library/Java/JavaVirtualMachines/jdk-11.jdk/Contents/Home/bin/java |
|  | Identifier=com.oracle.java.11.0.20.java |
|  | Format=Mach-O thin (arm64) |
|  | CodeDirectory v=20500 size=936 flags=0x10000(runtime) hashes=18+7 location=embedded |
|  | Signature size=9010 |
|  | Timestamp=Jun 14, 2023 at 5:32:54 AM |
|  | Info.plist entries=5 |
|  | TeamIdentifier=VB5E2TV963 |
|  | Runtime Version=11.1.0 |
|  | Sealed Resources=none |
|  | Internal requirements count=1 size=188 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/9e874ff7550a576c0b315c0dad2d05e9/raw/903bf1fa0cb0c7a0c9b8bfd42bafbcc9a564bb77/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9e874ff7550a576c0b315c0dad2d05e9#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

**Note:** The bundle identifier may be different for each version of Oracle’s Java. You may be able to block using only the Team Identifier, but the drawback of this is that you may also block other Oracle apps which use that same code signing Team Identifier, like [Oracle’s VirtualBox hypervisor software](https://www.virtualbox.org):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % codesign -dv /Applications/VirtualBox.app |
|  | Executable=/Applications/VirtualBox.app/Contents/MacOS/VirtualBox |
|  | Identifier=org.virtualbox.app.VirtualBox |
|  | Format=app bundle with Mach-O thin (x86\_64) |
|  | CodeDirectory v=20500 size=19145 flags=0x10000(runtime) hashes=587+7 location=embedded |
|  | Signature size=9009 |
|  | Timestamp=Jul 27, 2023 at 11:49:35 AM |
|  | Info.plist entries=17 |
|  | TeamIdentifier=VB5E2TV963 |
|  | Runtime Version=10.15.6 |
|  | Sealed Resources version=2 rules=13 files=224 |
|  | Internal requirements count=1 size=192 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/e82e5be6481a01b8603c1cf8f5eb2a0e/raw/24c1647dcce00a1d54cf7923b9467c06348f0a8c/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e82e5be6481a01b8603c1cf8f5eb2a0e#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

**Block with parental controls**:

You can use a macOS configuration profile to set [all binaries in a particular directory path to be blocked from running](https://derflounder.wordpress.com/2017/05/20/application-blacklisting-using-management-profiles/). While this functionality [has been deprecated by Apple as of macOS Catalina](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsapplicationrestrictions), it continues to work as of macOS Ventura.

In this case, you can set the enclosing directory paths of Oracle’s Java binaries to the block list and thus prevent Oracle’s Java binaries from running:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % java -version |
|  | exec failed: Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied" UserInfo={NSLocalizedFailureReason=Failed to execute /Library/Java/JavaVirtualMachines/jdk-1.8.jdk/Contents/Home/bin/java: Permission denied} |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/6f324b2bac655dab5975f65b3a550f4a/raw/19f91909cbbee2f1115c7c55c494e262aaeef46d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/...