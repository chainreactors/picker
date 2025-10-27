---
title: How To Detect and Decloak Linux Stealth Rootkit Data
url: https://www.sandflysecurity.com/blog/how-to-detect-and-decloak-linux-stealth-rootkit-data
source: Sandfly Security Blog RSS Feed
date: 2022-11-16
fetch_date: 2025-10-03T22:53:01.667685
---

# How To Detect and Decloak Linux Stealth Rootkit Data

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# How To Detect and Decloak Linux Stealth Rootkit Data

15 November 2022

Rootkits

Linux stealth rookits have a variety of mechanisms to hide on a host. Aside from standard tactics such as hiding running processes (which we show you [how to decloak here](https://www.sandflysecurity.com/blog/linux-stealth-rootkit-process-decloaking-tool-sandfly-processdecloak/)), they also can hide data inside files. This tactic can prevent security teams from detecting malicious modules loading and maintaining persistence on a host.

In this article, we'll show you how to decloak this hidden Linux rootkit data using two methods:

1) Using common command line tools *ls, cat,* and *wc.*

2) Using memory mapped file I/O with the free [*sandfly-file-decloak*](https://github.com/sandflysecurity/sandfly-file-decloak) utility.

We are releasing a free tool using the second method to help security teams detect cloaked data.

## Intrusion Detection Philosophy - Police Interrogation

To understand how to find stealth rootkits on Linux we suggest you adopt a philosophy used by our product Sandfly. That philosophy is taken directly from police interrogation techniques and is simple:

**Ask the same question multiple ways to see if the answers are identical.**

If you ask the question multiple ways, but one or more of the answers is different, then you know there is a problem. You see this method used by the police when investigating a case. For instance:

"Where were you last night?"

"We have surveillance footage showing your vehicle at the crime scene, why is that?"

"You were seen with the victim last night. What were you doing with them?"

Now all of the above questions try to get the same data: Was the suspect where the crime happened? The questions start out generic and vague to let the suspect tell a lie. Then they start to get more specific about the incident and police can then use the initial answers to start finding inconsistencies in the story and ask more questions.

Sandfly adopts the same approach with our tactics hunting and we want you to do the same when investigating a Linux host for compromise. Don't ask just one question and take the answer as truth. Instead, ask the same question several different ways and see if the answers are the same.

Using the above, we're going to ask the same question about a system with a Linux Loadable Kernel Module (LKM) stealth rootkit running on it and see if the answers are the same. Almost always, they are not.

## Linux Stealth Rootkit Hiding Data

Most rootkits try to maintain persistence by hiding in various start-up files located under */etc* on Linux. For LKM rootkits, they need to load their module into the kernel during boot to activate. After activation they can then hide the data in the file they used to start.

For example, a stealth rootkit will often target the following files to load its module on boot:

`/etc/modules
/etc/ld.so.conf`

Critical system directories like below can also contain malicious insertion code:

`/etc/modules-load.d
/etc/init.d
/etc/rc*.d`

There are any number of places it can happen, but the above are pretty common.

To prevent the module from being seen by the victim, the rootkit will have a special tag sequence they can wrap around their boot-up entry. When the rootkit is active it will not show the data that is between these tags. For instance, the Reptile rootkit uses a couple special tags (*#<reptile>* and *<#/reptile>*) to hide any data that is between them when active.

For example under */etc/modules:*

`# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.

# malicious content below
#<reptile>
malicious_module_to_load
#</reptile>`

The tags appear as comments in the file, but the file *malicious\_module\_to\_load* will be read on boot and inserted into the kernel space. After this happens if you run commands like *cat* or even an editor like *vi* it will not show the tags or data between them to the viewer. We see this in action in this screenshot of opening the file with *vi* on an infected host:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Stealth rootkit cloaked data invisible.](https://www.datocms-assets.com/56687/1668127936-vi-cloaked-data.png?auto=format&dpr=2&q=60&w=920 "Stealth rootkit cloaked data invisible.")

By cloaking the data the malicious rootkit module can maintain persistence indefinitely unless you are able to see what is going on. We're going to show you how to do just that next.

## Searching for Incorrect Byte Counts

Hiding data like this is very clever, but it suffers from a big issue on Linux and that is this:

**The Linux file system wants consistency and doesn't want to hide how many bytes are present in a file by removing data on the fly.**

Something on the system will know the data is there because it *is* there. We just have to ask the right questions.

To take advantage of this we are going to again ask the system the same question in multiple different ways. Our question for finding this attack is simple:

**How many bytes do you see in this file?**

We will ask this question of the file system with a simple directory listing. Then we ask the same question of the kernel by having it give us the bytes of data it reads. Then, we see if they match. We will use the tools *ls,* *cat,* and *wc* to do this in the commands below:

`ls -al /etc/modules
cat /etc/modules | wc -c`

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![A Linux stealth rootkit hiding data and being revealed.](https://www.datocms-assets.com/56687/1668508075-decloak-with-ls-and-wc.png?auto=format&dpr=2&q=60&w=920 "A Linux stealth rootkit hiding data and being revealed.")

Here we see the file */etc/modules* in the directory listing under an active LKM rootkit. It shows 283 bytes according to the file system using *ls*. Now we ask the kernel to read the file and tell us how many bytes are there using the *cat /etc/modules | wc -c* command to count the bytes. Here *wc* reports 222 bytes are present from the *cat* command output. **There is a 61 byte discrepancy between these results.** Where are those bytes that the *cat* command couldn't see?

## The Case of the Missing Bytes

The byte counts above don't match because the rootkit cannot cover all the ways a file can be seen on a Linux host. Yes, it hooked the file read calls that *cat* and other command line tools use. But, it is not altering what the file system returns in the internal *stat()* calls for file size data.

In this case the file system reports the correct size with the *ls* command. However reading the data passes through the hooked kernel calls and the data is scrubbed for the *cat* command. One is correct and the other is not. Basically, we are expecting the rootkit to lie to us and are using the fact it is lying to reveal itself by getting a known good value it didn't expect to compare against.

The key takeaway is this:

**It's one thing to get the kernel to lie about file contents, but something entirely more complicated to get the file system to agree with this lie.**

Again the file system wants to maintain consistency to avoid data corruption. It is much harder to have bogus data returned through the kernel and also get the file system to show the same bogus data. The task would require much more coding to do well and likely would cause serious system performance and stability issues even if it did work in some capacity.

In our above technique we simply are asking the kernel and the file system a simple question: "Do you agree that both of these files have the...