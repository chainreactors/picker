---
title: 紧急！问脉开源工具支持扫描 MinIO 敏感信息泄露漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247496054&idx=3&sn=459c362b0e7873f861960f8026e4758e&chksm=e92ce5d5de5b6cc34530cb457dfa2656c9930f0c9b7ab39156f5007750ef4e8135f7e82d2820&scene=58&subscene=0#rd
source: CT Stack 安全社区
date: 2023-04-01
fetch_date: 2025-10-04T11:22:32.668249
---

# 紧急！问脉开源工具支持扫描 MinIO 敏感信息泄露漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1HSdSibDdRfuxENEVxArribd777J40YBkqywMFnQDVrDI5iaUWia10Aia4DUX7iaEjZPIOIDpBLakpdj75vdGdzbfNYA/0?wx_fmt=jpeg)

# 紧急！问脉开源工具支持扫描 MinIO 敏感信息泄露漏洞

CT Stack 安全社区

以下文章来源于长亭百川云平台
，作者问脉团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM56bWiaa6ic0ZJu9qGoOKP5dobAVNOxcfxgial7YI8dpTLwg/0)

**长亭百川云平台**
.

百川云平台（Rivers）是长亭面向企业开放的在线安全产品服务，包含了多个安全产品，如问脉容器安全产品，关山WebShell检测产品，牧云主机安全产品，以及其他第三方安全公司提供的安全产品等。

「问脉独家」支持扫描 MinIO 敏感信息泄露漏洞（CVE-2023-28432）

## 漏洞风险

漏洞描述：在集群模式的配置下，MinIO 部分接口由于信息处理不当返回了所有的环境变量信息（包括 MINIO\_SECRET\_KEY 和 MINIO\_ROOT\_PASSWORD），从而导致敏感信息泄漏漏洞，攻击者可能通过获取到的密钥配置信息直接登陆操作 MinIO 接口。

**只有 MinIO 被配置为集群模式时才会受此漏洞影响，此漏洞的利用无需用户身份认证，官方建议所有使用集群模式配置的用户尽快升级。**

---

影响范围：MinIO RELEASE.2019-12-17T23-16-33Z <= MinIO Version < MinIO RELEASE.2023-03-20T20-16-18Z

---

官方信息：3月20日，MinIO 官方发布了安全补丁，修复了一处敏感信息泄露漏洞 CVE-2023-28432：https://github.com/minio/minio/security/advisories/GHSA-6xvq-wj2x-3h3q

## 问脉专项插件介绍

veinmind-minio 基于问脉引擎，快速识别并发现 镜像/容器 中是否存在 CVE-2023-28432 漏洞，文末阅读原文使用工具

* 快速扫描容器/镜像中的minio CVE-2023-28432风险
* 支持JSON/CLI/HTML等多种报告格式输出

兼容性

* linux/amd64
* linux/386
* linux/arm64
* linux/arm

使用命令

***./veinmind-minio scan [image/container]***

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfuxENEVxArribd777J40YBkqdOsYl4OicgL6SkTh4YMlZZmX4SicUEJZFibVDT7roxybC6nhndiaZX9vVQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfuxENEVxArribd777J40YBkqCJAVKjhdKQCibArHyZ74SLyfgaN0ze9cERvQO2UomLQ208XicWwbMSsw/640?wx_fmt=png)

**扫码添加小助手，一起学习、共同进步！**

![](https://mmbiz.qpic.cn/mmbiz_png/NtPFQib0CNabiaAiaCKn4Gj60LeAJYhtWJsgBAUnxFUV0dsqtlkOuhibUOglQKeXslRqkB3PNKbSH5BJHDLK0azkSw/640?wx_fmt=png)

---

问脉 Tools 社区版是长亭牧云团队孵化的一款开源容器安全检测工具集。目前已支持镜像/容器漏洞、逃逸风险、恶意文件、后门、敏感信息、弱口令、资产识别等扫描功能。

为了提供更优质的服务，我们同时提供商业版牧云·云原生安全平台。首推零侵入探针，采用 Agentless 方案进行部署，保证业务节点实现严格意义上的零侵入检测，让用户能够轻装上阵，轻松解决云原生安全问题。

---

👇点击阅读原文前往Github下载使用问脉工具，随手star的你最帅

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

CT Stack 安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

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