---
title: RunMRU is not the only one forensic artifact left by the “Run” Prompt
url: https://cyberdefnerd.com/2024/11/13/runmru-is-not-the-only-one-forensic-artifact-left-by-the-run-prompt/
source: Instapaper: Unread
date: 2024-11-22
fetch_date: 2025-10-06T19:23:13.543473
---

# RunMRU is not the only one forensic artifact left by the “Run” Prompt

[Skip to content](#main)

[![CyberDefNerd](https://cyberdefnerd.com/wp-content/uploads/2024/11/cropped-CyberDefNerd__1_-removebg-preview.png)](https://cyberdefnerd.com/)

* [Home](https://cyberdefnerd.com/)
* [Articles](https://cyberdefnerd.com/blog/)
* [Videos](https://cyberdefnerd.com/videos/)
* [About](https://cyberdefnerd.com/tools/)

[Subscribe](https://www.linkedin.com/in/krzysztof-gajewski-537683b9/)

* [Home](https://cyberdefnerd.com/)
* [Articles](https://cyberdefnerd.com/blog/)
* [2024](https://cyberdefnerd.com/2024/)
* [November](https://cyberdefnerd.com/2024/11/)
* [13](https://cyberdefnerd.com/2024/11/13/)
* RunMRU is not the only one forensic artifact left by the “Run” Prompt

Posted in[Forensics](https://cyberdefnerd.com/category/forensics/)

# RunMRU is not the only one forensic artifact left by the “Run” Prompt

Posted by

![](https://secure.gravatar.com/avatar/0a65a146cbfa1774e32687e50eabb5aa04bf7d155bec54e8f948e7b6e079a926?s=30&d=mm&r=g)

[Krzysztof Gajewski](https://cyberdefnerd.com/author/krzysiu_rysiu/ "View all posts by Krzysztof Gajewski")
2024-11-13[No Comments](https://cyberdefnerd.com/2024/11/13/runmru-is-not-the-only-one-forensic-artifact-left-by-the-run-prompt/#respond)

![](https://cyberdefnerd.com/wp-content/uploads/2024/11/mem.jpg)

In this article, we will discuss the ‘**Run**‘ prompt in Windows. In addition to covering the well-known **RunMRU** artifact in the registry, I’ll also introduce another artifact that reflects the usage of this feature, namely the **Activity Cache**…

Table of contents:

1. [Run prompt – Introduction](#RUNPROMPT)
2. [Example usage of the Run Prompt – Fake CAPTCHA](#FakeCAPTCHA)
3. [Forensics Collection](#ForensicsCollection)
4. [Registry – Analysis](#Registry)
5. [Activity Cache – Analysis](#ActivityCache)
6. [Summary](#Summary)

## 1. RUN PROMPT

First, let’s take a look at the RUN prompt. We all know how to press ‘Win + R,’ but what actually happens in the background? To understand this a little better, we need to locate the ‘Run’ program on the system.

It can find under `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools`, and it’s actually a .LNK file!

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/0-1.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/0-1.png)

But where does it point? Nowhere? If you click “Open file location” it will take you to EXPLORER … let’s parse that LNK file and see how it looks like:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/lnk.jpg)](https://cyberdefnerd.com/wp-content/uploads/2024/11/lnk.jpg)

As you can see, it realy does not point to any other executable, the only one refference we have here is **Microsoft.Windows.Shell.RunDialog**. So at least ,we know it is not a normal shortuck pointing to a diffrent PE file, like we would have for CHROME or EDGE.

## 2. Example usage of the Run Prompt – Fake CAPTCHA

Now it’s time to see how the **Run Prompt** is used. We’ll start with the recently common FAKA CAPTCHA campaign.

The first element of this campaign is a malicious page that asks you to verify you are not a robot:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/1-1.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/1-1.png)

If you click the button that looks like a normal CAPTCHA, a new window will appear, prompting you to launch a new ‘Run’ prompt and paste the contents of your clipboard:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/2-1.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/2-1.png)

Pasted content looks like that:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/3.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/3.png)

I am not gonna run that code, but let’s just quickly take a look at that payload:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/4.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/4.png)

Of course, it is BASE 64 ENCODED code – we can easly decode it using Notepad++:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/5.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/5.png)

We still can’t read it, but by using Notepad++ once more, we can replace all NUL characters with nothing to get a readable output:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/6-1.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/6-1.png)

In results we got the folloing code:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/7.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/7.png)

So, if we run the content of our clipboard as instructed, the Run prompt would simply start a new process for PowerShell, which in turn would download and execute code from the C2 server using IEX. For this demo, I don’t want to infect the VM, so we’ll run something else this way and then check all artifacts.

This is a command we will run, Powershell starting PING:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/8.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/8.png)

## 3. Forensics Collection

To properly analyze the execution of the Run prompt, we need to collect two things:

* The registry hive for the user running the Run prompt
* The Activity Cache database

Here’s the path to the the registry hive for the user – **NTUSER.DAT**: `C:\Users\<username>\NTUSER.DAT`. Don’t forget to collect transaction logs!

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/9.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/9.png)

The path to the **Activity Cache** in Windows is located in the following directory: `C:\Users\<username>\AppData\Local\Microsoft\Windows\ActivityCache`.

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/10.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/10.png)

Obviously, in a normal situation, you would perform a standard forensic collection that includes these two paths along with everything else. If you’re unsure about what should be collected, let me know in the comments, and we can discuss it in upcoming posts/episodes.

Armed with that two artifacts, we can start parsing them.

## 4. Registry – Analysis

We will start with the registry and focus on **RunMRU**.

**RunMRU** (Run Most Recently Used) is a registry key in Windows that stores a list of commands entered into the **Run** prompt. From a forensic perspective, **RunMRU** is valuable for tracking user activity, as it provides evidence of recently executed programs, files, or commands. This data can help investigators reconstruct user actions and identify potentially suspicious behavior or system compromises. The **RunMRU** key can be found in the Windows registry under: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`.

I will demonstrate two tools, that allow us to review that registry key:

* [Registry Explorer](https://download.ericzimmermanstools.com/net6/RegistryExplorer.zip) created by [Eric Zimmerman](https://www.linkedin.com/in/eric-zimmerman-6965b22/overlay/about-this-profile/)
* [RegRipper 4.0](https://github.com/keydet89/RegRipper4.0) created by [Harlan Carvey](https://www.linkedin.com/in/harlan-carvey-86a8694b/)

Starting with Registry Explorer, we need to install the .NET Framework; otherwise, Eric’s tool will not work:

[![](https://cyberdefnerd.com/wp-content/uploads/2024/11/11.png)](https://cyberdefnerd.com/wp-content/uploads/2024/11/11.png)

Once we have that, we can run the tool and open the registry hive we want to parse. If it’s a **dirty** hive, the tool will prompt you to provide **transaction** logs and will attempt to merge everything together.

A **DIRTY HIVE** refers to registry keys in Windows that are in an inconsistent or incomplete state due to uncommitted changes. These changes are often stored in memory and not yet written to the corresponding registry hive file on disk. When the system crashes, shuts down improperly, or experiences a sudden termination of a process that modifies the re...