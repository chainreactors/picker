---
title: Windows 11 quietly introduced a new execution artifact investigators should start checking
url: https://andreafortuna.org/2026/03/19/windows11-pca-artifact.html
source: Instapaper: Unread
date: 2026-03-23
fetch_date: 2026-03-24T04:18:07.085722
---

# Windows 11 quietly introduced a new execution artifact investigators should start checking

[Andrea Fortuna](/)
[ ]

[About](/about/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Windows 11 quietly introduced a new execution artifact investigators should start checking

Mar 19, 2026

Digital forensics often rewards people who look in places nobody else is checking yet.

![cover](/assets/2026/pca-artifact.png)

That is exactly why a small and almost invisible Windows 11 artifact deserves more attention than it is getting today. Starting with Windows 11 (22H2+), Microsoft introduced a plain text execution trace tied to the [Program Compatibility Assistant](https://www.sygnia.co/blog/new-windows-11-pca-artifact/) service, and it can be surprisingly useful during an investigation.

The location is:

```
C:\Windows\appcompat\pca\PcaAppLaunchDic.txt
```

Inside that directory, investigators may find text files that record programs launched through Explorer, including the full executable path and a UTC timestamp. No proprietary parser is required. No obscure binary structure needs to be decoded first. In many cases, the evidence is simply sitting there in readable text.

That alone should make DFIR analysts, incident responders, and threat hunters pay attention.

## Why this artifact matters

Most Windows investigations still revolve around the usual execution artifacts: Prefetch, Amcache, Shimcache, UserAssist, SRUM, Jump Lists, and event logs. Those sources remain valuable, of course, but they all come with caveats. Some are disabled in certain environments. Some are noisy. Some require careful interpretation. Some are easy to misunderstand if taken in isolation.

What makes the PCA launch dictionary interesting is not that it replaces those artifacts. It does not. What makes it interesting is that it adds a fresh and highly readable layer of evidence that [many analysts are not yet including in their workflow](https://aboutdfir.com/new-windows-11-pro-22h2-evidence-of-execution-artifact/). If an attacker, insider, or end user launched a program by double-clicking it in Explorer, there is a chance this artifact captured that action with enough detail to become immediately useful. That includes binaries executed from local folders, removable media, and even network shares.

From an investigative perspective, that creates several opportunities. First, it can help answer a very simple but very important question: was this executable actually launched on this system? Second, it can help connect an alert to user activity. Suppose EDR telemetry flags a suspicious binary in `C:\Temp`, or a malicious file downloaded to the Desktop disappears before triage begins. If it was launched through Explorer, this artifact may still preserve the path and time of execution even after the file itself has been deleted. Third, it gives responders another way to validate or challenge a timeline. In real cases, confidence often comes from correlation, not from a single log entry.

## What Windows is doing behind the scenes

The artifact is linked to the Program Compatibility Assistant service, also known as `PcaSvc`. This service has existed since the Windows Vista era and was originally designed to monitor launched applications, detect compatibility issues, and suggest fixes when older software behaved badly on newer Windows versions. With Windows 11 (22H2+), Microsoft added a more persistent text-based tracking mechanism to support that process.

In other words, this was not created for digital forensics. It was created for system functionality. But as often happens in incident response, an operating system feature built for one purpose ends up becoming valuable evidence for another. That is also why this artifact may remain underused for a while. Many analysts focus on the evidence sources they already know well, and new ones tend to spread slowly across the [DFIR community](https://github.com/Psmths/windows-forensic-artifacts/blob/main/execution/program-compatibility-assistant.md). Until a source is documented in popular cheat sheets, supported by mainstream tools, and discussed in conference talks, it often stays in the blind spot.

## Reading the artifact

The file format is plain text, encoded in UTF-16 LE, with one entry per line. Each line contains the full executable path followed by a pipe-separated UTC timestamp. Here is what a raw entry looks like:

```
C:\Users\Alice\Downloads\Quarterly_Review.pdf.exe|2026-03-15 09:42:11.000
C:\Temp\tool.exe|2026-03-15 09:43:05.000
D:\AUTORUN\payload.exe|2026-03-15 09:44:22.000
```

The third entry above is particularly interesting: `D:\` is a removable drive. The artifact records the full path at the time of execution, which means USB-based delivery is immediately visible from the path prefix alone.

### Quick triage with PowerShell

During live response or remote triage, you can read and display the file content directly with PowerShell. Because the file is UTF-16 LE encoded, a standard `Get-Content` call needs the correct encoding parameter:

```
Get-Content -Path "C:\Windows\appcompat\pca\PcaAppLaunchDic.txt" -Encoding Unicode
```

To filter for entries containing suspicious paths like `C:\Temp`, `Downloads`, or `AppData`, you can pipe into `Select-String`:

```
Get-Content -Path "C:\Windows\appcompat\pca\PcaAppLaunchDic.txt" -Encoding Unicode |
  Select-String -Pattern "Temp|Downloads|AppData|\\Users\\"
```

### Collecting the file during triage

For offline or image-based analysis, grab the file before acquisition or use it as part of a targeted collection. A simple copy via cmd works:

```
copy "C:\Windows\appcompat\pca\PcaAppLaunchDic.txt" %USERPROFILE%\Desktop\PcaAppLaunchDic.txt
```

For KAPE users, the artifact is available in the `!SANS_Triage` target collection or can be added manually. The [Eric Zimmerman KAPE](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape) target path to include is:

```
C:\Windows\appcompat\pca\PcaAppLaunchDic.txt
C:\Windows\appcompat\pca\PcaGeneralDb0.txt
C:\Windows\appcompat\pca\PcaGeneralDb1.txt
```

Note that the `PcaGeneralDb` files alternate as active logs and contain additional detail about compatibility errors and application exits, making them a useful companion to `PcaAppLaunchDic.txt`.

### Parsing with Python

If you want to automate parsing across multiple endpoints or integrate this artifact into a larger pipeline, here is a minimal Python snippet that reads the file, splits each line on the pipe separator, and outputs structured results:

```
import sys

def parse_pca(filepath):
    results = []
    with open(filepath, encoding="utf-16-le", errors="replace") as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                path, timestamp = line.rsplit("|", 1)
                results.append({"path": path.strip(), "timestamp": timestamp.strip()})
    return results

if __name__ == "__main__":
    entries = parse_pca(sys.argv[1])
    for e in entries:
        print(f"[{e['timestamp']}] {e['path']}")
```

Run it as:

```
python3 parse_pca.py PcaAppLaunchDic.txt
```

For a more robust implementation with timeline output and CSV export, Harlan Carvey published [PCAParse](https://windowsir.blogspot.com/2024/02/pcaparse.html), a dedicated Perl-based parser that converts timestamps to Unix epoch format and supports batch processing.

## What kind of activity it can reveal

The strongest use case is straightforward: a user opens Explorer, browses to a file, and launches an executable by double-clicking it. That covers a lot of real-world intrusion activity. Think about how many malicious payloads are still executed through social engineering. A user receives a ZIP archive, extracts it, and opens a fake invoice from the Downloads folder. An operator drops a tool into `C:\Temp` during hands-on-keyboard activity and launches it manually. A technician runs a utility from a USB drive. A user opens a r...