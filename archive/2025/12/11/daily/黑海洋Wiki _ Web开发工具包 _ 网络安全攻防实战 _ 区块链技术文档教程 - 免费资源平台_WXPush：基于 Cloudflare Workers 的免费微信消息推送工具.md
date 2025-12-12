---
title: WXPush：基于 Cloudflare Workers 的免费微信消息推送工具
url: https://blog.upx8.com/4924
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-11
fetch_date: 2025-12-12T03:21:23.289227
---

# WXPush：基于 Cloudflare Workers 的免费微信消息推送工具

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# WXPush：基于 Cloudflare Workers 的免费微信消息推送工具

发布时间:
2025-12-11

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
4099

## 免费高效的微信消息推送解决方案：WXPush

**WXPush** 是一个轻量级的微信消息推送服务，依托 Cloudflare Workers 构建，无需服务器即可运行，完全免费，每日支持 10 万次推送额度，适合个人用户、独立开发者及小型项目使用。服务通过 API 接口直接向指定微信用户发送模板消息，带来原生微信弹窗通知与声音提醒体验，是构建自动化提醒系统、信息同步服务的理想选择。

![WXPush：基于 Cloudflare Workers 的免费微信消息推送工具](https://cdn.skyimg.net/up/2025/12/11/a0a9e6f6.webp)

---

## 功能亮点

* **永久免费使用**：每天高达 100,000 次推送调用，无需担心费用问题
* **真正的微信原生体验**：支持弹窗提醒 + 微信声音提示
* **多用户支持**：可配置多个用户同时接收推送
* **极简部署**：复制代码即用，快速上线
* **跳转稳定、换肤灵活**：支持跳转链接和皮肤更换，满足多样化需求

## 谁适合使用 WXPush？

* 希望构建自用消息提醒系统的开发者
* 想通过 API 接口向微信发送信息的个人站长
* 追求极简部署与免费使用的自动化爱好者
* 无服务器开发范式的拥护者（Serverless）

---

## 快速部署指南

### 方法一：直接部署到 Cloudflare Workers

无需本地环境，只需：

1. 登录 Cloudflare 仪表盘
2. 创建 Worker 服务
3. 粘贴并保存 `src/index.js` 代码
4. 设置环境变量：
   * `API_TOKEN`：自定义访问令牌
   * `WX_APPID` / `WX_SECRET`：公众号凭据
   * `WX_USERID`：多个用户用 `|` 分隔
   * `WX_TEMPLATE_ID`：微信模板 ID
   * `WX_BASE_URL`（可选）：跳转链接
5. 一键部署上线

所有敏感配置都可加密存储，确保安全性。

### 方法二：通过 GitHub 自动部署

适用于希望通过 Git 版本控制和 CI/CD 的用户：

* Fork 本项目到 GitHub 仓库
* 在 Cloudflare Pages 中连接仓库
* 配置部署参数与环境变量
* 自动构建和部署，更新即上线

---

## 教学视频

视频教程：<https://www.youtube.com/watch?v=sE1Kcol_XRs>

## 开源地址

项目 GitHub 地址：🔗 <https://github.com/frankiejun/wxpush>

[取消回复](https://blog.upx8.com/4924#respond-post-4924)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2025 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")