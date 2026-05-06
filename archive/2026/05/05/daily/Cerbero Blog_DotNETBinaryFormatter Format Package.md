---
title: DotNETBinaryFormatter Format Package
url: https://blog.cerbero.io/dotnetbinaryformatter-format-package/
source: Cerbero Blog
date: 2026-05-05
fetch_date: 2026-05-06T05:09:12.409588
---

# DotNETBinaryFormatter Format Package

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

# DotNETBinaryFormatter Format Package

We are happy to announce support for the .NET BinaryFormatter serialization format. The new DotNET BinaryFormatter Format package replaces the old decoder with a full parser, providing reliable parsing and embedded object detection for malware analysis and forensic investigations.

![](/wp-content/uploads/2026/04/dotnetbinfmt.png)

BinaryFormatter (`System.Runtime.Serialization.Formatters.Binary.BinaryFormatter`) is a .NET binary serialization mechanism that has been widely used since the early days of .NET. It is also notoriously insecure: deserialization of untrusted data can lead to arbitrary code execution, which has made it a favored vector for .NET exploitation payloads. Malware authors frequently embed executables, shellcode, and configuration data inside BinaryFormatter byte arrays. Having native support in Cerbero Suite means analysts can safely inspect these payloads, navigate the serialized object graph, and extract embedded objects without risking code execution.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [May 5, 2026](https://blog.cerbero.io/dotnetbinaryformatter-format-package/)Categories [Package](https://blog.cerbero.io/category/package/)Tags [.NET](https://blog.cerbero.io/tag/net/)

## Leave a Reply [Cancel reply](/dotnetbinaryformatter-format-package/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: EROFS Format Package](https://blog.cerbero.io/erofs-format-package/)

Search for:

Search

## Recent Posts

* [DotNETBinaryFormatter Format Package](https://blog.cerbero.io/dotnetbinaryformatter-format-package/)
* [EROFS Format Package](https://blog.cerbero.io/erofs-format-package/)
* [ROMFS Format Package](https://blog.cerbero.io/romfs-format-package/)
* [CRAMFS Format Package](https://blog.cerbero.io/cramfs-format-package/)
* [VBA Beautifier Package](https://blog.cerbero.io/vba-beautifier-package/)
* [YAFFS Format Package](https://blog.cerbero.io/yaffs-format-package/)
* [Lua Decompiler Package](https://blog.cerbero.io/lua-decompiler-package/)
* [LUAC Format Package](https://blog.cerbero.io/luac-format-package/)
* [JFFS2 Format Package](https://blog.cerbero.io/jffs2-format-package/)
* [DMG Format Package](https://blog.cerbero.io/dmg-format-package/)

## Archives

Archives

Select Month
 May 2026  (1)
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

[Cerbero Blog](https://blog.cerbero.io/)  [Proudly powered by WordPress](https://wordpress.org/)