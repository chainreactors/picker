---
title: 【家族介绍】DragonForce，一个将勒索做成企业的家族
url: https://mp.weixin.qq.com/s/56aFr15O4ArqGajRmX3wkw
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:23:37.517345
---

# 【家族介绍】DragonForce，一个将勒索做成企业的家族

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/887OLfia3YQZ85PWBKic7DDDMickNDia1GAQkmEa6Epa6Uj5H5OG4eWze8OJic8GGOrV0hnHReMeuia1qIt016bOfoYI2wAO0NVtdEpSmicnSbcTsg/0?wx_fmt=jpeg)

# 【家族介绍】DragonForce，一个将勒索做成企业的家族

州弟学安全、Moir
州弟学安全、Moir

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

依托 **Solar 安全运营响应团队**的日常实战沉淀，我们会定期分享在安全运营中处置的典型应急响应事件，涵盖**银狐木马、APT 攻击、勒索病毒**等各类主流威胁。

作为专业的应急响应中心，Solar 致力于为复杂多变的安全事件提供从深度溯源到闭环处置的全流程支持。针对银狐、APT 等具有高隐蔽性的威胁，我们不仅聚焦于对其攻击行为的深度剖析，更致力于还原其完整的活动链路，并同步输出切实可行的**清除闭环操作方案**。

**突发危机干预通道：**若您的核心资产正面临加密锁定或数据勒索风险，请通过文末二维码联系我们。我们提供全天候紧急介入服务，协助您快速切断攻击链路，全力挽回业务损失。

## 写在前面

7月14日，DragonForce在其暗网泄露站点上，几个小时内接连挂出四家国内科技与制造企业，涉及数据总量超过1.4TB。我们在事发48小时内发布了专项预警。

预警文章发出后，不少读者问：这个DragonForce到底是什么来头？之前没怎么听过，为什么一出手就是这么大的动静？

其实这个家族已经活跃了整整三年。它2023年8月首次出现，在勒索病毒地下市场里算是后来者，但成长速度远超同期家族。更值得注意的是它的运作方式：它不太像一个传统意义上的黑客团伙，更像一家把勒索当成主营业务来经营的公司，有产品、有渠道、有客服，也有品牌意识。

这篇文章不做具体案例复盘。我们把长期监测到的公开信息、后台界面截图和逆向分析结果整理出来，系统讲清楚这个家族的运作逻辑，以及它对防守方意味着什么。

## 一、家族档案：活跃三年，634家企业被挂牌

DragonForce是一个勒索软件即服务（RaaS）组织，2023年8月开始活跃，采用典型的双重勒索模式：先窃取数据，再加密系统，受害者不按要求付款，就把数据公开在自家泄露站点上。

根据Solar威胁情报平台的监测数据，截至2026年8月，被该组织勒索并挂牌的企业达到634家，波及64个国家和10个行业，监测期内的月度新增数量整体呈上升趋势，2026年以来增长明显提速。受害者分布上，46%位于美国（294家），其后依次是英国（44家）、德国（32家）、加拿大（20家）、意大利（19家）和澳大利亚（18家），法国、印度、瑞士及中国香港等均在列；行业上，专业服务（144家）与制造业（139家）首当其冲，科技（73家）、零售与电子商务、医疗保健、交通运输、金融服务、能源与公用事业等无一幸免。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZQO8ndPtUibreGrrFu4VsrAHfmPAAz0KVqb6ghe5L5faQV07x1qicdoibtVdRlkDgn5JEecnh3VlrKCfxuamkBhrsE1NaQyZ5OYA/640?wx_fmt=png&from=appmsg)

DragonForce暗网泄露站点首页，受害者以卡片形式公示，逐一标注所在地区、业务描述和被窃取的数据量

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYMxfOHCbkvliciciajbpPndxnu8dCwVe8s0NB6CeiaNrEicob3Yo8MZcIhYE7hRAQSVgUdjMRhKrqAD2e7A1KibCOGMoUHgDaqkMqpQ/640?wx_fmt=png&from=appmsg)

Solar威胁情报平台收录的DragonForce家族档案，总受害者634家，含行业分布、国家分布与月度增长曲线

