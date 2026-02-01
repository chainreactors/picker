---
title: 攻防必备，DLL侧载（白加黑）自动化生成
url: https://mp.weixin.qq.com/s/0qxJXIzvybc2ojyjkFkCiw
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:27.319017
---

# 攻防必备，DLL侧载（白加黑）自动化生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TxTGvuNE4vO31OoTFOJ9mtozRUH6ckljz4jibXbjkib1sdvMTWxZ2OKfd8OJqSdcFqb0d90Ykk1guRQg7icdEhvlw/0?wx_fmt=jpeg)

# 攻防必备，DLL侧载（白加黑）自动化生成

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器中沉浸阅读

还在用传统方法制作白加黑，操作繁琐费劲？现在不需要了。

### 一、背景

#### 什么是"DLL侧载"（白加黑）？

DLL侧载（`DLL Side-Loading`），常被称为"`白加黑`"技术，是一种利用Windows动态链接库加载机制的攻防技术。

> 应用程序在运行时，会加载所需的DLL文件。如DLL缺失确则提示缺少DLL, 如被篡改则程序也将持续运行而无法判断。DLL侧载本质上是DLL未做防篡改导致的`安全漏洞`。

#### 传统手工编译存在缺陷：

一是环境配置复杂，制作可能需要一堆工具及命令，过程繁琐。需要理解PE文件结构、导出函数等知识，同时手工编译的DLL特征明显,尤其是Visual Studio。

### 二、解决方案

高级白加黑技术操作简单，行业入门者也可轻松掌握该技术，工具全自动化编译处理，DLL低特征且自带[反沙箱](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484622&idx=1&sn=dc9f87df89fc3e2a58b955162700d3d0&scene=21#wechat_redirect)。

![工具界面](https://mmbiz.qpic.cn/sz_mmbiz_png/TxTGvuNE4vO31OoTFOJ9mtozRUH6ckljH8ibLPtPxPrsj1icY6MbhR53IibzicHI9myWia6qzxT6rAUtPU8utaEsCZA/640?wx_fmt=png&from=appmsg "null")

工具界面

该技术是2026年红队战术攻防武器库个人产品手册.xlsx[1]主要技术之一。

> DLL侧载只是DLL劫持技术之一，另一种是[DLL代理](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484601&idx=1&sn=f4999fd27213a121586f86882ba9f354&scene=21#wechat_redirect)。

**视频演示：**

### 三、使用场景

* • 适用于高级攻防，在合法授权的渗透测试中使用该技术。
* • 挖掘DLL侧载漏洞提交SRC获取酬金。
* • 理解攻击原理，设计防御方案。

**提示**：部分进攻性方案需签订红队工具销售与使用合规协议[2]

### 四、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

* • 仅可用于已获得书面授权的目标系统测试；
* • 遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 推荐阅读

* • [采用黑白名单匹配进行反沙箱](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484631&idx=1&sn=a67da130197f244e8932ac29346260b1&scene=21#wechat_redirect)
* • [[版本更新]Cobalt Strike基础部署手册&高级白加黑&高级lnk快捷方式新技术](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484622&idx=1&sn=dc9f87df89fc3e2a58b955162700d3d0&scene=21#wechat_redirect)
* • [[0day]新挖掘到一套高级LNK快捷方式](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484553&idx=1&sn=1e2519baefe6c1cafad43d50e21a44f6&scene=21#wechat_redirect)
* • [高级LNK快捷方式自动维持权限与进程注入](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484527&idx=1&sn=cc2e0c5aed6ab97ea43049c7efc09aa2&scene=21#wechat_redirect)
* • [DLL侧载和DLL代理](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484517&idx=1&sn=3edd5871f112f3ff594f36fe37255bee&scene=21#wechat_redirect)
* • [[版本更新]高级lnk快捷方式武器化GUI](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484462&idx=1&sn=4fbe6b7ec7a5e8ac5f86645c945efa23&scene=21#wechat_redirect)
* • [大幅更新-高级lnk快捷方式新技术](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484364&idx=1&sn=3e5971e933477d3fb6f8add935ca5d3f&scene=21#wechat_redirect)
* • [完全无法检测的cobaltstrike更新](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484350&idx=1&sn=315be5bb352b68482ce277b76b6df5d1&scene=21#wechat_redirect)
* • [[工具发布]幻影加载器GUI，高级堆栈欺骗](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483997&idx=1&sn=3bdb95163b6ee8b2f090dd077971f264&scene=21#wechat_redirect)
* • [[工具发布]高级lnk快捷方式武器化GUI](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483965&idx=1&sn=f4d572300f5ea87f73ee964e4a723a71&scene=21#wechat_redirect)
* • [AV终结者结束进程](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483813&idx=1&sn=bd8057f2913cea15526dace893c5d656&scene=21#wechat_redirect)
* • [LNK快捷方式的检测与突破](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483803&idx=1&sn=f428c12e70d4a1ccaf04e999f46fb666&scene=21#wechat_redirect)
* • [红队加载器过主流杀软-混淆最终版](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483791&idx=1&sn=feedaf2b5772d7cdd6f94f4cc5734ad5&scene=21#wechat_redirect)
* • [红队有效载荷加载器](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483765&idx=1&sn=77e289d5df2c6fa011c30c7c79053013&scene=21#wechat_redirect)
* • [10行代码即可免杀全球绝大多数杀毒软件](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483760&idx=1&sn=8aca2da5299bd7133bd295584b597ffc&scene=21#wechat_redirect)
* • [Cobaltstrike4.9.1平台高级匿名技术手册](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483755&idx=1&sn=9e3d1494e319d123bb46d98a45510a23&scene=21#wechat_redirect)
* • [Cobaltstrike4.9.1平台基础部署手册](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483747&idx=1&sn=ab65ae30af9fc0f089cd8a58c0b6ab35&scene=21#wechat_redirect)
* • [全网唯一，高级LNK快捷方式新技术发布](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483729&idx=1&sn=23ba1450e51c2418f99b7ad8c2180a95&scene=21#wechat_redirect)
* • [顶级武器-完全无法检测的cobalt strike](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483684&idx=1&sn=5b97213cbd35cd78540645379db925a1&scene=21#wechat_redirect)

#### 引用链接

`[1]` ++2026年红队战术攻防武器库个人产品手册.xlsx++: *https://www.kdocs.cn/l/coR1BuQkseWz*
`[2]` ++红队工具销售与使用合规协议++: *https://www.kdocs.cn/l/cqPic7iLh0hn*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/TxTGvuNE4vMI7CibneGnaTrUe8AO96ickclFib7VibicQZPEB6kJBcIGEmib8iaAjeoT30iaKayk1fd1ask6Z3ksINc84A/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TxTGvuNE4vMI7CibneGnaTrUe8AO96ickclFib7VibicQZPEB6kJBcIGEmib8iaAjeoT30iaKayk1fd1ask6Z3ksINc84A/0?wx_fmt=png)

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