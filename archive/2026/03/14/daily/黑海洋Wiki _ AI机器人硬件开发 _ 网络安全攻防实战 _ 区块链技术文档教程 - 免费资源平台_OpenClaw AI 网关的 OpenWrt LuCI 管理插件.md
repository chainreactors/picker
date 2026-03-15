---
title: OpenClaw AI 网关的 OpenWrt LuCI 管理插件
url: https://blog.upx8.com/OpenClaw-AI-OpenWrt-LuCI
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-03-14
fetch_date: 2026-03-15T04:34:12.980169
---

# OpenClaw AI 网关的 OpenWrt LuCI 管理插件

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# OpenClaw AI 网关的 OpenWrt LuCI 管理插件

发布时间:
2026-03-14 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
3233

OpenClaw AI 网关的 OpenWrt LuCI 管理插件。

在路由器上运行 OpenClaw，通过 LuCI 管理界面完成安装、配置和服务管理。

![OpenClaw AI 网关的 OpenWrt LuCI 管理插件](https://cdn.skyimg.net/up/2026/3/14/2f59e546.webp)

**系统要求**

| 项目 | 要求 |
| --- | --- |
| 架构 | x86\_64 或 aarch64 (ARM64) |
| C 库 | musl（自动检测；离线包仅支持 musl） |
| 依赖 | luci-compat, luci-base, curl, openssl-util |
| 存储 | **1.5GB 以上可用空间** |
| 内存 | 推荐 1GB 及以上 |

## 📦 安装

### 方式一：.run 自解压包（推荐）

无需 SDK，适用于已安装好的系统。

```
wget https://github.com/10000ge10000/luci-app-openclaw/releases/latest/download/luci-app-openclaw.run
sh luci-app-openclaw.run
```

### 方式二：.ipk 安装

```
wget https://github.com/10000ge10000/luci-app-openclaw/releases/latest/download/luci-app-openclaw.ipk
opkg install luci-app-openclaw.ipk
```

### 方式三：集成到固件编译

适用于自行编译固件或使用在线编译平台的用户。

```
cd /path/to/openwrt

# 添加 feeds
echo "src-git openclaw https://github.com/10000ge10000/luci-app-openclaw.git" >> feeds.conf.default

# 更新安装
./scripts/feeds update -a
./scripts/feeds install -a

# 选择插件
make menuconfig
# LuCI → Applications → luci-app-openclaw

# 编译
make package/luci-app-openclaw/compile V=s
```

使用 OpenWrt SDK 单独编译：

```
git clone https://github.com/10000ge10000/luci-app-openclaw.git package/luci-app-openclaw
make defconfig
make package/luci-app-openclaw/compile V=s
find bin/ -name "luci-app-openclaw*.ipk"
```

### 方式四：手动安装

```
git clone https://github.com/10000ge10000/luci-app-openclaw.git
cd luci-app-openclaw

cp -r root/* /
mkdir -p /usr/lib/lua/luci/controller /usr/lib/lua/luci/model/cbi/openclaw /usr/lib/lua/luci/view/openclaw
cp luasrc/controller/openclaw.lua /usr/lib/lua/luci/controller/
cp luasrc/model/cbi/openclaw/*.lua /usr/lib/lua/luci/model/cbi/openclaw/
cp luasrc/view/openclaw/*.htm /usr/lib/lua/luci/view/openclaw/

chmod +x /etc/init.d/openclaw /usr/bin/openclaw-env /usr/share/openclaw/oc-config.sh
sh /etc/uci-defaults/99-openclaw
rm -f /tmp/luci-indexcache /tmp/luci-modulecache/*
```

## 🔰 首次使用

1. 打开 LuCI → 服务 → OpenClaw，点击「安装运行环境」
2. 安装完成后服务会自动启动，点击「刷新页面」查看状态
3. 进入「Web 控制台」添加 AI 模型和 API Key
4. 进入「配置管理」可使用向导配置消息渠道

## 📂 目录结构

```
luci-app-openclaw/
├── Makefile                          # OpenWrt 包定义
├── luasrc/
│   ├── controller/openclaw.lua       # LuCI 路由和 API
│   ├── model/cbi/openclaw/basic.lua  # 主页面
│   └── view/openclaw/
│       ├── status.htm                # 状态面板
│       ├── advanced.htm              # 配置管理（终端）
│       └── console.htm               # Web 控制台
├── root/
│   ├── etc/
│   │   ├── config/openclaw           # UCI 配置
│   │   ├── init.d/openclaw           # 服务脚本
│   │   └── uci-defaults/99-openclaw  # 初始化脚本
│   └── usr/
│       ├── bin/openclaw-env          # 环境管理工具
│       └── share/openclaw/           # 配置终端资源
├── scripts/
│   ├── build_ipk.sh                  # 本地 IPK 构建
│   ├── build_run.sh                  # .run 安装包构建
│   ├── download_deps.sh              # 下载离线依赖 (Node.js + OpenClaw)
│   ├── upload_openlist.sh            # 上传到网盘 (OpenList)
│   └── build-node-musl.sh            # 编译 Node.js musl 静态链接版本
└── .github/workflows/
    ├── build.yml                     # 在线构建 + 发布
    └── build-node-musl.yml           # Node.js musl 构建
```

## 🤝 项目：https://github.com/10000ge10000/luci-app-openclaw

[取消回复](https://blog.upx8.com/OpenClaw-AI-OpenWrt-LuCI#respond-post-6710)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")