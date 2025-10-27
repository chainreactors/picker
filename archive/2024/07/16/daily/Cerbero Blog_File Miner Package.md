---
title: File Miner Package
url: https://blog.cerbero.io/file-miner-package/
source: Cerbero Blog
date: 2024-07-16
fetch_date: 2025-10-06T17:42:46.257850
---

# File Miner Package

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

# File Miner Package

We are thrilled to announce the launch of the [File Miner package](https://cerbero.io/packages/fileminer/), a sophisticated file carving tool now available for all Cerbero Suite licenses. Designed to aid malware and forensic analysts in their daily tasks, this package stands out as a top-tier utility in its category, and we plan to enhance it further by supporting additional file formats.

![](/wp-content/uploads/2024/07/fm/logo.png)

File Miner offers flexible configuration through the settings. By default, it automatically carves files selectively from specific groups, such as excluding archives where carving generally provides no benefit. Users have the ability to customize settings to select which file groups are automatically carved and which specific groups or file formats should be detected.

![](/wp-content/uploads/2024/07/fm/settings.png)

Additionally, the carving speed for each file type is prominently displayed, allowing for more informed decisions.

![](/wp-content/uploads/2024/07/fm/speed.png)

Here’s an example of File Miner in action: a malware sample was processed, during which the executable was unpacked using the [UPX Unpacker package](https://cerbero.io/packages/upxunpacker/). File Miner identified four additional executables within the unpacked file.

![](/wp-content/uploads/2024/07/fm/malware.png)

File Miner can be initiated from any hex view as an action.

![](/wp-content/uploads/2024/07/fm/run_action.png)

For instance, we launched it on the data from a memory dump.

![](/wp-content/uploads/2024/07/fm/action.png)

Upon completion of the carving process, File Miner presents a comprehensive view of the extracted files.

![](/wp-content/uploads/2024/07/fm/results.png)

You have the option to access each file individually or save them in batches. When batch-saving, you can opt to add them as child objects, root objects, or save them directly to the disk.

![](/wp-content/uploads/2024/07/fm/children.png)

Once the objects are added, they can be inspected in the same manner as those carved automatically.

![](/wp-content/uploads/2024/07/fm/child.png)

File Miner’s functionality can be enhanced through the integration of additional installed packages. In fact, certain file formats are only detected when their corresponding format packages are installed. For instance, PYC files and RAR archives can be detected and processed only with the relevant packages installed.

The package is exposed to the SDK. The following code snippet demonstrates how to carve files programmatically:

```
from Pro.Core import *
from Pro.UI import *
from Pkg.FileMiner import *

def callback(match, ud):
    print("MATCH:", match.format, "offset:", hex(match.offset), "size:", hex(match.size))

def main():
    c = createContainerFromFile("path/to/file")
    fm = FileMiner()
    wo = proContext().startWait("Carving...")
    fm.mine(c, callback=callback, wait_object=wo)
    wo.stop()
```

As we continue to develop and expand this tool, we remain committed to equipping our users with the most powerful and intuitive resources for their cybersecurity and forensic needs.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [July 15, 2024July 16, 2024](https://blog.cerbero.io/file-miner-package/)Categories [Package](https://blog.cerbero.io/category/package/)Tags [File Carving](https://blog.cerbero.io/tag/file-carving/)

## Leave a Reply [Cancel reply](/file-miner-package/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: .NET Decompiler Package](https://blog.cerbero.io/net-decompiler-package/)

[Next Next post: Cerbero Suite 7.7 Release](https://blog.cerbero.io/cerbero-suite-7-7-release/)

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