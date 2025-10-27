---
title: 勒索病毒Coffee新变种“卷土重来” 360防勒索解决方案教你轻松拿捏
url: https://www.4hou.com/posts/6VQO
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-16
fetch_date: 2025-10-04T01:38:48.004797
---

# 勒索病毒Coffee新变种“卷土重来” 360防勒索解决方案教你轻松拿捏

勒索病毒Coffee新变种“卷土重来” 360防勒索解决方案教你轻松拿捏 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索病毒Coffee新变种“卷土重来” 360防勒索解决方案教你轻松拿捏

企业资讯
[行业](https://www.4hou.com/category/industry)
2022-12-15 15:07:41

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)956733

收藏

导语：近日，360数字安全集团高级威胁研究分析中心（CCTGA勒索软件防范应对工作组成员）监测到针对我国高校与科研机构的Coffee勒索病毒再次出现了新变种，这是继Coffee勒索病毒在2022年1月首次出现后的再度“升级”。

近日，360数字安全集团高级威胁研究分析中心（CCTGA勒索软件防范应对工作组成员）监测到针对我国高校与科研机构的Coffee勒索病毒再次出现了新变种，这是继Coffee勒索病毒在2022年1月首次出现后的再度“升级”。

经360安全分析团队研判分析，新变种对加密触发方式、加密格式、远程勒索shellcode C2获取方式等进行了更新调整。新变种通过邮箱传播，加密过程更加隐蔽，潜伏期最多可长达15天，同时使用DNS隧道技术来获取C2信息，免杀能力更强，需引起高度重视和警惕。

**Coffee勒索病毒新变种的特征对比分析**

据了解，相较于前期主要通过群发钓鱼邮件、QQ群文件、QQ自动发送等方式进行传播，Coffee勒索病毒新变种主要通过邮箱传播，加密过程更加隐蔽。截止目前，该勒索病毒经过多次版本迭代，下图为对该勒索病毒主要两次版本变化的比较：

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671087797198955.png "1671087797198955.png")

此外，新变种的加密算法和之前版本并未发生变化，仍然使用RC4加密，以获得快速加密的效果。新变种对触发加密的条件做了限制，使加密过程更加隐蔽！新变种还在获取远程payload地址的方式进行了调整，使用了DNS隧道的方法，在C2信息隐藏在了域名的txt记录中。同时勒索信相关的帮助链接也采用了类似的方式来进行解析更新。

在执行方面，新版病毒也使用了新的免杀手段，在白利用加载的dll会随机生成大小为20-50M的文件，以提升杀软收集样本的难度，躲避杀软查杀。病毒在运行后，会弹出假的VC运行库错误提示框，以迷惑用户。

**Coffee勒索病毒快速蔓延**

**360防勒索整体解决方案精准出击**

360防勒索整体解决方案从“云、管、端、地、险”五个维度出发，利用360本地安全大脑、360高级持续性威胁预警系统（360 NDR）、360终端安全检测响应系统（360 EDR）等多款安全产品及360安全服务，帮助用户感知风险、看见威胁、抵御攻击，实现多方位、全流程、体系化的勒索防护。

360本地安全大脑汇聚终端、流量、业务访问等全场景行为数据，通过大数据分析平台进行集中存储和快速检索，进而实现对所有可疑活动的持续监测，360云端专家7\*24h值守，协助研判可疑事件，快速发现、分析处置异常行为。360本地安全大脑基于360 EDR、360 NDR的行为类日志开发的XDR分析规则可以检测Coffee勒索软件使用的攻击技战术，确定影响实体范围、联动EDR对受影响主机快速阻断进程、隔离下线，截图为检测其查询域名DNS设置中TXT记录获取C2地址的行为：

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671087829132317.png "1671087829132317.png")

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671087846198142.png "1671087846198142.png")360 NDR文件检测报告截图

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671087866389259.png "1671087866389259.png")

360 NDR流量监测预警截图

360 EDR针对Coffee家族的勒索病毒，通过主动监控功能，当用户通过QQ、微信、邮件、共享文件夹等方式将coffee病毒文件在终端落地时，会进行病毒检测可以检出病毒文件；也可以通过快速查杀、定时查杀对磁盘文件进行病毒检测的时候扫描发现coffee病毒。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671087890212042.png "1671087890212042.png")

360安全服务在防护产品自动检测扫描的基础上，进行二次检查与加固，补充安全产品能力，实现快速响应，全面发现并彻底清理客户业务主机的漏洞。同时，360安全服务专家还可以将用户业务与云、管、端告警和情报结合，还原勒索攻击全貌，提供全面、专业的分析结论并提出针对性建设意见，确保用户防护设备可以防护此勒索病毒风险。

该病毒主要攻击高校与科研院所，用户在收到来历不明的邮件时，务必谨慎访问。360在此提醒用户：首先，安装并使用安全软件，不随意退出防护功能；其次，谨慎打开QQ消息，QQ群共享文件，以及邮件附件中的文件，打开这些文件时，如果安全软件提示拦截或报毒，切勿继续执行。目前，360解密大师已经第一时间支持该勒索病毒解密，受到Coffee勒索病毒影响的用户，可尝试使用360解密大师解密，或联系360安全中心寻求帮助。同时，360专家建议您使用360防勒索整体解决方案，通过360相关安全产品及服务，为您的安全保驾护航。

截至目前，360防勒索解决方案已累计为超万例勒索病毒救援求助提供帮助。未来，360将继续完善防勒索解决方案，赋能更多用户感知风险、看见威胁、抵御攻击，筑牢数字安全屏障，护航数字经济发展。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?O55rWPXK)

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

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/aQWl)

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