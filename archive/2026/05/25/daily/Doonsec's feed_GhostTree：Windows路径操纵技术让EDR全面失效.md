---
title: GhostTree：Windows路径操纵技术让EDR全面失效
url: https://mp.weixin.qq.com/s/GP1Xt_rQmoBzowgh1UUndA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:30.068259
---

# GhostTree：Windows路径操纵技术让EDR全面失效

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Pt7xmiaibuWXSLlAibb862ibhGWuJDL5aSG5x5UGYiaQCxALAP7MqbMh7vfRxT7SyjRnsgzmB4tBjZfLgOpXKUydzK1wz80I3VbeicA/0?wx_fmt=jpeg)

# GhostTree：Windows路径操纵技术让EDR全面失效

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Nfy04C0rQr3wOibQzSguYsqbT0atxCb9OpMMjuwZ5GVHszAshOicquPVKM2sFDmD4KfsXCT0tGzINtG6BHHzuYXHJ3enw4LKGBM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617500&idx=1&sn=73c0634d23ef9a5a7ca009cf0e3b1929&scene=21#wechat_redirect)

> **导语**：大多数安全团队认为NTFS连接点和符号链接只是小众的文件系统功能。然而安全研究人员的最新发现证明，通过巧妙的路径构造，任何普通用户都可以创建递归循环，让EDR的文件夹扫描功能陷入死循环——恶意文件就此消失于无形。

## 一、NTFS连接点基础知识

在深入GhostTree之前，我们需要了解NTFS的两种重解析点（Reparse Point）：

**符号链接（Symbolic Link）**：可以指向文件或目录，跨越卷操作 **连接点（Junction）**：仅可指向目录，本卷内操作

这两种功能都是Windows为兼容性和灵活性而设计的，正常情况下需要管理员权限才能创建——但有一个例外：**用户创建的连接点不需要特殊权限**，只需要目标文件夹的写权限。

## 二、GhostBranch：基础的单点循环

### 2.1 原理

GhostBranch是GhostTree的基础技术。它的核心思想非常简单：

```
# 创建子文件夹
mkdir C:\test\child

# 将child指向其父文件夹C:\test
mklink /J C:\test\child C:\test
```

结果是什么？`C:\test\child`既是`C:\test`的子文件夹，又指向`C:\test`本身。这创建了一个逻辑循环。

### 2.2 路径爆炸效果

通过这个结构，可以生成无限多的有效路径：

```
C:\test\child\child\child\...
C:\test\child\child\child\child\...
```

所有这些路径都指向同一个地方——但Windows认为它们都是有效的。

## 三、GhostTree：二叉树结构的路径迷宫

GhostTree在GhostBranch的基础上引入多个子文件夹，产生指数级的路径爆炸：

### 3.1 创建方法

```
# 创建两个子文件夹
mkdir C:\parent\P
mkdir C:\parent\B

# 将它们都指向父文件夹
mklink /J C:\parent\P C:\parent
mklink /J C:\parent\B C:\parent
```

### 3.2 路径多样性

现在每一层路径可以在"P"和"B"之间选择：

```
C:\parent\P\P\P\P...
C:\parent\B\B\B\B...
C:\parent\P\B\P\B...
```

随着路径增长，可能的路径数量呈指数增长：

**数学计算**：

* 单层最大深度约126个文件夹（受路径长度限制）
* 每层2种选择（P或B）
* 总路径数 = 2^126 ≈ 8.5×10^18

这个数字已经超过地球上沙粒的总数。

## 四、为什么这能绕过EDR？

### 4.1 EDR的扫描机制

现代EDR产品普遍使用文件夹扫描作为恶意软件检测手段之一。当EDR安装时，它会扫描系统中的关键文件夹，寻找已知的恶意文件特征。

### 4.2 遭遇GhostTree的场景

假设攻击者：

1. 在某文件夹中放置恶意软件
2. 创建GhostTree结构
3. 当EDR尝试递归扫描该文件夹时...

EDR会陷入无限递归，因为每进入一层，理论上都有两个新的子文件夹，而它们都循环回父文件夹。实际扫描会达到Windows路径长度限制（约260字符），但此时已经扫描了亿亿计的"假"路径。

