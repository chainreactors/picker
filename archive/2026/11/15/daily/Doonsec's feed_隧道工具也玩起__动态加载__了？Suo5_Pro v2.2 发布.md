---
title: 隧道工具也玩起\"动态加载\"了？Suo5_Pro v2.2 发布
url: https://mp.weixin.qq.com/s/MA3FAjRDZLdBuEV-mnfQMA
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:43:45.260473
---

# 隧道工具也玩起\"动态加载\"了？Suo5_Pro v2.2 发布

# 隧道工具也玩起"动态加载"了？Suo5\_Pro v2.2 发布

原创

Joy
Joy

安全很忙

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 先说痛点：大马的时代该过去了

做过红队的兄弟应该都有这种体验：

辛辛苦苦传了个 1000 多行的 jsp 上去，还没等隧道连上，先出事了——文件太大被管理员发现、字符串特征被 WAF 标记、Tomcat 版本不对直接 500……

所以这次更新，我把整个思路换掉了。

参考冰蝎、哥斯拉的思路：目标上不再放完整的大 shell，只放一个几十行的小文件（我叫它 stub）。真正的隧道逻辑（payload），在第一次连接的时候由客户端加密下发，在内存里动态加载。

换个说法就是：

* 落盘文件从 1000+ 行缩到几十行
* 静态特征从"全暴露"变成"几乎没有"
* payload 全程 AES 加密传输，中间件重启了客户端还会自动补传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icEiaxZSAJibhnfbaC3aaiaet6uYPM81QaplprIpia8Mff5Z3sxCknTiciaGHm3IfibhFCHPSRho7tNbMRRp6vJUyd4hJyj3fubCICWNpXnSEtuEAJI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhlI6KRsKU5bhdI2GKaUz3YFUiaHuAOghBFtx8ChSiaXNjSulj84PK7H5uVmFgNrV1XKaib9QTuekHm4tvCAVNP1HHiavNnicKJblSaM/640?wx_fmt=png&from=appmsg)

---

## 六个扩展名，一次补齐

以前想换个环境，得来回换 shell。这次直接一把梭：

| 平台 | 支持的扩展名 |
| --- | --- |
| Java | jsp、jspx |
| .NET | aspx、ashx、asmx |
| PHP | php |

说几个有意思的点：

* jsp 双变体：javax 和 jakarta 两个版本自动适配，老 Tomcat 和新 Tomcat 10+ 都能用，不用自己改源码了
* asmx 也能玩：.NET 4 对 asmx 的限制很恶心（远程方法调用只放行 SOAP），我把请求包成了 SOAP 信封来绕过，用起来跟其他扩展名没区别
* payload 全部复用：一个平台的编译产物，所有扩展名共享，不用维护多套逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhnaic5aPZofVcekLmy7FTk4MiciaCt440E0Fibhyle3sW5nfZMibmkEbMnZaAxbLqdhtUtp7SJiakJAg8cf6c8df3L7Y1obtaVeicQjP0/640?wx_fmt=png&from=appmsg)

---

## 去特征化做到什么程度

这版在隐蔽性上下了不少功夫，随便列几个：

1. URL 上没有任何参数——探测、上传靠请求特征区分，不是靠 `?p=0` 这种一眼假的标记
2. 浏览器直接访问显示 404 文本——加载前、加载后表现完全一致，不暴露状态
3. 类名、函数名、文件名全部中性化——不会再出现 `suo5` 字样的字符串
4. 伪装 PHP 会话——正常带 PHPSESSID，混在正常流量里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icEiaxZSAJibhkrNhTMvF06VGOyGzMYYvVIVoFnyVBUm9s0FAXdvFHQusds0LOAm1H264Lia7jZ8SOnAicnC4TsX3QD5gfMybiagMliaExc5TpIJFI/640?wx_fmt=png&from=appmsg)

---

##

## 上手就三步

```
# 1. 生成 shell（挑一个类型）suo5 -g --stub-type jsp --pass foobar -o shell.jsp # 2. 部署到目标 # 3. 连接suo5 -t http://target/shell.jsp --pass foobar
```

连上之后就是熟悉的 SOCKS5 隧道，proxychains、Burp 怎么用就怎么用。

不喜欢命令行的，这版GUI 也同步支持了：生成 Shell、配置口令、连接管理都在界面上点。

![](https://mmbiz.qpic.cn/mmbiz_png/icEiaxZSAJibhlSeVsMhHT1HH7SnZ1vao12ojwk7pic56tQGvHU8VN9cdCbVBdPKPw5UnrlWRsvthhrIg1qzPWqbIbXTaLE6Ef61nYg9LmoPsXA/640?wx_fmt=png&from=appmsg)

---

## 实测情况

这版不是纸上谈兵，本地三套环境全部跑过：

* IIS（aspx/ashx/asmx，half/classic 模式）
* Tomcat 9（jsp/jspx，full/half 模式）
* phpStudy PHP 7.4（php，half/classic 模式）

六种扩展名 × 各模式全通过，连接稳定。

---

## 怎么获取

工具和后续更新只在内部星球发布。

加入方式：微信扫下方二维码 → 加入星球 → 置顶帖自取下载链接和口令。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icEiaxZSAJibhlefbyBAXFMzpv9LiaWK9iadAmpUV8rB0wCeVlwgYVfrdMADOh7ooUh8feKYLzSJ0qoibTiacOJZQwgClCrP2MA9ibCM2IgysMEOphw/640?wx_fmt=jpeg&from=appmsg)

星球里除了工具本体，还会放：

* 各平台 shell 的部署手册和踩坑记录
* 遇到 WAF/杀软时的处理思路
* 我后续版本的第一手更新

---

\*本文所有内容仅用于安全研究与授权测试，请遵守当地法律法规。

预览时标签不可点

作者提示: 内容由AI生成

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZoMH8QJVDfOZxDG0a7Y9rnnQhswjACn0U57PWMdATS0TSJLO0ZKNRibYILiaYl5ns7WB1VaXhWTHphEGOIIaVeLQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过