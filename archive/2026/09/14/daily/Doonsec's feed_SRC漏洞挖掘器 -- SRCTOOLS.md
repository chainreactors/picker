---
title: SRC漏洞挖掘器 -- SRCTOOLS
url: https://mp.weixin.qq.com/s/p9As2jhdwPhJYhvxsDsidw
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:01:38.514724
---

# SRC漏洞挖掘器 -- SRCTOOLS

# SRC漏洞挖掘器 -- SRCTOOLS

99-sketch
99-sketch

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

针对教育行业漏洞平台 / 高校 SRC 的公益挖洞自动化工具，集成全国高校， 支持选校后自动执行「资产收集 → 漏洞挖掘 → 复测」全流程，产出一键缓存管理的精准渗透报告。

⚠️ 合规声明：本工具仅用于获得授权的公益安全研究。 教育网（edu.cn）资产受 CERNET 等机构管理，请在平台授权范围内、遵循负责任披露原则使用。 未经授权对任何目标进行测试属于违法行为，后果自负。

```
核心设计原则（重要）：本工具宁可漏报、不可误报。被动泄露：漏洞必须附带 HTTP 200 响应体真实证据（源码/配置/备份内容）才算真漏洞； 服务器返回 5xx/4xx（如 502 Bad Gateway）一律判定为误报剔除，绝不进入报告。主动注入：SQLi/XSS/路径穿越/开放重定向必须提供基线-注入差分证据链（报错签名、 AND 1=1/1=2 布尔差分、payload 原样反射、/etc/passwd 真实内容、Location 携带签名域）才判 confirmed； 只做只读·最小影响验证，不写库、不删改、不执行RCE。Nday特征：Shiro deleteMe / Actuator 暴露 / 反序列化入口均为无害行为探测得出的真实特征。robots.txt 可访问不属于漏洞，仅作信息收集。
```

**0x02 安装与使用**

可视化 GUI 软件（推荐，双击即用）

教育SRC挖洞工具.exe（约91MB，图形界面软件，全功能内置）

双击即打开图形窗口，无需命令提示符、无需 Python、无任何伴随文件：

顶部：搜索目标学校（如 北京、zju、清华），下拉选择

中部按钮：①资产收集 → ②漏洞挖掘 → ③复测 → ④生成报告，以及 ▶一键全流程、■停止

多标签页实时展示：资产（子域名/存活）、漏洞发现、Nday线索、运行日志、报告管理

报告管理页：报告自动缓存登记，支持刷新/查看内容/打开/重命名/删除，双击即可查看

底部进度条与阶段状态，■停止 可随时中止

单文件，双击即用。全程图形化，无需命令行。

结果固定写 outputs\ 目录（不写C盘）。

报告生成后自动登记进「报告管理」，可随时查看/打开/删除。

网盘下载链接（一定要在虚拟机运行）：

```
后台回复：20260914获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_jpg/U7LDNXUGXQvRM7omc2ES2NSLMZ2Nbib7VftC67uHpXxKTZqyibjeicgibLRzg0Xiao8B2x6JB25gOIdKTSwHD3F28Ek94lQmlM9E8xkAHvRjrLHw/640?wx_fmt=jpeg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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