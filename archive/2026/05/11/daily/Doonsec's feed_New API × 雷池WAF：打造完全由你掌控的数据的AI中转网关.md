---
title: New API × 雷池WAF：打造完全由你掌控的数据的AI中转网关
url: https://mp.weixin.qq.com/s/W3jM4azSoaakT_rKEmcYxA
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:29.770080
---

# New API × 雷池WAF：打造完全由你掌控的数据的AI中转网关

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hjtlibzdr5X8h7LPO8lJb2sB0D6Jib2s9icsiblHJmPE31FeaUFgfbEjVVCyricJtIn4EricDwh7Biay0pThxiayibdWd9rWeohHquNEiaicvuz6nSXEB4/0?wx_fmt=jpeg)

# New API × 雷池WAF：打造完全由你掌控的数据的AI中转网关

原创

小志z
小志z

志在片语

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

我经常遇见手上有多个Apikey但是会出现协议不一致，而且需要频繁切换api地址等问题。用别人的中转站？方便是方便，但你的每一条数据都要经过别人服务器，你甚至不知道它背后映射的究竟是什么模型。

基于此，在手头上有闲置服务器资源的情况下还是自建比较适合我自己。既能统一协议、告别地址切换，又能把数据牢牢攥在手里。

## New API安装与配置

> 文档基于 RedHat 系 Rocky Linux 10.1 编写，安装软件包的命令与 Debian 系（如 Ubuntu）有所不同，请根据实际环境调整。

### 配置前置条件

先更新系统并安装基础工具

```
#更新系统sudo dnf update -y
#安装基础工具sudo dnf install -y vim git
```

添加阿里云 Docker CE 源

```
sudo dnf config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

安装Docker

```
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

配置Docker镜像源

```
vim /etc/docker/daemon.json
```

```
{    "registry-mirrors": [        "https://docker.xuanyuan.me",        "https://docker.m.daocloud.io"    ]}
```

启动并设置开机自启Docker

```
systemctl enable --now docker
```

可以Docker Pull一下测试镜像源是否可用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8kYBpqibohDpnxZJz3wibKRnx8kLHIic2REhPnAMFE5cyVN4Qe4h2T5Gic74OA3liaRXbics59ibvr8oMp4ZZyWwCdiaxD54JicSWDm6r8/640?wx_fmt=png&from=appmsg)

### 安装New API

Clone项目 并进入目录

```
git clone https://github.com/QuantumNous/new-api.gitcd new-api
```

配置Docker compose 配置文件（主要是为了改密码 改掉弱口令 记得把所有123456的弱口令批量替换成强密码

```
vim docker-compose.yml
```

```
version: '3.4' # For compatibility with older Docker versions
services:  new-api:    image: calciumion/new-api:latest    container_name: new-api    restart: always    command: --log-dir /app/logs    ports:      - "3000:3000"    volumes:      - ./data:/data      - ./logs:/app/logs    environment:      - SQL_DSN=postgresql://root:123456@postgres:5432/new-api # ⚠️ IMPORTANT: Change the password in production!      - REDIS_CONN_STRING=redis://:123456@redis:6379 # ⚠️ IMPORTANT: Change the password in production!      - TZ=Asia/Shanghai      - ERROR_LOG_ENABLED=true # 是否启用错误日志记录 (Whether to enable error log recording)      - BATCH_UPDATE_ENABLED=true  # 是否启用批量更新 (Whether to enable batch update)      - NODE_NAME=new-api-node-1  # 节点名称，用于审计日志中标识节点身份；多节点/容器部署时建议设置 (Node name used in audit logs; recommended when running multiple instances or in containers)
    depends_on:      - redis      - postgres    networks:      - new-api-network    healthcheck:      test: ["CMD-SHELL", "wget -q -O - http://localhost:3000/api/status | grep -o '\"success\":\\s*true' || exit 1"]      interval: 30s      timeout: 10s      retries: 3
  redis:    image: redis:latest    container_name: redis    restart: always    command: ["redis-server", "--requirepass", "123456"]  # ⚠️ IMPORTANT: Change this password in production!    networks:      - new-api-network
  postgres:    image: postgres:15    container_name: postgres    restart: always    environment:      POSTGRES_USER: root      POSTGRES_PASSWORD: 123456  # ⚠️ IMPORTANT: Change this password in production!      POSTGRES_DB: new-api    volumes:      - pg_data:/var/lib/postgresql/data    networks:      - new-api-network
volumes:  pg_data:
networks:  new-api-network:    driver: bridge
```

启动Docker compose

```
docker compose up -d
```

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicpcAMcHkCHyEqXomrWSjibuQYhob4oOZR3GuCqfeXP8SRdPEIMgO0EdeibVeKbibgf9CpfN5AKwUPXxsOQjyp32A5xbV3uia8mJqo/640?wx_fmt=png&from=appmsg)

然后看一下docker容器状态 全都是up就没问题啦

