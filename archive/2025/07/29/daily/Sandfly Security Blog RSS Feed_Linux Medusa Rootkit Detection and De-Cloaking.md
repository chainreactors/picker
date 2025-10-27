---
title: Linux Medusa Rootkit Detection and De-Cloaking
url: https://sandflysecurity.com/blog/linux-medusa-rootkit-detection-and-de-cloaking
source: Sandfly Security Blog RSS Feed
date: 2025-07-29
fetch_date: 2025-10-06T23:52:27.557584
---

# Linux Medusa Rootkit Detection and De-Cloaking

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Linux Medusa Rootkit Detection and De-Cloaking

27 July 2025

Malware

There is a new rootkit called [Medusa](https://github.com/ldpreload/Medusa) on Linux and we wanted to give some tips on how to deal with this style of attack. Medusa is what we call an LD\_PRELOAD style of stealth rootkit. Basically, it intercepts calls going to dynamically linked libraries and replaces the functions with altered versions to change what the user sees. It is related to LD\_PRELOAD because this is a special kind of section on Linux systems that allow dynamically loaded libraries to be prioritized and loaded before other libraries. In other words, pre-loading them before anyone else.

### Dynamic Libraries on Linux

So what is dynamic library intercepting? Well these rootkits do a kind of Jedi mind trick on system commands. For example, when you list a directory with the *ls* command on Linux the rootkit intercepts the normal system call to show all files in a directory and instead returns an altered list that leaves out the directories and files it wants to hide.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux rootkit performs Jedi Mind Trick to hide.](https://www.datocms-assets.com/56687/1753654332-medusa-jedi-mind-trick.jpeg?auto=format&dpr=2&q=60&w=920 "Linux rootkit performs Jedi Mind Trick to hide.")

The reason this works is because most Linux binaries use what are called *dynamic* libraries. These are used as a way to allow many programs to share common system functions instead of needing to have them all themselves. It saves a lot of space when programs can share common code and makes updating easier because a single library update applies to all programs instead of needing to do it across many.

Think of dynamic libraries like a big toolbox that everyone in the neighborhood can share. When someone needs a wrench, they simply go to the toolbox to use it. This way, everyone can get access to the same tools but they all don't need to go out and buy their own tools.

### Dynamic Library Hijacking

Medusa and similar rootkits abuse this shared library concept by intercepting all the programs that want to use the library and replacing it with a corrupted version. The new version often can be used to return bogus data to hide files, fake process data, hide network ports, and even conceal things like high CPU usage to help cryptominers and other high CPU tasks evade detection. The idea is simple but works surprisingly well because it avoids going into the kernel to hide which carries significantly higher risk of crashing a system or breaking during updates.

### De-Cloaking Medusa and Other LD\_PRELOAD Rootkits

If you think an LD\_PRELOAD style rootkit is on a system, you can easily poke around and de-cloak it by using a statically built version of *BusyBox* like shown below. The reason we want to use the *static* version of *BusyBox* is that it won't use dynamically loaded libraries. The libraries are statically built with the binary. In other words, statically built binaries are "batteries included" and do not rely on system dynamic libraries to work.

Because static binaries do not rely on dynamic libraries to work, they are not fooled by rootkits that have modified them. Statically built binaries simply don't use these altered libraries at all which means they see through the smoke screen being created.

Here we see what the normal system shell sees on a compromised Debian host, and what the same shell sees as we run it with a static version of *BusyBox*. The hidden directory under */lib/libseconf* is hidden with the normal system shell command *ls*, but becomes visible with the *BusyBox* version when you run the shell:

*busybox ash*

*<run ls and other shell commands like normal>*

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Using statically built BusyBox to de-cloak Medusa rootkit.](https://www.datocms-assets.com/56687/1753654431-medusa-rootkit-busybox-static.png?auto=format&dpr=2&q=60&w=920 "Using statically built BusyBox to de-cloak Medusa rootkit.")

### Loading Static BusyBox

Many Linux distributions will have a static version of *BusyBox* or you can build it yourself. On our sample Debian host we simply ran this for the demonstration to install it:

*apt install busybox-static*

**WARNING:** The above command is for demonstration purposes. If you do this on a compromised system you will alter the state of the box which may not be what you want to happen. It can overwrite deleted areas on the file system or alter the package manager state corrupting important forensic data. You may want to have this binary on another host or disk and mount it remotely. Or, move it to the host for investigation perhaps into the */dev/shm* ramdisk area to prevent writing to the disk.

If you are unsure what you want to do here, contact someone familiar with Linux incident response and ask for advice.

### BusyBox Commands for Linux Forensics

*BusyBox* has many other commands like *ash (shell), netstat*, *cat, echo,* *sha1sum,* and so on that will show hidden processes, ports, users, etc. as well. The ones we underlined below are useful for doing quick investigations if you want to bypass LD\_PRELOAD rootkit hiding. Not all versions of *BusyBox* have these commands compiled in, so if you see some missing you may need to build your own version that includes them.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Useful BusyBox commands for Linux forensics.](https://www.datocms-assets.com/56687/1753656408-medusa-busybox-static-commands-highlighted.png?auto=format&dpr=2&q=60&w=920 "Useful BusyBox commands for Linux forensics.")

### Other LD\_PRELOAD Rootkit Considerations

LD\_PRELOAD rootkits slow down the box quite a bit as every command is potentially being intercepted. Users may notice the command line is not as snappy, etc. and this can lead to a closer look. These rootkits work OK, but like most stealth rootkits on Linux, they often cause more trouble than they are worth.

### Automate Finding Medusa and Other Stealth Rootkits

Stealth rootkits on Linux can be a significant threat and can hide quite well. Due to their nature, security teams should use automated means to search for rootkits so they get an early alert before attackers get really dug in.

For Medusa and other stealth rootkits, we get alerts on this activity with Sandfly and our agentless Linux security platform. Below we see some alerts. We only use static binaries so are not affected by the hiding in this kind of rootkit and can de-cloak suspicious activity immediately.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![A suspicious file left by Medusa found by Sandfly.](https://www.datocms-assets.com/56687/1753656488-medusa-suspicious-file-details.png?auto=format&dpr=2&q=60&w=920 "A suspicious file left by Medusa found by Sandfly.")

### AI Analysis of Linux Rootkit

Sandfly's new AI enabled forensic analyst is really powerful. Even if your team has limited Linux security experience, the new AI assistant can quickly summarize and recommend investigation actions.

Below we pass in the affected host for AI analysis and get back an accurate summary of the situation. Sandfly's agentless security data is very accurate and detailed, making analysis with major LLM providers extremely valuable to security teams conducting an investigation.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly's AI analysis of a host infected by Medusa.](https://www.datocms-assets.com/56687/1753656543-medusa-host-analysis.png?auto=format&dpr=2&q=60&w=920 "Sandfly's AI analysis of a host infected by Medusa.")

### Virtual Security Analyst at Your Finger...