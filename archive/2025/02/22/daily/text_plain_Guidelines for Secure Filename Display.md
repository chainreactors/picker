---
title: Guidelines for Secure Filename Display
url: https://textslashplain.com/2025/02/21/guidelines-for-secure-filename-display/
source: text/plain
date: 2025-02-22
fetch_date: 2025-10-06T20:36:48.020759
---

# Guidelines for Secure Filename Display

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Guidelines for Secure Filename Display

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-02-212025-03-10](https://textslashplain.com/2025/02/21/guidelines-for-secure-filename-display/)Posted in[dev](https://textslashplain.com/category/dev/), [security](https://textslashplain.com/category/security/), [web](https://textslashplain.com/category/tech/web/)Tags:[security](https://textslashplain.com/tag/security/)

Many years ago, I [wrote](https://textslashplain.com/2019/01/11/securely-displaying-urls/) the first drafts of Chromium’s [Guidelines for Secure URL Display](https://chromium.googlesource.com/chromium/src/%2B/master/docs/security/url_display_guidelines/url_display_guidelines.md). These guidelines were designed to help feature teams avoid security bugs whereby a user might misinterpret a URL when making a security decision.

From a security standpoint, **URLs are tricky** because they consist of a mix of security-critical information (the `[Origin](https://learn.microsoft.com/en-us/archive/blogs/ieinternals/same-origin-policy-part-0-origins)`) and attacker-chosen content (the rest of the URL). Additionally, while URLs are conceptually simple, there are many [uncommon and complicated features](https://textslashplain.com/2023/03/22/attack-techniques-spoofing-via-userinfo/) that lead to misunderstandings. In many cases, the best approach for safely-rendering a URL is to instead render its Origin, the most security-sensitive component and the one best protected against spoofing.

The challenge of securely displaying **filenames** is *similar*, but not *identical*. A filename consists of two components of varying levels of trustworthiness:

[![](https://textslashplain.com/wp-content/uploads/2024/10/image-1.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/10/image-1.png)

The (red) attacker-chosen “**base name**” is entirely untrustworthy. However, the (green) file type-declaring **extension** at the end of the string is security-critical on many platforms because [it determines how the file will be handled](https://textslashplain.com/2023/04/05/file-types/#:~:text=that%20information%20somewhere.-,File%20Extensions,-Finally%2C%20we%20come).

In most cases when opening a file, the file’s extension is parsed and interpreted by the operating system’s shell, meaning that the OS will correctly choose the handler for a given file, no matter what spoofing tricks an attacker may use.

As a part of this file-invocation process, the OS will correctly apply security policy based on the type of the file (e.g. [showing a pre-execution warning](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/) for executables and no warning before sending a text file to notepad). If attacker sends a dangerous file (e.g. a malicious executable) with an incorrect extension, the result is typically harmless, for example, showing the code as text inside Notepad:

[![](https://textslashplain.com/wp-content/uploads/2025/02/image-9.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/02/image-9.png)

So, if the OS behaves correctly based on a filename’s *actual* extension, is there any meaningful spoofing threat at all?

Yes. There are two important threats:

1. Not all dangerous file types are known by the system
2. Systems will typically allow a user to run/open potentially unsafe files if they first accept a security prompt

### Problem #1: Not All Dangerous Types are marked as such

Windows contains a built-in list of potentially-dangerous file type extensions, but third-party handler software can introduce support for new extensions (e.g. Python or Perl) without [properly indicating to Windows](https://textslashplain.com/2024/12/12/mark-of-the-web-real-world-protection/#:~:text=and%20adding%20the-,FTA_AlwaysUnsafe,-flag) that files of that type may be dangerous. As such, the OS will allow the user to invoke files of that type from untrusted sources without warning.

If the user installs a handler for one of these dangerous types, the burden is on the user to avoid invoking a file of that type if they do not trust the file.

However, a spoofing vulnerability that obscures the file’s true type could trick a user into (for example) running a Python script when they thought they were going to open a text file.

### Problem #2: Security Prompts

One protection against malicious files is the *user recognizing that a file is potentially dangerous* before they copy or download it to their computer from an untrusted location. A spoofing attack could trick the user into failing to recognize a potentially-dangerous file (e.g. a `.hta` file) when a safe file (e.g. a `.html` file) is expected:

Similarly, another protection against malicious files is the OS warning shown before executing a potentially dangerous file. This warning might be the SmartScreen Application Reputation warning:

[![](https://textslashplain.com/wp-content/uploads/2025/02/image-10.png?w=667)](https://textslashplain.com/wp-content/uploads/2025/02/image-10.png)

…or the decades-old Attachment Execution Services warning:

[![](https://textslashplain.com/wp-content/uploads/2025/02/image-11.png?w=873)](https://textslashplain.com/wp-content/uploads/2025/02/image-11.png)

A spoofing attack against these security UIs could render them ineffective: a user who clicks “Run anyway” or “Open” based on spoofed information would be compromised.

### Attacks

In most cases, an attacker has significant latitude when choosing the base filename and thus can execute any of many attacks:

* An overlong filename might cause UI truncation, such that the user cannot even see the real extension.
* A filename containing many embedded whitespaces (spaces, tabs, or any of dozens of Unicode characters) might push the extension so far away from the start of the filename that it’s either truncated or the user simply doesn’t see it.

[![](https://textslashplain.com/wp-content/uploads/2025/02/image-15.png?w=850)](https://textslashplain.com/wp-content/uploads/2025/02/image-15.png)

* A filename containing a Unicode right-to-left override character might display with the extension in the middle. For example:

[![](https://textslashplain.com/wp-content/uploads/2025/02/image-14.png?w=757)](https://textslashplain.com/wp-content/uploads/2025/02/image-14.png)

In HTML, this could render as `This is safe and not an exe.txt` because the RTL-override character has reversed the text direction in the middle of the string.

* A filename of `Pic.gif from Download.com` might be mistaken as a GIF from Download.com, when it’s really a `.com` executable from elsewhere.

[![](https://textslashplain.com/wp-content/uploads/2025/02/image-16.png?w=450)](https://textslashplain.com/wp-content/uploads/2025/02/image-16.png)

Prompt to save a file with a confusing name (“Pic.gif from download.com”); the user thinks it’s an image, but it’s an executable of type [COM](https://en.wikipedia.org/wiki/COM_file).

#### Some notes on Filename Limits

In many scenarios, filenames are limited to `MAX_PATH`, or 260 characters. While Windows can be [configured to increase MAX\_PATH to ~32k](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later) and apps manifested to declare their support, this feature is not broadly used and thus attackers cannot rely upon its availability.

Characters with special meaning in the filesystem, specifically, **`\/:*?"<>|`** are not allowed to appear in names. There’s also small list of filenames that are prohibited on Windows to avoid overlapping with device names (e.g. [`con,lpt1`, etc](https://source.chromium.org/chromium/chromium/src/%2B/main%3Anet/base/filename_util.cc;l=189;drc=83e81bc2b5215791ff089dabef990a52266dfba3)).

At the low-level the...