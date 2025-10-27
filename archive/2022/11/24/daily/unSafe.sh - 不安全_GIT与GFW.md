---
title: GIT与GFW
url: https://buaq.net/go-136964.html
source: unSafe.sh - 不安全
date: 2022-11-24
fetch_date: 2025-10-03T23:36:52.004572
---

# GIT与GFW

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

GIT与GFW

11.24 GIT与GFWhttp://scz.617.cn:8/unix/202211231303.txtQ:有时可能需要git clone --recursive [email protected
*2022-11-23 23:59:13
Author: [mp.weixin.qq.com(查看原文)](/jump-136964.htm)
阅读量:23
收藏*

---

11.24 GIT与GFW

http://scz.617.cn:8/unix/202211231303.txt

Q:

有时可能需要

git clone --recursive [[email protected]](https://mp.weixin.qq.com/cdn-cgi/l/email-protection)…

但.gitmodules中是这样的

[submodule "subm1"]

于是递归中出现

git clone https://…

众所周知，寡妇王对HTTPS并不友好，挂线路自然是可以的，但我想问的是，假设可以手工修改拖回本地的.gitmodules，有无正经办法让递归时不用HTTPS。现在只能clone完主模块后，手工clone每个子模块，将https换成git；倒也可行，只是太low。

A: 2022-11-23

网友「李同学virusdefender」(3560808645)指出，可以用insteadOf配置。实测如下用法满足原始需求

```
cd /tmp
git config --global [email protected]:.insteadOf https://github.com/
git config -l
git clone --recursive https://github.com/libbpf/libbpf-bootstrap.git libbpf-bootstrap
git config --global --unset [email protected]:.insteadOf
git config -l
```

"git config -l"无必要，只是为了观察配置。"--unset"无必要，只是出于洁癖，我不喜欢改.gitconfig文件。配置生效期间，所有"https://"被自动替换成"[[email protected]](https://mp.weixin.qq.com/cdn-cgi/l/email-protection)…"。

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzUzMjQyMDE3Ng==&mid=2247486327&idx=1&sn=d725ae94076bc483248485bba8d5f34f&chksm=fab2c848cdc5415ea039d28a0dd64368908c6485798dfd019251aa2299af84cb3c5f0a0c90e9#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)