---
title: 标准实践 | T/TAF 078.7-2022 “摇一摇”乱跳转相关条款技术解析
url: https://www.4hou.com/posts/3r7R
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-12
fetch_date: 2025-10-06T17:16:01.519089
---

# 标准实践 | T/TAF 078.7-2022 “摇一摇”乱跳转相关条款技术解析

标准实践 | T/TAF 078.7-2022 “摇一摇”乱跳转相关条款技术解析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 标准实践 | T/TAF 078.7-2022 “摇一摇”乱跳转相关条款技术解析

爱加密
[技术](https://www.4hou.com/category/technology)
2024-05-11 18:15:28

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)217998

收藏

导语：为协助各App开发者了解工信部查处标准，特编写本文解读标准相关内容。

![蓝色渐变毛玻璃求职招聘微信公众号封面.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407792604592.png "1715407792604592.png")

24年3月，工信部发布《关于侵害用户权益行为的APP（SDK）通报（2024年第2批，总第37批）》，对“摇一摇”乱跳转、信息窗口“关不掉”加强管理，工信部自2024年起于通报中强调本类问题，未来或将持续加强管理。为协助各App开发者了解工信部查处标准，特编写本文解读标准相关内容。

**一、通报依据**

“摇一摇”乱跳转问题查处依据工信部26号文及《T/TAF 078.7-2022 APP用户权益保护测评规范》。

在工信部26号文中提及：“开屏和弹窗信息窗口提供清晰有效的关闭按钮，保证用户可以便捷关闭；不得频繁弹窗干扰用户正常使用，或利用“全屏热力图”、高灵敏度“摇一摇”等易造成误触发的方式诱导用户操作。”

《T/TAF 078.7-2022 APP用户权益保护测评规范》对欺骗误导强迫用户点击跳转的情况细化为了4种情况，并对交互动作数值给出了明确限制，APP 欺骗误导强迫用户点击跳转，具体场景包括但不限于以下方式：

1、APP以欺骗、误导或者强迫等方式向用户提供互联网信息服务或者产品；

2、未以显著方式明示或未经用户主动选择同意，APP 信息窗口页面，存在跳转、使用第三方的行为；

3、APP信息窗口页面，跳转、使用第三方时，存在欺骗误导强迫用户跳转的文字、图片或视频链接；

4、APP信息窗口通过用户“摇一摇”等交互动作触发页面或第三方应用跳转的，未清晰明示用户需要执行的触发动作及交互预期，或通过设置高灵敏度降低交互动作判定阈值，造成误导、强迫式跳转。

注：触发用户跳转的交互动作可参照如设备加速度不小于15m/s2，转动角度不小于35°，操作时间不少于3s，或同时考虑加速度值与方向、转动角度的方式，或与前述单一触发条件等效的其他参数设置，确保用户在走路、乘车、拾起放下移动智能终端等日常生活中，非用户主动触发跳转的情况下，不会出现误导、强迫跳转。

**二、常见违规原因**

1、触发时操作时间小于3S&加速度小于15m/s

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407709174900.png "1715407326199502.png")

2、转动角度小于35°&操作时间少于3s

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407710682227.png "1715407384538707.png")

如不符合上述要求，将导致用户在走路、公共交通或甩手等日常使用场景下造成误触发，严重影响用户日常使用。企业此类违规行为完全无法欺瞒监管机构，爱加密作为各大监管机构支撑单位，可轻易检测出企业具体转动角度、加速度，给出整改意见。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407710160640.png "1715407446641101.png")

**三、如何查控参数**

目前大多数App开发者依赖第三方广告SDK实现“摇一摇广告”，App开发者仅能调控是否开启“摇一摇广告”，无法调控具体触发精度。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407711860434.png "1715407497194362.png")

由于“摇一摇广告”检测难度较大，涉及大量专业模拟器、特定代码检测，常规App开发者完全无力检测广告SDK设置的具体参数，将App违规风险、用户体验置于广告SDK。**对于力求App合规运营的企业而言，急寻通过个人信息检测机构在应用上架前及购物节前检测App“摇一摇广告”参数**。

目前，每逢“618”、“双十一”等大型购物节，在用户感知中开屏摇一摇广告变得更易触发，且落地页均为3大电商平台。因此引发海量用户的反感，并促使工信部自2024年起针对性查处并通报批评，通报名单中包含多款BAT旗下核心App。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407712452799.png "1715407546273480.png")

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407713108073.png "1715407570142400.png")

爱加密基于法规内容，适配自动化检测，在检测过程中模拟”设备加速度不小于 15m/s2，转动角度不小于 35°，操作时间不少于 3s”的加速度传感器、陀螺仪传感器参数，看是否触发广告跳转。

如小于法规规定的情形产生了跳转行为，判断APP违规。基于模拟传感器的实现，我们同时推出了深度检测的模拟传感器，用户可通过实时投屏，同步操作APP。在必现的“摇一摇”广告中验证是否合规。用户可通过预设加速度传感器、操作时间、和角速度传感器的数值，在进入“摇一摇”广告或可触发跳转的其他页面时，触发传感器。我们将按照预设的数值模拟，此时观察是否触发跳转，达到人工检测的目的。

**爱加密已实现模拟传感器检测“摇一摇”跳转广告的方案**，需要手动输入多组数据进行实验，在法规规定的数值“设备加速度不小于 15m/s2，转动角度不小于 35°，操作时间不少于 3s”范围多次测试验证，确认是否违规。

为了接近真实使用场景，提高实验准确性，与国内某实验室合作，通过电机、固定装置、蓝牙模块、外置传感器等机械装置，组成机械臂；与平台链接，同时记录蓝牙传感器的加速度、角速度和手机传感器的加速度和角速度等数据，且手机在机械臂中为固定方向，更好的形成对照组和实现组数据，减少多个方向晃动产生多组数据影响结果评估。调整电机档位，实现不同粒度的“摇一摇”复现实际用户使用情况。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240511/1715407714886832.png "1715407664185627.png")

爱加密时刻关注我国的移动应用安全发展状况，致力于通过优质的核心技术服务监管部门及企业，从行业实践角度着手大力推动我国移动应用生态的良好发展。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0hGZh50t)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/portraits/d5e3fd1b7ee8329a1891c67842713376.png)

# [爱加密](https://www.4hou.com/member/zrDm)

服务企业及开发者用户50万+，保护移动应用100万+

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/zrDm)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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