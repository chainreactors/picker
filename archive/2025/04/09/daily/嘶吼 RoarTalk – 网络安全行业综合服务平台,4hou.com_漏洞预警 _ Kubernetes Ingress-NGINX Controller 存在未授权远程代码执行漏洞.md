---
title: 漏洞预警 | Kubernetes Ingress-NGINX Controller 存在未授权远程代码执行漏洞
url: https://www.4hou.com/posts/9jmD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-09
fetch_date: 2025-10-06T22:04:28.018094
---

# 漏洞预警 | Kubernetes Ingress-NGINX Controller 存在未授权远程代码执行漏洞

漏洞预警 | Kubernetes Ingress-NGINX Controller 存在未授权远程代码执行漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 漏洞预警 | Kubernetes Ingress-NGINX Controller 存在未授权远程代码执行漏洞

盛邦安全
[行业](https://www.4hou.com/category/industry)
2025-04-08 17:26:16

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)47748

收藏

导语：Ingress-Nginx 是 Kubernetes 生态中基于 Nginx 实现的 ‌Ingress 控制器‌‌，用于管理集群外部的 HTTP(S) 和 WebSocket 流量路由‌。

**漏洞概述**

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744104342181629.png "1744104342181629.png")

近日，Ingress-Nginx 项目的维护者们发布了一批关键漏洞的修复补丁，其中包含了高风险漏洞（CVE-2025-29927），攻击者可以利用该漏洞轻易接管你的 Kubernetes 集群。目前有 40% 以上的 Kubernetes 管理员正在使用 ingress-nginx，建议您及时开展安全风险自查。

Ingress-Nginx 是 Kubernetes 生态中基于 Nginx 实现的 ‌Ingress 控制器‌‌，用于管理集群外部的 HTTP(S) 和 WebSocket 流量路由‌。其核心作用是通过定义路由规则，将外部请求按域名、路径等策略转发至集群内部服务，并提供负载均衡、SSL 终止、限流等高级功能‌。

据描述，Ingress-Nginx 在 v1.11.5、v1.12.1 之前的版本中存在一个安全漏洞。攻击者向同一 Pod 内的 NGINX 服务器发送一个长缓冲请求。NGINX 会将该请求缓存为一个临时文件，然后攻击者发送第二个请求至准入验证 Webhook 服务器（Admission Validating Webhook Server）。该 Webhook 会触发 NGINX 生成一个包含恶意配置指令 ssl\_engine badso\_location;准入 Webhook 会执行 nginx -t 命令来验证配置文件的合法性。由于 NGINX 在加载配置时会直接解析并执行特定指令，攻击者可通过恶意指令在 NGINX 服务器的上下文中触发远程代码执行（RCE），从而完全控制服务器。

漏洞影响的产品和版本：

< v1.11.0

v1.11.0 - 1.11.4

v1.12.0

**漏洞复现**

![QQ20250407-155202.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744104343165789.png "1744013388503008.png")

**资产测绘**

据daydaymap数据显示互联网存在15102个资产，国内风险资产分布情况如下：

![QQ20250407-155210.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744104344998872.png "1744013383946388.png")

**解决方案**

**临时缓解方案：**

启用mTLS认证准入控制器；

定期审计Ingress注解使用情况；

实施Pod安全策略限制挂载敏感目录。

**升级修复：**

目前官方已发布修复安全补丁

```
kubectl set image deployment/ingress-nginx-controller \controller=k8s.gcr.io/ingress-nginx/controller:v1.12.1
```

**参考链接**

```
https://github.com/kubernetes/kubernetes/issues/131009
https://www.ddpoc.com/DVB-2023-9016.html
```

[原文链接](https://mp.weixin.qq.com/s/rgzQi4BvnMcejVNmowLORA)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?k0Xm5Qew)

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