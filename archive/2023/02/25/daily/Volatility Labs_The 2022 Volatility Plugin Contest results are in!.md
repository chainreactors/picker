---
title: The 2022 Volatility Plugin Contest results are in!
url: https://volatility-labs.blogspot.com/2023/02/the-2022-volatility-plugin-contest-results.html
source: Volatility Labs
date: 2023-02-25
fetch_date: 2025-10-04T08:07:30.121609
---

# The 2022 Volatility Plugin Contest results are in!

# [[Archive of Volatility Labs]](https://volatility-labs.blogspot.com/)

**This site is an archive of the Volatility Labs blog. The blog has moved to <https://volatilityfoundation.org/volatility-blog/>**

## Friday, February 24, 2023

### The 2022 Volatility Plugin Contest results are in!

Results from the 10th Annual Volatility Plugin Contest are in! There were 8 submissions this year, including submissions from 2 contestants from previous years who have continued to build on their previous work. Submissions included updates to graphical interfaces, plugins to detect Linux rootkits, plugins to extract threat actor activity despite anti-forensics techniques, and a new analytical capability for leveraging handle information to augment investigations. As usual, we would like to thank the participants for their hard work on their submissions and contributions to Volatility community!

Independent open source projects and communities only remain viable because of contributors who are willing to sacrifice their time and resources. Please show your appreciation for the contestants’ contributions by following them on Twitter/GitHub/LinkedIn, providing feedback on their ideas, and helping to improve their code with testing, documentation, or contributing patches.

We would like to thank [Volexity](https://www.volexity.com/) for being a sustaining sponsor of the [Volatility Foundation](https://www.volatilityfoundation.org/) and, in particular, for contributing to this year’s contest. We would also like to thank the core Volatility developers and the previous winners of the contest who helped review and deliberate the submissions.**Placements and Prizes for the 2022 Volatility Plugin Contest:**

1st place and $3000 USD cash or One Free Seat at [Malware and Memory Forensics Training by the Volatility Team](https://www.memoryanalysis.net/memory-forensics-training) goes to:

> Felix Guyard: Prefetch Plugin, Inodes Plugin, AnyDesk Plugin, and VolWeb UI

2nd place and $2000 USD cash goes to:

> Asaf Eitani: check\_seqops Plugin, check\_fops Plugin, and fileless Plugin

3rd place and $1000 USD cash goes to:

> Aviel Zohar: HandleXView with Vol3xp UI

Below is a detailed summary of all submissions, ordered alphabetically by first name. If you have feedback for the participants, we're sure they'd love to hear your thoughts! As previously mentioned, these developers deserve praise for their amazing work. We look forward to seeing future work by these authors!

**Asaf Eitani:  check\_fops Plugin**

A common technique used by Linux kernel rootkits is to hook file operations in order to avoid detection. For example, it is often used to hide files, directories, and processes from procfs and any tools that rely on procfs data. This plugin is used to detect hooking on file\_operations structures. The plugin detects kernel-level malware that manipulates cached file structures to hide files from live analysis.

*Related References:*

<https://github.com/AsafEitani/rootkit_plugins/>

**Asaf Eitani:  check\_seqops Plugin**

This plugin detects manipulation of the data structures, seq\_operations, used to populate network analysis tools, such as netstat. Hooking these data structures is commonly leveraged by Linux kernel rootkits to avoid detection of network-related activity.

*Related References:*

<https://github.com/AsafEitani/rootkit_plugins/>

**Asaf Eitani:  Fileless Plugin**

This plugin detects processes that were created from a temporary file system (like /dev/shm or memfd) or instances where the executable was deleted after the process was launched. This is also a common techniques used to avoid detection by disk scanning security solutions and to make malware analysis more difficult. Temporary file systems are memory-only and cleared upon reboot. This makes them a prime location used by scripts and attackers to download, store, and manipulate files.

*Related References:*

<https://github.com/AsafEitani/rootkit_plugins/>

**Aviel Zohar: HandleXView**

This submission adds another very practical capability to Vol3xp, a GUI for Volatility 3 that is already loaded with nice features. HandleXView triages handle usage (aka resource sharing) across processes to help analysts spot anomalies and malicious behaviors, such as the following:

* Credential theft
* Bypassing security controls
* Code injection
* Persistence
* Privilege escalation
* Snooping on network activity
* Denial of service
* Vulnerability exploitation
* Monitoring keyboards and mice

Within the Vol3xp GUI, handle sharing can be visualized in 4 different ways, including a complete listing and organizing them by object, pid, and percentage.

*Related References:*

<https://github.com/memoryforensics1/Vol3xp>

**Felix Guyard: AnyDesk Plugin**

The AnyDesk plugin is the first Volatility Plugin to extract AnyDesk artifacts from memory samples. Attackers, such as Conti's ransomware operators, have been leveraging remote access software like AnyDesk to gain and maintain access to compromised systems. Threat actors also frequently attempt to obfuscate their actions with anti-forensics techniques, such as removing or modifying logs. The AnyDesk plugin finds memory resident "ad.trace" and "ad\_svc.trace" files and extracts useful information, such as IP addresses, timestamps, and involved PIDs, that can provide valuable context to investigators about user activity. The plugin also facilitates the integration of this data with the Timeliner plugin.

*Related References:*

<https://twitter.com/k1nd0ne>
<https://www.forensicxlab.com/posts/anydesk/>
[https://github.com/forensicxlab/volatility3\_plugins](https://github.com/forensicxlab/volatility3_plugins%22%20%5Ct%20%22_blank)

**Felix Guyard: Inodes Plugin**

The inodes plugin extracts inode metadata to help give investigators more context about files that are open on a system. The plugin can also generate a timeline of files opened by an active process. This can allow an investigator to piece together recent file system access by applications running on the system to determine persistence points, log files, and other components of a toolkit.

*Related References:*

<https://twitter.com/k1nd0ne>
[https://www.forensicxlab.com/posts/inodes/](https://www.forensicxlab.com/posts/inodes/%22%20%5Ct%20%22_blank)
[https://github.com/forensicxlab/volatility3\_plugins](https://github.com/forensicxlab/volatility3_plugins%22%20%5Ct%20%22_blank)

**Felix Guyard: Prefetch Plugin**

This plugin extracts information from memory-resident Windows Prefetch files to aid investigators.  This includes information about which programs were executed on the system, associated timestamps, and how many times they were run. The plugin attempts to collect this information across all modern versions of Windows. In developing this capability the author also implemented the Microsoft Xpress decompression algorithm in Python 3.

*Related References:*

<https://www.forensicxlab.com/posts/prefetch/>
<https://github.com/forensicxlab/Xpress_LZ77Huffman>
[https://github.com/forensicxlab/volatility3\_plugins](https://github.com/forensicxlab/volatility3_plugins%22%20%5Ct%20%22_blank)

**Felix Guyard: VolWeb**

This submission provides an update to the Django-based VolWeb web interface, which was originally submitted to the 2021 Volatility Plugin Contest. The interface is focused on improving the efficiency of investigators; offering compelling graphs and visualizations; and enabling collaborative analysis. In addition to integrating Linux support, the latest release has expanded capabilities regarding tagging and reporting. It provides a platform for future work and integrations.

*Related References:*

<https://github.com/k1nd0ne/VolWeb>
<https://twitter.com/k1nd0ne>
<https://www.forensicxlab.com/posts/cyberdefenders_brave/>

Here are some additional resources for previous contests and community-driven plugins:

Volatility Foundation Contest Home Page:  <http://www.volatilityfoundation.org/contest>

Volatili...