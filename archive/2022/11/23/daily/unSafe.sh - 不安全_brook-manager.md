---
title: brook-manager
url: https://buaq.net/go-136800.html
source: unSafe.sh - 不安全
date: 2022-11-23
fetch_date: 2025-10-03T23:28:34.132862
---

# brook-manager

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

brook-manager

A Web UI for fully automatic management of BrookFeaturesFeatures功能Fully aut
*2022-11-22 22:56:1
Author: [github.com(查看原文)](/jump-136800.htm)
阅读量:18
收藏*

---

A Web UI for fully automatic management of [Brook](https://github.com/txthinking/brook)

## Features

| Features | 功能 |
| --- | --- |
| Fully automatic deployment of brook | 全自动部署 brook |
| User registration/payment/adding nodes will automatically trigger deployment brook | 用户注册/支付/添加节点会自动触发部署 brook |
| You never even need to log into the node machine | 你甚至永远不需要登录节点机器 |
| User registration | 用户注册 |
| Traffic Statistics | 流量统计 |
| Multi-port multi-user | 多端口多用户 |
| Single-port multi-user | 单端口多用户 |
| Audit rules | 审计规则 |
| multi-level lines | 多级别线路 |
| Multi-level VIP | 多级别 VIP |
| Order and payment | 订单及支付 |
| Automatically generate subscription links | 自动生成订阅链接 |
| Ban/Restore User | 禁用/恢复用户 |
| One-line command deployment | 一行命令部署 |
| MySQL database [Auth](https://github.com/denodrivers/mysql/issues/37#issuecomment-651771807) | MySQL 数据库 [Auth](https://github.com/denodrivers/mysql/issues/37#issuecomment-651771807) |
| Reset all user traffic on the 1st of every month | 每月 1 号重置所有用户流量 |
| Automatically clear their nodes when users expire | 当用户到期自动清除其节点 |
| It also supports adding your own manual deployment brook link and traffic Statistics | 同时也支持添加你自己手动部署的 brook link 和流量统计 |
| ... | ... |

## Install [nami](https://github.com/txthinking/nami)

```
bash <(curl https://bash.ooo/nami.sh)
```

#### Install mysql

Here take Ubuntu 22.04 as an example, if there is a problem, you can google how to solve the problem of mysql installation and configuration

```
apt-get install mysql-server mysql-client
nami install mysql-init
mysql-init
systemctl restart mysql.service
```

Test via mysql client

```
mysql -h 127.0.0.1 -u root -p111111
```

#### Install brook-manager

```
nami install joker nico hancock mad brook-manager
```

#### Run brook-manager http server

create a http server `http://127.0.0.1:8080`

```
brook-manager --listen 127.0.0.1:8080 --ui default --mysqladdress 127.0.0.1:3306 --mysqlusername root --mysqlpassword 111111 --mysqldbname brook
```

#### Run brook-manager task

```
brook-manager --task --mysqladdress 127.0.0.1:3306 --mysqlusername root --mysqlpassword 111111 --mysqldbname brook
```

#### Run a reverse proxy web server

Here is an example of nico, of course you need to prepare a domain name and resolve it to your server IP

```
nico domain.com http://127.0.0.1:8080
```

#### How to run command as daemon

You may like [joker](https://github.com/txthinking/joker)

#### Amdin URL

<https://domain.com/admin/>

#### User URL

<https://domain.com>

## PR Welcome

```
nami install hancock mad 7z deno denobundle
git clone https://github.com/txthinking/brook-manager.git
cd brook-manager

dev=1 deno run -Ar main.js --listen 127.0.0.1:8080 --ui default --mysqladdress 127.0.0.1:3306 --mysqlusername root --mysqlpassword 111111 --mysqldbname brook
dev=1 deno run -Ar main.js --task --mysqladdress 127.0.0.1:3306 --mysqlusername root --mysqlpassword 111111 --mysqldbname brook

# then open http://127.0.0.1:8080/admin/
# then open http://127.0.0.1:8080
```

#### File introduction

```
├── adminapi.js     // admin api
├── userapi.js      // user api
├── cron.js         // cron
├── task.js         // task
├── main.js         // entry
├── mysqlmigrate.js // mysql db migration
├── static/
│   └── default/    // default ui, you can create more ui
│       ├── account.html
│       ├── admin/  // admin ui
│       ├── cryptocurrency_payment.html
│       ├── index.html
│       ├── lang/   // i18n
│       ├── signin.html
│       ├── signup.html
│       ├── simulate_payment.html
│       └── vip.html
```

## License

```
- Any client-side web page based on this project and any derivatives must provide merchant contact information:

    telegram group or other ways to contact you

- Any client-side web page based on this project and any derivatives must contain the following statement in a prominent place(or other languages with the same meaning):

    The current site is built by the merchant based on the open source software brook-manager(https://github.com/txthinking/brook-manager), and brook has no interest in you. If you encounter problems, please contact the merchant.
```

## Disclaimer

We have no liability to you.

文章来源: https://github.com/y35uishere/brook-manager
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)