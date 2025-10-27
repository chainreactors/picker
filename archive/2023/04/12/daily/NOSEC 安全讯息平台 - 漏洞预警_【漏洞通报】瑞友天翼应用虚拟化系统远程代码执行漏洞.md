---
title: 【漏洞通报】瑞友天翼应用虚拟化系统远程代码执行漏洞
url: https://nosec.org/home/detail/5078.html
source: NOSEC 安全讯息平台 - 漏洞预警
date: 2023-04-12
fetch_date: 2025-10-04T11:29:06.873034
---

# 【漏洞通报】瑞友天翼应用虚拟化系统远程代码执行漏洞

[![](https://nosec.org/home/image/logo.png)](/)

[登录/注册](https://nosec.org/home/caslogin)

[投稿](https://nosec.org/home/caslogin)

[首页](/home/index)
[威胁情报](/home/index/threaten.html)
[安全动态](/home/index/security.html)
[漏洞预警](/home/index/hole.html)

数据泄露

* [新闻浏览](/home/index/leakage.html)
* [图表统计](/home/index/graphshtml)

[专题报告](/home/index/speech.html)
[技术分析](/home/index/skill.html)
[安全工具](/home/index/tool.html)

# 【漏洞通报】瑞友天翼应用虚拟化系统远程代码执行漏洞

![](https://nosec.org/home/image/headImg.png)xiannv  906天前

# 一、    漏洞概述

瑞友天翼应用虚拟化系统（GWT System）是国内具有自主知识产权的应用虚拟化平台，是基于服务器计算（Server-ba sedComputing）的应用虚拟化平台。它将用户所有应用软件（ERP、OA、CRM、PDM、CAD……）集中部署在天翼服务器（群）上，客户端通过WEB即可快速安全的访问经服务器上授权的应用软件，实现集中应用、远程接入、协同办公等，从而为用户打造集中、便捷、安全、高效的虚拟化支撑平台。

瑞友天翼应用虚拟化系统远程代码执行漏洞(0day)，攻击者可以通过该漏洞执行任意代码，导致系统被攻击与控制。瑞友天翼应用虚拟化系统是基于服务器计算架构的应用虚拟化平台，它将用户各种应用软件集中部署到瑞友天翼服务集群，客户端通过WEB即可访问经服务器上授权的应用软件，实现集中应用、远程接入、协同办公等。

# 二、    影响范围

本次漏洞影响范围如下：

| 5.x <= 瑞友天翼 <= 7.0.2.1 |
| --- |

FOFA Query：

| [app="REALOR-天翼应用虚拟化系统"](https://fofa.info/result?qbase64=YXBwPSJSRUFMT1It5aSp57%2B85bqU55So6Jma5ouf5YyW57O757ufIg%3D%3D) |
| --- |

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（app="REALOR-天翼应用虚拟化系统"）共有53,946个相关服务对外开放。中国使用数量最多，共有53,810个；中国香港特别行政区第二，共有53个；印尼第三，共有39个；新加坡第四，共有22个；巴基斯坦第五，共19个。

全球范围内分布情况如下（仅为分布情况，非漏洞影响情况）：

![1.png](/avatar/uploads/attach/image/9ff41a84640fad021f0e93208674c21e/1.png)

中国大陆地区广东使用数量最多，共有14,789个；福建第二，共有4,734个；上海第三，共有2,269个；河南第四，共有1,887个；浙江第五，共有1,857个。

![image.png](/avatar/uploads/attach/image/3323e6a2791b9592c041aeb54282c515/image.png)

# 三、    漏洞复现

白帽汇安全研究院于第一时间复现了该漏洞：

![3.png](/avatar/uploads/attach/image/2ff08558d93dd3a73356d8b42d4920a8/3.png)

# 四、    修复建议

1、官方已修复该漏洞，请及时关注厂商修复信息： <http://www.realor.cn/product/tianyi>

2、通过防火墙等安全设备设置访问策略，设置白名单访问。

 3、如非必要，禁止公网访问该系统。

# 五、    参考链接

[1.]    <http://www.realor.cn/product/tianyi>

[上一篇：
Goby 利用内存马中的一些技术细节【技......](/home/detail/5077.html)
[下一篇：
跨越语言的艺术：Weblogi......](/home/detail/5079.html)

浏览: 25863
评论: 5

![](https://nosec.org/home/image/weibo.png)

#### 最新评论

![](/home/image/headImg.png)

realor
 :
谢谢白帽安全讯息平台！针对改漏洞，瑞友\*\*目前已发布新版本进行漏洞修复，可以在瑞友\*\*(\*\*.realor.cn)下载最新版本，建议使用瑞友天翼应用虚拟化\*\*的用户尽快进行版本更新，同时做好网络访问的\*\*，尽量避免瑞友天翼应用虚拟化\*\*\*\*在公网或不安全的网络\*\*中。

904天前
回复

![](/home/image/headImg.png)

realor
 :
这个漏洞瑞友\*\*已经修复啦，可以去瑞友\*\*下载最新版本。

904天前
回复

![](/home/image/headImg.png)

666
 :
666

430天前
回复

![](/home/image/headImg.png)

666
 :
a

430天前
回复

![](/home/image/headImg.png)

666
 :
a

430天前
回复

![](/home/image/loading.gif)
评论正在提交，请稍等...

昵称

邮箱

已有账号，[登录](/home/caslogin)评论

提交评论

[x]  有人回复邮件通知我

![](https://nosec.org/home/image/code.png)

## 相关推荐

[【安全通报】Atlassian JIRA 多...](/home/detail/4797.html "【安全通报】Atlassian JIRA 多个产品远程代码执行漏洞（CVE-2020-36239）")

[【安全通报】微软10月漏洞补丁日...](/home/detail/4885.html "【安全通报】微软10月漏洞补丁日修复多个高危漏洞")

[【安全通报】Weblogic 七月份更...](/home/detail/5032.html "【安全通报】Weblogic 七月份更新多个高危漏洞")

[【安全通报】Cisco ASA 和 Cisco...](/home/detail/4514.html "【安全通报】Cisco ASA 和 Cisco Firepower 未授权读取文件漏洞")

[【安全通报】通达OA 多个高危漏...](/home/detail/4534.html "【安全通报】通达OA 多个高危漏洞")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)