它的目标偏好很明确：经济价值高、IT基础设施庞大复杂、对业务中断"零容忍"的企业。原因不复杂，这类企业付得起钱，也停不起工。

## 二、两套加密器：一套来自泄露，一套自己改写

DragonForce的联盟成员可以使用两套勒索软件。

第一套是LockBit 3.0的变种。LockBit的构建器源码此前在地下市场泄露，DragonForce在此基础上做了改造，成熟稳定，加密速度快。

第二套是它自己开发的版本，基于Conti V3的源码修改，最大的特点是自带恶意驱动程序。这种手法在行业内被称为BYOVD（Bring Your Own Vulnerable Driver，自带脆弱驱动）：攻击者在受害者系统上加载一个带有合法数字签名、但存在内核漏洞的驱动程序，利用系统对合法签名的信任进入内核层，从底层终止或致盲EDR、XDR等终端防护软件。它攻击的不是某个具体漏洞，而是整个信任机制。这也是不少部署了终端防护的企业仍然被加密的原因之一。

我们对该家族的加密器做过完整的逆向分析，几个关键结论值得记录：加密采用ChaCha20与RSA双重算法，每个文件使用独立随机生成的密钥；加密策略按文件类型差异化处理，数据库文件100%全加密，虚拟机文件只加密20%，1MB以下的小文件全加密，1MB到5MB的文件只加密头部，5MB以上的大文件分5段条状加密、合计50%。这套策略的意图很清楚，在保证破坏效果的前提下，把加密耗时压到最短，压缩防守方的响应窗口。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQZtxichOrTclmGyceRIx4rtTBuayxPWYLfhmEC9XP1smYQxibjWljmNl7ibmJoYZpQZCN73gFKfAYbgzia0V7PCOdncSY0oIXVv0YU/640?wx_fmt=png&from=appmsg)

DragonForce加密器执行流程，初始化反HOOK模块、解析参数、批量创建加密线程、删除影卷备份、执行网络扫描

加密完成后，原文件名经base32编码，追加.dragonforce\_encrypted后缀，勒索信以readme.txt释放。目前该家族没有可用的免费解密器。平台覆盖方面，按它自己在招募帖里的说法，Windows、ESXi、BSD、NAS、Linux全部支持。

## 三、80%分成的联盟生意，一小时就能组建团队

DragonForce能快速做大规模，靠的不是自己动手，而是把攻击"分包"出去。

2024年6月26日，它在Ramp黑客论坛发布招募帖，公开邀请"合伙人"加入，开出的条件在当时的勒索市场里相当激进：赎金的80%归联盟成员，平台只留20%。招募文案写得很像正规公司的招聘广告：全流程自动化、作战软件覆盖ESXi/NAS/BSD/Windows、7×24小时服务器监控、Anti-DDoS防护、PB级无限存储、免费的呼叫中心服务，最后还补了一句"work without paranoia"，意思是安心干活，不用提心吊胆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQafJCn3AcFlt8hiavzkAMkicP8xoWWZNtkboInUuzqFEL4icckOUM9EKiaPnOmFMt8qCXgZW8QkYj1BXXklHOdUcCm8xhdpFia8JJRw/640?wx_fmt=png&from=appmsg)

DragonForce在Ramp论坛发布的招募帖，明确写着"80% goes to you (we only take 20%)"

这还不算完。它后来在暗网首页顶部挂出一条横幅："We've opened the public registration, build your own RaaS team in 1 hour"。开放公开注册，号称一小时就能组建自己的勒索团队。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQadCldId0BibVE1lZEXiaxXZUhQkObIFmBljUpibSibFzBe0oshvhNfvicjXlZDrhtdQqHcw2D20NeGfkBhrlibOicWX1P3F4Kd1yzlac/640?wx_fmt=png&from=appmsg)

DragonForce暗网首页的公开注册横幅，以及"Welcome, Miami!"、"Suppliers"等官方公告

招募帖和横幅只是门面，真正的问题在于：加入之后，联盟成员拿到的到底是一套什么样的系统？

