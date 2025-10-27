---
title: Linux脚本iptables屏蔽指定国家或海外IP恶意访问网站的详细方法
url: https://blog.upx8.com/3176
source: 黑海洋 - WIKI
date: 2023-01-14
fetch_date: 2025-10-04T03:53:17.755667
---

# Linux脚本iptables屏蔽指定国家或海外IP恶意访问网站的详细方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux脚本iptables屏蔽指定国家或海外IP恶意访问网站的详细方法

发布时间:
2023-01-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
18309

[![](https://blog.tag.gg/d/file/p/2022/05-05/eb773959348d3d3fd25c979931f694c6.jpg)](https://blog.tag.gg/d/file/p/2022/05-05/eb773959348d3d3fd25c979931f694c6.jpg)

**前言：**对于网站站长来说,经常遇到海外ip恶意抓取或恶意CC攻击的情况,对于这种问题,很是头痛,之前本站也有一篇教程介绍在Linux系统下使用SH脚本如何屏蔽海外ip的详细方法,虽然可以屏蔽,但功能不强大,本次在网上找到了一篇非常使用的教程，可以屏蔽指定国家的ip访问服务器,现在转载过来,希望对大家有帮助
本教程

**相关阅读：**
**1、Linux系统屏蔽国外(海外)IP解决被CC攻击的方法：**[https://blog.tag.gg/showinfo-3-36155-0.html](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnRhZy5nZy9zaG93aW5mby0zLTM2MTU1LTAuaHRtbA)
**2、被CC攻击了怎么办?Linux系统使用shell脚本自动屏蔽简单解决CC攻击方法：**[https://blog.tag.gg/showinfo-3-36156-0.html](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnRhZy5nZy9zaG93aW5mby0zLTM2MTU2LTAuaHRtbA)

---

**功能：屏蔽指定国家地区的IP访问**
**方法一：使用大神的开源脚本，屏蔽指定国家地区的IP访问**
执行如下命令下载脚本并执行

> wget https://blog.tag.gg/soft/block-ips.sh
> sh block-ips.sh

执行效果如图
封禁`ip`时会要求你输入国家代码，国家代码以及国家对应的ip段可查看：[点击进入](https://blog.upx8.com/go/aHR0cDovL3d3dy5pcGRlbnkuY29tL2lwYmxvY2tz)。记住所填参数均为小写字母。比如`JAPAN (JP)`，我们就输入`jp`这个参数

[![](https://blog.tag.gg/d/file/p/2022/05-05/6e3c5c325db126e61aec4a8736c79370.jpg)](https://blog.tag.gg/d/file/p/2022/05-05/6e3c5c325db126e61aec4a8736c79370.jpg)

**方法二：使用IPIP的数据库进行流量屏蔽（推荐，目前已支持centos6和7还有ubuntu系统）**
1、创建一个shell脚本文件例如block\_ip.sh,并写入如下代码保存

> #!/bin/bash
> #判断是否具有root权限
> root\_need() {
>     if [[ $EUID -ne 0 ]]; then
>         echo "Error:This script must be run as root!" 1>&2
>         exit 1
>     fi
> }
>
> #检查系统分支及版本(主要是：分支->>版本>>决定命令格式)
> check\_release() {
>     if uname -a | grep el7  ; then
>         release="centos7"
>     elif uname -a | grep el6 ; then
>         release="centos6"
>         yum install ipset -y
>     elif cat /etc/issue |grep -i ubuntu ; then
>         release="ubuntu"
>         apt install ipset -y
>     fi
> }
>
> #安装必要的软件(wget),并下载中国IP网段文件(最后将局域网地址也放进去)
> get\_china\_ip() {
>     #安装必要的软件(wget)
>     rpm --help >/dev/null 2>&1 && rpm -qa |grep wget >/dev/null 2>&1 ||yum install -y wget ipset >/dev/null 2>&1
>     dpkg --help >/dev/null 2>&1 && dpkg -l |grep wget >/dev/null 2>&1 ||apt-get install wget ipset -y >/dev/null 2>&1
>
>     #该文件由IPIP维护更新，大约一月一次更新(也可以用我放在国内的存储的版本，2018-9-8日版)
>     [ -f china\_ip\_list.txt ] && mv china\_ip\_list.txt china\_ip\_list.txt.old
>     wget https://github.com/17mon/china\_ip\_list/blob/master/china\_ip\_list.txt
>     cat china\_ip\_list.txt |grep 'js-file-line">' |awk -F'js-file-line">' '{print $2}' |awk -F'< ' '{print $1}' >> china\_ip.txt
>     rm -rf china\_ip\_list.txt
>     #wget https://qiniu.wsfnk.com/china\_ip.txt
>
>     #放行局域网地址
>     echo "192.168.0.0/18" >> china\_ip.txt
>     echo "10.0.0.0/8" >> china\_ip.txt
>     echo "172.16.0.0/12" >> china\_ip.txt
> }
>
> #只允许国内IP访问
> ipset\_only\_china() {
>     echo "ipset create whitelist-china hash:net hashsize 10000 maxelem 1000000" > /etc/ip-black.sh
>     for i in $( cat china\_ip.txt )
>     do
>             echo "ipset add whitelist-china $i" >> /etc/ip-black.sh
>     done
>     echo "iptables -I INPUT -m set --match-set whitelist-china src -j ACCEPT" >> /etc/ip-black.sh
>     #拒绝非国内和内网地址发起的tcp连接请求（tcp syn 包）（注意，只是屏蔽了入向的tcp syn包，该主机主动访问国外资源不用影响）
>     echo "iptables  -A INPUT -p tcp --syn -m connlimit --connlimit-above 0 -j DROP" >> /etc/ip-black.sh
>     #拒绝非国内和内网发起的ping探测（不影响本机ping外部主机）
>     echo "iptables  -A INPUT -p icmp -m icmp --icmp-type 8 -j DROP" >> /etc/ip-black.sh
>     #echo "iptables -A INPUT -j DROP" >> /etc/ip-black.sh
>     rm -rf china\_ip.txt
> }
>
> run\_setup() {
>     chmod +x /etc/rc.local
>     sh /etc/ip-black.sh
>     rm -rf /etc/ip-black.sh
>     #下面这句主要是兼容centos6不能使用"-f"参数
>     ipset save whitelist-china -f /etc/ipset.conf || ipset save whitelist-china > /etc/ipset.conf
>     [ $release = centos7 ] && echo "ipset restore -f /etc/ipset.conf" >> /etc/rc.local
>     [ $release = centos6 ] && echo "ipset restore < /etc/ipset.conf" >> /etc/rc.local
>     echo "iptables -I INPUT -m set --match-set whitelist-china src -j ACCEPT" >> /etc/rc.local
>     echo "iptables  -A INPUT -p tcp --syn -m connlimit --connlimit-above 0 -j DROP" >> /etc/rc.local
>     echo "iptables  -A INPUT -p icmp -m icmp --icmp-type 8 -j DROP" >> /etc/rc.local
>     #echo "iptables -A INPUT -j DROP" >> /etc/rc.local
> }
>
> main() {
>     check\_release
>     get\_china\_ip
>     ipset\_only\_china
>
> case "$release" in
> centos6)
>     run\_setup
>     ;;
> centos7)
>     chmod +x /etc/rc.d/rc.local
>     run\_setup
>     ;;
> ubuntu)
>     sed -i '/exit 0/d' /etc/rc.local
>     run\_setup
>     echo "exit 0" >> /etc/rc.local
>     ;;
> esac
> }
> main

2、输入命令 block\_ip.sh 执行脚本即可。
希望对大家有帮助

[取消回复](https://blog.upx8.com/3176#respond-post-3176)

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