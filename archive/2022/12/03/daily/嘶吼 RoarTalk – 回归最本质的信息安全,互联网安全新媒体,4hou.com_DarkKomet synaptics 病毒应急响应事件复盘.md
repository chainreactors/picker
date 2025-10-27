---
title: DarkKomet synaptics 病毒应急响应事件复盘
url: https://www.4hou.com/posts/MBv1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-03
fetch_date: 2025-10-04T00:22:53.648837
---

# DarkKomet synaptics 病毒应急响应事件复盘

DarkKomet synaptics 病毒应急响应事件复盘 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DarkKomet synaptics 病毒应急响应事件复盘

货拉拉安全应急响应中心
[技术](https://www.4hou.com/category/technology)
2022-12-02 15:07:33

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)168132

收藏

导语：DarkComet （暗黑彗星）是由 Jean-Pierre Lesueur（称为 DarkCoderSc）开发的远程访问木马（称为 RAT）

**一、准备阶段**

**1.1 基本情况**

DarkComet （暗黑彗星）是由 Jean-Pierre Lesueur（称为 DarkCoderSc）开发的远程访问木马（称为 RAT），在 2012 年初开始扩散，它用于许多有针对性的攻击，能够通过网络摄像头拍照，通过连接到 PC 的麦克风窃听对话，并获得对受感染机器的完全控制。该 RAT 还以其键盘记录和文件传输功能而闻名，因此，任何远程攻击者都可以将任何文件加载到受感染的机器上，甚至窃取管理员权限、计算机/用户名、语言/国家、操作系统信息、使用的内存、网络摄像头信息、文档等。它会禁用任务管理器、注册表编辑器和文件夹选项，修改注册表项以禁用 Windows 防火墙设置，此操作允许此恶意进程执行而不会被 Windows 防火墙检测到。别名有：Fynloski、Krademok、DarkKomet 等。

**1.2 功能**

DarkKomet 主要功能：远控，对用户行为进行监控并为攻击者开启 SYSTEM 后门，窃取用户信息并回传窃取的信息发送给攻击者，同时还可以下载其他恶意软件。

**1.3 传播方式**

DarkKomet 将自身伪装成笔记本电脑触控板的驱动程序 Synaptics Pointing Device Driver，启动后，会全盘遍历 exe 文件、xlsx 文件，并将目标文件更新到病毒资源中，将 shellcode 注入的图标资源替换为目标文件图标，然后用病毒文件覆盖目标文件，完成感染，实现不死及复生能力。并可通过U盘插入、xlsx 文件分享、远控软件捆绑实现横向扩散，具有极强传播能力。

**二、检测阶段**

![1.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964474368004.jpeg "1669964474368004.jpeg")

货拉拉终端应急响应检测机制基于TTP驱动、离群数据驱动、杀毒事件驱动、威胁情报驱动混合。该次事件由EDR收集终端全量启动项数据，结合威胁情报接口，实现终端权限维持数据基线的分钟级扫描。高危事件通过webhook 实现IM告警，方便安全运营人员实时接入处置，并通过工单记录汇总。

聚合N day内 该病毒感染的终端量及感染者的账号、用户名、部门等信息，最终由多条alert形成单条完整incident。

![2.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964485455582.jpeg "1669964485455582.jpeg")

通过 webhook/工单形式将消息推送给终端安全运营人员对事件进行下钻，IOC/TTP加入EDR实时检测阻断规则，完成由单次事件检测 —— 一类事件阻断的事件闭环。

**三、抑制阶段**

**3.1 事件的处置**

1、拦截回连c2域名、IP，中断连接。

2、远程接入应急溯源，获取TTP。

**四、根除阶段**

**4.1 删维权**

该病毒通过 Run 键实现到权限维持（开机自启动），删除启动项

![3.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964495134763.jpeg "1669964495134763.jpeg")

**4.2 清进程**

结束 2 个Synaptics.exe进程

![4.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964502643289.jpeg "1669964502643289.jpeg")

**4.3 删文件**

进入 DarkKomet 文件目录，只有WS文件夹，却找不到相关可执行文件

