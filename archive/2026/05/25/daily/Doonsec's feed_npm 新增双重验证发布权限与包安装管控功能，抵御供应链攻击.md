---
title: npm 新增双重验证发布权限与包安装管控功能，抵御供应链攻击
url: https://mp.weixin.qq.com/s/_CwEWJB9CrQOeviN200uRg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:07:35.817079
---

# npm 新增双重验证发布权限与包安装管控功能，抵御供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DYqn7TU9icq0cHkcnMglh0zu0BNvr6VTLjBlu7X5Ndj5gTUfVFhqqU664YHwnibh1I4tcVP7rhqqJxxBtoD5ZzgGI8f3KgQwNf9KuzAFYUnRQ/0?wx_fmt=jpeg)

# npm 新增双重验证发布权限与包安装管控功能，抵御供应链攻击

鹏鹏同学
鹏鹏同学

黑猫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

GitHub 为 npm 上线多项全新管控功能，加固软件供应链安全，包维护者可在安装包对外开放前手动审核放行。

该功能名为**分阶段发布**，目前已正式全面启用。规则要求维护者完成双重身份验证，才可将软件包推送至 npm 官网。

GitHub 介绍：软件包不再一键直接发布、即刻可供下载，打包文件会先存入待发布队列，必须经维护者手动审批后，才能对外安装使用。

隶属于微软的 GitHub 表示，此次更新能核验每一次发布均为真人操作，即便非交互式 CI/CD 流程、依托 OIDC 协议的可信发布操作也全部纳入验证范围。

启用分阶段发布需满足以下条件：

1. 具备对应软件包的发布权限
2. 软件包已托管在 npm 仓库，全新包暂不支持该功能
3. 账号已开启双重验证

开发者可在包根目录执行`npm stage publish`命令提交至待审核区，使用该指令需将 npm 命令行升级至 11.15.0 及以上版本。官方建议搭配 OIDC 可信发布模式，防护效果更佳。

npm 同步新增三项安装来源限制参数，与原有`--allow-git`参数配合使用：

* `--allow-file`

  ：管控本地文件与压缩包安装
* `--allow-remote`

  ：管控网络地址资源安装
* `--allow-directory`

  ：管控本地目录安装

开发者可凭借这些参数，对所有非官方仓库的安装来源统一设置白名单权限。

近期针对开源生态的供应链攻击频发，黑客组织 TeamPCP 通过持续入侵篡改海量热门开源包，此次安全升级以此为背景推出。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

黑猫安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过