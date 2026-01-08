---
title: CSTIS：关于防范SleepyDck恶意软件的风险提示
url: https://www.4hou.com/posts/kgYr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-07
fetch_date: 2026-01-08T03:29:05.519719
---

# CSTIS：关于防范SleepyDck恶意软件的风险提示

CSTIS：关于防范SleepyDck恶意软件的风险提示 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# CSTIS：关于防范SleepyDck恶意软件的风险提示

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12954

收藏

导语：SleepyDuck是一种极具威胁性的复杂远程访问木马（RAT）。

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测发现SleepyDuck恶意软件持续活跃，其主要攻击目标为使用Cursor和Windsurf等代码编辑器的开发者，可能导致数据泄露、系统受控、业务中断等风险。

SleepyDuck是一种极具威胁性的复杂远程访问木马（RAT），于2025年10月31日以“juan-bianco.solidity-vlang”名称首次在OpenVSX市场发布，11月1日更新至0.0.8版本并植入恶意功能。该恶意软件通过名称抢注技术（攻击者抢先注册与合法软件、品牌等高度相似名称，伪装成可信来源诱骗用户下载恶意软件的手段）伪装成合法Solidity工具，当用户打开新代码编辑器窗口或选择.sol文件时该恶意软件被激活。激活后，它首先收集主机名、用户名、MAC地址、时区等机器信息，并通过创建锁定文件确保单次执行、调用伪装函数初始化恶意载荷、使用沙箱环境执行命令等技术规避检测。随后，该恶意软件连接主命令与控制（C2）服务器sleepyduck[.]xyz，以30秒轮询间隔接收指令，可远程完全控制受感染的Windows系统、窃取敏感数据、执行恶意命令。SleepyDuck核心特点是利用以太坊区块链合约实现高级持久化——将备用配置数据存储在以太坊合约地址0xDAfb81732db454DA238e9cFC9A9Fe5fb8e34c465。当主C2服务器失效时，SleepyDuck会查询该不可篡改的区块链合约，获取更新后的服务器地址、轮询间隔甚至紧急命令。此外，它采用去中心化的基础设施，即便主域名被查封也能维持运营，大幅提升了安全监测分析的难度。

建议相关单位和用户立即组织排查，更新防病毒软件，实施全盘病毒查杀，卸载相关恶意扩展，仅从官方市场下载开发工具，并严格验证开发者身份，加强网络监控，阻断与sleepyduck[.]xyz及特定以太坊合约地址的非法交互，并可通过定期备份数据等措施，防范网络攻击风险。

文章来源自：网络安全威胁和漏洞信息共享平台

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gHmI6OBI)

#### 你可能感兴趣的

* [![]()

  2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)
* [![]()

  CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)
* [![]()

  仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)
* [![]()

  Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)
* [![]()

  《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)
* [![]()

  新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)
  2026-01-07 12:00:00
* [CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)
  2026-01-07 11:48:18
* [仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)
  2026-01-06 12:00:00
* [Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)
  2026-01-05 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)

  山卡拉
* [CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)

  胡金鱼
* [仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)

  胡金鱼
* [Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)

  胡金鱼
* [《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)

  胡金鱼
* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)

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