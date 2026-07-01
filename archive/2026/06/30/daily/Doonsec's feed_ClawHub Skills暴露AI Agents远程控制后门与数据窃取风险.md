---
title: ClawHub Skills暴露AI Agents远程控制后门与数据窃取风险
url: https://mp.weixin.qq.com/s/mahA44c1FxyUKdkXtoamAg
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:21:04.311573
---

# ClawHub Skills暴露AI Agents远程控制后门与数据窃取风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3NDCotwfCN1IdsATichukxGKqh9vGcnKjPlsliaSMKhx0Vqc0pLtJYeH2ibe8EfxTnqcXJK8IGXMvEbZGK0rD87Epvib1QE9YicO94/0?wx_fmt=jpeg)

# ClawHub Skills暴露AI Agents远程控制后门与数据窃取风险

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3VUUnOoWhz6tsw4h76cHkd49mMFd6dqX3ia1ttZGCjjhEjKU9IwqwJR8NkqruQ6iaf8ZjHOX5DcCFCFBaLYD0noJUcaB7iaSBglg/640?wx_fmt=gif)

![图片](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1UYibj1kNEy2XtY1ER26qZPicPibGicZYG0QzYicXUKTaNMZDjSSEZKeW9vwZnjWAqKrb6QtazzyiaRSAQUmIcLcO6kwXUmXAM8IMY0/640?wx_fmt=png)

Part01

AI Agents功能扩展带来新型攻击面

现代AI Agents已超越简单的问答功能，能够代表用户执行操作、管理文件及运行代码。这种能力跃迁同时开启了危险的新攻击维度——针对ClawHub市场的恶意skills已暴露出AI Agent生态系统的严重脆弱性。作为2026年增长最快的开源AI Agent平台OpenClaw的官方技能市场，ClawHub的skills数量从1月的不足2000个激增至4月的5万余个，这种爆炸式增长在吸引数百万用户的同时，也引来了攻击者的持续关注。

腾讯朱雀实验室使用其开源测试平台AIG扫描了近5万个ClawHub skills，发现攻击者早在大多数用户意识到问题前就已预先部署攻击面。2026年1月下旬的"ClawHavoc"攻击行动中，攻击者利用12个遭入侵的账户向ClawHub投放了1184个恶意skills，最终导致24.7万次确认安装并窃取价值230万美元的加密货币。尽管平台事后增加了检测机制，但威胁已演变为更隐蔽的形式。

Part02

高危权限与隐蔽攻击链

Skills在用户环境中拥有完整权限，单次安装即可读写文件、建立网络连接并执行shell命令。这种高级别访问权限与平台的极速扩张相结合，形成了天然防御极少的高价值攻击目标。最令人警觉的发现是某个skill在通过ClawHub所有官方安全检查的同时，隐藏了可运作的远程控制后门。该skill伪装成"分布式状态恢复工具"，配有专业文档和合理的权限请求，表面毫无可疑之处。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX15O2wrhe6JGMTDOkiaQn3TzpZicPHV7mOJm10fn5IDQDyvic6eVH13eHX5ncBkJdastTvFREavNPnoJfZ8icyJ5Q4Y1ibbcic66A5Eo/640?wx_fmt=png)

实际执行时，它会连接远程C2服务器，获取经过Base64、ROT13和十六进制多层编码的载荷，随后通过Python的pickle模块反序列化执行，在受害者机器上实现任意代码运行。AIG平台通过识别远程获取、链式编码和反序列化的完整组合，将其标记为高风险远程代码执行攻击链。

2026年3月的另一起攻击则利用排名操纵漏洞——攻击者发现可向ClawHub后端发送未认证请求人为提升skill下载量。通过将伪装成"Outlook Graph集成工具"的恶意skill推至排行榜首位，利用AI Agents自主选择工具时优先高下载量skill的特性，实现了无需人工干预的自动安装。

Part03

生态系统级安全风险

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0dLKlibBHcvaOAicZ949c23iaqfYOGTMr00gOjiaia0ysQZI9GKGtibv7WIvXdrYuUBYDVNqgqiawDQv7g5gwsSh8yLXC6jE1kUxzzq4/640?wx_fmt=png)

腾讯的扫描暴露出超越单个恶意skill的系统性风险。在分析的近5万个skills中，74.6%声明了网络请求权限，意味着四分之三的skill会在正常使用时连接互联网。当恶意流量隐藏在海量常规连接中，检测变得极为困难。

文件访问与网络权限的结合为数据窃取创造了直接路径，平台上存在数百个引用私钥和凭证的路径。上海交通大学SkillProbe团队发现，超过90%的高下载量skill未能通过严格安全审计，打破了"流行skill更安全"的固有认知。前20名开发者共发布5422个skills，其中单个账户三个月内发布955个，符合自动化批量生成特征。这种生产能力使得攻击者可轻松大规模上传伪装样本。

腾讯建议用户在安装任何skill前后执行基础审查：安装前检查作者发布历史、确认权限与声明用途匹配、调查文档中的陌生域名；安装后审计活跃skills的过度权限，优先移除来源不明的高权限skill。

**攻击指标(IoCs):**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX293CP2KUDtpufKZXuGz2ZEZ2ucVO8FhhjZc5yNutgXrqKMvTezUc14lczZ4x0OibgMPNKnd9OvnupxPC8TQslaXOibfCnz3kKib0/640?wx_fmt=png&from=appmsg)

注：IP地址和域名已做无害化处理（如\_[.]\_），避免意外解析或超链接。仅在MISP、VirusTotal等威胁情报平台中恢复原始格式。

参考来源：

ClawHub Skills Expose AI Agents to Remote Control Backdoors and Data Theft Attacks

https://cybersecuritynews.com/clawhub-skills-expose-ai-agents/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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