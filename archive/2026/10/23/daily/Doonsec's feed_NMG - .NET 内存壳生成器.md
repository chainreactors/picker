---
title: NMG - .NET 内存壳生成器
url: https://mp.weixin.qq.com/s/G7XDZ5M9k7HbvtsTzocRwA
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:46.539870
---

# NMG - .NET 内存壳生成器

# NMG - .NET 内存壳生成器

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本文所涉及的技术、思路和工具仅用于本地靶场安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，请务必在获得明确书面授权的环境下使用，并遵守相关法律法规，一切后果由使用者自行承担！！

项目介绍

   NMG 生成参数化的 .NET 内存壳负载，注入 IIS/ASP.NET 应用程序且不留文件于磁盘。注入后，你连接现有的webshell管理器（Godzilla / Behinder / AntSword）——NMG只是让服务器端工作。

可以这样理解：输入参数 -> 编译的负载 -> 注入 -> 连接客户端

```
+-----------------------------------------------------+|                    nmg.exe (CLI)                     |+------------------------+----------------------------+|  generate (payload)    |  probe (env detection)     |+------------------------+----------------------------+|                  Protocol Layer                      ||  +----------+  +----------+  +----------+           ||  | Godzilla |  | Behinder |  | AntSword |           ||  | AES-128  |  | AES-128  |  | Base64   |           ||  +----------+  +----------+  +----------+           |+------------------------------------------------------+|               Template Layer                         ||  +----------+  +----------+  +--------------+       ||  |   VPP    |  |  Route   |  | HttpListener |       ||  | IIS hook |  |MVC Route |  |  Standalone  |       ||  +----------+  +----------+  +--------------+       |+------------------------------------------------------+|             Compilation Engine                       ||        Roslyn -> DLL (net40/net472)                 ||    deterministic / XOR obfuscated / randomized      |+------------------------------------------------------+|                Output Layer                          ||    aspx injector / base64 / dll                     |+------------------------------------------------------+
```

### 类型

| 类型 | 目标 | .NET 框架 | 触发点 |
| --- | --- | --- | --- |
| `vpp` | IIS/ASP.NET | 2.0+ | VirtualPathProvider.GetCacheKey |
| `route` | MVC/WebAPI | 3.5+ | RouteBase.GetRouteData |
| `httplistener` | 独立/系统 | 2.0+ | HttpListener（独立于 IIS） |

### 协议

| 协议 | 客户 | 加密 | 已验证 |
| --- | --- | --- | --- |
| `godzilla` | 哥斯拉4.x | AES-128（key=MD5（pass+key）[0：16]） | ✅ 端到端 |
| `behinder` | 4.x 之后 | AES-128（键=MD5（传递）[0：16] 原始字节） | ✅ 端到端 |
| `antsword` | 蚁剑 | Base64 | ✅ 端到端 |

GitHub地址：

```
https://github.com/baguette168/nmg
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满400人，欢迎各位进圈子交流学习！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQXm0N3QQT1byMjhzMvPx3RqYswWyvlOTqPbxMWYiawjx8h7EJwTTDrE5Wp4CytmjG2dYtIGjAJMCSicXoY1N8nOcFE2a0oqNwWnE/640?wx_fmt=jpeg&from=appmsg)

****圈子目前更新相关技术文章：****

************* HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* HeBypassAV内部版Patch免杀工具-轻松绕过杀软EDR
* Heavenly自动化红队后渗透工具免杀生成器
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* Heavenly专版Linux免杀工具
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass免杀AV
* Frp免杀隧道工具
* 1day和0dayPOC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队工具文章！期待您的加入！！！**********

**往期推荐**

**********[安全天书免杀课来袭｜助力实战免杀钓鱼(文末送福利)](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485167&idx=1&sn=7ab4393e75cf94d13cb79e22b92fb8d0&scene=21#wechat_redirect)**

**[【红队工具】攻防后渗透工具自动化免杀！！！](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485305&idx=1&sn=3b4c50d0f88a753089767db5304b6626&scene=21#wechat_redirect)**

**[【红队工具】红队内网后渗透CobaltStrike插件更新](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485006&idx=1&sn=e3bcf2070226fcfc93b565ae2c9d85ad&scene=21#wechat_redirect)**

**[免杀更新--Heavenly自动化生成白加黑3.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485679&idx=1&sn=991c111e2627ec8835dc13b8bc919eb3&scene=21#wechat_redirect)**

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)**************

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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