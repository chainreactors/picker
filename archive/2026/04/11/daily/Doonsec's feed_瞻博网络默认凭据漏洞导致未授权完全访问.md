---
title: 瞻博网络默认凭据漏洞导致未授权完全访问
url: https://mp.weixin.qq.com/s/SZG_nvVa7t_WA-00T-6P9g
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:01.264277
---

# 瞻博网络默认凭据漏洞导致未授权完全访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnswGicMbicS0b1MXKegOI4JcJYNfcwuaKrWjVUr8FBU6Ac0zdiahv1H2HusDqA8TppL8BwtzxLgxGiaIUYwIFdtticAsU2o6gxUOghg/0?wx_fmt=jpeg)

# 瞻博网络默认凭据漏洞导致未授权完全访问

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJntIBLPQucXbRd1Yd6yGEgX0DPf0nibQYxaZsyG2gynFhBSibJmvmjjLu1sSJR2erpjWbTPF4c4AfJcaJkiayH2JsuCpguaicRFcXq8/640?wx_fmt=png&from=appmsg)

瞻博网络近日发布了一则严重安全警告，指出其Support Insights（JSI）虚拟轻量级收集器（vLWC）存在一个高危漏洞。

这个被标记为CVE-2026-33784的漏洞源于默认密码设置问题，CVSS v3.1评分高达9.8分，几乎达到最高危险等级。如果不及时修复，远程攻击者无需任何身份验证就能完全掌控受影响的网络设备。

问题出在vLWC软件的初始配置环节。当企业部署新的vLWC软件时，系统会自带一个高权限账户的默认密码。更严重的是，设备在初次使用时并不会强制要求管理员更改这个预设密码。

这就意味着，只要攻击者和设备在同一个网络中，就能用这个众所周知的默认密码轻松突破安全防线。一旦成功登录，攻击者就能获得最高权限，不仅可以随意修改系统设置、窃取数据，还能以此为跳板进一步入侵企业内网的其他设备。

**影响范围与应对措施**

这个漏洞的危险性在于攻击门槛极低——不需要特殊技术，也不需要用户配合，只要能连上网络就能登录。因此安全团队必须高度重视。

具体来看：

* 受影响版本：所有3.0.94之前的vLWC软件版本
* 严重程度：CVSS v3.1评分9.8，CVSS v4.0评分9.3
* 内部编号：JDEF-1032
* 发现过程：瞻博内部安全测试时发现
* 当前状况：暂未发现野外实际攻击案例

瞻博网络强烈建议管理员尽快将vLWC软件升级到3.0.94或更高版本，这是彻底解决问题的唯一方法。新版本已经改进了初始密码设置流程。

如果暂时无法升级，也有临时解决方案：管理员只需登录设备设置界面，通过JSI Shell手动修改默认密码。只要换成强度足够、独一无二的新密码，就能有效阻止未授权访问，为后续正式修复争取时间。

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