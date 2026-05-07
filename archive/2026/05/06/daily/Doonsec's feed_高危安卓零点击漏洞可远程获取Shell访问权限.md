---
title: 高危安卓零点击漏洞可远程获取Shell访问权限
url: https://mp.weixin.qq.com/s/BDVEi3LzN3A32-ofzXWgng
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:17.257069
---

# 高危安卓零点击漏洞可远程获取Shell访问权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnuTGOdyhOLuSEsM6GWLaHJxXjX2vibUAfWgZRmoia3eLMibtSvJYWuYdCcRnibliaricW2FPJv6SNoWcicZXstS0lQibIMRK5x4kRlqMUA/0?wx_fmt=jpeg)

# 高危安卓零点击漏洞可远程获取Shell访问权限

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnsyymFcUwficicl2HkuQsRMibMvnXKIxKzy4fpj3HVrhflDyDKxoRuKwzGibZBaCDSLtgK21t5toFTudtISpj784obxduzr0r4GxFk/640?wx_fmt=png&from=appmsg)

谷歌于2026年5月4日发布的Android安全公告重点修复了高危漏洞CVE-2026-0073，该漏洞存在于**Android调试桥守护进程（adbd）子组件**中，允许攻击者在**无需用户交互的情况下通过局域网或物理邻近位置远程获取设备shell访问权限**。此漏洞影响Android 14至16-QPR2所有版本，需立即安装**2026年5月1日或更高版本的安全补丁**以彻底修复。

---

## 一、漏洞核心信息

### 1. 漏洞详情

* **漏洞编号**：CVE-2026-0073
* **严重程度**：**高危（Critical）**，因攻击**无需用户交互或额外权限**即可触发。
* **根本原因**：adbd（Android Debug Bridge守护进程）子组件存在逻辑缺陷，导致攻击者可**绕过常规应用沙箱防护**，以`shell`用户身份执行任意代码。

### 2. 攻击条件与影响

* **攻击向量**：需与目标设备处于**同一局域网或物理邻近范围**（如公共Wi-Fi、蓝牙覆盖区域）。
* **危害范围**：

+ 攻击者可**直接执行系统级命令**，读取敏感数据或植入恶意负载。
+ **绕过Android沙箱机制**，突破应用权限隔离限制。
+ 适用于**所有依赖Project Mainline更新的现代Android设备**（Android 10及以上）。

## 二、影响范围与修复方案

### 1. 受影响设备

* **操作系统版本**：Android 14、15、16及16-QPR2。
* **关键说明**：

+ 由于adbd属于**Project Mainline模块**，漏洞修复可通过Google Play系统更新直接推送，**无需等待厂商定制ROM**。
+ 旧版本设备（Android 10以下）需依赖厂商OTA更新，风险暴露时间更长。

### 2. 修复措施

* **安全补丁级别**：必须升级至**2026-05-01或更高版本**。
* **用户自查方法**：

+ 进入设备**系统设置 → 关于手机 → 安全更新**，确认补丁日期≥2026-05-01。
+ 手动检查**Google Play系统更新**（部分设备需单独触发）。

* **企业级防护**：

+ 企业设备管理员应通过MDM工具**强制部署5月安全更新**，防范局域网攻击风险。
+ 启用**Google Play Protect**实时监控可疑行为。

## 三、技术背景补充

### 1. Project Mainline机制的作用

* **快速响应漏洞**：adbd作为Mainline模块（模块名`com.android.adbd`），可通过Google Play直接更新，**跳过传统OTA流程**。
* **模块化优势**：仅替换受损组件（APEX格式），避免完整系统升级，**降低修复延迟**。

### 2. 为何无需用户交互？

* 漏洞触发依赖adbd的**后台网络监听行为**（默认端口5555），攻击者通过构造恶意网络数据包即可触发，**无需诱导用户点击或下载文件**。

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