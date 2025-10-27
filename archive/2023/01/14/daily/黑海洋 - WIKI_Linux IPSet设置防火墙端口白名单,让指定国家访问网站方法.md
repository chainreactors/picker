---
title: Linux IPSet设置防火墙端口白名单,让指定国家访问网站方法
url: https://blog.upx8.com/3175
source: 黑海洋 - WIKI
date: 2023-01-14
fetch_date: 2025-10-04T03:53:18.009798
---

# Linux IPSet设置防火墙端口白名单,让指定国家访问网站方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux IPSet设置防火墙端口白名单,让指定国家访问网站方法

发布时间:
2023-01-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
15723

[![](https://blog.tag.gg/d/file/p/2022/05-05/ea0f719fb74ae4d6012ae279df8616a7.jpg)](https://blog.tag.gg/d/file/p/2022/05-05/ea0f719fb74ae4d6012ae279df8616a7.jpg)

前言：之前转载过几篇在linux系统中屏蔽指定国家ip达到预防CC攻击的目的.本教程将介绍利用IPSet设置只允许某国家访问网站的方法。
**相关阅读：**
**1、Linux系统屏蔽国外(海外)IP解决被CC攻击的方法：**[https://blog.tag.gg/showinfo-3-36155-0.html](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnRhZy5nZy9zaG93aW5mby0zLTM2MTU1LTAuaHRtbA)
**2、被CC攻击了怎么办?Linux系统使用shell脚本自动屏蔽简单解决CC攻击方法：**[https://blog.tag.gg/showinfo-3-36156-0.html](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnRhZy5nZy9zaG93aW5mby0zLTM2MTU2LTAuaHRtbA)
**3、Linux脚本iptables屏蔽指定国家或海外IP恶意访问网站的详细方法：**[https://blog.tag.gg/showinfo-3-36210-0.html](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnRhZy5nZy9zaG93aW5mby0zLTM2MjEwLTAuaHRtbA)

---

**方法**
首先需要得到国家IP段，下载地址：http://www.ipdeny.com/ipblocks/。这里以我们国家为例。
**1、安装ipset**
#Debian/Ubuntu系统

> apt-get -y install ipset

#CentOS系统

> yum -y install ipset

CentOS 7还需要关闭firewall防火墙：

> systemctl stop firewalld.service
> systemctl disable firewalld.service

**2、清空之前的规则**
#防止设置不生效，建议清空下之前的防火墙规则

> iptables -P INPUT ACCEPT
> iptables -F

**3、创建新规则**
#创建一个名为cnip的规则

> ipset -N cnip hash:net

#下载国家IP段，这里以中国为例

> wget -P . http://www.ipdeny.com/ipblocks/data/countries/cn.zone

#将IP段添加到cnip规则中

> for i in $(cat /root/cn.zone ); do ipset -A cnip $i; done

**4、设置IP段白名单**
#放行IP段

> iptables -A INPUT -p tcp -m set --match-set cnip src -j ACCEPT

#关掉所有端口

> iptables -P INPUT DROP

这时候就只有指定国家的IP能访问服务器了。
如果你在国内，网站不允许被国内人访问，建议别关所有端口，这样你的SSH会上不去，我们可以只关闭80/443端口。
#关闭指定端口，比如80/443

> iptables -A INPUT -p tcp --dport 80 -j DROP
> iptables -A INPUT -p tcp --dport 443 -j DROP

这时候其他国家的IP是无法访问你服务器的80/443端口，等于无法访问你的网站，其它端口还是可以访问的。
**5、删除规则**
#将参数里的-A改成-D就是删除规则了，如

> iptables -D INPUT -p tcp -m set --match-set cnip src -j ACCEPT
> iptables -D INPUT -p tcp --dport 443 -j DROP

**说明**
设置防火墙后，可能有些服务器重启系统后会清空防火墙规则，导致设置的失效，所以我们设置规则后，需要使用iptables命令保存下，保存命令可能在很多系统中都不通用，这里就不说了，需要各位自行搜索解决了，有耐心的也可以每次重启的时候都重新设置一下防火墙。

[取消回复](https://blog.upx8.com/3175#respond-post-3175)

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