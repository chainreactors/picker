---
title: 4.55亿月活里的APT跳板：UNC3569链式攻破搜狗输入法全过程
url: https://mp.weixin.qq.com/s/6jED7tURasxPRpl4Kr6wLg
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T07:01:16.815608
---

# 4.55亿月活里的APT跳板：UNC3569链式攻破搜狗输入法全过程

# 4.55亿月活里的APT跳板：UNC3569链式攻破搜狗输入法全过程

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PuTtzCxu1zk86NdFNo23IgjHOxtAibtzhwu6a5sGe9bjibISTl79AmWy1Eiawp50aS37iccSaNsjwGWnAfGK5f5WJ4j3Dic2TRUmQM/640?from=appmsg)
> **导语**：Gen Digital周四发布报告，披露中国关联黑客组织UNC3569利用搜狗输入法Windows版一键shell漏洞CVE-2026-51990，在4.55亿月活用户上部署GRAYRABBIT后门。这是一次教科书级的链式攻击——三个独立缺陷被精准串成一个完整的"点击即shell"路径，而腾讯的修复只解决了一半。

---

## 一、事件背景：4.55亿用户输入法成为APT跳板

搜狗输入法在2023年Citizen Lab（多伦多大学公民实验室）的统计里，月活用户超过4.55亿，全平台用户占中文输入法市场约70%，美国用户也占了3.3%的访问份额——一款输入法的影响力远超想象。

攻击者UNC3569是Google Threat Intelligence Group（谷歌威胁情报组）跟踪多年的"黑客雇佣"组织，自2021年起活跃，目标为东亚和东南亚的政府、教育、科技、金融行业。标志性武器正是本文主角——**GRAYRABBIT后门**：远程命令执行、文件双向搬运、可加载任意模块。

Gen Digital在2026年4月9日报告漏洞，腾讯12天内修复完成，自动更新版本16.3.0.3498于4月21日全量推送。9月11日公开披露报告。

![搜狗输入法Windows版产品示意](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Nj8oleQ9Dj87pLujsRzxhGib0wQVW8VfXvCfGLDLj9PLmLTAVA43MyBIwejruPUFxMlpicYLI0pRGLwoicdxGFl5bJSr7gQ97M6w/640?from=appmsg "搜狗输入法Windows版产品示意")

*图源：The Hacker News原报道配图*

---

## 二、攻击链拆解：教科书级三连击

整个攻击由三个互相独立的缺陷串成，每一击都看似无害，组合起来就是"一键shell"。

### 2.1 第一击：自定义URL协议 sgbiz: 的参数透传

Windows上的搜狗输入法不是单一程序，而是一组通过自定义URL协议 `sgbiz:` 通信的组件。任何 `sgbiz:` 链接都会被Windows传递给 `biz_helper.exe`，由它读取链接内容并启动对应的Sogou组件。

关键缺陷：`biz_helper.exe` 检查要启动的程序，**但不检查传递的命令行参数**——Gen Digital完全没发现任何过滤。攻击者只需构造一个 `sgbiz:` 链接指明启动 `SGMyInput.exe`（设置程序），并附带自己想要参数。第一道防线就被一道"招呼"打过。

### 2.2 第二击：皮肤商店 = 任意URL的浏览器跳转

`SGMyInput.exe` 收到参数后打开"皮肤商店"界面。皮肤商店是设置程序里唯一会打开浏览器窗口的入口——它会把浏览器导向"传入的URL"，且**完全不做校验**。

这是典型的"功能组件被滥用"案例：开发者只想让皮肤商店显示官方推荐的皮肤页面，没想过任何人能把它指向恶意网站。

### 2.3 第三击：内嵌Chromium 80 + 关闭沙箱 + 关闭同源策略

这里的浏览器不是Edge也不是Chrome，是Sogou自家编译的 **Chromium 80——2020年3月版本**。Gen Digital发现这个内置浏览器里两项保护在代码里就被关掉：

* **沙箱关闭**：浏览器被攻陷等同于用户态任意代码执行
* **同源策略关闭**：网页可读取其他源数据

CVE-2021-38003（V8引擎 JSON.stringify 内存破坏漏洞）的EXP代码此时直接生效——Chrome 95（2021年10月）就修了的洞，搜狗**5年没补**。

Gen Digital说"点击链接就是全部触发流程"；腾讯则认为"链路相对复杂，攻击者需社工让用户授权浏览器弹窗确认"。Chromium在打开外部程序时会弹确认框，用户可勾选"不再提示"——这条链在某些场景下可被绕过。Gen Digital补充，攻击者还可以通过邮件或聊天消息投递链接绕过弹窗路径。

---

## 三、载荷投递：7-Zip DLL劫持 + 进程数反沙箱

