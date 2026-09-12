---
title: 红队4大攻击场景 你在哪一秒能拦住
url: https://mp.weixin.qq.com/s/MeuS-kWW6nJaSmpq9EeZAA
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:44:13.882839
---

# 红队4大攻击场景 你在哪一秒能拦住

# 红队4大攻击场景 你在哪一秒能拦住

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

网络安全老宋// 攻防演练 · 蓝队复盘

// 攻防演练 · 蓝队乙方

# 红队4大攻击场景 你在哪一秒能拦住

把攻击链拆开，每个节点都留过门

蓝队工程师攻击溯源检测规则

🔑 一句话精华：红队赢在"你没看见"，蓝队赢在"看见的那一秒"——这4条攻击链，每个节点都留过门。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl93iaI9TW8f4X8Mmcc4r7pZmiceGCa07R7flv9nb5t119G9t6MYOabDRlia910YnR1qcCOdGuzhlhYvewSPFXcsfmvBkrzcSlMaxk/640?wx_fmt=png&from=appmsg)

红队攻击手册把"怎么打"写得透透的，但蓝队真正该练的，不是比红队更会打，而是比红队更早看见。我拿手册里复盘的四类真实场景，一条一条还原攻击链，在每个红队得手的节点上，标出蓝队本可以拦下的那一秒，再配上能直接落进 SIEM/SOC 的检测规则。

你去年护网是不是也遇到过：告警刷了一屏，没人认领，红队早进了域控才发现？这篇文章就是给这种情况用的。收藏好，演练前过一遍。

## 01钓鱼邮件破 OA：第一道门没拦，后面全白搭

**攻击链还原**：红队买好仿冒域名 → 发带宏病毒的钓鱼邮件 → 员工打开启用宏 → 木马落地 → 横向到 OA 服务器 → 拖走通讯录和文档。

这条链最该拦的，是"邮件落地"和"宏执行"两个节点。很多单位邮件网关只拦了已知病毒签名，红队换个免杀宏就进来了。

**蓝队可拦截的时机**：① 邮件网关层——陌生发件域 + 带 .docm 宏附件，直接 quarantine；② EDR 层——Word 派生 powershell 执行加密命令，行为拦截；③ 网络层——木马回连 C2 的外连请求，出网管控拦下。

⏺ HQL · 钓鱼宏落地检测

-- Office 进程派生 powershell 执行加密脚本

数据源 = "终端监测" and 父进程路径 rlike "winword\.exe|excel\.exe"

and 进程命令行 rlike "powershell.\*-enc|iex"

💡 **注意：**光看"powershell 启动"会误报爆炸，必须锚定"Office 父子进程"这个稳定特征，误报能降一大半。

## 02VPN 弱口令破域控：咽喉失守，内网裸奔

**攻击链还原**：红队扫到 VPN 入口 → 弱口令爆破成功 → 进内网 → 扫描到域控 389/636 → Kerberoasting 抓服务票据 → 离线破解 → 拿下域管 → 控全场。

这个场景最痛的点：VPN 爆破那一步，日志里全是无数的 "Failed password"，但因为没人设阈值告警，红队慢慢蹭进去了。

**蓝队可拦截的时机**：① 接入层——VPN 连续失败 5 次锁账号，对爆破源 IP 限速；② 认证层——非工作时间、异地 IP 的域登录二次校验；③ 域控层——新增域管、异常 Kerberos 票据请求，立刻告警。

⏺ HQL · 暴力破解与Kerberoasting

-- 同源短时大量失败登录

数据源 = "认证日志" and 事件摘要 rlike "Failed password|登录失败"

and 发生时间 >= now-10m group by 源IP having count >= 20

-- Kerberoasting 特征：RC4 票据请求

数据源 = "域控审计" and (进程命令行 rlike "kerberoast|tgtdeleg"

or 事件摘要 rlike "RC4.\*AS-REQ|0x17")

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9yR5gGqQ5n9GPILCtP4SDPIAXxekdic10DVcx9Y4tx2f1CRvibY8JUBTbQQWno4Vib2PWlkFPRdc0lmxotmmwJqKxmnaG1z1ibgfY/640?wx_fmt=png&from=appmsg)

