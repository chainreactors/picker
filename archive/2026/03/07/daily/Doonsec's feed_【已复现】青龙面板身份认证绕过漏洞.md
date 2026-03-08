---
title: 【已复现】青龙面板身份认证绕过漏洞
url: https://mp.weixin.qq.com/s/PfWn7dhq8__NAQU5yLQmkw
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:07:12.320886
---

# 【已复现】青龙面板身份认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5yYXmGfnscQib5etsC3Hib9g44xyyTbTlVMQ0iaEe1LTeiaMqFOgfgtIpxiaORvic5qC96WsWddXHUMRibT3zRrQNOhjtDJMS8HicAX9ubQ8lstZzLw/0?wx_fmt=jpeg)

# 【已复现】青龙面板身份认证绕过漏洞

乌雲安全

![]()

在小说阅读器中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 青龙面板身份认证绕过漏洞 | | |
| **漏洞编号** | QVD-2026-10895 | | |
| ****公开时间**** | 2026-02-27 | ****影响量级**** | 万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **9.8** |
| **威胁类型** | 身份认证绕过 | **利用可能性** | ****高**** |
| **POC状态** | **已公开** | **在野利用状态** | 已发现 |
| **EXP状态** | **已公开** | **技术细节状态** | **已公开** |
| **危害描述：**攻击者可利用该漏洞，通过发送构造的恶意请求绕过身份验证，获取系统管理员权限，并在服务器上执行任意系统命令，完全控制目标设备。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

青龙（qinglong）是一款开源的定时任务管理与脚本自动化运行平台，支持 JavaScript、Shell、Python 等多种脚本语言，常用于京东签到、自动抢购、数据爬取等场景。其提供 Web 管理界面、RESTful API 接口、脚本上传与执行、环境变量管理等功能，广泛部署于个人服务器、NAS 设备及企业内网环境中，具有较高的用户活跃度和社区支持。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复青龙面板身份认证绕过漏洞(QVD-2026-10895)，该漏洞源于青龙面板存在多个认证绕过漏洞，攻击者可通过路径大小写变体（如/API/替代/api/）绕过认证访问受保护接口，通过 /open/user/init 路径在已初始化的系统上绕过认证并重置用户凭证，从而获得未授权访问权限，并在服务器上执行任意系统命令，最终完全控制目标设备。目前该漏洞PoC和技术细节已公开。鉴于该漏洞已发现在野利用，建议客户尽快做好自查及防护。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

青龙面板（Qinglong）< v2.20.2

**>****>****>****>**

**其他受影响组件**

无

**03**

**复现情况**

目前，奇安信威胁情报中心安全研究员已成功复现青龙面板身份认证绕过漏洞(QVD-2026-10895)，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555utGmebJNd3lpMiaHWEUJibmAnRbAtKwQJcJznaXfUsNBic3qGr4piaZuMz15LtSsV9Vv8T5kKqKuqiauRohvCaJyIS7BjibeQdjnp00/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=0)

**04**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，青龙面板身份认证绕过漏洞(QVD-2026-10895)关联的国内风险资产总数为17243个，关联IP总数为7029个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555vnkXKW0TFnOzicsPDzaSvI0Dg7GdXILnH07ydvFXVcyKIX0ze8rhW4vPHxJel3PqwTZPr2EW1bhsucNr4qHiabvx3vtybo8b8K0/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

**05**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布安全补丁，请及时更新至最新版本：

青龙面板（Qinglong）>= v2.20.2

下载地址：

https://github.com/whyour/qinglong/

**06**

**参考资料**

[1]https://github.com/whyour/qinglong/pull/2935

[2]https://github.com/whyour/qinglong/pull/2941

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bMyibjv83iavx2yyhJibAziblI8R81ZMyNFzQ4wrvUIE2Ks14R3ZfGmjEwNXbCzXm5Qcwkcuxsm8pn2ibIISmRoxPLA/0?wx_fmt=png)

乌雲安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bMyibjv83iavx2yyhJibAziblI8R81ZMyNFzQ4wrvUIE2Ks14R3ZfGmjEwNXbCzXm5Qcwkcuxsm8pn2ibIISmRoxPLA/0?wx_fmt=png)

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