---
title: 自建 RustDesk 远程中继服务器
url: https://mp.weixin.qq.com/s/enzc7EaB8FuPGqh3gMrzxQ
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:18.925177
---

# 自建 RustDesk 远程中继服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LtibzcRx8GjU6uvwPk4jggzcwmia6C1SWg9qibmeBcJEZVt0jEETQX7uxiaY5qnz7PGfCciaYyU1xEI74b12TibTRMU94wwkzF7SewV1683skuPKo/0?wx_fmt=jpeg)

# 自建 RustDesk 远程中继服务器

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

RustDesk 是一款优秀的开源远程桌面工具，但在实际使用中，默认的公共中继服务器常常难以保证稳定的连接质量，高峰时段甚至无法建立会话。若想获得更可靠、更可控的远程访问体验，自建 RustDesk Server 几乎是必经之路。好在整个部署流程十分简洁，只需一台云服务器，几分钟即可搭建完成，全程基于 Docker 运行。

本文将以 Ubuntu 22.04 为例，演示如何快速部署一套 RustDesk 中继服务，并完成客户端配置。

---

## 环境准备

建议选用国内的云服务器，例如腾讯云、阿里云或华为云等，以获得更低的网络延迟。操作系统推荐 Ubuntu 22.04。

---

## 第一步：安装 Docker

使用官方脚本一键安装 Docker：

```
curl -fsSL https://get.docker.com | bash
```

安装完成后，验证版本：

```
docker -v
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWCX4IS080IoN11LGVaXNONm7GWMEL3mhoRaFeIPRqwBebUqw9djWLkPP2zWbdewnCX6VaparHtyYGsq6FJr5zJwoQyiaEvxhak/640?wx_fmt=png&from=appmsg)

---

## 第二步：创建工作目录

```
mkdir -p /opt/rustdeskcd /opt/rustdesk
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUDAQhOapU9aU4rvfZGOsgbkF7u3a1ibicMeak9H1Ria0ibOs6T0nhctm0PuWVXpiaq4UYbPT0kQJUcJuCg9VkfzlCuoDaIbAusHibbA/640?wx_fmt=png&from=appmsg)

---

## 第三步：编写 docker-compose.yml

使用 nano 创建编排文件：

```
nano docker-compose.yml
```

填入以下内容：

```
cat << 'EOF' | tee docker-compose.yml > /dev/nullservices:  hbbs:    image: rustdesk/rustdesk-server:latest    container_name: hbbs    command: hbbs    network_mode: host    volumes:      - ./data:/root    depends_on:      - hbbr    restart: unless-stopped
  hbbr:    image: rustdesk/rustdesk-server:latest    container_name: hbbr    command: hbbr    network_mode: host    volumes:      - ./data:/root    restart: unless-stoppedEOF
```

保存并退出（`Ctrl+O` → 回车 → `Ctrl+X`）。

---

## 第四步：启动服务

先创建数据持久化目录，再拉取并启动容器：

```
mkdir datadocker compose up -d
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjUyUebZznicvYnZ4v0PbicfJA2BshWJQIiaeIUVXAFOcIJ30sXDHL0HEGCykZx3k0d6zx1yK1POqG7xu15o9Kq63cjZfcJ9qu6lYQ/640?wx_fmt=png&from=appmsg)

查看容器运行状态：

```
docker ps
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVvQTLytTJ9khJ0EBtSdMlbPXibddiacBu9wpBpnGe3Mn9ZPrXRicaueI1VJtX8w9gd9t0IYfzIcMGqdS3b51dsASZibsI7PeW9nG8/640?wx_fmt=png&from=appmsg)

正常情况下应看到 `hbbs` 与 `hbbr` 两个容器。

---

## 第五步：配置防火墙与安全组

请确保云服务器安全组放行以下关键端口：

* **21115（TCP）**
* **21116（TCP 和 UDP）**
* **21117（TCP）**

部分教程还会额外开放 21118（TCP）和 21119（TCP），一并放行即可。

---

## 第六步：获取公钥

进入数据目录，查看生成的公钥文件：

```
cd /opt/rustdesk/datacat id_ed25519.pub
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWkn5NggUTLA5q0CXCQVVWLf2hc97cQVgudoSTuh4uxjNpCGle6np0KAosrZyl8CNA8P8Y1nTKZtEaP49hWHqrpaBuhw2EKrwk/640?wx_fmt=png&from=appmsg)

输出类似：

```
zF2kGQ.........
```

请妥善保存这段公钥，后续客户端配置时需要用到。

---

## 第七步：客户端设置

在 RustDesk 客户端中，进入 **设置 → 网络 → ID/Relay 服务器**，填写以下信息：

* **ID 服务器**

  ：你的服务器公网 IP
* **中继服务器**

  ：你的服务器公网 IP
* **Key**

  ：上一步复制的公钥内容

示例：

```
ID 服务器：1.2.3.4中继服务器：1.2.3.4密钥：zF2kGQ.........
```

---

## 第八步：连接测试

将两台设备的客户端都配置为相同的自建服务器。若主界面显示 “就绪”（Ready），表示服务已成功连接，可以开始享受稳定流畅的远程控制体验。

---

## 进阶：绑定自定义域名

如果拥有域名（例如 `rd.example.com`），可将其解析至服务器公网 IP。但需要注意，**RustDesk 并非标准的 HTTP 协议服务，因此在使用 Cloudflare 等 CDN 时，务必关闭代理（灰色云朵，DNS Only 模式）**，不能开启橙色云朵（Proxied），否则会导致连接失败。

配置完成后，客户端中的服务器地址即可填写域名：

```
ID 服务器：rd.example.com中继服务器：rd.example.com密钥：（同上）
```

---

## 结语

至此，你已经拥有了一套完全属于自己的 RustDesk 中继服务，不仅摆脱了对公共服务器的依赖，也大幅提升了远程桌面的稳定性与安全性。整个部署过程仅需几条命令，后期维护也几乎零成本，非常适合个人或小团队长期使用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

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