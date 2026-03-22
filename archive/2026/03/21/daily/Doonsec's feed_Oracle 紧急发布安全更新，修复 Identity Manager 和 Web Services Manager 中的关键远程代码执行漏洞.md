---
title: Oracle 紧急发布安全更新，修复 Identity Manager 和 Web Services Manager 中的关键远程代码执行漏洞
url: https://mp.weixin.qq.com/s/3czRaDI1lNghUxt21UIBzQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:15:38.262942
---

# Oracle 紧急发布安全更新，修复 Identity Manager 和 Web Services Manager 中的关键远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnvCFSETELiagSNvFQukJJa2sv8JzZmtn95PWWml2l4AvhouysjH1dzpW95MyoaXf1ww9Mw4z4OKxwwRqia7xkg9Fha3MkmzSNNiaQ/0?wx_fmt=jpeg)

# Oracle 紧急发布安全更新，修复 Identity Manager 和 Web Services Manager 中的关键远程代码执行漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnto4BLeffzXvy0ZBoSjfC0WcDgz9DfbWk1ibY0zfG4WicNibo9aeLSOaZSbiaj4UYGvlEB0PRzGLPAKgpAWVVTWeiceibudTiczNYmuBk/640?wx_fmt=png&from=appmsg)

Oracle 发布了一则紧急（带外）安全警报，修复一个严重的远程代码执行（RCE）漏洞 CVE-2026-21992。该漏洞影响两个广泛部署的 Fusion Middleware 组件：Oracle Identity Manager 和 Oracle Web Services Manager。

该漏洞的 CVSS 3.1 基础评分为 9.8，属于 Oracle 风险评估体系中最严重的等级之一。

CVE-2026-21992 是一个无需身份验证、可远程利用的漏洞，攻击者无需用户交互或特殊权限即可发起攻击。其攻击向量为网络，利用复杂度较低，这意味着攻击者只需通过 HTTP 访问暴露的接口，即有可能触发远程代码执行。

该漏洞在机密性（Confidentiality）、完整性（Integrity）和可用性（Availability）三个方面的影响均被评为“高”，表明一旦成功利用，攻击者可能完全控制受影响系统。

在 Oracle Identity Manager 中，漏洞存在于 REST Web Services 组件；而在 Oracle Web Services Manager 中，漏洞位于 Web Services Security 模块。

Oracle 指出，Web Services Manager 通常会与 Oracle Fusion Middleware Infrastructure 一同部署，这进一步扩大了企业环境中的潜在攻击面。

---

### 受影响版本

该漏洞影响以下产品版本：

* **Oracle Identity Manager**

  ：12.2.1.4.0、14.1.2.1.0
* **Oracle Web Services Manager**

  ：12.2.1.4.0、14.1.2.1.0

上述版本均属于 Fusion Middleware 的补丁支持范围。相关补丁文档可通过 Oracle 安全警报页面及 My Oracle Support（文档编号：KB878741）获取。

---

由于该漏洞无需认证且 CVSS 评分高达 9.8，对于部署在互联网环境中的 Oracle Fusion Middleware 系统而言，风险尤为严重。

Oracle Identity Manager 是广泛使用的身份治理平台，而 Oracle Web Services Manager 则负责 Web 服务的安全策略执行。这两个组件在大型企业和政府环境中属于关键基础设施。一旦被利用，可能导致系统完全失陷、凭据泄露，甚至在关联系统之间进行横向移动。

---

Oracle 强烈建议所有客户立即应用官方补丁。该安全警报最初发布于 2026 年 3 月 19 日，并于 3 月 20 日进行了更新，补充了额外说明。

对于仍在运行不受支持版本的组织，建议尽快升级至受支持版本。根据 Oracle 生命周期支持策略，补丁仅提供给处于 Premier Support 或 Extended Support 阶段的版本。

---

应优先修复所有对外暴露的实例，并在修复完成前，重点检查 REST Web Services 和 Web Services Security 相关 HTTP/HTTPS 接口的暴露情况。用户还可以通过 Oracle 官方安全警报门户查看完整的风险矩阵及详细的 CVE 信息。

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