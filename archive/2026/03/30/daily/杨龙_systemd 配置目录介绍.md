---
title: systemd 配置目录介绍
url: https://www.yanglong.pro/systemd-%e9%85%8d%e7%bd%ae%e7%9b%ae%e5%bd%95%e4%bb%8b%e7%bb%8d/
source: 杨龙
date: 2026-03-30
fetch_date: 2026-03-31T04:35:47.106380
---

# systemd 配置目录介绍

[跳至正文](#content)

# [杨龙](https://www.yanglong.pro/)

菜单

* [首页](https://www.yanglong.pro/)
* [links](https://www.yanglong.pro/link/)

# systemd 配置目录介绍

[发表评论](https://www.yanglong.pro/systemd-%E9%85%8D%E7%BD%AE%E7%9B%AE%E5%BD%95%E4%BB%8B%E7%BB%8D/#respond)

# systemd 配置目录详解

## 主要配置目录

### 1. **`/etc/systemd/system/`** （用户自定义配置）

* **用途**: 存放用户和系统管理员创建的服务单元
* **优先级**: 最高（会覆盖 `/usr/lib/systemd/system/` 中的同名文件）
* **典型应用**:
  + 自定义服务配置
  + 服务覆盖配置（override）
  + 服务的符号链接

```
# 查看目录内容示例
ls -la /etc/systemd/system/
```

### 2. **`/usr/lib/systemd/system/`** （系统默认配置）

* **用途**: 软件包安装时提供的默认服务单元文件
* **管理方式**: 由包管理器（apt/yum/dnf）维护
* **注意**: 不应直接修改此目录的文件

```
# 查看已安装服务的默认配置
ls -la /usr/lib/systemd/system/
```

### 3. **`/run/systemd/system/`** （运行时配置）

* **用途**: 运行时动态生成的单元文件
* **特点**: 系统重启后内容会丢失
* **优先级**: 高于 `/etc/systemd/system/`

---

## 配置文件类型

### 服务单元（`.service`）

定义系统服务的行为：

```
[Unit]
Description=My Application Service
After=network.target

[Service]
Type=simple
User=www-data
ExecStart=/usr/bin/php /var/www/html/artisan queue:work
Restart=always

[Install]
WantedBy=multi-user.target
```

### 路径监控单元（`.path`）

监控文件或目录变化：

```
[Unit]
Description=Watch config file changes

[Path]
PathChanged=/var/www/html/config.php
Unit=myapp.service

[Install]
WantedBy=multi-user.target
```

### 定时器单元（`.timer`）

定时任务（类似 cron）：

```
[Unit]
Description=Run backup daily

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

### 目标单元（`.target`）

分组管理服务（类似运行级别）：

* `multi-user.target` – 多用户文本模式
* `graphical.target` – 图形界面模式
* `network.target` – 网络就绪

---

## 常用管理命令

```
# 重载 systemd 配置（修改配置后必须执行）
sudo systemctl daemon-reload

# 启用服务（开机启动）
sudo systemctl enable myapp.service

# 启动服务
sudo systemctl start myapp.service

# 停止服务
sudo systemctl stop myapp.service

# 重启服务
sudo systemctl restart myapp.service

# 查看服务状态
sudo systemctl status myapp.service

# 查看服务日志
sudo journalctl -u myapp.service -f

# 禁用服务
sudo systemctl disable myapp.service

# 列出所有失败的服务
sudo systemctl --failed

# 查看服务依赖关系
systemctl list-dependencies myapp.service

# 查看启用的所有服务
systemctl list-unit-files --type=service --state=enabled
```

---

## 配置优先级顺序

```
/run/systemd/system/     (最高优先级)
    ↓
/etc/systemd/system/     (用户配置，推荐修改此处)
    ↓
/usr/lib/systemd/system/ (最低优先级，软件包默认配置)
```

---

## 实际应用场景

### 场景 1：创建自定义服务

```
# 1. 创建服务文件
sudo vim /etc/systemd/system/myapp.service

# 2. 重载配置
sudo systemctl daemon-reload

# 3. 启用并启动服务
sudo systemctl enable --now myapp.service
```

### 场景 2：覆盖现有服务配置

```
# 创建覆盖配置（不修改原文件）
sudo systemctl edit nginx

# 这会在 /etc/systemd/system/nginx.service.d/override.conf
# 添加自定义配置片段
```

### 场景 3：调试服务配置

```
# 测试服务配置是否正确
systemd-analyze verify /etc/systemd/system/myapp.service

# 查看服务启动时间分析
systemd-analyze blame
```

---

## 结合您的 WordPress 项目

基于您的项目结构，如果要为 WordPress 或相关服务创建 systemd 配置：

**示例：WordPress Cron 服务**

```
# /etc/systemd/system/wp-cron.service
[Unit]
Description=WordPress Cron Handler
After=network.target mysql.service

[Service]
Type=oneshot
User=www-data
WorkingDirectory=/var/www/html
ExecStart=/usr/bin/php wp-cron.php

[Install]
WantedBy=multi-user.target
```

**示例：监控配置文件变化**

```
# /etc/systemd/system/wp-config-monitor.path
[Unit]
Description=Monitor wp-config.php changes

[Path]
PathChanged=/var/www/html/wp-config.php
Unit=php-fpm.service

[Install]
WantedBy=multi-user.target
```

需要我帮您创建具体的 systemd 配置文件吗？

本条目发布于[2026年3月30日](https://www.yanglong.pro/systemd-%E9%85%8D%E7%BD%AE%E7%9B%AE%E5%BD%95%E4%BB%8B%E7%BB%8D/ "下午5:47")。属于[Linux](https://www.yanglong.pro/category/linux/)分类，被贴了 [systemd](https://www.yanglong.pro/tag/systemd/) 标签。作者是[杨龙](https://www.yanglong.pro/author/admin/ "查看所有由杨龙发布的文章")。

### 文章导航

[← MySQL 长度较大的VARCHAR索引限制说明](https://www.yanglong.pro/mysql-%E9%95%BF%E5%BA%A6%E8%BE%83%E5%A4%A7%E7%9A%84varchar%E7%B4%A2%E5%BC%95%E9%99%90%E5%88%B6%E8%AF%B4%E6%98%8E/)

### 发表回复 [取消回复](/systemd-%E9%85%8D%E7%BD%AE%E7%9B%AE%E5%BD%95%E4%BB%8B%E7%BB%8D/#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

Math Captcha
1 × 6 =

Powered by [MathCaptcha](https://wordpress.org/plugins/wp-advanced-math-captcha)

搜索

搜索

[502](https://www.yanglong.pro/tag/502/)
[certbot](https://www.yanglong.pro/tag/certbot/)
[composer](https://www.yanglong.pro/tag/composer/)
[docker](https://www.yanglong.pro/tag/docker/)
[ElasticSearch](https://www.yanglong.pro/tag/elasticsearch/)
[Flask-RESTful](https://www.yanglong.pro/tag/flask-restful/)
[flex](https://www.yanglong.pro/tag/flex/)
[gizp](https://www.yanglong.pro/tag/gizp/)
[goaccess](https://www.yanglong.pro/tag/goaccess/)
[GuzzleHttp](https://www.yanglong.pro/tag/guzzlehttp/)
[InnoDB存储引擎](https://www.yanglong.pro/tag/innodb%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E/)
[javascript](https://www.yanglong.pro/tag/javascript/)
[jdk](https://www.yanglong.pro/tag/jdk/)
[laravel](https://www.yanglong.pro/tag/laravel/)
[lru](https://www.yanglong.pro/tag/lru/)
[LVM](https://www.yanglong.pro/tag/lvm/)
[make](https://www.yanglong.pro/tag/make/)
[mongodb](https://www.yanglong.pro/tag/mongodb/)
[MySQL](https://www.yanglong.pro/tag/mysql/)
[mysql 函数大全](https://www.yanglong.pro/tag/mysql-%E5%87%BD%E6%95%B0%E5%A4%A7%E5%85%A8/)
[nginx](https://www.yanglong.pro/tag/nginx/)
[nginx gzip](https://www.yanglong.pro/tag/nginx-gzip/)
[openssl](https://www.yanglong.pro/tag/openssl/)
[php-fpm](https://www.yanglong.pro/tag/php-fpm/)
[pt-online-schema-change](https://www.yanglong.pro/tag/pt-online-schema-change/)
[python](https://www.yanglong.pro/tag/python/)
[RabbitMQ](https://www.yanglong.pro/tag/rabbitmq/)
[redis](https://www.yanglong.pro/tag/redis/)
[RESTful](https://www.yanglong.pro/tag/restful/)
[rockylinux](https://www.yanglong.pro/tag/rockylinux/)
[SELinux](https://www.yanglong.pro/tag/selinux/)
[shell](https://www.yanglong.pro/tag/shell/)
[slave](https://www.yanglong.pro/tag/slave/)
[solr](https://www.yanglong.pro/tag/solr/)
[SQL\_SLAVE\_SKIP\_COUNTER](https://www.yanglong.pro/tag/sql_slave_skip_counter/)
[Supervisor](https://www.yanglong.pro/tag/supervisor/)
[swoole](https://www.yanglong.pro/tag/swoole/)
[web.py](https://www.yanglong.pro/tag/web-py/)
[WebService](https://www.yanglong.pro/tag/webservice/)
[X-Forwarded-For](https://www.yanglong.pro/tag/x-forwarded-for/)
[xfs](https://www.yanglong.pro/tag/xfs/)
[xml](https://www.yanglong.pro/tag/xml/)
[Zend Studio](https://www.yanglong.pro/tag/zend-studio/)
[弹性布局](https://www.yanglong.pro/tag/%E5%BC%B9%E6%80%A7%E5%B8%83%E5%B1%80/)
[慢查询](https://www.yanglong.pro/tag/%E6%85%A2%E6%9F%A5%E8%AF%A2/)

### 其他操作

* [登录](https://www.yanglong.pro/wp-login.php)
* [条目 feed](https://www.yanglong.pro/feed/)
* [评论 feed](https://www.yanglong.pro/comments/feed/)
* [WordPress.org](https://cn.wordpress.org/)

### 交流讨论群

[![PHP开发技术交流](//pub.idqqimg.com/wpa/images/group.png "PHP开发技术交流")](https://qm.qq.com/cgi-bin/qm/qr?k=83kWH9ed7-t8BXB5zh3uDC2TfJdNtSJj&jump_from=webapi)

[![Flag Counter](data:image/bmp;base64...)](https://info.flagcounter.com/Egb7)
[![本站支持IPv6访问](https://static.ipw.cn/icon/ipv6-s3.svg)](https://ipw.cn/ipv6webcheck/?site=www.yanglong.pro "本站支持IPv6访问")

[粤ICP备2026014361号](https://beian.miit.gov.cn)

[粤公网安备44030002010655号](https://beian.mps.gov.cn/#/query/webSearch?code=44030002010655)

[自豪地采用WordPress](https://cn.wordpress.org/ "优雅的个人发布平台")