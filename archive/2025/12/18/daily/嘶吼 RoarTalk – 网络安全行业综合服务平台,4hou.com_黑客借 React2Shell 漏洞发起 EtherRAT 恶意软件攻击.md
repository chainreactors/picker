---
title: 黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击
url: https://www.4hou.com/posts/J1v9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-18
fetch_date: 2025-12-19T03:22:04.236741
---

# 黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击

黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)5802

收藏

导语：EtherRAT整合了多项复杂功能，包括基于区块链的命令与控制（C2）通信、多层Linux持久化、载荷实时重写，以及依托完整Node.js运行时环境实现的反检测能力。

在近期的React2Shell漏洞攻击事件中，一款名为EtherRAT的新型恶意植入程序被安全研究人员发现，该程序不仅内置五种独立的Linux系统持久化机制，还会借助以太坊智能合约与攻击者建立通信链路。

研究人员认为，这款恶意软件的特征与朝鲜黑客组织在Contagious Interview攻击活动中使用的工具相符。他们在React2Shell高危漏洞（CVE-2025-55182）披露仅两天后，便从某遭入侵的Next.js应用中成功提取到EtherRAT样本。

EtherRAT整合了多项复杂功能，包括基于区块链的命令与控制（C2）通信、多层Linux持久化、载荷实时重写，以及依托完整Node.js运行时环境实现的反检测能力。尽管其与朝鲜Lazarus组织发起的Contagious Interview攻击存在诸多特征重合，但在多个核心层面仍具备独特性。

React2Shell是React服务端组件（RSC）Flight协议中存在的最高级别反序列化漏洞，攻击者可通过特制HTTP请求实现无认证远程代码执行。

该漏洞影响大量运行React/Next.js的云环境，在上周漏洞公开数小时后便已出现野外利用。随着自动化攻击工具的普及，已有跨多个行业的至少30家组织机构遭入侵，攻击者借此窃取凭证、开展加密货币挖矿，并部署通用型后门程序。

**EtherRAT的攻击链路**

Sysdig指出，EtherRAT采用多阶段攻击链路，其流程如下：

1. 漏洞利用与初始载荷投放：首先通过React2Shell漏洞在目标设备上执行Base64编码的Shell命令，该命令会尝试通过curl、wget或python3（备选）工具下载恶意Shell脚本s.sh，并每300秒循环执行一次直至下载成功。脚本获取后会先经过校验，再被赋予可执行权限并启动。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251210/1765354504579022.png "1765354070410446.png")

脚本逻辑

2. 运行时环境部署：脚本会在用户目录$HOME/.local/share/下创建隐藏文件夹，从nodejs.org直接下载并解压合法的Node.js v20.10.0运行时环境。随后写入加密载荷数据块与混淆后的JavaScript投放器，通过已下载的Node二进制文件执行投放器，执行完毕后脚本会自行删除。

3. 恶意程序解密与加载：名为.kxnzl4mtez.js的混淆JavaScript投放器会读取加密数据块，通过硬编码的AES-256-CBC密钥完成解密，并将解密结果写入另一隐藏JavaScript文件。该解密后的文件即为EtherRAT植入程序，最终通过前一阶段安装的Node.js环境完成部署。

**高级植入程序的核心特征**

**基于以太坊智能合约的C2通信**

EtherRAT采用以太坊智能合约实现C2操作，该方式不仅具备灵活的运营能力，还能有效抵御反制与关停措施。其会并行查询9个公共以太坊RPC节点，并以多数节点的响应结果为准，可防止单点节点投毒或域名劫持攻击。

此外，该恶意软件每500毫秒便会向C2发送随机生成的类CDN格式URL，并通过AsyncFunction构造器执行攻击者下发的JavaScript代码，形成可完全交互的Node.js命令行环境。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251210/1765354508593801.png "1765354119520086.png")

构建随机URL

朝鲜黑客此前便曾使用智能合约进行恶意软件投放与分发，该技术被称为EtherHiding，谷歌与GuardioLabs均曾发布相关技术报告。

**Linux系统的五层持久化机制**

EtherRAT在Linux系统中具备极强的持久化能力，通过部署五层冗余机制确保控制权不丢失，具体包括：

**·**定时任务（Cron jobs）

**·**bashrc配置注入

**·**XDG自动启动项

**·**Systemd用户服务

**·**配置文件（Profile）注入

借助多维度持久化手段，即便目标系统经历重启或运维操作，攻击者仍能维持对受感染设备的访问权限。

**自主更新与载荷重混淆能力**

EtherRAT的另一独特功能是可通过向API端点发送自身源代码实现自主更新。其会接收功能一致但混淆方式不同的替换代码，完成自身覆盖后启动新进程运行更新后的载荷。该机制既能帮助恶意软件规避静态检测，也可阻碍逆向分析，同时支持按需加载特定攻击功能。

鉴于目前React2Shell漏洞已被多方黑客组织利用，系统管理员需尽快将React/Next.js版本升级至安全版本。研究人员建议用户应快速排查上述持久化机制的存在痕迹、监控以太坊RPC相关流量、审计应用程序日志，并及时轮换各类账户凭证。

文章来源自：https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-react2shell-flaw-in-etherrat-malware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?dYa2eggI)

#### 你可能感兴趣的

* [![]()

  黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
* [![]()

  漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)
* [![]()

  新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
* [![]()

  漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)
* [![]()

  微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
* [![]()

  Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
  2025-12-18 12:00:00
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)
  2025-12-11 15:50:27
* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
  2025-12-09 12:00:00
* [漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)
  2025-12-04 16:57:08

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)

  胡金鱼
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)

  盛邦安全
* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)

  胡金鱼
* [漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)

  盛邦安全
* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)

  胡金鱼
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)

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