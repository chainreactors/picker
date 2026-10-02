---
title: MalCheck-杀毒特征分析工具
url: https://mp.weixin.qq.com/s/vfj-g6kfZUjx-y-Roie8IQ
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:43:11.240989
---

# MalCheck-杀毒特征分析工具

# MalCheck-杀毒特征分析工具

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

工具介绍

通过二分搜索精确定位触发检测的字节区域，针对真实引擎（Defender、AMSI）。为侦测工程、规则编写和紫队研究而设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVeIhuribk66YibXfR0q3icf9bVVewQH5OXgDDic33b3DvaVeh465ice9iaB4HE6EUJpPEcCxhIsx42ky50UaCHnyKP9NuHu2RJ1eU48/640?wx_fmt=png&from=appmsg)

工具原理

MalCheck 利用字**节范围的二分搜索**，针对真实的杀毒引擎来隔离最小触发区域：

```
┌─────────────────────────────────────────────────────────┐│  Full file  ──►  Detected?  ──►  YES                    ││                                                         ││  Split in half ──► Test each half ──► Narrow range      ││       │                                                 ││       ▼                                                 ││  Repeat until exact byte boundaries are found           ││       │                                                 ││       ▼                                                 ││  Signature #1: offset 0x4F1A0 – 0x4F1C8 (40 bytes)     ││  Section: .text  │  Pattern: 48 8B 05 ?? ?? ?? ??      │└─────────────────────────────────────────────────────────┘
```

**算法步骤：**

1. 将目标文件加载到内存中
2. 确认所选发动机检测到完整的样品
3. 在后缀仍触发签名开始时，二分搜索**最大可移除前缀**→
4. 二分搜索是从该起点起点的**最小后缀**，同时仍能触发签名→结束
5. 可选地对剩余字节重复此操作以找到**所有签名**

GitHub地址：

```
https://github.com/security-attack/MalCheck
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