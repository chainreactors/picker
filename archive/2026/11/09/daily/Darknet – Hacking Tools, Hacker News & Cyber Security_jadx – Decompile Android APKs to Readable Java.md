---
title: jadx – Decompile Android APKs to Readable Java
url: https://www.darknet.org.uk/2026/11/jadx-decompile-android-apk-to-java/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-11-09
fetch_date: 2026-11-10T09:00:42.724220
---

# jadx – Decompile Android APKs to Readable Java

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet.org.uk is a cybersecurity site online since 2000. It covers security tools, technical research and hacking news, alongside an archive of earlier posts.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / jadx – Decompile Android APKs to Readable Java

# jadx – Decompile Android APKs to Readable Java

Published November 9, 2026 |

Views: 85

jadx turns an Android app’s compiled code back into Java you can read. Point it at an APK and you get a folder of `.java` files and decoded resources, or open the app in its GUI and search it, jump to declarations and follow where a method is used. It is usually the first thing to reach for when you want to know what an app actually does. It will not decompile all of it, though, and how it marks the parts it gets wrong decides how far you can trust what you are reading.

![jadx: Decompile Android APKs to readable Java, beside a glass lens turning scattered grey code fragments into ordered orange lines.](https://www.darknet.org.uk/wp-content/uploads/2026/11/jadx-decompile-android-apk-to-java-1024x576.webp)

jadx turns an Android app’s compiled code back into Java you can read.

## What is jadx?

jadx is an open-source decompiler for Android, written in Java and released under the Apache 2.0 licence, with a command-line tool and a GUI in the same download. It reads Dalvik bytecode from APK, dex, AAB, XAPK and similar packages, decodes `AndroidManifest.xml` and the resources in `resources.arsc`, and turns the code into Java. It also opens plain Java bytecode (jar, class and aar files) and smali, and it has a deobfuscator for apps whose names have been shrunk to single letters.

Advertisement

That makes it a reading tool: triaging a suspicious app, finding the endpoint or the hard-coded key a pentest report needs, or working out which check you will have to patch. It does not rebuild an app. For that you need Apktool, and the two are often used together (more on that below).

The project dates from 2013 and is busy: the current release is 1.5.6, from 10 July 2026, and commits were still landing at the end of October.

## How to download and install jadx

Each release on GitHub has three downloads. `jadx-1.5.6.zip` is the one for every platform, with both tools under `bin`: `jadx` and `jadx-gui`, and `.bat` versions of each for Windows. It needs a 64-bit Java 11 or later. The two Windows bundles run `jadx-gui-1.5.6.exe` instead, and the larger `with-jre` bundle, 99 MB, carries its own Java, so it is the one to take on a Windows machine without a JDK. On a Mac, `brew install jadx`; on Arch, `sudo pacman -S jadx`; and Flathub has it as `com.github.skylot.jadx`. On Kali it is a package too, `sudo apt install jadx`, and Kali rolling, Arch and Homebrew all carry 1.5.6, according to Repology.

The 1.5.6 zip is 72,646,741 bytes, and its published SHA-256 is:

545ea2be9c242511bc145755cf4bda2485ade42966e096f8b4d3da2a230e8974

|  |  |
| --- | --- |
| 1 | 545ea2be9c242511bc145755cf4bda2485ade42966e096f8b4d3da2a230e8974 |

Check it in PowerShell before you unzip it:

Get-FileHash .\jadx-1.5.6.zip -Algorithm SHA256

|  |  |
| --- | --- |
| 1 | Get-FileHash .\jadx-1.5.6.zip -Algorithm SHA256 |

jadx keeps its settings and cache in your user profile, and it stops if it cannot create them. I ran it in a sandbox with no profile, where every decompile failed at once with “Failed to init common directories” and an access-denied error on `AppData\Roaming\skylot`. If you hit the same on a locked-down or shared account, point the two folders somewhere you can write with the environment variables the README documents:

Advertisement

$env:JADX\_CONFIG\_DIR = "C:\apk-work\jadx-config"
$env:JADX\_CACHE\_DIR = "C:\apk-work\jadx-cache"

|  |  |
| --- | --- |
| 1  2 | $env:JADX\_CONFIG\_DIR = "C:\apk-work\jadx-config"  $env:JADX\_CACHE\_DIR = "C:\apk-work\jadx-cache" |

## How to decompile an APK with jadx from the command line

Give it an output folder with `-d` and the app. From the unzipped folder, in PowerShell:

.\bin\jadx.bat -d out\binaryeye binaryeye.apk

|  |  |
| --- | --- |
| 1 | .\bin\jadx.bat -d out\binaryeye binaryeye.apk |

On Linux or a Mac it is `bin/jadx`, or plain `jadx` after a package install. To see it on a real app, I used Binary Eye 1.75.5, the open-source barcode scanner from F-Droid that I also took apart for the Apktool guide, on Temurin 21. jadx worked through 2,539 classes in 23.6 seconds:

![jadx 1.5.6 decompiling the Binary Eye 1.75.5 APK in PowerShell and finishing with the line ERROR - finished with errors, count: 8](data:image/svg+xml...)![jadx 1.5.6 decompiling the Binary Eye 1.75.5 APK in PowerShell and finishing with the line ERROR - finished with errors, count: 8](https://www.darknet.org.uk/wp-content/uploads/2026/11/jadx-1-5-6-decompile-binary-eye-1024x431.webp)

jadx 1.5.6 on Binary Eye 1.75.5: complete output, and an error count at the end.

The output has two folders, `sources` with 2,798 Java files and `resources` with the decoded manifest and resources. Look at the last line, though. jadx reported “finished with errors, count: 8” and exited with code 1, although the output was complete and perfectly usable. The sandbox run that failed at start-up, before decompiling anything, exited with 1 as well. So if you script jadx, the exit code alone cannot tell you which of the two you have: read the log too. The usable run worked through its progress count and ended on “finished with errors”; the failed one stopped at “Process error” within nine seconds, before any progress line.

A few options are worth knowing from the start. `-s` (`--no-src`) skips the code and `-r` (`--no-res`) skips the resources, so you can decode only the half you need. `--single-class` decompiles just one class by its full name. `-j` sets the number of threads, which by default is half your CPU threads. And `--deobf` renames the shrunk classes and members: on Binary Eye it moved the R8-renamed classes that jadx had put in a folder called `defpackage` to one called `p000`, with the same number of files. Readable names help when you are following code around; they are jadx’s guesses, not the originals.

## What jadx does when it cannot decompile a method

It warns you in the code, and by default it shows you the bytecode instead of guessing. The README is upfront that in most cases jadx cannot decompile all of an app, and Binary Eye bore that out: 406 of the Java files carry at least one `JADX WARN` or `WARNING` comment, 20 contain a method marked “Code decompiled incorrectly”, and 12 have a method whose dump was skipped altogether.

None of those 20 is in the app’s own code, the 86 Java files under `de.markusfisch.android.binaryeye`. They are all in AndroidX, Material Components and the classes R8 renamed. On a real target, look at where the warnings are before deciding how far to trust the output: the code you came for may decompile cleanly while the libraries around it fail, or the other way round.

Here is one of the failures, the `onCreate` method of AndroidX’s `InitializationProvider`, as jadx writes it by defa...