---
title: EDU攻防实战：对山东某高校的线下渗透+近源复盘②
url: https://mp.weixin.qq.com/s/aMU_qWmaiwiw-GTBTSWW0w
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:05.887914
---

# EDU攻防实战：对山东某高校的线下渗透+近源复盘②

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQqsvERR7XFLqNJkFG4nphH60UhSBUiaiaUC7NaaSJDgdg53wgfoWRmLC7M4b44yfzRFt2X6F224C7kK2iaSiakCmMhmAhCj4CLj2NQ/0?wx_fmt=jpeg)

# EDU攻防实战：对山东某高校的线下渗透+近源复盘②

原创

Thanatos
Thanatos

星宇Sec

![]()

在小说阅读器中沉浸阅读

本次受邀加入专项安全测试团队，前往济南某高校开展线下内网渗透授权演练，全程在学校安全部门监督下合规推进，所有操作均获得校方正式授权，无任何违规越界行为。

本次渗透测试突破常规内网检测范围，从校内内网打点切入，逐步横向拓展、纵向深挖，最终成功突破外网边界，不仅发现该校智慧安防平台等核心系统的大量高危漏洞，更意外排查出外网关联数据库中泄露了其他学校的相关敏感数据，隐患范围远超预期。

为保护校方信息安全及相关敏感数据，本文所涉及的校园内网拓扑、设备信息、漏洞详情等全部进行脱敏处理，渗透过程中临时下载的各类数据，已在测试结束后第一时间全部彻底删除，不留存任何相关缓存及备份。

考虑到内容的完整性和可读性，以下直接附上本次线下内网渗透的脱敏报告（部分内容由AI整理）

---

# 济南某高校图书馆服务平台漏洞报告（脱敏版）

## 1. 测试说明

* 测试性质：经授权安全测试
* 测试对象：济南某高校图书馆服务平台
* 目标地址：`https://10.x.x.x`（已脱敏）
* 涉及产品：XXXXXX有限公司XX图书馆服务平台
* 涉及版本：`VX.X.X.X` 及以下版本（需厂商进一步确认）

## 2. 风险概述

测试发现该平台存在批量敏感信息泄露和SQL注入风险。核心问题是后端接口对输入参数过滤不足，导致攻击者可通过构造异常请求绕过正常查询边界，读取大量读者数据；在部分接口中还可触发 SQL 注入行为，进一步放大数据库被控制的风险。另外近源测试结果也发现了敏感信息泄露等漏洞。

## 3. 影响范围

* 济南某大学当前部署实例
* XXXXXX有限公司XX图书馆服务平台 `VX.X.X.X` 及以下版本其他机构（存在同类风险可能）

## 4. 基础复现路径

1. 访问登录页：`https://10.x.x.x/XXXXX/login?redirect=%2Fhome`。
2. 尝试使用弱口令及社工字典进行账号登录。
3. 进入“近期工作 -> 流通业务”。
4. 点击“读者信息查询”，进入目标功能页并开启抓包工具（Burp Suite）。

![step-01-login-page](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQpKwByjoETDxFgldCtciapfJBTGsqCsfHNmKZbmC1Mw1BL275Knlr70m7BAmelNKZGJzcbVu9hSC38Cc53GOddKp29H2j5hiabrg/640?wx_fmt=png&from=appmsg)

step-01-login-page

![step-02-circulation-module](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQric7UjyshyhPQtKczB1cQZsvjU7vM2diaaa256oOpDsbPtelMRXYhbjHGEset9rTqZjj0iaxPmjt9wxicJfrdYicMEmuMXnPyxBdgU/640?wx_fmt=png&from=appmsg)

step-02-circulation-module

![step-03-reader-query-page](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqEJw5zc3EPKj3PcNiavB2HtIzGDGTD4lBDNN7t6b0Vd4TOzJk02iaeb51dQMdvtuMj8EoUwW0PnkXtEBpdVxY7NNsLicE4mQySAw/640?wx_fmt=png&from=appmsg)

step-03-reader-query-page

## 5. 信息泄露漏洞明细

以下 10 个接口的复现逻辑高度相似：先触发正常查询请求，再将请求体中的 `operator` 参数追加单引号（如 `=` 改为 `='`，`<=` 改为 `<='`），重放后可返回超出授权范围的数据。

### 5.1 漏洞 1：读者基础信息泄露

* 接口：`/XXXXX/XXX/patron_info_query/all/list`
* 影响：返回约 `18217` 条记录，字段包含用户 ID、密码、姓名、学工号、身份证号等高敏感信息。

