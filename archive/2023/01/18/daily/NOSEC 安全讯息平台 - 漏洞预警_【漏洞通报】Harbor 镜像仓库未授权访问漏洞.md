---
title: 【漏洞通报】Harbor 镜像仓库未授权访问漏洞
url: https://nosec.org/home/detail/5061.html
source: NOSEC 安全讯息平台 - 漏洞预警
date: 2023-01-18
fetch_date: 2025-10-04T04:06:15.764285
---

# 【漏洞通报】Harbor 镜像仓库未授权访问漏洞

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

# 【漏洞通报】Harbor 镜像仓库未授权访问漏洞

![](https://nosec.org/home/image/headImg.png)xiannv  990天前

![1.jpg](/avatar/uploads/attach/image/cf414dfc5d878675dec69769de3bf521/1.jpg)

# 一、        漏洞概述

Harbor 是一个开源的 Docker Registry 管理项目，用于托管容器镜像。

Harbor 镜像仓库存在配置不当导致的访问控制缺陷，攻击者可通过页面搜索镜像名称，绕过登陆验证逻辑，直接查看结果中未授权的私有镜像仓库并获取仓库信息（Pull、Push的时间和commit信息，以及镜像存在的漏洞信息等）。

# 二、        影响范围

本次漏洞影响范围如下：

| Harbor 所有版本 |
| --- |

FOFA Query：

| app="HARBOR" |
| --- |

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（app="HARBOR"）共有 25,524 个相关服务对外开放。中国使用数量最多，共有 15,796 个；美国第二，共有 2,640 个；德国第三，共有 1,310 个；中国香港特别行政区第四，共有679 个；新加坡第五，共有 650 个。

全球范围内分布情况如下（仅为分布情况，非漏洞影响情况）：

![2.png](/avatar/uploads/attach/image/957fd6d9f66106d62a236a6467e02900/2.png)

中国大陆地区北京使用数量最多，共有1,964 个；广东第二，共有 1,582 个；浙江第三，共有 1,438 个；上海第四，共有 1,228 个；四川第五，共有 440 个。

![3.png](/avatar/uploads/attach/image/6583dc2242b955172bc30bcdb2851f5d/3.png)

# 三、        漏洞复现

白帽汇安全研究院第一时间复现了该漏洞：

![4.png](/avatar/uploads/attach/image/dc1193ffe79522037ff793c9149ccafe/4.png)

# 四、        修复建议

此漏洞为配置不当导致，建议用户修改配置：“项目设置”——“配置管理”——“项目仓库”中的“公开”取消勾选，即可限制公开访问。如图：

![5.png](/avatar/uploads/attach/image/55ac1c8749ae7dd24c1aa28878e0c9cf/5.png)

# 五、        参考链接

[1.]  <https://github.com/lanqingaa/123/blob/main/README.md>

[上一篇：
FOFA实战攻防对抗中企业安全运营场景下......](/home/detail/5060.html)
[下一篇：
【安全通报】Oracle 一月......](/home/detail/5062.html)

浏览: 38053
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

[Joomla! 3.7.5 - LDAP注入20秒破...](/home/detail/1571.html "Joomla! 3.7.5 - LDAP注入20秒破解密码")

[【安全通报】Apache ActiveMQ远...](/home/detail/4567.html "【安全通报】Apache ActiveMQ远程代码执行漏洞（CVE-2020-13920）")

[【漏洞预警】Metinfo 5.3.5- 5.3...](/home/detail/1559.html "【漏洞预警】Metinfo 5.3.5- 5.3.13 SSRF漏洞[0day]")

[【高危漏洞预警】Wordpress Core...](/home/detail/1498.html "【高危漏洞预警】Wordpress Core 远程代码执行0day（无需验证和插件）")

[【漏洞预警】泛微E-cology OA远...](/home/detail/2980.html "【漏洞预警】泛微E-cology OA远程命令执行漏洞")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)