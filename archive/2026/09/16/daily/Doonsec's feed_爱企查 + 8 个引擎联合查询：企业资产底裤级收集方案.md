---
title: 爱企查 + 8 个引擎联合查询：企业资产底裤级收集方案
url: https://mp.weixin.qq.com/s/pRsQR9vc4my-r1rvLa918Q
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:56:46.000725
---

# 爱企查 + 8 个引擎联合查询：企业资产底裤级收集方案

# 爱企查 + 8 个引擎联合查询：企业资产底裤级收集方案

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# AsamF：一站式资产收集工具

AsamF 是一款集成多平台数据源的安全资产收集工具，支持 Fofa、Hunter、Quake、Zoomeye、Shodan、爱企查、Chinaz、0.zone 及 subfinder，帮助安全研究员快速完成企业资产测绘与信息收集。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFzyc1CfHN1mbTc2cDc2t91UoUTsqAApp9qphnPgEUmIvSWzFIKicOF6AZoMp1ibl1x5B8WIyJG6uapxYbd2icGZnWQjv6EpCU7dY/640?wx_fmt=png&from=appmsg)

## 快速配置

配置文件位于 `~/.config/asamf/config.json`，支持录入多平台 API Key。建议按阿拉伯数字命名键值，便于通过 `-fk`、`-zk` 等 flag 快速切换。所有命令及子命令均支持短命令形式，提升操作效率。

查询结果自动保存至 `~/asamf/` 目录。

---

## 核心功能模块

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFFnzHzEeicibcmVVicyUia5zKsZfcZB8WgvjK7CGtYepbaNodHkUBEVDwyYic4RvAONRQcgDMUL9wC9JZNicrdAy0sicDdBiax8KghYeMA/640?wx_fmt=jpeg&from=appmsg)

### 爱企查（`a`）

企业信息一站式收集，支持企业名反查 URL、主机、备案、控股关系、分支机构，并联动子域名、信息系统、泄露邮箱、人员信息、App 资产、目录及代码收集。

* 单企业深度查询：`AsamF a cn -q 公司名`
* 批量企业 URL/IP 提取：`AsamF a cnf -q target.txt`
* 按控股比例递归：`AsamF a cn -q 公司名 -p 100`

### 网络空间搜索引擎

| 平台 | 命令 | 核心功能 |
| --- | --- | --- |
| Fofa | `f` | 账户信息、icon 搜索、主机搜索、聚合统计、批量查询 |
| Hunter | `h` | 快速查询（注：`info` 子命令会扣除 10 积分） |
| Quake | `q` | 账户信息、蜜罐识别（`hy`），按会员等级返回 500-10000 条数据 |
| Zoomeye | `z` | Web 应用、子域名、主机搜索 |
| Shodan | `s` | 端口、主机信息、DNS 解析/反向、查询标签、漏洞及 facets 统计 |

### 联合查询（`u`）

无需记忆各平台语法，内置 domain、app、server、port、host、title、body 字段，直接输入内容即可跨平台联合检索： AsamF u d -q baidu.com    # 域名

AsamF u a -q apache       # 应用

AsamF u p -q 8080         # 端口

![](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFHGJrnxM2HkA9RoicUYZcZ8MWblOAKuOfeWCiaF4fRCEXtAV58G5ux2pVspKHlQ3IZfoU9XM8NN5zyrNj3VJWI5deC47TO7OzE6g/640?wx_fmt=jpeg&from=appmsg)

### 其他工具

* **Chinaz（`c`）**：IP 归属、ICP 备案、权重、Whois 及反查
* **子域名收集（`sd`）**：`AsamF sd -q baidu.com`，支持被其他模块联动调用
* **本机 IP（`myip`）**：快速获取出口 IP

---

## 典型工作流

1. 配置多平台 Key 至 `config.json`
2. 通过 `info` 子命令验证 Key 有效性（如 `AsamF f info -fk 1`）
3. 以 `Union` 命令快速定位目标资产轮廓
4. 针对特定平台深度挖掘（Fofa 主机搜索、Quake 蜜罐检测等）
5. 结合爱企查完成企业关联资产梳理
6. 结果自动归档至 `~/asamf/`，便于后续分析

---

## 获取帮助

执行 `AsamF -h` 或各模块短命令（如 `f -h`、`a -h`）查看详细用法。所有子命令均支持 `-h` 获取上下文帮助。

---

*注：各平台数据返回量受账户等级限制，建议根据实际需求合理配置多 Key 轮换。*

### 项目地址

```
https://github.com/Kento-Sec/AsamF
```

## 低价出售安全证书不限于cisp、pte等cnvd、建了项目群，想进群的请回复进群

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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