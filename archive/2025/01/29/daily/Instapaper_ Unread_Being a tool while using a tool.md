---
title: Being a tool while using a tool
url: https://www.hexacorn.com/blog/2025/01/25/being-a-tool-while-using-a-tool/
source: Instapaper: Unread
date: 2025-01-29
fetch_date: 2025-10-06T20:12:06.912437
---

# Being a tool while using a tool

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2025/01/01/smuggling-payloads-and-tools-in-using-wim-images-part-2/)
[Next →](https://www.hexacorn.com/blog/2025/01/31/9839/)

# Being a tool while using a tool

Posted on [2025-01-25](https://www.hexacorn.com/blog/2025/01/25/being-a-tool-while-using-a-tool/ "1:22 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This case is kinda DFIR-fascinating.

There is an unwritten rule in the DFIR world that says – always check the results provided by one tool, with another tool, or manually…

Well… it all sounds nice in theory, until we come across a case that will change it all.

So…

If you use many different tools, and on regular basis, be warned that this case will destroy your faith in them…

Ready?

Let’s go!

I have been using Total Commander for over 2 decades. I absolutely love this tool, and can’t imagine working with gazillion of files and samples that I play with on regular basis, without using it.

But recently, I got fooled by it.

When you download the Signal desktop client installer for Windows (v7.39), you can browse its contents with Total Commander+its (various) archive plugins to see the following output:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/01/tc_signal1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/01/tc_signal1.png)

I was specifically interested in the `Signal.exe` binary so I used TC to copy `Signal.exe` to my temporary work folder.

To my surprise, the sigcheck reported that this binary was compiled for… ARM processors!

```
Verified:       Signed
Signing date:   01:00 2025-01-23
Publisher:      Signal Messenger, LLC
Company:        Signal Messenger, LLC
Description:    Signal
Product:        Signal
Prod version:   7.39.0.0
File version:   7.39.0
MachineType:    64-bit ARM
```

Huh?

I was puzzled.

I literally downloaded what I believed to be an installer of Signal that was meant for Intel-based Windows, but now I am seeing the ARM binary inside it!

<Anxiety level intensifies>

I then tried the very same approach with the installer of the older version of Signal (7.38), but the result was the same….

What’s going on here? I wondered…

I must make a note here that the Signal setup program is using the Nullsoft installer to deliver the software to users. And in the reverse engineering world, once you recognize the installer type, the natural step in analysis is to decompile the script used by the installer.

Using the older version of 7z (7z\_1505) that extracts the [NSIS].nsi script file I got the following output listing all the embedded files inside the most recent Signal installer:

```
$PLUGINSDIR\app-64.7z
$PLUGINSDIR\app-arm64.7z
$PLUGINSDIR\nsExec.dll
$PLUGINSDIR\nsis7z.dll
$PLUGINSDIR\SpiderBanner.dll
$PLUGINSDIR\StdUtils.dll
$PLUGINSDIR\System.dll
$PLUGINSDIR\WinShell.dll
$R0\Uninstall Signal.exe
$PLUGINSDIR\installerHeaderico.ico
[NSIS].nsi
```

Huh…

As you can see, there are two embedded 7z files listed above:

* $PLUGINSDIR\app-64.7z
* $PLUGINSDIR\app-arm64.7z

The first one is Intel-based, and the second one is ARM-based.

The [NSIS].nsi script references them here (using the respective 7z file depending on the architecture):

```
label_796:
  StrCmp $_40_ ARM64 0 label_799
  SetOverwrite on
  AllowSkipFiles on
  File $PLUGINSDIR\app-arm64.7z
  Goto label_802
label_799:
  StrCmp $_40_ 64 0 label_802
  File $PLUGINSDIR\app-64.7z
  Goto label_802
```

Kinda surprisingly, we can actually locate these 2 7z files inside the main installer file at the following offsets:

* 0x0003C57B – app-arm64.7z
* 0x087904C4 – app-64.7z

and after carving/extraction, browsing them with Total Commander we can reveal their content as shown below:

**ARM (app-arm64.7z):**

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/01/tc_signal2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/01/tc_signal2.png)

**INTEL (app-64.7z):**

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/01/tc_signal3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/01/tc_signal3.png)

Do you see where it is going?

With files/installers using many embedded files, the Total Commander’s (+its plugins’) visibility seems to be limited only to the first embedded archive, in this case it is the *app-arm64.7z* file! (in fact, it’s a bit more complicated in case TC or its plugins can parse PE file/their sections of the sample, adding an additional layer in a game of nested dolls).

When I look at that original Signal installer again now I can see the Total Commander (+its plug-ins) only see the first embedded archive. As a result, I see the Intel-targeting setup file embedding the ARM-targeting file shown in TC. The proper handling would include full file analysis of the installer and recognition of all embedded archives as virtual subfolders… at least.

The bottom line is this:

* Let’s admit it, file formats are complicated, especially if they are mixed/overlapping
* Trust, but verify — use multiple tools to extract/parse installer scripts, analyze/compare their outputs
* Don’t trust GUI-only programs
* Question what you see (in my case: the Intel-CPU targeting installer including ARM binaries as seen by TC in the installer’s body looked odd)
* Analyze as many properly formatted file types as possible on a file format level to spot anomalies and inconsistencies in the future
* Use carving and static analysis tools on samples: extracted sections, embedded media files, executables, configuration files, URLs, IPs. github repository addresses, PDB paths, etc. – this can add a lot of intelligence value long term

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Batch Analysis](https://www.hexacorn.com/blog/category/batch-analysis/), [File Formats ZOO](https://www.hexacorn.com/blog/category/file-formats-zoo/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/), [Malware Analysis](https://www.hexacorn.com/blog/category/malware-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/01/25/being-a-tool-while-using-a-tool/ "Permalink to Being a tool while using a tool").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")