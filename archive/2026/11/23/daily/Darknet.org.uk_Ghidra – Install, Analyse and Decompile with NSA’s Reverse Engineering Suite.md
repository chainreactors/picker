---
title: Ghidra – Install, Analyse and Decompile with NSA’s Reverse Engineering Suite
url: https://www.darknet.org.uk/2026/11/ghidra-nsa-reverse-engineering-decompiler/
source: Darknet.org.uk
date: 2026-11-23
fetch_date: 2026-11-24T11:47:45.130850
---

# Ghidra – Install, Analyse and Decompile with NSA’s Reverse Engineering Suite

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

Darknet.org.uk

Darknet.org.uk is a cybersecurity site online since 2000. It covers security tools, technical research and hacking news, alongside an archive of earlier posts.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / Ghidra – Install, Analyse and Decompile with NSA’s Reverse Engineering Suite

# Ghidra – Install, Analyse and Decompile with NSA’s Reverse Engineering Suite

Published November 24, 2026 |

Views: 177

Ghidra is the NSA’s reverse engineering suite, free and open source: give it a compiled program and it shows you the disassembly and, beside it, a decompiler’s attempt at the original C. Getting the current release, 12.2, to start is the first hurdle, because its launcher has firm ideas about where Java lives. The second is finding the program’s real `main`, which the decompiler will not label for you. This guide gets you past both.

![Ghidra: NSA's free reverse engineering suite, beside a dark maze with one orange path leading to a lit point at its centre.](data:image/svg+xml...)![Ghidra: NSA's free reverse engineering suite, beside a dark maze with one orange path leading to a lit point at its centre.](https://www.darknet.org.uk/wp-content/uploads/2026/11/ghidra-nsa-reverse-engineering-decompiler-1024x576.webp)

## What is Ghidra?

Ghidra is a software reverse engineering framework “developed by NSA’s Research Directorate”, in the project’s own words, and released under the Apache 2.0 licence. Its documentation lists disassembly, assembly, decompilation, debugging, emulation, graphing and scripting among its capabilities, and it reads the common executable formats for a wide range of processor instruction sets. It runs as a desktop application, and as a headless analyser you can drive from the command line.

Advertisement

People use it to work out what a binary does when there is no source: triaging malware, finding the bug a patch fixed, checking what a closed-source agent sends home, or reading firmware. For Android apps, [jadx](https://www.darknet.org.uk/2026/11/jadx-decompile-android-apk-to-java/) gets you to readable Java faster; Ghidra is the tool for native code.

It is very much alive. Version 12.2 came out on 22 October 2026, after four 12.1 releases since May, and commits were still landing on the main branch in November.

## How to download and install Ghidra

There is no installer. Each release on GitHub is a single zip for every platform, and you unzip it where you want it and run the launcher inside. The README warns against unzipping a new release on top of an existing one, and against the two “Source Code” downloads on the release page, which are not what you want. The 12.2 file is `ghidra_12.2_PUBLIC_20261016.zip`, 569,712,708 bytes, and its published SHA-256 is:

2c2cd776db3c1f6a097ba418922378ac3649cadd5e844a6f5f088ae628a7be67

|  |  |
| --- | --- |
| 1 | 2c2cd776db3c1f6a097ba418922378ac3649cadd5e844a6f5f088ae628a7be67 |

Check it in PowerShell before you unzip it:

Get-FileHash .\ghidra\_12.2\_PUBLIC\_20261016.zip -Algorithm SHA256

|  |  |
| --- | --- |
| 1 | Get-FileHash .\ghidra\_12.2\_PUBLIC\_20261016.zip -Algorithm SHA256 |

Getting Started lists Windows 10 (build 1809 or later), Linux and macOS 10.13 or later, with at least 4 GB of RAM and 1 GB of disk for the program itself. Then start it with `ghidraRun.bat` on Windows or `./ghidraRun` on Linux and macOS. That is the whole install, as long as Java is in place.

## Ghidra and Java: JDK 25, PATH and JAVA\_HOME

Ghidra 12.2 needs at least JDK 25, 64-bit, and a full JDK rather than just a runtime. Getting Started points to Adoptium Temurin and Amazon Corretto as free long-term-support builds. Installing one is not quite the end of it, though. The launcher looks for `java` on your `PATH`, or under `JAVA_HOME`, which wins if both are set, and with neither it stops at once. I ran the headless launcher with no Java on the path and no `JAVA_HOME`:

Advertisement

![Ghidra 12.2's analyzeHeadless.bat in PowerShell stopping with ERROR: The 'java' command could not be found in your PATH or with JAVA_HOME](data:image/svg+xml...)![Ghidra 12.2's analyzeHeadless.bat in PowerShell stopping with ERROR: The 'java' command could not be found in your PATH or with JAVA_HOME](https://www.darknet.org.uk/wp-content/uploads/2026/11/ghidra-12-2-java-command-not-found.webp)

With no Java it can see, the launcher gives up before doing anything.

“The ‘java’ command could not be found in your PATH or with JAVA\_HOME” is the message to search for if you hit it. The usual cause is a JDK unpacked from a zip, which puts nothing on the path. Either add the JDK’s `bin` folder to your `PATH`, which Getting Started walks through for each platform, or set `JAVA_HOME` for the session before you launch. In PowerShell, with the folder wherever you unpacked it:

$env:JAVA\_HOME = "C:\Tools\jdk-25.0.5+8"
.\ghidraRun.bat

|  |  |
| --- | --- |
| 1  2 | $env:JAVA\_HOME = "C:\Tools\jdk-25.0.5+8"  .\ghidraRun.bat |

If the Java it finds is older than 25, the launcher uses it to look for a newer JDK on the machine, and asks you for the path to one if it cannot find it, according to Getting Started. So an old Java 8 or 17 on the path is fine as long as a JDK 25 is installed too.

## How to analyse and decompile a binary with Ghidra headless

Ghidra works on projects: you import a program into one, Ghidra analyses it, and you read the result. In the desktop application that is interactive. The same work also runs without a window through `support\analyzeHeadless.bat` (`analyzeHeadless` on Linux and macOS), and that is the version you can script and repeat. It takes a folder for the project, a project name, the file to import, and optionally scripts to run before or after analysis.

To try it on something you are entitled to take apart, use the binary Ghidra ships for its own class: `WinHelloCPP.exe`, a small Windows program among the class’s exercise files in the release’s `docs` folder. I imported it with Ghidra 12.2 on Temurin 25.0.5, in a sandbox with no network, and ran a short post-analysis script of my own that prints what the analysis found and the decompiled C of the entry point. To repeat it, work in the folder that holds the unzipped `ghidra_12.2_PUBLIC`, create an empty `proj` folder for the project and a `scripts` folder, and save this in `scripts` as `DarknetDecompile.java`:

// Prints what auto-analysis found, then the decompiler's C for the entry
// point and for any function whose name contains "WinMain".
//@category darknet
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.symbol.Symbol;
import java.util.LinkedHashSet;
import java.util.Set;
public class DarknetDecompile extends GhidraScript {
@Override
protected void run() throws Exception {
println("program: " + currentProgram.getName());
println("format: " + currentProgram.getExecutableFormat());
println("language: " + curr...