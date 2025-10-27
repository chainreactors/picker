---
title: NPS内网穿透详细案例 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18868280
source: 博客园 - 渗透测试中心
date: 2025-05-10
fetch_date: 2025-10-06T22:30:00.124090
---

# NPS内网穿透详细案例 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [NPS内网穿透详细案例](https://www.cnblogs.com/backlion/p/18868280 "发布于 2025-05-09 15:27")

**NPS工具介绍**

NPS工具是一款使用go语言编写的轻量级、功能强大的内网穿透工具。支持TCP、UDP流量转发，支持内网HTTP、SOCKS5代理，同时支持snappy压缩(节省带宽和流量)、站点保护、加密传输、多路复用、header修改等。同时还支持web图形化管理。该工具使用简单，相比于FRP，NPS是图形化界面，因此配置更加简单

[root@ls4jtubcnt opt]#wget <https://github.com/ehang-io/nps/releases/download/v0.26.10/linux_amd64_server.tar.gz>

[root@ls4jtubcnt opt]# mkdir nps

[root@ls4jtubcnt opt]# tar -zxf linux\_amd64\_server.tar.gz -C  nps/

[root@ls4jtubcnt opt]# cd nps/

[root@ls4jtubcnt nps]# ./nps install                  #执行安装命令

[root@ls4jtubcnt nps]# ./nps  start                #启动NPS，nps start|stop|restart|uninstall|reload

[root@ls4jtubcnt nps]# cd /etc/nps/conf/      #安装后配置文件位于/etc/nps/conf目录下

nps.confg配置文件：

appname = weblogger

#Boot mode(dev|pro)

# 指定运行模式(dev|pro)

runmode = dev

#HTTP(S) proxy port, no startup if empty

# http[s]代理,如果设置为空,则表示忽略

#http\_proxy\_ip=

#http\_proxy\_port=

#https\_proxy\_port=

#https\_just\_proxy=

#default https certificate setting

# 指明 https 缺省证书文件位置

https\_default\_cert\_file=conf/server.pem

https\_default\_key\_file=conf/server.key

##bridge

# 客户端和服务端之间所用的通信协议,端口和服务端绑定 ip

bridge\_type=tcp

bridge\_port=8024

bridge\_ip=0.0.0.0

# Public password, which clients can use to connect to the server

# After the connection, the server will be able to open relevant ports and parse related domain names according to its own configuration file.

# 客户端以配置文件模式启动时的密钥,设置为空表示关闭客户端配置文件连接模式

public\_vkey=Pksfy2312df70i5osc

#Traffic data persistence interval(minute)

#Ignorance means no persistence

# 服务端流量数据持久化间隔,单位分钟,忽略表示不持久化

flow\_store\_interval=3

# log level LevelEmergency->0  LevelAlert->1 LevelCritical->2 LevelError->3 LevelWarning->4 LevelNotice->5 LevelInformational->6 LevelDebug->7

# 输出运行日志,如下,写到当前目录下的 weblogger.log 文件中,7 表示调试模式

log\_level=7

log\_path=weblogger.log   #生成的日志文件路径为：/weblogger.log

#Whether to restrict IP access, true or false or ignore

# 是否限制 ip 访问,true 或 false 或忽略

#ip\_limit=true

#p2p

#p2p\_ip=127.0.0.1

#p2p\_port=6000

#web

# web 控制面板配置,包括域名,访问端口和登录账号密码,域名访问需要使用反向代理进行配置

web\_host=login.weblogger.com

web\_username=backlion

web\_password=bks.net@#125

web\_port = 8081

web\_ip=0.0.0.0

web\_base\_url=

web\_open\_ssl=false

web\_cert\_file=conf/server.pem

web\_key\_file=conf/server.key

# if web under proxy use sub path. like http://host/nps need this.

#web\_base\_url=/nps

#Web API unauthenticated IP address(the len of auth\_crypt\_key must be 16)

#Remove comments if needed

# auth\_key 为 web api 密钥,auth\_crypt\_key 表示获取服务端 authKey 时的 aes 加密密钥,16 位

#auth\_key=ATi39sdp2d

auth\_crypt\_key =AmSo173adsPEWRSZ

#allow\_ports=9001-9009,10001,11000-12000

# 为防止 nps 服务端端口滥用,可限制可开启的端口,忽略或者不填表示端口不受限制

#Web management multi-user login

# 是否支持多用户登录,默认该功能是关闭的,一般也不会用

