---
title: ProxyCat 渗透测试ip代理池工具
url: https://blog.upx8.com/4736
source: 黑海洋 - Wiki
date: 2025-04-13
fetch_date: 2025-10-06T22:05:26.111718
---

# ProxyCat 渗透测试ip代理池工具

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# ProxyCat 渗透测试ip代理池工具

发布时间:
2025-04-12

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
27568

## ProxyCat简介

一款部署于云端或本地的隧道代理池中间件，可将静态代理IP灵活运用成隧道IP，提供固定请求地址，一次部署终身使用

## 开发缘由

在渗透过程中，经常需要隐藏或更换IP地址以绕过安全设备。然而，市面上的隧道代理价格高昂，普遍在20-40元/天，这对于许多人来说难以接受。笔者注意到，短效IP的性价比很高，一个IP只需几分钱，平均每天0.2-3元。

综上所述，**ProxyCat** 应运而生！本工具旨在将持续时间仅有1分钟至60分钟不等的短效IP转变为固定IP供其他工具使用，形成代理池服务器，部署一次即可永久使用。

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1003-1-scaled.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDMtMS1zY2FsZWQud2VicA)

## 功能特点

* **两种协议监听**：支持 HTTP/SOCKS5 协议监听，兼容更多工具。
* **三种代理地址**：支持 HTTP/HTTPS/SOCKS5 代理服务器及身份鉴别。
* **灵活切换模式**：支持顺序、随机及自定义代理选择，优化流量分配。
* **动态获取代理**：通过 GetIP 函数即时获取可用代理，支持 API 接口调用。
* **代理保护机制**：在使用 GetIP 方式获取代理时，首次运行不会直接请求获取，将会在收到请求的时候才获取。
* **自动代理检测**：启动时自动检测代理有效性，剔除无效代理。
* **智能切换代理**：仅在请求运行时获取新代理，减少资源消耗。
* **失效代理切换**：代理失效后自动验证切换新代理，确保不中断服务。
* **身份认证支持**：支持用户名/密码认证和黑白名单管理，提高安全性。
* **实时状态显示**：展示代理状态和切换时间，实时掌握代理动态。
* **动态更新配置**：无需重启服务，动态检测配置并更新。
* **Web UI界面**：提供 Web 管理界面，操作管理更加便捷。
* **Docker部署**：Docker 一键部署，Web 统一管理。
* **中英文双语**：支持中文英文一键切换。
* **配置灵活**：通过 config.ini 文件自定义端口、模式和认证信息等。
* **版本检测**：自动检查软件更新，保证版本最新。

## 免责申明

* 如果您下载、安装、使用、修改本工具及相关代码，即表明您信任本工具。
* 在使用本工具时造成对您自己或他人任何形式的损失和伤害，我们不承担任何责任。
* 如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
* 请您务必审慎阅读、充分理解各条款内容，特别是免除或者限制责任的条款，并选择接受或不接受。
* 除非您已阅读并接受本协议所有条款，否则您无权下载、安装或使用本工具。
* 您的下载、安装、使用等行为即视为您已阅读并同意上述协议的约束。

## 下载地址

[ProxyCat-V2.0.4.zip](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hvbm1hc2hpcm9uZWtvL1Byb3h5Q2F0L3JlbGVhc2VzL2Rvd25sb2FkL1Byb3h5Q2F0LVYyLjAuNC9Qcm94eUNhdC1WMi4wLjQuemlw)

## ProxyCat 使用手册

### 重要事项

* Python版本最好为Python 3.11
* Releases中为较为稳定的打包版本，不一定是最新
* API 接口所获取的代理地址必须为 IP:PORT 格式且只提供一条地址

### 源码使用及 Docker 部署

#### 源码手册

**Windows&Mac**：浏览器访问位于 Github 的源码存储库并下载：[ProxyCat](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hvbm1hc2hpcm9uZWtvL1Byb3h5Q2F0)

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1003-2.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDMtMi53ZWJw)

**Linux**：通过 Git 方法拉取项目到本地

```
git clone https://github.com/honmashironeko/ProxyCat.git
```

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1003-3.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDMtMy53ZWJw)

安装 Python 依赖（**请尽量保证Python版本为3.8-3.11**）

```
pip install -r requirements.txt
# 或使用国内源：
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

进入 config 文件夹内找到 config.ini 配置文件，按照自己拥有的资源选择不同的代理服务器获取方法

1️⃣如果您的代理服务器地址为固定的连接，不需要动态更换，可以使用本地 ip.txt 的方式提供格式如下所示

```
# 支持 http/https/socks5 三种代理服务器地址，支持账号密码校验
socks5://neko:123456@127.0.0.1:7890
https://neko:123456@127.0.0.1:7890
http://neko:123456@127.0.0.1:7890
socks5://127.0.0.1:7890
https://127.0.0.1:7890
http://127.0.0.1:7890
...
```

2️⃣如果您是通过 API 方式获取代理地址，可以在 config.ini 中修改配置（配置后不再读取 ip.txt）

```
# config.ini 配置文件中将以下两条配置进行修改
use_getip = True
getip_url = 获取代理地址的 API 接口
# 请注意，API 接口所获取的代理地址必须为 IP:PORT 格式且只提供一条地址，如果格式不同请到 getip.py 脚本中修改代码，如果您需要指定协议（默认为socks5）可以进入 getip.py 脚本中修改
```

当您配置完成之后就可以运行工具了

```
python ProxyCat.py
python app.py (Web控制管理-推荐方式)
```

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1003-4.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDMtNC53ZWJw)

### Docker 手册

Windows 可以下载 Docker 官方工具：[Docker Desktop](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hvbm1hc2hpcm9uZWtvL1Byb3h5Q2F0L2Jsb2IvbWFpbi9Qcm94eUNhdC1NYW51YWwvZG9jcy5kb2NrZXJkLmNvbS5jbg)

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1003-5.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDMtNS53ZWJw)

Linux 可以通过清华大学源提供的脚本一键安装：[清华大学安装脚本](https://blog.upx8.com/go/aHR0cHM6Ly9taXJyb3JzLnR1bmEudHNpbmdodWEuZWR1LmNuL2hlbHAvZG9ja2VyLWNlLw)

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1003-6.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDMtNi53ZWJw)

安装完成后请测试docker、docker-compose是否安装成功，如果安装失败请百度

Windows&Linux 进入 ProxyCat 文件夹下（**在此之前请根据源码手册中 config.ini 配置部分完成参数修改**）运行以下命令进行部署

```
# 进入ProxyCat文件夹中并构建镜像和启动容器
docker-compose up -d --build

