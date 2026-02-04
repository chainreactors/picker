---
title: 蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用
url: https://www.4hou.com/posts/BvDW
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-03
fetch_date: 2026-02-04T04:05:54.462711
---

# 蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用

蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用

企业资讯
[行业](https://www.4hou.com/category/industry)
19小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8835

收藏

导语：AI数字分身，让安全运营分钟级响应。

1月29-30日，由四川警察学院、公安部网络安全等级保护中心主办的2026年网络安全等级保护技术学术交流活动在成都举行。活动以“科技赋能·筑基强网”为主题，多名来自国内网络安全领域的权威技术、法律专家分享了新技术及热点研究成果。**蚂蚁集团天宸实验室主任刘焱出席本次交流活动，并做《网络安全垂域大模型在安全运营场景下的数字分身应用》主题分享**。

![人物.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20260203/1770107643139588.jpg "1770107643139588.jpg")

刘焱指出，高度复杂业务使安全保障任务面临巨大挑战，如

**数据内视能力不足**：检测系统过度依赖单一数据源，缺乏对应用层、操作系统等多维数据的全面监控；

**攻击检测能力不足**：攻击行为复杂多变、内部体系架构繁杂，大量用于风险研判的运行时上下文缺失，导致研判结论偏差，出现告警风暴；

**响应联动不足**：AI驱动的自动化攻击成本降低，并且以多种手段隐藏身份，防御方自动化分析难度高，全链路回溯挑战巨大，人均响应能力与攻击规模严重失衡。

刘焱表示，真正制约大模型落地效果的并非模型本身能力，而是数据的质量与深度。现有安全建设中存在四大数据源“深度”问题：数据难以还原事实本源、采集范围受限于现有技术手段、观测时机窗口易缺失、海量数据无法持久储存。

对此，蚂蚁集团首创了安全平行切面体系，该体系基于AOP（面向切面编程）思想，实现非侵入式数据采集与逻辑注入，在不修改应用源码的情况下给程序动态添加或修改功能，并通过切面平行舱保证其有序运行，即在不影响业务运行的情况下获取深层执行数据，提供精准的安全内视与干预服务。蚂蚁集团围绕安全平行切面打造了企业安全建设的基础设施，实现了威胁对抗能力与效率的跨越式提升。

在数据采集层面，应用安全平行切面后，可以实现“日志自由”。例如，在JAVA服务器中检测内存马时，按照传统常见的方法需要在敏感节点打日志、修改代码，如使用的是招聘等第三方系统，操作则会更加复杂。但应用切面技术后，仅仅需要关注三个关键函数，对读取后的数据进行研判即可，全过程无需升级软件本身。

![场景.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20260203/1770107672115161.jpg "1770107672115161.jpg")

刘焱提到，大模型并非万能，实践发现其用于威胁检测细分领域时存在局限性，尤其是在“信息不足”时，其严重的幻觉问题会导致其研判错误。蚂蚁集团提出的DKCF大模型推理可信应用框架，是对大模型专业应用可信问题解决之道的探索，其中D指的是充足的数据供给；K指的是专业知识工程，包括了行业数据集和专业知识图谱对齐；C指的是协同规划、编排，把高难度问题拆解为多个简单问题，人类专家与AI专家融合演进；F指的是高效核验、反馈，并根据反馈内容不断迭代。

在威胁检测领域中，切面与DKCF结合，可以实现全域联动获取数据，能精准感知威胁、定性事件、智能定损。

**在数据层面**，安全平行切面技术的信息采集解耦，提供了“数据和日志自由”；

**在知识层面**，利用大模型对多维实时行为序列抽取，构建主客凭据关联以及行为依赖生成行为知识图谱，结合ATT&CK技战术领域知识库，提供分析依据；

**在协同层面**，基于用户行为链构建行为序列校验引擎，实现了检测智能体调用链，融合专家智能和机器智能；在核验、反馈层面，残差分析、反馈弥补了各层次（策略、知识、能力等）不足，解决了误报多、未知威胁发现能力弱、可解释性差的痛点。

实践落地中，大模型威胁检测风险研判的“判黑”准确率超85%，召回率超95%，响应时间从30分钟以上缩短至分钟级。

演讲的最后，刘焱表示，大模型时代，工作范式发生了变化，从人工操作转变为人机协同，目前阶段的人机协同从以人为主过渡到以AI为主，人工参与解决AI遇到的难题。未来，对于安全运营的愿景是让AI成为工作人员的数字分身，去承担枯燥、重复的工作，安全团队则作为“指挥官”，聚焦更高价值的安全研究、 “攻防边界”探索，推动网络安全更好的发展。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?eUOJmsV2)

#### 你可能感兴趣的

* [![]()

  【梆梆安全监测】安全隐私合规监管趋势及漏洞风险报告（1123-1206）](https://www.4hou.com/posts/2XYj)
* [![]()

  应对在线作弊挑战：教育平台移动端安全监测与主动防御实践](https://www.4hou.com/posts/rpzB)
* [![]()

  面向智能家居与数字零售：梆梆安全制造业移动应用一体化安全解决方案](https://www.4hou.com/posts/qoyD)
* [![]()

  蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用](https://www.4hou.com/posts/BvDW)
* [![]()

  嘶吼快讯|网安厂商动态汇（第9期）](https://www.4hou.com/posts/zA1O)
* [![]()

  2026开门红，CACTER又双叒获3大奖项认可](https://www.4hou.com/posts/ArBp)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [【梆梆安全监测】安全隐私合规监管趋势及漏洞风险报告（1123-1206）](https://www.4hou.com/posts/2XYj)
  2026-02-03 17:11:12
* [应对在线作弊挑战：教育平台移动端安全监测与主动防御实践](https://www.4hou.com/posts/rpzB)
  2026-02-03 17:08:16
* [面向智能家居与数字零售：梆梆安全制造业移动应用一体化安全解决方案](https://www.4hou.com/posts/qoyD)
  2026-02-03 17:05:42
* [蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用](https://www.4hou.com/posts/BvDW)
  2026-02-03 16:35:06

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [【梆梆安全监测】安全隐私合规监管趋势及漏洞风险报告（1123-1206）](https://www.4hou.com/posts/2XYj)

  梆梆安全
* [应对在线作弊挑战：教育平台移动端安全监测与主动防御实践](https://www.4hou.com/posts/rpzB)

  梆梆安全
* [面向智能家居与数字零售：梆梆安全制造业移动应用一体化安全解决方案](https://www.4hou.com/posts/qoyD)

  梆梆安全
* [蚂蚁集团刘焱：网络安全垂域大模型在安全运营场景下的数字分身应用](https://www.4hou.com/posts/BvDW)

  企业资讯
* [嘶吼快讯|网安厂商动态汇（第9期）](https://www.4hou.com/posts/zA1O)

  胡金鱼
* [2026开门红，CACTER又双叒获3大奖项认可](https://www.4hou.com/posts/ArBp)

  CACTER

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