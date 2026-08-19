---
title: Cerbero Suite 9 Release
url: https://blog.cerbero.io/cerbero-suite-9-release/
source: Cerbero Blog
date: 2026-08-18
fetch_date: 2026-08-19T02:56:18.186902
---

# Cerbero Suite 9 Release

[Skip to content](#content)

[Cerbero Blog](https://blog.cerbero.io/)

Menu

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# Cerbero Suite 9 Release

We are excited to announce the release of Cerbero Suite 9! All our customers with a valid license can now upgrade directly within the application. What follows are the most relevant new features.

### Cerbero Shell

One of the main new features of this release is Cerbero Shell, a small command language designed for binary analysis. It powers the new shell view, is available in the analysis workspace as well as in other workspaces, can be run from the terminal with the `cshell` tool, and can be embedded by plugins through the [Pro.Shell module](https://sdk.cerbero.io/Pro.Shell.html).

At its simplest, the shell is a calculator that speaks the language of reverse engineering: integers are always displayed in both decimal and hexadecimal, while bitwise operations, bytes, and encodings are first-class citizens.

```
> 0x401000 + 0x1a2b0
4305584 (0x41b2b0)
> (1 << 20) - 1
1048575 (0xfffff)
> b64dec("TVqQ")
b"MZ\x90"
```

When a file is being analyzed, the shell exposes function domains for inspecting it: PE, .NET, ELF and Mach-O structures, strings, disassembly, and much more. Results are values, so they can be filtered with ‘grep’ and chained with the pipe operator. For instance, to check whether an executable imports `GetProcAddress`:

```
> pe.imports -> grep "getproc"
[0]:
  dll: "KERNEL32.dll"
  functions:
    [0]:
      name: "GetProcAddress"
```

The same style works everywhere: `strings.filter rx.email rx:true` keeps only strings that look like email addresses, `dotnet.disasm(token) -> print` prints the disassembly of a .NET method, and appending `?` to any function name shows its documentation.

The language is intentionally not Python: it never executes arbitrary code, every function is read-only, and mutating operations require explicit consent. This makes the shell safe to expose even to automated agents. Plugins [can extend it](https://sdk.cerbero.io/Pro.Shell.html) with their own functions.

The complete guide to the language is available in our [SDK documentation](https://sdk.cerbero.io/Shell.html).

Currently, only built-in file formats are exposed to Cerbero Shell. We’re in the process of exposing all applicable optional packages as well.

### Filter Line Options

All filter lines now have options available, such as case sensitivity, whole-word matching, and regular expressions. Additionally, we provide a set of common regular expression search patterns for convenience.

![](/wp-content/uploads/2026/08/v9/foptions.png)

In this CTF memory challenge, we filtered by email, which gave us one of the flags.

![](/wp-content/uploads/2026/08/v9/filter.png)

### File Search

File system views now support file search.

![](/wp-content/uploads/2026/08/v9/filesearch.png)

This is convenient when you need to search for specific file names within a file system.

### System Settings

We have improved the system settings, and it is now possible to register context menu associations on Linux and macOS as well.

![](/wp-content/uploads/2026/08/v9/system.png)

Additionally, plugins can register their own file associations.

### Proxy Settings

We have introduced proxy settings for organizations that need to route their network traffic through a proxy.

![](/wp-content/uploads/2026/08/v9/proxy.png)

### Miscellaneous

\* Scan performance has been improved, especially for file types such as Portable Executable that use file ranges to detect foreign data.
\* XML parsing has been greatly improved to handle malformed samples even better.
\* The SDK has been expanded considerably.
\* Packing filters have been added.
\* Many bug fixes and improvements.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [August 18, 2026](https://blog.cerbero.io/cerbero-suite-9-release/)Categories [Suite](https://blog.cerbero.io/category/suite/)Tags [News](https://blog.cerbero.io/tag/news/)

## Leave a Reply [Cancel reply](/cerbero-suite-9-release/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

[ ]  Notify me of follow-up comments by email.

[ ]  Notify me of new posts by email.

## Post navigation

[Previous Previous post: CPIO Format Package](https://blog.cerbero.io/cpio-format-package/)

Search for:

Search

## Recent Posts

* [Cerbero Suite 9 Release](https://blog.cerbero.io/cerbero-suite-9-release/)
* [CPIO Format Package](https://blog.cerbero.io/cpio-format-package/)
* [FDT Format Package](https://blog.cerbero.io/fdt-format-package/)
* [LittleFS Format Package](https://blog.cerbero.io/littlefs-format-package/)
* [CDEX Format Package](https://blog.cerbero.io/cdex-format-package/)
* [VDEX Format Package](https://blog.cerbero.io/vdex-format-package/)
* [SPIFFS Format Package](https://blog.cerbero.io/spiffs-format-package/)
* [WASM Format & Decompiler Packages](https://blog.cerbero.io/wasm-format-decompiler-packages/)
* [F2FS Format Package](https://blog.cerbero.io/f2fs-format-package/)
* [DotNETBinaryFormatter Format Package](https://blog.cerbero.io/dotnetbinaryformatter-format-package/)

## Archives

Archives

Select Month
 August 2026  (1)
 June 2026  (1)
 May 2026  (8)
 April 2026  (13)
 March 2026  (3)
 February 2026  (3)
 January 2026  (2)
 December 2025  (6)
 November 2025  (8)
 October 2025  (9)
 September 2025  (2)
 August 2025  (2)
 July 2025  (2)
 June 2025  (3)
 May 2025  (7)
 April 2025  (4)
 March 2025  (2)
 October 2024  (3)
 September 2024  (1)
 August 2024  (3)
 July 2024  (5)
 June 2024  (2)
 April 2024  (4)
 March 2024  (1)
 February 2024  (1)
 January 2024  (4)
 December 2023  (3)
 November 2023  (7)
 October 2023  (3)
 September 2023  (1)
 July 2023  (1)
 May 2023  (11)
 March 2023  (9)
 February 2023  (3)
 January 2023  (1)
 November 2022  (1)
 September 2022  (2)
 August 2022  (2)
 July 2022  (3)
 June 2022  (2)
 May 2022  (5)
 April 2022  (3)
 March 2022  (4)
 February 2022  (6)
 January 2022  (1)
 November 2021  (4)
 October 2021  (5)
 September 2021  (7)
 June 2021  (1)
 April 2021  (1)
 March 2021  (4)
 February 2021  (1)
 December 2020  (1)
 November 2020  (1)
 October 2020  (1)
 September 2020  (2)
 July 2020  (2)
 January 2020  (1)
 September 2019  (1)
 August 2019  (2)
 July 2019  (1)
 June 2019  (1)
 May 2019  (3)
 April 2019  (2)
 June 2018  (1)
 April 2018  (1)
 March 2018  (1)
 January 2018  (1)
 November 2017  (2)
 March 2017  (5)
 July 2016  (2)
 May 2016  (2)
 April 2016  (1)
 October 2015  (2)
 September 2015  (2)
 June 2015  (2)
 December 2014  (2)
 October 2014  (1)
 September 2014  (3)
 August 2014  (1)
 July 2014  (1)
 December 2013  (2)
 November 2013  (5)
 October 2013  (5)
 September 2013  (6)
 August 2013  (6)
 July 2013  (1)
 June 2013  (4)
 May 2013  (7)
 April 2013  (5)
 March 2013  (3)
 February 2013  (4)
 January 2013  (3)
 December 2012  (3)
 November 2012  (5)
 October 2012  (3)
 September 2012  (1)
 August 2012  (2)
 July 2012  (2)
 June 2012  (2)
 May 2012  (2)
 April 2012  (1)
 March 2012  (6)
 February 2012  (5)
 January 2012  (8)
 November 2011  (1)
 August 2011  (1)

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engin...