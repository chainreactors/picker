---
title: NGINX 爆出堆溢出高危漏洞，可致 RCE！我们开源了一款自查工具
url: https://mp.weixin.qq.com/s/eJ5WgkGQNN0FyOy1SzB1Bg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:16.637835
---

# NGINX 爆出堆溢出高危漏洞，可致 RCE！我们开源了一款自查工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VszWkovemuibrPCZxZR2J7ibqhhWFIV5uKt1o2LmLibrXJhDKH91eRl23icaZXN7VZJrh7LTVbpKdqk1TADwwn0T1zxEufrXvWVTHKtuVAbOhtU/0?wx_fmt=jpeg)

# NGINX 爆出堆溢出高危漏洞，可致 RCE！我们开源了一款自查工具

原创

iak3ec
iak3ec

薛定谔的安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# NGINX 爆出堆溢出高危漏洞，可致 RCE！我们开源了一款自查工具

---

## 前言

近日，NGINX 官方披露了一个存在于 `ngx_http_rewrite_module` 中的**堆溢出漏洞（CVE-2026-42945）**，影响范围涵盖 NGINX 开源版 0.6.27 至 1.30.0 以及 NGINX Plus 商业版 R32 至 R36。

该漏洞一旦被利用，攻击者可实现**拒绝服务（DoS）甚至远程代码执行（RCE）**，对使用 NGINX 作为反向代理或负载均衡器的互联网基础设施构成严重威胁。

为帮助广大安全运维人员快速排查风险，我们第一时间开发并开源了 **NGINX Rift** 漏洞扫描与验证工具，支持远程指纹识别和本地深度配置审计。

---

## 一、漏洞原理：一个问号引发的"灾难"

CVE-2026-42945 的根因在于 NGINX 处理 rewrite 规则时，对**未命名捕获组反向引用**（如 `$1`、`$2`）的内存拷贝逻辑存在缺陷。当替换字符串中同时包含 `?`（查询字符串分隔符）和未命名捕获组引用时，内部的堆缓冲区拷贝操作可能越界写入。

### 触发条件（三者缺一不可）

1. NGINX 配置中存在 `rewrite` 指令
2. 替换 URL 中包含 `?` 字符
3. 替换 URL 中使用了 `$1`、`$2` 等未命名捕获组引用

### 存在漏洞的配置

```
# 危险！同时包含 ? 和 $1 未命名捕获组
rewrite ^/api/(.*)$ /internal?id=$1 last;
```

### 安全的配置写法

```
# 安全：使用命名捕获组 <myid> 替代 $1
rewrite ^/api/(?<myid>.*)$ /internal?id=$myid last;
```

为什么命名捕获组是安全的？因为 NGINX 内部对命名捕获组（`?<name>`）和未命名捕获组（`$1`）走了**完全不同的代码路径**，命名版本不涉及触发溢出的那段内存拷贝逻辑。

---

## 二、影响范围

| 组件 | 受影响版本 | 修复版本 |
| --- | --- | --- |
| NGINX 开源版 | 0.6.27 ~ 1.30.0 | 1.30.1 (stable) / 1.31.0 (mainline) |
| NGINX Plus 商业版 | R32 ~ R36 | R32 P6, R33 P4, R34 P4, R35 P3, R36 P4 |
| NGINX Ingress Controller | 多个版本线受影响 | v1.9.6+, v1.10.2+, 3.7.3, 4.0.2, 5.4.2 |

### 一个容易踩的坑：版本号 ≠ 是否安全

很多运维同学看到自己服务器上 `nginx -v` 显示的版本号比较老，就认为一定存在漏洞。但实际上，**Linux 发行版（Ubuntu、CentOS 等）的包管理器经常会对旧版本进行 Backport（向后移植）补丁修复**。

也就是说，你的 NGINX 版本号可能是 `1.18.0`，但 Canonical 或 Red Hat 已经在 `1.18.0-0ubuntu1.4` 这样的包版本中悄悄修补了 CVE-2026-42945。

**所以，判断是否安全，不能只看版本号，还要检查 OS 包的补丁状态。**

---

## 三、NGINX Rift：一键自查

