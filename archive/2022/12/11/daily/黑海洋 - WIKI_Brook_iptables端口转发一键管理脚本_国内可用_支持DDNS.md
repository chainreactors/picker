---
title: Brook/iptables端口转发一键管理脚本/国内可用/支持DDNS
url: https://blog.upx8.com/3146
source: 黑海洋 - WIKI
date: 2022-12-11
fetch_date: 2025-10-04T01:12:32.391422
---

# Brook/iptables端口转发一键管理脚本/国内可用/支持DDNS

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Brook/iptables端口转发一键管理脚本/国内可用/支持DDNS

发布时间:
2022-12-10

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
19129

iptables是一款非常强大的防火墙管理工具，同样支持端口转发，同时也支持端口段转发<BBR对于iptables不起作用的>

brook脚本流量转发，可转发TCP/UDP流量，支持动态域名转发，不支持端口段转发，可以自行配置brook.conf（/usr/local/brook-pf/brook.conf）运行。

推荐使用brook或者haproxy(不支持UDP流量)。

其他端口转发工具：nginx，gost，ehco，socat，realm（[https://github.com/seal0207/EasyRealM](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3NlYWwwMjA3L0Vhc3lSZWFsTQ)）

## Iptables端口转发/流量转发脚本

**国内可用：**

```
wget --no-check-certificate -qO natcfg.sh http://www.arloor.com/sh/iptablesUtils/natcfg.sh && bash natcfg.sh
```

```
国外可用：
```

|  |  |
| --- | --- |
|  | wget --no-check-certificate -qO natcfg.sh https://raw.githubusercontent.com/arloor/iptablesUtils/master/natcfg.sh && bash natcfg.sh |
|  | #卸载 |
|  | wget --no-check-certificate -qO uninstall.sh https://raw.githubusercontent.com/arloor/iptablesUtils/master/dnat-uninstall.sh && bash uninstall.sh |

**使用：**

![Brook/iptables端口转发一键管理脚本/国内可用/支持DDNS](https://maobuni.com/wp-content/uploads/2022/01/image-13-1024x389.png "Brook/iptables端口转发一键管理脚本/国内可用/支持DDNS")

来源：[https://github.com/arloor/iptablesUtils](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FybG9vci9pcHRhYmxlc1V0aWxz)

## Brook端口转发/流量转发脚本

**For RHEL / CentOS:**

```
yum install bind-utils -y && yum install wget -y && wget https://raw.githubusercontent.com/ECIAP/brook/master/brook-pf-mod.sh && chmod +x brook-pf-mod.sh && bash brook-pf-mod.sh
```

**For Debian / Ubuntu:**

```
apt-get install dnsutils -y && sudo apt-get install wget -y && wget https://raw.githubusercontent.com/ECIAP/brook/master/brook-pf-mod.sh && chmod +x brook-pf-mod.sh && bash brook-pf-mod.sh
```

**对于v20200801以及之前版本可以使用：**

|  |  |
| --- | --- |
|  | wget https://raw.githubusercontent.com/NewCheung/brook/master/brook-pf-mod.sh && bash brook-pf-mod.sh |
|  | #管理界面之后手动输入版本号，如： |
|  | v20200801 |

来源：[https://github.com/ECIAP/brook](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0VDSUFQL2Jyb29r)

## **Brook国内服务器可用脚本:**

本站提供，解决国内机器与github链接不佳

centos提前安装：yum install bind-utils -y

debian提前安装：apt-get install dnsutils -y

|  |  |
| --- | --- |
|  | wget http://download.maobuni.com/brook/brook-pf-mod.sh |
|  | bash brook-pf-mod.sh |
|  | #直接安装v20200801版本 |

[取消回复](https://blog.upx8.com/3146#respond-post-3146)

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