---
title: 安全预警：Apifox 桌面客户端官方 CDN 脚本遭供应链投毒
url: https://mp.weixin.qq.com/s/IgzNQWQXEv8GwN1_gW231w
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:01.010336
---

# 安全预警：Apifox 桌面客户端官方 CDN 脚本遭供应链投毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCLpRZXdH0Lq7zbtBaXyVvdgEY4Zb4UKJjWCxTAnapdZCASFA6gafljLbuBAGElicoueEibKwj0UMjwo6ujBt2E6hNxPjKCryic8wI/0?wx_fmt=jpeg)

# 安全预警：Apifox 桌面客户端官方 CDN 脚本遭供应链投毒

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器中沉浸阅读

作者：Yao

编辑：77

**********# 1. 背景

慢雾安全团队监测到一起供应链攻击，Apifox 官方 CDN 所托管的前端脚本文件(hxxps[:]//cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js)，被植入经重度混淆处理的恶意 JavaScript 代码。该恶意代码以合法的统计埋点功能为掩护，在 Apifox Electron 桌面客户端环境中运行时，将窃取用户认证凭据及系统敏感信息，并向攻击者控制的 C2 服务器发送，进而拉取并执行任意远程代码，实现完整的远程命令执行(RCE)。

# 2. 投毒入口分析**********

****# 攻击入口为 Apifox 官方 CDN 资源被篡改：****

**********# 正常资源：

hxxps://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js

恶意版本（Web Archive 还原）：

hxxps://web.archive.org/web/20260305051418/hxxps://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js

从样本对比看，恶意版本在原有正常统计逻辑基础上，嵌入了混淆恶意代码，用于实施信息窃取与远程控制。

## 2.1 恶意 JS 分析

恶意代码被注入至 Apifox 官方 CDN 脚本中，Apifox 桌面客户端（基于 Electron 框架）在启动或运行过程中自动加载该脚本，无需用户任何交互即可触发。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCKc95V1y7OWvZrcFOcnGce5bObHnNh33q290KtfoSjuqmXjP8uFUvBO8ic0SuMCfLkxOWTAjPkKl5p2TIM3orIyLQfEApHCaibAE/640?wx_fmt=png&from=appmsg)

(hxxps://web.archive.org/web/20260305051418/hxxps://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js）

## 2.2 攻击流程**********

**********![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCLeOCnL8hdceIA8xrnefswEpFbrT0aibBwzyiauXQomuohD4GzBzJofNov6LAfdWMdylWLTic0bXpFkOpbIbibobZhtfPJ5Ln2Rs9s/640?wx_fmt=png&from=appmsg)

##

## 2.3 周期性 C2 Beacon 与任务拉取机制

恶意代码内置随机定时器，在 Apifox 客户端运行期间周期性执行，持续窃取数据并拉取最新 Payload：

|  |  |
| --- | --- |
| 参数 | 值 |
| 最短间隔（MIN\_MS） | 30 分钟 |
| 最长间隔（MAX\_MS） | 3 小时 |
| 执行方式 | 随机间隔，首次启动即触发 |

##**********

****## 2.4 混淆与对抗检测手段****

*********** ## 使用 javascript-obfuscator 对恶意代码段进行高强度混淆

* 所有字符串通过 RC4 算法加密存储于大型字符串数组，运行时动态解密
* 所有关键数字常量（时间间隔、块大小等）均通过多步运算表达，规避静态扫描
* C2 通信全程 RSA 加密，内嵌 RSA 私钥（256 字节分块），防止流量分析
* 恶意代码段附于合法统计代码之后，利用白名单信任绕过安全检测

# 建议**********

**********# 建议受影响用户

1. 立即吊销历史 accessToken，并检查是否存在异常 API 调用记录。

2. 退出并重新登录 Apifox 账户，强制废止当前 Token。

3. 修改 Apifox 账户密码，并检查账户是否存在异常登录记录

4. 网络层封锁 apifox.it.com 及其所有子域名

5. 清除 Apifox 客户端的 localStorage，删除 \_rl\_headers 和 \_rl\_mc 键：

* 在 Apifox 客户端开发者工具控制台执行**********

```
localStorage.removeItem('_rl_headers');localStorage.removeItem('_rl_mc');
```

************# IoCs

Domain

apifox.it.com

\*.apifox.it.com

URL

hxxp[:]//cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js

hxxp[:]//cdn.apifox.com/www/assets/js/user-tracking.min.js

File

filename: apifox-app-event-tracking.min.js

SHA256: 91d48ee33a92acef02d8c8153d1de7e7fe8ffa0f3b6e5cebfcb80b3eeebc94f1************

**往期回顾**

[SlowMist Agent Security Skill 正式发布，守护 AI Agent 每一道防线](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504542&idx=1&sn=877bb46e71ffb4b97ef69748773ee304&scene=21#wechat_redirect)

[SlowMist × Bitget AI 安全报告：把钱交给“龙虾”等 AI Agent 真的安全吗？](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504477&idx=1&sn=57f7323b9460df2d03b15f39de4e4dd1&scene=21#wechat_redirect)

[活动回顾 | SlowMist KYT 新品亮相，重构合规基座](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504461&idx=1&sn=245db26fb01a7da89e732ef1ca28b422&scene=21#wechat_redirect)

[慢雾报告：合规压力下 VASP 的猫捉老鼠困境](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504454&idx=1&sn=27742de4ac090d63ca765483be9723e3&scene=21#wechat_redirect)

[倒计时 1 天｜慢雾(SlowMist) 链上合规新品发布会即将开启](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504420&idx=1&sn=f62874b1aeec756939b474be4052f11e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbEP8f4tadFenoLauzHpicWdWbVap3aia38LUGPflBho9ibDHXjoG5fecGJSaYa4S4zYdoicXibSmjv9tg/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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