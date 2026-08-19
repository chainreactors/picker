---
title: SANDCLOCK后门入侵LiteLLM供应链，2500+组织凭证泄露
url: https://mp.weixin.qq.com/s/92dyiBFlu1vZVGuXQKccGQ
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:55:07.778002
---

# SANDCLOCK后门入侵LiteLLM供应链，2500+组织凭证泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0l7RibicGPlU4hetA5zeyu6PbLw4U0GC9zjqhib0SJqAfzOdPBC60vfWIgZrHq9uRKFjCf1cmI3KicpWXEZOlAKcl5tGb2s2Y1zZA/0?wx_fmt=jpeg)

# SANDCLOCK后门入侵LiteLLM供应链，2500+组织凭证泄露

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX26Dk0ulBS1OBW7wuVlzQTvuNrI8HIm04JlHNyMlpHxzM6v98Nj79Y0bIYic6Oa6BicNLjbx0YgTkKgBmuaokBcVHLmJ39EDfVaM/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2xaGNoibjpPBfPDAF0Xzo2mYjw1QScavRibrPWr5A7c7HHnloiaVLW3RXNa2YYXJsCkj2TibzFwo6zKcno8gShT9ibQB3JiabibsK4ibI/640?wx_fmt=png&from=appmsg)

Part01

SANDCLOCK供应链攻击概况

美国Resecurity公司评估了受“SANDCLOCK”后门影响最严重的行业。该后门源于攻击者入侵代码仓库，并借此植入恶意代码。网络安全专家认为，LiteLLM/TeamPCP供应链攻击（Supply-Chain Attack）将造成长期影响。

通过入侵AI应用中一个广为人知的组件，攻击者将成倍扩大影响范围（blast radius）——部分受害者组织仍未意识到该后门及其影响。LiteLLM是一款热门的开源AI Gateway（AI网关）和工具库，可为OpenAI、Anthropic、GoogleGemini以及本地Ollama模型等100多个大型语言模型提供商统一API调用。

Part02

事件时间线与暴露范围

此类事件涉及大量MTTD（Mean Time to Detect，平均检测时间）和MTTR（Mean Time to Respond，平均响应时间）。2026年3月左右，威胁行为组织“TeamPCP”入侵了LiteLLM维护者凭证，并向PyPI发布了恶意版本1.82.7和1.82.8，从而造成至少数月的暴露窗口。

超过2500家组织以及数十万个CI/CD环境出现完整凭证泄露，涉及云基础设施密钥、仓库访问令牌、SSH凭证、Kubernetes Secrets以及AI提供商（如OpenAI、Anthropic）API密钥。

Part03

受影响实体与行业分布

Resecurity已获取到归因于TeamPCP使用“SANDCLOCK”凭证窃取器发起的LiteLLM供应链攻击的150GB存档。根据已发布的事件报告，随附的受害者清单列出了2038个仓库中898个遭入侵的GitHub所有者（组织/账户）。

受影响所有者包括多家全球大型企业，其中有Microsoft、Azure、IBM、NVIDIA、PayPal（Zettle）、Deloitte、Bosch、S&P Global、ElevanceHealth、84.51°（Kroger）、Adeo（LeroyMerlin）、Kärcher、Dräger、ID.me和1inch。

按受害者组织画像统计，受影响最严重的十大行业如下：

* 科技/软件
* 银行/金融/保险
* 医疗保健/制药/医疗技术
* 零售/电子商务
* 媒体/游戏/广告科技
* 制造/工业
* 专业服务
* 网络安全
* 加密货币
* 政府

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1xmT4ZECdYse3zgzojic9aw3qiaYDdxAnBicoGqq5BnX9C8EhVXsozKaLQ5jk2CUdYsM8gXvztOyMK92qnhNR8U9WrlU9rAumfSY/640?wx_fmt=png&from=appmsg)

Part04

调查细节与响应建议

Resecurity按密钥名称统计了2146条记录（除结构脱敏外，从未检查实际值）。其中绝大多数是GitHub CI/CD身份信息，同时有少量高价值的云端和注册表凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0y0HXZzlCWamrjnqzThFHv1p5wJaPxzDxSe3YrA7KC67nG0JDSAicVrFAkAEAicdspSO86rKLS1FibtjK8E65LmXRyxwkA6PRXIw/640?wx_fmt=png&from=appmsg)

受害者清单（owners.txt、repos.txt）列出了2038个仓库中898个不同的受影响GitHub所有者。分布呈长尾特征：631个所有者仅涉及单个受影响仓库，而受影响最严重的所有者（Cencosud-Cencommerce）涉及64个仓库。关键是，这些所有者中包含全球大型企业和受监管机构。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3VwqBykcIXHibJNVEz4Vnz0lgMAicLA7B9UICHx2Wg8iaOrh4JKdVedqaToxZo5sGvVkybmiaOby7EKmPG9N91FUg68LDKYMSEzm0/640?wx_fmt=png&from=appmsg)

所有受LiteLLM事件影响的组织都应撤销或轮换GitHub App私钥、PAT（个人访问令牌）、AWS/GCP/Firebase凭证、ECR/JFrog令牌、SSH密钥和签名密码，并使会话失效。

参考来源：

LiteLLM Supply-Chain Attack – Technology, Banking and Healthcare the Most Affected

https://securityaffairs.com/197377/hacking/litellm-supply-chain-attack-technology-banking-and-healthcare-the-most-affected.html

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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