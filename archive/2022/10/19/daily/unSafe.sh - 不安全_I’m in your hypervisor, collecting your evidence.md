---
title: I’m in your hypervisor, collecting your evidence
url: https://buaq.net/go-131512.html
source: unSafe.sh - 不安全
date: 2022-10-19
fetch_date: 2025-10-03T20:12:05.914992
---

# I’m in your hypervisor, collecting your evidence

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

I’m in your hypervisor, collecting your evidence

Authored by Erik SchamperData acquisition during incident response engagements is always a b
*2022-10-18 23:1:35
Author: [blog.fox-it.com(查看原文)](/jump-131512.htm)
阅读量:22
收藏*

---

**Authored by** Erik Schamper

Data acquisition during incident response engagements is always a big exercise, both for us and our clients. It’s rarely smooth sailing, and we usually encounter a hiccup or two. Fox-IT’s approach to enterprise scale incident response for the past few years has been to collect small forensic artefact packages using our internal data collection utility, “acquire”, usually deployed using the clients’ preferred method of software deployment. While this method works fine in most cases, we often encounter scenarios where deploying our software is tricky or downright impossible. For example, the client may not have appropriate software deployment methods or has fallen victim to ransomware, leaving the infrastructure in a state where mass software deployment has become impossible.

Many businesses have moved to the cloud, but most of our clients still have an on-premises infrastructure, usually in the form of virtual environments. The entire on-premises infrastructure might be running on a handful of physical machines, yet still restricted by the software deployment methods available within the virtual network. It feels like that should be easier, right? The entire infrastructure is running on one or two physical machines, can’t we just collect data straight from there?

Turns out we can.

## Setting the stage

Most of our clients who run virtualized environments use either VMware ESXi or Microsoft Hyper-V, with a slight bias towards ESXi. Hyper-V was considered the “easy” one between these two, so let’s first focus our attention towards ESXi.

VMware ESXi is one of the more popular virtualization platforms. Without going into too much premature detail on how everything works, it’s important to know that there are two primary components that make up an ESXi configuration: the hypervisor that runs virtual machines, and the datastore that stores all the files for virtual machines, like virtual disks. These datastores can be local storage or, more commonly, some form of network attached storage. ESXi datastores use VMware’s proprietary VMFS filesystem.

There are several challenges that we need to overcome to make this possible. What those challenges are depends on which concessions we’re willing to make with regards to ease of use and flexibility. I’m not one to back down from a challenge and not one to take unnecessary shortcuts that may come back to haunt me. Am I making this unnecessarily hard for myself? Perhaps. Will it pay off? Definitely.

The end goal is obvious, we want to be able to perform data acquisition on ideally live running virtual machines. Our internal data collection utility, “Acquire”, will play a key part in this. Acquire itself isn’t anything special, really. It builds on top of the Dissect framework, which is where all its power and flexibility comes from. Acquire itself is really nothing more than a small script that utilizes Dissect to read some files from a target and write it to someplace else. Ideally, we can utilize all this same tooling at the end of this.

## The first attempts

So why not just run Acquire on the virtual machine files from an ESXi shell? Unfortunately, ESXi locks access to all virtual machine files while that virtual machine is running. You’d have to create full clones of every virtual machine you’d want to acquire, which takes up a lot of time and resources. This may be fine in small environments but becomes troublesome in environments with thousands of virtual machines or limited storage. We need some sort of offline access to these files.

We’ve already successfully done this in the past. However, those times took considerably more effort, time and resources and came had their own set of issues. We would take a separate physical machine or virtual machine that was directly connected to the SAN where the ESXi datastores are located. We’d then use the open-source vmfs-tools or vmfs6-tools to gain access to the files on these datastores. Using this method, we’re bypassing any file locks that ESXi or VMFS may impose on us, and we can run acquire on the virtual disks without any issues.

Well, almost without any issues. Unfortunately, vmfs-tools and vmfs6-tools aren’t exactly proper VMFS implementations and routinely cause errors or data corruption. Any incident responder using vmfs-tools and vmfs6-tools will run into those issues sooner or later and will have to find a way to deal with them in the context of their investigation. This method also requires a lot of manual effort, resources and coordination. Far from an ideal “fire and forget” data collection solution.

## Next steps

We know that acquiring data directly from the datastore is possible, it’s just that our methods of accessing these datastores is very cumbersome. Can’t we somehow do all of this directly from an ESXi shell?

When using local or iSCSI network storage, ESXi also exposes the block devices of those datastores. While ESXi may put a lock on the files on a datastore, we can still read the on-device filesystem data just fine through these block devices. You can also run arbitrary executables on ESXi through its’ shell (except when using the execInstalledOnly configuration, or can you…? 😉), so this opens some possibilities to run acquisition software directly from the hypervisor.

Remember I said I liked a challenge? So far, everything has been relatively straightforward. We can just incorporate vmfs-tools into acquire and call it a day. Acquire and Dissect are pure Python, though, and incorporating some C library could overcomplicate things. We also mentioned the data corruption in vmfs-tools, which is something we ideally avoid. So that’s the next logical step? If you guessed “do it yourself” you are correct!

## You got something to prove?

While vmfs-tools works for the most part, it lacks a lot of “correctness” with regards to the implementation. Much respect to anyone who has worked on these tools over the years, but it leaves a lot on the table as far as a reference implementation goes. For our purposes we have some higher requirements on the correctness of a filesystem implementation, so it’s worth spending some time working on one ourselves.

As part of an upcoming engagement, there just so happened to be some time available to work on this project. I open my trusty IDA Pro and get to work reverse engineering VMFS. I use vmfs-tools as a reference to get an idea of the structure of the filesystem, while reverse engineering everything else completely from scratch.

Simultaneously I work on reconstructing an ESXi system from its “offline” state. With Dissect, our preferred approach is to always work from the cleanest slate possible, even when dealing with a live system . For ESXi, this means that we don’t utilize anything from the “live” system, but instead will reconstruct this “live” state within Dissect ourselves from however ESXi stores its’ files when it’s turned off. This can cause an initial higher effort but pays of in the end because we can then interface with ESXi in any possible way with the same codebase: live by reading the block devices, or offline from reading a disk image.

This also brought its own set of implementation and reverse engineering challenges, which include:

* Writing a FAT16 implementation, which ESXi uses for its bootbank filesystem.
* Writing a vmtar implementation, a slightly customized tar fil...