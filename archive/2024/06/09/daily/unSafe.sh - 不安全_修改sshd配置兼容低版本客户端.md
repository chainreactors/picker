---
title: 修改sshd配置兼容低版本客户端
url: https://buaq.net/go-244116.html
source: unSafe.sh - 不安全
date: 2024-06-09
fetch_date: 2025-10-06T16:55:44.450814
---

# 修改sshd配置兼容低版本客户端

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

修改sshd配置兼容低版本客户端

Linux新版Ubuntu 24.04 LTS，Fedora 40等Linux发行版陆续发布，系统自带的OpenSSH版本（包括SSL等依赖库）也随同更新升级。新版OpenSSH-server默认使
*2024-6-8 20:52:6
Author: [itlanyan.com(查看原文)](/jump-244116.htm)
阅读量:30
收藏*

---

[Linux](https://itlanyan.com/category/linux/)

新版Ubuntu 24.04 LTS，Fedora 40等Linux发行版陆续发布，系统自带的OpenSSH版本（包括SSL等依赖库）也随同更新升级。新版OpenSSH-server默认使用更安全、更新的加密算法，可能导致旧客户端、包括使用旧版openssh库的程序/组件无法正常登录。

命令 `journalctl -xe --no-pager -u sshd.service` 可以查看密钥交换过程中的错误信息，一般是密钥交换算法、主机密钥算法不匹配导致。解决方法一是更新升级客户端，二是修改服务端配置，使用兼容的算法。

如果使用第二种解决方式，需要修改 `/etc/ssh/sshd_config` 文件。最为关键的四个配置如下代码段所示，根据错误提示修改对应配置项即可（一般需要修改 KexAlgorithms 和 HostKeyAlgorithms）。

```
Ciphers aes128-ctr,aes192-ctr,aes256-ctr
HostKeyAlgorithms ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-rsa,ssh-dss
KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1,
diffie-hellman-group-exchange-sha256
MACs hmac-sha2-256,hmac-sha2-512,hmac-sha1
```

## 参考

1. <https://www.openssh.com/legacy.html>

赞

文章来源: https://itlanyan.com/config-sshd-to-old-clients/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)