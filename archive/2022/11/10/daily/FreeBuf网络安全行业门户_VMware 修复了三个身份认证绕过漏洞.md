---
title: VMware 修复了三个身份认证绕过漏洞
url: https://www.freebuf.com/articles/349339.html
source: FreeBuf网络安全行业门户
date: 2022-11-10
fetch_date: 2025-10-03T22:15:07.947607
---

# VMware 修复了三个身份认证绕过漏洞

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

VMware 修复了三个身份认证绕过漏洞

* ![]()
* 关注

VMware 修复了三个身份认证绕过漏洞

2022-11-09 19:17:27

所属地 上海

Bleeping Computer  网站披露，VMware 近期发布了安全更新，以解决 Workspace ONE Assist 解决方案中的三个严重漏洞，分别追踪为 CVE-2022-31685（认证绕过）、CVE-2022-31686 （认证方法失败）和 CVE-2022-31687 （认证控制失败）。据悉，这些漏洞允许远程攻击者绕过身份验证并提升管理员权限。![1667992735_636b8c9f1b4b13affe56f.jpg!small?1667992735334](https://image.3001.net/images/20221109/1667992735_636b8c9f1b4b13affe56f.jpg!small?1667992735334)

Workspace ONE Assist  可以提供远程控制、屏幕共享、文件系统管理和远程命令执行，以帮助服务后台和 IT 人员从 Workspace ONE 控制台实时远程访问设备并排除故障。

未经身份认证的威胁攻击者可以在不需要用户交互进行权限升级的低复杂度攻击中利用这些漏洞。从 VMware 发布的声明来看，一旦具有 Workspace ONE Assist 网络访问权限的恶意攻击者成功利用这些漏洞，无需对应用程序进行身份验证就可以获得管理访问权限。

## ****漏洞现已********修复****

目前，VMware为Windows 已经为客户发布了 Workspace ONE Assist 22.10（89993），对这些漏洞进行了修补。

此外，VMware 还修补了一个反射式跨站脚本（XSS）漏洞（CVE-2022-31688）以及一个会话固定漏洞（CVE-2022-31689），前者允许攻击者在目标用户的窗口中注入 javascript 代码，，后者允许攻击者获得有效会话令牌后进行身份验证。

![](https://image.3001.net/images/20221109/1667992787_636b8cd3d11ebe9789f23.png!small)值得一提的是，Workspace ONE Assist 22.10 版本修补的所有漏洞都是由 REQON IT-Security的Jasper Westerman、Jan van der Put、Yanick de Pater 和 Harm Blankers 发现并报告给 VMware 的。

## VMware 修复了多个安全漏洞

今年 8 月，VMware 警告管理员要修补 VMware Workspace ONE Access、Identity Manager 和 vRealize Automation 中另外一个关键身份认证绕过安全漏洞，该漏洞允许未经认证的攻击者获得管理权限。

同年 5 月，Mware 修补了一个几乎相同的关键漏洞，该漏洞是 Innotec Security的Bruno López 在 Workspace ONE Access、VMware Identity Manager（vIDM）和vRealize Automation 中发现的另一个身份验证绕过漏洞（CVE-222-22972）。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/vmware-fixes-three-critical-auth-bypass-bugs-in-remote-access-tool/

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

漏洞现已修复

VMware 修复了多个安全漏洞

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)