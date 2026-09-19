---
title: 近期漏洞简单整理复现-showdoc/Nacos/JimuReport
url: https://mp.weixin.qq.com/s/6v00MkyOxvuIUnDB7DW8gw
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:53:54.618842
---

# 近期漏洞简单整理复现-showdoc/Nacos/JimuReport

# 近期漏洞简单整理复现-showdoc/Nacos/JimuReport

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

# ShowDoc ≤ v3.9.2 RCE漏洞

## **漏洞描述**

ShowDoc v3.9.2 及以下版本存在一个未授权远程代码执行（RCE）漏洞。该漏洞源于注册接口对 `username` 参数缺乏严格的字符白名单校验，攻击者可在无需登录的情况下，将 PHP 代码写入默认位于 Web 根目录下的 SQLite 数据库文件（`Sqlite/showdoc.db.php`），随后通过直接访问该文件触发代码执行，从而完全控制服务器。

## 漏洞核心原理

该漏洞的利用依赖三个关键条件的叠加：

1. **注入点：用户名过滤不严**注册接口 `/server/index.php?s=/api/user/registerByVerify` 对 `username` 参数仅执行了 `trim()` 函数（去除首尾空白），**没有**进行字符类型或白名单校验。这意味着包含 `<?php` 等 PHP 标签的任意字符串都能被作为用户名原样写入数据库。
2. **落地点：数据库文件后缀为 `.php`**ShowDoc 默认使用 SQLite 存储数据，数据库文件路径为 `Sqlite/showdoc.db.php`。该文件被设计为 `.php` 后缀，原意是防止数据库文件被直接下载（Web 服务器会将 `.php` 文件交由 PHP 解析器处理）。这意外地为攻击者提供了让恶意代码进入 PHP 词法扫描的通道。
3. **触发点：直接访问数据库文件**攻击者通过 `GET /Sqlite/showdoc.db.php?cmd=你的命令` 请求该文件。Web 服务器（如 Nginx）匹配到 `.php` 后缀后，会将请求交给 PHP-FPM 解析。文件内的恶意用户名会被作为 PHP 代码执行。

## 影响范围与修复

影响版本：ShowDoc <= v3.9.2（默认 SQLite 部署，且注册功能开启）。

修复版本：ShowDoc v3.9.3。官方在 3.9.3 版本中对 username 增加了严格的格式正则校验（仅允许字母、数字、下划线、横线、中文）。

## 资产测绘

```
fofa:icon_hash=1969934080 || title="ShowDoc"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQhia1d42vic2kKfzpVMx1Fic2AQWjofc44Cs6OLz0NF6aahLLJJPXmukiaTSicJzrKvrqHv4S0OU16U6nBCJlWXjiagIK3zHjzdt2Lw/640?wx_fmt=png&from=appmsg)

## 漏洞复现

确定资产

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSXqHJfXmwibORoqTo8mHWXogQRSZia4mKlh4jSp77Z9wfrACvSFj7WwzdKciarHFO1yrHVW0I3273gnkIX0ibFHlGZpvibYK9nnmKI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQHP3CqCKOwReBR8L3icV6yIXvlbCoKYF78xPo1kjV4c9A02dGMWiclkllY182LUs3YhtYED6OhcTnXAAv1qBthbbIP9BOicic63zY/640?wx_fmt=png&from=appmsg)

漏洞poc

地址

```
工具地址https://github.com/Mr-xn/showdoc-registerbyverify-rce#1
工具用法# 自动打码 (推荐): 双模型识别 + 失败自动换码重试python3 exploit.py --url http://<target>:<port> --ocr --cmd id
# 手动验证码: 脚本下载验证码图片后输入, 或 --captcha 直接指定python3 exploit.py --url http://<target>:<port> --captcha XXXX --cmd id
# 交互模式python3 exploit.py --url http://<target>:<port> --ocr -i
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS2QFRvmlrcLDwop3DzJENbDJns9nMHfQJiaCPHS7VrCsRibatgxichic09vcJicZxOBhovRFN1f4UAtk1MU1fsUoibeff2jibWbPBhp4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSn4Vibbq1AVtFUPp74wpOynI0ibMe7nqBia2o00DHrKthchtIJuNJicIpicS8DQicpbhCwSs1X56DgZXiavRpCWbxYB8auLAAVeiaJkJ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT9OkVFTib5j06Vf2XX8yUib7YtMAvkRt0EgXO6gjHomKG4TbkoI9T7lGqrIsFfnGicnN9ibDZchMSibscpJltypQAB5LhwGkLdq0icI/640?wx_fmt=png&from=appmsg)

## 漏洞修复

关闭注册功能：在数据库的 options 表中将 register\_open 设置为 0。

禁止访问数据库目录：在 Nginx 或相关 Web 服务器配置中，添加规则禁止访问 /Sqlite/ 目录或 \*.db.php 文件。

迁移数据库：将 SQLite 数据库文件移出 Web 根目录（例如移到 /data/ 目录下），或考虑切换为 MySQL 数据库。

