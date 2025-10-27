---
title: EvilTree - A Remake Of The Classic "Tree" Command With The Additional Feature Of Searching For User Provided Keywords/Regex In Files, Highlighting Those That Contain Matche
url: https://buaq.net/go-137612.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:07.153531
---

# EvilTree - A Remake Of The Classic "Tree" Command With The Additional Feature Of Searching For User Provided Keywords/Regex In Files, Highlighting Those That Contain Matche

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

![](https://8aqnet.cdn.bcebos.com/9d3e54e118112f0fb41f2b96efd30131.jpg)

EvilTree - A Remake Of The Classic "Tree" Command With The Additional Feature Of Searching For User Provided Keywords/Regex In Files, Highlighting Those That Contain Matche

A standalone python3 remake of the classic "tree" command with the additional feature of searc
*2022-11-28 21:30:0
Author: [www.kitploit.com(查看原文)](/jump-137612.htm)
阅读量:63
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj3vmZM-pdRewX_8qDhW1Sck1XBVQSripBbC9Dn2ImVuKjbSlrM00yY6OKF6KiKayUgDtj3s1zYUdtxDnnNYa9r-kYJADP5BsGIYlSJcUBqTRL25kmeMG41nCyfg61HShNbQdsagkl7C3jycbPhkDJTNvzQ67e6JCSq8fpPmImNdJWn6nNmuqeFy4mhsw=w570-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEj3vmZM-pdRewX_8qDhW1Sck1XBVQSripBbC9Dn2ImVuKjbSlrM00yY6OKF6KiKayUgDtj3s1zYUdtxDnnNYa9r-kYJADP5BsGIYlSJcUBqTRL25kmeMG41nCyfg61HShNbQdsagkl7C3jycbPhkDJTNvzQ67e6JCSq8fpPmImNdJWn6nNmuqeFy4mhsw)

A standalone python3 remake of the classic "tree" command with the additional feature of searching for user provided keywords/regex in files, highlighting those that contain matches. Created for two main reasons:

