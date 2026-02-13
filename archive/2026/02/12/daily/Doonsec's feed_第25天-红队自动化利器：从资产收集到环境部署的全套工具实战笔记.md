---
title: 第25天-红队自动化利器：从资产收集到环境部署的全套工具实战笔记
url: https://mp.weixin.qq.com/s/IyhlhzMlbhKHjovLVtEgBA
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:41.414546
---

# 第25天-红队自动化利器：从资产收集到环境部署的全套工具实战笔记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9quQMvYnLUIQEliamMe4l5cc2Cs2FMHjVliaiahuicYeSZ5fbAW9XYPpd18rUxKuXN0jFo4kk6oB3erYeVicwicoWXsicyeqpmu7CVTN3g/0?wx_fmt=jpeg)

# 第25天-红队自动化利器：从资产收集到环境部署的全套工具实战笔记

原创

萧瑶
萧瑶

AlphaNet

![]()

在小说阅读器中沉浸阅读

攻防对抗中，效率决定成败。本文汇总了网络空间测绘、企业信息收集、综合资产管理、环境一键部署四大场景下的六款明星开源工具，全程基于阿里云香港服务器实操，提供保姆级配置指南与使用思路。无论你是蓝队排查还是红队渗透，这套“自动化组合拳”都能帮你快速构建攻击面管理能力。

---

📡 一、网络空间资产测绘：Yakit & TScanPlus

🔹 1. Yakit —— 网络安全“瑞士军刀”

· 项目地址：https://www.yaklang.com/

· 一句话简介：集成化渗透测试平台，通过插件化框架联动 Yak 语言，支持 MITM 劫持、端口扫描、漏洞验证等，此处重点使用其 网络空间引擎查询插件。

配置与启动（Linux / macOS）：

```bash

# 下载并安装（自动识别系统架构）

bash <(curl -sS -L http://www.yaklang.io/install.sh)

# 启动 Web UI

yakite web

```

访问 http://127.0.0.1:8080，进入“插件商店”安装 Fofa / Hunter / Quake 等查询插件，配置 API Key 后即可在“网络空间”模块一键查询目标资产。

🔹 2. TScanPlus —— 空间引擎聚合查询终端

· 项目地址：https://github.com/TideSec/TscanPlus

· 核心能力：同时调用 Fofa、Hunter、Quake、Zoomeye、Shodan、Censys、VT、0.zone、微步 等 9 个测绘/威胁情报平台，支持语法转换、结果去重导出。

快速上手：

```bash

# 下载二进制（以 Linux amd64 为例）

wget https://github.com/TideSec/TscanPlus/releases/latest/download/TscanPlus\_linux\_amd64.zip

unzip TscanPlus\_linux\_amd64.zip && cd TscanPlus

chmod +x TscanPlus

# 首次运行生成配置文件

./TscanPlus

# 编辑 config.yaml 填入各平台 API

vim config.yaml

# 示例查询：查找 title 包含“后台”且开放 443 端口的 IP

./TscanPlus -engine fofa -query 'title="后台" && port="443"' -max 100

```

---

🏢 二、企业股权/资产情报收集：ENScan\_Go

🔹 针对国内企业的信息搜集“杀手锏”

· 项目地址：https://github.com/wgpsec/ENScan\_GO

· 场景：HW/SRC 中快速获取目标集团的子公司、对外投资、域名、公众号、APP、ICP 备案等。

· 特点：基于天眼查/企查查/爱企查等公开数据，递归深度挖掘。

首次配置：

```bash

# 下载编译或直接下载 release

go install github.com/wgpsec/ENScan\_GO@latest

# 生成配置文件模板

ENScan\_GO -v

```

编辑 ~/.config/enscan/config.yaml，填入 天眼查、企查查 的 Cookie（建议注册会员账号提升额度）。

基础使用示例：

```bash

# 搜索某公司全称，递归获取 2 层子公司及对应域名

ENScan\_GO -n "阿里巴巴（中国）有限公司" -depth 2 -field company,domain

# 批量查询企业列表

ENScan\_GO -f company\_list.txt -o result.xlsx

```

详细参数见项目文档，实战中推荐配合 ARL/Nemo 做资产入库。

---

🗂️ 三、综合资产管理与攻击面收敛：ARL、Nemo、TestNet

1️⃣ ARL 灯塔（增强版）

· 项目地址：

· adysec 升级版：https://github.com/adysec/ARL

· ARL-plus-docker（推荐）：https://github.com/ki9mu/ARL-plus-docker

· 功能：域名爆破、端口扫描、服务识别、WAF 探测、POC 验证等，增强版修复了原版依赖问题并集成更多指纹。

Docker 快速部署（Ubuntu 20.04）：

