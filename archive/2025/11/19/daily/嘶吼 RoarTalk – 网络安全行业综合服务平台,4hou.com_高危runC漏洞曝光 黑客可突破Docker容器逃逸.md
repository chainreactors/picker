---
title: 高危runC漏洞曝光 黑客可突破Docker容器逃逸
url: https://www.4hou.com/posts/XP4l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-19
fetch_date: 2025-11-20T03:08:06.691600
---

# 高危runC漏洞曝光 黑客可突破Docker容器逃逸

高危runC漏洞曝光 黑客可突破Docker容器逃逸 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 高危runC漏洞曝光 黑客可突破Docker容器逃逸

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8374

收藏

导语：这三个安全问题的漏洞编号分别为CVE-2025-31133、CVE-2025-52565和CVE-2025-52881。

Docker和Kubernetes中使用的runC容器运行时被披露存在三个新漏洞，攻击者可利用这些漏洞绕过隔离限制，获取主机系统访问权限。

这三个安全问题的漏洞编号分别为CVE-2025-31133、CVE-2025-52565和CVE-2025-52881（均为高危级别），由SUSE软件工程师于本周披露。

runC是一款通用容器运行时，同时也是开放容器倡议（OCI）的容器运行参考实现。它负责执行创建容器进程、配置命名空间、挂载点和控制组等底层操作，供Docker、Kubernetes等上层工具调用。

攻击者利用这些漏洞可获取容器底层主机的写入权限，并获得root权限，具体漏洞细节如下：

**·**CVE-2025-31133：runC通过绑定挂载/dev/null来“屏蔽”主机敏感文件。若攻击者在容器初始化阶段将/dev/null替换为符号链接，runC可能会将攻击者控制的目标以可读写模式绑定挂载到容器中，进而允许攻击者写入/proc目录，实现容器逃逸。

**·**CVE-2025-52565：/dev/console的绑定挂载可通过竞争条件或符号链接被重定向，导致runC在防护机制生效前，将非预期目标挂载到容器内。这同样会使proc文件系统的关键条目暴露可写入权限，为容器逃逸创造条件。

**·**CVE-2025-52881：攻击者可诱使runC向/proc目录执行写入操作，且该操作会被重定向至攻击者控制的目标。在部分版本中，该漏洞可绕过Linux安全模块（LSM）的重新标记防护，将runC的常规写入操作转化为对/proc/sysrq-trigger等危险文件的任意写入。

其中，CVE-2025-31133和CVE-2025-52881影响所有版本的runC，CVE-2025-52565则影响1.0.0-rc3及后续版本的runC。目前，runC 1.2.8、1.3.3、1.4.0-rc.3及更高版本已提供修复补丁。

**漏洞可利用性与风险**

安全研究人员指出，利用这三个漏洞“需要具备以自定义挂载配置启动容器的能力”，攻击者可通过恶意容器镜像或Dockerfile实现这一条件。

截至目前，尚无这些漏洞被在真实环境中主动利用的相关报告，但可通过监测可疑的符号链接行为，检测是否存在利用这三个安全漏洞的尝试。

runC开发者已公布缓解措施，包括为所有容器启用用户命名空间，且不将主机root用户映射到容器命名空间中。

这一预防措施可阻断攻击的关键环节，因为Unix自主访问控制（DAC）权限会阻止命名空间内的用户访问相关文件。

Sysdig还建议，若条件允许，应使用无root权限容器，以降低漏洞被利用后可能造成的损害。

文章翻译自：https://www.bleepingcomputer.com/news/security/dangerous-runc-flaws-could-allow-hackers-to-escape-docker-containers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?nNqmtJdA)

#### 你可能感兴趣的

* [![]()

  高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
* [![]()

  Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
* [![]()

  Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
* [![]()

  QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
* [![]()

  近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
* [![]()

  RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
  2025-11-19 11:10:33
* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
  2025-11-06 12:00:00
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
  2025-11-04 12:00:00
* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
  2025-10-30 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)

  胡金鱼
* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)

  胡金鱼
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

  胡金鱼
* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)

  胡金鱼
* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)

  胡金鱼
* [RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)

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