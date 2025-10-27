---
title: 各种类型文件头部特征
url: https://buaq.net/go-164985.html
source: unSafe.sh - 不安全
date: 2023-05-22
fetch_date: 2025-10-04T11:36:53.803479
---

# 各种类型文件头部特征

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

各种类型文件头部特征

从 Ultra－edit-32 中提取出来的FileTypeExtensionsHeaderJPEGjpgFFD8FFP
*2023-5-21 22:31:59
Author: [blog.upx8.com(查看原文)](/jump-164985.htm)
阅读量:46
收藏*

---

## 从 Ultra－edit-32 中提取出来的

| File | Type | ExtensionsHeader |
| --- | --- | --- |
| JPEG | jpg | FFD8FF |
| PNG | png | 89504E47 |
| GIF | gif | 47494638 |
| TIFF | tif | 49492A00 |
| Windows Bitmap | bmp | 424D |
| CAD | dwg | 41433130 |
| Adobe Photoshop | psd | 38425053 |
| Rich Text Format | rtf | 7B5C727466 |
| XML | xml | 3C3F786D6C |
| HTML | html | 68746D6C3E |
| Email [thorough only] | eml | 44656C69766572792D646174653A |
| Outlook Express | dbx | CFAD12FEC5FD746F |
| Outlook | pst | 2142444E |
| MS Word/Excel | xls.or.doc | D0CF11E0 |
| MS Access | mdb | 5374616E64617264204A |
| WordPerfect | wpd | FF575043 |
| Postscript | eps.or.ps | 252150532D41646F6265 |
| Adobe Acrobat | pdf | 255044462D312E |
| Quicken | qdf | AC9EBD8F |
| Windows Password | pwl | E3828596 |
| ZIP Archive | zip | 504B0304 |
| RAR Archive | rar | 52617221 |
| Wave | wav | 57415645 |
| AVI | avi | 41564920 |
| Real Audio | ram | 2E7261FD |
| Real Media | rm | 2E524D46 |
| MPEG | mpg | 000001BA |
| MPEG | mpg | 000001B3 |
| Quicktime | mov | 6D6F6F76 |
| Windows Media | asf | 3026B2758E66CF11 |
| MIDI | mid | 4D546864 |

## 从 winhex 中取出的文件头列表

| File | Type | ExtensionsHeader |
| --- | --- | --- |
| JPEG | jpg;jpeg | 0xFFD8FF |
| PNG | png | 0x89504E470D0A1A0A |
| GIF | gif | GIF8 |
| TIFF | tif;tiff | 0x49492A00 |
| TIFF | tif;tiff | 0x4D4D002A |
| Bit map | bmp | BM |
| AOL ART | art | 0x4A47040E000000 |
| AOL ART | art | 0x4A47030E000000 |
| PC Paintbrush | pcx | 0x0A050108 |
| Graphics Metafile | wmf | 0xD7CDC69A |
| Graphics Metafile | wmf | 0x01000900 |
| Graphics Metafile | wmf | 0x02000900 |
| Enhanced Metafile | emf | 0x0100000058000000 |
| Corel Draw | cdr | CDR |
| CAD | dwg | 0x41433130 |
| Adobe Photoshop | psd | 8BPS |
| Rich Text Format | rtf | rtf |
| XML | xml |  |
| HTML | html;htm;php;php3;php4;phtml;shtml | type |
| Email | eml | Delivery-date: |
| Outlook Express | dbx | 0xCFAD12FE |
| MS Office/OLE2 | doc;xls;dot;ppt;xla;ppa;pps;pot;msi;sdw;db | 0xD0CF11E0A1B11AE1 |
| MS Access | mdb;mda;mde;mdt | Standard J |
| WordPerfect | wpd | 0xFF575043 |
| OpenOffice Writer | sxw | writer |
| OpenOffice Calc | sxc | calc |
| OpenOffice Math | sxm | math |
| OpenOffice Impress | sxi | impress |
| OpenOffice Draw | sxd | draw |
| Adobe FrameMaker | fm |  |
| PostScript | eps.or.ps;ps;eps | %!PS-Adobe |
| Adobe Acrobat | pdf | %PDF-1. |
| Quicken | qdf | 0xAC9EBD8F |
| QuickBooks Backup | qbb | 0x458600000600 |
| Sage | sly.or.srt.or.slt;sly;srt;slt | 0x53520100 |
| Sage Backup | 1 | SAGEBACKUP |
| Lotus WordPro v9 | lwp | 0x576F726450726F |
| Lotus 123 v9 | 123 | 0x00001A00051004 |
| Lotus 123 v5 | wk4 | 0x00001A0002100400 |
| Lotus 123 v3 | wk3 | 0x00001A0000100400 |
| Lotus 123 v1 | wk1 | 0x2000604060 |
| Windows Password | pwl | 0xE3828596 |
| ZIP Archive | zip;jar | 0x504B0304 |
| ZIP Archive (outdated) | zip | 0x504B3030 |
| RAR Archive | rar | Rar! |
| GZ Archive | gz;tgz | 0x1F8B08 |
| BZIP Archive | bz2 | BZh |
| ARJ Archive | arj | 0x60EA |
| 7－ZIP Archive | 7z | 7z 集 |
| Wave | wav | WAVE |
| AVI | avi | AVI |
| Real Audio | ram;ra | .ra?0 |
| Real Media | rm | .RMF |
| MPEG | mpg;mpeg | 0x000001BA |
| MPEG | mpg;mpeg | 0x000001B3 |
| Quicktime | mov | moov |
| Windows Media | asf | 0x3026B2758E66CF11 |
| MIDI | mid | MThd |
| Win32 Executable | exe;dll;drv;vxd;sys;ocx;vbx | MZ |
| Win16 Executable | exe;dll;drv;vxd;sys;ocx;vbx | MZ |
| ELF Executable | elf;; | 0x7F454C4601010100 |

文章来源: https://blog.upx8.com/3571
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)