## 03供应链破核心系统：你信的"自己人"带着刀

**攻击链还原**：红队不正面刚你的防火墙，而是攻陷你用的运维工具、第三方组件、或外包人员的笔记本 → 借合法通道进核心系统 → 因为"来源可信"没人怀疑。

手册里这条叫"供应链破核心系统"，本质是利用信任链。蓝队最容易漏的，是把外包、第三方组件当成白名单放行。

**蓝队可拦截的时机**：① 资产层——第三方组件版本台账，定期扫 CVE；② 终端层——运维工具突然访问从没连过的核心库，行为异常告警；③ 网络层——可信来源却连了陌生高危端口，不放行。

⏺ HQL · 运维工具异常外连

数据源 = "网络流量" and (进程命令行 rlike "npm|pip|ansible|expect")

and 目的端口 in (1433, 3306, 6379, 27017)

💡 **注意：**供应链检测别只盯外部 IP，很多投毒是"内部可信进程干了不该干的事"，行为基线比对比黑名单更管用。

## 04云 K8s 容器攻击链：新战场，蓝队最陌生

**攻击链还原**：红队发现 K8s API Server 没鉴权或令牌泄露 → 拿集群权限 → 利用 runc/容器运行时漏洞逃逸到宿主机 → 控制节点 → 顺着云凭证偷走 AK/SK → 拖库。

这条链是 2025 年演练里涨得最快的。K8s token 泄露在 22% 的云环境里存在，runc 三重漏洞（CVE-2025-31133/52565/52881）、IngressNightmare（CVE-2025-1974，CVSS 9.8）都是现成的逃逸跳板。

**蓝队可拦截的时机**：① 集群层——API Server 禁止匿名访问，kubeconfig 令牌单独保管；② 运行时层——容器以 --privileged 或挂宿主目录启动，直接拦截；③ 云层——宿主机上出现云 CLI 读取凭证文件的行为，告警。

⏺ HQL · 容器逃逸与云凭证窃取

-- 特权模式启动或挂载宿主敏感路径

数据源 = "容器运行时" and 进程命令行 rlike "docker.\*run.\*--privileged|--mount.\*/proc|/var/run/docker\.sock"

-- 容器内访问云元数据或读取凭证文件

数据源 = "主机审计" and 进程命令行 rlike "169\.254\.169\.254|aws/credentials|\.kube/config|aliyun.\*accessKey"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93fl9KfpprBPrxcTxLpjHrRufmKicZTNLxLbyF8icY5lRAxtqYCM6LryYMEj2A04s3QpibjstM7oibwgXN4Jqo7Q8DjffQsnUbbX2gKc0/640?wx_fmt=png&from=appmsg)

## 05把四个场景串成一条蓝队时间线

红队每一步都得留下痕迹，蓝队要做的，是让"看见"发生在红队得手之前。我习惯按这条时间线排兵布阵：

**接入期**（邮件/VPN/边界）→ 拦在落地前，靠网关和双因子；**立足期**（宏执行/弱口令登录）→ 拦在提权前，靠 EDR 行为拦截；**横移期**（扫描/票据/异常外连）→ 拦在控场前，靠网络基线和告警；**收割期**（拖库/逃逸/窃凭证）→ 拦在出网前，靠数据外发管控。

每个阶段至少布一条"必看告警"，演练时专人盯，比堆一百条没人看的规则有用。

// 老宋说：蓝队最大的误区，是把自己当成"更高级的红队"，天天研究怎么打，却没把"怎么看见"这件事做扎实。红队手册翻烂了，不如把你们 SOC 里那几条没人认领的告警规则重写一遍。

行业里一个现实：很多单位的检测规则是"上线即退役"，写了从不调优，误报高了就静音，最后等于没写。演练的价值，恰恰在于逼你把规则跑到真实攻击上验一遍。

你这周能做的，是把上面 02、04 两条规则先接进你的平台，用历史日志回放跑一遍，看误报多少、漏报多少——别等演练开始才第一次跑规则。

规则别写完就放着，用历史日志回放验一遍误报漏报，这才是蓝队该干的活。

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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