# Nacos 管理接口权限绕过漏洞

## 漏洞描述

该漏洞源于 Nacos 3.x 版本中 UserControllerV3.createUser() 等用户、角色、权限管理接口的 Secured 注解缺少 apiType 参数，而该参数默认值为 OPEN\_API，导致这些本应受管理员鉴权保护的接口错误地落入由 AuthFilter 处理、且默认关闭（nacos.core.auth.enabled=false）的普通鉴权作用域，而非由 AuthAdminFilter 处理、默认开启（nacos.core.auth.admin.enabled=true）的 ADMIN\_API 作用域，最终使攻击者可在未授权状态下直接调用这些管理接口创建高权限管理员账户，完全接管 Nacos 服务端。

### 受影响接口

| 接口 | 路径 | 方法 |
| --- | --- | --- |
| 创建/删除用户 | `/nacos/v3/auth/user` | POST / DELETE |
| 创建/删除角色 | `/nacos/v3/auth/role` | POST / DELETE |
| 创建/删除权限 | `/nacos/v3/auth/permission` | POST / DELETE |

### 漏洞危害

攻击者可在未授权状态下创建管理员账户，进而完全接管 Nacos 服务端，具体包括：

* 窃取所有微服务配置信息（含数据库连接字符串、API 密钥等敏感凭证）
* 修改配置导致业务中断
* 创建后门账户实现持久化
* 利用获取的凭证横向移动攻击企业内网其他系统

## 影响范围

### 3.1 受影响版本

**3.0.0 <= Nacos <= 3.2.3**

## 资产测绘

```
FOFA语句:app="nacos" && port="8848"body="HTTP Status 404 – Not Found" && port="8848"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRYdS9O3n58QWSoVP0WHah2YOnZicb1tiaK60H8Aj4WSCZ8iaJCD01LVYYdTA8oIdPtia6ib1ft0h6oA1ibgEmyqNr46fVo04ManUgVI/640?wx_fmt=png&from=appmsg)

## 漏洞复现

资产确定

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTTszqASmbe8jTMAMqKm9qYMlmia75DwhyLyibZia4dZc7LySQEH40o2xYmjk1dZQQr4kD6MDzp1KjicAP44iaY84r9cHRy3xqvO0rg/640?wx_fmt=png&from=appmsg)

```
工具地址https://github.com/TlyHj/nacos-v3-attack
工具用法python3 poc.py                                # 默认打 127.0.0.1:8848python3 poc.py --host 10.0.0.5 --port 8848python3 poc.py --check-only                   # 只读探测，不写入python3 poc.py --no-cleanup                   # 打完不删注入的账号
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboROQnHlPm6Rc31fg6xwt2jAA9GgE3ln7sRp0icPLScRI5mZD81YcYaGn3YrNlygztWBia53CxDFc2NUjbGbFuauVjAobSoGJj1Lg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQZww2LLdEgAG7kJgicZORS2gssvyCLHbkSVdVj7F50PPzbC1SiayRLsAb7F4aFldSbDEicdvzTd6PFh6VGoLKKQhM4HddhibGbyia4/640?wx_fmt=png&from=appmsg)

## 漏洞修复

官方已在 Nacos 3.2.4 版本中修复此漏洞。修复方式为在受影响接口的 @Secured 注解中补上 apiType = ApiType.ADMIN\_API。

# JimuReport 2.5.1 未授权RCE漏洞

## 漏洞描述

该漏洞源于 JimuReport（积木报表）v2.5.1 自动导出功能在身份校验与表达式执行两方面存在安全缺陷的叠加。

一方面，导出接口 /jmreport/auto/export/python/plugin 被设计为免登录访问，但其签名校验使用了硬编码的固定密钥。

攻击者可直接利用该密钥伪造任意有效的 X-Sign 请求签名，完全绕过身份认证。

另一方面，该接口在导出报表时会遍历请求中的查询参数值，并将其送入 Aviator 表达式引擎执行。代码未对以“=”开头的参数做任何过滤或白名单约束，攻击者可利用 Aviator 沙箱逃逸实现任意 Java 反射调用，最终在无任何凭据的情况下达成远程代码执行。

## 漏洞影响

影响版本： JimuReport = 2.5.1（且依赖的 Aviator 版本 < 5.4.4）。

## 漏洞危害

完全控制服务器：以应用权限执行任意系统命令，实现服务器沦陷。

数据泄露：访问、修改或删除服务器上的敏感数据。

持久性后门：在服务器上安装后门，以便未来随时访问。

服务中断：破坏服务器正常运行，导致服务瘫痪。

## 资产测绘

