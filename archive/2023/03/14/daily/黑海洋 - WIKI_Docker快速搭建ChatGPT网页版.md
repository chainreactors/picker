---
title: Docker快速搭建ChatGPT网页版
url: https://blog.upx8.com/3264
source: 黑海洋 - WIKI
date: 2023-03-14
fetch_date: 2025-10-04T09:30:39.294666
---

# Docker快速搭建ChatGPT网页版

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Docker快速搭建ChatGPT网页版

发布时间:
2023-03-13

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
27811

[![cover](https://github.com/Chanzhaoyu/chatgpt-web/raw/main/docs/c1.png)](https://github.com/Chanzhaoyu/chatgpt-web/blob/main/docs/c1.png) [![cover2](https://github.com/Chanzhaoyu/chatgpt-web/raw/main/docs/c2.png)](https://github.com/Chanzhaoyu/chatgpt-web/blob/main/docs/c2.png)

## **GitHub地址：**[https://github.com/Chanzhaoyu/chatgpt-web](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0NoYW56aGFveXUvY2hhdGdwdC13ZWI)

支持双模型，提供了两种非官方 `ChatGPT API` 方法

| 方式 | 免费？ | 可靠性 | 质量 |
| --- | --- | --- | --- |
| `ChatGPTAPI(gpt-3.5-turbo-0301)` | 否 | 可靠 | 相对较笨 |
| `ChatGPTUnofficialProxyAPI(网页 accessToken)` | 是 | 相对不可靠 | 聪明 |

对比：

1. `ChatGPTAPI` 使用 `gpt-3.5-turbo-0301` 通过官方`OpenAI`补全`API`模拟`ChatGPT`（最稳健的方法，但它不是免费的，并且没有使用针对聊天进行微调的模型）
2. `ChatGPTUnofficialProxyAPI` 使用非官方代理服务器访问 `ChatGPT` 的后端`API`，绕过`Cloudflare`（使用真实的的`ChatGPT`，非常轻量级，但依赖于第三方服务器，并且有速率限制）

警告：

1. 你应该首先使用 `API` 方式
2. 使用 `API` 时，如果网络不通，那是国内被墙了，你需要自建代理，绝对不要使用别人的公开代理，那是危险的。
3. 使用 `accessToken` 方式时反向代理将向第三方暴露您的访问令牌，这样做应该不会产生任何不良影响，但在使用这种方法之前请考虑风险。
4. 使用 `accessToken` 时，不管你是国内还是国外的机器，都会使用代理。默认代理为 [acheong08](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2FjaGVvbmcwOA) 大佬的 `https://bypass.duti.tech/api/conversation`，这不是后门也不是监听，除非你有能力自己翻过 `CF` 验证，用前请知悉。[社区代理](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3RyYW5zaXRpdmUtYnVsbHNoaXQvY2hhdGdwdC1hcGkjcmV2ZXJzZS1wcm94eQ)（注意：只有这两个是推荐，其他第三方来源，请自行甄别）
5. 把项目发布到公共网络时，你应该设置 `AUTH_SECRET_KEY` 变量添加你的密码访问权限，你也应该修改 `index.html` 中的 `title`，防止被关键词搜索到。

切换方式：

1. 进入 `service/.env.example` 文件，复制内容到 `service/.env` 文件
2. 使用 `OpenAI API Key` 请填写 `OPENAI_API_KEY` 字段 [(获取 apiKey)](https://blog.upx8.com/go/aHR0cHM6Ly9wbGF0Zm9ybS5vcGVuYWkuY29tL292ZXJ2aWV3)
3. 使用 `Web API` 请填写 `OPENAI_ACCESS_TOKEN` 字段 [(获取 accessToken)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGF0Lm9wZW5haS5jb20vYXBpL2F1dGgvc2Vzc2lvbg)
4. 同时存在时以 `OpenAI API Key` 优先

**获取自己的OPENAI的APIkey：**[https://platform.openai.com/account/api-keys](https://blog.upx8.com/go/aHR0cHM6Ly9wbGF0Zm9ybS5vcGVuYWkuY29tL2FjY291bnQvYXBpLWtleXM)

**更新环境**

```
apt update -y  && apt upgrade -y && apt install -y curl wget sudo socat
```

**安装 Docker**

```
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

curl -L "https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
```

**创建GPT目录，创建配置文件**

```
cd /home/ && mkdir gpt && cd gpt && nano docker-compose.yml
```

**compose配置代码**

version: '3.8'

```
services:

app:

image: chenzhaoyu94/chatgpt-web:main

ports:

- 3002:3002

environment:

OPENAI_API_KEY: Zeix8v6K00KpP      # 用自己的API KEY
```

**运行指令**

```
cd /home/gpt && docker-compose up -d
```

**创建nginx目录结构**

```
mkdir -p /home/nginx

touch /home/nginx/nginx.conf

mkdir -p /home/nginx/certs
```

**申请证书**

```
curl https://get.acme.sh | sh

~/.acme.sh/acme.sh --register-account -m xxxx@gmail.com

~/.acme.sh/acme.sh --issue -d gpt.kjlion.ga --standalone
```

**下载证书**

```
~/.acme.sh/acme.sh --installcert -d gpt.kjlion.ga  --key-file /home/nginx/certs/key.pem --fullchain-file /home/nginx/certs/cert.pem
```

**进入目录编辑文件**

```
cd /home/nginx/ && nano nginx.conf
```

**反向代理配置，代理指定IP加端口**

```
events {

worker_connections  1024;

}

http {

client_max_body_size 1000m;

#上传限制参数1G以内文件可上传

server {

listen 80;

server_name gpt.kjlion.ga;

return 301 https://$host$request_uri;

}

server {

listen 443 ssl;

server_name gpt.kjlion.ga;

ssl_certificate /etc/nginx/certs/cert.pem;

ssl_certificate_key /etc/nginx/certs/key.pem;

location / {

proxy_pass http://0.0.0.0:3002;

proxy_set_header Host $host;

proxy_set_header X-Real-IP $remote_addr;

proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

}

}

}
```

**部署容器**

```
docker run -d --name nginx -p 80:80 -p 443:443 -v /home/nginx/nginx.conf:/etc/nginx/nginx.conf -v /home/nginx/certs:/etc/nginx/certs -v /home/nginx/html:/usr/share/nginx/html nginx:latest
```

**查看运行状态**

```
docker ps -a
```

**开机自启动**

```
docker update --restart=always nginx

docker update --restart=always gpt-app-1
```

[取消回复](https://blog.upx8.com/3264#respond-post-3264)

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