我们获取其联盟后台的界面。如果遮住顶部的龙形标志，这套系统和一家公司的OA后台几乎看不出区别。进入后台的第一道门槛就很"企业"：账号、密码、登录按钮，和任何一家公司的内部系统登录页没有任何不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbXuTngbib5Y3joRldAUrXF8xJbGfBynCmb2SyG4tGicM9g6FwzfxZMaecY7ZOFLXnQPF1zENhLoX3vkC2wCWNyztgn8nkOibJXn0/640?wx_fmt=png&from=appmsg)

**DragonForce联盟后台登录页，标准的账号密码登录流程**

登录进去，早期版本的导航栏上有七个模块：CLIENTS（客户管理）、BUILDER（样本构建）、MY TEAM（团队管理）、PUBLICATIONS（发布管理）、RULES（规则）、BLOG（博客）、PROFILE（资料），一应俱全。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQad4Atrc4t7VoAst0JIgOzTGyUjtNBRp2Zp5e3lZIibpRXtGr90OibibBuMWhtoyOFXkW9QykJlNicvib7sc3gM4crQfQzJg2NR6YNA/640?wx_fmt=png&from=appmsg)

联盟后台早期版本的导航栏，七个功能模块完整可见

而这还只是一个中间版本。2026年8月6日的最新界面显示，后台导航栏已经扩充到十个入口：GOLDEN BUTTON（黄金按钮）、OVERVIEW（工作台）、CLIENTS、BUILDER、MY TEAM、PUBLICATIONS、README（自述文件）、NEWS（新闻）、TICKETS（工单）、PROFILE。一个勒索平台在持续迭代自己的产品线，这件事本身就值得警惕。

接下来，我们按导航栏的顺序，逐个模块看一遍。

### OVERVIEW：可定制的工作台

点开OVERVIEW，先看到一排统计卡片：在手受害者总数、待处理、谈判中、已删除、已发布、已解密，逻辑和CRM系统里的销售漏斗完全一致。中间是受害者列表，状态、创建者、公司网址、数据规模、倒计时、创建时间逐列排开。页面底部留给工单和新消息。这套工作台甚至连布局都可以自己拖：统计、客户、发布、工单四个组件支持移动、禁用和编辑，跟企业SaaS的个性化首页是同一个设计思路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYXACRg4OvibgIiaza6yfrBESCMQeH5oZ6Qq6vUsXtTRQ8dow5dOpImruiarL5rcYzKN2GJYl40sqB3cFJd8gsTdu40WL4KqSPaRY/640?wx_fmt=png&from=appmsg)

OVERVIEW工作台，顶部为受害者状态统计，列表中Revenue列标注赎金金额

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbpl07swaTOfrSq7jtW4jV2oK9ef3Kd8LiakSwsbKgHKCqFjevbdf7CtfOyL7iat3GH67eykYsDoeVDOic1eoNU5Sg6c4jibiaiaNkhs/640?wx_fmt=png&from=appmsg)

工作台设置弹窗，四个组件可自由启用、禁用和调整顺序

### CLIENTS：客户管理，外加两个聊天室

客户管理页藏着整套系统里最有"公司味"的设计：页面左侧直接内嵌了一个即时聊天窗口，分"全球的"（Global）和"团队"（Team）两个频道，底部状态栏实时显示WebSocket连接状态。右边管着受害者名单，左边聊着工作，算是把企业办公做进了CRM。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYTic20NjOH7Bx0pxib6CZltpewBU8C374LOv6od7GfQPv37icJmibgiasjhB4y2ysPYyfqjgA6wMQedHVzzlyiak2NKpuuVfhs4Khas/640?wx_fmt=png&from=appmsg)

CLIENTS页面，左侧为全球与团队双频道聊天室，右侧为受害者列表（界面为便于阅读做了汉化处理，下同）

全球聊天室里都在聊什么？署名root的平台管理员像所有公司的技术负责人一样发全员公告：文件系统因上传下载负载过高决定重写，新版本正在推进；Windows加密器的v2版本正在各种环境下测试，将支持命令行参数、换用BearSSL加密库、增加模拟用户身份等功能。公告结尾还不忘致谢："谨代表DragonForce合作伙伴计划，感谢您与我们携手共进"。