![leak-01-request](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoPRj7jO7ib7Ur39snyZW9YibXboqw82u9G1ZXrBXic0BeB2SekNT3OUxM1tmaJNsV5kC6qjtYldB6TupKHK2iaqIWIYjTib0MKulX4/640?wx_fmt=jpeg&from=appmsg)

leak-01-request

![leak-01-response](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqEEdV6z9SoorPTn62oiaJz7E43ULZOrXdiaHqPaH4oPyVsOnXEQ6zWx3Vaqf8Y5iaVXibhsHc7AsRzpUOERibJicgaBQDvjWeJhH3vI/640?wx_fmt=png&from=appmsg)

leak-01-response

### 5.2 漏洞 2：书刊借阅记录泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/loan/normal/list`
* 影响：可批量获取借阅记录等敏感业务数据。

![leak-02-request](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQqHfy4Vo1Sr0B2CXUonVNxM2ErrNNNDj3KE9YI5VxRmibrkCYKSxQHulTm8pKooPaz3DBgsTicoCasRFT4Lzr4m6BIiapAPDOaVSo/640?wx_fmt=png&from=appmsg)

leak-02-request

![leak-02-response](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqXl9bLuhjKUobjjVPxkR6vepI6WT49vGC8BoN5picC5icLJH5wwiaF4XxxBnmDpy2Licj3IO1gUZWgHf8poRZk176kEE1jcQ0O9GM/640?wx_fmt=jpeg&from=appmsg)

leak-02-response

### 5.3 漏洞 3：借阅超期记录泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/loan/overdue/list`
* 影响：可批量获取超期借阅数据（单条记录字段较多）。

![leak-03-request](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQq6PC7BV85ZUB9yHJcY4ibl8dxQRX0Tpyflk9jGD5Cdcx7Lxkq8jaEicSY2Y3o8L37nzTIkian2NRE4qHWCmiapT06MKtibJT2AUQp0/640?wx_fmt=png&from=appmsg)

leak-03-request

![leak-03-response](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQofDB99xaAGgMzmEQanKMa8ywwwErcWAjrjmCQYPHlAu4DFSahsaEZ083yIQPSfhyxSMniauRPFKzk1ewBb5nhCM5JkmtbSD03A/640?wx_fmt=png&from=appmsg)

leak-03-response

### 5.4 漏洞 4：借阅历史记录泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/loan/history/list`
* 影响：可读取完整历史借阅信息。

![leak-04-request](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQpJr96ibwmjoHMdErria1licKjOmnnS6g2QCEzYzhYhVKpV1V2cYK0ZKgAOn4TWudIcZ7EmQhniawN6CA8jelZbutxqyzbSRevCSvI/640?wx_fmt=png&from=appmsg)

leak-04-request

![leak-04-response](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQo1q4SCW5biakAficDnKp0IOTlC2N4LlmTicoXA5qOicibry7tcEbnYgxLUR7sepXjwZcMCE0JaX52MfQRDlmEBwicicLSpziaQ36gHbtI/640?wx_fmt=jpeg&from=appmsg)

leak-04-response

### 5.5 漏洞 5：滞纳金信息泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/fine/list`
* 影响：可批量读取滞纳金相关信息。

![leak-05-request](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQpYYiaZQdCNLaibb9XiaibMPrdqfPlEJyS5wf1dCOnYIQekCFMqMI7ZwCgL6lx6fkl6CBpcaiahu7iaSxEE9pW0STicbbwhRAhvjVwlVg/640?wx_fmt=png&from=appmsg)

leak-05-request

![leak-05-response](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQoOBNRQl71FMdCgC3AoZyCuBgibZWWa8UavLdLfWibHboHmPfD9UclQOXlUKMOjAAJRzxGg9mGCXqCC73Mhia4FTtE4pAtBsaEqSo/640?wx_fmt=jpeg&from=appmsg)

leak-05-response

### 5.6 漏洞 6：预约信息泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/preg/list`
* 影响：可批量读取书刊预约信息。

![leak-06-request](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQoqtJiaeHXv0KNQTSgMuAIEIVA5FYoqoFjiaANwWcDxrfrqwMmArDSWciatZicTNe9LsqolPKjiaEuV8yjTicfImyPSz4Pp9ZM3UMvBQ/640?wx_fmt=png&from=appmsg)

leak-06-request

![leak-06-response](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQr97E3b4vLUTW94zcSM33Nyibtl3Hia5iac54Iia4XK7XV9h5MtMxdI3pO6phtlm145ynv04FVOAYqCdqV5ib8x0GMYsT9Z6CtImOSU/640?wx_fmt=jpeg&from=appmsg)

