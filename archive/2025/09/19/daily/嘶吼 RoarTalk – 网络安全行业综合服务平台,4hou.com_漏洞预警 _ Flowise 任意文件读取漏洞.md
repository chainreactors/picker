---
title: 漏洞预警 | Flowise 任意文件读取漏洞
url: https://www.4hou.com/posts/qo13
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-19
fetch_date: 2025-10-02T20:21:21.546589
---

# 漏洞预警 | Flowise 任意文件读取漏洞

漏洞预警 | Flowise 任意文件读取漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 漏洞预警 | Flowise 任意文件读取漏洞

盛邦安全
[行业](https://www.4hou.com/category/industry)
2025-09-18 15:57:27

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)23237

收藏

导语：漏洞预警 | Flowise 任意文件读取漏洞

## 一、漏洞概述

![QQ20250918-140250.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250918/1758175834214089.png "1758175834214089.png")

近日，Flowise 发布更新修复高风险漏洞，攻击者可以利用该漏洞读取服务器上任意文件。建议您及时开展安全风险自查。

Flowise 是一个开源的、可视化的 LLM 应用构建平台，专为 LangChain.js 打造，支持通过拖拽组件的方式快速构建聊天机器人、问答系统、嵌入式 AI 服务等。它极大降低了构建 LLM 应用的门槛，适合开发者、数据科学家以及产品团队进行原型设计与部署。

据描述，Flowise 存在一个严重的任意文件读取漏洞，攻击者可通过未授权访问以下两个 API 接口：

```
/api/v1/get-upload-file
/api/v1/openai-assistants-file/download
```

攻击者可构造恶意 chatId 参数（如 ../../）绕过路径校验机制，读取服务器本地任意文件。默认部署情况下，可直接读取。/root/.flowise/database.sqlite —— 包含所有数据库内容，包括 API 密钥、用户数据等敏感信息。该漏洞利用了 fallback 路径逻辑，在文件未找到时会尝试去除 orgId 并重新拼接路径，从而绕过原有的目录限制校验。

漏洞影响的产品和版本：

Flowise <= 3.0.5

## 二、资产测绘

据daydaymap数据显示互联网存在5,587个资产，风险资产分布情况如下。

![QQ20250918-140428.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250918/1758175870132147.png "1758175870132147.png")

## 三、漏洞复现

![QQ20250918-140503.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250918/1758175877438421.png "1758175877438421.png")

## 四、解决方案

▪ 临时缓解方案

限制公网访问相关 API 接口，建议通过防火墙或网关进行访问控制。

审计历史访问日志，排查是否存在异常文件读取行为。

更换 API 密钥，如怀疑数据库已被读取。

启用 Web 应用防火墙（WAF），拦截路径穿越类请求

▪ 升级修复

立即升级 Flowise 至 v3.0.6 或以上版本

## 五、参考链接

```
https://github.com/advisories/GHSA-99pg-hqvx-r4gf https://www.ddpoc.com/DVB-2025-10219.htm
```

[原文链接](https://mp.weixin.qq.com/s/XDNkP4uvmBzuh19S0-bKBg)

## 本文来源于：Beacon Tower Lab（烽火台实验室）公众号，作者：烽火台实验室

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?P1JUHzhj)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)