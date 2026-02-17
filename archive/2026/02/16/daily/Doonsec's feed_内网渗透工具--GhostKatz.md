---
title: 内网渗透工具--GhostKatz
url: https://mp.weixin.qq.com/s/C5De4eyL0xje0w1TGG_BAQ
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:17:50.706520
---

# 内网渗透工具--GhostKatz

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQX59bRVcVdPic1ia31KAqZAuqw5kstIY8dST0niaJquH8DpsHibBko7Mv1qBYPw8Nk9yP2aiciboGu9YkTpWhoiaK3wUiagfEsW4otciabk/0?wx_fmt=jpeg)

# 内网渗透工具--GhostKatz

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

通过利用物理内存读取原语滥用签名易受攻击的驱动程序，直接从物理内存提取LSASS凭证，绕过传统用户模式检测功能。

使用：

把攻击者脚本加载到脚本管理器里。`ghostkatz.cna`

要运行 GhostKatz，请使用命令 。`ghostkatz [logonpasswords/wdigest] -prv <provider id>`

你可以在信标控制台中运行帮助命令，使用： `help ghostkatz`

```
beacon> help ghostkatzSynopsis: ghostkatz [logonpasswords/wdigest] -prv <provider id>Description:  Dump credentials from LSASS by using signed kernel drivers to read physical memory.
Examples:  ghostkatz logonpasswords -prv 1  ghostkatz wdigest
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXicQic1iaNtfLYydicgicJJuCs7bEYKL1dR5ziaEeZ9hGibfEvxuuoemI312dWKPvRHibHE3HYS0r5a2jmicUEicGcBWoXfNA0LAbicMXgic8/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/RainbowDynamix/GhostKatz
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

0x02 红蓝偶像练习生小圈子

********圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化作，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结，学习笔记以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！****

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版-轻松免杀各大杀软
* Heavenly白加黑自动化生成免杀工具
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass国内AV
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
* HeavenlyProtectionCS内部CS插件
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
* **还有更多红队思路文章！期待您的加入！！！************

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQX2oibkmZ4pqwWSbbGvgY4Q2KMXWcxalic7CPskiatPO81lbJUm1yebkpPwZCV8XLuKRiczVagwTeMNsnSBofgkC3mYoZNQCvrWh0Y/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

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