```
docker ps -a
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9TXAxtIRcRc02uHMEibtYzl9rKialQm2Xsollo3FgnIT95Ce7ian8s3dYiaZ5Gs8ZwIbDRgqAZicHNAicNqGViaEaUQnnLUqcyPQ7UlE/640?wx_fmt=png&from=appmsg)

用浏览器打开对应机器的3000端口 注意一下防火墙会不会拦截

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5Xib63OkSTialkDGDfibJ1Av6taPVGD4cNVjUDHUYTm5vIxFjOE1ZJXICI2sPpMiciaYd1a9qRbthKrrMOudYPoo6pfIic4NGZicRvBLa8/640?wx_fmt=png&from=appmsg)

然后设置好管理员账户 根据自己需求选择功能 完成初始化就好啦

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X920Sw2ayXhUO8VWbP99Z3ibfxJRMEutsZQQjG75ZafhT2bL4trKzajibzfgqBdFTicRd7xUpTGyibfZdOu3NZtsUJvKYhVSCUVRNc/640?wx_fmt=png&from=appmsg)

### 配置New API

增加中转模型 先登录后台 依次点击 渠道管理 添加渠道 我这里以英伟达Api为例子 填入Api地址和apikey

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9icofUqb0ZFzwwgmVbUewIYsvsj23rwAvziaMjGhsGSaHvCNx5M9Y9rN1DibzMMTFjK9IUneyGDNEzYDOLKic9wqowiaibPSfnIZbBE/640?wx_fmt=png&from=appmsg)

然后点击获取模型列表 将你需要的模型选入 看你的需求选择即可 最后点击提交

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicesiaSJCDiart64Qs62ryuYuB0Ihl0jxPJRs4XCAyTAl6PS6ibZ8UHYZgYUhHg3d0XKAm7urUAH7iaYsm5a2bynUlJMZdBBs5kltc/640?wx_fmt=png&from=appmsg)

然后点击测试 测一下这些接口是否能用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XicuCaSfbw6gnEvADdpoRLMQycFgaFIH7XuM20oK0iaTic4eXuBQ8dUH0qsWLhOhMZQk5a9stJUXChJh9p7eQtS8vfiaUnf5Fn3KBg/640?wx_fmt=png&from=appmsg)

### 测试一下中转效果

因为添加的模型都是openai协议的 尝试获得一个该平台的apikey

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5Xicvl41DemicJBu4cPiaXW4ONDE0ic4kdCXp1d0RqvjbxeAiaI6TJxAde4q1EZKDJSQfYPsstdhoBUZPkMtUibrLdKqskCLpeaB0DI5U/640?wx_fmt=png&from=appmsg)

然后复制apikey 到claude code进行测试即可 url设置到根就可以用内网测试的时候 对话测试一下

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8tBRqfb0J3G8rV3WwIt8EDS6dK2KZLoj9O2icGtxleuScv2N14UibriceAaTJcVcDQuSNxRegcyWlhbuKsbmamrOlnYY999rfCkg/640?wx_fmt=png&from=appmsg)

进行一下非对话交互也没问题！

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicEDPTJb7kogWHpM00vjWT71YlWpLJcnD0rOWlJuJwbmdibnSVTxlUlS1oiacUUCuDp8TLBTyzOOIHhbuicI2z5mxWa4oJ9VBxfg8/640?wx_fmt=png&from=appmsg)

## 配置雷池WAF

### 安装WAF

直接使用命令一键安装即可

```
sudo bash -c "$(curl -fsSLk https://waf-ce.chaitin.cn/release/latest/manager.sh)"
```

然后跟随指示安装即可 也是非常的方便

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8ydkGshjIwUHWqpyRIQicc1wMaqTLfIwVLMglVUk5jDYTf08SMThjXuNibKXjKfNcoh7KwjasaROEP00ty7aWmJjVN6XzvKUD9E/640?wx_fmt=png&from=appmsg)

等到显示了默认密码以及url 打开浏览器登录即可

![](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8LbWCJkoqKUWzRCF4Fa9aTDDF7DPKhREpBnUPEv1iaSOqzOfPK8yXAiay3ibgNuO2NFOic9FZJOpSicicAggHwqmvEEKSTwwoNAkvzg/640?wx_fmt=png&from=appmsg)

### 配置WAF

点击防护应用 添加一个防护 根据你自己需求添加即可 把上游设置成本机的3000端口 对外暴露端口根据你自己需求设置即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibVeOo1wFiaT8QuJzneeez8TibTlO00KQw4V0aibGBYucL5bVzZia6ib7osUw7ugwhUdpFp6qmf4mleMbFfQCmJwKVEIMYcoDCrq74M/640?wx_fmt=png&from=appmsg)

然后再访问你设置好的url 进行连接测试 发现没问题！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XicGcpsgrqd9BnTCTgJWuic6nMR9FUHmbrE617iaI6iaia5h7uicSYpxD36UUibnf6nNX3ONqqsxMHgokT0PjrLW86gyqCz4bVEic7eWVY/640?wx_fmt=png&from=appmsg)

然后把需要防护的自行打开即可 主要是起到一个日志记录 以及简单的防护

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibXDiav4DttL2duIrsY8pibHcEDG2VphVYLjzszgiawSkXFBiayRcNPTicVA3U0EdVKPRpvjqWLzhSDQiaMOUXAD9hw5FiamB2Ky1GhNE/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7dZqFspfFfHmfPEOUds23ibFibYPtvSsjS80euzsm0cuYoAeRkdqWPu4ukZEmfaRk4ibPKtpK2LvYg/0?wx_fmt=png)

志在片语

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7dZqFspfFfHmfPEOUds23ibFibYPtvSsjS80euzsm0cuYoAeRkdqWPu4ukZEmfaRk4ibPKtpK2LvYg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过