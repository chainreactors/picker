---
title: 国家网络与信息安全信息通报中心通报：主流JavaScript软件包管理平台npm遭供应链投毒攻击
url: https://mp.weixin.qq.com/s/3oLiraDdslkN7r-zqaSgZQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:11.261389
---

# 国家网络与信息安全信息通报中心通报：主流JavaScript软件包管理平台npm遭供应链投毒攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pCMriaDGbE4u0tCameGwDxY1ml0IqYxRwwYIR3meAd5BnPBTbPHVawzSzFy3bCQzWbfo9tibce89XW0LvY0lyMTGz145dQYibpXiaoWg8IzooAY/0?wx_fmt=jpeg)

# 国家网络与信息安全信息通报中心通报：主流JavaScript软件包管理平台npm遭供应链投毒攻击

公安部网安局

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

国家网络与信息安全信息通报中心监测发现，全球主流JavaScript软件包管理平台npm遭“沙虫”（Shai-Hulud）供应链投毒攻击。攻击者攻陷了npm官方维护者账户，并在短时间内批量投放大量恶意软件包，涉及300余个独立程序包的600余个恶意版本，影响多个热门开源项目。当开发者安装恶意依赖包后，程序会自动在本地主机、CI/CD流水线环境执行恶意代码，窃取GitHub Token、npm Token、云服务密钥、SSH私钥、Kubernetes凭据、数据库连接字符串等敏感信息。此次投毒攻击具备极强蠕虫式自我复制与横向传播能力，攻击者可利用窃取的npm发布权限篡改和二次发布开发者名下的其他软件包，造成供应链风险持续扩散、危害持续升级。

一、影响范围

主要受影响项目包括echarts-for-react、@antv系列核心库（@antv/g2、@antv/g6、@antv/x6等）、TanStack系列42个包、Mistral AI相关PyPI包以及timeago.js等社区包。受影响对象主要包括前端开发者、人工智能或机器学习开发者、开源项目维护者及企业研发人员等。由于恶意软件具备蠕虫式传播能力，可自动重新发布受害者维护的其他包，导致共享开发环境的其他用户及依赖同一维护者发布的其他软件包的用户也可能面临间接感染风险。

二、处置建议

一是隔离风险设备。若本地设备近期安装过相关受影响的npm依赖，建议暂停项目运行，并断开可疑设备网络连接，防止恶意代码继续外联。二是排查依赖文件。检查package.json、package-lock.json、pnpm-lock.yaml、yarn.lock及node\_modules目录，核实是否存在异常preinstall、postinstall等自动执行脚本。三是清理残留痕迹。排查Claude Code hooks、VS Code任务配置等位置，检查是否存在router\_runtime.js、setup.mjs等可疑文件，避免恶意代码在卸载依赖后继续残留。四是更换敏感凭证。及时更新GitHub Token、npm Token、云服务密钥、SSH私钥、数据库密码等各类密钥与令牌，对关联账号执行“退出全部设备”操作。五是提升安全意识。安装npm第三方依赖前，应核验项目官方来源、近期发布记录和脚本内容，不盲目安装热门包，优先选用安全稳定的官方版本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/E1iauzlb2BTn7wvyIQ71iaKIJr6icdmdiarF3K2hcQI9JGE5iaFgXHK59ogKDLEJPYJ30TqbT6w8dJGoJ1rtkia7Uaiag/0?wx_fmt=png)

公安部网安局

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/E1iauzlb2BTn7wvyIQ71iaKIJr6icdmdiarF3K2hcQI9JGE5iaFgXHK59ogKDLEJPYJ30TqbT6w8dJGoJ1rtkia7Uaiag/0?wx_fmt=png)

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