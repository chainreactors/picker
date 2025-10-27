---
title: Aftermath - A Free macOS IR Framework
url: https://buaq.net/go-141593.html
source: unSafe.sh - 不安全
date: 2022-12-28
fetch_date: 2025-10-04T02:34:45.776806
---

# Aftermath - A Free macOS IR Framework

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

![](https://8aqnet.cdn.bcebos.com/2cb5c8fa927ded9417bc960043b33548.jpg)

Aftermath - A Free macOS IR Framework

Aftermath is a Swift-based, open-source incident response framework. Aftermath can be le
*2022-12-27 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-141593.htm)
阅读量:34
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhjWLGt2r6ldOQjwclTgqWmESkj9bF58AThZAS1wjCBdLsmQtkq8ErwDfhuypV7zdMR57CMr6CbGLM5sPUQqW9a4YtyJaRSRm_BBD99Shdd3j4hst55_OVKapNDpm2dj0XdQLO8LdEAUTP-iJ1kf_oaFAxZ5J-3oqHY6TbmO-AOJArm7Py-eFLXJV4Z6A=w640-h112)](https://blogger.googleusercontent.com/img/a/AVvXsEhjWLGt2r6ldOQjwclTgqWmESkj9bF58AThZAS1wjCBdLsmQtkq8ErwDfhuypV7zdMR57CMr6CbGLM5sPUQqW9a4YtyJaRSRm_BBD99Shdd3j4hst55_OVKapNDpm2dj0XdQLO8LdEAUTP-iJ1kf_oaFAxZ5J-3oqHY6TbmO-AOJArm7Py-eFLXJV4Z6A)

Aftermath is a Swift-based, open-source [incident response](https://www.kitploit.com/search/label/Incident%20Response "incident response") framework.

Aftermath can be leveraged by defenders in order to collect and subsequently analyze the data from the compromised host. Aftermath can be deployed from an MDM (ideally), but it can also run independently from the infected user's command line.

Aftermath first runs a series of modules for collection. The output of this will either be written to the location of your choice, via the `-o` or `--output` option, or by default, it is written to the `/tmp` directory.

Once collection is complete, the final zip/archive file can be pulled from the end user's disk. This file can then be analyzed using the `--analyze` argument pointed at the archive file. The results of this will be written to the `/tmp` directory. The administrator can then unzip that [analysis](https://www.kitploit.com/search/label/Analysis "analysis") [directory](https://www.kitploit.com/search/label/Directory "directory") and see a parsed view of the locally collected databases, a timeline of files with the file creation, last accessed, and last modified dates (if they're available), and a storyline which includes the file metadata, database changes, and browser information to potentially track down the infection vector.

## Build

To build Aftermath locally, clone it from the repository

```
git clone https://github.com/jamf/aftermath.git
```

`cd` into the Aftermath directory

```
cd <path_to_aftermath_directory>
```

Build using Xcode

`cd` into the Release folder

Run aftermath

## Usage

Aftermath needs to be root, as well as have *full disk [access](https://www.kitploit.com/search/label/Access "access") (FDA)* in order to run. FDA can be granted to the Terminal application in which it is running.

The default usage of Aftermath runs

To specify certain options

```
sudo ./aftermath [option1] [option2]
```

Examples

```
sudo ./aftermath -o /Users/user/Desktop --deep
```

```
sudo ./aftermath --analyze <path_to_collection_zip>
```

## Releases

There is an Aftermath.pkg available under [Releases](https://github.com/jamf/aftermath/releases "Releases"). This pkg is signed and notarized. It will install the aftermath [binary](https://www.kitploit.com/search/label/Binary "binary") at `/usr/local/bin/`. This would be the ideal way to deploy via MDM. Since this is installed in `bin`, you can then run aftermath like

```
sudo aftermath [option1] [option2]
```

## Uninstall

To uninstall the aftermath binary, run the `AftermathUninstaller.pkg` from the [Releases](https://github.com/jamf/aftermath/releases "Releases"). This will uninstall the binary and also run `aftermath --cleanup` to remove aftermath directories. If any aftermath directories reside elsewhere, from using the `--output` command, it is the responsibility of the user/admin to remove said directories.

## Help Menu

Contributors

* Stuart Ashenbrenner
* Jaron Bradley
* Maggie Zirnhelt
* Matt Benyo
* Ferdous Saljooki

## Thank You

This project leverages the open source [TrueTree](https://github.com/themittenmac/TrueTree "TrueTree") project, written and [licensed](https://github.com/themittenmac/TrueTree/blob/master/license.md "licensed") by Jaron Bradley.

文章来源: http://www.kitploit.com/2022/12/aftermath-free-macos-ir-framework.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)