---
title: 漏洞复现 | 用友NC ServletForESBAdaptor 反序列化RCE漏洞
url: https://mp.weixin.qq.com/s/76vg9O1K5kr0dynaOgEacA
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:03:56.470540
---

# 漏洞复现 | 用友NC ServletForESBAdaptor 反序列化RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yIciaKAicYtorVwngy7NJvDcM10Jiavn2j7J4w46f37aybEGJicVGiaz1N9NgwDkvWZtAf96f2Fvqv8o4bpf5VVLnvicwiae7bFQn3rsJA1ia6qEEZE/0?wx_fmt=jpeg)

# 漏洞复现 | 用友NC ServletForESBAdaptor 反序列化RCE漏洞

实战安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

|  |
| --- |
| 本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！ |

1

**漏洞描述**

用友NC ServletForESBAdaptor 反序列化RCE漏洞，未经身份攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个 web 服务器。

2

**影响版本**

用友-UFIDA-NC

3

**测绘语法**

fofa语法

```
app="用友-UFIDA-NC"
```

![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtopRlpjXaVVnsS709XP74JH0uXcNuJt30BhHLGYM58jxqhpcmIO3ZWArgXkdUlVgXuq5vDTicYicSWkPZunicS899OpfP3dOZxMDY0/640?wx_fmt=png&from=appmsg)

4

**漏洞复现**

执行命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtoqqvera1WhUOgiawjxSfqlibeHVyib4J0hTI1qOmolkiaSI47icfItGVfS8VRicEQhNtCH6aDy85QyZiau9OBUDzXrk1zfZolibVtvvcia4/640?wx_fmt=png&from=appmsg)

5

**检测POC**

nuclei

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtormeBfHvAngicy1aJdB2xXeNxEpiaTDVRcoITSZicunsDYH01aE1Dx0mLXc5s8m4lslIqD0TeyJ9ItHg8Ynw0mGibPf7RicXayxzeUQ/640?wx_fmt=png&from=appmsg)

afrog

![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtoqJA0Cf2AYgIehMDZRzEx58yAmEnrgXfR6PibG70Rd7Zib1QqsciaOGHp5w6QvLhxJC37PdqzrIibZxtXEfW4VTxp4ZUAtaI4DicLZ8/640?wx_fmt=png&from=appmsg)

6

**漏洞修复**

1、建议联系厂商打补丁或升级版本。

2、增加Web应用防火墙防护。

3、关闭互联网暴露面或接口设置访问权限。

7

**内部圈子**

**现在已更新POC数量 2300+（中危以上）**

🔥 **1day/Nday 漏洞实战圈上线** 🔥

还在到处找公开漏洞 POC？

这里专注整合全网公开1day/Nday漏洞POC和复现，一站式解决你的痛点！

🔍 圈子福利

✅ 整合全网 1day/Nday 漏洞POC，附带复现步骤，新手也能快速上手

✅ 每周更新 7-15 个POC测试脚本，经过实测验证，到手就能用

✅ 完美适配 Nuclei/Afrog 扫描工具，脚本无需额外修改，即拿即用

✅ 重磅福利：免费 FOFA 高级会员查询，无需账号也能高效资产测绘

✅ 专属权益：提供指纹识别库，指纹库持续更新

💡 适合对象

渗透测试🔹攻防演练🔹安全运维🔹企业自查🔹SRC漏洞挖掘

⚠️ 重要提醒

仅限授权范围内的合法安全测试，严禁用于未授权攻击行为！

本服务为虚拟资源服务，一经购买概不退款，请按需谨慎购买！

目前圈子已满150人，价格由64.9调整为66.9元（交个朋友啦），200人后调整为69.9元。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yIciaKAicYtoq2m23RRtN5eeDmvVrDbu9WiaNSNHQXQKICfd9ibekFKRXyrRibCKEU5ULmDCwsicOG1Dk4FAqvQ7R2M3KhUEsiapLLUQQj3nZ8v9QQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF11icZP3IFHQ3V3ayPqKCuRxbljuSc8zianApHibibJQzEG3qXvkW76uWBjvYrGNTZOmcvXTl5K8ely0g/0?wx_fmt=png)

实战安全研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF11icZP3IFHQ3V3ayPqKCuRxbljuSc8zianApHibibJQzEG3qXvkW76uWBjvYrGNTZOmcvXTl5K8ely0g/0?wx_fmt=png)

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