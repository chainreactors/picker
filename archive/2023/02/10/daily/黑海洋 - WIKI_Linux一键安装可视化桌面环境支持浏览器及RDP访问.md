---
title: Linux一键安装可视化桌面环境支持浏览器及RDP访问
url: https://blog.upx8.com/3211
source: 黑海洋 - WIKI
date: 2023-02-10
fetch_date: 2025-10-04T06:14:29.077817
---

# Linux一键安装可视化桌面环境支持浏览器及RDP访问

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux一键安装可视化桌面环境支持浏览器及RDP访问

发布时间:
2023-02-09

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
17215

![](https://sunpma.com/usr/uploads/2021/12/2500300474.jpg)

## 说明

* 支持：`Ubuntu 18.04/20.04` `Debian 10` `CentOS 7/8`；
* 内存：`Ubuntu/Debian` 1G以上 `CentOS` 1.5G以上；
* 支持浏览器访问，同时支持`Windows`自带的远程连接通过3389访问；
* 编译安装`Guacamole`服务器；
* 配置`Guacamole Web APP`；
* 安装`Tomcat 9` `XRDP/TigerVNC` `XFCE4`桌面环境及火狐浏览器；
* 一键安装配置`Let’s Encrypt`安全证书，开启`OCSP`装订；
* 支持安装`Nginx`反代`Tomcat`；

## 预览

[![](https://sunpma.com/usr/uploads/2021/12/2684543372.png)](https://sunpma.com/usr/uploads/2021/12/2684543372.png)
[![](https://sunpma.com/usr/uploads/2021/12/2991849531.png)](https://sunpma.com/usr/uploads/2021/12/2991849531.png)
[![](https://sunpma.com/usr/uploads/2021/12/2863663085.png)](https://sunpma.com/usr/uploads/2021/12/2863663085.png)
[![](https://sunpma.com/usr/uploads/2021/12/3235156355.png)](https://sunpma.com/usr/uploads/2021/12/3235156355.png)
[![](https://sunpma.com/usr/uploads/2021/12/3938299294.png)](https://sunpma.com/usr/uploads/2021/12/3938299294.png)

## 中文支持

如果需要中文显示，需要修改系统语言，并添加中文字体；
**安装中文语言包**

```
apt-get install language-pack-zh* -y
apt-get install chinese* -y
```

**安装亚洲字体**

```
apt-get install fonts-arphic-ukai fonts-arphic-uming fonts-ipafont-mincho fonts-ipafont-gothic fonts-unfonts-core -y
```

**重置系统区域**

```
dpkg-reconfigure locales
```

选择`All locales`后回车；
[![](https://sunpma.com/usr/uploads/2021/12/2994789300.png)](https://sunpma.com/usr/uploads/2021/12/2994789300.png)
选择`zh_CN.UTF-8`后回车；
[![](https://sunpma.com/usr/uploads/2021/12/829690686.png)](https://sunpma.com/usr/uploads/2021/12/829690686.png)
**等待更新完成后重启服务器；**

## 安装桌面

可以直接使用`ROOT`用户安装，也可以选择其它系统用户安装；
安装过程都是中文的，根据提示进行设置即可；

```
wget https://raw.githubusercontent.com/Har-Kuun/OneClickDesktop/master/OneClickDesktop_zh-CN.sh && sudo bash OneClickDesktop_zh-CN.sh
```

如果出现以下界面，直接回车即可；
[![](https://sunpma.com/usr/uploads/2021/12/2015073175.png)](https://sunpma.com/usr/uploads/2021/12/2015073175.png)
安装完成后即可使用`http://YOU_IP:8080/guacamole`进行访问或者直接3389连接
`Guacamole`的登陆账户为安装时自行设定的，然后输入系统用户及密码来完成登录；

如果没有火狐浏览器就自己安装：apt install firefox

## 其它设置

默认端口修改，编辑文件`/etc/tomcat9/server.xml`文件修改其中的`8080`端口后保存
然后使用`systemctl restart tomcat9`命令重启`tomcat`即可；

由于现代浏览器的限制无法在本地和网页桌面上进行复制粘贴
解决此问题可以使用带`SSL`的域名进行反向代理
**#宝塔反向代理（复制到站点的配置文件里，删除location相关代码替换以下内容）：**
location / {
 proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
 proxy\_set\_header Host $http\_host;
 proxy\_set\_header X-Real-IP $remote\_addr;
 proxy\_set\_header Range $http\_range;
 proxy\_set\_header If-Range $http\_if\_range;
 proxy\_redirect off;
 proxy\_pass http://127.0.0.1:8080/guacamole/;
}

**参考链接**
[https://github.com/Har-Kuun/OneClickDesktop](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0hhci1LdXVuL09uZUNsaWNrRGVza3RvcA)
[https://qing.su/article/oneclick-desktop.html](https://blog.upx8.com/go/aHR0cHM6Ly9xaW5nLnN1L2FydGljbGUvb25lY2xpY2stZGVza3RvcC5odG1s)

[取消回复](https://blog.upx8.com/3211#respond-post-3211)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")