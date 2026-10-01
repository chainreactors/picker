---
title: 【安全圈】Citrix NetScaler高危双零日遭在野利用：Root权限与隧道木马曝光
url: https://mp.weixin.qq.com/s/SR7zfvGvEzdsVNQpalz9Wg
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:57:38.874413
---

# 【安全圈】Citrix NetScaler高危双零日遭在野利用：Root权限与隧道木马曝光

# 【安全圈】Citrix NetScaler高危双零日遭在野利用：Root权限与隧道木马曝光

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**事件核心要点：**Citrix 旗下应用交付控制器（NetScaler ADC）与网关（NetScaler Gateway）被曝出两个遭到在野实战利用的严重零日漏洞（CVE-2026-88772、CVE-2026-88771）。攻击者无需任何认证凭据，仅通过向 DTLS 握手端口发送特制分片畸形数据包，即可击穿数据包处理引擎（NSPPE），在底层 FreeBSD 系统直接取得 Root 最高控制权，并植入具备 HTTP 头部隐匿特性的 WebShell 及内网流量穿透隧道。CISA 已签发加急指令，强制联邦机构限期完成关停修复。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHWT2pSSXDGy6hHXtwbzJsKwqibgrNgslsdC5wVU5wm8YmNxwjazcrkL4hxaxlFll4PvAn30osxY6YciaZ8yyvxckbS5yfvheskE/640?wx_fmt=other&from=appmsg)

## 🚨 漏洞成因：DTLS 握手分片重组出现 174KB 堆溢出

安全机构 watchTowr Labs 披露的技术复现报告显示，核心漏洞 CVE-2026-88772（CVSS 评分 9.5）源于 NetScaler 数据包处理引擎（NSPPE）在解析数据报传输层安全协议（DTLS）时的逻辑缺陷。

在预认证握手阶段，NSPPE 盲目信任了客户端上报的 DTLS 记录头声明。攻击者构建一个声明总长度为 120 字节的握手消息，但将其拆散为 120 个单独分片，每个分片的 `fragment_length` 字段虚假标记为 1 字节。

```
[DTLS 握手畸形包] 声明总长度: 120 字节 | 拆分为 120 个分片 [分片虚标] 每一个分片头部谎称: fragment_length = 1 字节 [底层缓存分配] 每个分片实载 1459 字节，完整存入 NetScaler Buffer (NSB) 链表 [重组堆溢出] 拼装目标临时暂存区仅 35,840 字节 (35KB) [溢出结果] 120 个分片累计驻留约 174KB 数据，强行灌入 35KB 缓冲区导致严重堆覆写 [执行劫持] 调用 mprotect() 击穿 NX (不可执行) 保护，执行任意 Root Shellcode
```

由于 NSPPE 代码并未校验下一个数据包拼装后是否会超出暂存区容量，累积约 174KB 的真实数据直接倾泻至仅有 35KB 的暂存空间，引发毁灭性堆越界写入。攻击者随后通过 `mprotect()` 系统调用击穿内存执行保护，直接获取底层 FreeBSD 操作系统的 Root Shell 权限。

## 🔍 深度伪装后渗透工具链：WHIPSHOT 与 SLAPSHOT 现身

谷歌威胁情报集团（GTIG）与 Mandiant 在北美及欧洲的政务、金融、科技行业实战应急响应中，捕获到了黑客在获取初始 Root 访问后投递的成套持久化后门。

攻击者篡改了 NetScaler 本地的 `httpd.conf` 与 Web 运行时配置，将 Linux 下常规的 Debian 软件包后缀（`.deb`）以及签名文件（`.sig`）映射为由 `mod_php` 引擎直接执行的脚本：

* **图标请求暗度陈仓**

  ：攻击者将外部对 `/vpn/media/*.ico` 图标资源的 HTTP GET 请求，在网关内部重写路由至 `/var/netscaler/gui/vpn/scripts/linux/*.sig` 恶意脚本。外部访问日志呈现看似正常的 404 响应，实际响应体体积却达数 KB 并消耗显著计算时长。
* **WHIPSHOT 头部隐匿后门**

  ：这套新型 PHP WebShell 专门从原生 HTTP 请求标头中抽取经 Base64 编码的 C2 指令，在静默执行后再将加密回显嵌入 HTTP 响应头返回，彻底规避常规 WAF 的请求体内容检测。
* **SLAPSHOT 流量穿透代理**

  ：黑客同步植入了基于 Python 开发的流量隧道组件，以该边界网关作为跳板节点，向受害单位深层内网发起横向探测、内网穿透与活动目录凭证搜集。
* **固化持久控制**

  ：攻击者利用临时安装脚本篡改 `/bin/sh` 执行权限，并在设备全量重启后依然常驻内存。

## 🛡️ 官方处置清单与受影响版本核查

Citrix 官方确认，仅当 NetScaler 设备被配置为网关（Gateway：如 VPN、ICA 代理）或认证鉴权虚拟服务器（AAA-TM）时，该攻击路径才处于开启状态。纯负载均衡（LB）模式且未监听 DTLS 握手的节点暂不受此路径波及。

📦 受影响产品线与已修复固件版本：

• **NetScaler ADC / Gateway 14.1 分支**：必须升级至 `14.1-36.48` 或更高版本；

• **NetScaler ADC / Gateway 13.1 分支**：必须升级至 `13.1-56.19` 或更高版本；

• **NetScaler ADC 13.1-FIPS 分支**：升级至 `13.1-37.208`；

• **应急排查项**：核查 `/var/netscaler/gui/vpn/scripts/linux/` 目录是否存在异常 `.sig` 或 `.deb` 文件；检索 `httperror-vpn` 与 Web 日志中异常的 `.ico` 长时请求。

***END***

阅读推荐

[【安全圈】看张图片就中招？苹果的这个漏洞你一定要看](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079161&idx=1&sn=d33e558e6c0b63eff92e7b87e35da4f9&scene=21#wechat_redirect)

[【安全圈】OpenAI叫停大模型训练：Agent突破沙箱偷连外部服务](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079161&idx=2&sn=afb4262b4d676f9ed2b6da390755c347&scene=21#wechat_redirect)

[【安全圈】MCP官方SDK高危漏洞：恶意服务可盗取OAuth凭证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079161&idx=3&sn=704f24afc846aa0d28375d6b5f4d600a&scene=21#wechat_redirect)

[【安全圈】苹果崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079150&idx=1&sn=f25dd80dbe08777b632a88ab45425b84&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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