```bash

apt update && apt install unzip wget docker.io docker-compose -y

cd /opt && mkdir docker\_arl && cd docker\_arl

wget -O docker.zip https://github.com/ki9mu/ARL-plus-docker/archive/refs/tags/v3.0.1.zip

unzip -o docker.zip

docker volume create arl\_db

cd ARL-plus-docker-3.0.1

docker-compose pull

docker-compose up -d

```

访问 https://服务器IP:5003，默认密码 admin/arlpass。

使用建议：配置“资产分组”与“策略模板”，定时任务结合 ENScan\_Go 输出的域名列表进行周期性巡检。

---

2️⃣ Nemo\_Go —— 轻量自动化资产收集平台

· 项目地址：https://github.com/hanc00l/nemo\_go

· 定位：纯 Go 重构，部署极简，支持 IP 段/域名/子域名/指纹识别/漏洞扫描 任务编排，可视化展示。

Docker 部署（Ubuntu 18.04+）：

```bash

# 下载 release 包

wget https://github.com/hanc00l/nemo\_go/releases/download/v2.5.1/nemo\_linux\_amd64.tar

mkdir nemo && tar xvf nemo\_linux\_amd64.tar -C nemo && cd nemo

# 启动 mysql + redis + nemo\_server

docker-compose up -d

```

访问 http://IP:8080，默认密码 nemo。

亮点：支持调用 Goby API 进行漏洞验证，可通过 Webhook 对接企业微信/钉钉实时告警。

---

3️⃣ TestNet —— 持续资产发现与风险监控

· 项目地址：https://github.com/testnet0/testnet

· 特性：基于 Golang + Vue3，专注于 攻击面持续监测，包含子域名爬取、端口变更识别、SSL 证书监控、暗链检测等。

一键构建（Ubuntu 22.04）：

```bash

git clone https://github.com/testnet0/testnet.git

cd testnet

bash build.sh   # 自动安装依赖、启动 docker-compose

```

运行成功后访问 http://IP:8000，注册账户即可创建监测任务。

特色功能：支持导入 ARL/Nemo 的资产结果，生成攻击面拓扑图，直观展示暴露面变化。

---

🚀 四、环境即服务：F8x 武器库一键部署

🔹 再也不用手动装工具了！

· 项目地址：https://github.com/ffffffff0x/f8x

· 理念：红队/蓝队常用工具集、代理环境、开发环境的 一键部署脚本，目前已集成 100+ 工具。

安装方式（推荐 CF Workers 国内加速）：

```bash

# 使用 wget

wget -O f8x https://f8x.io/

# 或使用 curl

curl -o f8x https://f8x.io/

chmod +x f8x

```

常用部署组合：

```bash

# 基础渗透环境（nmap、sqlmap、burp、msf、cs、字典等）

./f8x -p

# 内网渗透套件（fscan、frp、蚁剑、冰蝎等）

./f8x -i

# 代理隧道环境（frp、nps、gost、brook）

./f8x -f

# 全部安装（约 8GB，建议按需选择）

./f8x -all

```

脚本执行后会在 /opt/f8x 生成完整工具目录，并自动配置环境变量。

进阶技巧：编辑脚本头部 Config 区块可自定义下载源、工具版本。

---

💡 总结：打造自动化资产收集闭环

工具 核心贡献 配合场景

Yakit/TScanPlus 空间引擎聚合 从攻击者视角搜集暴露面，生成初始 IP/域名

ENScan\_Go 企业股权与数字资产 由公司名到子公司、域名、备案，填充资产台账

ARL/Nemo/TestNet 自动化扫描与持续监控 对资产进行端口、指纹、漏洞扫描，形成风险闭环

F8x 渗透环境快速构建 在新服务器/VPS 上一键部署红队作战工具集

工作流建议：

1️⃣ 使用 F8x 部署一台资产收集专用机（预装 docker、python3、go 环境）

2️⃣ 通过 ENScan\_Go 获取目标集团完整资产清单

3️⃣ 将清单导入 ARL 进行全端口+Web 指纹扫描

4️⃣ 同步资产至 Nemo/TestNet 开启周期性监控，并联动 Yakit/TScanPlus 验证测绘引擎新曝光的资产

5️⃣ 每日接收风险报告，对新增端口、漏洞进行应急响应

---

⚠️ 免责声明：本文所有工具仅供授权测试及安全研究使用，请遵守《网络安全法》及相关法律法规，切勿用于非法攻击。

📎 参考资料：

· Yakit 官方文档：https://www.yaklang.com/docs/start/

· ENScan\_Go 配置详解：https://github.com/wgpsec/ENScan\_GO/wiki

· ARL-plus-docker FAQ：https://github.com/ki9mu/ARL-plus-docker/issues

· Nemo 任务编排示例：https://github.com/hanc00l/nemo\_go/blob/main/README\_CN.md

· TestNet 开发计划：https://github.com/testnet0/testnet#readme

· F8x 全参数说明：https://github.com/ffffffff0x/f8x#readme

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

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