---
title: ARL-AI：ARL 资产侦察灯塔 + AI MCP
url: https://mp.weixin.qq.com/s/66aloqgIjz6eMVQ0mGw0EQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:53.364725
---

# ARL-AI：ARL 资产侦察灯塔 + AI MCP

# ARL-AI：ARL 资产侦察灯塔 + AI MCP

AC-UVC
AC-UVC

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

**ARL-AI：ARL 资产侦察灯塔 + AI MCP**在开源资产侦察灯塔 ARL 上叠加的 MCP 服务器 —— AI 可直接下发侦察任务、检索全量资产（站点/域名/IP/C 段/WIH/文件泄露/指纹/漏洞），灯塔 UI 内置 MCP 管理面板，支持一键部署与已有灯塔零拷贝叠加。

灯塔之上加了 **MCP 服务**，AI（ZCode / Claude 等）可直接增删改查灯塔的任务与资产；灯塔 UI 左侧菜单带 **MCP 栏目**（开关 / 密钥 / 监听 IP 与端口全部在界面上管理）。

![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMIDH81BPrPPnU9Ga7dn9ia6HnRic1cFeV43dsFdF585023azPr7jzCuWp5CqgE1SGn9ImQWZKJdLnapE1A954J9DuWIYEsCyoSEE/640?wx_fmt=png&from=appmsg)

## 灯塔 UI 的 MCP 栏目

左侧菜单底部「MCP」→ 管理面板：

| 功能 | 说明 |
| --- | --- |
| 服务状态 | 开/关服务，关闭后 AI 一律 403 |
| 监听设置 | 连接地址 IP 可选（枚举网卡 + `MCP_PUBLIC_IP`），端口可选，改端口自动重启生效（带占用预检，防止重启死循环） |
| 调用密钥 | 运行时生成 48 位 hex，可重置；缺失/错误一律 401 |
| 客户端配置 | 一键复制带 `X-API-Key` 请求头的 MCP 客户端 JSON |

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKmqaHia5cWV7XlhFibvnLUh82CiafhQ02feWSb8ser5jO1chCBWyr1YyhzicR8plKaWBFvn1Z5PmhKYbAYOqeom1NuZ81aYGrG6Qg/640?wx_fmt=webp&from=appmsg)

## 部署到服务器

### 方式零：叠加到已有灯塔（数据零拷贝，推荐存量场景）

原灯塔数据多不想拷贝？直接在它上面叠加，**不新起灯塔、不碰数据库**：

```
cd scripts/deploy
bash overlay_install.sh --dir /opt/docker_arl --web-port 5003 \
     --web-container arl_web --mcp-port 8010 --admin-port 8011 \
     --arl-pass <原灯塔密码> --public-ip <公网IP可选>
```

原理与保障：

* compose 增量走 `docker-compose.override.yml`（compose 原生合并），**原 docker-compose.yml 零改动**； 回滚 = 删 override 等三个文件 + `docker compose up -d web`（脚本末尾打印完整回滚命令）
* 前端注入放独立目录 `frontend-mcp/`，nginx 注入版为独立文件 `nginx-mcp.conf`，均以挂载方式生效
* 重建的只有 web 容器（约 30 秒界面中断）；worker/scheduler/mongodb 全程不动，**正在跑的扫描不受影响**
* MCP 服务 systemd 直连原灯塔 API，原灯塔全部历史数据即刻可读

### 方式一：一键部署（新服务器）

把工作目录拷到服务器，进入 `scripts/deploy/` 执行：

```
cd scripts/deploy
bash install.sh                                   # 默认端口 5003/5005/8010/8011
# 或自定义：
bash install.sh --web-port 5003 --http-port 5005 \
                --mcp-port 8010 --admin-port 8011 \
                --prefix arl --dir /opt/docker_arl_ai \
                --service mcp-ai --public-ip <服务器公网IP>
```

脚本自动完成：前置检查 → 写 compose/配置 → **从镜像提取前端并注入 MCP 栏目** → 注入 nginx 代理 → 启动容器组 → 安装 MCP 服务（venv + `mcp>=1.2,<2`）→ 写 systemd → 就绪等待 → 自检（Web/面板 API/数据面 401）→ 输出地址与卸载命令。 需要在 `scripts/deploy/` 同目录备好 `arl_mcp/`、`mcp_service.py`、`mcp_panel.js`（工程里都有）。 镜像默认 `swr.cn-south-1.myhuaweicloud.com/mingy/arl:latest`，可 `--image` 换源或提前 `docker load`。

### 方式二：手动分步部署

### 前置

* 已按 ARL 官方方式运行的灯塔（本方案用 `docker compose`，项目目录示例 `/opt/docker_arl_ai`， 容器名/端口/卷与原灯塔完全隔离）
* Python ≥ 3.10（宿主机跑 MCP 服务，`pip install "mcp>=1.2,<2" httpx uvicorn`；**注意必须 <2**，mcp 2.x 已把 FastMCP 改名）
* 前端注入：从 `arl_web` 容器拷出 `/code/frontend`，将 `mcp_panel.js` 放入并在`index.html` 的 `</body>` 前加 `<script src=/mcp_panel.js?v=1></script>`，目录挂载回容器

### nginx（灯塔 web 容器）

443 与 80 两个 server 块都加：

```
location /mcp_admin/ {
    proxy_pass http://host.docker.internal:8011/admin/;   # 需 extra_hosts: host-gateway
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

compose 里 web 服务加 `extra_hosts: ["host.docker.internal:host-gateway"]`。

### systemd（`/etc/systemd/system/mcp-ai.service`）

```
[Service]
WorkingDirectory=/opt/arl-ai
Environment=PYTHONPATH=/opt/arl-ai
Environment=ARL_URL=https://127.0.0.1:5004
Environment=ARL_MCP_WORKSPACE=/opt/arl-ai
Environment=ARL_USER=admin
Environment=ARL_PASS=<灯塔密码>
Environment=MCP_PORT=8010
Environment=MCP_ADMIN_PORT=8011
ExecStart=/opt/arl-ai/.venv/bin/python /opt/arl-ai/mcp_service.py
Restart=always
```

## 工具获取

点击关注下方名片进入公众号

回复关键字【261118】获取下载链接

## 往期精彩

往期推荐

[一款应急响应图形化界面软件工具且支持MCP服务进行AI自动化应急响应分析。](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498056&idx=1&sn=557db5081126920726c5cf2c3f8bcf54&scene=21#wechat_redirect)

[iOS 内存与诊断取证工具包：DSH 插件（15 个 ios\_\* 工具 + 右侧栏面板）、MCP server、代码健康扫描](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498022&idx=1&sn=48133d02cd64f4e99e79ab3659715e80&scene=21#wechat_redirect)

[CVE-2026-98260-小米 17 Pro Max（popsicle）一键 root · KernelSU 越狱模式 | 仅限自己持有并授权的设备](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498015&idx=1&sn=e2af054c3379f3feb330b2bdee079f89&scene=21#wechat_redirect)

[AgenticPenTest  | Agent 协作渗透测试工作台](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498014&idx=1&sn=fc8bb3e9c58a1dd597f89e4d015b3526&scene=21#wechat_redirect)

[CTF 线下赛用的离线 PHP 速查手册 | 11,930 条条目、196 条实战技巧、990 个payload、PHP 官方中文手册索引](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498006&idx=1&sn=4d7a4c451c63c7dc94e9c5cba8cf6683&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过