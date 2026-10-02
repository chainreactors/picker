---
title: Field Notes: Reconstructing the Attacker's LSASS Dump
url: https://dfir.ch/posts/field_notes_trickdump/
source: Over Security
date: 2026-10-01
fetch_date: 2026-10-02T07:49:24.745583
---

# Field Notes: Reconstructing the Attacker's LSASS Dump

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Field Notes: Reconstructing the Attacker's LSASS Dump

1 Oct 2026

**Table of Contents**

* [TrickDump in 3 Minutes](#trickdump-in-3-minutes)
* [Back to our incident](#back-to-our-incident)
* [Don’t stop at “LSASS was dumped”](#dont-stop-at-lsass-was-dumped)
* [Reconstructing the attacker’s LSASS dump](#reconstructing-the-attackers-lsass-dump)
* [Hunting](#hunting)
* [Conclusion](#conclusion)

One of the things I find fascinating is how much effort attackers sometimes put into avoiding traditional forensic artefacts. And yet, very often, they leave just enough behind for us to reconstruct what happened. This was exactly the case during a recent incident.

While analysing one of the compromised systems, we found a suspicious archive in the `C:\Users\Public` directory. Inside were four files:

* barrel.json
* lock.json
* shock.json
* trick.zip

A quick search led us to Ricardo J. Ruiz’s [TrickDump](https://github.com/ricardojoserf/TrickDump) project.

## TrickDump in 3 Minutes

`TrickDump` is an LSASS dumping technique with one particularly interesting property - it does not create a conventional LSASS minidump on the victim system. Instead, the information required to build the dump is collected separately. The project divides the operation into three stages:

* **Lock** collects information about the operating system using `RtlGetVersion`.
* **Shock** enables `SeDebugPrivilege`, locates LSASS, obtains a process handle, and collects information about the process and its loaded modules using native APIs such as `NtGetNextProcess`, `NtQueryInformationProcess`, and `NtReadVirtualMemory`.
* **Barrel** enables `SeDebugPrivilege`, walks the LSASS virtual address space, and dumps committed memory regions that are not marked `PAGE_NOACCESS` using `NtQueryVirtualMemory` and `NtReadVirtualMemory`.

The result is not a conventional lsass.dmp. Instead, you get metadata describing the process together with the individual chunks of LSASS memory. The project’s `create_dump.py` script can later combine those pieces into a minimal, parseable Windows minidump. This separation is important from a defensive point of view. File-based detections that rely on the creation of a recognizable LSASS minidump lose that signal with TrickDump. The tool still needs to obtain a handle to LSASS and read its memory, however, so the absence of a conventional dump file makes the activity less obvious to detect.

This also explained the four artefacts we had recovered: `lock.json` contained the operating-system information, `shock.json` described the process modules, `barrel.json` mapped dumped memory regions to virtual addresses, and `trick.zip` contained the corresponding memory-region data.

There is another interesting aspect: the operation can be split across three different executables instead of having a single process perform the complete credential-dumping workflow. TrickDump also supports several techniques for overwriting the .text section of ntdll.dll (disk, knowndlls, and debugproc) to bypass user-mode API hooks. However, one important limitation is that TrickDump does not work against LSASS when `Protected Process Light` (PPL) is enabled.

## Back to our incident

The files we recovered matched TrickDump’s expected output: three JSON files containing reconstruction metadata and a ZIP archive containing the captured memory regions. For example, `barrel.json` contained entries similar to:

```
[
  {
    "field0": "mmbsrqvwn.aqw",
    "field1": "0x7ffe0000",
    "field2": 4096
  }
]
```

The individual fields are not particularly descriptive, but the structure becomes much more meaningful once you know what TrickDump is doing. The archive contained hundreds of files with seemingly random filenames:

```
% ls -l | head
total 779080
-rw-rw-r--@ 1 malmoeb  staff     28672 Nov 30  1979 aacajycbx.cwe
-rw-rw-r--@ 1 malmoeb  staff     24576 Nov 30  1979 aacowerij.qtu
-rw-rw-r--@ 1 malmoeb  staff   4194304 Nov 30  1979 abmgppwnr.qut
-rw-rw-r--@ 1 malmoeb  staff     81920 Nov 30  1979 abobjzuqb.pvf
-rw-rw-r--@ 1 malmoeb  staff     12288 Nov 30  1979 acbkmsmuy.qry
-rw-rw-r--@ 1 malmoeb  staff     24576 Nov 30  1979 acemuxrfd.ytp
-rw-rw-r--@ 1 malmoeb  staff     12288 Nov 30  1979 acghylwki.kxv
-rw-rw-r--@ 1 malmoeb  staff     16384 Nov 30  1979 acjxcjhnf.fiu
-rw-rw-r--@ 1 malmoeb  staff    323584 Nov 30  1979 acslimbyb.lcu
```

Running `file` against one of them was not particularly enlightening: `aacajycbx.cwe: PEX Binary Archive`.

These files are chunks copied from the target process’s virtual memory. The filenames themselves are randomly generated; the mapping between each file and its corresponding virtual memory region is stored in the accompanying metadata.

## Don’t stop at “LSASS was dumped”

Do not make the mistake of stopping here. Yes, we know the attacker dumped LSASS memory. But was the dump actually usable? And what information could the attacker recover from it? If the attacker attempted to dump LSASS but the resulting data was corrupt, incomplete, or contained no useful credential material, that is one situation. If the dump contains reusable credentials, Kerberos keys, machine-account material, or credentials belonging to privileged users, that is a very different situation.

## Reconstructing the attacker’s LSASS dump

TrickDump includes `create_dump.py`, which takes the metadata and captured memory regions and reconstructs a conventional minidump. Using the files recovered during the investigation:

```
$ python3 create_dump.py \
    -l trick/lock.json \
    -s trick/shock.json \
    -b trick/barrel.json \
    -z trick/trick.zip \
    -o recovered.dmp
```

The script reconstructs the required minidump structures and maps the captured LSASS memory regions back into them.

```
[+] Total number of modules:    137
[+] ModuleListStream size:      24452
[+] Mem64List offset:           24576
[+] Mem64List size:             39744
[+] Dump file recovered.dmp created
```

The TrickDump repository describes exactly this workflow: collect the individual memory regions and metadata on the victim, then run `create_dump.py` on another system to generate the final minidump. We now had a valid LSASS minidump and could parse it with `pypykatz`:

```
$ pypykatz lsa minidump recovered.dmp
```

In our case, the reconstructed dump contained reusable credential material for the affected account; the actual values have been redacted. The excerpt below shows only the corresponding logon-session metadata for one of the affected accounts.

```
FILE: ======== recovered.dmp =======
== LogonSession ==
authentication_id 8495610186 (1fa60b94a)
session_id 0
username prtg
domainname <redacted>
logon_server
logon_time 2026-03-11T03:44:13.286691+00:00
sid S-1-5-21-<redacted>
luid 8495610186
	== Kerberos ==
		Username: prtg
		Domain: <redacted>
[...]
```

## Hunting

TrickDump avoids a conventional LSASS minidump on the victim, but it still has to obtain a handle to lsass.exe, enable `SeDebugPrivilege`, and read virtual memory. Useful starting points:

* `lock.json`, `shock.json`, `barrel.json` together with a ZIP of many randomly named chunks (`barrel.zip` by default; `trick.zip` in our incident), especially in staging directories.
* Unexpected processes obtaining handles to lsass.exe with access rights permitting virtual-memory reads (Sysmon EID 10 / EDR process-access telemetry), if `ProcessAccess` telemetry is configured/collected.
* A sequence of up to three binaries in the same working directory, with Shock and Barrel accessing LSASS in close temporal proximity. Lock only collects operating-system information and may be absent if that information is already known. The all-in-one Trick variant collapses the workflow into a single process.
* Where endpoint telemetry is available, look for `SeDebugPrivilege` enablement followed by extensive LSASS virtual-memory reads and su...