为了帮助大家快速确认自身环境的风险状态，我们开发了 **NGINX Rift** 工具，提供两种检测模式。

### 模式一：远程扫描 (Scan)

适用于批量摸排互联网资产。工具会向目标发送 HTTP 请求，解析 `Server` 响应头中的 NGINX 版本号，判断是否在受影响范围内。

```
# 扫描单个目标
./nginx_rift_scanner scan -u http://your-target.com

# 批量扫描（从文件读取）
./nginx_rift_scanner scan -f targets.txt
```

批量扫描完成后，工具会输出分类汇总：哪些目标存在风险、哪些安全、哪些连接失败。

### 模式二：本地深度验证 (Verify)

适用于登录到服务器后的深度自查。工具会执行三步立体审计：

**第一步：二进制版本检测 + OS 补丁回溯检查**

运行 `nginx -v` 获取版本号，然后调用 `dpkg-query`（Debian/Ubuntu）或 `rpm --changelog`（CentOS/RHEL）检查系统包是否已包含 CVE-2026-42945 的修复补丁。

**第二步：配置文件语义分析**

递归解析 NGINX 配置文件（包括所有 `include` 引入的子配置），精准识别包含 `?` 和 `$1` 的危险 rewrite 规则。

**第三步：K8s Ingress 资源探测**

如果服务器上安装了 `kubectl`，工具会自动获取集群中所有 Ingress 资源，检查是否存在危险的 `rewrite-target` 注解配置。

```
# 自动查找默认配置路径
./nginx_rift_scanner verify

# 指定配置文件
./nginx_rift_scanner verify -p /etc/nginx/nginx.conf
```

---

## 四、修复方案

根据你的环境和条件，可以选择以下方案：

### 方案一：紧急配置缓解（推荐，零停机）

如果你无法立即升级 NGINX，可以**在不重启服务的情况下**修改配置：

```
# 修改前（存在漏洞）
rewrite ^/api/(.*)$ /internal?id=$1 last;

# 修改后（安全）
rewrite ^/api/(?<myid>.*)$ /internal?id=$myid last;
```

修改后执行 `nginx -t && nginx -s reload` 即可生效，**完全不影响线上服务**。

### 方案二：操作系统包管理器更新

```
# Ubuntu / Debian
sudo apt-get update && sudo apt-get upgrade nginx

# CentOS / RHEL
sudo yum update nginx
```

更新后建议使用 NGINX Rift 的 `verify` 模式确认补丁已生效。

### 方案三：源码编译升级

从 NGINX 官方下载 1.30.1+ 或 1.31.0+ 版本重新编译安装。商业版用户升级至对应的安全补丁版本。

### 方案四：云原生 K8s 环境

排查所有 Ingress 资源中的 `rewrite-target` 注解，升级 NGINX Ingress Controller 至安全版本。

### 方案五：纵深防御

无论是否受漏洞影响，建议在 `http` 块中添加：

```
server_tokens off;
```

隐藏版本号，增加攻击者的侦察成本。

---

## 五、下载地址

关注微信公众号，私信发送`NGINX-Rift`或`CVE-2026-42945`获取项目地址

---

## 总结

CVE-2026-42945 是一个影响范围极广的 NGINX 高危漏洞，但好在**触发条件明确、配置缓解手段简单**。我们建议所有使用 NGINX 的团队：

1. **立即使用 NGINX Rift 扫描**，确认自身风险状态
2. **优先采用命名捕获组**替代未命名捕获组，零成本消除攻击面
3. **尽快升级**至官方修复版本
4. 开启 `server_tokens off`，做好纵深防御

安全无小事，防患于未然。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GqOLIEjJdyVtB1P8EBBia65utKwcBgcnrWY4gT2aPxuiabDU59FkwHpUoicsABAxUcuFiclBHC1KspACicFhFEH043w/0?wx_fmt=png)

薛定谔的安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GqOLIEjJdyVtB1P8EBBia65utKwcBgcnrWY4gT2aPxuiabDU59FkwHpUoicsABAxUcuFiclBHC1KspACicFhFEH043w/0?wx_fmt=png)

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