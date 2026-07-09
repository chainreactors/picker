---
title: 腾达路由器疑似出行暗藏后门，可直接获取管理员权限，暂无官方修复补丁
url: https://mp.weixin.qq.com/s/mqRa7CDWv28vwao4FrbsAQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:59:34.236795
---

# 腾达路由器疑似出行暗藏后门，可直接获取管理员权限，暂无官方修复补丁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DYqn7TU9icq29ewUEWbjNBLERhen0eskRykNTNxPE3Udm9DRibfKOyicFD1sricWoQrLoEj0uJAbml2t9ic1NvPtfvBhAU6Ckrt8ef6BOvIIJKjs/0?wx_fmt=jpeg)

# 腾达路由器疑似出行暗藏后门，可直接获取管理员权限，暂无官方修复补丁

鹏鹏同学
鹏鹏同学

黑猫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0ibxBEh3kxDgB84xsF3ItTfgVRJuiaUicDzVJ9ictFU41ntn6rfCKSxZMK8lcVcTeOldibtXkRgsrUarl5HJy7a8OI5OHyFVSic0rjI/640?wx_fmt=png&from=appmsg)

美国 CERT/CC 发布安全预警，披露腾达多款路由器固件存在未公开的内置后门漏洞 CVE-2026-11405。攻击者可使用专属后门密码绕过用户自定义管理员密码，直接获得设备完整后台管理员权限。该漏洞目前**无厂商补丁、暂无修复方案**。

受影响型号包括 FH1201、W15E、AC10、AC5、AC6 等多条产品线。这些设备的 Web 登录逻辑位于 `/bin/httpd` 程序的登录函数中：系统先执行正常 MD5 密码校验，若校验失败，会自动触发备用后门校验流程。

漏洞核心机制为：系统会读取设备内置后门密码 `sys.rzadmin.password`，并以**明文比对**方式验证用户输入。只要输入后门密码，无论填写任意用户名，均可成功登录并获得最高管理员权限，原有设备密码被完全绕过。

攻击者成功入侵后，可完全接管路由器，篡改 DNS、修改网络配置、关闭安全防护，并以路由器为跳板渗透整个内网，造成**全网沦陷风险**。

该后门属于**固件固化后门**，并非配置文件漏洞，用户无法通过重置、修改后台设置关闭或移除后门，属于厂商出厂预置问题。

漏洞由匿名研究员上报，但腾达官方至今**未确认、未回应、未发布修复计划**。

CERT/CC 给出临时缓解建议：

1. 立即关闭路由器远程管理功能，禁止公网访问后台；
2. 修改默认 LAN 网段，降低被自动化扫描器探测的概率；
3. 该方法仅能降低暴露风险，**无法彻底修复漏洞**。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

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