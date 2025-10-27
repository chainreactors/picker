---
title: Mark-of-the-Web: Additional Guidance
url: https://textslashplain.com/2022/12/02/mark-of-the-web-additional-guidance/
source: text/plain
date: 2022-12-03
fetch_date: 2025-10-04T00:24:11.822606
---

# Mark-of-the-Web: Additional Guidance

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Mark-of-the-Web: Additional Guidance

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2022-12-022025-03-26](https://textslashplain.com/2022/12/02/mark-of-the-web-additional-guidance/)Posted in[design](https://textslashplain.com/category/design/), [dev](https://textslashplain.com/category/dev/), [security](https://textslashplain.com/category/security/)Tags:[dev](https://textslashplain.com/tag/dev/), [MoTW](https://textslashplain.com/tag/motw/), [security](https://textslashplain.com/tag/security/), [zones](https://textslashplain.com/tag/zones/)

*I’ve been writing about Windows Security Zones and the Mark-of-the-Web (MotW) security primitive in Windows for* decades *now, with 2016’s [Downloads and MoTW](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/) being one of my longer posts that I’ve updated intermittently over the last few years. If you haven’t read that post already, you should start there.*

## Advice for Implementers

At this point, MotW is old enough to vote and almost old enough to drink, yet understanding of the feature remains patchy across the Windows developer ecosystem.

MotW, like most security primitives ([e.g. HTTPS](https://textslashplain.com/2015/06/30/https-only-works-if-you-use-it/)), **only works if you use it**. Specifically, an application which **generates** local files from untrusted data (i.e. anywhere on “The Internet”) must ensure that the files bear a MoTW to ensure that the Windows Shell and other applications recognize the files’ origins and treat them with appropriate caution. Such treatment might include running anti-malware checks, prompting the user before running unsafe executables, or opening the files in Office’s Protected View.

Similarly, if you build an application which **consumes** files, you should carefully consider whether files from untrusted origins should be treated with extra caution in the same way that Microsoft’s key applications behave — locking down or prompting users for permission before the file initiates any potentially-unwanted actions, more-tightly sandboxing parsers, etc.

### Writing MotW

The best way to write a Mark-of-the-Web to a file is to let Windows do it for you, using the `[IAttachmentExecute::Save()](https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nf-shobjidl_core-iattachmentexecute-save)` API. Using the Attachment Execution Services API ensures that the MotW is written (or not) based on the client’s configuration. Using the API also provides future-proofing for changes to the MotW format (e.g. Win10 started preserving the original URL information rather than just the ZoneID).

If the URL is not known, but you wish to ensure Internet Zone handling, use the special url **`[about:internet](https://source.chromium.org/chromium/chromium/src/%2B/main%3Acomponents/services/quarantine/quarantine_win.cc;l=126;drc=8ba1bad80dc22235693a0dd41fe55c0fd2dbdabd)`**.

You should also use `about:internet` if the URL is longer than 2083 characters ([`INTERNET_MAX_URL_LENGTH`](https://source.chromium.org/chromium/chromium/src/%2B/main%3Avs_files/1023ce2e82/Windows%20Kits/10/Include/10.0.20348.0/um/wininet.h;drc=2df668b7cbf6c1d0766b6ee0ae8147adc8830f2e;bpv=1;bpt=1;l=99?gsn=INTERNET_MAX_URL_LENGTH&gs=kythe%3A%2F%2Fchromium.googlesource.com%2Fchromium%2Fsrc%3Flang%3Dc%252B%252B%3Fpath%3Dvs_files%2F1023ce2e82%2FWindows%2520Kits%2F10%2FInclude%2F10.0.20348.0%2Fum%2Fwininet.h%3Froot%3Dthird_party%2Fdepot_tools%2Fwin_toolchain%23INTERNET_MAX_URL_LENGTH%2523m%25402569)), or if the URL’s scheme isn’t one of `HTTP`/`HTTPS`/`FILE`.

Ensure that you write the MotW to any untrusted file written to disk, regardless of how that happened. For example, one mail client would properly write MotW when the user used the “Save” command on an attachment, but failed to do so if the user drag/dropped the attachment to their desktop. Similarly, browsers have written MotW to “downloads” for decades, but needed to add similar marking when the [File Access API](https://developer.mozilla.org/en-US/docs/Web/API/window/showSaveFilePicker) was introduced.

Take care with anything that would prevent proper writing of the MotW– for example, if you build a decompression utility for ZIP files, ensure that you write the MotW *before* your utility applies any `readonly` bit to the newly extracted file, otherwise the tagging [will fail](https://twitter.com/wdormann/status/1590044005395357697).

#### Beware Race Conditions

In certain (rare) scenarios, there’s the risk of a race condition whereby a client could consume a file before your code has had the chance to tag it with the Mark-of-the-Web, resulting in a security vulnerability. For instance, consider the case where your app (1) downloads a file from the internet, (2) streams the bytes to disk, (3) closes the file, finally (4) calls `IAttachmentExecute::Save()` to let the system tag the file with the MotW. If an attacker can induce the handler for the new file to load it *between* steps #3 and #4, the file could be loaded by a victim application *before* the MotW is applied.

Unfortunately, there’s not generally a great way to prevent this — for example, the `Save()` call can perform operations that depend on the file’s name and content (e.g. an antivirus scan) so we can’t simply call the API against an empty file or against a bogus temporary filename (i.e. `inprogress.temp`).

The best approach I can think of is to avoid exposing the file in a predictable location *until* the MotW marking is complete. For example, you could download the file into a randomly-named temporary folder (e.g. `%TEMP%\InProgress\{guid}\setup.exe`), call the `Save()` method on that file, then move the file to the predictable location.

*Note: This approach (extracting to a randomly-named temporary folder, carefully named to avoid 8.3 filename collisions that would reduce entropy) is now used by Windows 10+’s ZIP extraction code.*

### Correct Zone Mapping

**To check the Zone for a file path or URL, use the [MapUrlToZone](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537133%28v%3Dvs.85%29) (sometimes called `MUTZ`) function in `URLMon.dll`. You should not try to implement this function yourself– you will get burned.**

Because the MotW is *typically* stored as a simple key-value pair within a NTFS alternate data stream:

[![](https://textslashplain.com/wp-content/uploads/2022/12/image-1.png?w=766)](https://textslashplain.com/wp-content/uploads/2022/12/image-1.png)

…it’s *tempting* to think “*To determine a file’s zone, my code can just read the `ZoneId` directly*.”

Unfortunately, doing so is a recipe for failure.

Firstly, consider the simple corner cases you might miss. For instance, if you try to open with read/write permissions the `Zone.Identifier` stream of a file whose readonly bit is set, the attempt to open the stream will fail because the file isn’t writable.

***Aside******:** A 2023-era vulnerability in Windows was caused by failure to open the Zone.Identifier due to an unnecessary demand for write permission.*

Second, there’s a ton of subtlety in performing a proper zone mapping.

2a: For example, files stored under certain paths or with certain Integrity Levels are treated as Internet Zone, even without a `Zone.Identifier` stream:

[![](https://textslashplain.com/wp-content/uploads/2022/12/image-2.png?w=1024)](https://textslashplain.com/wp-content/uploads/2022/12/image-2.png)

2b: Similarly, files accessed via a `\\UNC` share are implicitly *not* in the Local Machine Zone, even if they don’t have a `Zone.Identifier` stream.

***Aside******:** The February 2024 security patch ([CVE-2024-21412](https://www.trendmicro.com/en_us/research/24/b/cve202421412-water-hydra-targets-traders-with-windows-defender-s.html)) fixed a vulnerability ...