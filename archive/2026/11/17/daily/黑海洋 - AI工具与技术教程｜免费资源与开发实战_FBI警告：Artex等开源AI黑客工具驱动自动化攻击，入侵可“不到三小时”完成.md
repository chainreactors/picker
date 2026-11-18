---
title: FBI警告：Artex等开源AI黑客工具驱动自动化攻击，入侵可“不到三小时”完成
url: https://blog.upx8.com/FBI-Artex%E7%AD%89AI%E9%BB%91%E5%AE%A2%E5%B7%A5%E5%85%B7%E4%B8%8D%E5%88%B03%E5%B0%8F%E6%97%B6%E5%8F%AF%E5%8F%96%E5%BE%97%E7%9B%AE%E6%A0%87%E7%BD%91%E7%BB%9C%E7%89%B9%E6%9D%83
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-17
fetch_date: 2026-11-18T09:21:47.133002
---

# FBI警告：Artex等开源AI黑客工具驱动自动化攻击，入侵可“不到三小时”完成

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)
[晴

**晴空图床**
*tp.776161.xyz*](https://tp.776161.xyz/)

[首页](https://blog.upx8.com)
/
[资讯](https://blog.upx8.com/news)
/
FBI警告：Artex等开源AI黑客工具驱动自动化攻击，入侵可“不…

# FBI警告：Artex等开源AI黑客工具驱动自动化攻击，入侵可“不到三小时”完成

[资讯](https://blog.upx8.com/news)
11-17
·
约 4 分钟
·
黑海洋
·

4,272

美国联邦调查局（FBI）在最新网络安全快速通报中警告，黑客正依赖Artex等开源自主AI黑客工具发动攻击，目标涵盖金融服务、政府、科技、国防、电信及律所等多个行业。通报指出，部分Artex相关攻击从锁定系统到完成入侵“不到三小时”。Artex是一款开源AI渗透测试框架，可将Anthropic、OpenAI等前沿大模型或开源模型接入自主Agent，由Agent自动扫描目标、运行工具、分析结果并调整失败步骤，整个攻击过程仅需极少人工介入。

## 韩国金融业：基础防护缺失导致至少6.8万人数据被盗

自今年7月首次公开以来，Artex已被用于多起攻击。韩国多家金融机构因缺乏多因素认证等基础防护被攻破，至少6.8万人的个人数据被盗。调查显示，攻击者并未直接突破银行核心清算与账务系统，而是集中攻击了防护标准较低、行为检测空白但数据价值较高的外围辅助系统，如中介查询系统、员工办公支持系统及外包人员数据库。CrowdStrike评估认为，操作者可能并非顶级黑客，但Artex将一名初级人员放大为多目标渗透团队，数天内完成了过去需要专业团队数周才能完成的工作。

## ConnectWise与微软365：至少2250家客户云环境受波及

微软此前披露，攻击者利用Artex入侵IT管理公司ConnectWise，进而进入至少2250家客户的微软365云环境。FBI确认了这一发现。微软将相关活动归因于Storm-0940，该组织被描述为具有龙国国家背景。需要说明的是，2250这一数字描述的是攻击者尝试访问的租户数量，而非确认已成功入侵或数据已被窃取的租户数量。攻击者利用的是客户已授权的ConnectWise应用权限，试图借此进入关联的微软365环境。

## Barracuda：因日志不足“按最坏情况处理”

安全公司Barracuda亦披露遭遇Artex关联攻击。攻击始于一把提供给第三方AI厂商的云访问密钥——项目结束后该密钥未被撤销，攻击者于11月1日利用它进入Barracuda云环境，在约44小时内访问了约10个云账户。Barracuda表示，攻击序列、识别痕迹及内置凭据搜索例程与Artex模式吻合，但因日志不够详细，无法完全排除客户集成凭据被读取的可能性，因此选择“按最坏情况处理”，通知少部分可能受影响的XDR客户撤销并重新创建相关凭据。Barracuda首席信息安全官Arve Kjoelen对此评论：“依赖发现恶意活动再响应的防御方，往往在攻击者收工后才到场。”

## 工具扩散与暴露风险

Artex开发者在攻击事件后将软件转为闭源，但FBI指出旧的开源版本仍在流传且“广泛可获取”。安全公司Censys的研究显示，超过800个Artex部署实例在公网无需密码即可访问，其中就包括用于攻击韩国金融机构的那一台。这些暴露的实例不仅使工具本身可被任意人使用，还暴露了其中存储的植入物与攻击数据。Censys首席安全研究员Silas Cutler指出，并非每个实例都被恶意运营，许多用于授权测试，但数百个系统暴露在公网的原因仍不明确，因为该软件本身并不要求联网访问。

FBI建议防御方限制公网暴露的管理工具、缩减应用权限、扫描代码仓库中存储的密钥，并将异常应用登录行为与凭证新增、角色变更、高频API调用进行关联分析。在攻击以“机器速度”推进、单次自动化突发仅持续数秒到数分钟的节奏下，依赖人工发现异常后再响应的模式，其时间窗口正在被系统性压缩。

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[安全](https://blog.upx8.com/tag/%E5%AE%89%E5%85%A8/)
[工具](https://blog.upx8.com/tag/%E5%B7%A5%E5%85%B7/)
[攻击](https://blog.upx8.com/tag/%E6%94%BB%E5%87%BB/)
[黑客](https://blog.upx8.com/tag/%E9%BB%91%E5%AE%A2/)
[AI](https://blog.upx8.com/tag/AI/)

[上一篇
Deva：一个对话带起一支 AI 团队，把 Agent 能力装进桌面聊天框](https://blog.upx8.com/Deva-AI-Agent)
[下一篇
GTA VI泄露案黑客认罪：用酒店电视棒攻破Rockstar，勒索未遂后公开90段视频](https://blog.upx8.com/2022%E5%B9%B4GTA-VI%E6%B3%84%E9%9C%B2%E4%BA%8B%E4%BB%B6%E8%83%8C%E5%90%8E%E7%9A%84%E9%BB%91%E5%AE%A2%E8%AE%A4%E7%BD%AA)

## 相关文档

* [印度金融机构遭AI工具驱动黑客攻击：“狡猾猎鹰”组织持续活跃
  11-06](https://blog.upx8.com/%E5%8D%B0%E5%BA%A6%E9%87%91%E8%9E%8D%E6%9C%BA%E6%9E%84%E9%81%AD%E5%88%A9%E7%94%A8AI%E5%B7%A5%E5%85%B7%E7%9A%84%E9%BB%91%E5%AE%A2%E6%94%BB%E5%87%BB)
* [赵长鹏称币安可能遭遇史上最大规模加密货币盗窃案
  10-30](https://blog.upx8.com/%E8%B5%B5%E9%95%BF%E9%B9%8F%E7%A7%B0%E5%B8%81%E5%AE%89%E5%8F%AF%E8%83%BD%E9%81%AD%E9%81%87%E5%8F%B2%E4%B8%8A%E6%9C%80%E5%A4%A7%E8%A7%84%E6%A8%A1%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E7%9B%97%E7%AA%83%E6%A1%88)
* [比利时、瑞典超市冷冻柜遭遇黑客攻击
  11-02](https://blog.upx8.com/%E6%AF%94%E5%88%A9%E6%97%B6-%E7%91%9E%E5%85%B8%E8%B6%85%E5%B8%82%E5%86%B7%E5%86%BB%E6%9F%9C%E9%81%AD%E9%81%87%E9%BB%91%E5%AE%A2%E6%94%BB%E5%87%BB)
* [币安63亿美元被盗事件全解析：从虚假面试到四分钟盗币的完整入侵链
  11-04](https://blog.upx8.com/%E5%B8%81%E5%AE%89%E8%B5%84%E4%BA%A7%E8%A2%AB%E7%9B%97%E4%BA%8B%E4%BB%B6%E6%8A%A5%E5%91%8A-%E9%BB%91%E5%AE%A2%E7%BB%8F%E8%99%9A%E5%81%87%E9%9D%A2%E8%AF%95%E5%85%A5%E4%BE%B5)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [韩国金融业：基础防护缺失导致至少6.8万人数据被盗](#sec-1)
* [ConnectWise与微软365：至少2250家客户云环境受波及](#sec-2)
* [Barracuda：因日志不足“按最坏情况处理”](#sec-3)
* [工具扩散与暴露风险](#sec-4)

[![黑海洋](https://blog.upx8.com/logo.webp)
**黑海洋**
WIKI](https://blog.upx8.com/)

黑海洋专注 AI 智能体、程序开发、开源工具与免费资源分享，提供保姆级部署教程、源码下载、云服务器运维与安全资讯。

分类

[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)

常用

[全部文档](https://blog.upx8.com/all.html)
[RSS 订阅](https://blog.upx8.com/feed/)
[RSS 评论](https://blog.upx8.com/feed/comments/)
[Sitemap](/sitemap.xml)

关于

[关于本站](/about.html)
[友情链接](https://blog.upx8.com/links.html)
[我的收藏](https://blog.upx8.com/library.html)

Copyright © 2026 黑海洋

[浙ICP备2021040518号-1](https://beian.miit.gov.cn)

站点正常

[首页](https://blog.upx8.com/)

分类

搜索
[收藏](https://blog.upx8.com/library.html)

**全部分类**

[资源
2021](https://blog.upx8.com/Free)
[安全
375](https://blog.upx8.com/os_security)
[开发
536](https://blog.upx8.com/code)
[资讯
1971](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)