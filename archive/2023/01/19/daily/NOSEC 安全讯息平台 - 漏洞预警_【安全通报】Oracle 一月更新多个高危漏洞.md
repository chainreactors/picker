---
title: 【安全通报】Oracle 一月更新多个高危漏洞
url: https://nosec.org/home/detail/5062.html
source: NOSEC 安全讯息平台 - 漏洞预警
date: 2023-01-19
fetch_date: 2025-10-04T04:16:10.347174
---

# 【安全通报】Oracle 一月更新多个高危漏洞

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

# 【安全通报】Oracle 一月更新多个高危漏洞

![](https://nosec.org/home/image/headImg.png)xiannv  989天前

![Image](/avatar/uploads/attach/image/0020d39d11bf8c80ac757f5ebbf3c8e4/Snipaste_2022-01-19_10-16-43.png)

近日，Oracle官方 发布了 2023 年 1 月份的安全更新。涉及旗下产品（Weblogic Server、Database Server、Java SE、MySQL等）的 327 个漏洞。此次修复的漏洞中包括 10 个和 Weblogic 相关的漏洞，均无需身份验证和用户交互即可通过网络进行远程利用。

## FOFA 查询

[app="BEA-WebLogic-Server" || app="Weblogic\_interface\_7001"](https://fofa.info/result?qbase64=YXBwPSJCRUEtV2ViTG9naWMtU2VydmVyIiB8fCAgYXBwPSJXZWJsb2dpY19pbnRlcmZhY2VfNzAwMSI%3D)

## 影响范围

```
CVE-2023-21839
Weblogic Server 12.2.1.3.0
Weblogic Server 12.2.1.4.0
Weblogic Server 14.1.1.0.0
```

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（app="BEA-WebLogic-Server" || app="Weblogic\_interface\_7001"）共有 124,386 个相关服务对外开放。中国使用数量最多，共有 43,848 个；美国第二，共有 27,307 个；日本第三，共有 4,524 个；德国第四，共有 4,043 个；印度第五，共有 3,891 个。

![2023-01-17-21-54-37-image.png](/avatar/uploads/attach/image/4091ac8d341d33d6586cb787dee5b7e4/2023-01-17-21-54-37-image.png)

中国大陆地区北京使用数量最多，共有 9,947 个；浙江第二，共有 6,791 个；上海第三，共有 4,437 个；广东第四，共有 3,695 个；山东第五，共有 3,220 个。

![2023-01-17-21-55-36-image.png](/avatar/uploads/attach/image/04f51f549d48212c2421455bcb55db00/2023-01-17-21-55-36-image.png)

## 修复方案

**通用修补建议**

参考Oracle官方更新的补丁，及时进行更新：<https://www.oracle.com/security-alerts/cpujan2023.html>

## 参考

[1] <https://www.oracle.com/security-alerts/cpujan2023.html>

白帽汇安全研究院从事信息安全，专注于安全大数据、企业威胁情报。

公司产品：FOFA-网络空间安全搜索引擎、FOEYE-网络空间检索系统、NOSEC-安全讯息平台。

为您提供：网络空间测绘、企业资产收集、企业威胁情报、应急响应服务。

[上一篇：
【漏洞通报】Harbor 镜像仓库未授权......](/home/detail/5061.html)
[下一篇：
【漏洞通报】Weblogic远......](/home/detail/5063.html)

浏览: 28379
评论: 0

![](https://nosec.org/home/image/weibo.png)

#### 最新评论

![](/home/image/loading.gif)
评论正在提交，请稍等...

昵称

邮箱

已有账号，[登录](/home/caslogin)评论

提交评论

[x]  有人回复邮件通知我

![](https://nosec.org/home/image/code.png)

## 相关推荐

[【安全通报】Apache ShardingSph...](/home/detail/4308.html "【安全通报】Apache ShardingSphere远程代码执行漏洞")

[【安全通报】Skywalking远程代码...](/home/detail/4678.html "【安全通报】Skywalking远程代码执行漏洞")

[【安全通报】Tomcat 拒绝服务漏...](/home/detail/4487.html "【安全通报】Tomcat 拒绝服务漏洞")

[【安全通报】FortiProxy SSL VPN...](/home/detail/4691.html "【安全通报】FortiProxy SSL VPN未授权访问漏洞(CVE-2021-22128)")

[【安全通报】Apache Druid 远程...](/home/detail/4714.html "【安全通报】Apache Druid 远程代码执行漏洞 (CVE-2021-26919)")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)