**结果**：扫描永远无法完成，恶意文件从未被检测。

## 五、实测效果

安全研究人员测试了GhostTree对Windows Defender的影响：

```
# 创建一个GhostTree结构
mkdir C:\malicious\P
mkdir C:\malicious\B
mklink /J C:\malicious\P C:\malicious
mklink /J C:\malicious\B C:\malicious

# 放置恶意软件
copy malware.exe C:\malicious\
```

使用Windows Defender进行文件夹扫描时，系统会陷入长时间的扫描状态，最终超时——恶意文件保持未检测状态。

## 六、Microsoft回应

研究人员向微软报告了这一问题。微软的回应是：

> "绕过高德纳终端防御不是跨越安全边界"

换句话说，微软认为这只是"规避检测"而非真正的安全漏洞，因此不予修复。这与微软对"边界内"攻击的传统定义一致。

不过研究人员指出，这种技术确实可以被用于实际的攻击场景，不仅仅是"检测规避"。

## 七、检测与防御建议

### 7.1 监控junction创建

安全团队应该在SIEM中创建规则，监控异常数量的连接点创建：

```
# 监控 Junction 创建的 PowerShell 脚本
Get-WinEvent -FilterHashtable @{LogName="Security";ID=4657} |
    Where-Object {$_.Message -match "mklink"} |
    Select-Object TimeCreated, ProcessName, TargetName
```

### 7.2 文件访问模式分析

EDR应该监控以下异常行为：

* 短时间内对同一文件的多次不同路径访问
* 递归扫描过程中的异常超时
* Junction创建事件与后续文件写入的关联

### 7.3 缓解措施

**短期**：

* 部署专门检测GhostTree的EDR规则
* 监控Junction创建事件
* 限制普通用户创建连接点的能力（通过组策略）

**长期**：

* EDR需要实现循环检测和路径规范化验证
* 微软应该考虑为连接点创建添加审核日志

## 八、攻击场景

GhostTree可以被用于：

**恶意软件持久化**：将恶意软件藏在无法被扫描的文件夹中

**数据外泄掩护**：在大量假路径中混入真实的外泄通道

**后门隐藏**：让后门文件完全逃脱AV/EDR的文件夹扫描

## 九、总结

GhostTree是一个巧妙利用Windows文件系统特性的攻击技术。它不依赖任何漏洞利用，而是"合理使用"系统的已有功能。这种"设计内"的攻击往往更难防御，因为微软可以辩称这是"按预期工作"。

对于安全团队而言，这意味着需要从单纯的签名扫描转向更智能的行为分析和异常检测。路径操纵技术再次提醒我们：防御不是简单地建立规则，而是要理解攻击者的思维方式。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MkQ9uQgrplJ1VM22B3ibaib5I7E66cFThF5gcSHUiblD0nSpyO1aMzhkpCntC7YFupvbo3uySFBYn8fIZbxn75B3DhyvyltPsta8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617065&idx=1&sn=1e30ce488590711587c29414a82b7ab8&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M6kfpWeYytyBgO0DC1jZPRU2TibWlRJC5yPHf8Nh8FJBKLXm3icia8YdibIByciaWbKLkV0QWibwFRriaDzMYEUGKF41FlImbkb4V5G8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617222&idx=2&sn=a600c58c6ac251bf0313134ad70a4fd8&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PhonibtNh9JibUEsbcxjX9iabDfmibaSZSvqdmp4Ey0apM8Ll8zRUgibCARXiaCcJPLMLLrk6Pv8AbVCclDKyy5EqOjFpGNgcDLxPbM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617751&idx=1&sn=f1c1ed68d848029fc1ff726087cac05a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MKE8UsztH3T5yt5F13tk2udcoNmLlyTbAicYiaPrFzulCbOGjcmZRwZIyyKNkCHRpktJz6LwpyyU5jHugpDSTKp1cUyRvm3Nvzo/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617464&idx=1&sn=a447b46bf211ae577eec30f82ed1d089&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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