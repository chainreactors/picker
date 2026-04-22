---
title: 红队效率神器｜一键提取、加载、分析JS，攻防 SRC双丰收
url: https://mp.weixin.qq.com/s/LOI9vTOQp4rUlwsoRo4vkQ
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:40:27.753141
---

# 红队效率神器｜一键提取、加载、分析JS，攻防 SRC双丰收

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gL9yql6ibrhKIYRW5ZlMeSx7ovgwkpW1BAUPMqFAx7XCM41XsYic17NdD6dgYE5jpnN6E7yQoib5qOvppzj7jrJPdjVaLib4MMrXYauZqzUdjQ0/0?wx_fmt=jpeg)

# 红队效率神器｜一键提取、加载、分析JS，攻防 SRC双丰收

xz-zone
xz-zone

鹏组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0YvAy5BgkyNJe4vC6qtyDX3vcGgiameZcOwiaYlDgwuutJUicHD1ZWicn2T6WTuuiaLvsAcnHBq2a4f6LkwqGtGOuxw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

为红队信息收集打造的**Chrome 插件 ，一键搞定 Webpack JS 文件提取、自动加载、深度分析，攻防演练、SRC 挖掘高频出货工具**

**![one](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhJe2STnNZxhibkJowWcgdnnUNzNbMlb8N7cVrq5yuiaH5GZG6XiajTL7B0m3Syfk5AiculUGOEJzDRV9ibTYCicqxg5Jr9jmb7mt7iaZU/640?wx_fmt=png&from=appmsg)**

## 工具定位

**Webpack\_extract**是JS 自动化工具，核心服务红队人员，解决 Webpack 站点 JS 文件难以提取、分析繁琐的痛点，实现**信息收集 - 加载 - 分析**全流程自动化，Chrome 环境无缝适配，已在实战中验证高效性。

## 核心功能

1. **一键提取映射**

   自动识别 Webpack 加密 / 打包 JS，快速抓取映射关系，直接获取目标 JS 文件，告别手动查找拆解。
2. ![one](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhKibicrMVLENqImbUKOhdD143v0VQch8KtscBP3O1hOfJiaRpQ5W66oYtO1vkpQ0S2HDj7Deh9SHhLicudMDTyySXX9dHDHhj5z0icg/640?wx_fmt=png&from=appmsg)
3. **一键自动加载**

   提取的 JS 文件自动加载到浏览器 Sources 目录，无需手动导入，调试分析一步到位。
4. ![three](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhJc3JxShZCL4Re7DH14qUSPefiaYraxTagLDM4MzDZnq2uiazAqYrbOrNUvQzCBARZiaz5SCNabOT8uQnlrVO7f5LgYiaJfkibXjoZg/640?wx_fmt=png&from=appmsg)
5. **![six](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhL2iacKVgfrL8Hk8B1DvM2o5R1noUH9QjYWUX1fibkUI1axoFRgp3MFHHoxoQ9DYtoFYNm45SRAsP4QmAk2TawKsR6c1rzribvjQw/640?wx_fmt=png&from=appmsg)**
6. **一键深度分析**

   内置规则引擎，自动扫描 JS 中的敏感信息、接口、密钥等，结合 HaE 规则能力，挖掘效率拉满。
7. **一键下载 / 复制**

   支持批量下载提取的 JS 文件、一键复制映射内容，本地留存分析更便捷。
8. ![two](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhINqA2b48dDffz8qib90xkjNUIMibhiaFa8DwslfF21IzbjM7kYNvvzgOqzAlpj9VO081vyfWjTYYp0zAKRojlOK4zialQEAbpazaU/640?wx_fmt=png&from=appmsg)
9. **规则自定义**

   支持外部导入规则、YAML 转 JS 规则，可灵活适配不同站点分析需求。

## 超简安装步骤

1. 打开 Chrome，进入`chrome://extensions/`
2. 开启右上角**开发者模式**
3. 点击「加载已解压的扩展程序」，选择工具文件夹
4. 安装完成，工具栏直接使用，无复杂配置

## 版本迭代亮点

* 2025-09-01：初始版本上线，核心提取功能落地
* 2025-09-17：解决 CORS 跨域、HTTPS 信任问题，兼容性拉满
* 2025-09-25：新增一键分析，敏感信息自动抓取
* 2025-11-17：新增一键下载，文件留存更方便
* 2026-01-15：支持外部导入规则，自定义能力升级
* 2026-02-15：Sources 可视化加载，优化打包体验

##

## 则转换教程

工具支持 HaE 规则快速转换，两步搞定：

1. 安装依赖：

   ```
   npm init -y && npm install js-yaml fs
   ```
2. 运行转换脚本：node transformation.js

自动将`config.yml`转为工具可用的`Rules.js`，无缝复用现有规则。

项目地址：https://github.com/xz-zone/Webpack\_extract

[鹏组安全社区站：您身边的安全专家-情报 | 攻防 | 渗透 | 线索 | 资源社区](https://mp.weixin.qq.com/s?__biz=Mzg5NDU3NDA3OQ==&mid=2247491205&idx=1&sn=b212739965f6617c84c89726cc85d50c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyNHF1CWPJ9XSApBFhIGwF5Jh0zD2ySOcHvBkYgicU4xZsqvR3XEjUEnfGKH7ya8TgqCibHpYZKcibDBQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=28)

**扫码关注**

**社区**

鹏组安全社区：comm.pgpsec.cn

专注网络技术与骇客的一个综合性技术性交流与资源分享社区

老用户续费88折扣![图片](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhJYheZibR4K46iaORkE4DSb9UVzOuiazEGW7GHfDs758OywY6I8mWcTv7KI9ouEwCmSURf4DKb3lwXM0jZqSnK8w90gSibfZdElibibM/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

社区首页

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyN92OtiagxgUpDAeq8RbcPacH8L82CwLzHtvucDrP1RrgfzeUYY8cS4WHk8niap3jKZzys9wK5oHB9w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=29)

免责声明

由于传播、利用本公众号鹏组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号鹏组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

好文分享收藏赞一下最美点在看哦

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyMD7I0zCGRx4cPrP4o4wlMpgZicY0R4ENahs8NIk1GkREYoIic48qMVebUnzHcaBL0Gzib4mvE9VsibFQ/0?wx_fmt=png)

鹏组安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyMD7I0zCGRx4cPrP4o4wlMpgZicY0R4ENahs8NIk1GkREYoIic48qMVebUnzHcaBL0Gzib4mvE9VsibFQ/0?wx_fmt=png)

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