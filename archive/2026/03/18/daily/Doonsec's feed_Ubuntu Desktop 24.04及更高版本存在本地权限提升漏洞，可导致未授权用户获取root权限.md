---
title: Ubuntu Desktop 24.04及更高版本存在本地权限提升漏洞，可导致未授权用户获取root权限
url: https://mp.weixin.qq.com/s/K2XGRMr0VeG3o-L46fOnhQ
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:50.468006
---

# Ubuntu Desktop 24.04及更高版本存在本地权限提升漏洞，可导致未授权用户获取root权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnulSxcbgwD4jFwUH29ib0prnpOCJmXWBZUtDDBLdn3hib9jUub78HITHxvc61BdRTZjrZmibJicy2vMzIrnRxeObcK3rFj3WC464oU/0?wx_fmt=jpeg)

# Ubuntu Desktop 24.04及更高版本存在本地权限提升漏洞，可导致未授权用户获取root权限

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnt2ua2LnloIHUjCzkuUPzWZsqIDJbiaicm39vWB7QcSlVr6fGJuiaPVleG0vPbeI9Z1UP4CrBibKY9GLkNa0n6JAHiclgYBnESL1rGg/640?wx_fmt=jpeg&from=appmsg)

**默认安装的Ubuntu Desktop 24.04及更高版本中存在一个本地权限提升(LPE)漏洞**，允许未授权的本地攻击者获取完整的root访问权限。

## 漏洞基本信息

* **漏洞编号**：CVE-2026-3888
* **发现者**：Qualys威胁研究部门(The Qualys Threat Research Unit)
* **影响范围**：Ubuntu Desktop 24.04及更高版本的默认安装
* **漏洞性质**：通过**snap-confine**和**systemd-tmpfiles**两个标准系统组件之间的意外交互实现权限提升

## 系统组件解析

### 1. snapd服务

* Ubuntu的**后台服务**，负责管理snap软件包（包含自身依赖的自包含应用程序包）
* 不仅是软件包管理器，还**强制执行权限模型**，控制每个snap对主机的访问权限
* 本质上是**软件包管理器与安全策略引擎**的结合体

### 2. 漏洞核心组件

* **snap-confine**：以root权限运行的setuid二进制文件，负责在应用程序执行前构建snap沙箱

+ 处理**挂载命名空间隔离**、**cgroup强制执行**、**AppArmor策略加载**和**seccomp过滤**
+ 构成完整的**沙箱限制堆栈**，确保snap应用程序在其边界内运行

* **systemd-tmpfiles**：管理**/tmp**、**/run**和**/var/tmp**等临时目录

+ 在系统启动时创建这些目录，并按计划清除过期文件
+ **配置不当或可预测的清理周期**可能打开符号链接竞争窗口，导致本地权限提升

## 漏洞技术分析

### 1. 漏洞评分与攻击条件

* **CVSS v3.1评分**：7.8（高危）
* **攻击向量**：AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H

+ 需要**本地访问**和**低权限**
+ **无需用户交互**
+ 产生**范围变更**，意味着成功利用会影响漏洞组件之外的资源
+ 对**机密性**、**完整性**和**可用性**均有高影响

### 2. 攻击复杂性与时间机制

* **高攻击复杂性**源于漏洞链中固有的**时间延迟机制**
* 默认情况下，systemd-tmpfiles被安排在以下时间后删除/tmp中的过期数据：

+ Ubuntu 24.04：**30天后**
+ 更高版本：**10天后**

### 3. 攻击三阶段流程

1. **等待阶段**：攻击者等待清理守护进程删除**/tmp/.snap**（snap-confine在沙箱初始化期间使用的关键目录）
2. **准备阶段**：删除后，攻击者**重新创建/tmp/.snap**并填充恶意负载
3. **利用阶段**：在下一次沙箱初始化时，snap-confine以**root权限绑定挂载**这些文件，从而在**特权上下文中执行任意代码**，实现**完整主机控制**

## 修复建议与受影响版本

### 紧急升级指南

表格

| Ubuntu版本 | 易受攻击的snapd | 修复版本 |
| --- | --- | --- |
| Ubuntu 24.04 LTS | 低于2.73+ubuntu24.04.1 | 2.73+ubuntu24.04.1 |
| Ubuntu 25.10 | 低于2.73+ubuntu25.10.1 | 2.73+ubuntu25.10.1 |
| Ubuntu 26.04 LTS (开发版) | 低于2.74.1+ubuntu26.04.1 | 2.74.1+ubuntu26.04.1 |
| 上游snapd | 低于2.75 | 2.75 |

### 旧版系统说明

* **Ubuntu 16.04–22.04 LTS**在默认配置下**不受影响**
* 但Qualys建议**应用补丁**作为预防措施，因为非默认设置可能表现出类似新版本的行为

## 相关安全问题：uutils coreutils漏洞

在Ubuntu 25.10发布前的安全审查中，Qualys TRU发现了**uutils coreutils包**（标准GNU工具的Rust重写版）中的一个竞争条件漏洞：

* **漏洞位置**：rm实用程序
* **攻击方式**：允许未授权的本地攻击者在**root拥有的cron执行期间**将目录条目替换为符号链接
* **主要目标**：/etc/cron.daily/apport
* **潜在影响**：

+ 以**root权限删除任意文件**
+ 通过针对snap沙箱目录实现**进一步权限提升**

### 修复措施

* Ubuntu安全团队在**公开发布前**通过将Ubuntu 25.10中的默认rm命令恢复为GNU coreutils来缓解风险
* 上游修复已应用于**uutils仓库**

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