---
title: Apktool – Decompile, Edit and Rebuild Android APKs
url: https://www.darknet.org.uk/2026/11/apktool-decompile-edit-rebuild-android-apk/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-11-02
fetch_date: 2026-11-03T08:49:50.074249
---

# Apktool – Decompile, Edit and Rebuild Android APKs

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

[![darknet.org.uk logo](data:image/svg+xml...)![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet.org.uk is a cybersecurity site online since 2000. It covers security tools, technical research and hacking news, alongside an archive of earlier posts.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / Apktool – Decompile, Edit and Rebuild Android APKs

# Apktool – Decompile, Edit and Rebuild Android APKs

Published November 2, 2026 |

Views: 103

Apktool turns an Android app back into something you can read and change: the manifest as plain XML, the layouts and strings as resource files, and the code as smali, the assembly language of Android’s runtime. Change what you need and it packs the folder back into an APK. It has been doing that round trip since 2010, and most of the tutorials you will find for it were written for version 2. Since version 3, several of their commands no longer work.

![Apktool: Decompile, edit and rebuild Android APKs, beside a curved graphite shell opened to reveal stacked layers and orange resin.](data:image/svg+xml...)![Apktool: Decompile, edit and rebuild Android APKs, beside a curved graphite shell opened to reveal stacked layers and orange resin.](https://www.darknet.org.uk/wp-content/uploads/2026/11/apktool-decompile-edit-rebuild-android-apk-1024x576.webp)

## What is Apktool?

Apktool is an open-source command-line tool for reverse engineering Android apps, written in Java and released under the Apache 2.0 licence. An APK is a zip file, but unzipping one gets you compiled code in `classes.dex`, a binary `resources.arsc` and an `AndroidManifest.xml` you cannot read. Apktool decodes all three into source form you can edit, then packs the edited folder back into an APK, which you sign before it will install.

Advertisement

That makes it the tool for jobs that change an app rather than just read it: making a build debuggable, adding a network security configuration for proxy testing, patching a check in smali, or translating the strings. It does not give you Java source. For reading the logic of an app, jadx is the better tool, and the two are often used side by side (more on that below).

The current release is 3.0.3, from 20 July 2026, and the project was still committing in October. One name clash to clear up: “Apktool M”, which fills Google’s suggestions for this search, is a separate Android app, not a version of this project.

## How to install Apktool on Windows, Linux and macOS

Apktool is a single jar, so the only prerequisite is Java. The install guide still gives Java 8 as the minimum, but version 3 dropped 32-bit platforms, and the `aapt2` program it carries inside the jar for Windows and Linux is a 64-bit x86 build (I read the binaries’ headers). Install a current 64-bit JDK and you avoid the question. The 3.0.3 jar does start on a 32-bit Java 8 – mine printed its version on one – but decoding and building are where `aapt2` does its work. Everything below I ran on Temurin 21, a free 64-bit build of the JDK.

Then get the jar from the project’s [GitHub release](https://github.com/iBotPeaches/Apktool/releases/tag/v3.0.3) or its Bitbucket downloads page, and check it before you use it. The 3.0.3 jar is 15,478,013 bytes, and its published SHA-256 is:

dbf930b076c6b9be08d57c449cacefc3bdd6b71ebd59b3066fc0e1f5b14f9423

|  |  |
| --- | --- |
| 1 | dbf930b076c6b9be08d57c449cacefc3bdd6b71ebd59b3066fc0e1f5b14f9423 |

In PowerShell:

Get-FileHash .\apktool\_3.0.3.jar -Algorithm SHA256

|  |  |
| --- | --- |
| 1 | Get-FileHash .\apktool\_3.0.3.jar -Algorithm SHA256 |

Stay on 3.0.2 or later if you open APKs you did not build. Apktool has a history of path-traversal bugs, where a crafted app makes the decoder write files outside the output folder, and 3.0.2 fixed the latest one, CVE-2026-39973, by validating resource type names against Android’s own rules.

Advertisement

You can run the jar directly with `java -jar apktool_3.0.3.jar`, but the install guide’s wrapper scripts are worth the extra minute. On Windows, put `apktool.bat` and the jar in the same folder on your PATH; on Linux and macOS the shell wrapper and jar go in `/usr/local/bin`, made executable, and on a Mac `brew install apktool` does it for you. The guide says to rename the jar to `apktool.jar`, though the current Windows script will also find the highest-numbered `apktool_X.Y.Z.jar` beside it.

The guide calls the wrappers optional, a way to avoid typing `java -jar`. Read the Windows one and it does more than that: it starts Java with a 1 GB heap, UTF-8 file encoding and a switch that relaxes Java’s checks on zip64 fields, and run bare, the jar gets none of those. Those options come after `-jar` in the script, which looks like a mistake, but Java accepts them there: the script’s exact Java line printed `3.0.3` on Temurin 21. If a large app fails to decode with the bare jar, try it through the wrapper before anything else.

Windows users have one more step. Windows treats `Layout.xml` and `layout.xml` as the same file, and the install guide asks you to turn on case sensitivity for correct operation. Microsoft’s way is per folder, from PowerShell run as Administrator, on an empty folder you will decode into:

fsutil.exe file setCaseSensitiveInfo C:\apk-work enable

|  |  |
| --- | --- |
| 1 | fsutil.exe file setCaseSensitiveInfo C:\apk-work enable |

## How to decompile an APK with Apktool

Decoding is `d` (or `decode`), and I would name the output folder every time:

apktool d app.apk -o app

|  |  |
| --- | --- |
| 1 | apktool d app.apk -o app |

The reason is that the project disagrees with itself about the default. The 3.0.3 help says `apk.out`, while the documentation’s decoding page shows `bar.apk` going to a folder called `bar`. With `-o` you never have to find out. Add `-f` to overwrite a folder from an earlier run.

To see it on a real app, I took Binary Eye 1.75.5, an open-source barcode scanner, straight from F-Droid and checked the download against F-Droid’s index. Decoding it took 44 seconds:

![Apktool 3.0.3 decoding the Binary Eye 1.75.5 APK in PowerShell: baksmaling classes.dex, loading the framework, decoding resources and the manifest](data:image/svg+xml...)![Apktool 3.0.3 decoding the Binary Eye 1.75.5 APK in PowerShell: baksmaling classes.dex, loading the framework, decoding resources and the manifest](https://www.darknet.org.uk/wp-content/uploads/2026/11/apktool-3-0-3-decode-binary-eye.webp)

Decoding Binary Eye 1.75.5 with Apktool 3.0.3.

Inside the folder you get the decoded `AndroidManifest.xml`, the layouts, strings and other resources as editable files, the code as smali, and `apktool.yml`, the file Apktool reads to rebuild the app. Leave that file alone unless you know why you are changing it. Binary Eye came out as 2,936 smali files, and 2,606 of them sit loose at the top with names like `a.smali` and `a0.smali` rather than in package folders. Expect to search rather than browse.

The command in the screenshot adds `-p work\framework`, which sets where Apktool keeps its framework files. You will not normally need it; I ran it in a sandbox with no user profile,...