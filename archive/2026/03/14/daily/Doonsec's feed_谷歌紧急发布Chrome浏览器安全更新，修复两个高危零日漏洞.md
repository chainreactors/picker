---
title: 谷歌紧急发布Chrome浏览器安全更新，修复两个高危零日漏洞
url: https://mp.weixin.qq.com/s/IHweiTB_-tjD45pb5OzzmA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:26:01.746561
---

# 谷歌紧急发布Chrome浏览器安全更新，修复两个高危零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnsouFomYYnPiaNzer3aGrAc6k461s8lAr1BVMItANT2113JabKxj0CWKORJ4wFzkH01owRSibndn9ZM0z3cibPiaxYYibtTp48p53N0/0?wx_fmt=jpeg)

# 谷歌紧急发布Chrome浏览器安全更新，修复两个高危零日漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnsT82LQMWT1NeN15J9Rf7zaRDlZ2ouictvg7eWJYzr7EEZQgdfIhGoo1xOPxFqzXHsKrjs1LqHrstOAcicBE7ibicQqibaJ8mFN6KK0/640?wx_fmt=jpeg&from=appmsg)

**谷歌已为其Chrome浏览器发布紧急安全更新**，此前确认两个高严重性零日漏洞正在野外被积极利用。

## 更新版本信息

* **Windows和macOS平台**：146.0.7680.75/76版本
* **Linux平台**：146.0.7680.75版本
* **推送时间**：预计在未来几天到几周内完成用户更新

## 漏洞详情

### 1. CVE-2026-3909：Skia中的越界写入漏洞

* **漏洞位置**：Skia（Chrome渲染管线的开源2D图形引擎）
* **风险等级**：高严重性
* **技术影响**：

+ 允许攻击者**覆盖相邻内存区域**
+ 可能导致**任意代码执行或应用程序崩溃**
+ 在浏览器环境中可被利用来**逃逸沙箱保护**，在受害者系统上执行恶意代码

### 2. CVE-2026-3910：V8中的不当实现漏洞

* **漏洞位置**：V8（Chrome的高性能JavaScript和WebAssembly引擎）
* **风险等级**：高严重性
* **技术影响**：

+ 攻击者可**创建恶意网页**，用户访问后触发漏洞
+ 可在**浏览器进程上下文中执行恶意代码**
+ 由于JavaScript在正常浏览中不断执行，**利用机会丰富**

## 重要安全声明

* **漏洞发现时间**：2026年3月10日（由谷歌安全团队内部报告）
* **当前状态**：谷歌已**明确确认**这两个漏洞的利用代码已在野外存在
* **技术细节限制**：相关技术细节和错误跟踪条目将保持限制，直到相当一部分用户应用补丁，以防止进一步利用

## 紧急缓解措施

### 个人用户操作指南

1. **手动触发更新**：

* 打开Chrome并导航至 **菜单 → 帮助 → 关于Google Chrome**
* Chrome将**自动检查并应用**最新更新
* **重启浏览器**以完成安装

### 企业用户建议

* **优先级**：应**立即**将146.0.7680.75/76版本推送到整个环境
* **高风险环境**：**不建议**等待自动推送，应主动部署更新

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