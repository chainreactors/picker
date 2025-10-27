---
title: 自建DERP服务器提升Tailscale连接速度(使用Nginx转发)
url: https://jiajunhuang.com/articles/2024_11_20-tailscale_derp.md.html
source: Jiajun的技术笔记
date: 2024-11-21
fetch_date: 2025-10-06T19:13:51.762102
---

# 自建DERP服务器提升Tailscale连接速度(使用Nginx转发)

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

* [自建DERP服务器提升Tailscale连接速度(使用Nginx转发)](#%25E8%2587%25AA%25E5%25BB%25BADERP%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8%25E6%258F%2590%25E5%258D%2587Tailscale%25E8%25BF%259E%25E6%258E%25A5%25E9%2580%259F%25E5%25BA%25A6%2528%25E4%25BD%25BF%25E7%2594%25A8Nginx%25E8%25BD%25AC%25E5%258F%2591%2529)
* [安装DERP](#%25E5%25AE%2589%25E8%25A3%2585DERP)
* [配置Nginx](#%25E9%2585%258D%25E7%25BD%25AENginx)
* [配置 ACL 规则](#%25E9%2585%258D%25E7%25BD%25AE%2bACL%2b%25E8%25A7%2584%25E5%2588%2599)

# 自建DERP服务器提升Tailscale连接速度(使用Nginx转发)

官方文档里，DERP服务器默认是直接占用443端口的，但是我的服务器上已经有了Nginx服务，因此好一顿折腾，终于成功了。

## 安装DERP

我没有使用 Docker 镜像，而是直接二进制+systemd的方式安装的(首先你得分配一个域名指向这个机器)：

```
# go install tailscale.com/cmd/derper@latest
# cp ~/go/bin/derper /usr/local/bin/
```

然后编辑`/etc/systemd/system/derper.service`：

```
[Unit]
Description=My Derper Service
After=network.target

[Service]
ExecStart=/usr/local/bin/derper -hostname=<域名，后面还会用> -a :30001 -http-port 30001 -stun-port 3478 -verify-clients
Restart=on-failure
User=root

[Install]
WantedBy=multi-user.target
```

然后`systemctl enable derper && systemctl start derper`。

## 配置Nginx

增加如下Nginx配置文件：

```
server {
    listen 80;
    listen 443 ssl;
    server_name <域名>;

    access_log <Nginx 日志路径>;
    error_log <Nginx 错误日志路径>;

    ssl_certificate <Let's Encrypt 证书路径>;
    ssl_certificate_key <Let's Encrypt 证书私钥路径>;

    location / {
        client_max_body_size 1G;

        # websockets
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        # other settings
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://127.0.0.1:30001;
    }
}
```

请注意，这里 WebSocket 的配置是必须的，否则 Tailscale 无法正常工作，我掉到这个坑好久才爬出来。

> 参考掉坑 issue: <https://github.com/tailscale/tailscale/issues/4072>

## 配置 ACL 规则

打开 tailscale 的管理页面，添加 ACL 规则，允许你的域名访问 DERP 服务器。

在 `ssh` 同级，添加：

```
// Define private derp
"derpMap": {
    "omitDefaultRegions": false,
    "regions": {
        "901": {
            "regionID":   901,
            "regionCode": "MyHK",
            "regionName": "My HongKong",
            "nodes": [
                {
                    "name":     "myhk",
                    "regionID": 901,
                    "hostName": "<域名>",
                    "DERPPort": 443,
                    "IPv4":     "<机器IP>",
                    "IPv6":     "none", // 如果你的服务器没有 IPv6
                    //"InsecureForTests": true,
                    "STUNPort": 3478,
                },
            ],
        },
    },
},

// ssh...
```

然后重启 tailscaled 服务，`systemctl restart tailscaled`。

就可以使用自有 DERP 服务器了，速度飞起。

---

##### 相关文章

* [让浏览器下载文件](/articles/2024_09_06-browser_download_file.md.html)
* [HTTP 压力测试中的 Coordinated Omission](/articles/2024_08_30-http_load_testing.md.html)
* [2的补码](/articles/2024_07_24-twos_complement.md.html)
* [编程语言中的 context 是什么？](/articles/2024_07_21-context.md.html)
* [flutter macOS 构建出错](/articles/2024_03_20-flutter_macos.md.html)
* [Flatpak 使用小记](/articles/2024_03_19-flatpak.md.html)
* [Golang CAS 操作是怎么实现的](/articles/2024_03_10-golang_cas.md.html)
* [PostgreSQL 当MQ来使用](/articles/2024_03_09-postgresql_as_mq.md.html)
* [Clash 结合 工作VPN 的网络设计](/articles/2024_03_08-clash_vpn.md.html)
* [使用 PostgreSQL 搭建 JuiceFS](/articles/2024_03_07-juicefs_postgresql.md.html)
* [PostgreSQL 配置优化和日志分析](/articles/2024_03_05-postgresql_conf.md.html)
* [有GitHub Copilot？那就可以搭建你的ChatGPT4服务](/articles/2024_03_03-copilot_as_gpt4.md.html)
* [窗口函数的使用(以PG为例)](/articles/2024_03_01-pg_window_function.md.html)
* [读《为什么学生不喜欢上学》](/articles/2024_01_16-why_dont_students_like_school.md.html)
* [OpenAI Prompt Engineering 摘录和总结](/articles/2024_01_07-openai_prompt_engineering.md.html)

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