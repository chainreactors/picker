---
title: 守护最后一道防线:Coremail邮件安全网关推出邮件召回功能
url: https://www.4hou.com/posts/MBR5
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-25
fetch_date: 2025-10-04T08:02:31.320603
---

# 守护最后一道防线:Coremail邮件安全网关推出邮件召回功能

守护最后一道防线:Coremail邮件安全网关推出邮件召回功能 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 守护最后一道防线:Coremail邮件安全网关推出邮件召回功能

CACTER
[行业](https://www.4hou.com/category/industry)
2023-02-24 10:03:48

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113542

收藏

导语：根据Coremail邮件安全大数据中心2022年Q4季报显示，2021年CAC识别钓鱼邮件1.81亿，2022年上升至2.25亿，增幅高达24.1%。

根据Coremail邮件安全大数据中心2022年Q4季报显示，2021年CAC识别钓鱼邮件1.81亿，2022年上升至2.25亿，增幅高达24.1%。

这表明2022年平均每天有61万7088封钓鱼邮件被接收及发出，企业用户面临潜在经济损失不可估量。

![1677121428107752.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230223/1677121476142489.png "1677121428107752.png")

尤其是活跃至今的诈骗补贴钓鱼邮件，从2021年Coremail曝光披露以来，黑产团伙为逃避邮件厂商反垃圾反钓鱼引擎检测，钓鱼手法发生了三次变化。

![1677121486130066.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230223/1677121486130066.png "1677121486130066.png")

诈骗补贴钓鱼样例

**阶段一**

初始阶段，黑产团伙常常冒充国家相关部门下发钓鱼邮件，主题为【工资补贴通知】【《2022财务补贴声明》】。此阶段诈骗补贴邮件由正文+主题+钓鱼网站二维码构成，诱导用户扫码进入仿冒银行网站，目的是套取银行账密，转账卡内余额。

**阶段二**

随着市面邮件系统厂商逐渐加强对【诈骗补贴】邮件的检测拦截，黑产团伙的钓鱼手法转变为先盗号，使用被盗账号伪装公司“财务部”“人事部”等内部员工，向域内大量传播诈骗邮件，利用域内邮箱的高信用度逃避反垃圾反钓鱼检测。

**阶段三**

Coremail在与黑产团伙的多轮攻防中发现，目前【诈骗补贴】钓鱼手法已由常规的图片嵌入，转变为html标签引用附件ID展示二维码。由于二维码图片不是直接以图片的形式嵌入，导致图片提取引擎无法以原有逻辑提取二维码，对邮件厂商的反垃圾反钓鱼引擎产生极大考验。

![1677121500139496.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230223/1677121500139496.png "1677121500139496.png")

钓鱼诈骗屡禁不绝，令人防不胜防。

为进一步加强邮件系统安全，Coremail全新推出邮件威胁事后处置方案——邮件召回！

![1677121528188216.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230223/1677121528188216.jpeg "1677121528188216.jpeg")邮件召回方案主要针对新型变种威胁邮件绕过反垃圾反钓鱼反病毒引擎检查，甚至是云沙箱检测，成功投递至邮件系统无法撤回时，企业管理员可以启用CACTER邮件安全网关的邮件召回功能，一键召回已经投递至邮件系统的威胁，守护邮箱系统安全最后一道防线。

![](https://pic4.zhimg.com/80/v2-0844469529481f524822f732f1b82fa7_1440w.webp)CACTER邮件网关召回方案需与Coremail邮件系统深度绑定，操作便捷，一旦出现安全事件，管理员进行一键召回操作后，不仅不影响终端邮箱用户的使用，且用户无任何感知，可极大降低企业安全事故衍生风险。

邮件网关召回方案是Coremail聚焦25000+客户的实际痛点全新研发，面对钓鱼诈骗手法层出不穷，“黑灰产”推波助澜的情况下，仅聚焦于互联网（外域）投递至邮件系统（内域）的威胁邮件是不够的，必须不断迭代网关功能版本为客户提供事前—事中—事后的全链条保障服务，通过综合性解决方案，为客户邮件系统业务运行保驾护航

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?FgLVqy2p)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/789873803bbe1d5cf9b06a0859e2af0b.png)

# [CACTER](https://www.4hou.com/member/64Y9)

国内领先企业级邮件安全解决方案提供商，提供一站式防护。

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/64Y9)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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