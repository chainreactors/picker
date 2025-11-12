---
title: Balancer协议V2池遭黑客攻击 损失超1.28亿美元
url: https://www.4hou.com/posts/NG4K
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-11
fetch_date: 2025-11-12T03:11:06.871700
---

# Balancer协议V2池遭黑客攻击 损失超1.28亿美元

Balancer协议V2池遭黑客攻击 损失超1.28亿美元 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Balancer协议V2池遭黑客攻击 损失超1.28亿美元

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10948

收藏

导语：​此次Balancer攻击是2025年规模最大的加密货币盗窃事件之一。

Balancer协议宣布其V2流动性池成为黑客攻击目标，据报道此次攻击造成的损失估计超过1.28亿美元。

Balancer是基于以太坊区块链构建的去中心化金融（DeFi）协议，兼具自动做市商与流动性基础设施层功能。该协议提供支持自定义代币组合的灵活流动性池，用户可存入资产赚取手续费，交易者则能进行资产互换。协议由BAL代币治理，事发前该代币的市值为6500万美元。

Balancer尚未披露事件过多细节，但已警示用户警惕潜在诈骗或钓鱼攻击。该协议已确认，V2可组合稳定池遭遇漏洞利用攻击，且该问题未影响包括V3在内的其他任何Balancer流动性池。

![BalancerV2Hack.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251104/1762248278601946.jpg "1762245675400634.jpg")

**攻击原因争议**

关于攻击的具体成因目前尚无统一结论。据GoPlus Security分析，Balancer V2的漏洞利用源于金库（Vault）swap交易计算过程中的精确舍入误差。每次互换操作都会对代币数量向下取整，产生微小偏差，而攻击者可反复利用这一偏差。通过批量互换功能串联多次交易，这些舍入损失会累积形成巨大的价格扭曲，最终被攻击者利用。

![G410mubbsAAj0Vg.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251104/1762248281244614.jpg "1762245713470049.jpg")

使用缩放因子对代币数量进行标准化

另有部分自称了解内情的用户表示，攻击源于Balancer V2金库内部的授权不当与回调处理漏洞。据透露，攻击者恶意部署的合约在流动性池初始化阶段操纵了金库调用，成功绕过安全防护措施，实现了跨关联池的未授权互换与余额操控。

Balancer承诺将“尽快分享此次攻击的更多细节及完整事后分析报告”。值得注意的是，自2021年以来，Balancer V2已历经11次安全审计，每次审计的检查范围各有不同。

**仿冒官方的钓鱼企图**

与此同时，有不法分子试图借此次事件牟利——冒充Balancer官方联系黑客，提出“白帽赏金”方案：若黑客同意将其余赃款退回指定地址，可获得被盗金额20%的奖励。

该钓鱼信息措辞严谨，通过多重设计营造可信度，包括明确奖励比例、设定截止日期及附带威胁内容，全程以谈判姿态逼迫黑客立即配合。

若黑客拒绝该交易，冒充Balancer的诈骗者威胁称，将动用从区块链取证专家、执法机构及监管合作伙伴处获取的所有信息，定位并起诉攻击者。

此次Balancer攻击是2025年规模最大的加密货币盗窃事件之一。目前攻击责任方尚未确定，但去中心化金融（DeFi）领域机构面临的最大威胁来自朝鲜黑客组织。

到今年10月为止，与朝鲜黑客盗窃相关的加密货币金额已超过20亿美元，其中规模最大的是2月发生的Bybit交易所攻击事件，黑客当时窃取了15亿美元的加密货币。

文章翻译自：https://www.bleepingcomputer.com/news/cryptocurrency/hacker-steals-over-120-million-from-balancer-defi-crypto-protocol/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?9pLf6VsO)

#### 你可能感兴趣的

* [![]()

  Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)
* [![]()

  TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)
* [![]()

  恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)
* [![]()

  Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
* [![]()

  8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
* [![]()

  黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)
  2025-11-11 12:00:00
* [TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)
  2025-11-10 12:00:00
* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)
  2025-11-06 12:00:00
* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
  2025-11-05 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)

  胡金鱼
* [TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)

  胡金鱼
* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)

  胡金鱼
* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)

  胡金鱼
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)

  胡金鱼
* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)