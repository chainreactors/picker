---
title: AI Captcha Solver：AI大模型自动识别验证码（Chrome扩展）
url: https://blog.upx8.com/4932
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-29
fetch_date: 2025-12-30T03:25:55.062275
---

# AI Captcha Solver：AI大模型自动识别验证码（Chrome扩展）

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# AI Captcha Solver：AI大模型自动识别验证码（Chrome扩展）

发布时间:
2025-12-29 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
2539

AI Captcha Solver 是一款基于大语言模型的浏览器插件，专为开发者、数据工作者及自动化爱好者打造。它支持多种主流AI模型，如 OpenAI、Claude、Google Gemini 等，自动识别网页中的图像类验证码，并完成智能填充。整个过程本地运行，保障安全与隐私。

![AI Captcha Solver：AI大模型自动识别验证码（Chrome扩展）](https://img.7761.cf/img/20251229/1342681033.png)

### 支持多模型与自定义API配置

插件内置对多个主流AI服务的支持，包括：

* OpenAI：如 gpt-4o
* Claude：如 claude-3-5-sonnet
* Google Gemini：如 gemini-1.5-flash

用户也可自由添加自定义API，兼容各类AI模型，满足不同场景需求。

### 智能验证码识别机制

* 识别图像类型验证码（img/canvas/svg）
* 支持手动元素选择，类似 DevTools 拾取器
* 自动保存验证码位置，下次自动应用
* 成功识别后自动填充到对应输入框
* 模拟用户行为，适配各类防爬机制

### 数据安全与隐私保障

* API密钥通过 Web Crypto API 使用 AES-GCM 加密保存
* 所有识别请求均在本地发起
* 插件仅在用户手动操作时启动，不主动运行

### 使用与配置简洁直观

插件以源码方式安装，支持 Chrome 开发者模式加载。设置中可快速配置API密钥，选择模板或添加自定义接口。

下载地址:[网盘](https://pan.quark.cn/s/29cdfedd5d3d "AI Captcha Solver：AI验证码自动识别扩展")

1. git clone 此项目
2. 打开Chrome浏览器，访问 `chrome://extensions/`
3. 开启右上角的「开发者模式」
4. 点击「加载已解压的扩展程序」
5. 选择 `auto_captcha` 文件夹

#### 常见使用流程：

1. 启动“选择元素”模式，点击页面验证码
2. 运行“识别验证码”，由AI识别图像
3. 点击“填充”，自动完成验证码输入

保存的验证码规则将在下次访问同站点时自动复用，大幅提高效率。

### 已知限制说明

* 跨域图片需目标网站开放CORS
* 暂不支持滑动验证码与点选验证码

## 项目地址与开源链接

下载地址：[网盘](https://wwbfo.lanzouq.com/iqCIS3esb1jc "AI Captcha Solver：AI验证码自动识别扩展")

开源项目地址：[GitHub – auto\_captcha](https://github.com/dxxzst/auto_captcha "GitHub - auto_captcha")

1. ![koi](//q2.qlogo.cn/headimg_dl?dst_uin=695154&spec=100)

   **koi**

   2025-12-29 18:05:45

   [回复](https://blog.upx8.com/4932/comment-page-1?replyTo=30737#respond-post-4932)

   Google Gemini 的gemini-1.5-flash模型 是错误的，要写gemini-2.5-flash才行

[取消回复](https://blog.upx8.com/4932#respond-post-4932)

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