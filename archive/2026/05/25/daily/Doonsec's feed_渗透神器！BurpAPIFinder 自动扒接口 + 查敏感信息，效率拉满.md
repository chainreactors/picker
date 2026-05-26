---
title: 渗透神器！BurpAPIFinder 自动扒接口 + 查敏感信息，效率拉满
url: https://mp.weixin.qq.com/s/aroFBUTFo5lk_5p9LUvsUA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:07:57.253519
---

# 渗透神器！BurpAPIFinder 自动扒接口 + 查敏感信息，效率拉满

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zqnzfCSS1kABwmHV1VgicMibblc2bcGh1dWVCKvRAehicibXWicFUgFAxvOs4HAd7Uibp7A8RXbojia4AibMh9dgl7v6WRJuxUD3N2r9CuBj7CJsrc4/0?wx_fmt=jpeg)

# 渗透神器！BurpAPIFinder 自动扒接口 + 查敏感信息，效率拉满

Hack分享吧

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 免费加入 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

做渗透测试的朋友都懂，手动翻 JS 找接口、查敏感信息有多折磨人。

页面上看不到的接口藏在 JS 路由里，后台路径埋在配置文件中，账号密码、云密钥、Token 等敏感数据说不定就明晃晃漏在响应里…… 一个个翻、一个个试，不仅慢还容易漏。

今天给大家安利一款**专为渗透测试打造的 Burp 插件 ——BurpAPIFinder**，不用复杂配置，挂着代理跑一跑，前端接口全梳理、敏感信息全标记，直接解放双手！

![](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kASM7HsOCT6j2zHEzlv9UPJm4BeRDdeQZmyeicH7d9Qt3Tgn1hNe7JOib9Q7dDUT1gdib87HBpF7UmyA2MicIPG69mO8xO1Kv61iaiaU/640?wx_fmt=png&from=appmsg)

**插件到底能干嘛？核心功能一目了然**

BurpAPIFinder 是基于 Burp Suite 开发的接口发现与敏感信息识别插件，全程监听代理流量，自动干活不添乱，核心能力超实用：

**1、全自动提取接口路径**

不只是正则匹配，支持多模式从 HTML、JS 文件里扒出绝对 URL、相对路径、接口后缀，连隐藏 API、管理端路径都能揪出来。

2. **2、一站式敏感信息排查**

   内置 106 条攻防实战指纹，还集成 HaE、APIKit、sweetPotato 三大主流规则，账号密码、手机号、身份证、云 KEY、JWT、Shiro 特征全不放过。
4. **3、智能路径补全探测**

   支持自定义父路径，自动把发现的接口拼接到 /api/v1、/admin 等前缀下重试，专治前后端分离、版本化接口。
6. **4、可视化结果一键筛选**

   主界面实时展示请求数据，支持 “只看重点”“只看敏感内容”“只看 200 状态”，海量接口快速收敛，重点漏洞优先查。
8. **5、带凭证自动复测**

   可自定义 Cookie、Authorization 请求头，匿名访问不通的接口，带凭证自动重测，不放过未授权访问漏洞。
9. ![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kD0xxdjzNNloSXwhLTpr33ZFCCktILJViaEqTfyNbZPp6LuZDcD9lmUP8ibh8oibhDhOF3qwVxRyS186lpzpgY7Mq7YicSLlhoxiadU/640?wx_fmt=png&from=appmsg)

**技术原理：轻量高效，不干扰测试流程**

插件全程只监听 Burp Proxy 响应包，不修改原始请求，测试更安全，核心流程超清晰：

1. 监听 Burp 代理流量，读取 URL、请求方法、状态码、响应内容；
2. 自动过滤静态文件、白名单路径、3xx/404 无效响应，减少噪声；
3. 从 HTML/JS 中提取接口路径，存入本地 SQLite 数据库；
4. 调用指纹规则匹配敏感信息，在界面标记结果，方便人工复核。

整体模块分工明确，Proxy 监听、路径提取、任务调度、指纹识别、结果存储各司其职，运行稳定不卡顿。

**5 分钟快速上手，零门槛即用**

### 1. 下载插件

前往项目 GitHub Releases 页面，直接下载编译好的 jar 包，要求 JDK 9 + 环境，新版 Burp 直接兼容。项目地址：https://github.com/shuanx/BurpAPIFinder

### 2. Burp 加载插件

打开 Burp Suite → Extensions → Installed → Add → Java → 选择下载的 BurpAPIFinder jar 包，加载成功后会出现专属标签页。

### 3. 开始自动扫描

浏览器配置 Burp 代理，正常访问目标站点，插件自动监听流量、提取接口、识别敏感信息，全程无需手动操作。

