---
title: vps常用脚本和部署项目
url: https://blog.upx8.com/4912
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-03
fetch_date: 2025-12-04T03:17:48.685531
---

# vps常用脚本和部署项目

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# vps常用脚本和部署项目

发布时间:
2025-12-03 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
2340

### 💻 VPS 基础测试与信息查询 (Testing & Info)

| 类别 | 功能描述 | 命令/脚本 |
| --- | --- | --- |
| **融合怪** | **全面性能测试**，通常包含系统信息、IO、测速等。 | `curl -L https://github.com/spiritLHLS/ecs/raw/main/ecs.sh -o ecs.sh && chmod +x ecs.sh && bash ecs.sh` |
| **IP解锁** | 检查当前IP地址的媒体流（如Netflix等）解锁情况。 | `bash <(curl -Ls IP.Check.Place)` |
| **聚合测评** | NodeLoc 综合性能测评脚本。 | **CentOS：** `yum install wget&&wget -O Nlbench.sh https://raw.githubusercontent.com/everett7623/nodeloc_vps_test/main/Nlbench.sh && chmod +x Nlbench.sh && ./Nlbench.sh` **Debian/Ubuntu/Deepin：** `wget -O Nlbench.sh https://raw.githubusercontent.com/everett7623/nodeloc_vps_test/main/Nlbench.sh && chmod +x Nlbench.sh && ./Nlbench.sh` |
| **路由追踪** | **去程路由追踪。** | `curl [nxtrace.org/nt](http://nxtrace.org/nt) |
| *路由追踪* | **查看回程路由。** | `nexttrace 你的宽带ip` |
| **Iperf测速** | **Iperf3 网络测速**（需先安装）。 | `apt update` `apt install iperf3` **客户端测试命令示例：** `iperf3.exe -c 小鸡的ip -P 1 -t 60 -R` |
| **是否超售** | 检查是否使用了 `virtio_balloon`，间接判断可能存在超售（仅适用于KVM）。 | `lsmod |

---

### 🛠️ VPS 系统管理和优化 (System Tools & Optimization)

| 类别 | 功能描述 | 命令/配置 |
| --- | --- | --- |
| **脚本合集** | **大杂烩多功能脚本。** | `curl -fsSL https://raw.githubusercontent.com/eooce/ssh_tool/main/ssh_tool.sh -o ssh_tool.sh && chmod +x ssh_tool.sh && ./ssh_tool.sh` |
| **科技lion** | **通用脚本合集**（注意：原版可能收集信息）。 | **原版：** `bash <(curl -sL kejilion.sh)` **修改版（去除统计，未经验证）：** `bash <(curl -sS <https://raw.githubusercontent.com/kejilion/sh/main/kejilion.sh> |
| **内存优化** | **增加 2G 虚拟内存 (Swap)。** | `sudo fallocate -l 2G /swapfile` `sudo chmod 600 /swapfile` `sudo mkswap /swapfile` `sudo swapon /swapfile` `echo '/swapfile none swap sw 0 0' |
| **修改SSH端口** | 将 SSH 默认端口 `22` 改为自定义端口。 | `sudo nano /etc/ssh/sshd_config` (修改 `Port` 行) `sudo systemctl restart sshd` |
| **密钥登录** | 设置仅允许 SSH 密钥登录，提高安全性。 | `nano ~/.ssh/authorized_keys` (加入公钥) ... (修改 `sshd_config` 配置项) `sudo systemctl restart sshd` |
| **UFW 防火墙** | 安装 UFW，并配置基本出入站规则（允许 SSH 端口）。 | `sudo apt install ufw -y` `sudo ufw default allow outgoing` `sudo ufw default deny incoming` `sudo ufw allow 22` (替换为你的 SSH 端口) `sudo ufw enable` |
| **Fail2ban** | **安装 Fail2ban**，防止 SSH 暴力破解。 | **手动安装：** `sudo apt install fail2ban` **一键脚本：** `wget https://raw.githubusercontent.com/FunctionClub/Fail2ban/master/fail2ban.sh` `bash fail2ban.sh` |
| **修改主机名** | 解决主机名解析问题。 | `nano /etc/hosts` (修改 `127.0.1.1` 后的主机名) |
| **修改DNS** | 更换系统 DNS 解析器，用于解锁或改善解析速度。 | **脚本：** `chattr -i /etc/resolv.conf && wget -N --no-check-certificate https://raw.githubusercontent.com/chengziqaq/dnsunblocknetflix/master/dns-change.sh && chmod +x dns-change.sh && ./dns-change.sh 要增加的dns` |
| **TCP 调优** | **网络参数优化**，主要用于优化线路质量和稳定性。 | `wget -q https://raw.githubusercontent.com/BlackSheep-cry/TCP-Optimization-Tool/main/tool.sh -O tool.sh && chmod +x tool.sh && ./tool.sh` |