leak-06-response

### 5.7 漏洞 7：预约到馆信息泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/preg/arrival/list`
* 影响：可批量读取预约到馆明细。

![leak-07-request](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrXFHGiawIib7Afx8cjH3vnXf2TA8PsvlBXOTJJu5jOZkC4ibSOB26uZqw3e72l91Yic1fFOZSUtFzibSc82K11qkJ168VwpKvQXB50/640?wx_fmt=png&from=appmsg)

leak-07-request

![leak-07-response](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoHmxfIGIJicfQROOZoQoo0VadricyAmJziaAiaGs7IDgq81IXdNSmnAEuauNOchqfMWukAYBrZ3zic9XSAUtTZ26RLh2AaZzEGd4Mc/640?wx_fmt=jpeg&from=appmsg)

leak-07-response

### 5.8 漏洞 8：账目清单信息泄露

* 接口：`/XXXXX/XXX/feetrans/search`
* 影响：可读取读者账目流水等数据。

![leak-08-request](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQoct9L7Q1L3Hic5Bntpj39ic2vtyWHTThDumtHyoj3oL29NqkvvzvTayPiaiceicfhOiaBX91Z5fgjZYed2R2GFmKzOibUvfWTUWPf6Zs/640?wx_fmt=png&from=appmsg)

leak-08-request

![leak-08-response](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQob4yg5Amziawr3c9icg6jYh7IBArnmQENYhkMk8oJLdZQ2DvqeBBzUqSxCcjuUEeRPSTCknQ8sO7Wx9WBHuG0LiaEibX36BgdLW4g/640?wx_fmt=jpeg&from=appmsg)

leak-08-response

### 5.9 漏洞 9：积分明细泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/credit/list`
* 影响：可批量读取积分相关信息。

![leak-09-request](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQpfxFajfCA6onKxM9gRY3RJZ4PPWhLoY6cZmeibQNhR1vRN8YOTeiaTmeUrjLHngGZic1GSiay61hkRW65xia8wvd8xKhhicFibqRx8bQ/640?wx_fmt=png&from=appmsg)

leak-09-request

![leak-09-response](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQo4W12OLXj32kyt2MSxBdiaQaSFpPkb8x6bkU42TOlyZtOzwBxzGOdctjia9MaaCQCvtM82OL5AAQZblhNpTnC6eNmT85wSLYVIs/640?wx_fmt=jpeg&from=appmsg)

leak-09-response

### 5.10 漏洞 10：荐读明细泄露

* 接口：`/XXXXX/XXX/patron_info_query/export/suggest/list`
* 影响：可批量读取荐读明细。

![leak-10-request](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrScvqyUJyCjZ8ribc2nPAhavA65JjTaf2q3q0PAzolaDm07ONicUYrFCa2dleeaDJJZbQAwQZw9G6PJRnicr41s4Zz0UNao5RX7Y/640?wx_fmt=png&from=appmsg)

leak-10-request

![leak-10-response](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrtpTEhfwPQQdhYtOpAElMKH8Qt4MWI1PsbpRQKOjAvegXYb6Uvor9bOt6zTVewBt2G1R2a11iaV1G5NpmkFKgx9AfMh1GCwABo/640?wx_fmt=jpeg&from=appmsg)

leak-10-response

## 6. SQL 注入漏洞验证

* 接口：`/XXXXX/XXX/feetrans/search`
* 请求包：

```
POST /XXXXX/XXX/feetrans/search HTTP/2
Host: 10.x.x.x
Cookie: XXX.session=[REDACTED]
Content-Type: application/json

{"sort":"createdDate","direction":"asc","pageSize":20,"page":1,"items":[{"logic":0,"field":"feeTrans.uid","operator":"=","values":[13]}]}
```

* 验证命令：

```
python sqlmap.py --threads 10 --random-agent -r 1.txt --dbs --is-dba --users --passwords --banner
```

* 验证结果摘要：

```
web application technology: Nginx
back-end DBMS: MySQL >= 5.0.12
banner: '8.0.29'
current user is DBA: True
```

* SQLMap 输出显示可触发基于时间的盲注，并已枚举出多个数据库账户（含高权限账户），风险等级为高危。

![sqli-sqlmap-result](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrLibcllZvnq2FY6LW7ayZXgiadagsZqP6tfgl7Isq3Umyf2Gx0n1nibn7w52FgAOY6PWOz2tzSTDbj5fwY5cjw6Wdf0rAnBpNB8g/640?wx_fmt=jpeg&...