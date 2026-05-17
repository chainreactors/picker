---
title: 红队神器｜Vue 站点未授权漏洞一键挖掘 -v2.0
url: https://mp.weixin.qq.com/s/8gGSgPpLkQ1xtlXvINSzDw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:13.967567
---

# 红队神器｜Vue 站点未授权漏洞一键挖掘 -v2.0

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5yYXmGfnscRicD4Jhso3PNPBKu6ynDDehfKWicibEPgEaHHcd6Qc3JwSjjIC2H15mRgkTBfa5R3a1G9ORg6UV8uo4ENjwH6QcFsnict8bTN2Hv4/0?wx_fmt=jpeg)

# 红队神器｜Vue 站点未授权漏洞一键挖掘 -v2.0

Ad1euDa1e
Ad1euDa1e

乌雲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

介绍

这是一个专为红队人员开发的浏览器插件，用于分析Vue网站的路由结构，并绕过路由守卫，从而发现站点的隐藏资产与未授权访问漏洞。

**本工具已多次在攻防、SRC挖掘场景中出货。**

## V2.0更新

* 新增“梭哈”模式（All-in）：支持按站点开启，刷新页面后自动生效。主要通过在Vue Router初始化之前前置注入，从而实现浏览器的跳转拦截与路由拦截
* UI 稳定性优化：优化了弹窗交互与列表渲染，解决跳转时的UI抖动与状态丢失问题
* 路由结果更稳：优化缓存、基础路径识别与当前路由记忆逻辑，便于连续测试与结果复盘
* 复杂页面兼容性提升：针对延迟加载、动态挂载、多次渲染等场景增强检测与接管流程

## 核心功能

* 自动检测Vue框架：快速识别目标站点是否使用Vue.js
* 路由接管与验证辅助：自动处理常见路由守卫与前端鉴权元信息
* “梭哈”模式：面向复杂 SPA 场景提供前置增强注入，提高分析成功率与稳定性
* 路由结构分析：提取所有路由路径，包括延迟挂载、动态加载后暴露的路由信息
* 批量操作：支持一键复制和访问所有发现的路由
* 更稳定的结果展示：支持缓存恢复、基础路径识别、当前路由高亮与 URL 切换展示

## 使用方法

1. 在 Chrome 或基于 Chromium 的浏览器中安装此扩展
2. 访问基于Vue的测试目标网站
3. 点击扩展图标，工具将显示当前识别到的路由与可生成的 URL
4. 根据测试需求查看、复制或打开对应路由，验证前端路由与访问控制实现
5. 如普通模式下无法绕过，可开启 **“梭哈”模式** 并刷新页面后重新测试

项目地址

https://github.com/Ad1euDa1e/VueCrack

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bMyibjv83iavx2yyhJibAziblI8R81ZMyNFzQ4wrvUIE2Ks14R3ZfGmjEwNXbCzXm5Qcwkcuxsm8pn2ibIISmRoxPLA/0?wx_fmt=png)

乌雲安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bMyibjv83iavx2yyhJibAziblI8R81ZMyNFzQ4wrvUIE2Ks14R3ZfGmjEwNXbCzXm5Qcwkcuxsm8pn2ibIISmRoxPLA/0?wx_fmt=png)

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