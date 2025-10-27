---
title: 攻击技术研判 | 利用WIFI对抗虚拟机分析
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490096&idx=1&sn=3c5004f2914fff3485dfc61b4cef7e4a&chksm=c187da21f6f0533745b75595921f939efb314a877e108e63edb2f2bd1ed8d520042c92d7d4e0&scene=58&subscene=0#rd
source: M01NTeam
date: 2022-11-08
fetch_date: 2025-10-03T21:56:59.981700
---

# 攻击技术研判 | 利用WIFI对抗虚拟机分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0uRib2BWFGoIAfIiccsibfl8aeuic9nic8R8D0p8rHaZOcicyvUpqia2zNOMTCg/0?wx_fmt=jpeg)

# 攻击技术研判 | 利用WIFI对抗虚拟机分析

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0uADW94cmJOJyGbrRNY7vNPhjbWxHBefFtiaxic2ATMS6BiazSULTe98P7Q/640?wx_fmt=gif)

**情报背景**

近期，Perception Point发现了一起复杂的网络钓鱼攻击事件，该钓鱼攻击中使用了Doenerium恶意软件进行数字货币窃取和信息窃取，该恶意软件中使用了一个较为罕见的反虚拟机技术：利用WIFI对抗虚拟机，本文将对此技术进行分析。

|  |  |
| --- | --- |
| **组织名称** | 无 |
| **相关工具** | Doenerium |
| **战术标签** | 防御规避 |
| **技术标签** | 反虚拟机 反分析 |
| **情报来源** | https://perception-point.io/  doenerium-malware/ |

**01** 攻击技术分析

此次攻击过程如下：

1.制作主题为"重要Windows更新"的电子邮件进行钓鱼

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0uAzbj0nicupvzicK5IWVcLzFjx972UbPUhFn4Gj6FylfDQzm89UWG2G1w/640?wx_fmt=png)

2.在用户点击邮件中的下载后，会重定向至恶意软件网址

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0uIeXaibb4sjZpSLcnoPM3THg4xO0WbFkeG2wd87muyYA67jGtkLOZCWQ/640?wx_fmt=png)

3.下载下来的zip文件中包含了使用说明readme和伪装成Windows更新的恶意软件

4.执行恶意软件，攻击者进行信息窃取，达到攻击目的

**亮点 利用WIFI反虚拟机**

反虚拟机

恶意代码编写者经常使用反虚拟机技术用于逃避分析，检测自己是否运行在虚拟机中。当恶意代码检测到自己在虚拟机中运行，会选择执行与正常情况下不同的行为代码，比如：停止自身运行或执行正常程序功能。

WIFI信息利用

在该恶意软件中使用如下代码实现WIFI数量检测

```
if (client.config.counter.wifinetworks == 0) {
    const wifi_connections = await client.requires.systeminformation.getDynamicData();
    if (wifi_connections.wifiNetworks.length == 0) {
        result = true;
    }
}
```

WIFI作为现在人们上网常用的网络连接方式之一，一般情况下电脑都曾使用过WiFi。

检测WIFI实现反虚拟机技术有如下优点：

Windows虚拟机将所有网络连接识别为有线连接。因此，在一般情况下虚拟机中没有WiFi连接痕迹，而作为一台真实物理机，一般都曾连接过WiFi。因此有较好的区分虚拟机和真实物理机的作用，有较好的实战效果。

执行CMD命令netsh wlan show profiles,可获取本机的所有WIFI信息，具体对比入下图：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0u2FJLbtkLDvriapPb5nib514ibrHXeLaHzUbrr7GKWmP0InEOxMOAqLxbw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0u900xGhVOKXKuPgWEWQl9KA9I78Ms7w2m6HLUjfjibHVGdQ8BghfDpxA/640?wx_fmt=png)

2.该方式基于逻辑检测，而不是技术对抗，实现上比较简单，当虚拟机仿照真实环境配置WiFi时，也可以进一步修改逻辑，进行对抗。

同2可得，在譬如外连无线USB适配器至虚拟机的特殊情况下，虚拟机中还是会有WiFi连接痕迹存在。因此，该方式适合作为反虚拟机的条件之一使用或在攻防过程中继续改进使用。

**02**总结

在如今直接的技术对抗难度不断升级的情况下，攻击者往往会通过寻找真实环境与虚拟环境下的不同，寻找逻辑漏洞，进行逻辑上的对抗。逻辑对抗上实现简单，可不断改进，是反调试、反虚拟机等对抗技术的好的着落点。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0uhY1JqWUCBMYZR5UHqWUaE9TJlPpsLp4pQOjs34UBRBLfhibnu4TQNqg/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0uDiaeESTx0CJicfYUejYH3xia3ibmUtDTs9Wx24BGBb8ngCTCk0Bj1knHAw/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0umL89txvyHDndeyq8IjMyribzib1ibAO90sjP2ChjoxU0sZ8epicH6bic7Kw/640?wx_fmt=jpeg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

**往期推荐**

[攻击技术研判｜使用cdb.exe规避主机安全防御](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490039&idx=1&sn=fead1f2842b4d407c26ec54c75572fe7&chksm=c187d9e6f6f050f0c8d799b5501148e9d13f995bbdecff930d6736edb3f5965a65c58dcc9149&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0ut1FGcnfduPF90qVnianMY5Wokpe5FlDn75nsW1aLSO22HibvdibTtFtkg/640?wx_fmt=png)

[攻击技术研判 | 典型BYOVD利用与Ring0防御削弱技术研判](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247489886&idx=1&sn=a8cb6f678fc2f1163eb32527dbc06081&chksm=c187d94ff6f050592013ee9c5a004201d76f37b14aed6248cebdf0ed1d167c692f76733f91d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0ut1FGcnfduPF90qVnianMY5Wokpe5FlDn75nsW1aLSO22HibvdibTtFtkg/640?wx_fmt=png)

[攻击技术研判 | 后宏时代：PPT鼠标悬停事件的新利用](http://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247489812&idx=1&sn=00cc78f00864d47489068dffca01540a&chksm=c187d905f6f050135c4e0ea41c2770c30b1f15fd27fc4b0032576a5f0a2f0dcd40b2cc4342fd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbBtyr4jYSdMHF5K7pOFK0ut1FGcnfduPF90qVnianMY5Wokpe5FlDn75nsW1aLSO22HibvdibTtFtkg/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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