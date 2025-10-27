---
title: Cerbero Suite 6.4 and Cerbero Engine 3.4 are out!
url: https://blog.cerbero.io/?p=2658
source: Cerbero Blog
date: 2023-05-02
fetch_date: 2025-10-04T11:38:37.440012
---

# Cerbero Suite 6.4 and Cerbero Engine 3.4 are out!

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
  + [Resources](https://cerbero.io/resources/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# Cerbero Suite 6.4 and Cerbero Engine 3.4 are out!

We have released Cerbero Suite 6.4 and Cerbero Engine 3.4. What follows is a list of the most important new features.

### Silicon Shellcode Emulator

Silicon Shellcode Emulator is a lightweight x86/x64 emulator designed for Windows shellcode. The package is available to all commercial licenses of Cerbero Suite Advanced.

The emulator can be launched from the main window, from the command line or from an action.

[![](/wp-content/uploads/2023/04/64/sse1.png)](/wp-content/uploads/2023/04/64/sse1.png)

The emulator can be executed from an action within any hex view.

[![](/wp-content/uploads/2023/04/64/sse2.png)](/wp-content/uploads/2023/04/64/sse2.png)

Before the emulator is launched, a settings dialog is shown: an architecture and a memory profile must be selected.

[![](/wp-content/uploads/2023/04/64/sse3.png)](/wp-content/uploads/2023/04/64/sse3.png)

If a memory profile isn’t already available, on Windows you can create a new one from a process on your system. An x86 shellcode requires an x86 process memory profile and an x64 shellcode requires an x64 process memory profile. Make sure that the selected process maps Urlmon.dll, which is often used by shellcode. On Linux and Mac it is necessary to copy a memory profile created on Windows to the profile directory.

Once the profile has been selected, the emulator can be launched.

[![](/wp-content/uploads/2023/04/64/sse4.png)](/wp-content/uploads/2023/04/64/sse4.png)

In this case, we didn’t step through the code manually and just let the emulator run the code. As can be observed in the output view, the emulator simulated the APIs invoked by the shellcode.

In the upcoming weeks we’ll be showcasing Silicon Shellcode Emulator in videos and articles.

### IceDark Theme

To celebrate the release of Silicon Shellcode Emulator we have created a new theme which gives Cerbero Suite a look which might be familiar to old-school fellows.

[![](/wp-content/uploads/2023/04/64/ice.png)](/wp-content/uploads/2023/04/64/ice.png)

### DES Filter

We’ve added the DES crypto filter which supports DES, DEX and 3DES. While the DES algorithm family is no longer recommended for encryption, it can still be found in malware.

[![](/wp-content/uploads/2023/04/64/des.png)](/wp-content/uploads/2023/04/64/des.png)

### ITSF & JPEG module documentation

We have documented the [ITSF module](https://sdk.cerbero.io/latest/Pro.ITSF.html) which provides the API for parsing Microsoft CHM files and the [JPEG module](https://sdk.cerbero.io/latest/Pro.JPEG.html).

[![](/wp-content/uploads/2023/04/64/doc.png)](/wp-content/uploads/2023/04/64/doc.png)

### Improved command line interpreter

We’ve improved the command line interpreter control and workspaces can now add their [own interpreters](https://sdk.cerbero.io/latest/Pro.UI.html#Pro.UI.ProWorkspace.addCommandLineInterpreter).

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [May 1, 2023May 1, 2023](https://blog.cerbero.io/cerbero-suite-6-4-and-cerbero-engine-3-4-are-out/)Categories [Engine](https://blog.cerbero.io/category/engine/), [Suite Advanced](https://blog.cerbero.io/category/suite-advanced/), [Suite Standard](https://blog.cerbero.io/category/suite-standard/)Tags [News](https://blog.cerbero.io/tag/news/)

## Leave a Reply [Cancel reply](/cerbero-suite-6-4-and-cerbero-engine-3-4-are-out/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: URL Extractor Package](https://blog.cerbero.io/url-extractor-package/)

[Next Next post: Video: Silicon Shellcode Emulator Introduction](https://blog.cerbero.io/video-silicon-shellcode-emulator-introduction/)

Search for:

Search

## Recent Posts

* [Memory Challenge 1: Reveal](https://blog.cerbero.io/memory-challenge-1-reveal/)
* [NSIS Format Package](https://blog.cerbero.io/nsis-format-package/)
* [ASAR Format Package](https://blog.cerbero.io/asar-format-package/)
* [InnoSetup Format Package 2.0](https://blog.cerbero.io/innosetup-format-package-2-0/)
* [Cerbero Journal Issue 6](https://blog.cerbero.io/cerbero-journal-issue-6/)
* [Memory Analysis Package 0.5](https://blog.cerbero.io/memory-analysis-package-0-5/)
* [Cerbero Suite 8.5](https://blog.cerbero.io/cerbero-suite-8-5/)
* [Memory Analysis Package 0.4](https://blog.cerbero.io/memory-analysis-package-0-4/)
* [Cerbero Suite 8.4](https://blog.cerbero.io/cerbero-suite-8-4/)
* [WIM Format Package](https://blog.cerbero.io/wim-format-package/)

## Archives

Archives

Select Month
 October 2025  (1)
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
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Resources](https://cerbero.io/resources/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

[Cerbero Blog](https://blog.cerbero.io/)  [Proudly powered by WordPress](https://wordpress.org/)