---
title: Chrome新\"bug\": 恶意网站可以0.5 click窃取用户之前上传的文件，漏洞赏金$1000
url: https://mp.weixin.qq.com/s/WC9ArlS-5ieCyOuO4OUMFQ
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:29.110391
---

# Chrome新\"bug\": 恶意网站可以0.5 click窃取用户之前上传的文件，漏洞赏金$1000

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNUGE76ib6gketiaV9u7mcXvibVZDFics9PLycNZunokGapG7J8zCRDCaFMT4sAib1Hg1O6GicfuyWiafkvf4OsHOAYtURWpZ7x3CO90dE/0?wx_fmt=jpeg)

# Chrome新"bug": 恶意网站可以0.5 click窃取用户之前上传的文件，漏洞赏金$1000

原创

助力行业的
助力行业的

李白你好

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 🎯 一句话速览

一个编号为`CVE-2026-2322`的Chrome浏览器漏洞被发现，它可以让一个精心设计的恶意网站，在你**长按回车键**的瞬间，悄无声息地窃取你之前在其他网站上上传过的文件。由于其利用了简单的键盘操作，该手法也被戏称为 **“0.5点击”攻击**。

```
https://issues.chromium.org/issues/470928605
```

![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVkKBoWKMuricEpIK6gyO5EhJlfJ1ZM9uYEuQJ7dI7evDx6XV8R9kOQtibhlUZax0JjBfkeDwmCLvA5r2cFgVciaYSVibrprG4Ogvc/640?wx_fmt=png&from=appmsg)

## ⚙️ 攻击手法：一次简单的“按键模仿”

* **精心设计的陷阱**：当你访问一个恶意网站时，该网站会通过JavaScript动态创建一个文件上传按钮（`<input type="file">`），并强制让这个按钮处于页面的激活状态。
* **完美的“替身”**：同时，网站会伪造一个诱饵按钮，比如“点击参与抽奖”或“领取优惠券”，并利用页面布局或视觉欺骗，让你以为自己在点击这个假按钮。但实际上，你点击的却是那个隐藏的、真实的文件上传按钮。
* **关键的0.5秒**：最关键的一步来了——文件上传按钮被点击后，会弹出一个系统文件选择窗口。此时，如果你正巧按着回车键（Enter键），浏览器会默认将这个回车操作理解成用户对“确认选择”按钮的“双击”，从而自动确认并上传文件，无需你进行任何额外的鼠标点击。

**总结一下：你长按的回车键，被漏洞利用，直接“批准”了恶意网站上传文件的操作。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNUS8lmw58CsQCA2Jg4XKUWmBiaCGm8oruqbiafy3HqR20pYMNUmGZBXMxZuChp0MML4D2JudUHrwH7yNDuSMUiabU9XWvHCK5bwqc/640?wx_fmt=png&from=appmsg)

## ⚠️ 你的什么文件最危险？

该漏洞主要威胁的是你曾在浏览器中上传过的文件，这些文件的路径通常会被浏览器缓存。攻击者通过上述技巧，可以直接调取这些“历史记录”中的文件。具体来说，最危险的文件包括：

* **网站配置文件**：如 `.env`、`config.php` 等，它们可能包含数据库密码、API密钥等核心凭证，是黑客窃取的首选目标。
* **用户数据文件**：如 `.csv`、`.xlsx` 等数据导出文件，可能包含大量用户个人信息或业务数据。
* **脚本文件**：如 `.sh`、`.py` 等，一旦被篡改或分析，可能被用于后续的渗透攻击。
* **任何你在网页上提交过的文件**：比如你上传到网盘、社交媒体、在线办公软件的图片、文档等，都有可能被恶意网站利用此漏洞尝试窃取。

## 🌍 谁最受影响？

该漏洞（CVE-2026-2322）主要影响了**在Ubuntu或其他Linux发行版上运行的Chrome浏览器**，但理论上其他操作系统也存在一定风险。鉴于Chrome的庞大用户群体，该漏洞的影响范围十分广泛。

## 🛡️ 如何修复？立即行动！

该漏洞已在Chrome 145.0.7632.45及更高版本中得到修复。

**🔧 立即检查更新：**

1. 打开Chrome浏览器，点击右上角的“三个点”菜单。
2. 选择“**帮助**” -> “**关于Google Chrome**”。
3. 浏览器会自动检查更新，如有新版本，请立即**重启浏览器**完成更新。

## 💡 反思与建议

这个“低”风险的漏洞被谷歌开出了$1000美金的赏金，它提醒我们：**即使是被评定为低风险的漏洞，也可能造成严重的数据泄露。** 更值得注意的是，Red Hat等安全机构对此漏洞给出了“**Moderate**”（中等）的威胁评级，谷歌的Chromium安全团队也将其标记为“**Medium**”（中等）风险，这进一步印证了其潜在威胁不容小觑。

除了更新浏览器，你还应培养良好的上网习惯：

* 在点击任何链接前，都仔细检查其真实目的。
* 不要轻易在不可信的网站上按住回车键。
* 为你的操作系统和浏览器开启“自动更新”功能。

## 网络安全情报攻防站

**www.libaisec.com**

综合性的技术交流与资源共享社区

专注于红蓝对抗、攻防渗透、威胁情报、数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNUBd6YHx2iaIMcHvxIztn38KXibxGibdz8yElysNTymkMcIWYCqtY2e7Vg8sDVY9gsibSeLLrKnUHH5aENHVPlv8v5S06yFWCMyrLk/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

李白你好

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

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