# 停止服务和启动服务（每次修改完配置后需要重启服务）
docker-compose down | docker-compose up -d

# 查看日志信息
docker logs proxycat

# docker端口默认为1080和5000,1080为监听端口，5000为web页面管理如需其他端口请对应修改并放行
```

### 配置文件介绍

```
# 日志显示级别(默认为:1)
# 0: 仅显示代理切换和错误信息
# 1: 显示代理切换、倒计时和错误信息
# 2: 显示所有详细信息
# 仅终端管理时生效
display_level = 1

# 本地服务器监听端口(默认为:1080)
# Local server listening port (default:1080)
port = 1080

# Web 管理页面端口(默认为:5000)
web_port = 5000

# 代理地址轮换模式：cycle 表示循环使用，loadbalance 表示负载均衡(默认为:cycle)
# Proxy rotation mode: cycle means cyclic use, loadbalance means load balancing (default:cycle)
mode = cycle

# 代理地址更换时间（秒），设置为 0 时每次请求都更换 IP(默认为:300)
# Proxy address rotation interval (seconds), when set to 0, IP changes with each request (default:300)
interval = 300

# 是否使用 getip 模块获取代理地址 True or False(默认为:False)
# Whether to use getip module to obtain proxy addresses True or False (default:False)
use_getip = False

# 获取新代理地址的URL
# URL to get new proxy address
getip_url = http://example.com/getip

# 代理服务器认证用户名(如果代理服务器需要认证)
# Proxy server authentication username (if proxy server requires authentication)
proxy_username =

# 代理服务器认证密码(如果代理服务器需要认证)
# Proxy server authentication password (if proxy server requires authentication)
proxy_password =

# 代理地址列表文件(默认为:ip.txt)
# Proxy address list file (default:ip.txt)
proxy_file = ip.txt

# 是否启用代理检测功能 True or False(默认为True)
# Whether to enable proxy detection feature True or False (default:True)
check_proxies = True

# 语言设置 (cn/en)
# Language setting (cn/en)
language = cn

# IP白名单文件路径（留空则不启用白名单）
# IP whitelist file path (leave empty to disable whitelist)
whitelist_file = whitelist.txt

# IP黑名单文件路径（留空则不启用黑名单）
# IP blacklist file path (leave empty to disable blacklist)
blacklist_file = blacklist.txt

# IP认证优先级（whitelist/blacklist）
# IP authentication priority (whitelist/blacklist)
# whitelist: 优先判断白名单，在白名单中的IP直接放行
# whitelist: prioritize whitelist check, IPs in whitelist are allowed directly
# blacklist: 优先判断黑名单，在黑名单中的IP直接拒绝
# blacklist: prioritize blacklist check, IPs in blacklist are rejected directly
ip_auth_priority = whitelist

# Web 管理页面访问token，留空则无需token(默认为:honmashironeko)
token = honmashironeko

# 在[Users]下面是用户管理组，"账号=密码"一行一个，留空时代理无需身份鉴别(默认为:neko=123456)
[Users]
neko=123456
```

### Web 控制面板

采用源码部署的话通过 **python app.py** 启动 Web 控制面板，并根据提示访问 Web

[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1004-7.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDQtNy53ZWJw)
[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1004-8.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDQtOC53ZWJw)
[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1004-9.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDQtOS53ZWJw)
[![ProxyCat 渗透测试ip代理池工具](https://www.ddosi.org/wp-content/uploads/2025/04/1004-10.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzEwMDQtMTAud2VicA)

## 问题Q&A

Q：为什么运行后我的XXX工具代理还是没换？

A：ProxyCat 并不是全局代理工具，需要XXX工具支持使用代理，将流量发送到 ProxyCat 的本地监听端口才会经过代理池。

Q：为什么倒计时结束后代理没有更换？

A：ProxyCat 为了节约硬件资源和代理服务器资源，特意修改运行逻辑为有流量经过的时候才会更换代理，这样可以减少资源的浪费，同时可以部署一次，长期可用。

Q：为什么我用 getip 方式获取代理地址的时候，首次运行会报 None ，没有可用的代理地址？

A：为了防止资源浪费，通过 getip 获取的情况一般是付费购买静态短效IP，运行就获取的话会浪费大量资源从而导致资金损耗，为避免这种情况发生，首次运行不会主动获取，您只需要正常使用发包，ProxyCat 会自动获取并发送。

Q：getip.py 当中的appKey和anquanma是做什么的？

A：这两个参数是用作自动将当前请求IP添加到服务商（请查看readme中最下面的第一个推荐）的白名单中，免去每次IP变更需重新添加的烦恼，其中anquanma(安全码)需要到个人中心配置。

Q：我自己有静态IP提供地址...