* While searching for [secrets](https://www.kitploit.com/search/label/Secrets "secrets") in files of nested [directory](https://www.kitploit.com/search/label/Directory "directory") structures, being able to visualize which files contain user provided keywords/regex patterns and where those files are located in the hierarchy of folders, provides a significant advantage.
* "tree" is an amazing tool for analyzing directory structures. It's really handy to have a standalone alternative of the command for [post-exploitation](https://www.kitploit.com/search/label/Post-Exploitation "post-exploitation") [enumeration](https://www.kitploit.com/search/label/Enumeration "enumeration") as it is not pre-installed on every linux distro and is kind of limited on Windows (compared to the UNIX version).

## Usage Examples

**Example #1**: Running a regex that essentially matches strings similar to: `password = something` against `/var/www`

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjlV0RKRvimp3bbKR5dqybdVaq2Mi66bTb0phTsatOY6XV6JlxD6ACmQLVpRu_APsxgH0D-4Ek2WOhrB8jcBtpJSLdGB-_Mj5N3g7G5d2TN1Nf7qFJYctv5d2mZHXwnCIDxRpgM53Tlg1EswamfvKuwvOnkJOk7u88W_reQzNp46py4az47vWXczCIP-w=w640-h592)](https://blogger.googleusercontent.com/img/a/AVvXsEjlV0RKRvimp3bbKR5dqybdVaq2Mi66bTb0phTsatOY6XV6JlxD6ACmQLVpRu_APsxgH0D-4Ek2WOhrB8jcBtpJSLdGB-_Mj5N3g7G5d2TN1Nf7qFJYctv5d2mZHXwnCIDxRpgM53Tlg1EswamfvKuwvOnkJOk7u88W_reQzNp46py4az47vWXczCIP-w)

**Example #2**: Using comma separated keywords instead of regex:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj3vmZM-pdRewX_8qDhW1Sck1XBVQSripBbC9Dn2ImVuKjbSlrM00yY6OKF6KiKayUgDtj3s1zYUdtxDnnNYa9r-kYJADP5BsGIYlSJcUBqTRL25kmeMG41nCyfg61HShNbQdsagkl7C3jycbPhkDJTNvzQ67e6JCSq8fpPmImNdJWn6nNmuqeFy4mhsw=w570-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEj3vmZM-pdRewX_8qDhW1Sck1XBVQSripBbC9Dn2ImVuKjbSlrM00yY6OKF6KiKayUgDtj3s1zYUdtxDnnNYa9r-kYJADP5BsGIYlSJcUBqTRL25kmeMG41nCyfg61HShNbQdsagkl7C3jycbPhkDJTNvzQ67e6JCSq8fpPmImNdJWn6nNmuqeFy4mhsw)

**Disclaimer**: Only tested on [Windows 10](https://www.kitploit.com/search/label/Windows%2010 "Windows 10") Pro.

## Further Options & Usage Tips

Notable features:

* Regex `-x` search actually returns a unique list of all matched patterns in a file. Be careful when combining it with `-v` (--verbose), try to be specific and limit the length of chars to match.
* You can search keywords/regex in binary files as well by providing option `-b`.
* You can use this tool as the classic "tree" command if you do not provide keywords `-k` and regex `-x` values. This is useful in case you have gained a limited shell on a machine and want to have "tree" with colored output to look around.
* There's a list variable `filetype_blacklist` in `eviltree.py` which can be used to exclude certain file extensions from content search. By default, it excludes the following: `gz, zip, tar, rar, 7z, bz2, xz, deb, img, iso, vmdk, dll, ovf, ova`.
* A quite useful feature is the `-i` (--interesting-only) option. It instructs eviltree to list only files with matching keywords/regex content, significantly reducing the output length:

  [![](https://blogger.googleusercontent.com/img/a/AVvXsEioulvPEN3iWL_MHRFd7-IAu7OrCAmfLVJpx_BGnJQ0AhSwjANokIk0LwbFon-h4o3ADgxwxxhkLB-EDxvhU6KKtFSQf_QcJpSdmbtbXJOMIKw-IAS72xDuFAu3YNUc20TuxJm7deDHDSx8nDyAdBQ2bn9smgbVGH7uWgOz29qjgdR7pO5vPInnyNXoKg=w640-h308)](https://blogger.googleusercontent.com/img/a/AVvXsEioulvPEN3iWL_MHRFd7-IAu7OrCAmfLVJpx_BGnJQ0AhSwjANokIk0LwbFon-h4o3ADgxwxxhkLB-EDxvhU6KKtFSQf_QcJpSdmbtbXJOMIKw-IAS72xDuFAu3YNUc20TuxJm7deDHDSx8nDyAdBQ2bn9smgbVGH7uWgOz29qjgdR7pO5vPInnyNXoKg)

## Useful keywords/regex patterns

* Regex to look for passwords: `-x ".{0,3}passw.{0,3}[=]{1}.{0,18}"`
* Keywords to look for sensitive info: `-k passw,db_,admin,account,user,token`

EvilTree - A Remake Of The Classic "Tree" Command With The Additional Feature Of Searching For User Provided Keywords/Regex In Files, Highlighting Those That Contain Matche
![EvilTree - A Remake Of The Classic "Tree" Command With The Additional Feature Of Searching For User Provided Keywords/Regex In Files, Highlighting Those That Contain Matche](https://blogger.googleusercontent.com/img/a/AVvXsEj3vmZM-pdRewX_8qDhW1Sck1XBVQSripBbC9Dn2ImVuKjbSlrM00yY6OKF6KiKayUgDtj3s1zYUdtxDnnNYa9r-kYJADP5BsGIYlSJcUBqTRL25kmeMG41nCyfg61HShNbQdsagkl7C3jycbPhkDJTNvzQ67e6JCSq8fpPmImNdJWn6nNmuqeFy4mhsw=s72-w570-c-h640)
Reviewed by Zion3R
on
10:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/eviltree-remake-of-classic-tree-command.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)