---
title: NGINX 漏洞预警：18 年老洞可 RCE，PoC 已公开
url: https://mp.weixin.qq.com/s/s4fizQHJgSEMm2p-g0UEwg
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:29.193317
---

# NGINX 漏洞预警：18 年老洞可 RCE，PoC 已公开

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J8Ev2iczlWG0MW1UV4yLd3eeYUiaibzYapyGCmIKTibKRGQQFJGQ2siaSk0dttAXjDTpsnnrvjibPaLgWnuRxVOlnhqCFgO3PsxZmjvKJ8icxFicYRw/0?wx_fmt=jpeg)

# NGINX 漏洞预警：18 年老洞可 RCE，PoC 已公开

猎户攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

5月13日，安全研究机构 DepthFirst 的自动化漏洞扫描系统一次性发现了 NGINX 的 4 个安全漏洞。其中最严重的 CVE-2026-42945（NGINX Rift） 影响范围横跨 0.6.27 到 1.30.0，存在了将近 18 年，官方 PoC 已公开。

## 漏洞清单

| CVE | 严重度 | 模块 | 影响 |
| --- | --- | --- | --- |
| CVE-2026-42945 | 🔴 Critical 9.2 | ngx\_http\_rewrite\_module | 堆溢出 → RCE/DoS |
| CVE-2026-42946 | 🟠 High 8.3 | ngx\_http\_scgi\_module / uwsgi\_module | ~1TB 内存分配 → worker 崩溃（DoS） |
| CVE-2026-40701 | 🟡 Medium 6.3 | ngx\_http\_ssl\_module | TLS 关闭后 OCSP DNS use-after-free |
| CVE-2026-42934 | 🟡 Medium 6.3 | ngx\_http\_charset\_module | UTF-8 跨缓冲区越界读（off-by-one） |

修复版本：**1.30.1+**（稳定分支）/ **1.31.0+**（主线）

## 重点分析

**CVE-2026-42945（NGINX Rift）—— 堆溢出可RCE**

这是本次最严重的漏洞。当配置中 rewrite 的替换串包含 `?`，且后续通过 `set`/`if`/`rewrite` 引用了正则捕获组（如 `$1`、`$2`）时，攻击者发送特制 URI 即可触发堆溢出。可导致 worker 进程崩溃，在绕过 ASLR 的条件下可实现远程代码执行。

受影响配置示例：

```
rewrite ^/old/(.*)$ /new?param=$1;    # 替换串含 ? 且引用了 $1
set $my_var $1;                        # 引用捕获组
```

**CVE-2026-42946 —— SCGI/uwsgi 内存耗尽**

触发后可导致约 1TB 的内存分配，直接打挂 worker 进程。所有使用 SCGI 或 uWSGI 后端的部署均受影响。

## PoC / 利用脚本

CVE-2026-42945 的 PoC 已公开：

* • 官方 PoC：https://github.com/DepthFirstDisclosures/Nginx-Rift

> **关于 PoC 的实际利用能力说明：** 该 PoC 主要在 ASLR 关闭的环境（如 DepthFirst 提供的 Docker 测试环境）下能稳定实现 RCE。在真实生产环境（默认开启 ASLR 的 Linux 系统）上，大概率只能实现可靠的 DoS 崩溃，完整 RCE 需要额外技巧。**请仅在自己可控的测试环境中使用，严禁用于任何未经授权的服务器，否则属于违法行为。**

## 排查方法

**第 1 步：资产清点 — 确认 NGINX 版本**

```
# 本地最准确检查
nginx -v
nginx -V

# 远程通过 Header 检查
curl -sI https://your-domain.com/ 2>/dev/null | grep -i "^Server:"

# 批量扫描（推荐）
while read host; do
  echo -n "$host | "
  curl -skI --max-time 5 "https://$host" 2>/dev/null | grep -i "^Server:" || echo "无法访问或 Server 头已隐藏"
done < host_list.txt
```

判定标准：

* • 版本在 **0.6.27 ~ 1.30.0** 之间（含 NGINX Plus R32~R36）→ **受影响，立即升级**
* • 版本 **≥ 1.30.1** 或 **≥ 1.31.0** → 已修复

**第 2 步：模块与编译选项检查**

```
# 查看已编译模块
nginx -V 2>&1 | tr ' ' '\n' | grep --color=never -E 'module|http_rewrite|http_scgi|http_uwsgi|http_charset|http_ssl'
```

**第 3 步：配置触发条件检查（最核心！）**

```
# 查找含 ? 的 rewrite + 匿名捕获组
grep -rnE 'rewrite\s+.*\?.*\$[0-9]' /etc/nginx/ --include="*.conf"

# 查找所有匿名捕获组使用
grep -rnE '\$([1-9][0-9]?)' /etc/nginx/ --include="*.conf"

# 检查 SCGI/uWSGI（CVE-2026-42946）
grep -rnE 'scgi_pass|uwsgi_pass' /etc/nginx/ --include="*.conf"
```

**第 4 步：日志异常检查**

```
# worker 崩溃记录
grep -E "exited on signal|segfault|signal 11|worker process" /var/log/nginx/error.log | tail -30

# 可疑 URI 请求
grep -E "(\+|%26|%25)" /var/log/nginx/access.log | tail -50
```

## 修复建议

**首选：立即升级 NGINX**

```
# CentOS / RHEL
yum update nginx

# Ubuntu / Debian
apt update && apt install nginx

# Docker
docker pull nginx:1.31.0

# 验证
nginx -v   # 确保 >= 1.30.1
```

**临时缓解（无法立即升级时）**

针对 CVE-2026-42945，最有效的办法是把匿名捕获组改成 **named captures**：

```
# 推荐写法
rewrite ^/users/(?<user_id>[0-9]+)/profile/(?<section>.*)$ /profile.php?id=$user_id&tab=$section last;
```

---

**参考链接：**

* • DepthFirst 官方技术分析https://github.com/DepthFirstDisclosures/Nginx-Rift
* • F5 安全公告 K000161019https://my.f5.com/manage/s/article/K000161019
* • NGINX 安全公告https://nginx.org/en/security\_advisories.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ic56Y1PMq5MXZqt7tQYtI8F8JSmqo65GeapTpQWHVJBBdtOUiaibVZPx3p9hibUFaQRLIWtbScgReERUmeDBz6GmJg/0?wx_fmt=png)

猎户攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ic56Y1PMq5MXZqt7tQYtI8F8JSmqo65GeapTpQWHVJBBdtOUiaibVZPx3p9hibUFaQRLIWtbScgReERUmeDBz6GmJg/0?wx_fmt=png)

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