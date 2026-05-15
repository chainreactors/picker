---
title: 18年积弊：NGINX脚本引擎堆缓冲区溢出可致远程代码执行
url: https://mp.weixin.qq.com/s/Z-hV8A4XQ0G5OoN1ptEsNw
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:49:41.960011
---

# 18年积弊：NGINX脚本引擎堆缓冲区溢出可致远程代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOqicdFSPctQMq5ZuCiax33H2BcC3jibknwDsHfa816eyLibThrBclG8z258iaVbwicpG25DYAhr1Voqr4KQkY6bRzNStWTaAS3hRobR98/0?wx_fmt=jpeg)

# 18年积弊：NGINX脚本引擎堆缓冲区溢出可致远程代码执行

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 漏洞概述

2026年初，安全研究组织depthfirst通过其自动化代码审计系统对NGINX源代码进行深度扫描，在六小时内识别出五个安全缺陷，其中四个已获得NGINX官方确认并分配CVE编号。这一发现揭示了NGINX核心组件中存在的严重内存损坏问题，攻击者可利用这些漏洞实现远程代码执行。

**关键CVE清单：**

| CVE编号 | 严重性 | 漏洞类型 | 影响组件 |
| --- | --- | --- | --- |
| CVE-2026-42945 | Critical (9.2) | 堆缓冲区溢出 | ngx\_http\_rewrite\_module |
| CVE-2026-42946 | High (8.3) | 过度内存分配 | ngx\_http\_scgi\_module, ngx\_http\_uwsgi\_module |
| CVE-2026-40701 | Medium (6.3) | 释放后使用 | ngx\_http\_ssl\_module |
| CVE-2026-42934 | Medium (6.3) | 越界读取 | ngx\_http\_charset\_module |

CVE-2026-42945作为该批次中最严重的漏洞，CVSS评分高达9.2，漏洞代码于2008年引入，跨越近18年未被发觉，影响范围覆盖NGINX Open Source 0.6.27至1.30.0版本以及NGINX Plus R32至R36版本。该漏洞的利用门槛较低，在禁用ASLR的环境中已验证可实现可靠的远程代码执行。

## 技术根因分析

### 脚本引擎两遍处理机制

NGINX配置中的rewrite指令和set指令是构建API网关和请求路由的核心组件。rewrite指令允许通过正则表达式修改请求URI，当替换字符串包含问号时，NGINX将问号后的内容作为查询字符串处理。set指令则用于将值赋给自定义变量，支持捕获组的引用，这两个指令的组合使用极为普遍。

NGINX内部通过脚本引擎（script engine）优化这些操作。在配置解析阶段，脚本引擎将这些指令编译为操作序列；在运行时，通过两遍（two-pass）机制执行：首先计算最终字符串的总长度，从内存池分配精确大小的缓冲区；随后执行复制操作将实际数据写入新分配的缓冲区。这种设计避免了多次小额内存分配的性能开销，但要求两遍之间的引擎状态保持一致。

### is\_args标志传播失效

漏洞根因位于`src/http/ngx_http_script.c`。当rewrite指令的替换字符串包含问号时，函数`ngx_http_script_start_args_code`会将主引擎的`e->is_args`标志设置为1：

```
void ngx_http_script_start_args_code(ngx_http_script_engine_t *e) {
    e->is_args = 1;
    e->args = e->pos;
    e->ip += sizeof(uintptr_t);
}
```

该标志在后续处理中**从未被重置**。当后续的set指令引用正则捕获组时，触发`ngx_http_script_complex_value_code`函数执行长度计算。此时，该函数创建一个**完全清零的子引擎**：

```
void ngx_http_script_complex_value_code(ngx_http_script_engine_t *e) {
    ngx_http_script_engine_t le;
    ngx_memzero(&le, sizeof(ngx_http_script_engine_t));
    le.ip = code->lengths->elts;
    // ...
}
```

由于子引擎被初始化为全零，`le.is_args`为0。长度计算函数`ngx_http_script_copy_capture_len_code`据此判断不需要进行URL转义，计算出的长度是原始捕获字节数。然而在实际复制阶段，主引擎的`e->is_args`仍为1，复制函数调用`ngx_escape_uri`进行URL转义，每个可转义字节扩展为3字节（%XX格式）。**长度计算与实际写入数据量之间的不匹配，导致堆缓冲区溢出。**

### 攻击向量与利用链

漏洞触发需要同时满足两个条件：rewrite指令的替换字符串包含问号，且后续存在引用捕获组的set指令。攻击者可通过构造恶意请求路径，利用截断的正则表达式捕获未转义的路径字符。

depthfirst已公开完整的概念验证代码，验证了以下攻击路径：

1. 攻击者通过跨请求堆风水（heap feng shui）技术操控堆布局
2. 利用POST body喷洒（spraying）破坏相邻的`ngx_pool_t`结构
3. 将cleanup指针重定向至伪造的`ngx_pool_cleanup_s`结构
4. 在内存池销毁时触发system()调用，获得远程shell 在Ubuntu 24.04.3 LTS环境中，该概念验证代码已验证可行。

