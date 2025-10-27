---
title: Linux服务器常用脚本工具包
url: https://blog.upx8.com/3095
source: 黑海洋 - WIKI
date: 2022-11-19
fetch_date: 2025-10-03T23:13:43.287541
---

# Linux服务器常用脚本工具包

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux服务器常用脚本工具包

发布时间:
2022-11-18

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
24247

# jcnf 常用脚本工具包

玩机，是不是有很多命令或者脚本记不住，因此我整理了一些我个人常用的脚本。

---

# 使用说明

安装依赖（新机器必须运行一次，此后无需运行）

```
yum install -y curl wget 2> /dev/null || apt install -y curl wget
```

安装并运行脚本

```
wget -O jcnfbox.sh https://raw.githubusercontent.com/Netflixxp/jcnf-box/main/jcnfbox.sh && chmod +x jcnfbox.sh && clear && ./jcnfbox.sh
```

英文版，机器翻译English version

```
wget -O jcnfbox-en.sh https://raw.githubusercontent.com/Netflixxp/jcnf-box/main/jcnfbox-en.sh && chmod +x jcnfbox-en.sh && clear && ./jcnfbox-en.sh
```

---

# 功能说明

1. 服务器检查：
   * Lemonbench 综合测试
   * 三网Speedtest测速
   * 内存压力测试
   * 回程路由追踪
   * Speedtest测速
   * 获取本机IP
   * 流媒体解锁测试
   * 检测/诊断Youtube地域
2. 服务器功能
   * Linux换源脚本
   * ipv4/6优先级调整
   * 虚拟内存SWAP一键安装
   * 一键安装BBR
   * 系统网络配置优化
   * 宝塔中文官方一键安装
   * 宝塔英文官方一键安装（无需验证）
   * 宝塔破解纯净版
   * Cloudflare WARP 一键配置脚本（2021年7月3日添加）
3. 科学上网工具
   * iptables一键中转
   * gost一键中转
   * MTP&TLS 一键脚本
   * xray一键安装8合一脚本
   * v2-ui一键安装
   * wulabing一键xray脚本
   * Ehcoo隧道中转(2021年7月3日添加)

[![功能列表](https://camo.githubusercontent.com/25f7dbeb0b2bbfbd36326aad07a1f44cfaa6ad646d6a5f1fd5f88960fa7fb5ac/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f4e6574666c697878702f6a636e662d626f782f696d672f736d2e6a7067)](https://blog.upx8.com/go/aHR0cHM6Ly9jYW1vLmdpdGh1YnVzZXJjb250ZW50LmNvbS8yNWY3ZGJlYjBiMmJiZmJkMzYzMjZhYWQwN2ExZjQ0Y2ZhYTZhZDY0NmQ2YTVmMWZkNWY4ODk2MGZhN2ZiNWFjLzY4NzQ3NDcwNzMzYTJmMmY2MzY0NmUyZTZhNzM2NDY1NmM2OTc2NzIyZTZlNjU3NDJmNjc2ODJmNGU2NTc0NjY2YzY5Nzg3ODcwMmY2YTYzNmU2NjJkNjI2Zjc4MmY2OTZkNjcyZjczNmQyZTZhNzA2Nw)

1. **[Ubuntu和Debian 初始化](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudXB4OC5jb20vMzEyMA)**

   2024-08-17 23:35:00

   [回复](https://blog.upx8.com/3095/comment-page-1?replyTo=30072#respond-post-3095)

   [...]rm -rf /etc/iptables && rebootLinux常用脚本（测速.bbr等）wget -O jcnfbox.sh https://raw.githubusercontent.com/Netflixxp/jcnf-box/main/jcnfbox.sh && chmod +x jcnfbox.sh && clear &&am[...]
2. **[Ubuntu和Debian 初始化](https://blog.upx8.com/3120)**

   2024-06-06 13:59:13

   [回复](https://blog.upx8.com/3095/comment-page-1?replyTo=29704#respond-post-3095)

   [...]rm -rf /etc/iptables && rebootLinux常用脚本（测速.bbr等）wget -O jcnfbox.sh https://raw.githubusercontent.com/Netflixxp/jcnf-box/main/jcnfbox.sh && chmod +x jcnfbox.sh && clear &&am[...]

[取消回复](https://blog.upx8.com/3095#respond-post-3095)

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