---

### 💿 系统重装 (DD System)

| 类别 | 功能描述 | 命令/脚本 |
| --- | --- | --- |
| **leitbogioro** | **DD 系统为 Debian**（SSH 端口不变，默认密码 `LeitboGi0ro`）。 | **安装依赖和脚本：** `apt update -y` `apt install wget -y` `wget --no-check-certificate -qO InstallNET.sh 'https://raw.githubusercontent.com/leitbogioro/Tools/master/Linux_reinstall/InstallNET.sh' && chmod a+x InstallNET.sh` **执行：** `bash InstallNET.sh -debian` |
| **煎饼佬** | **DD 系统脚本**（默认密码 `123@@@`，可自定义）。 | `curl -O <https://raw.githubusercontent.com/bin456789/reinstall/main/reinstall.sh> |
| **第三方工具** | DD 系统的其他参考脚本。 | (链接地址) |

---

### 🚀 代理服务及网络工具 (Proxy & Network)

| 类别 | 项目 / 协议 | 功能描述 | 命令/脚本 |
| --- | --- | --- | --- |
| **sing-box** | 233boy | sing-box 代理服务安装脚本。 | `bash <(wget -qO- -o- https://github.com/233boy/sing-box/raw/main/install.sh)` |
| **sing-box** | fscarmen | sing-box 代理服务带订阅功能脚本。 | `bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/sing-box/main/sing-box.sh)` |
| **sing-box** | mack-a | mack-a 8合1 sing-box 脚本。 | `wget -P /root -N --no-check-certificate "https://raw.githubusercontent.com/mack-a/v2ray-agent/master/install.sh" && chmod 700 /root/install.sh && /root/install.sh` |
| **sing-box** | ygkkk | yonggekkk 的 sing-box 脚本。 | `bash <(curl -Ls https://raw.githubusercontent.com/yonggekkk/sing-box-yg/main/sb.sh)` |
| **3x-ui** | 面板管理 | 代理服务面板管理系统。 | `bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)` |
| **WARP** | 解锁工具 | 安装 WARP，用于解锁流媒体（如Netflix）。 | **首次运行：** `wget -N https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh && bash menu.sh [option] [lisence/url/token]` |
| **端口转发** | realm | 使用 realm 进行端口转发。 | `wget -N https://raw.githubusercontent.com/qqrrooty/EZrealm/main/realm.sh && chmod +x realm.sh && ./realm.sh` |
| **端口转发** | gost | 使用 gost 进行端口转发。 | `wget --no-check-certificate -O gost.sh https://raw.githubusercontent.com/qqrrooty/EZgost/main/gost.sh && chmod +x gost.sh && ./gost.sh` |
| **DNS解锁** | 流媒体解锁 | 使用脚本一键设置 DNS 解锁。 | `wget https://raw.githubusercontent.com/Jimmyzxk/DNS-Alice-Unlock/refs/heads/main/dns-unlock.sh && bash dns-unlock.sh` |

---

### 📊 探针和监控 (Probes & Monitoring)

| 类别 | 项目 | 功能描述 | 命令/脚本 |
| --- | --- | --- | --- |
| **哪吒探针** | v1 脚本 | 官方安装脚本。 | `curl -L https://raw.githubusercontent.com/nezhahq/scripts/refs/heads/main/install.sh -o nezha.sh && chmod +x nezha.sh && sudo ./nezha.sh` |
| **哪吒探针** | Cf tunnel 版 | 基于 Cloudflare Tunnel 的版本（推荐）。 | (链接地址) |
| **beszel 探针** | 直接运行 | 轻量级探针，用于实时监控。 | **下载并运行：** `curl -sL "..." |
| **beszel 探针** | Docker 版 | 使用 Docker Compose 部署 beszel。 | `wget https://github.com/henrygd/beszel/raw/refs/heads/main/supplemental/docker/hub/docker-compose.yml` `docker-compose up -d` |
| **Webssh** | Next terminal | 基于 Web 的终端访问和管理工具。 | (官方文档链接) |
| **Webssh** | Easynode | 便捷的 Web 终端工具。 | (Github 链接) |

---

### 🌐 建站和面板 (Web Panels)

| 类别 | 项目 | 功能描述 | 命令/脚本 |
| --- | --- | --- | --- |
| **1Panel** | 国产面板 | 现代化、易用的 Linux 服务器运维管理面板。 | `curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh` |
| **aapanel** | 国际版宝塔 | 国际版建站和运维面板。 | `URL=https://www.aapanel.com/script/install_7.0_en.sh && if [ -f /usr/bin/curl ];then curl -ksSO "$URL" ;else wget --no-check-certificate -O install_7.0_en.sh "$URL";fi;bash install_7.0_en.sh aapanel` |
| **宝塔** | 国内面板 | 宝塔 Linux 面板（LTS 稳定版）。 | `wget -O install.sh https://download.bt.cn/install/install_lts.sh && bash install.sh ed8484bec` |

---

### 🐳 Docker 相关 (Docker & Compose)

#### Docker 安装与管理

| 类别 | 功能描述 | 命令/脚本 |
| --- | --- | --- |
| **安装 Docker** | 官方一键安装脚本。 | `curl -fsSL https://get.docker.com -o get-docker.sh` `sudo sh get-docker.sh` |
| **更新容器** | 使用 **Watchtower** 自动（或手动）更新所有容器并清理旧镜像。 | `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once` |
| **lucky** | **Docker 版本的lucky**，用于反向代理和自动申请证书。 | `docker run -d --name lucky --restart=always --net=host gdy666/lucky` |
| **微信转发** | Docker 部署微信消息转发服务。 | (Docker Run 命令) |
| **Filebrowser** | Docker 部署文件浏览器。 | (Docker Run 命令) |

#### Docker Compose 部署示例

| 项目 | 功能描述 | Compose Yaml 主要内容 |
| --- | --- | --- |
| **Dockge** | Docker Compose 的 Web UI 管理工具。 | (安装初始化命令，用于下载 `compose.yaml` 并启动) |
| **chatgpt-next-web** | **ChatGPT Next Web** 的优化版本。 | (Compose Yaml 配置，注意端口映射和环境变量) |
| **new-api 和 openwebui** | **新一代 AI 接口转发和 Web 聊天界面** 组合。 | (Compose Yaml 配置，注意端口映射、数据卷和网络设置) |

---

### 📦 PT/媒体相关 (PT & Media)

| 类别 | 功能描述 | 命令/脚本 |
| --- | --- | --- |
| **盒子刷流** | **Dedicated-Seedbox** 脚本，用于 PT 盒子刷流。 | `bash <(wget -qO- https://raw.githubusercontent.com/jerry048/Dedicated-Seedbox/main/Install.sh) -u <帐号> -p <密码> -c 3072 -q 4.3.9 -l v1.2.19 -b -v` |

| 分类 | 编号 | 项目名称 | 作用/描述 | GitHub/文档链接 |
| --- | --- | --- | --- | --- |
| **密码与认证** | 1 | **Vaultwarden** | Bitwarden密码管理器的轻量级实现。 | `https://github.com/dani-garcia/vaultwarden` |
| **远程与终端** | 2 | **RustDesk** | 远程桌面软件的开源替代品。 | `https://github.com/rustdesk/rustdesk` |
|  | 3 | **EasyNode** | 在线SSH工具。 | `https://github.com/chaos-zhu/easynode` |
|  | 4 | **Nexus-Terminal** ...