allow\_user\_login=false

allow\_user\_register=false

allow\_user\_change\_username=false

#extension

# 其它杂项,如,流量限制,带宽限制,对客户端的隧道数限制,最大连接数 等等等...默认忽略就好

allow\_flow\_limit=false

allow\_rate\_limit=false

allow\_tunnel\_num\_limit=false

allow\_local\_proxy=false

allow\_connection\_num\_limit=false

allow\_multi\_ip=false

# nps 服务端支持在 web 上显示和统计服务器相关信息,但默认一些统计图表是关闭的,可以通过此选项打开

system\_info\_display=true

#cache

# http 缓存设置,保持默认即可

http\_cache=false

http\_cache\_length=100

#get origin ip

http\_add\_origin\_header=false

#pprof debug options

#pprof\_ip=0.0.0.0

#pprof\_port=9999

#client disconnect timeout

disconnect\_timeout=60

服务端启动后会首先监听两个端口,一个是 web 面板访问端口[ 此处为 8081 ],另一个就是 nps 客户端和服务端的通信端口[ 此处为 9099 ]

[root@ls4jtubcnt conf]# netstat  -tulnp

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152647751-1604441388.png)

访问：http://vps ip:8081/,并输入以上/etc/nps/conf/nps.confg配置文件下设置的用户名和密码

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152648727-1489102701.jpg)

如下,便是登录成功后,整个 nps web 控制面板的实际效果图,因为当前暂时还没有任何客户端在线,所以才全部显示为

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152649387-1051885394.jpg)

客户端，新建一个客户端的链接方式（注意此处的这个 用户名和密码,只有在进行 socks5 和 http 代理时才会用到）

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152649974-1723173939.png)

以下是客户端创建成功后的样子,特别注意下这个 id,后面的所有隧道代理和socks5代理都会基于这个 id 来创建

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152650546-901288886.png)

客户端下执行命令: .

/npc -server=106.13.218.47:8024 -vkey=yxznk7q02rirabtz -type=tcp

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152651117-1045580108.png)

发现客户端已在线，表示已与服务器端进行了连接

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152651654-1745806902.png)

## tcp隧道

适用范围： ssh、远程桌面，数据库等tcp连接场景

假设场景： 想通过访问公网服务器1.1.1.1的2022端口，连接内网机器192.168.126.128:的22端口，实现ssh连接

使用步骤

* 在刚才创建的客户端隧道管理中添加一条tcp隧道，填写监听的端口（2022）、内网目标ip和目标端口（192.168.126.128:22），保存

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152652288-366356992.png)

* 访问公网服务器ip（1.1.1.1）,填写的监听端口(2022)，相当于访问内网ip(192.168.126.128):目标端口(22)

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152652825-801680511.png)

## udp隧道

适用范围： 内网dns解析等udp连接场景

假设场景： 内网有一台dns（10.1.50.102:53），在非内网环境下想使用该dns，公网服务器为1.1.1.1

使用步骤

* 在刚才创建的客户端的隧道管理中添加一条udp隧道，填写监听的端口（53）、内网目标ip和目标端口（10.1.50.102:53），保存。
* 修改需要使用的dns地址为1.1.1.1，则相当于使用10.1.50.102作为dns服务器

## socks5代理

适用范围： 在外网环境下如同使用vpn一样访问内网设备或者资源

假设场景： 想将公网服务器1.1.1.1的3538端口作为socks5代理，达到访问内网任意设备或者资源的效果

使用步骤

* 在刚才创建的客户端隧道管理中添加一条socks5代理，填写监听的端口（3538），保存

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152653386-973001912.png)

* 在外网环境的本机配置socks5代理(例如使用proxifier进行全局代理)，ip为公网服务器ip（1.1.1.1），端口为填写的监听端口(3438)，即可畅享内网了

添加代理服务器

菜单栏点击Proxy Servers图标—add，这里添加socks代理，填写socks服务端的ip和端口[ 一定要记得此处的代理是有账号密码的,也就是我们开始创建客户端配置时设置的那个账号密码 ]

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152654160-355578952.png)

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152654720-1704114224.png)

单击Proxification Rules图标—add，这里设置如果访问192.168.126.\* 目标内网段，这个ip段则走socks5代理

![](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509152655435-1953238627.png)

勾选我们添加的代理规则，默认的代理规勾选为Direct！！！记得

![](https://img2023.cnb...