## 其他关联漏洞

### CVE-2026-42946：SCGI/UWSGI模块过度内存分配

SCGI和UWSGI模块在解析上游状态行时存在状态不匹配问题。当状态行读取不完整时，跨缓冲区的指针减法运算产生约1TB的键长度，导致worker进程崩溃。

### CVE-2026-40701：SSL模块释放后使用

TLS连接关闭时，若异步OCSP DNS解析尚未完成，上下文池被销毁但解析器请求未被取消。后续DNS计时器回调将对已释放的内存指针进行解引用。

### CVE-2026-42934：Charset模块越界读取

Charset模块在处理跨代理缓冲区边界的不完整UTF-8序列时存在off-by-one错误，导致长度状态损坏，计算出负的源偏移量，在分配的上游缓冲区前读取2字节。

## APT威胁态势评估

### 利用可能性分析

CVE-2026-42945作为高严重性远程代码执行漏洞，具备以下APT利用特征：

* **漏洞成熟度**：漏洞代码存在18年，利用思路清晰，公开的概念验证代码可直接适配
* **攻击面广泛**：NGINX作为全球使用最广泛的Web服务器之一，占据约三分之一的市场份额，部署量巨大
* **利用门槛中等**：需要特定的配置组合（rewrite含问号 + set引用捕获组），但目标配置广泛存在于API网关场景

### 威胁行为体关注点

国家级APT组织通常将此类基础组件漏洞作为：

* **Initial Access阶段**：通过Web边界设备获得内网立足点
* **Lateral Movement载体**：攻陷Web服务器后进一步横向移动至后端系统
* **供应链投毒潜力**：若攻击者同时掌握构建环境，可进一步扩展影响范围

### 战术技术演变预测

根据MITRE ATT&CK框架，该漏洞利用涉及以下技术：

* **T1190**：利用面向公众的应用组件
* **T1059.003**：命令和脚本解释器（通过成功利用获得shell）
* **T1543.003**：创建或修改系统进程（维持持久化）

预计后续将出现针对该漏洞的自动化利用工具，降低攻击门槛。

## 防护建议

### 紧急处置

1. 立即统计境内部署的NGINX版本，识别0.6.27至1.30.0版本（开源版）及R32至R36版本（Plus版）的部署实例
2. 检查现有配置中是否包含rewrite指令含问号且后续存在set指令引用捕获组的组合模式
3. 在Web应用层之前部署WAF规则，检测异常HTTP请求路径特征

### 缓解措施

1. 升级至NGINX最新稳定版本（1.30.0+），确认供应商已发布的补丁已应用
2. 启用ASLR、DEP等系统级内存保护机制，增加利用难度
3. 以低权限账户运行NGINX worker进程，限制成功利用后的影响范围
4. 实施网络分段，限制Web服务器与后端关键系统的直接通信

### 监控策略

1. 部署内存完整性监控工具，检测heap overflow特征行为
2. 监控Web服务器进程异常退出和资源消耗异常
3. 建立NGINX配置变更的完整性校验机制

## 结论

CVE-2026-42945代表了基础组件中长期潜伏漏洞的典型风险模式。该漏洞根因在于2008年引入的代码设计缺陷，在特定配置组合下可被触发导致堆缓冲区溢出。鉴于NGINX的广泛部署和漏洞的严重性，APT组织极有可能将其纳入武器库。

建议安全运营团队将此次披露作为优先级事件进行响应，在确认受影响资产范围后尽快推进修复工作。考虑到公开漏洞利用代码的存在，**修补窗口期应尽可能压缩至72小时内**。

## IOC指标

| 类型 | 值 | 说明 |
| --- | --- | --- |
| CVE-2026-42945 | Critical (9.2) | ngx\_http\_rewrite\_module堆溢出 |
| CVE-2026-42946 | High (8.3) | SCGI/UWSGI模块内存分配问题 |
| CVE-2026-40701 | Medium (6.3) | ngx\_http\_ssl\_module UAF |
| CVE-2026-42934 | Medium (6.3) | ngx\_http\_charset\_module越界读取 |
| Affected Version | NGINX 0.6.27 - 1.30.0 | 开源版受影响范围 |
| Affected Version | NGINX Plus R32 - R36 | Plus版受影响范围 |

##

## MITRE ATT&CK技术映射

| ATT&CK技术 | ID | 说明 |
| --- | --- | --- |
| Exploit Public-Facing Application | T1190 | 利用面向Internet的Web服务器漏洞 |
| Command and Scripting Interpreter | T1059.003 | Unix Shell，用于成功利用后执行命令 |
| Create or Modify System Process | T1543.003 | 持久化机制 |

##

## 参考来源

* https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability
* https://github.com/DepthFirstDisclosures/Nginx-Rift

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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