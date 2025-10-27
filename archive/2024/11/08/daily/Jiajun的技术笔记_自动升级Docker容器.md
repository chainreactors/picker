---
title: 自动升级Docker容器
url: https://jiajunhuang.com/articles/2024_11_07-auto_upgrade_docker.md.html
source: Jiajun的技术笔记
date: 2024-11-08
fetch_date: 2025-10-06T19:15:12.614144
---

# 自动升级Docker容器

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

* [自动升级Docker容器](#%25E8%2587%25AA%25E5%258A%25A8%25E5%258D%2587%25E7%25BA%25A7Docker%25E5%25AE%25B9%25E5%2599%25A8)

# 自动升级Docker容器

我有一些自托管软件，都是以Docker容器的形式运行的。之前都是隔段时间手动升级，不够方便。因此花了点时间写了一个自动升级
脚本，一劳永逸。

```
import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)

def upgrade_docker(bash_script_path):
    result = subprocess.run(['bash', bash_script_path], capture_output=True, text=True)
    logging.info(
        "execute %s, stdout %s, stderr %s, success? %s",
        bash_script_path, result.stdout, result.stderr, result.returncode == 0,
    )

def upgrade_all():
    # iter all bash scripts in the 'docker' directory
    for file in os.listdir('docker'):
        if file.endswith('.sh'):
            upgrade_docker(f'docker/{file}')

    # finally, run docker system prune -f
    subprocess.run(['docker', 'system', 'prune', '-f'])

if __name__ == '__main__':
    upgrade_all()
```

> 代码很简单，就是遍历 `docker` 目录下的所有 `.sh` 文件，然后执行它们。最后再清理一下无用的镜像。

然后在同级目录下创建一个 `docker` 目录，里面放置所有的升级脚本，比如 `docker/alist.sh`:

```
#!/bin/bash

docker rm -f alist

docker pull xhofe/alist-aria2:latest

docker run -d --restart=always \
    -v /var/lib/data/alist:/opt/alist/data \
    -p 5244:5244 -e PUID=0 -e PGID=0 -e UMASK=022 \
    --name="alist" xhofe/alist-aria2:latest
```

> 套路都是一样的，先删除旧容器，再拉取新镜像，最后重新运行容器。

配合一个 `cronjob`:

```
0 0 * * 1 /usr/bin/python3 /path/to/upgrade_docker.py
```

每周一凌晨自动升级一次，再也不用担心忘记升级了。

---

##### 相关文章

* [修复Linux下curl等无法使用letsencrypt证书](/articles/2019_11_26-lets_encrypt_linux_shell.md.html)
* [欣赏一下K&R两位大神的代码](/articles/2019_11_24-code_from_k_and_r.md.html)
* [MySQL的ON DUPLICATE KEY UPDATE语句](/articles/2019_11_19-mysql_duplicate_key_update.md.html)
* [使用microk8s快速搭建k8s](/articles/2019_11_17-microk8s.md.html)
* [Python中优雅的处理文件路径](/articles/2019_11_15-python_pathlib_path.md.html)
* [Go语言MySQL时区问题](/articles/2019_11_14-golang_mysql_timezone.md.html)
* [我的技术栈选型](/articles/2019_11_13-tech_stack.md.html)
* [为什么我要用Linux作为桌面？](/articles/2019_11_11-why_linux_as_desktop.md.html)
* [disqus获取评论时忽略query string](/articles/2019_11_08-disqus_thread_identifier.md.html)
* [MySQL性能优化指南](/articles/2019_11_06-mysql.md.html)
* [网络编程所需要熟悉的那些函数](/articles/2019_11_01-network_programming.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [这些年，我们错过的n个亿](/articles/2019_10_25-oh_my_money.md.html)
* [给Linux用户的FreeBSD快速指南](/articles/2019_10_19-freebsd_for_linux_users.md.html)

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