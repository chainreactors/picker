---
title: 【漏洞预警】Smartbi 未授权任意代码执行漏洞
url: https://nosec.org/home/detail/5070.html
source: NOSEC 安全讯息平台 - 漏洞预警
date: 2023-03-02
fetch_date: 2025-10-04T08:23:59.887378
---

# 【漏洞预警】Smartbi 未授权任意代码执行漏洞

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

# 【漏洞预警】Smartbi 未授权任意代码执行漏洞

![](https://nosec.org/home/image/headImg.png)xiannv  947天前

![0.png](/avatar/uploads/attach/image/5e6a8cb645bbca5031ac123f6fbf34e6/0.png)

# 一、    漏洞概述

Smartbi大数据分析产品融合BI定义的所有阶段，对接各种业务数据库、数据仓库和大数据分析平台，进行加工处理、分析挖掘和可视化展现；满足所有用户的各种数据分析应用需求，如大数据分析、可视化分析、探索式分析、复杂报表、应用分享等等。

近日， Smartbi官方发布安全更新，其中包含Smartbi 远程命令执行漏洞。Smartbi大数据分析平台存在远程命令执行漏洞，未经身份认证的远程攻击者利用此漏洞向系统发送恶意数据，可能执行任意命令，导致系统被攻击与控制。

# 二、    影响范围

本次漏洞影响范围如下：

| V7 <= Smartbi <= V10.5.8 |
| --- |

FOFA Query：

| app="SMARTBI" |
| --- |

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（app="SMARTBI"）共有248 个相关服务对外开放。中国使用数量最多，共有 247 个；新加坡第二，共有1 个。

![1.png](/avatar/uploads/attach/image/22afa78ea1bfeae747a5f3d5e118d69c/1.png)

全球范围内分布情况如下（仅为分布情况，非漏洞影响情况）：

中国大陆地区北京使用数量最多，共有73 个；贵州第二，共有 33 个；广东第三，共有 20 个；上海第四，共有 9 个；湖北第五，共有 4 个。

![2.png](/avatar/uploads/attach/image/aa74452337692475c017b927327cbc54/2.png)

# 三、    漏洞复现

白帽汇安全研究院于第一时间复现了该漏洞：

![3.png](/avatar/uploads/attach/image/c58d85d3cf7a24ef192e7f262ea1cdee/3.png)

# 四、    修复建议

## （一）官方补丁

Smartbi官方已发布安全版本修复该漏洞，建议受影响用户尽快进行安全更新

自动升级：

登录后台->右上角系统监控->系统补丁->安装补丁->在线更新

手动升级：

下载补丁->登录后台->右上角系统监控->系统补丁->安装补丁->手动更新

补丁下载地址：<https://www.smartbi.com.cn/patchinfo>

# 五、    参考链接

[1.] <https://www.smartbi.com.cn/patchinfo>

[2.] <https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=50692623>

[上一篇：
如何快速发现诈骗类钓鱼网站](/home/detail/5068.html)
[下一篇：
FOFA模糊搜索的正确姿势](/home/detail/5071.html)

浏览: 29921
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

[【漏洞通报】GitLab CE/EE 远程...](/home/detail/5034.html "【漏洞通报】GitLab CE/EE 远程命令执行漏洞（CVE-2022-2992）")

[【漏洞预警】GPON光纤路由器越权...](/home/detail/1610.html "【漏洞预警】GPON光纤路由器越权和远程命令执行漏洞（CVE-2018-10561 & CVE-2018-10562）")

[【漏洞预警】Samba远程代码执行...](/home/detail/1502.html "【漏洞预警】Samba远程代码执行漏洞")

[【安全通报】SaltStack远程命令...](/home/detail/4452.html "【安全通报】SaltStack远程命令执行漏洞（CVE-2020-11651、CVE-2020-11652）")

[Adobe ColdFusion 任意文件读取...](/home/detail/4353.html "Adobe ColdFusion 任意文件读取和任意文件包含漏洞")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)