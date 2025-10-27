---
title: OFRAK - Unpack, Modify, And Repack Binaries
url: https://buaq.net/go-141346.html
source: unSafe.sh - 不安全
date: 2022-12-26
fetch_date: 2025-10-04T02:30:42.359614
---

# OFRAK - Unpack, Modify, And Repack Binaries

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

![](https://8aqnet.cdn.bcebos.com/7b8ea2757904d0a0fe0fd8c9b232b560.jpg)

OFRAK - Unpack, Modify, And Repack Binaries

OFRAK (Open Firmware Reverse Analysis Konsole) is a binary analysis and modification platfor
*2022-12-25 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-141346.htm)
阅读量:41
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjiBNkPBTHSL_td65ql_0b_cMdzWCtwMgQuwMSqgIf9TsRGW7jhUM1_ucJdf_0btYC-EK54ZJGB14Q7sm8U_7Dje8CoEVr7FAul3RbizvoQWD5l1ZpyLa5I_1YxpXvcP90CIZ6wmxzm3c29FQ3vW9iOQk1uDNK1DdL_3g2n116gfseyHgR-R6K5Ume2-w=w640-h370)](https://blogger.googleusercontent.com/img/a/AVvXsEjiBNkPBTHSL_td65ql_0b_cMdzWCtwMgQuwMSqgIf9TsRGW7jhUM1_ucJdf_0btYC-EK54ZJGB14Q7sm8U_7Dje8CoEVr7FAul3RbizvoQWD5l1ZpyLa5I_1YxpXvcP90CIZ6wmxzm3c29FQ3vW9iOQk1uDNK1DdL_3g2n116gfseyHgR-R6K5Ume2-w)

OFRAK (Open Firmware Reverse Analysis Konsole) is a [binary analysis](https://www.kitploit.com/search/label/Binary%20Analysis "binary analysis") and [modification](https://www.kitploit.com/search/label/Modification "modification") platform. OFRAK combines the ability to:

* **Identify** and **Unpack** many binary formats
* **Analyze** unpacked binaries with field-tested [reverse engineering](https://www.kitploit.com/search/label/Reverse%20Engineering "reverse engineering") tools
* **Modify** and **Repack** binaries with powerful patching strategies

OFRAK supports a range of embedded firmware file formats beyond userspace executables, including:

* Compressed filesystems
* Compressed & checksummed firmware
* Bootloaders
* RTOS/OS kernels

OFRAK equips users with:

* A **Graphical User Interface (GUI)** for interactive exploration and [visualization](https://www.kitploit.com/search/label/Visualization "visualization") of binaries
* A **Python API** for readable and reproducible scripts that can be applied to entire classes of binaries, rather than just one specific binary
* Recursive **identification, unpacking, and repacking** of many file formats, from ELF executables, to filesystem archives, to compressed and checksummed firmware formats
* Built-in, extensible **integration with powerful analysis backends** (angr, Binary Ninja, Ghidra, IDA Pro)
* **Extensibility by design** via a common interface to easily write additional OFRAK components and add support for a new file format or [binary patching](https://www.kitploit.com/search/label/Binary%20Patching "binary patching") operation

See [ofrak.com](https://ofrak.com "ofrak.com") for more details.

## GUI Frontend

The web-based GUI view provides a navigable resource tree. For the selected resource, it also provides: metadata, hex or text navigation, and a mini map sidebar for quickly navigating by entropy, byteclass, or magnitude. The GUI also allows for actions normally available through the Python API like commenting, unpacking, analyzing, modifying and packing resources.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjiBNkPBTHSL_td65ql_0b_cMdzWCtwMgQuwMSqgIf9TsRGW7jhUM1_ucJdf_0btYC-EK54ZJGB14Q7sm8U_7Dje8CoEVr7FAul3RbizvoQWD5l1ZpyLa5I_1YxpXvcP90CIZ6wmxzm3c29FQ3vW9iOQk1uDNK1DdL_3g2n116gfseyHgR-R6K5Ume2-w=w640-h370)](https://blogger.googleusercontent.com/img/a/AVvXsEjiBNkPBTHSL_td65ql_0b_cMdzWCtwMgQuwMSqgIf9TsRGW7jhUM1_ucJdf_0btYC-EK54ZJGB14Q7sm8U_7Dje8CoEVr7FAul3RbizvoQWD5l1ZpyLa5I_1YxpXvcP90CIZ6wmxzm3c29FQ3vW9iOQk1uDNK1DdL_3g2n116gfseyHgR-R6K5Ume2-w)

## Getting Started

**OFRAK uses Git LFS. This means that you must have Git LFS installed before you clone the repository!** Install Git LFS by following [the instructions here](https://git-lfs.github.com/ "the instructions here"). If you accidentally cloned the repository before installing Git LFS, `cd` into the repository and run `git lfs pull`.

See [`docs/environment-setup`](https://ofrak.com/docs/environment-setup.html "OFRAK: unpack, modify, and repack binaries. (9)") for detailed instructions on how to install OFRAK.

## Documentation

OFRAK has general documentation and API documentation. Both can be viewed at [ofrak.com/docs](https://ofrak.com/docs "ofrak.com/docs").

If you wish to make changes to the documentation or serve it yourself, follow the directions in [`docs/README.md`](https://github.com/redballoonsecurity/ofrak/blob/master/docs/README.md "OFRAK: unpack, modify, and repack binaries. (11)").

## License

The code in this repository comes with an [OFRAK Community License](https://github.com/redballoonsecurity/ofrak/blob/master/LICENSE "OFRAK Community License"), which is intended for educational uses, personal development, or just having fun.

Users interested in OFRAK for commercial purposes can request the Pro License, which for a limited period is available for a free 6-month trial. See [OFRAK Licensing](https://ofrak.com/license/ "OFRAK Licensing") for more information.

## Contributing

Red Balloon Security is excited for security researchers and developers to contribute to this repository.

For details, please see our [contributor guide](https://github.com/redballoonsecurity/ofrak/blob/master/CONTRIBUTING.md "contributor guide") and the [Python development guide](https://github.com/redballoonsecurity/ofrak/blob/master/docs/contributor-guide/getting-started.md "Python development guide").

## Support

Please contact [[email protected]](http://www.kitploit.com/cdn-cgi/l/email-protection#e6898094878da694838284878a8a89898895838593948f929fc885898b "ofrak@redballoonsecurity.com"), or write to us on [the OFRAK Slack](https://join.slack.com/t/ofrak/shared_invite/zt-1dywj33gw-DcicqLmzgbdeRTCSF0A_Jg "the OFRAK Slack") with any questions or issues regarding OFRAK. We look forward to getting your feedback! Sign up for the [OFRAK Mailing List](https://ofrak.com/sign-up "OFRAK Mailing List") to receive monthly updates about OFRAK code improvements and new features.

---

OFRAK - Unpack, Modify, And Repack Binaries
![OFRAK - Unpack, Modify, And Repack Binaries](https://blogger.googleusercontent.com/img/a/AVvXsEjiBNkPBTHSL_td65ql_0b_cMdzWCtwMgQuwMSqgIf9TsRGW7jhUM1_ucJdf_0btYC-EK54ZJGB14Q7sm8U_7Dje8CoEVr7FAul3RbizvoQWD5l1ZpyLa5I_1YxpXvcP90CIZ6wmxzm3c29FQ3vW9iOQk1uDNK1DdL_3g2n116gfseyHgR-R6K5Ume2-w=s72-w640-c-h370)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/ofrak-unpack-modify-and-repack-binaries.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)