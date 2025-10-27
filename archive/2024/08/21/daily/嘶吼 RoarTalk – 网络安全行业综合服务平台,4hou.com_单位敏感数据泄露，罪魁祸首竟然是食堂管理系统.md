---
title: 单位敏感数据泄露，罪魁祸首竟然是食堂管理系统
url: https://www.4hou.com/posts/Ey8k
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-21
fetch_date: 2025-10-06T18:01:03.527207
---

# 单位敏感数据泄露，罪魁祸首竟然是食堂管理系统

单位敏感数据泄露，罪魁祸首竟然是食堂管理系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 单位敏感数据泄露，罪魁祸首竟然是食堂管理系统

盛邦安全
[行业](https://www.4hou.com/category/industry)
2024-08-20 10:24:15

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)62431

收藏

导语：单位敏感数据泄露，罪魁祸首竟然是食堂管理系统

近日，在为某国企单位进行网络安全保障期间，盛邦安全RayAPI产品监测到智慧食堂管理系统信息查询接口存在未鉴权风险，可导致大量敏感信息泄露，包括账号信息、身份照片及系统运行日志等，随后，安全研究人员对该风险进行了详细的验证。

**验证步骤**

1、RayAPI发现智慧食堂管理系统信息查询接口存在未鉴权风险。

![QQ截图20240815170207.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723785668103820.png "1723785600366758.png")

2、关联攻击检测策略进行分析，发现针对该接口存在漏洞利用攻击尝试。

![QQ截图20240815170231.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723785668863250.png "1723785623133636.png")

3、查看接口返回信息，发现存在手机号、身份证信息等敏感数据泄露事件。

![QQ截图20240815170256.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723785669213001.png "1723785640227190.png")

4、对接口敏感信息进行检测分析，发现除个人隐私信息外，还涉及大量账号信息，其中包括各类摄像头、售卖机和消费机等终端的管理IP及账号口令。

![QQ截图20240815170320.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723785669357229.png "1723785657140486.png")

5、进行主动验证测试，发现通过该接口可以直接批量获取敏感信息。

**我们的建议**

近年来，随着企业信息化、数字化的转型与升级，智慧园区建设当中也不断引入各类新型系统来打通管理流程，例如智慧食堂管理系统，此类系统往往涉及大量员工个人信息，并与其他企业管理系统通过API接口互通，同时又容易被安全运维人员所忽视。对此，我们从系统建设与安全治理两方面给出如下建议：

**1、系统建设层面**

（1）加强API接口权限控制，尤其针对涉敏类接口，除必要的认证手段之外，还应设定合理的访问频率限制，防止接口被恶意爬取；

（2）加强敏感数据管控措施，尤其针对个人隐私信息，一方面需建立必要的加密传输手段，另一方面需减少非必要的数据内容传输，防止数据过度暴露。

**2、安全治理层面**

（1）做好接口暴露风险检测。以RayAPI为例，通过对接口类型、调用内容与访问轨迹等条件的关联检测，识别敏感接口的误暴露风险情况；

![QQ截图20240815170431.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723785694125595.png "1723785694125595.png")

（2）做好接口异常行为检测。以RayAPI为例，通过对接口访问频次、数据调用规模的趋势分析，识别可能存在的接口攻击行为，并配合安全基线要求设定访问控制策略。

![QQ截图20240815170509.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240816/1723785708890452.png "1723785708890452.png")

[原文链接](https://mp.weixin.qq.com/s?__biz=MzAwNTAxMjUwNw==&mid=2650276257&idx=1&sn=0b4cee9264a03374e46f3358e6359f5b&chksm=832f8cd5b45805c336fba3716cc21e551142526c5ae21ba60c49e24f093873d1f5f2461fa995&token=606558572&lang=zh_CN#rd)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Fy735u4N)

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

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

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