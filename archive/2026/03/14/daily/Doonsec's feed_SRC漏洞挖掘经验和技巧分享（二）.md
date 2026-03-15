---
title: SRC漏洞挖掘经验和技巧分享（二）
url: https://mp.weixin.qq.com/s/UzktGT1fASGI-hg_WL2Tfg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:29:06.657106
---

# SRC漏洞挖掘经验和技巧分享（二）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquOibeMppYQN2HJClnY0WAE08J2VibCdR3DO52gpW3GIFaAa4SNf6XOQjaPIkpOj5ISsQDpOz4at7LtG6Tjsp1VfkZqyNsA90aUIg/0?wx_fmt=jpeg)

# SRC漏洞挖掘经验和技巧分享（二）

船山团队
船山团队

船山信安

![]()

在小说阅读器中沉浸阅读

# SRC漏洞挖掘经验和技巧分享

继续衔接上篇，本篇从字典、业务安全、APP测试这三个环节来分析决定你能否挖到其他更高价值的漏洞

---

## 一、字典的收集与优化：从量变到质变

字典是爆破的灵魂，但网上公开的字典大多藏着掖着，或者不够全面。

对于字典其实我相信很多师傅都有自己的一套方法，但是在互联网上分享的字典或者对应的字典工具的确有点藏着掖着的感觉。

使自己的字典更强大是我这几年一直在做的事情，作为一个没有太多资源的安全爱好者，我能做的就是去收集能收集到的一切信息并做整合优化。

### 1. 子域名字典来源

* 各大子域名枚举工具自带的字典，合并去重。
* **rapid7的公开数据集**：https://opendata.rapid7.com/sonar.fdns\_v2/ 和 https://opendata.rapid7.com/sonar.rDNS\_v2/ 这两个数据包含海量的DNS记录，可以提取里面的子域名作为字典。当然数据量巨大，需要写脚本清洗，是个体力活。

### 2. 站点目录/文件/参数/JS字典来源

提前下载了1000多个开源的CMS源码，写正则提取它们的目录结构、脚本文件名、参数名、JS文件名等，分门别类存入数据库。比如：

* 目录类：/admin/, /upload/, /include/...
* 可执行脚本类：login.php, api.jsp, index.aspx...
* 参数类：id,page, file, callback...
* 静态资源类：jquery.js, main.js...

有了这些数据，字典的质量就上来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquMUJgTDTSXwZaic8VIciaXBIgId7BDo9PQPStLmo551QRh6zFO5xGlvU6eic3hSFotQypNTRQIicIOWdD5myjAibvPrZk1TmvibdWsvQ/640?wx_fmt=jpeg&from=appmsg)

### 3. 字典的优化

字典越全越好，但太大又影响效率。我的做法是：**将字典入库，增加一个命中次数计数器**。每次爆破时，从数据库里按命中次数降序提取关键词，优先使用高频词。爆破过程中，如果某个关键词命中了，就把它的计数加1。这样循环几次，字典就会自动优化，经常出现的词排前面，效率越来越高。

### 4. 实战案例

#### Uber的二次注入

有一次我在Uber的某个API接口里测试，发现参数名是 openid，直觉告诉我这里可能有二次注入。我添加了注入语句，结果返回正常；然后我查询刚刚添加的用户信息，果然触发了报错：

```
{"result":"error","ermsg":"ER_UNKNOWN_ERROR: XPATH syntax error: '-uber_community-'"}
```

最终Uber给了丰厚的奖励。这个案例让我意识到：**参数名的精准收集**有多重要，如果我字典里没有openid，可能就错过了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquNGDR6uEiazCsgMiac0fScV2bkn4DIxcDzULh6TMutCe0vWU6FhbUXPmYltepAfFGpTuL5wFYfwFibIrmOR0RKZN7eI1AS0otq5vY/640?wx_fmt=jpeg&from=appmsg)

#### 403页面的逆袭

另一个案例，一个IP访问首页返回403 Forbidden，很多人看到403就放弃了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquNmN0Oy3EnVg1T0k7NPWVkykZHHdibGPV40FpQW3wbGoRfe7vROWngcTl2jhNKltuX8xSreO9qgCb9lWhahdwcFLGk087jXImSs/640?wx_fmt=jpeg&from=appmsg)

但我用目录爆破和脚本文件爆破，找到了 /adver/landing.php

![](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquPEcezFGvV6FEfFicDt1UcibvyMWiamGE6PdeWvDicS5HeWtk0ldayLsdduD87Ay4Ey6uUSmSoRgOkibtv3VLkXavC8gk0KRrfh3yBU/640?wx_fmt=jpeg&from=appmsg)

访问提示缺少参数。接着爆破参数，找到 mac 参数，加上单引号测试，成功触发SQL注入，拿到了数据库权限，还是个游戏业务库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquOQgtACp1jiacqCnVe2Kjm8Sbicr9czgtdLsQEgg2hPoPmDqBibk42ClicSF6Jhkh0iakQbnfLibIo0t3hjXSkY9XCez51KEFQZkmdrY/640?wx_fmt=jpeg&from=appmsg)

所以，别放过任何一个403，说不定背后藏着大洞。

---

## 二、业务安全：盯住“非普通用户”和“新业务”

国内SRC最看重业务安全，因为业务漏洞直接影响厂商的钱袋子。大致分为两个最容易出问题的点：

1. **非普通用户权限**：比如商家后台、合作方接口、签约作者管理后台等。想尽办法搞到这些账号，哪怕用点小社工手段（当然要在合规范围内）。这些账号的权限比普通用户大，测试起来更容易发现越权、逻辑漏洞。
2. **新上线业务**：很多厂商新业务上线时，安全测试往往不够充分，而且业务方急于推广，可能忽略了一些细节。所以要多关注厂商的微信公众号、官方公告，第一时间拿到新业务的入口去测试。

---

## 三、APP测试：绕过证书锁定

现在很多APP都用了证书锁定（SSL Pinning），把服务器的SSL证书内置到APP里，导致抓包工具无法解密HTTPS流量。解决办法：

* **iOS**：越狱手机，安装插件 **SSL Pinning Disable**，就能绕过。具体教程我之前写在博客里：http://pwn.dog/index.php/ios/ios-disable-ssl-pinning.html
* **Android**：可以用 **DroidSSLUnpinning** 工具，GitHub地址：https://github.com/WooyunDota/DroidSSLUnpinning

绕过之后就能正常抓包分析APP的API接口了，往往能发现很多Web端没有的业务功能，基本都可以利用了。

---

### 总结:

### 就是拼细节。字典你比别人全一点，业务逻辑你多测一个点，APP你多抓一个包，漏洞点就可能更容易被发现。

以上内容根据个人经验整理，如有疏漏，欢迎指正。如果你有更好的技巧，也欢迎在评论区分享交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过