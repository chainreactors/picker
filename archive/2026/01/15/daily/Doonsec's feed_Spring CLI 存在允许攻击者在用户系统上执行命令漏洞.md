---
title: Spring CLI 存在允许攻击者在用户系统上执行命令漏洞
url: https://mp.weixin.qq.com/s/Q5i060kLY4LYTw4GB2NKag
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:22.653434
---

# Spring CLI 存在允许攻击者在用户系统上执行命令漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo4tv2I8icIGyC9JYH01gxjPlxbfJHKDybYDlxqofYrLtjhNHkQd8icuQF4ybAMVdu4DC8xLYGmMumxw/0?wx_fmt=jpeg)

# Spring CLI 存在允许攻击者在用户系统上执行命令漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo4tv2I8icIGyC9JYH01gxjPlRaveYiczpdgosmcxnia0UZMfMiaZyCmOUW0mlte1gajJ13KNJLZdIxQKA/640?wx_fmt=jpeg&from=appmsg)

Spring CLI VSCode扩展存在**命令注入漏洞**，攻击者可利用该漏洞在目标系统上执行任意命令。该漏洞被追踪为CVE-2026-22718，影响所有0.9.0及更早版本（均已结束生命周期）。

| 漏洞编号 | CVE-2026-22718 |
| --- | --- |
| 组件名称 | Spring CLI VSCode扩展 |
| 漏洞类型 | 命令注入（Command Injection） |
| CVSS评分 | 6.8（AV:L/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:L） |
| 严重等级 | Medium |
| 攻击条件 | 本地访问 + 用户交互 |
| 影响范围 | 所有0.9.0及更早版本 |

### 1. 漏洞原理

攻击者通过以下方式触发漏洞：

1. 诱导开发者在VSCode中执行恶意构造的Spring CLI命令
2. 利用扩展未正确过滤特殊字符（如`;`、`&`、`|`）的缺陷
3. 在目标系统上执行任意Shell命令

### 2. 攻击场景

* **初始访问**：需已具备本地系统访问权限（如共享开发环境）
* **漏洞利用**：通过诱导用户执行特制命令（如`spring init --dependencies=web;rm -rf /`）
* **执行权限**：继承当前用户权限（通常为开发者账户）
* **持久化**：修改`.bashrc`或VSCode扩展配置文件实现后门植入

## 受影响版本及修复方案

### 官方声明：

该扩展已于**2025年5月14日结束生命周期**（EOL），不再提供安全更新。Spring团队仍为此漏洞分配CVE编号，旨在提醒用户及时移除旧版工具。

| 扩展版本 | 修复建议 |
| --- | --- |
| ≤ 0.9.0 | **立即卸载**（无可用补丁） |

## 防御建议

* **强制卸载**：通过配置管理工具（如Ansible、SCCM）批量移除扩展
* **环境审计**：检查CI/CD流水线中的VSCode镜像是否包含该扩展
* **权限管控**：限制开发人员对系统级配置文件的修改权限

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