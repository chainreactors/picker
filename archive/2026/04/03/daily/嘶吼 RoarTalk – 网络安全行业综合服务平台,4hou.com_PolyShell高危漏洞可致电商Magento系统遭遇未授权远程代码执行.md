---
title: PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行
url: https://www.4hou.com/posts/jBG4
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-04-03
fetch_date: 2026-04-04T04:10:35.676763
---

# PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行

PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2026-04-03 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7509

收藏

导语：​本次高危漏洞命名“PolyShell”，核心特征为攻击者上传多格式兼容恶意文件，该文件既可伪装成常规图片绕过安全检测，又能解析执行后台恶意脚本后门。

近期，一则名为“PolyShell”的高危新型漏洞被公开披露，该安全漏洞影响所有Magento开源版与Adobe Commerce 2系列稳定版电商系统，攻击者无需登录身份认证，即可远程执行恶意代码、窃取接管管理员账号权限。

目前安全监测暂未捕获野外大规模实战挖矿勒索攻击，但Sansec紧急预警：完整漏洞攻击利用链已在地下黑产圈层流通扩散，自动化批量扫描爆破攻击或将很快全面爆发。

Adobe官方虽已紧急推送安全修复补丁，但该补丁仅内嵌于2.4.9版本第二轮Alpha测试预览版，正式商用生产稳定版暂未迭代更新，全网大量在线运营商城仍处于高危未防护裸奔状态。

Sansec补充说明，Adobe同步提供简易Web服务器防护配置模板，可大幅限制漏洞攻击危害扩散范围，但绝大多数中小企业商城均直接沿用云主机服务商默认一键建站配置，无自定义加固能力。

据Sansec发布的分析报告表示：Magento电商平台REST API接口，在处理购物车商品自定义附加选项时，违规开放恶意文件上传高危权限。

安全研究员拆解攻击原理：“当商品自定义选项设定为‘文件上传’类型时，系统会默认解析内嵌file\_info数据包，自动解码Base64加密恶意文件载荷、识别伪造MIME资源类型、读取伪装文件名，最终直接落地写入服务器 pub/media/custom\_options/quote/公开可访问目录。”

本次高危漏洞命名“PolyShell”，核心特征为攻击者上传多格式兼容恶意文件，该文件既可伪装成常规图片绕过安全检测，又能解析执行后台恶意脚本后门。

漏洞实际危害严重依赖服务器Web环境配置，通杀两大高危攻击链：轻则实现远程代码执行（RCE）接管服务器权限，重则植入存储型XSS恶意脚本劫持管理员后台会话Cookie，一键窃取全站账号权限，Sansec抽样全网监测显示，绝大多数商城默认配置均暴露上传目录高危风险。

在Adobe正式推送商用生产版安全补丁前，安全研究员建议商城运维管理员立即落地三大临时应急加固防护措施：

1. 严格限制封禁pub/media/custom\_options/目录外网直接访问权限；

2. 深度核查Nginx/Apache核心防护规则，确认目录拦截策略永久生效；

3. 全盘深度扫描服务器目录，排查清除已上传恶意网页后门、木马挖矿程序及各类窃听恶意软件。

文章来源自：https://www.bleepingcomputer.com/news/security/new-polyshell-flaw-allows-unauthenticated-rce-on-magento-e-stores/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?wWDf8nL9)

#### 你可能感兴趣的

* [![]()

  PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行](https://www.4hou.com/posts/jBG4)
* [![]()

  VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥](https://www.4hou.com/posts/0MlN)
* [![]()

  蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)
* [![]()

  谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
* [![]()

  思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)
* [![]()

  多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行](https://www.4hou.com/posts/jBG4)
  2026-04-03 12:01:00
* [VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥](https://www.4hou.com/posts/0MlN)
  2026-03-31 12:00:00
* [蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)
  2026-03-11 12:00:00
* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)
  2026-03-02 11:49:21

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [PolyShell高危漏洞可致电商Magento系统遭遇未授权远程代码执行](https://www.4hou.com/posts/jBG4)

  胡金鱼
* [VoidStealer恶意软件利用调试器漏洞窃取Chrome主密钥](https://www.4hou.com/posts/0MlN)

  胡金鱼
* [蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测](https://www.4hou.com/posts/kgyK)

  胡金鱼
* [谷歌API密钥安全漏洞曝光：前端暴露密钥可直接访问Gemini并窃取隐私数据](https://www.4hou.com/posts/kgyv)

  胡金鱼
* [思科Catalyst SD-WAN严重认证绕过漏洞遭长期入侵，可植入恶意节点控制网络](https://www.4hou.com/posts/vwNM)

  胡金鱼
* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)

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