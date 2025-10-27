---
title: Protected: Flare-On 11 – Task 7
url: https://hshrzd.wordpress.com/2024/12/09/flare-on-11-task-7/
source: hasherezade's 1001 nights
date: 2024-12-10
fetch_date: 2025-10-06T19:37:23.043777
---

# Protected: Flare-On 11 – Task 7

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/dark-cyber-scenery-bouncy-castle-hell-with-a-description-on-2.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

[Skip to content](#content "Skip to content")

* [Home](https://hshrzd.wordpress.com)
* [Projects](https://hshrzd.wordpress.com/mycode/)
  + [PE-sieve](https://hshrzd.wordpress.com/pe-sieve/)
  + [PE\_unmapper](https://hshrzd.wordpress.com/pe_unmapper/)
  + [IAT Patcher](https://hshrzd.wordpress.com/iat-patcher/)
  + [PE-bear](https://hshrzd.wordpress.com/pe-bear/)
  + [ViDi](https://hshrzd.wordpress.com/vidi-visual-disassembler/)
  + [DMA Unlocker](https://hshrzd.wordpress.com/mycode/dma-unlocker/)
* [How to start RE/malware analysis?](https://hshrzd.wordpress.com/how-to-start/)

[← Flare-On 11 – Task 5](https://hshrzd.wordpress.com/2024/12/08/flare-on-11-task-5/)

[Process Hollowing on Windows 11 24H2 →](https://hshrzd.wordpress.com/2025/01/27/process-hollowing-on-windows-11-24h2/)

## [Flare-On 11 – Task 7](https://hshrzd.wordpress.com/2024/12/09/flare-on-11-task-7/)

Posted on [December 9, 2024](https://hshrzd.wordpress.com/2024/12/09/flare-on-11-task-7/ "2:31 am") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

*[Flare-On](https://flare-on.com/) is an annual CTF run by [Mandiant Flare Team](https://cloud.google.com/blog/topics/threat-intelligence/flareon-11-challenge-solutions). In this series of writeups I present solutions to some of my favorite tasks from this year. All the sourcecodes are available on my Github, in dedicated repository: [flareon2024](https://github.com/hasherezade/flareon2024)*.

Task 7 comes with the following description:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/task7_desc.png?w=716)

We are provided with a PCAP, and a PE binary. At this point we can guess that the binary has generated the traffic saved in the PCAP, and we are supposed to decrypt it.

## Overview

#### The PCAP

The PCAP contains TCP traffic between two machines, represented by LAN addresses: 192.168.56.101 and 192.168.56.103.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/connection.png?w=1024)

The communication is an exchange of small data portions of various lengths, each of them is encrypted.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/tcp_stream.png?w=600)

#### The PE

I started the analysis from examining the executable with PE-bear. Even at the first look, the binary seems a bit atypical. Although in the task description it is mentioned that we will be dealing with a .NET binary, the file that we’ve got seems to be compiled to a native code…

Among the sections we can see some interesting names, that are not common for natively compiled binaries, such as `.managed` and `.hydrated`. The `.hydrated` section is unpacked dynamically in memory:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/sections.png?w=1024)

The export table has one entry: `DotNetRuntimeDebugHeader`.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/export_table.png?w=560)

The PE is very bulky, and it is clear that it has been statically linked with some libraries.

Googling for those atypical artifacts lead me to the great article, that explained in good details what I am dealing with, and how to proceed: <https://harfanglab.io/insidethelab/reverse-engineering-ida-pro-aot-net/>. So, it is a an AOT (Ahead Of Time compiled) .NET binary.

## Resolving functions by FLIRT signatures

The [article about AOT analysis](https://harfanglab.io/insidethelab/reverse-engineering-ida-pro-aot-net/) provides [a basic set of FLIRT signatures that can be used to makes sense out of the code](https://harfanglab.io/medias/2024/01/net_aot_7_0_1423.zip).

Before applying the signatures, the code is very convoluted, and hard to grasp:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/main_before.png?w=827)
![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/managed_main_before.png?w=464)

After applying all the signatures, we can see much clearer picture of what is going on:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/main_after_signs.png?w=644)
![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/after_signatures_main.png?w=746)

### Creating custom signatures

Although the found signatures help to clarify a lot what is going on, they are not sufficient. There are still plenty of function that haven’t been identified. To really make sense out of the code, we need to identify the libraries with which the task was compiled, and prepare our own signatures with a proper coverage.

As we know from the previous overview, the file `.hydrated` section is unpacked in memory. So, I decided to dump the executable with [PE-sieve,](https://github.com/hasherezade/pe-sieve/) to have this section saved in the binary that I am analyzing. Inside this section I found [some strings that suggest that the BouncyCastle](https://gist.github.com/hasherezade/a5b9aebae9f3e07743a4b9b2da91a98c#file-hydrated-txt-L959) cryptographic library has been used (and other strings belonging to various cryptographic functions).

Example:

```
Org.BouncyCastle.EC.Fp_Certainty
Org.BouncyCastle.EC.Fp_MaxSize
```

To create the relevant signatures for Bouncy Castle, I had to first create an AOT compiled .NET project with the Bouncy Castle library incorporated. The creation of AOT project, and generating signatures out of it, is very well documented in [the tutorial that I mentioned earlier](https://harfanglab.io/insidethelab/reverse-engineering-ida-pro-aot-net/).

#### Creating and publishing the AOT project

To create an AOT project, we need at least Visual Studio 2022. Upon creating a new .NET project, the option enabling AOT publishing has to be selected.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/aot_project.png?w=587)

The project can then be compiled to the typical .NET binary, or to the AOT binary. In order to generate an AOT binary we need to “Publish” it.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/publish_button.png?w=320)

It then requires us to fill settings of where an in which form the code should be published. Our target has to be compatible with the sample that we are analyzing. Once we filled all the settings (as on the picture), we need to click the “Publish” button. If everything went fine, the build will be saved to our predefined path.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/publish_settings.png?w=896)

Of course the goal is to create an executable that contains all the functions from the BouncyCastle library that our analyzed sample has, so that we can further identify them. At this point I don’t know yet what those functions are, but strings from the `.hydrated` section give some hints. We also need the functions related to the network communication.

To create an example with the Bouncy Castle library, I used some snippets from: [https://asecuritysite.com/csharp](https://asecuritysite.com/csharp/bc_ec02) (i.e. <https://asecuritysite.com/csharp/bc_ec02> ). It was kind of a trial and error, collecting and applying various signatures until the code was clarified enough with them.

I used the latest version of Bouncy Castle, added to the project via NuGet:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/nuget.png?w=356)

Several different versions are available to select, so sometimes it takes some trial and error to find out which one fits:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/bouncy_library.png?w=648)

This way, we get an AOT binary with Bouncy Castle, compiled with symbols. Now we can load it into IDA, and generate the FLIRT signatures out of those symbols.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/create_sig_file...