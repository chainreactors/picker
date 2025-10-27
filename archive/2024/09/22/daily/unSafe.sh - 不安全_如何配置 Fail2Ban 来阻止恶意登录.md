---
title: 如何配置 Fail2Ban 来阻止恶意登录
url: https://buaq.net/go-263254.html
source: unSafe.sh - 不安全
date: 2024-09-22
fetch_date: 2025-10-06T18:20:33.690929
---

# 如何配置 Fail2Ban 来阻止恶意登录

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

如何配置 Fail2Ban 来阻止恶意登录

介绍：Fail2Ban 是一个用于禁止多次认证错误的恶意登录的工具。通过扫描日志文件（例如 /var/log/auth.log），该工具可以识别并禁止过
*2024-9-21 17:54:39
Author: [www.upx8.com(查看原文)](/jump-263254.htm)
阅读量:18
收藏*

---

## 介绍：

Fail2Ban 是一个用于禁止多次认证错误的恶意登录的工具。通过扫描日志文件（例如 `/var/log/auth.log`），该工具可以识别并禁止过多失败登录尝试的 IP 地址。它通过更新系统的防火墙规则来实现这一功能，拒绝来自这些 IP 地址的新连接，尽管 Fail2Ban 可以降低错误认证尝试的频率，但它不能完全消除由弱认证带来的风险，建议设置仅使用两因素或公钥/私钥认证机制来更进一步保障安全。

## 环境要求：

* Python 版本 >= 3.5 或者 PyPy3
* python-setuptools 和 python-distutils（或 python3-setuptools）

  在 Python 解释器中尝试导入这两个模块来检查是否安装：

  未报错即证明安装成功

  安装方式：

  （注：一般情况下，在 CentOS 或 RHEL 系统中，distutils 通常已经在安装 Python 的时候自动安装了）
* （可选）pyinotify >= 0.8.3，可能需要：

  + Linux 版本 >= 2.6.13

## 部署方法：

### 第一步：下载源代码

* 可以直接下载 tar 文件，然后解压：
* 或者可以从 GitHub 克隆源代码：

### 第二步：运行安装脚本

在下载源代码的目录下，执行以下命令进行安装：

这会将 Fail2Ban 安装到 python 的库目录中，将可执行脚本放置到 /usr/bin，将配置文件放置到 /etc/fail2ban。

### 第三步：检查 Fail2Ban 是否正确安装

可以通过以下命令来查看安装的 Fail2Ban 的版本：

### 第四步：将 Fail2ban 设置为自动启动服务

将适合你的 Linux 发行版的脚本从 files 目录复制到 /etc/init.d。

例如，在 Debian 系统中：

### 第五步：进行具体配置

可通过`fail2ban-client -h`来查看具体的配置教程

举例：配置 Fail2Ban 使得对10分钟内登录失败次数达到 3 次的 IP 进行永久封锁

1. 创建 jail。这里将 jail 命名为 `myjail`，并使用 `polling` 作为后端：
2. 设置 jail 的日志路径。这里将 `/var/log/auth.log` 设置为要监视的日志文件：
3. 添加失败正则表达式。这个表达式将用于匹配登录失败的日志条目。具体的表达式需要根据实际日志格式进行修改：
4. 设置封禁时间。这里设置 `bantime` 为 `-1`，表示一旦 IP 被封禁，该封禁将永不过期：
5. 设置失败次数。这里设置 `maxretry` 为 `3`，表示如果一个 IP 地址在 `findtime` 时间内登录失败3次，那么该 IP 地址将被封禁：
6. 设置查找时间。这里设置 `findtime` 为 `600`，表示如果一个 IP 地址在过去的10分钟（600秒）内登录失败次数达到 `maxretry`，也就是3次，那么该 IP 地址将被封禁：
7. 最后，启动 jail：

完成以上步骤后，Fail2Ban 将开始监视 `/var/log/auth.log` 文件，如果在10分钟内有任何 IP 地址登录失败3次，那么该 IP 地址将被永久封禁。

## 相关地址：

GitHub地址：<https://github.com/fail2ban/fail2ban>

文章来源: https://www.upx8.com/4346
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)