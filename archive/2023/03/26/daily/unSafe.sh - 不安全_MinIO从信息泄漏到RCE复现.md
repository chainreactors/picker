---
title: MinIO从信息泄漏到RCE复现
url: https://buaq.net/go-155205.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:24.938658
---

# MinIO从信息泄漏到RCE复现

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

![](https://8aqnet.cdn.bcebos.com/244b923898a4e5eef82faf8ee5741c2d.jpg)

MinIO从信息泄漏到RCE复现

信息泄露（CVE-2023-28432）根据公告可得，漏洞利用的前提是使用分布式部署。官方在 https://github.com/minio/minio/pull/8550 中引入bootstrap
*2023-3-25 12:58:43
Author: [mp.weixin.qq.com(查看原文)](/jump-155205.htm)
阅读量:165
收藏*

---

## 信息泄露（CVE-2023-28432）

根据公告可得，漏洞利用的前提是使用分布式部署。

官方在 https://github.com/minio/minio/pull/8550 中引入bootstrap API 并于 RELEASE.2019-12-17T23-16-33Z发布，用于验证服务器配置。

漏洞相关代码如下：

```
// minio/cmd/bootstrap-peer-server.go
```

这里可以看到缺少鉴权，所以直接未授权访问，但是这个路由只有在集群部署的模式下才可访问，所以在集群部署的MinIO环境下攻击者构造恶意的请求，会打印出环境变量信息，当中正好包含了管理员的账号密码。

那么为什么环境变量中会包含账号密码信息呢？因为根据官方的启动说明，在MinIO在启动时会从环境变量中读取用户预设的管理员账号和密码，如果省略则默认账号密码为minioadmin/minioadmin。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wYsia8W1QNJsV5icTptoibB55xoGk29h8y57ibmJEDFFXibTnicKZ78icU5Ticnjt7YvOujStAmSMAGPBEGKnE7GURMEkQ/640?wx_fmt=jpeg)

那么还有有一种情况，如果开启动Minio时没有设置`MINIO_ROOT_USER`和`MINIO_ROOT_PASSWORD`，那么Minio就会启动默认的账号密码`minioadmin`，这时候通过信息泄露会发现读取不到管理员的账号密码，可以判断存在默认口令。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wYsia8W1QNJsV5icTptoibB55xoGk29h8y5iaXUQ3kCib7SJvVr3y1ymbyYLv8QY9klrWpQoUYRMf94YnCPUyQ0dF4Q/640?wx_fmt=jpeg)

## 从信息泄露到RCE

通过第一步获取到管理员账号密码之后，可以通过官方自带的mc（MinIO客户端）工具进行服务器管理，首先通过mc连接远程的MinIO服务器：

```
mc alias set myminio http://192.168.31.8:9000 minioadmin miniopassword
```

MinIO提供了一个非常方便的功能，可以通过mc（MinIO客户端）远程升级MinIO服务器，关键在于升级地址是可以通过预设自定义的，在官方的说明文档中并没有详细说明，企业如果是内网环境可以指定自己的更新地址以便于升级。

![](https://mmbiz.qpic.cn/mmbiz_png/wYsia8W1QNJsV5icTptoibB55xoGk29h8y5bqg9kJicz7c8xJDejTMRAfVX3OKGXCoD2q7Vmk5YhNPicUsdg6XQlQIw/640?wx_fmt=png)

经过研究发现，当执行升级命令后

```
mc admin update myminio -y
```

默认会从官方服务器获取最新版本，相关代码中的定义如下：

```
// minio/cmd/update.go
const (
    minioReleaseTagTimeLayout = "2006-01-02T15-04-05Z"
    minioOSARCH               = runtime.GOOS + "-" + runtime.GOARCH
    minioReleaseURL           = "https://dl.min.io/server/minio/release/" + minioOSARCH + SlashSeparator

    envMinisignPubKey = "MINIO_UPDATE_MINISIGN_PUBKEY"
    updateTimeout     = 10 * time.Second
)
```

通过跟进代码的相关逻辑可以发现，可以直接拉取一个二进制文件，然后实现自我更新，相关简化流程如下：

验证管理员权限→获取最新版本→获取最新版本的sha256sum信息→下载并验证sha256sum→验证无误后替换自身并重启

虽然sha256我们不可控，但是用于验证的sha256sum文件是我们可控的。

https://github.com/minio/minio/pull/16857/commits/4d4cc50dd6656512dee483492aa0a241babd35c4

跟进相关代码可以发现，envMinisignPubKe默认为空，导致签名校验失效，所以我们可以构造恶意升级包，最终形成RCE。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wYsia8W1QNJsV5icTptoibB55xoGk29h8y5OhwFnsu790TMRGmCibwSGlhObndicMr8iaYkuylNibteZFeTR3Htx2jHsQ/640?wx_fmt=jpeg)

构造恶意的更新指令后提示正常更新，并且执行了我们提供的恶意程序，但是替换了恶意程序之后，原本的MinIO服务会中断，所以想要无损利用需要考虑基于源程序进行魔改，并且这个漏洞的利用与部署方式无关，只要获取到了管理员账号密码就能实现恶意升级。

截止到发文前，官方对以上两个漏洞均已进行修复，建议用户更新到最新版本。**默安科技巡哨、刃甲等多产品已经支持该漏洞检测，幻阵沙箱云市场已发布该漏洞的诱捕沙箱。**

1.https://github.com/minio/minio/security/advisories/GHSA-6xvq-wj2x-3h3q

2.https://github.com/minio/minio

3.https://min.io/docs/minio/linux/reference/minio-mc-admin/mc-admin-update.html

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzkxMjI3MDgwOA==&mid=2247484679&idx=1&sn=b86fbb113964f7c7673de72430f3af08&chksm=c10e31b0f679b8a6f1c50d356a99f9b4128b29e940e6e706dc41c0177d86bda056dc4ca02860&mpshare=1&scene=1&srcid=0324auhHD1Ix54jBFFelPetK&sharer\_sharetime=1679720316610&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)