![5.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964511178753.jpeg "1669964511178753.jpeg")

怀疑DarkKomet隐藏自身，取消勾选【隐藏受保护的操作系统文件】并选中【显示隐藏文件】

![6.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964518576270.jpeg "1669964518576270.jpeg")

被隐藏的病毒文件 Synaptics.exe显形，

![7.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964528602634.jpeg "1669964528602634.jpeg")

删除文件，提示需要SYSTEM权限（高于Administrator），病毒文件通过修改文件属主及文件权限实现强行驻留

![8.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964535189452.jpeg "1669964535189452.jpeg")

修改文件属主为administrator并继承权限后，删除病毒文件

![微信图片_20221202152016.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669965683956601.png "1669965683956601.png")

**4.4 溯源头**

清除威胁后，溯源入口点，从取证角度获取 2022-05-17 16:29:30 运行软件信息，发现可疑文件路径

F:\柯美黑白机64位系统\

![10.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964553166336.jpeg "1669964553166336.jpeg")

可疑点：该文件位于F盘，且运行时间与病毒创建时间密切相关，但用户终端上却只有C、D、E盘。

![12.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964562785573.jpeg "1669964562785573.jpeg")

猜测该盘为第三方便携插入式U盘，咨询用户后得到【安装打印机】细节。

由此推测：该病毒原本位于U盘中，安装打印机时插入U盘，U盘内的病毒自动感染终端位于C盘的文件，实现横向扩散。

由于该病毒具有感染性，推测还感染了其他文件。通过遍历NTFS文件系统 MFT-TIME，获取 2022-05-17 16:29:30 - 2022 - 05 -17 16:29:40 创建及修改的所有文件，获取被感染文件信息

![13.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964569369925.jpeg "1669964569369925.jpeg")

通过日志回溯取证，发现 f:\京瓷复印机\Kx6111118\_en\setup.exe入驻Run键，创建病毒文件 C:\ProgramData\Synaptics\Synaptics.exe，并将Synatics.exe添加启动项 。由此映证猜测，C2病毒感染源头为安装打印机时插入U盘。

**五、恢复阶段**

1、清除被感染的"\_cache\_"文件

2、IOC / TTP 加入EDR、杀毒，复验攻击能被实时阻断。

3、受损用户更改密码

**六、总结阶段**

IOC：

DNS：xred.mooo.com

IP：69.42.215.252

TTP：

![14.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221202/1669964577291165.jpeg "1669964577291165.jpeg")

**6.1 历史事件**

某用户请第三方安装师傅安装打印机，插入 U 盘后，U 盘中已存在的 DarkKomet 组织 synaptics 病毒自动运行，进而感染终端位于 C 盘下的十余个进程及文件。

某员工下载被投毒的 todesk 进行远程办公【具有 todesk 功能，实为 synaptics 远控病毒新变种】，导致感染 synaptics 病毒。

某员工下载 CAD 破解软件，其中夹杂最新版 synaptics 病毒。

...

本轮 synaptics 应急响应，终端产生的威胁主要来自：U 盘扩散、软件投毒捆绑这两种形式。病毒最明显特征为：未签名进程 C:\ProgramData\Synaptics\Synaptics.exe 入驻Run键以权限维持。

当下阶段，利用人性弱点进行投毒的事件层出不穷。针对员工高频安装的浏览器类、IM类、运维工具类、远程控制类软件，需做好软件与对应签名的映射验证，并针对高危场景离群数据进行威胁狩猎。辅以外部/内生威胁情报，构建滤网机制，对启动项软件流水加以管控。实现启动项快照机制，对未知/离群/高危/权限维持数据定时清理，在提升攻击者成本的同时，也增加检测/阻断未知攻击的可能。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Yv8Cqd8y)

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

![](https://img.4hou.com/portraits/0ac25fc191bface77271c88967adcdb5.png)

# [货拉拉安全应急响应中心](https://www.4hou.com/member/VQQo)

https://llsrc.huolala.cn/

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/VQQo)

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

[©2024 北京嘶吼文化传媒有限公司 京ICP备1606343...