---
title: Vaultwarden 自建教程（Docker Compose 方式）
url: https://blog.upx8.com/Vaultwarden-Docker-Compose
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-01-24
fetch_date: 2026-01-25T03:56:11.731050
---

# Vaultwarden 自建教程（Docker Compose 方式）

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# Vaultwarden 自建教程（Docker Compose 方式）

发布时间:
2026-01-24 New Article

分类:
[程序开发/Code](https://blog.upx8.com/code)

热度:
1195

### **1)****创建目录**

```
mkdir -p /opt/vaultwarden/data
cd /opt/vaultwarden
```

### **2)****写入 docker-compose.yml**

```
version: '3'

services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    env_file:
      - ./.env
    volumes:
      - ./data:/data
    ports:
      - "8280:80"
```

**说明：**

* 这里把 Vaultwarden 暴露到 **8280****端口**（避免与宝塔冲突）。
* 宝塔 Nginx 将反代到这个端口。
* `ADMIN_TOKEN`必须自己改成一个超长随机字符串。

### **3)****写入 .env****文件****（把敏感信息放到`.env`****）**

```
# 基本
DOMAIN="https://yourdomain.com"  # 替换成你的域名
WEBSOCKET_ENABLED="true"         # 实时通知
SIGNUPS_ALLOWED="false"          # 是否允许注册
ADMIN_TOKEN="请在这里换成一个超长的随机字符串"

# SMTP（如果要启用邮件）
SMTP_HOST="smtp.office365.com"
SMTP_FROM="service@office365.com"
SMTP_PORT="587"
SMTP_SSL="starttls"
SMTP_USERNAME="service@office365.com"
SMTP_PASSWORD="你的邮箱密码或授权码"
```

### **4)****启动 Vaultwarden**

```
cd /opt/vaultwarden
docker compose pull
docker compose up -d
```

访问：

* http://服务器IP:8280
* 如果能打开 Bitwarden 网页端，就成功了。

### **5)**补充说明

**1. 登录ADMIN会提示：**

`` You are using a plain text `ADMIN_TOKEN` which is insecure. ``

`` Please generate a secure Argon2 PHC string by using `vaultwarden hash` or `argon2`. ``

`` See: Enabling admin page - Secure the `ADMIN_TOKEN` ``

`https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page#secure-the-admin_token`

解决这个问题，我们需要替换`ADMIN_TOKEN`，把 Admin Token 用 Argon2 哈希成 PHC 格式，增强安全性。

运行以下用来生成 Vaultwarden 管理员Token哈希​的命令：

```
docker run --rm -it vaultwarden/server:latest \
/vaultwarden hash
```

它会提示你输入明文 Token：

```
Password:
Confirm Password:
```

把你想使用的 Token 明文输入/粘进去，回车，就会得到这样一段：

```
ADMIN_TOKEN='$argon2id$v=19$m=65540,t=3,p=4$lVo1Sr……7dtUklqug'
```

将它直接替换`ADMIN_TOKEN`（如果这里值使用双引号包裹，则需要将`$`替换为`$$`： **双引号 “”** → 解析特殊字符（如 $变量）；**单引号****”** → 原样输出，不解析任何东西）。

**然后重启容器**

```
docker compose down
docker compose up -d
```

刷新网页后打开 /admin，输入你用于哈希的那个**明文****Token**（不是填入`.env`文件中的哈希值），能登录就成功啦。

**2. 宝塔反代配置：**

```
#PROXY-START/

location / {
    proxy_pass http://127.0.0.1:8280;
    # 必须透传真实的 Host，而不是写死
    proxy_set_header Host $host;
    # 基础反代头
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header REMOTE-HOST $remote_addr;
    # WebSocket 必须项
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    # 防止 Nginx 隐藏 Upgrade
    # proxy_hide_header Upgrade;
    add_header X-Cache $upstream_cache_status;
    # 静态缓存（可留可删）
    set $static_filer4jhQ5nY 0;
    if ($uri ~* "\.(gif|png|jpg|css|js|woff|woff2)$") {
        set $static_filer4jhQ5nY 1;
        expires 1m;
    }
    if ($static_filer4jhQ5nY = 0) {
        add_header Cache-Control no-cache;
    }
}

# 专门处理 Vaultwarden 的 WebSocket 通道
location /notifications/hub {
    proxy_pass http://127.0.0.1:8280;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

#PROXY-END/
```

[取消回复](https://blog.upx8.com/Vaultwarden-Docker-Compose#respond-post-5405)

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