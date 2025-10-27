---
title: 自动从Telegram频道下载CSV文件并提取443端口IP地址
url: https://blog.upx8.com/4887
source: 黑海洋 - Wiki
date: 2025-10-26
fetch_date: 2025-10-27T16:50:38.750823
---

# 自动从Telegram频道下载CSV文件并提取443端口IP地址

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 自动从Telegram频道下载CSV文件并提取443端口IP地址

发布时间:
2025-10-26

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
5464

# 前言

优选IP库太难找了，好不容易在Telegram频道找到了一个优选ip推送频道。现做个工作流自动从Telegram频道下载CSV文件并提取443端口IP地址。然后再用这个IP库来优选。

**项目地址：** [https://github.com/whggo/new\_cfip](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3doZ2dvL25ld19jZmlw)

---

### 效果演示：

github Actinos自动运行
[![](https://pic.510777.xyz/img/ScreenShot_2025-10-14_200249_951.jpg)](https://pic.510777.xyz/img/ScreenShot_2025-10-14_200249_951.jpg)

运行完成后输出ip.txt到仓库
[![](https://pic.510777.xyz/img/ScreenShot_2025-10-14_200416_823.jpg)](https://pic.510777.xyz/img/ScreenShot_2025-10-14_200416_823.jpg)

---

## 详细使用步骤

### 第一步：本地设置

1. 在本地创建新仓库或使用现有仓库
2. 将上述所有文件放入仓库
3. 运行 `pip install -r requirements.txt`

### 第二步：首次登录

1. 运行 `python setup_telegram.py`
2. 输入你的Telegram API信息（从 [https://my.telegram.org](https://blog.upx8.com/go/aHR0cHM6Ly9teS50ZWxlZ3JhbS5vcmcv) 获取）
3. 输入手机号
4. 输入收到的验证码
5. 成功后会生成 `telegram_session.session` 文件

### 第三步：配置GitHub

1. 将整个项目推送到GitHub
2. 在仓库设置 → Secrets and variables → Actions 中添加：
   * `TELEGRAM_API_ID`
   * `TELEGRAM_API_HASH`
   * `TELEGRAM_PHONE`

### 第四步：验证运行

1. 在GitHub Actions页面手动触发工作流
2. 检查是否成功运行并生成 `ip.txt` 文件

这样配置后，脚本就会每天自动运行，无需人工干预！

1. ![tg@jiemo123](https://gravatar.loli.net/avatar/avatar/f411333bb368ceaf818f5508ff52d8f8?s=32&r=&d=)

   **tg@jiemo123**

   2025-10-26 12:50:06

   [回复](https://blog.upx8.com/4887/comment-page-1?replyTo=30720#respond-post-4887)

   有个更好的办法。抓网络测速的站的ws包（如：itdog等），发包，js解密，拿到延迟数据筛选整理，定时自动就好；相当于是白嫖服务器检测点

[取消回复](https://blog.upx8.com/4887#respond-post-4887)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")