```
FOFAy语法icon_hash=1695246976 || title="欢迎使用积木报表"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTkk1fI5qVRgwPDdUD4u4ISwMFdwR18kvEvMpW2XhxO1YnCoMPdHKEibSBMNuFpIqLxksFfPaBMpx12Uzso6d4XcljQ4GCw9Q4o/640?wx_fmt=png&from=appmsg)

## 漏洞复现

资产确定

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTrDrUSMvOibYaOCpicndwe3db2icdbDHEjBv7Q5Nsob6YQBIGlaxphNuen6U3UGH5o1WBUDEnrOdW0zupBt7jeyz7m8ccibjNHL6A/640?wx_fmt=png&from=appmsg)

漏洞复现

这个漏洞如果不好复现，可以指定目标，让ai使用这个脚本来搞，或者改改脚本都可以。

```
工具地址https://github.com/mhtsec/jimureport-2.5.1-rce
工具使用
python3 exploit.py -t http://target:8085 -m exec -c 'id'      # RCE 执行命令并回显(默认 id)python3 exploit.py -t http://target:8085 -m read -p /etc/passwd      # 任意文件读python3 exploit.py -t http://target:8085 -m write -p /tmp/x -d hello # 任意文件写并读回验证python3 exploit.py -t http://target:8085 -m probe                    # 环境探测python3 exploit.py -t http://target:8085 -r <reportId> -k <param>    # 指定回显报表与参数名
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTnvibvsPibTMKylzp0vaHQ6hSd4icia0mtAxCOftfSIqJ8MvqywbYIV5nHgOcrPGSgWL1Ihu2Rj2FlPibntlUCGaWTP1OPjKcbVT3k/640?wx_fmt=png&from=appmsg)

# 白帽集市简单介绍

## 白帽集市：网安人的“海鲜市场”食用指南

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRHC3icUM6DB5c9VzJ4tXcWPcsjF7wtHV1xZRePOu5n3zNVQfNfekqYicBCr7Qfk5rKPxfQIrTg1TqL4JvsibL1yiajMYbc2NMejl4/640?wx_fmt=png&from=appmsg)

### 一、它是什么？为什么会出现？

白帽集市是 FreeBuf 知识大陆 APP 内打造的一个**面向网络安全行业的垂直交易平台**，官方定位是“网安人自己的海鲜市场”。

**它要解决的痛点很具体：**

过去，白帽子们把工具、课程、AI Agent、技术资料和安服资源发到微信群、朋友圈甚至二手平台，原因很简单——**除了这些地方，几乎没有更好的选择**。

但问题也很明显：

* 真正有需求的买家很难找到匹配商品
* 卖家也很难触达精准用户
* 沟通靠私聊，交付靠信任
* 既缺少展示机会，也缺少统一的服务保障

官方的判断是：**不是网安行业没有需求，而是一直缺少一个真正属于网安人的“海鲜市场”。**

所以白帽集市的目标很明确：让买家更容易找到商品，让卖家更容易找到用户，让每一位网安人的能力都能持续创造价值。

### 二、卖家能做什么？可以卖什么？

**与网络安全相关的数字商品和技术服务，都欢迎上架。**

官方给出的品类包括：

| 品类 | 具体例子 |
| --- | --- |
| **工具** | 扫描器、插件、自动化脚本、开发工具 |
| **知识资料** | 漏洞分析、代码审计笔记、CTF Writeup、SRC 实战经验 |
| **AI 相关** | AI 工具、安全 Agent、Prompt、自动化工作流 |
| **技术资源** | PoC、规则库、字典、模板、指纹库 |
| **课程与服务** | 视频课程、安全咨询、应急响应、培训陪跑 |

**卖家为什么选这里？**

核心原因是**用户精准**。FreeBuf 知识大陆的用户本身就是白帽、安全工程师、安全团队和企业用户，卖家面对的不再是二手平台上形形色色的买家，而是真正有需求的目标用户。

**费用方面：**

* 平台服务费 **0%**
* 仅收 **0.6%** 支付通道手续费
* 提现无上限，每周可提现到账

### 三、买家能做什么？

买家主要是**有实战需求的白帽子、SRC 漏洞猎人、安全从业者**。

**核心动作：**

* **买工具提效**：扫描器、插件、自动化脚本等实战工具
* **买知识资料**：漏洞分析、代码审计笔记、CTF Writeup、SRC 实战经验
* **买 AI 工具与安全 Agent**：Prompt、自动化工作流等
* **买技术资源**：PoC、规则库、字典、模板、指纹库
* **买课程与服务**：视频课程、安全咨询、应急响应、培训陪跑
* **看种草笔记再决定**：平台支持“种草笔记”和“种草电报”两种内容形式，都能挂载商品链接，买家可以先看推荐再下单

### 四、平台有哪些扶持政策？

**第一批卖家扶持计划：3 万元补贴**

官方明确表示：“任何一个生态，都离不开第一批创业者。”所以准备了 **3 万元扶持计划**。

**流量扶持：**

* 商品有机会进入平台推荐池
* 获得首页推荐、品类专区曝光
* 官方社群推荐、专题活动、直播推荐
* FreeBuf 主站流量扶持

**限时入驻福利：**

* 平台服务费 0%，仅收 0.6% 支付通道手续费
* 开店最高领取 **100 元**红包
* AI 工...