普通成员在聊业务。有成员推销平台新上线的"公司数据审计"服务："一份新的公司名单已经出炉，这些公司即使经过正确的日期分析，仍有95%的情况下会无故付款"，一分钟后又追了一条更正，"我的意思是他们无需锁定即可付款"。换句话说，名单上的企业就算没有被加密，也有九成五的概率会掏钱把数据买回去。有人接话问：审计部门会自己发邮件、打电话，还是只对数据做审计？对方的回答言简意赅："两者兼有"。管理员偶尔也在里面吆喝生意："美国优质新网络现已开放购买"。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYibKCwSZuiaNu8Wg4PEhSQlvQOHPcKxTHtX00yH6HXjUkjxUsibn9eb2mWTITnfXya3jbaLibfqpUSLpMBd3jxLfNxPFpv4w7CmQ8/640?wx_fmt=png&from=appmsg)

全球聊天室记录，成员推销数据审计服务，称名单上95%的企业未被加密也会付款

### BUILDER：表单化的样本生产线

在构建器里，联盟成员勾选目标公司的网址、年收入、测试解密开关、赎金支付时限、加密比例、排除的目录和文件、用于终止终端防护软件的驱动，点击创建，就能下载一套为该受害者定制的样本，Windows和ESXi版本打包提供。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYuZeqmWsHZ2c8icqFPGL4Goeh2LQIWDpghpoyIBehlMtlc4ekLEgpuNN6iaX9wqN8remxfRpiaibvianzMxEDqh6Oz0IK0pDfJWN4w/640?wx_fmt=png&from=appmsg)

样本构建器界面，多平台选项与加密参数全部以表单形式配置

### MY TEAM：一小时组建团队，不是一句口号

MY TEAM模块里，每个联盟团队都被当成一个独立经营单元来管理：页面上方是管理员名单和下级成员（Advertisers）名单，下方是一张团队经营曲线图，考核指标包括样本构建数、发帖数、新增硬件数、新增成员数和BTC收益，跟公司给业务部门画的增长报表一模一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQbOGR1PNdEzj3KCYJFPQ7ZHU5XbEPYIkNoqzMPa4kHaZKibctngBPM7uibb3chLZ8B8HySgnVN3lAIPGZ93MWrZq4xk4GjHqkicwY/640?wx_fmt=png&from=appmsg)

MY TEAM团队管理页，含管理员列表、下级成员列表和团队经营数据曲线

团队长点击ADD ADVER就能给团队招人：填登录名和密码，然后勾选权限，能不能在聊天室发言、能不能管理受害者的倒计时、能不能锁定客户，逐项配置，一个带角色权限体系的"员工账号"就建好了。这套东西放在任何一家正规互联网公司，都叫组织架构管理。所谓"一小时组建自己的RaaS团队"，靠的就是这套现成的账号和权限体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQapvlVJsmPnzicKcTdSyDhTSGtJcAuhFj8a5gpAcFMTia4x7593ZE4TS7x8jALNyBeK4Vcomr7TPbsLhuW7po8q2gQRQ0aBDicbEA/640?wx_fmt=png&from=appmsg)

创建下级成员账号的弹窗，发言、倒计时管理、客户锁定等权限逐项勾选

### PUBLICATIONS：泄露内容的内容运营

发布管理模块对应着对外泄露站点的排期。每一家企业都是一条待发的"稿件"，表格里带可见性开关、发布时间、浏览量（Views）和转发量（Forwarded）统计。泄露数据的传播效果，是被当成运营数据来跟踪的。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQar4bEUGwoY847oDibgmhDcJCKdcxZP9fEMMiaLBBiczqOZDjvDfEhKa5icicnfmEgcYMBbBYuuaOibopm7icYnhoMD6FajmVQFicCctEs/640?wx_fmt=png&from=appmsg)

### README：员工手册加产品文档中心

README模块分两部分。第一部分是14条平台规则，页面标注最近更新于2025年4月22日：禁止攻击医院、关键基础设施、非营利组织和独联体国家；赎金由系统自动分账，团队拿80%，平台抽20%；倒计时的标准配置是14天数据恢复期加28天谈判期，超时解密器永久删除、无法恢复；...