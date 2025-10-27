---
title: ISO Format Package
url: https://blog.cerbero.io/?p=2673
source: Cerbero Blog
date: 2023-05-04
fetch_date: 2025-10-04T11:39:13.766697
---

# ISO Format Package

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

# ISO Format Package

We have released the “ISO Format” package for all licenses of Cerbero Suite Standard and Advanced.

[![](/wp-content/uploads/2023/05/iso.png)](/wp-content/uploads/2023/05/iso.png)

The ISO Format package is exposed to the SDK:

```
from Pro.Core import *
from Pkg.ISO import *

def parseISO(fname):
    c = createContainerFromFile(fname)
    if c.isNull():
        return
    obj = ISOObject()
    if not obj.Load(c) or not obj.Initialize():
        return
    for dir_name, dir_entries, file_entries in obj.Walk("/"):
        print(dir_name)
        if dir_entries:
            print("    directories:")
            for entry in dir_entries:
                print("       ", str(entry))
        if file_entries:
            print("    files:")
            for entry in file_entries:
                print("       ", str(entry))
```

An entry can be also retrieved by name:

```
entry = obj.GetEntry(name)
```

And its data can be retrieve either by the entry instance or by name:

```
data = obj.GetEntryData(entry)
# or
data = obj.GetEntryData(name)
```

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [May 3, 2023May 2, 2023](https://blog.cerbero.io/iso-format-package/)Categories [Package](https://blog.cerbero.io/category/package/)Tags [File System](https://blog.cerbero.io/tag/file-system/), [Format](https://blog.cerbero.io/tag/format/), [FS](https://blog.cerbero.io/tag/fs/)

## Leave a Reply [Cancel reply](/iso-format-package/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: Video: Silicon Shellcode Emulator Introduction](https://blog.cerbero.io/video-silicon-shellcode-emulator-introduction/)

[Next Next post: OneNote Malware With ISO File](https://blog.cerbero.io/onenote-malware-with-iso-file/)

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