---
title: High Fidelity detections are Low Fidelity detections, until proven otherwise, Part 2
url: https://www.hexacorn.com/blog/2024/08/01/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise-part-2/
source: Hexacorn
date: 2024-08-02
fetch_date: 2025-10-06T18:02:26.562785
---

# High Fidelity detections are Low Fidelity detections, until proven otherwise, Part 2

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

[← Previous](https://www.hexacorn.com/blog/2024/07/14/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise/)
[Next →](https://www.hexacorn.com/blog/2024/08/02/the-value-proposition-of-building-and-maintaining-an-internal-threat-hunting-team/)

# High Fidelity detections are Low Fidelity detections, until proven otherwise, Part 2

Posted on [2024-08-01](https://www.hexacorn.com/blog/2024/08/01/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise-part-2/ "10:29 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my [last post](https://www.hexacorn.com/blog/2024/07/14/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise/) I looked at ‘good’ file names. Today I will look at them again.

Sort of…

Over the years I have written a number of yara rules that use a peculiar condition that hits on an internal PE file name sometimes being preserved inside some of the PE files, both DLL and EXE… If you ever looked at an internal structure of a PE file you know that its export directory has a capability to preserve a programmer-chosen, internal file name that is compiled into the final binary file, and that internal file name often differs from the file name being used on a file system level…

Some Threat actors know about it and abuse it, but many don’t – in some cases allowing us to write very precise detection rules… That internal file name is a great forensic and telemetry artifact and it would be a crime not to use it, where applicable…

In my old Yara rules I would usually rely on this (somehow) esoteric syntax that I copied and pasted from someone else (sorry, don’t remember who that person was):

```
strings:
   $dllname = "<filename>"
condition:
   ($dllname at pe.rva_to_offset(uint32(pe.rva_to_offset(pe.data_directories [pe.IMAGE_DIRECTORY_ENTRY_EXPORT].virtual_address)+12)))
```

which is basically a rudimentary PE file format parsing condition checking if the specific ANSI string is present at a given place inside the file’s export directory (where that internal PE file name resides) and if it matches the string I defined…

After the release of yara 4.0.0 we can use a far more simpler construct to define the very same condition – one that leverages the PE module:

```
pe.dll_name=="<filename>"
```

Now…

This internal file name preserved in the export directory of many PE files is a bit of a phenomenon because if we just focus on native Windows OS binaries we will discover a lot of interesting bits. Say, we look at the native PE files taken from the Windows 11 system32 directory — we can easily discover a number of PE files where the ‘external’ (file system-based) and ‘internal’ (PE export directory-based/pe.dll\_name) file names do not match…

Here’s a quick & dirty [list](https://hexacorn.com/d/internal_filenames.txt) of such files that I’ve extracted…

And just for a second, let me digress here – I must mention that I generated this quick&dirty file for the purpose of writing this post but then… just eyeballing its content… my attention was immediately drawn to this interesting finding…:

* The Windows’ library *AppVTerminator.dll* uses an internal file name of *Arnold.dll*. What’s more, the file exports a function called ‘IllBeBack’

If you ever watched the 80/90’s Terminator movie franchise you know this really cannot be a coincident, and a quick google session that followed led me to this [gist](https://gist.github.com/EvanMcBroom/ac2b9084bf3c84939efcb9c894fadd07) by [@mcbroom\_evan](https://twitter.com/mcbroom_evan). I really love to be the first reporting OS-related interesting facts, peculiarities, and things that make you go “hmmm interesting’, but I was simply late in this case! Kudos to you [@mcbroom\_evan](https://twitter.com/mcbroom_evan)!

Back to our quick & dirty list…

Looking at the internal file names used by many native Windows OS binaries we can immediately see a bit of a pattern:

* dll.dll 21
* deffile.dll 8
* stub.dll 7
* SWEEPRX.dll 3
* vm3ddevapi-release.exe 3
* vm3dum.dll 3
* vm3dum10.dll 3
* module.dll 3
* sb.dll 2
* iwb.dll 2
* USERCPL.dll 2
* smalldll.dll 2
* DeviceInfoParser.dll 2
* AppxDeploymentExtensions.dll 2
* inprocserver.dll 2
* winload.sys 2
* PACK2.dll 1
* Source.dll 1
* respub.DLL 1
* client.dll 1

Seeing these stats we can speculate that lot of early code for these native system DLLs might have been created via a simple copy&paste mechanism (*dll.dll*, *deffile.dll*, *smalldll.dll* and *stub.dll* are hardly unique file names…). Some discrepancies suggest internal struggles with terminology f.ex. *PrintIsolationProxy.dll* vs. *PrintSandboxProxy.dll* and some are completely off the limits (*tcblaunch.exe*/*winload.exe* -> *winload.sys*). I’d like to believe there is a logic to it, but I am not very optimistic.

Anyway…

Now that we know what this post is all about, let’s take a stab at a far larger set… that is, legitimate files produced by legitimate vendors – many of their files do include these internal PE file names too, so it would be a crime not to explore this data set…

So, here it is, [a list](https://hexacorn.com/d/_file_types_PE_INTERNAL_NAME.zip) of legitimate internal PE file names you may come across while analyzing samples. Using any of these ‘good’ internal file names as a ‘**pe.dll\_name==”<filename>”**‘ condition in your yara rules will most likely produce FPs… You have been warned 🙂

Note: you can’t use the \_file\_types\_PE\_INTERNAL\_NAME.zip/\_file\_types\_PE\_INTERNAL\_NAME files for commercial purposes.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Clustering](https://www.hexacorn.com/blog/category/clustering/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/08/01/high-fidelity-detections-are-low-fidelity-detections-until-proven-otherwise-part-2/ "Permalink to High Fidelity detections are Low Fidelity detections, until proven otherwise, Part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")