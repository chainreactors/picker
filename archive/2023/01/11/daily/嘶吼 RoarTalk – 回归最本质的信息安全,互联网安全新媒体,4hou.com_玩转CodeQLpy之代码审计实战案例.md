---
title: 玩转CodeQLpy之代码审计实战案例
url: https://www.4hou.com/posts/LB4r
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-11
fetch_date: 2025-10-04T03:31:22.677527
---

# 玩转CodeQLpy之代码审计实战案例

玩转CodeQLpy之代码审计实战案例 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 玩转CodeQLpy之代码审计实战案例

盛邦安全
[行业](https://www.4hou.com/category/industry)
2023-01-10 11:15:09

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)129747

收藏

导语：CodeQLpy是一款半自动化的代码审计工具，能有效提高代码审计的效率，目前项目仍处于测试阶段。

**0x01 背景介绍**

CodeQLpy是一款半自动化的代码审计工具，能有效提高代码审计的效率，目前项目仍处于测试阶段。项目地址https://github.com/webraybtl/CodeQLpy，在github主页有对应的安装和使用介绍，如图1.1所示。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259774118037.png "1673259291110460.png")

-t: 指定待扫描的源码路径。支持文件夹，jar包和war包，如果是文件夹，则必须是网站跟目录。

-d: 指定待扫描的CodeQL数据库。

-c: 指定待扫描的源码是编译前源码还是编译后源码。

-s: 指定是否跳过环境检查，本项目运行依赖于codeql和java环境，首次运行建议不跳过。

-v: 指定待测试源码的jdk版本，目前支持6，7，8，11。默认为8。

这里以某通用WEB应用为例，通过指纹body="changeAccount(\"varAccount\")" || body="KoronCom.TrustedSites"可以在资产测绘平台上找到近3000个资产。

![1673259322137453.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259775200823.png "1673259322137453.png")

![1673259354645651.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259776792664.png "1673259354645651.png")

**0x02 工具使用**

该系统的源码是主要由jsp文件和class文件组成，其中部分源码经过混淆，如图2.1所示。其中类名称和字段名称的可读性很差，不方便阅读，而且该系统的代码量较大，大约有4600个文件。如果通过传统的方式来进行代码审计，对审计人员的要求将会非常高。

![1673259388923834.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259776263105.png "1673259388923834.png")

图2.1 经过混淆的源码

使用CodeQLpy可以方便的帮助审计人员从大量源码中发现可能存在的安全隐患，使用步骤如下。

**Step1：生成数据库初始化**

python3 main.py -t /Users/xxx/Downloads/OAapp/ -c

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259777745513.png "1673259423120597.png")

图2.2 数据库初始化

最终运行成功之后会相应下一步进行数据库创建的命令。

**Step2：生成数据库**

这一步直接使用上一步命令最终返回的生成数据库的命令在cmd/bash环境中运行即可

mac命令如下

arch -x86\_64 codeql database create out/database/OAapp --language=java --command='/bin/bash -c /Users/xxx/CodeQLpy/out/decode/run.sh' --overwrite

windows命令如下

codeql database create out/database/OAapp --language=java --command='run.cmd' --overwrite

生成的过程中会报很多错误，可以忽略，如图2.3所示。因为这一步创建的数据库是用上一步反编译的源码进行编译，反编译的源码不能保证完全正确，所以会有错。但是有错的源码仍然可以创建数据库，不影响我们进行代码审计。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259777117351.png "1673259502206550.png")

图2.3 创建数据库

**Step3：代码审计**

这一步需要使用上一步命令最终相应的生成数据库的路径，如图2.4所示。

```
python3 main.py -d /Users/xxx/CodeQLpy/out/database/OAapp/
```

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259778406042.png "1673259522103085.png")

图2.4 使用ql插件分析可能存在的漏洞

最终得到的结果是csv文件，保存路径在out/result/目录，打开对应的文件，如图2.5所示。

![1673259543129805.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259778180687.png "1673259543129805.png")

图2.5 扫描结果内容

**0x03 结果验证**

扫描出来的结果很多，我们挑选几个有代表性的进行验证。

**1）BeanShell远程命令执行漏洞**

相关存在漏洞的文件在com/menyi/web/util/UtilServlet.class，如图3.1所示。从图中可以看出用户可控的输入value，传入了Interpreter类的eval方法，导致BeanShell任意代码执行。

![1673259568161231.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259779101337.png "1673259568161231.png")
图3.1 BeanShell远程命令执行漏洞

在测试平台上利用此漏洞，如图3.2所示。

![1673259584520888.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259780128044.png "1673259584520888.png")

图3.2 BeanShell远程命令执行漏洞exp

**2）FilePathInjection任意文件读取漏洞**

相关存在漏洞的代码在com.menyi.web.util.ReportServlet.class。如图3.3所示。

![1673259615220691.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259780207920.png "1673259615220691.png")

图3.3 任意文件读取漏洞

在测试平台上利用此漏洞，如图3.4所示。

![1673259719162386.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259781212307.png "1673259719162386.png")

图3.4 任意文件读取漏洞Exp

**3）SQL注入漏洞**

漏洞文件是在com.koron.oa.workflow.OAMyWorkFlowAction.class。如图3.5所示。

![1673259740154975.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259781129104.png "1673259740154975.png")

图3.5 用户可控输入tablename

继续跟进getOAMyWorkFlowInfo，如图3.6所示。

![1673259757105383.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230109/1673259782793558.png "1673259757105383.png")

图3.6 tableName参数传递到SQL语句

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?t6tPbulv)

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