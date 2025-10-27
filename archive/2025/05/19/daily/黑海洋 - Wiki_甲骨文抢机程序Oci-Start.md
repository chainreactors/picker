---
title: 甲骨文抢机程序Oci-Start
url: https://blog.upx8.com/4804
source: 黑海洋 - Wiki
date: 2025-05-19
fetch_date: 2025-10-06T22:26:32.676926
---

# 甲骨文抢机程序Oci-Start

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文抢机程序Oci-Start

发布时间:
2025-05-18

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
52156

# ![](https://cdn.skyimg.net/up/2025/5/18/c5f7acfa.webp)

# OCI-Start

一个使用API集成创建和管理Oracle云基础设施实例的系统。 目前支持的功能 功能一:支持多个api多实例开机 功能二:同步租户下的已开实例 功能三:引导卷管理(执行名称修改,引导卷vpu修改) 功能四:安全规则管理 功能五:登录用户管理(查询,添加admin用户) 功能六:ipv4切换一键开启ipv6 功能七:终止实例 功能八:实例流量查询 功能九:ip质量检测,并自动切换ip

## 功能特点

1. **主要功能**：
   * 使用API完成实例创建的程序，此程序支持多租户创建实例
   * 使用面板执行多个API的创建，以及API数据查询

## 项目地址

github地址:[https://github.com/doubleDimple/oci-start](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubm9kZXNlZWsuY29tL2p1bXA_dG89aHR0cHMlM0ElMkYlMkZnaXRodWIuY29tJTJGZG91YmxlRGltcGxlJTJGb2NpLXN0YXJ0)

## 环境要求

需要提前安装JDK 8+版本

### Debian/Ubuntu

```
sudo apt update
sudo apt install default-jdk
```

### CentOS/RHEL

```
# CentOS 7
sudo yum install java-1.8.0-openjdk-devel

# CentOS 8及之后版本（使用dnf）
sudo dnf install java-11-openjdk-devel
```

## 部署方法

### 方法一：脚本部署

*注意：新版本会检测安装Redis，之前安装了Redis的会有影响*

```
# 1. 切换到root用户下并创建文件夹
mkdir -p oci-start && cd oci-start

# 2. 下载执行脚本
wget -O oci-start.sh https://raw.githubusercontent.com/doubleDimple/shell-tools/master/oci-start.sh && chmod +x oci-start.sh

# 3. 直接运行脚本，即可自动安装部署

# 启动应用程序
./oci-start.sh start

# 停止应用程序
./oci-start.sh stop

# 重启应用程序
./oci-start.sh restart

# 更新到最新版本
./oci-start.sh update

# 完全卸载应用
./oci-start.sh uninstall
```

### 方法二：Docker部署

```
mkdir -p oci-start-docker && cd oci-start-docker

# 1. 下载执行脚本
wget -O docker.sh https://raw.githubusercontent.com/doubleDimple/shell-tools/master/docker.sh && chmod +x docker.sh

# 2. 执行脚本
# 安装应用
./docker.sh install

# 卸载应用
./docker.sh uninstall
```

# 查看容器状态

docker ps -a

# 查看容器日志

docker logs oci-start

```
## 配置说明

对于已经部署之前版本的用户，除了security配置完全删除外，其他配置可以暂时不要动，否则会导致找不到文件路径导致API失败。

```yaml
# 端口自行指定（默认端口为9856，如果不想改默认端口，不需要下载oci-start.yml）
server:
  port: 9856
```

## 操作命令

```
# 给oci-start.sh执行权限添加
chmod 777 oci-start.sh

# 启动程序
./oci-start.sh start

# 查看程序启动状态
./oci-start.sh status

# 停止程序
./oci-start.sh stop
```

## 访问

通过 `http://ip:port` 访问，注册用户名密码。

# ![](https://cdn.skyimg.net/up/2025/5/18/fdd02f52.webp)

## 另一个面板：oci-helper

## 核心功能

1. 支持同时**批量添加**多个租户配置信息，所有分页列表都支持**模糊搜索**、**状态筛选**。
2. 支持更改实例配置、引导卷配置、一键附加ipv6、一键放行所有端口、实例列表、引导卷列表、**一键开启免费AMD实例500MB**、**一键自动救援/缩小硬盘（默认47GB）**、**安全列表**、**实时流量统计**（分钟级别）、一键自动更新等功能。⭐⭐
3. 根据多个**CIDR网段**更换实例公共IP，遇到请求频繁等异常会直接忽略，不影响下一次执行，直至更换到指定IP段的IP。支持**更换IP后自动更新 Cloudflare DNS** 记录功能。⭐⭐
4. 多租户**同时批量开机**，后台一直运行，直至开机成功。⭐
5. 支持**断点续抢**，配置以及抢机任务都保存在本地数据库，服务重启会继续执行抢机任务，无需重复配置。⭐⭐
6. 支持多区号（配置项以region区分），例：我有一个4区号，则新增4个配置，修改region即可，其他配置项都一样。
7. 支持前端页面**实时查看后端日志**。
8. 支持**加密备份恢复**，实现无缝数据迁移，方便快捷。⭐⭐
9. 支持**MFA**登录验证功能（不是龟壳的，是我这个面板的登录），保证服务的安全性。
10. 支持分页查询、添加、更新、删除 **Cloudflare** 多个域名的 DNS 记录。⭐
11. 支持 **Telegram 机器人**简单操作，服务成功部署后向机器人发送`/start`选择操作。
12. 支持类似于甲骨文云 **Cloud Shell** 控制台功能，方便使用 netboot 救砖。⭐⭐
13. 支持IP信息查询（部署成功后访问 [http://ip:8818/ip-info](https://blog.upx8.com/go/aHR0cDovL2lwOjg4MTgvaXAtaW5mbw) ）以及首页显示全球服务器地图（可精确到街道的店铺），点亮全球。

## 💻一键 docker-compose 部署或更新

`bash <(wget -qO- https://github.com/Yohann0617/oci-helper/releases/latest/download/sh_oci-helper_install.sh)`

* 🔔 安装完成后浏览器直接`ip:8818`即可访问（建议之后通过https访问），账号密码默认都是：`yohann`。 第一次部署需要修改默认账号密码，`vi /app/oci-helper/application.yml`中的配置并执行`docker restart oci-helper`重启docker容器即可。
* 📃 如需查看完整日志，执行：`docker logs oci-helper >> /app/oci-helper/oci-helper.log`导出日志文件自行查看。

项目地址：https://github.com/Yohann0617/oci-helper

[取消回复](https://blog.upx8.com/4804#respond-post-4804)

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