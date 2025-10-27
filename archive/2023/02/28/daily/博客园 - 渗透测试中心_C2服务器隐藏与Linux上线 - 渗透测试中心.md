---
title: C2服务器隐藏与Linux上线 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17159661.html
source: 博客园 - 渗透测试中心
date: 2023-02-28
fetch_date: 2025-10-04T08:15:04.412330
---

# C2服务器隐藏与Linux上线 - 渗透测试中心

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

# [C2服务器隐藏与Linux上线](https://www.cnblogs.com/backlion/p/17159661.html "发布于 2023-02-27 14:49")

# 工具准备

国外服务器一台

自由鲸（VPN）

CS 4.4

nginx

# CS服务端配置

### 服务器禁ping

1、当服务器禁ping后，从某种角度可以判定为主机为不存活状态。

2、编辑文件/etc/sysctl.conf，在里面增加一行。net.ipv4.icmp\_echo\_ignore\_all=1
之后使命命令sysctl -p使配置生效。

```
vim /etc/sysctl.conf
net.ipv4.icmp_echo_ignore_all=1
sysctl -p
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144827835-1460586883.jpg)

3、之后在ping就无法ping通了。这种方式nmap还是可以扫描到服务器的存活的。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144828724-887380428.png)

### 修改端口

1、编辑teamserver文件，搜索50050，将其改为任意端口即可，这里改成65000

```
vim teamserver
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144829610-877637485.jpg)

2、保存退出，启动teamserver，发现端口已经变化。

```
./teamserver xx.xx.xx.xx xiao
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144830703-410050090.jpg)

### 修改默认证书

1、因为cs服务端生成的证书含有cs的相关特征所有，这里进行修改替换。修改方式有两种，分别为生成密钥库和修改启动文件。无论是那种方式都需要删去原有的文件cobaltstrike.store。

#### 方法一删除密钥库文件cobaltstrike.store（推荐）

1、生成新的密钥库文件

```
keytool -keystore ./cobaltstrike.store -storepass 123456 -keypass 123456 -genkey -keyalg RSA -alias baidu -dname "CN=baidu.com, OU=service operation department, O=Beijing Baidu Netcom Science Technology Co.\, Ltd, L=beijing, S=beijing, C=CN"
keytool -importkeystore -srckeystore cobaltstrike.store -destkeystore cobaltstrike.store -deststoretype pkcs12
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144831550-104496929.jpg)

2、查看证书

```
keytool -list -keystore cobaltstrike.store
```

```
![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144832343-1207281071.jpg)
```

3、启动服务器查看证书签名是否相同，经查看证书签名是相同的。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144833138-1324654750.jpg)

#### 方法二修改启动文件

1、teamserver 是启动cs服务端的启动文件。里面有环境检测的部分，其中就包括密钥库的检测，这部分的写法是，如检测不到密钥库就使用命令生成新的密钥库，修改这里生成命令。

2、将teamserver中圈出来的部分需要修改

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144834432-2038016818.jpg)

3、将其修改为如下内容：

```
keytool -keystore ./cobaltstrike.store -storepass 123456 -keypass 123456 -genkey -keyalg RSA -alias baidu -dname "CN=baidu.com, OU=service operation department, O=Beijing Baidu Netcom Science Technology Co.\, Ltd, L=beijing, S=beijing, C=CN"
```

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144835487-2027217953.jpg)

4、删除原有的./cobaltstrike.store密钥库文件，下次启动时会自动生成新的密钥库文件

```
rm -rf cobaltstrike.store
```

# 使用CDN隐藏

### 申请免费域名

1、进入[freenom](https://www.freenom.com/)官网，翻译中文，拉到最下面，选择开发人员。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144836612-1216181926.jpg)

2、拉到最下面，点击今天就获得一个随机的域账号

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144837421-401393924.jpg)

3、输入国际邮箱，然后点击验证邮箱，推荐使用[临时邮箱](https://temp-mail.org/zh)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144838184-1636008870.jpg)

4、几秒钟后，就会收到邮件，点击邮件点击确认跳转到freenom网站，翻译当前网页中文后，点击开发商。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144839006-1381884576.jpg)

5、将网站拉到最后下面，翻译中文，点击立即获取一个随机域账号。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144839826-1580750123.jpg)

6、然后来到个人信息填写页面

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144840800-1795941883.png)

7、因为IP选择的地址是弗罗里达州，所以需要借助[佛罗里达州个人信息生成器](https://www.meiguodizhi.com/usa-address/florida)和[个人信息生成器](https://www.shenfendaquan.com/)，两者需要结合。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144841675-865336806.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144842587-547291091.jpg)

8、信息按照生成器填写即可，填写后，勾选并点击完成订单，到此账号已经注册成功。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144843337-1650934063.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144844087-253020840.jpg)

9、回到网站首页，选取域名，输入xxx.tk，点击check availability，可用的话点击checkout。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144844825-600153102.jpg)

10、选择12个月免费版本，最后点击continue。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144845602-1239189976.jpg)

11、最后完成订单

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144846398-62631944.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144847138-956029880.jpg)

12、选择my domains，看到域名是存活的。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144847955-2046821606.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144848912-1360974677.jpg)

### CDN配置

1、cdn部分可以选择其实挺多的，我这里选择的是[cloudflare](https://dash.cloudflare.com/)

2、登录cloudflare后，选择添加站点

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144849797-584795960.jpg)

3、选择免费计划

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144850575-1858358753.jpg)

4、添加DNS记录，输入要保护的IP和A记录。

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144851699-664827035.jpg)

5、修改xxx.tk的dns服务器为cloudflare。修改完成后需要一定的时间生效

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144852553-675923245.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144853458-201526483.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144854220-1629371275.jpg)

6、关闭自动https重写和始终使用https、broti压缩

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144854987-1863074172.jpg)

7、点击finish完成

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144855745-1923565084.jpg)

8、出现如下界面就设置生效，可以使用cloudflare进行域名解析操作了

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144856530-714652068.jpg)

9、解析一个www.xxx.tk测试一下

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144857198-628058662.jpg)

10、使用全球ping，发现已经成功添加CDN

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144858256-1387941751.jpg)

11、配置SSL/TLS加密模式为完全

![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230227144859102-1493880580.jpg)

### cloudflare生成证书

1、在cloudflare的dash页面找到SSL/TLS->源服务器->创建...