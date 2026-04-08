---
title: 从原理到实战：COM劫持持久化机制全解析
url: https://mp.weixin.qq.com/s/qdgCLpyw6wVK-eklZT3TSA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:31:04.217754
---

# 从原理到实战：COM劫持持久化机制全解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/H6RmIowwbs4I1p9oKgYtZAjNosib0B1dluUOpYoI3BvHdWe4U7YBW4yZeicQnfXS2UGDaXaeWurIaecp7aZCfK0yulS0sImg8T2tZA1Rk1o7c/0?wx_fmt=jpeg)

# 从原理到实战：COM劫持持久化机制全解析

原创

weiqin
weiqin

大仙安全说

![]()

在小说阅读器中沉浸阅读

点击蓝字，关注我们

大

仙

![](https://mmbiz.qpic.cn/mmbiz_png/oZN2pbzJKdWUK3Ne8uSjJibGEKUc8s8FbE3ibZ4mjQicF2gDe1DTSIqmWKU5YsEtQgKubRf5IySO9NkDcr1valibkw/640?wx_fmt=png)

免责声明

大仙安全说的技术文章仅供参考，此文所提供的信息只为网络安全人员进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他! ! !

**01**

**COM劫持技术原理**

***一：COM组件机制***

COM（Component Object Model）是微软的跨进程组件通信标准。每个COM对象通过唯一的128位CLSID（ClassIdentifier）标识，注册表结构如下：

```
HKEY_CLASSES_ROOT\CLSID\{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}  ├── InprocServer32    → 指向DLL文件路径（内嵌服务器）  ├── LocalServer32     → 指向EXE文件路径（本地服务器）  ├── ProgID            → 人类可读的程序标识符  └── ThreadingModel    → 线程模型
```

***二：劫持顺序***

Windows按以下顺序查找COM对象：

```
HKEY_CURRENT_USER\Software\Classes\CLSID（用户级，优先）HKEY_CLASSES_ROOT\CLSID（HKCU与HKLM的合并视图）HKEY_LOCAL_MACHINE\Software\Classes\CLSID（系统级）
```

***三：劫持类型***

现有CLSID劫持：在HKCU创建同名CLSID覆盖HKLM配置

孤儿CLSID劫持：利用应用程序尝试加载不存在的COM对象

TreatAs重定向：修改TreatAs键指向恶意CLSID

TypeLib劫持：滥用类型库实现远程脚本执行

**02**

**实战样本分析**

先运行Procmon再点击样本进行捕获

注册表修改：

```
HKEY_CURRENT_USER\Software\Classes\CLSID\{b5f8350b-0548-48b1-a6ee-88bd00b4a5e7}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5qiaPkrryoxibib5V2QxhaXhRibicV4qfkic4NniaOZuxC73yH4uO2PFibdFFEBtvuaQHxk9OaibO3xiakRHia4V2ss0W11ZrcypNWkugvhE/640?wx_fmt=png)

紧接着捕获到文件创建：

C:\Windows\System下有2个文件创建

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs7skHia5bswpQn0L5d3bVPooHlaVhalPS27PN7Zabls4yiaWBOs0lQaicqDxndroIRYrNC0z1Enc5fmKgLTrsO9g6mRwNPeLY37Rk/640?wx_fmt=png)

**03**

**注册表与文件取证**

进入注册表发现默认值的数值路径与procmon捕获到的文件一致

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs6RVrhlXeU2eLqtVjmFxicBNeR65MU6Zz5qztYaud6eRbx0yGdUpx4fMSBZnv0TKdgvZu6iaCcQtasEJQpGOVJLicO64ga7d2VuzI/640?wx_fmt=png)

打开C:\Windows\System，确实有2个文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs7XG6KDCxjSYygKls9Zs4vrV8bS9L1UVbdWhbOc1CsaWG7a4J2xMaERdJ1HO9YF5iczKMqzGjLdSHr275N4Zyx7gHv1eT2zzms4/640?wx_fmt=png)

**04**

**沙箱分析验证**

将2个文件上传到微步云沙箱进行验证，2个文件都为COMpfun家族。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs52JMDjwQfiasgJEZZF5fvicSiblwjHeDUNg1WSia13WicbVEdeWOVmjjF4QgPibRrwDlswRPCPia8EniaYdENtoFW8DYuosBV91nXZpzA/640?wx_fmt=png)

COMpfun是一个隶属于Turla APT组织的远程访问木马（RAT）家族，以创新的COM劫持技术著称。是最早系统性使用COM劫持的恶意软件之一

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs62a4799vGAh83VS6KhNL5EIxx4ZxyyRKxRF2HXcQtDuzmhGsOrnXa9OW4tWTLmcFXvvfk8Ld21plnT1xLGRpHr9m4ibiaVhErUo/640?wx_fmt=png)

**05**

**总结**

COM劫持技术的隐蔽性和稳定性使其成为APT攻击中的首选持久化手段，但通过注册表监控、行为分析和应用控制，可以有效检测和防御此类威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs5Z9YYreb8LonZ0EKcxDIfILgz4JlpI06HusCS54yAIACRFm9N83cRX3lRvYDIvcqTj5pBj1oAn2XjKpRRTU21IYaaeibaAuARs/640?wx_fmt=png)

**添加好友注明来意**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Eghr41R49Dsaibt7QQtMcrDaRXfz1W7bnr1Ajjd8ia3xhsylXhcJcze1tic4XKZcrn5LFSm3rTicZBhg/640?wx_fmt=png)

**公众号丨大仙安全说**

**VX丨weiqin\_6666**

**长按关注**

《往期阅读》

[ProcMon也被注入？DLL 搜索顺序劫持排查](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485127&idx=1&sn=3a62ea33a82e2f3a913703b0224188ac&scene=21#wechat_redirect)

[隐藏在所有进程背后的黑手：AppInit\_DLLs 持久化机制深度拆解](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485126&idx=1&sn=6e90ef6c7f26a8669ebbf482ba3ea744&scene=21#wechat_redirect)

[注册表被“记事本”劫持？镜像劫持 + Winlogon 持久化](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485085&idx=1&sn=62fe8382de32300806eadd001313b0bc&scene=21#wechat_redirect)

[注册表被锁、任务管理器打不开？“Debugger=0”引发的](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485084&idx=1&sn=0b44a18056390d9ae175eac9e980096e&scene=21#wechat_redirect)

[实战拆解：Autoruns揪出隐藏的计划任务木马](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485083&idx=1&sn=899a620666440c37d664f3ca04823acb&scene=21#wechat_redirect)

[零基础也能分析病毒！Noriben新手入门指南](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485048&idx=1&sn=930f31e639608dd45717ac99f907307c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/y00icvcPjkfYXic35ml9MJkg41yEDAQhzc0iapH6CWjEX1NA3nKbfZutZD03lYTDD8xvsicziaB94zOohn2jEhFQnNg/640?wx_fmt=gif)

**分享、在看与点赞，至少我要拥有一个吧**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/afo75o4gacpFHp4O7KXstEGdnGtCnk9v1azmwLFNoS3XPibDA2mw0MKuDbLj96h4eNIdOKXRicDicTn4PiciagBpZWQ/0?wx_fmt=png)

大仙安全说

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/afo75o4gacpFHp4O7KXstEGdnGtCnk9v1azmwLFNoS3XPibDA2mw0MKuDbLj96h4eNIdOKXRicDicTn4PiciagBpZWQ/0?wx_fmt=png)

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