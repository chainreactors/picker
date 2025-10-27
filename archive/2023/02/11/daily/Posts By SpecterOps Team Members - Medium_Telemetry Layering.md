---
title: Telemetry Layering
url: https://posts.specterops.io/telemetry-layering-89185b5348ba?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-02-11
fetch_date: 2025-10-04T06:23:16.628159
---

# Telemetry Layering

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F89185b5348ba&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Ftelemetry-layering-89185b5348ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Ftelemetry-layering-89185b5348ba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-89185b5348ba---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-89185b5348ba---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Telemetry Layering

[![Jonathan Johnson](https://miro.medium.com/v2/resize:fill:64:64/1*ro6iOomAZwYlmMgljL7EfA.png)](https://jonny-johnson.medium.com/?source=post_page---byline--89185b5348ba---------------------------------------)

[Jonathan Johnson](https://jonny-johnson.medium.com/?source=post_page---byline--89185b5348ba---------------------------------------)

8 min read

·

Feb 10, 2023

--

Listen

Share

## Introduction

Creating detections can be challenging. There often isn’t a “simple” way to detect something, and once we see an event that seems to correlate with the activity we are looking for, it is easy to become fixated. We create that detection and move on. However, what if other telemetry sources had helped provide a different context to that action of interest? Could we have created multiple detections with various telemetry sources to provide better coverage? If a telemetry source can be “evaded,” should we not use it?

I want to answer these questions by talking about telemetry layering as it relates to the operation — loading .NET assemblies. Telemetry layering is built within the detection section of the [funnel of fidelity](/introducing-the-funnel-of-fidelity-b1bb59b04036) and ideally leads into detection layering (a subject for another day) that helps layer detection strategies on top of each other. Every detection has pros and cons, and these could be anything from the signal-to-noise ratio to an adversary’s patching a function so that logs aren’t created.

## .NET Assemblies

.NET assemblies consist of managed code and are the building blocks of any .NET application. They can come in the form of EXEs or DLLs. Using .NET allows for the following:

* Every Windows machine comes with some pre-installed .NET version. Check out [this link](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies) by Microsoft to check out the default installed versions.
* .NET is managed so you don’t have to worry about memory management.
* Assemblies can be loaded into memory, so you don’t have to drop a file to disk — i.e. executes in memory.
* Microsoft has incorporated a lot of libraries into the .NET framework that solve a lot of common programming tasks for developers like HTTP connections, cryptography, inter-process communication (IPC) (like named pipes).

Due to the reasons above a lot of offensive tooling is written in .NET and attackers like to opt-in to this capability. Which is why Cobalt Strike capabilities like execute-assembly and [InlineExecute-Assembly](https://github.com/anthemtotheego/InlineExecute-Assembly) exist.

## The Operation

The operation that we are going to look into is when someone loads a .NET assembly. There are various native ways this can be done. Let’s show a couple:

**PowerShell:**

```
Add-Type -TypeDefinition ‘public class Foo {}’
```

**.NET:**

```
[System.Reflection.Assembly]::LoadFrom(“C:\Example.dll”)
```

Obviously there are other .NET class methods like [System.Reflection.Assembly]::Load that could be used, but this blog isn’t a write-up on how loading an assembly works. If you are interested in this type of information I found the following blogs insightful:

* [Investigating .NET CLR Usage Log Tampering Techniques for EDR Evasion](https://bohops.com/2021/03/16/investigating-net-clr-usage-log-tampering-techniques-for-edr-evasion/) by bohops
* [Don’t Be Rude, Stay: Avoiding Fork&Run .NET Execution With InlineExecute-Assembly](https://securityintelligence.com/posts/net-execution-inlineexecute-assembly/) by @anthemtotheego

## Telemetry Layering

The last bit of my research after looking into any operation that I want to make a detection for is to identify the appropriate telemetry that can be used for a detection rule. Once that is done, how do I pick the appropriate telemetry source to use for a detection rule? What are its pros and cons? Can it be evaded in some way? Now, unfortunately, there is going to be some assumptions that will have to be made before moving forward:

* We have tracked the operation to the telemetry sources below

It is possible to validate, through code analysis, whether an event will be generated for when a target operation is executed. Unfortunately, that will take away from this post a little bit, so we will skip over it.

### Telemetry Source 1: AMSI

When looking into loading a .NET assembly, there are a couple of avenues to obtain visibility into this operation. One is through an ETW provider called Microsoft-Antimalware-Scan-Interface (AMSI). A lot of EDR’s have been using this data to pick up telemetry. We aren’t going to dive into all of the benefits of the AMSI event source and its inter-workings. Matt Graeber and Jimmy Astle have already done this for us in their blog: [Better know a data source: Antimalware Scan Interface](https://redcanary.com/blog/amsi/). AMSI provides a lot of great information, but the two we will focus on are:

* Appname — Application that submitted content to be scanned
* Content — For .NET this will be the PE contents of the .NET assembly that was loaded into memory

Great! Let’s see what this looks like:

Press enter or click to view image in full size

![]()

This seems like a nice event to use (assuming our vendor collects it), we see that a .NET assembly was loaded, the ProcessId where the .NET assembly was loaded, but the content doesn’t seem to be very helpful. As Matt and Jimmy mention in their blog this is supposed to be the PE contents of the .NET assembly. Though the content is helpful, there might need to be some additional manipulation to figure out what is in those contents.

As some might know, AMSI can be patched. This is done by patching out the [AmsiScanBuffer](https://learn.microsoft.com/en-us/windows/win32/api/amsi/nf-amsi-amsiscanbuffer) function before loading .NET (and others) code. This is common in a lot of CobaltStrike profiles. An example is [threatexpress malleable-c2](https://github.com/threatexpress/malleable-c2) repository. Although we are not trying to detect CobaltStrike’s execute-assembly or other capabilities that allow for the loading of .NET code, it is important to know that this patching capab...