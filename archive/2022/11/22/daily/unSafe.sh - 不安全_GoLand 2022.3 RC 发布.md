---
title: GoLand 2022.3 RC 发布
url: https://buaq.net/go-136640.html
source: unSafe.sh - 不安全
date: 2022-11-22
fetch_date: 2025-10-03T23:22:56.448468
---

# GoLand 2022.3 RC 发布

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

![](https://8aqnet.cdn.bcebos.com/181a585490a4996ce2426166f3c2c6a9.jpg)

GoLand 2022.3 RC 发布

这里记录每周值得分享的 Go 语言相关内容，周日发布。本周刊开源（GitHub：polaris1119/golangweekly[1]），欢迎投稿，推荐或自荐文章/软件/资源等，请提交 issue[2
*2022-11-21 18:12:55
Author: [mp.weixin.qq.com(查看原文)](/jump-136640.htm)
阅读量:22
收藏*

---

这里记录每周值得分享的 Go 语言相关内容，周日发布。本周刊开源（GitHub：polaris1119/golangweekly[1]），欢迎投稿，推荐或自荐文章/软件/资源等，请提交 issue[2] 。

鉴于一些人可能没法坚持把英文文章看完，因此，周刊中会尽可能推荐优质的中文文章。优秀的英文文章，我们的 GCTT 组织会进行翻译。

由于微信公众号不支持外链，文中大量链接可通过文末「**阅读原文**」查看。

![](https://mmbiz.qpic.cn/mmbiz_png/UWba2ryLMqnAMBFiaGwhfbVibfCfXdI04QQvCyMvIKfybQia87yibooe9euwneiaAUNC5y6mk0Kvr3nQj9l4P1BytWQ/640?wx_fmt=png)

题图：GoLand 2022.3 RC 发布

## 刊首语

以下代码输出什么？

```
package main

import "fmt"

func main() {
```

## 资讯

1、Google Go 风格指南[3]

Go Style Guide 和随附的文档整理了当前编写可读和惯用的 Go 的最佳方法。

2、GoLand 2022.3 RC 发布[4]

正式版不远了。

3、NSA 推荐使用类型安全的语言代替 C/C++[5]

推荐的重点包括 Go 和 Rust。

4、lo 1.35 发布[6]

基于泛型的 Lodash 风格库。

5、rqlite v7.11.0 发布[7]

轻量的、分布式关系数据库。

6、slashbase 1.1 发布[8]

数据库协作工具。

7、chroma 2.4 发布[9]

纯 Go 实现的通用语法高亮库。

8、ElasticSearch Go 8.5 发布[10]

ElasticSearch Go 8.5 官方客户端发布。

9、fzf 0.35.0 发布[11]

Command-line fuzzy finder。

## 文章

1、[Go标准库依赖的那些modules](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651453706&idx=1&sn=f616f0874b0156c797976540f43b8f9f&scene=21#wechat_redirect)

对于程序员来说，编写的代码依赖标准库是“天经地义”的事情。

2、基于 Twitch 的 Go RPC[12]

类似于 gRPC。

3、在 Go 程序中嵌入提交哈希的 3 种方法[13]

清晰的知晓当前程序使用的哪个提交。

4、[鹅厂后台大佬教你Go内存管理！](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651453711&idx=1&sn=66f4bd572d03eb2827a08cceb4659f0a&scene=21#wechat_redirect)

本文推选自腾讯云开发者社区-【技思广益 · 腾讯技术人原创集】专栏。

5、[Go每日一库之实时可视化Go Runtime指标](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651453714&idx=1&sn=4b81f82f3ccf3f0f68ba2144e1715a39&scene=21#wechat_redirect)

在浏览器中可以实时看到服务的 runtime 指标信息。

6、[成为 Go 高手的 8 个 GitHub 开源项目](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651453722&idx=1&sn=cb799938f25ae7fc74ad06f50beaea09&scene=21#wechat_redirect)

想成为 Go 高手吗？那推荐看看这些开源项目。

7、[一起看看 Go 1.20 新特性有哪些？](https://mp.weixin.qq.com/s?__biz=MzAxMTA4Njc0OQ==&mid=2651453725&idx=1&sn=7fce846e0d5aefa896334a2446e81d91&scene=21#wechat_redirect)

在这篇文章中，一起去Go 1.20 milestone 的 issues 列表中翻翻，提前看看究竟会有哪些新特性加入 Go。

## 开源项目

1、varint[14]

快速、内存高效的、支持任意位的整型。

2、golang-lru[15]

LRU 算法的实现。

3、pie[16]

slice 和 map 便利、通用的操作。

4、tamarin[17]

内嵌的脚本语言。

5、go-quartz[18]

小型、零依赖的调度库，启发自 Java 的 Quartz。

6、memos[19]

开源、自托管的知识管理和协作系统。

7、pdf[20]

从 PDF 文件中提取文本。

## 资源&&工具

1、一致性的 log[21]

基于 Go 官方的结构化日志（视频）。

2、Go Time 第 256 期[22]

grpc 和 protobuf。

3、sablier[23]

按需启动容器，在没有活动时自动关闭容器。Docker、Docker Swarm 模式和 Kubernetes兼容。

## 订阅

这个周刊每周日发布，同步更新在Go语言中文网[24]和微信公众号[25]。

微信搜索"Go语言中文网"或者扫描二维码，即可订阅。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UWba2ryLMqnAMBFiaGwhfbVibfCfXdI04Q8DtiaQzGWZXkpFqFfYIPibuQnp5lOmHgiaIZdh4XxAKlR2KjbB5aUVrVg/640?wx_fmt=jpeg)

wechat

### 参考资料

[1]

polaris1119/golangweekly: https://github.com/polaris1119/golangweekly

[2]

提交 issue: https://github.com/polaris1119/golangweekly/issues

[3]

Google Go 风格指南: https://google.github.io/styleguide/go/index

[4]

GoLand 2022.3 RC 发布: https://blog.jetbrains.com/go/2022/11/17/goland-2022-3-release-candidate-is-out/

[5]

NSA 推荐使用类型安全的语言代替 C/C++: https://www.theregister.com/2022/11/11/nsa\_urges\_orgs\_to\_use/

[6]

lo 1.35 发布: https://github.com/samber/lo

[7]

rqlite v7.11.0 发布: https://github.com/rqlite/rqlite/releases/tag/v7.11.0

[8]

slashbase 1.1 发布: https://github.com/slashbaseide/slashbase

[9]

chroma 2.4 发布: https://github.com/alecthomas/chroma

[10]

ElasticSearch Go 8.5 发布: https://github.com/elastic/go-elasticsearch

[11]

fzf 0.35.0 发布: https://github.com/junegunn/fzf/releases/tag/0.35.0

[12]

基于 Twitch 的 Go RPC: https://thedevelopercafe.com/articles/rpc-in-go-using-twitchs-twirp-3dcb78ece775

[13]

在 Go 程序中嵌入提交哈希的 3 种方法: https://developers.redhat.com/articles/2022/11/14/3-ways-embed-commit-hash-go-programs

[14]

varint: https://github.com/1pkg/varint

[15]

golang-lru: https://github.com/hashicorp/golang-lru

[16]

pie: https://github.com/elliotchance/pie

[17]

tamarin: https://github.com/cloudcmds/tamarin

[18]

go-quartz: https://github.com/reugn/go-quartz

[19]

memos: https://github.com/usememos/memos

[20]

pdf: github.com/dslipak/pdf

[21]

一致性的 log: https://www.youtube.com/watch?v=gd\_Vyb5vEw0

[22]

Go Time 第 256 期: https://changelog.com/gotime/256

[23]

sablier: https://github.com/acouvreur/sablier

[24]

Go语言中文网: https://studygolang.com/go/weekly

[25]

微信公众号: https://weixin.sogou.com/weixin?query=Go%E8%AF%AD%E8%A8%80%E4%B8%AD%E6%96%87%E7%BD%91

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzAxNzY0NDE3NA==&mid=2247490439&idx=1&sn=b4da69aae48e69a5deee4ca2eaefcd71&chksm=9be33466ac94bd70733c90c7e22ad56e3a1302558da71ed4e5b0881d1dded437ae5fea3d0df4#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)