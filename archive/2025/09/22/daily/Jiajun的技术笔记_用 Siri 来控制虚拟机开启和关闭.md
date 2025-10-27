---
title: 用 Siri 来控制虚拟机开启和关闭
url: https://jiajunhuang.com/articles/2025_09_21-siri_ssh.md.html
source: Jiajun的技术笔记
date: 2025-09-22
fetch_date: 2025-10-02T20:29:50.103842
---

# 用 Siri 来控制虚拟机开启和关闭

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [用 Siri 来控制虚拟机开启和关闭](#%25E7%2594%25A8%2bSiri%2b%25E6%259D%25A5%25E6%258E%25A7%25E5%2588%25B6%25E8%2599%259A%25E6%258B%259F%25E6%259C%25BA%25E5%25BC%2580%25E5%2590%25AF%25E5%2592%258C%25E5%2585%25B3%25E9%2597%25AD)
* [控制脚本](#%25E6%258E%25A7%25E5%2588%25B6%25E8%2584%259A%25E6%259C%25AC)
* [配置 sudo 免密执行该脚本](#%25E9%2585%258D%25E7%25BD%25AE%2bsudo%2b%25E5%2585%258D%25E5%25AF%2586%25E6%2589%25A7%25E8%25A1%258C%25E8%25AF%25A5%25E8%2584%259A%25E6%259C%25AC)
* [配置快捷指令](#%25E9%2585%258D%25E7%25BD%25AE%25E5%25BF%25AB%25E6%258D%25B7%25E6%258C%2587%25E4%25BB%25A4)

# 用 Siri 来控制虚拟机开启和关闭

我有下载专用的虚拟机和游戏专用的虚拟机，每次打开使用，都要通过 SSH 进去执行命令，或者用 cockpit 网页进行开关，
最近发现 iOS 快捷指令可以执行 SSH 命令，配置一个快捷指令，就可以通过 Siri 进行控制了。

## 控制脚本

```
#!/bin/bash

# 检查是否提供了参数
if [ $# -ne 2 ]; then
    echo "用法: $0 <start/shutdown> <虚拟机名称>"
    exit 1
fi

OP="$1"
VM_NAME="$2"

# 检查虚拟机是否存在
if ! sudo virsh dominfo "$VM_NAME" &>/dev/null; then
    echo "错误: 虚拟机 '$VM_NAME' 不存在"
    exit 2
fi

case "$OP" in
    "shutdown")
        echo "正在关闭虚拟机 '$VM_NAME'..."
        sudo virsh shutdown "$VM_NAME"
        ;;
    "start")
        echo "正在启动虚拟机 '$VM_NAME'..."
        sudo virsh start "$VM_NAME"
        ;;
    *)
        echo "虚拟机 '$VM_NAME' 处于未知状态: $VM_STATE"
        echo "请手动检查状态"
        exit 3
        ;;
esac
```

将文件内容保存到 `/usr/local/bin/vmctl.sh`，并设置执行权限

## 配置 sudo 免密执行该脚本

新增文件 `/etc/sudoers.d/vmctl`，内容如下:

```
# 允许用户无需密码执行vmctl
jiajun ALL=(ALL) NOPASSWD: /usr/local/bin/vmctl.sh *
```

## 配置快捷指令

在 Siri 设置中，点击左上角的添加按钮，搜索SSH，然后配置好用户名、IP、证书、命令，然后就可以通过Siri来控制虚拟机开启关闭，
非常方便。

---

##### 相关文章

* [ElasticSearch 学习笔记](/articles/2022_10_06-elasticsearch.md.html)
* [三种git流程以及发版模型](/articles/2022_07_28-git_flows.md.html)
* [错误处理实践](/articles/2022_07_27-how_to_return_error.md.html)
* [权限模型(RBAC/ABAC)](/articles/2022_07_15-access_control.md.html)
* [OIDC(OpenID Connect) 简介](/articles/2022_07_06-openid_connect.md.html)
* [任务队列简介](/articles/2022_07_05-task_queue.md.html)
* [PostgreSQL 操作笔记](/articles/2022_04_29-postgres_notes.md.html)
* [使用Drone CI构建CI/CD系统](/articles/2022_04_29-drone_ci.md.html)
* [Golang migrate 做数据库变更管理](/articles/2022_04_28-golang_migrate_iofs.md.html)
* [使用PostgreSQL做搜索引擎](/articles/2022_04_12-postgresql_fulltext_search.md.html)
* [Nginx 源码阅读（三）: 连接池、内存池](/articles/2022_03_23-nginx_source_code_3.md.html)
* [Nginx 源码阅读（二）: 请求处理](/articles/2022_03_22-nginx_source_code_2.md.html)
* [Nginx 源码阅读（一）: 启动流程](/articles/2022_03_21-nginx_source_code_1.md.html)
* [Go 泛型简明教程](/articles/2022_03_17-go_generics.md.html)
* [KVM 显卡穿透给 Windows](/articles/2022_03_15-kvm_windows_gpu_passthrough.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。