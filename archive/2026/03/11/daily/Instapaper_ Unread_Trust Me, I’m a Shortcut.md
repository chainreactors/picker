---
title: Trust Me, I’m a Shortcut
url: https://www.wietzebeukema.nl/blog/trust-me-im-a-shortcut
source: Instapaper: Unread
date: 2026-03-11
fetch_date: 2026-03-12T04:08:59.320213
---

# Trust Me, I’m a Shortcut

# Trust Me, I’m a Shortcut

Windows’ primary mechanism for shortcuts, LNK files, is frequently abused by threat actors for payload delivery and persistence. This blog post introduces several new LNK file flaws that, amongst other things, allow attackers to fully spoof an LNK’s target. It also introduces [lnk-it-up](https://www.github.com/wietze/lnk-it-up), a tool suite that can generate such deceptive LNK files, as well as detect anomalous ones.

---

## Shortcuts in Windows

Windows shortcuts exist to make life easier. Attackers noticed.

In an effort to improve the usability of the Windows operating system, LNK files were introduced with the launch of Windows 95 [[1](https://www.loc.gov/preservation/digital/formats/fdd/fdd000596.shtml)]. The concept of a pointer to another file or directory was not unique: symbolic links were introduced in 1982 in 4.1a BSD Unix [[2](https://github.com/dspinellis/unix-history-repo/blob/BSD-4_1c_2/usr/man/man0/changes.4-82#L28)]. The Windows LNK file is, however, different in a number of ways: its complex binary file format [[3](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/16cb4ca1-9339-4d0c-a68d-bf1d6cc0f943)] can point to files, directories, but also start programs with command-line arguments. Various optional metadata fields allow the operating system to find the intended target even when it has been renamed or moved; additionally, it is possible to store window settings, set the working directory the target should operate in, and a custom icon can be specified.

![The meme "Totally not a virus.Trust me...im a dolphin". The source/copyright are unknown.](/assets/2026-02-12-trust-me.jpg)

The meme "Totally not a virus.Trust me...im a dolphin". The source/copyright are unknown.

Although LNK files can be opened from a command prompt or script, they remain largely a GUI feature. Shortcuts can be recognised by the white square containing an arrow rendered on top of the shortcut’s icon in the bottom left corner. This visual cue is, in a way, a security feature: it makes it clear to users that upon double-clicking the file, something else will be opened. From an end-user perspective, the only practical way to inspect what an LNK file points to is by right-clicking it and clicking *Properties*. This opens the Properties dialog, which reveals the target of the LNK file.

Ever since their introduction, LNK files have been used by threat actors. A notable example is the Stuxnet campaign, which exploited critical Windows vulnerability CVE-2010-2568, where specially crafted LNK files could trick the system into loading arbitrary DLL files without the user even opening them [[4](https://euvd.enisa.europa.eu/vulnerability/CVE-2010-2568)]. More commonly, however, LNK files are used in social engineering attacks: email phishing [[5](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)], social media phishing [[6](https://labs.k7computing.com/index.php/from-lnk-to-rat-deep-dive-into-the-lnk-malware-infection-chain/)], torrents/Usenet downloads [[7](https://www.reddit.com/r/usenet/comments/1ffvk70/malicious_files_lnk_downloaded_from_ninjacentral/)], USB worms [[8](https://www.threatdown.com/blog/usb-worms-still-wriggling-on-to-under-protected-computers-after-all-these-years/), [9](https://asec.ahnlab.com/en/91280/)] and fake downloads [[10](https://cloud.google.com/blog/topics/threat-intelligence/lnk-between-browsers/)]. In all of these attacks, the shortcuts disguise themselves as something else, e.g. a PDF document, a drive folder or a legitimate piece of software, and lure the user into opening them. Upon triggering, the attacker’s payload is executed - as the aforementioned examples show, these often rely on Living off the Land Binaries and Scripts (LOLBINs/LOLBAS) [[11](https://lolbas-project.github.io/)].

Thus, the fact that LNKs still work as an attack vector, comes down to trust: users are made to believe that the shortcut opens something they are after or trust. The best defence is therefore to validate the target of an (unknown) LNK file prior to opening it.

But can Windows Explorer’s File Properties dialog be trusted?

## LNK Structure

To understand LNK attacks, let’s consider how they work. Unlike symbolic links and Microsoft’s own .URL files [[12](https://www.cyanwerks.com/formats/file-format-url.html)], which are in plain text, LNKs use a binary file format. Microsoft provides detailed information [[3](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/16cb4ca1-9339-4d0c-a68d-bf1d6cc0f943)] on the structure of LNK files, which tells us that LNK files have up to 5 sections, that are specified in the following order:

* `ShellLinkHeader`, which is always present;
* `LinkTargetIDList`, which is only present if the `HasLinkTargetIDList` flag is set;
* `LinkInfo`, which is only present if the `HasLinkInfo` flag is set;
* `StringData`, which is only present if at least one of 5 specific flags are set;
* `ExtraData`, which is a generic structure of which 0 or more can be present, depending on certain flags being set.

### ShellLinkHeader

An example `ShellLinkHeader`. Hover over the byte fields to see what they represent.

The `ShellLinkHeader` has a fixed length of 76 bytes; it is the only required structure in any LNK file. It contains a number of common data fields, and defines the layout of the LNK file.

The first two fields have predefined values that the documentation warns should not be changed.

The third field `LinkFlags` is, albeit just 4 bytes in size, perhaps the most fundamental field: this value sets out what the remainder of the LNK file will look like. For example, setting `HasTargetIdField` (`0x01`) indicates a `LinkTargetIDList` will be present, `HasLinkInfo` (`0x02`) indicates `LinkInfo` will be present, `HasArguments` (`0x40`) indicates `StringData` will contain command-line arguments, and so on. The documentation defines 25 possible flags that can be set here; meaning there are 225 ≈ 33.5 million possibilities.

This flags field is followed by `FileAttributes`, which indicates what file attributes the target has set; these are merely hints for how Explorer should display the target. Similarly, the following `CreationTime`, `AccessTime` and `WriteTime` represent timestamps of the target - these can be useful forensic artifacts. Finally, some integer/enum fields are defined: `FileSize`, `IconIndex`, `ShowCommand` (which controls if the target should be opened minimised, maximised, or normal), `HotKey`, and some reserved fields.

### LinkTargetIDList

An example representing `c:\test\a.txt`. Hover over the byte fields to see what they represent.

This structure is the main mechanism to represent the target file/directory of the LNK. Although not required, it is commonly found in LNK files - for example, an LNK file generated through Windows Explorer will always specify this structure. Typically, you will find an absolute path here: it could be on the local drive, a removable drive, a network path, or any other location that can be accessed through UNC [[13](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats#unc-paths)].

The `LinkTargetIDList` structure represents a path as a list of Shell Items [[14](https://github.com/libyal/libfwsi/blob/main/documentation/Windows%20Shell%20Item%20format.asciidoc#extension_block_0xbeef0026)], which unlike LNKs themselves, are not formally documented. Each part of a path may contain extra metadata, such as size, last modified, and optionally even NTFS attributes. This allows Windows to find targets even if they have been renamed or moved on disk. Next to this, special locations (e.g. My Computer, Network Locations, Control Panel) as well as special file types (e.g. Control Panel items) can be represented. For the purpose of this post, we will limit ourselves to normal, on-disk paths.

### LinkInfo

Regarding this ...