V8漏洞EXP触发后，从阿里云香港IP 8.218.50[.]207下载三个文件到 `C:\Users\Public\Documents\`：

* 合法7-Zip可执行文件
* 恶意DLL `7z.dll`（7-Zip启动时会从同目录加载这个DLL）
* 加密的最终载荷 `p`

攻击者执行的压缩命令本身无意义，唯一作用就是启动7-Zip，从而加载恶意DLL。这是Windows下经典的"DLL搜索路径劫持"。

**反分析机制**：恶意DLL在解密前先统计当前系统进程数——**少于50个进程就用错密钥**，payload直接变垃圾。自动化沙箱通常只跑几个进程，真桌面不可能少于50。这种简单但实用的反检测手法直接绕过了Gen Digital和其他厂商的自动化分析。

**自删除机制**：DLL把自己内容移进NTFS备用数据流，再标记文件删除。磁盘上文件消失，但行为日志里也没有删除调用。

最终GRAYRABBIT后门启动，C2连接 mail.uaiubifas[.]top:443。**端口443通常承载TLS，但这里用的是RC4加密的明文TCP——443端口的非TLS流量值得专门监控**。

---

## 四、IoC清单（Gen Digital公布）

* **恶意DLL**`7z.dll`：29c7ee41d0cc9e07d981e451df56d0c3d37c41ac4ec10c7b516cc033ee397a63
* **加密payload**`p`：749160a2f20f82744026719cf72e483595c6aad718efa74d675a98662e02422e
* **GRAYRABBIT**`core.dll`：d7a3c7eb94edc0e020f74c678743d71d61e944634aade4a67a96c3589e828b3a
* **后门C2**：mail.uaiubifas[.]top:443（RC4非TLS）
* **漏洞页面**：noht1ng[.]top
* **暂存服务器**：8.218.50[.]207（阿里云香港）
* **投放路径**：`C:\Users\Public\Documents\`

---

## 五、腾讯修复了一半：入口修了，浏览器没修

修复全部落在 `biz_helper.exe`：检查两个含URL的参数、拒绝非HTTPS、只允许4个域名结尾（sogou.com、qq.com、woa.com、sogou）。

**关键问题**：内嵌浏览器没修。Gen Digital在修复后的版本里检查发现：

* 沙箱开关**仍然是关闭的**
* 同源策略开关**仍然写在代码里关闭**
* Chromium引擎**仍然是2020年的80版本**

攻击入口堵住了，但只要攻击者能在 sogou.com / qq.com / woa.com 域名下找到XSS，或拿下这几个域下的某个页面，仍能复用完全相同的攻击链。

更尴尬的是，The Hacker News比对CISA KEV目录后发现：41个Chromium V8漏洞中至少**32个**的修复版本发布在搜狗内置版本之后——攻击者手里有大把已公开EXP可挑选使用。

---

## 六、防御建议

1. **立即升级**：搜狗输入法 Windows 版升级到 16.3.0.3498 或更高版本
2. **网络层监控**：对443端口的非TLS/非标准TLS流量做告警，RC4特征可作为辅助判定
3. **主机层监控**：

* 监控 `C:\Users\Public\Documents\` 下出现的可疑 DLL
* 监控合法7-Zip出现在Public目录的行为（异常）
* 关注 NTFS 备用数据流的异常

4. **DNS层阻断**：阻断 uaiubifas[.]top、noht1ng[.]top
5. **建议腾讯**：尽快把内嵌Chromium升级到当前版本，并开启沙箱——这是治本之策

---

## 七、红队视角总结

三个独立缺陷——协议处理器参数透传、设置程序任意URL跳转、内嵌浏览器配置错误——单独看都不致命，精准串联后就成了"点击即shell"。

讽刺的是腾讯的修复：堵住了入口，但内嵌浏览器仍然是2020年的Chromium 80，沙箱仍然关闭，同源策略仍然关闭。这种"修了一半"才是真正的风险——APT组织下次只需在 sogou.com 域名下找到一个XSS，就能完全复用同样的攻击链。

**这就是现代供应链攻击的核心逻辑：攻方只需要找到一个能用的洞组合，守方却要堵住所有可能的入口。**

腾讯12天内修了入口，值得肯定；但内嵌浏览器这颗定时炸弹，他们迟早要面对。

---

**素材来源**：本文根据 The Hacker News 2026年9月11日报道综合整理，原文链接 https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html ，技术细节引自 Gen Digital 官方研究报告 https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou 。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PIrO2QZ9VeJicGvbbhHoCrJ5OA0vPOohtAyMIIb6r3iaQagtf90ibYZsWrvIxvHq1NicGa6UOc5ibMWUv4akiaQr27Fe4xvJrwTaGrI/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PEHVsINicgVLibuKHicoeAD3NHSrKGo9xgSibGZLlqzNgzeftjD1lJM7DvaukqdibynDYlAnYzUzTAIap1dibzr57TRMyTUe3w05VFM/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OXjy5yt165Vc8Oll4cCK8I4jiagUWQicZnBeNaWomoahEy0IHImFeAmUXcP23hNELPMCUj3uVtaRicnNGMC8I4Fyfq3PswuSM6tw/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OPmUkibZJyib5yIqQ3r9DDc7pZ60KSHnIzzPfS8nrS6hibicqcLaToqoWsA6BnhdTrPwYAk4JF7pwo7J69aKLNtA60OpqMwWWaxFk/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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