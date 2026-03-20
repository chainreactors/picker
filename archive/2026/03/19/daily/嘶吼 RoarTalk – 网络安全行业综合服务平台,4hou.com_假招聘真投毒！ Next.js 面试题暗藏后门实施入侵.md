---
title: 假招聘真投毒！ Next.js 面试题暗藏后门实施入侵
url: https://www.4hou.com/posts/rpJW
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-19
fetch_date: 2026-03-20T04:07:10.856475
---

# 假招聘真投毒！ Next.js 面试题暗藏后门实施入侵

假招聘真投毒！ Next.js 面试题暗藏后门实施入侵 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 假招聘真投毒！ Next.js 面试题暗藏后门实施入侵

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-03-19 11:58:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8229

收藏

导语：攻击者通过搭建恶意代码仓库，伪装成合法的 Next.js 项目与技术测评材料（包括招聘编程测试题）实施入侵。

近期，一场以软件开发人员为目标、以招聘求职为诱饵的协同攻击活动正在展开。攻击者通过搭建恶意代码仓库，伪装成合法的 Next.js 项目与技术测评材料（包括招聘编程测试题）实施入侵。

攻击者的目的是在开发者设备上实现远程代码执行（RCE），窃取敏感数据，并在已沦陷系统中部署更多载荷。

**多重触发机制**

Next.js 是一款基于 React、后端依赖 Node.js 的热门 JavaScript Web 应用框架。微软 Defender 安全团队披露，攻击者伪造基于 Next.js 开发的 Web 应用项目，并将其包装成编程作业，在面试或技术测评环节分发给开发者。

研究人员最初在代码托管平台 Bitbucket 上发现一个恶意仓库，随后又识别出多个代码结构、加载器逻辑与命名模式高度相似的关联仓库。

当目标按正常流程克隆仓库并在本地打开项目时，启动应用的操作会自动触发恶意 JavaScript 代码。

该脚本会从攻击者服务器下载后续恶意代码（JavaScript 后门），并在正在运行的 Node.js 进程中直接内存执行，从而实现对主机的远程代码执行。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260226/1772098297481300.png "1772098297481300.png")

攻击链概览

为提升感染成功率，攻击者在恶意仓库中设置了多重触发点：

VS Code 触发：通过配置 .vscode/tasks.json 中的 runOn: “folderOpen”，项目文件夹被打开（且受信任）后立即执行 Node 脚本。

开发服务器触发：当开发者执行 npm run dev 启动开发服务时，被篡改的恶意组件会解码隐藏 URL，从远程服务器拉取加载器并在内存中执行。

后端启动触发：服务启动时，后端模块从 .env 文件中解码 Base64 加密的服务器地址，将环境变量发送给攻击者，并执行返回的 JavaScript 代码。

**攻击流程与能力**

入侵过程会释放第一阶段 JavaScript 载荷，用于收集主机信息并上线到命令与控制（C2）服务器，以固定周期轮询指令。

随后升级为第二阶段任务控制器，连接另一台 C2 服务器接收任务，在内存中执行指定代码并监控进程状态。该载荷还支持文件枚举、目录遍历与分段数据窃取。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260226/1772098327104060.png "1772098327104060.png")

第二阶段服务器轮询功能

微软指出，此次攻击涉及多个命名规范、加载器结构与基础设施高度一致的仓库，表明这是一次协同式攻击活动，而非偶发的单一事件。截至目前，研究人员尚未披露攻击者身份及攻击影响范围。

**安全建议**

微软提醒开发者：日常开发流程本身就是高风险攻击面，必须提高警惕并采取防护措施。建议采取的缓解措施包括：

**·**启用 VS Code 工作区信任/受限模式

**·**配置攻击面减少（ASR）规则

**·**通过 Microsoft Entra ID Protection 监控风险登录行为

**·**最小化在开发终端上存储敏感密钥信息

**·**尽可能使用最小权限、短时有效的访问令牌

文章来源自：https://www.bleepingcomputer.com/news/security/fake-nextjs-job-interview-tests-backdoor-developers-devices/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?V9TkGIXd)

#### 你可能感兴趣的

* [![]()

  仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包](https://www.4hou.com/posts/rpJL)
* [![]()

  嘶吼安全动态｜马自达系统遭入侵，员工信息或泄露 Perseus安卓银行木马出现升级版](https://www.4hou.com/posts/XPjV)
* [![]()

  2026职场AI观察：禁而不止的影子代理，正在埋下企业数据安全隐患](https://www.4hou.com/posts/PG26)
* [![]()

  嘶吼安全动态｜官方辟谣“七部门AI安全治理三年行动计划” 新型iPhone攻击工具“DarkSword”曝光](https://www.4hou.com/posts/RX4w)
* [![]()

  假招聘真投毒！ Next.js 面试题暗藏后门实施入侵](https://www.4hou.com/posts/rpJW)
* [![]()

  AI时代中国网络安全产业的五年变局|| 网络安全投融资的残酷分流](https://www.4hou.com/posts/MXY1)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包](https://www.4hou.com/posts/rpJL)
  2026-03-20 12:01:00
* [嘶吼安全动态｜马自达系统遭入侵，员工信息或泄露 Perseus安卓银行木马出现升级版](https://www.4hou.com/posts/XPjV)
  2026-03-20 12:00:00
* [2026职场AI观察：禁而不止的影子代理，正在埋下企业数据安全隐患](https://www.4hou.com/posts/PG26)
  2026-03-19 12:01:00
* [嘶吼安全动态｜官方辟谣“七部门AI安全治理三年行动计划” 新型iPhone攻击工具“DarkSword”曝光](https://www.4hou.com/posts/RX4w)
  2026-03-19 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包](https://www.4hou.com/posts/rpJL)

  胡金鱼
* [嘶吼安全动态｜马自达系统遭入侵，员工信息或泄露 Perseus安卓银行木马出现升级版](https://www.4hou.com/posts/XPjV)

  山卡拉
* [2026职场AI观察：禁而不止的影子代理，正在埋下企业数据安全隐患](https://www.4hou.com/posts/PG26)

  灵魂舞者
* [嘶吼安全动态｜官方辟谣“七部门AI安全治理三年行动计划” 新型iPhone攻击工具“DarkSword”曝光](https://www.4hou.com/posts/RX4w)

  山卡拉
* [假招聘真投毒！ Next.js 面试题暗藏后门实施入侵](https://www.4hou.com/posts/rpJW)

  胡金鱼
* [AI时代中国网络安全产业的五年变局|| 网络安全投融资的残酷分流](https://www.4hou.com/posts/MXY1)

  山卡拉

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