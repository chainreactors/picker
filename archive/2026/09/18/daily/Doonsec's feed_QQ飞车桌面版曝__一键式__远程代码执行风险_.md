---
title: QQ飞车桌面版曝\"一键式\"远程代码执行风险?
url: https://mp.weixin.qq.com/s/kvU0LZQtXlmIW-lCW_Y4BA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:59:34.895327
---

# QQ飞车桌面版曝\"一键式\"远程代码执行风险?

# QQ飞车桌面版曝"一键式"远程代码执行风险?

tuto
tuto

杂杂咱谈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

据安全研究人员描述，QQ飞车桌面版疑似存在远程代码执行攻击链，攻击者可通过公共/游戏聊天中的系统消息触发漏洞，结合输入过滤绕过、PV规范化缺陷以及不受限制的Lua执行入口，最终实现任意系统命令执行。

攻击链大致涉及：

```
攻击者  │  ▼构造恶意 System Message  │  ▼公共/游戏聊天传播  │  ▼Sanitization Bypass输入清理机制绕过  │  ▼Unsafe PV Canonicalization不安全的PV规范化  │  ▼Lua Execution Sink进入非预期Lua执行入口  │  ▼Unrestricted Lua Execution不受充分限制的Lua执行  │  ▼Arbitrary Command Execution任意系统命令执行  │  ▼QQ飞车桌面客户端被控制
```

#Simple #QQ飞车 #RCE

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LCF75xtxMiaiaUiauC6TKOGdQ4TYySakdjbD0xCM5iakCGJ1S98zU7AahSSrSrtoqdNQUSjoQZ2ia7KHDichAXQSQsPw/0?wx_fmt=png)

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