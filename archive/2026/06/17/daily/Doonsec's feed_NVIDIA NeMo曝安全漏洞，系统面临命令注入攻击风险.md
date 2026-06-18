---
title: NVIDIA NeMo曝安全漏洞，系统面临命令注入攻击风险
url: https://mp.weixin.qq.com/s/wgnYYjGmHUnkJcV7IEafvA
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:13.737979
---

# NVIDIA NeMo曝安全漏洞，系统面临命令注入攻击风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnsJUxrVJzLJVkRz8bgnfmqljw3MQhjN7tguUVibNGVXViau1icJuu0Q0vhfhNLniaV3GgibTbfuriac9teyD5412pBRb9Ou9XDWnO4icY/0?wx_fmt=jpeg)

# NVIDIA NeMo曝安全漏洞，系统面临命令注入攻击风险

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJntOzcDykIw1C0I1ic6gRtQD8eq5AWibSGUYjkRkRng9uViaXVOmuGn1aQCju2xyClbre0zuaxCyja6BEhZZjbMbtK5nuSubPKAYq4/640?wx_fmt=png&from=appmsg)

NVIDIA披露NeMo框架存在多个高危漏洞，含可致远程代码执行的关键命令注入缺陷

NVIDIA在2026年6月安全公告中披露，其NeMo框架存在多个高危漏洞，其中最严重的命令注入漏洞（CVE-2026-24252）可能使攻击者在受影响系统上执行任意代码。该问题影响所有平台中2.7.2及更早版本的NeMo，成功利用将导致权限提升、数据篡改及敏感信息泄露。

核心漏洞风险分析

Linux系统命令注入（CVE-2026-24252）

仅影响Linux部署环境，因对用户输入处理不当，低权限攻击者无需交互即可执行任意系统命令。

考虑到NeMo广泛应用于AI模型开发及自动化部署流程，该漏洞在企业级研发环境中风险尤为突出——模型编排常涉及系统级操作脚本，攻击者可能借此突破权限边界。

跨平台代码注入漏洞（CVE-2026-24155）

归类为CWE-94类漏洞，攻击者可操控应用行为并执行恶意代码，同样导致数据篡改与信息泄露。

不安全反序列化缺陷（CVE-2026-24228）

涉及CWE-502风险，通过构造恶意数据包可能触发远程代码执行或权限提升。

关键风险特征

三项漏洞CVSS v3.1基础评分均为7.8（高危），攻击向量需本地访问权限且仅需低权限，但无需用户交互。

尽管要求本地攻击条件，但在多用户系统、共享计算环境及AI流水线中风险仍显著——此类场景通常已放宽访问控制策略，攻击者易获取初始立足点。

修复与应对建议

NVIDIA已发布NeMo 2.7.3版本修复漏洞，用户需立即从官方GitHub仓库升级。

企业应根据实际部署环境评估风险：

重点检查生产环境与共享集群的访问控制策略

审计自动化脚本中对用户输入的校验机制

对涉及系统级操作的模型编排流程实施权限最小化原则

| CVE编号 | 漏洞类型 | 核心风险 | CVSS评分 |
| --- | --- | --- | --- |
| CVE-2026-24155 | 代码注入（CWE-94） | 恶意代码执行、权限提升、数据篡改、信息泄露 | 7.8（高） |
| CVE-2026-24252 | 系统命令注入（CWE-78） | Linux系统任意命令执行 | 7.8（高） |
| CVE-2026-24228 | 不可信数据反序列化（CWE-502） | 代码执行、系统沦陷 | 7.8（高） |

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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