### 4. 查看与筛选结果

主界面展示请求总数、JS 解析成功数等数据，通过筛选按钮快速定位重点接口与敏感内容，人工验证效率翻倍。

### 5. 自定义配置（可选）

在配置页调整敏感关键词、开启主动探测、设置自定义父路径；旧版本升级需删除同目录下 BurpAPIFinder.db 和 finger-tmp.json，避免冲突。

### 6. 手动编译（可选）

喜欢折腾的朋友可拉取源码，用 Maven 一键打包：

```
git clone https://github.com/shuanx/BurpAPIFinder.gitcd BurpAPIFindermvn package
```

**四大实战场景，渗透测试必备**

### 1. 前端接口资产梳理

访问首页、登录页、管理页，插件自动整理 JS 中所有接口路径，快速完成资产面摸底，不用手动复制粘贴。

### 2. 敏感信息泄漏排查

一键扫描响应包，精准定位账号、密码、云密钥、凭证、身份证等敏感数据，排查泄漏漏洞快准狠。

### 3. JS 路径智能补全

针对 /api、/api/v1 等网关前缀，自动拼接路径重试，轻松找到常规扫描遗漏的版本化接口。

### 4. 授权接口未授权检测

配置凭证后自动复测，快速发现匿名访问受限、带凭证可获取数据的未授权 / 越权漏洞。

**写在最后**

Burp 原生流量视图只记录请求，而 BurpAPIFinder 完美补齐短板，把前端散落的接口和敏感线索全部收拢，转化为可筛选、可复测的清晰结果。

如果你还在手动翻 JS、试接口，这款插件绝对能让你的渗透测试效率直接翻倍，攻防演练、内网自查、靶场练习都能用得上。

最后提醒：本工具仅用于授权测试与安全自查，请勿用于非法攻击，合规使用，人人有责！

**下载地址**

**点击下方名片进入公众号**

**回复关键字【****26****0525****】获取**下载链接****

---

**知 识 星 球**

星球已过800人，暂不再发放优惠券，如还有需要的师傅可加我VX：**S\_3had0w，**等你一起来学习**...！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/79gZQNibQ6ucZmnEM4ic7BNGMGr4B0qcmNL0s67Upd0MjN2OS0GomjDySCNHCb9ONP8Bqrt98luYMEkt8BVsn4Tg/640?wx_fmt=jpeg&from=appmsg)

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 限时免费 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

|  |  |
| --- | --- |
|  |  |

往期推荐工具

[红队必备：不进系统，扒光虚拟机所有密码](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493081&idx=1&sn=5b6d531e21f4d4c7e5f3f99547e13ca2&scene=21#wechat_redirect)

[微信小程序捡洞神器：自动反编译+扫密钥](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493056&idx=1&sn=8b89bb66e8f0e141149cf8803a8fd953&scene=21#wechat_redirect)

[Everything 这两大新功能太牛了！](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493019&idx=1&sn=5133b5ccc33c4e5d463dc62d758231fb&scene=21#wechat_redirect)

[把AI大脑装进BurpSuite，自动挖洞来了！](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493002&idx=1&sn=5d6c6773aa3e5c7e2402f71ad5a88d19&scene=21#wechat_redirect)

[高级WebShell管理与后渗透神器](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492971&idx=1&sn=431cbbda7d6da109c86dd2c9254b0ed1&scene=21#wechat_redirect)

[263+上传漏洞检测与绕过工具](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492915&idx=1&sn=156543f9b79e9cde446cd8bae695ee43&scene=21#wechat_redirect)

[ProxyBridge (Proxifier替代工具)](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492808&idx=1&sn=139b4696d1d90983b55c3d8ef139a831&scene=21#wechat_redirect)

[基佬的"自动化"渗透测试扫描工具](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492716&idx=1&sn=a9b49b3ddf8da8f73008d36764b4eddf&scene=21#wechat_redirect)

[最好用的下一代目录爆破工具](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492620&idx=1&sn=b3f78bc0af5e231ea4cae18b381b8afa&scene=21#wechat_redirect)

预览时标签不可点

作者提示: 内容由AI生成

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/79gZQNibQ6udVsppUXB8icSrqs3DgXGQmtNTUU8UDwxIvyu0V7s0jZy28sf6rLNTHviad1N9qQicqsibACs6YRQwdhw/0?wx_fmt=png)

Hack分享吧

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/79gZQNibQ6udVsppUXB8icSrqs3DgXGQmtNTUU8UDwxIvyu0V7s0jZy28sf6rLNTHviad1N9qQicqsibACs6YRQwdhw/0?wx_fmt=png)

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