---
title: Cerbero Suite 8.1
url: https://blog.cerbero.io/cerbero-suite-8-1/
source: Cerbero Blog
date: 2024-10-24
fetch_date: 2025-10-06T18:50:29.108782
---

# Cerbero Suite 8.1

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

# Cerbero Suite 8.1

We’re excited to release Cerbero Suite 8.1 and Cerbero Engine 5.1!

The main highlight of this release is that we have finally completed the documentation of the SDK. However, there are also some other news which we’ll be discussing in this post.

## SDK Documentation

We have completed the documentation of the [SDK](https://sdk.cerbero.io/), including built-in file formats, installable packages, and external modules.

![](/wp-content/uploads/2024/10/81/doc.png)

This means that the entire SDK is now available for auto-completion in the Python editor. Every time you install a package that is exposed to the SDK, auto-completion becomes available for that package as well.

The SDK of Cerbero Suite and Cerbero Engine is unparalleled in scope and depth, offering a vast array of functionalities for developers. With the documentation, you can easily explore all the capabilities the SDK has to offer. Whether you’re writing plugins to automate tasks, analyzing complex file formats, or creating new tools, the SDK provides the necessary tools and resources.

The integrated Python editor in Cerbero Suite further enhances your development experience by providing features like syntax highlighting, hints and code completion. To get started, simply navigate to the [SDK documentation website](https://sdk.cerbero.io/), where you’ll find extensive guides, API references, and examples. The documentation is organized to help both beginners and advanced users quickly find the information they need.

## UEFI Firmware Images

We have released the [UEFI Firmware Image Format package](https://cerbero.io/packages/uefifirmwareimageformat/) for all licenses of Cerbero Suite!

The package supports a variety of UEFI firmware image formats and, in addition to allowing you to inspect their structure, it automatically extracts embedded files.

![](/wp-content/uploads/2024/10/uefi/image.png)

The package usually identifies the UEFI firmware image format automatically. However, if the format is not automatically recognized, you will need to manually specify it when opening the file.

![](/wp-content/uploads/2024/10/uefi/format.png)

## Windows Link Format SDK

We have exposed the Windows Link (.lnk) format to the [SDK](https://sdk.cerbero.io/Pro.Lnk.html).

Here is an example of how to output the contents of a link file:

```
from Pro.Core import *
from Pro.Lnk import *

def parseLink(fname):
    c = createContainerFromFile(fname)
    if c.isNull():
        return
    obj = LnkObject()
    if not obj.Load(c) or not obj.Initialize():
        return
    out = proTextStream()
    obj.Dump(out)
    print(out.buffer)
```

## Save Child Objects to Disk Action

We have added a very useful action to the context menu of the hierarchy view: the ability to save child objects to disk.

![](/wp-content/uploads/2024/10/81/save_children.png)

This new feature allows you to export all child objects to disk with just a few clicks. To use this feature, simply right-click on a parent object in the hierarchy view and select “Save Children to Disk”. You will then be prompted to choose a destination folder where all the child objects will be saved.

This simplified workflow eliminates the need to manually extract each object individually, saving you time and effort. This feature is particularly useful when you need to process the child objects using external applications.

## Improvements & Bug Fixes

As usual, each release contains improvements and bug fixes, but this release in particular offers a refined user experience, especially on Linux.

We hope you enjoy the new features and improvements in Cerbero Suite 8.1 and Cerbero Engine 5.1. As always, we welcome your feedback and look forward to seeing how you leverage the SDK and new functionalities in your projects.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [October 23, 2024](https://blog.cerbero.io/cerbero-suite-8-1/)Categories [Suite](https://blog.cerbero.io/category/suite/)Tags [News](https://blog.cerbero.io/tag/news/)

## Leave a Reply [Cancel reply](/cerbero-suite-8-1/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: UEFI Firmware Image Format Package](https://blog.cerbero.io/uefi-firmware-image-format-package/)

[Next Next post: Cerbero Suite 8.2](https://blog.cerbero.io/cerbero-suite-8-2/)

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
  + [Cerbero Suite](https://cerbero.io/sui...