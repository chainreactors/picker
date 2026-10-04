---
title: 一个默认口令，端掉整个商会系统：一次授权渗透的完整复盘
url: https://mp.weixin.qq.com/s/Tp6embs2uJtGv-62RjqIYw
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:37:14.949273
---

# 一个默认口令，端掉整个商会系统：一次授权渗透的完整复盘

# 一个默认口令，端掉整个商会系统：一次授权渗透的完整复盘

原创

钟智强
钟智强

哪吒网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 作者：钟智强（哪吒网络安全）　|　授权安全评估 · 非破坏性验证

前几天做完一次授权安全评估，整理报告的时候，我一直在想同一个问题。

真正让我停下来复盘的，不是哪个技术含量高的漏洞。是一个密码。

**admin / admin123**

它背后守着的，是赣州一家下辖百余家会员企业的商会。会员资料、管理员真实姓名和手机号、会费账单、捐款记录，全在那一串字符后面。

![portal.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa3qh0KaPKXVgnwgbQorKHpibYRHia5iaMMibolh1r7YRZ6PoKAgjn7lDmkzf0s7llqMI05ej2J5H6tDsMnOtVJuIWMgKLQvbG0Oicfw/640?wx_fmt=png&from=appmsg)

---

## 一、一个 IP，后面站着三个系统

评估从一个地址开始。8080 端口打开是个 H5 会员端，标题写着「商会会员端·小程序预览」，深蓝配金，外观上没什么可挑的。

真正的收获不在页面上，在源码里。

这个前端是单文件 HTML，明文可读，所有接口调用全都写死在里面。我顺着数了一遍，光 `/api/` 开头的路径就暴露了几十个——会员登录、账单、捐款、会议、党建、积分兑换，整条业务线一览无余。

顺手看了下这台机器还开了哪些端口。

80 端口是另一套「广告自助投放系统」。8081 端口是个 Vue 写的管理后台，登录页标题四个字：商会管理系统。

一个 IP，三个应用。**管理后台的入口，就这么直接开在公网上。**

这一步其实什么攻击都没做，取的全是公开可访问的静态资源。但它把后面的搜索空间，从「盲猜接口」压缩成了「定向验证」。

---

## 二、后台的接口前缀，也是前端告诉我的

8081 打开只有一个登录框，干净得很。

但它是打包过的 Vue 单页应用，主 bundle 一百多万字符。下载下来搜一遍，JS 里引用了三个 chunk，其中一个叫 request，只有六百多字节。

就是这六百多字节把底交了出来：

```
const s = n.create({ baseURL: "/api", timeout: 15e3 });
s.interceptors.request.use(e => {
  const t = localStorage.getItem("admin_token");
  return t && (e.headers.Authorization = `Bearer ${t}`), e;
});
```

`baseURL` 是 `/api`，鉴权头是 `Bearer` 加 localStorage 里的 `admin_token`。

再结合登录 chunk 里的调用路径，后台的登录接口就确定了：`POST /api/admin/login`。

**这就是前端源码审计的价值。** 你不需要爆破目录，不需要猜路径。开发者自己把接口清单写在了页面上，只是他们以为没人会看。

---

## 三、那就试试默认口令

登录接口只要两个字段，username 和 password。

我按顺序试了几个常见的。admin 配 admin，返回「用户名或密码错误」。admin 配 123456，还是一样。

试到 admin 配 admin123——

```
{"code":0,"msg":"ok","data":{
  "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....",
  "user":{"id":1,"username":"admin","role":"super_admin"}
}}
```

服务端签回来一个 JWT。把中间那段 Base64 解开：

```
{
  "type": "admin",
  "id": 1,
  "username": "admin",
  "role": "super_admin",
  "realName": "超级管理员",
  "iat": 1790950430,
  "exp": 1791555230
}
```

`super_admin`。超级管理员。

![微信图片_20261002234552_418_39.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ia7TorzX5Pa1gUicOuzXvyicvx4YKdPsOA8ottwabbpk9f2Lk3ibRkcUkypJkrricvdVZB9A7c9bl8Rcwn0HXxhcgfyeuRYexWrXzzxDicBvuwjK8/640?wx_fmt=jpeg&from=appmsg)

![jwt_decode.png](https://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa0Gq6iavDA9e4Pa0GnGVicLrDyue6PjrswnbZiabeibY4dyPaVZSNwG6O4HicYvUO6diaPDYic1iaDVr7uGkMtG4oJmpY01x8bAm6JZ22Y/640?wx_fmt=png&from=appmsg)

### 那个「用户名或密码错误」，其实是好消息

它说明这个后台的鉴权逻辑本身没坏。不是谁都能进，而是**恰好这个密码能被猜中**。

这两件事的性质完全不同。前者是代码 bug，改几行就好；后者是没有人在管。

这个区分很重要，因为它决定了修复方向：你不需要重写认证模块，你需要的是口令策略和账号治理。

### 顺带说个令牌设计问题

这个 JWT 有效期 7 天（`exp - iat = 604800` 秒），没有刷新机制，也没有 `jti` 之类的吊销标识。

意味着什么？一旦泄漏，在有效期内**无法主动失效**，只能等它自然过期，或者轮换签名密钥把所有人踢下线。

在本次评估里，这个令牌经过了我的终端、响应体、截图，好几次。这还只是一次被动观察。

---

## 四、进去之后能看到什么

因为是授权评估，进去之后我只做只读访问，不碰任何写操作。

先请求管理员列表：

```
[
  {"id":1,"username":"admin","real_name":"超级管理员",
   "role":"super_admin","phone":null,"permissions":""},
  {"id":7,"username":"001","real_name":"徐小芹",
   "role":"level1_admin","phone":"1990****277",
   "permissions":"dashboard,member,fee,audit,party,announce,points,system"}
]
```

注意第二个账号。`001`，角色 `level1_admin`，权限清单里有 `system`。

**默认凭据问题不是某一个人的疏忽，是账号治理层面的系统性缺口。**

再往下，数据看板给出全局数字，会议、活动、捐款、议题、分组挨个能读。会议议程原文、捐款金额和备注、会员建议的完整内容、分组对应的乡镇。

![dashboard.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ia7TorzX5Pa1V9G5dzDFqHptgbSM9r6lSM2rwDOTVeQcslia3bt9wNLiaDGBK6NCvfiaRJrT8WZ3Y34icgXRSWRCbq9Vhfc8ibTHkGd1d4GKqlPdo/640?wx_fmt=png&from=appmsg)

一个商会的全部运营数据，加上所有管理员的真实姓名和联系方式。而这些请求，用的都是同一个密码换来的令牌。

---

## 五、比默认口令更意外的，是不用登录也能改数据

如果只有前四节，这就是一份标准的弱口令报告，不新鲜。

真正让我觉得不对劲的是后面这个。

会员端有个诉求反馈功能，会员可以提建议、给满意度评分。对应接口是 `POST /api/public/appeals/feedback`。

注意它在 `/api/public/` 下面。public 这个前缀，意思是给未登录用户用的。

于是它真的不校验登录：

```
POST /api/public/appeals/feedback HTTP/1.1Host: 120.27.232.145:8080Content-Type: application/json{"id":1,"satisfied":"不满意"}HTTP/1.1 200 OK{"code":0,"msg":"反馈成功","data":null}
```

```

```

不带任何身份凭证，记录就改了。

站内消息也一样。`POST /api/public/messages/read` 带上一个 `id`，就能把任意会员的未读消息清空。而且 `id` 是自增整数，枚举成本几乎为零。

看一下前端的调用代码，问题更清楚：

```
function feedbackSatisfied(id, ok) {  fetch(API + '/public/appeals/feedback', {    method: 'POST',    headers: {'Content-Type': 'application/json'},    body: JSON.stringify({ id, satisfied: ok ? '满意' : '不满意' })  }).then(() => { toast('感谢您的反馈'); loadMyAppeals(); });}
```

```

```

请求体里**没有身份，也没有 Token 头**。前端从来没试图携带身份，说明后端也从来没校验身份。

写接口被放进了「公开」路由组。这已经不是漏了一个校验，**是路由分组的时候方向就定错了**。

> 说明一下，这次测试唯一产生的一点副作用就是那条记录。发现之后我立刻按原值改了回去并复核一致。除此之外没有动过任何生产数据。

---

## 六、把三类路由并列看，问题一目了然

我把评估中探测过的接口按路由组整理了一下：

| 路由组 | 设计意图 | 实际状态 |
| --- | --- | --- |
| `/api/public/*` | 未登录可访问 | 全部可访问，**含两个写接口** |
| `/api/member/*` | 需会员登录 | 除 `announcements` 外均返回 401 |
| `/api/admin/*` | 需管理员登录 | 除 `settings` 外均返回 401 |

`/api/public/*` 组的定义本身就是错的。它把「不需要登录」和「可以写」这两件事绑在了一起。

修复的核心不是给某个接口补校验，而是重新划分路由组的语义边界：

```
// 默认拒绝：所有 /api 路由先过鉴权，白名单显式放行
app.use('/api', authMiddleware);

// 白名单只放真正的只读公开接口
const PUBLIC_ROUTES = [
  'POST /api/register',
  'GET  /api/public/settings',
  'GET  /api/public/groups'
];
```

另外两组的 `announcements` 和 `settings` 各漏了一处。这种「1/N 漏一个」的形态，是人工维护白名单的典型症状——**修的时候要做全量路由审计，不能只补这两个接口**。

---

## 七、顺手说一个 Burp 排错的坑

复现的时候卡了一会儿，值得写下来。

用 Burp 的 Repeater 发请求，一直返回 400 Bad Request，响应体是 nginx 的 HTML 错误页。第一反应是令牌无效，换了几次都一样。

其实不是。仔细看请求头，里面有**两个 Host**：

```
GET /api/admin/users HTTP/1.1
Host: 120.27.232.145:8080
Authorization: Bearer eyJhbGci...
...
Host: 120.27.232.145:8081        ← 多出来的这一行
```

第二个 Host 是从 8081 登录之后，手动把目标端口改成 8080 时留下的。HTTP/1.1 规定 Host 头唯一，nginx 在应用层之前就拒绝了这个请求，它**根本没到达后端**。

删掉多余那行，立刻返回 200。我用原始 socket 又验了一遍：

```
两个 Host 头  → HTTP/1.1 400 Bad Request
单个 Host 头  → HTTP/1.1 200 OK
```

这类问题最迷惑人的地方在于，它看起来像权限问题，实际上是请求压根没发出去。以后看到 nginx 的 HTML 错误页而不是应用返回的 JSON，先怀疑这一层。

---

## 八、还有一些小问题

报告里还记了几条，单独看都不致命，但放在一起能说明整体工程水平：

**技术栈暴露得太干净。** 响应头里有 `Server: nginx/1.24.0 (Ubuntu)`，还有 `X-Powered-By: Express`。报错信息里又写着 `cannot be bound to SQLite parameter`。三条线索拼起来，攻击者不用做任何探测就知道你是 nginx + Express + SQLite。

**前端源码里硬编码了真实手机号和密码。**

```
// 模拟手机号13807970003（张春生），正式版从微信获取var phone = '13807970003';body: JSON.stringify({ phone: phone, password: '123456' })还有短信验证码在客户端生成（localStorage.setItem('mockSmsCode', code)），以及一个 http://localhost:3000/api/member/me 的开发接口。
```

```

```

**CORS 配成了通配符。** `Access-Control-Allow-Origin: *`，还放行了全部方法。因为这套系统用 Bearer 而不是 Cookie 鉴权，暂时偷不到登录态，所以只定到 Low。但如果哪天改成 Cookie 鉴权，这个配置立刻变成高危。

---

## 九、没打进去的，我也写了

SQL 注入和路径遍历我都试了，没打进去。

`memberId` 参数试了 `1'`、`1 AND 1=1`、`1 AND 1=2`、`UNION SELECT`、`;SELECT`，全都返回空集且无报错——参数化绑定，做得对。路径遍历的几种变体（`../`、`%2e%2e%2f`、`..%2f`、`....//`）也都被规范化拦掉了。

这些我照样写进了报告，单独开一章叫「负面测试结论」。

**没打进去的也得写。** 安全评估的价值不只在于找到多少漏洞，也在于明确界定「已经验证过、确认不存在」的范围。这让委托方知道哪些风险已被排除，也避免后续重复投入。

有意思的是，VUL-03 那条报错（`cannot be bound to SQLite parameter`）反过来印证了 SQLi 的阴性结论——它证明那里用的是绑定查询。

---

## 十、修复清单和优先级

| 优先级 | 事情 | 时限 |
| --- | --- | --- |
| **P0** | 改默认口令、停用多余账号、强制改密、加登录锁定、后台收内网 | 24 小时内 |
| **P1** | public 写接口补鉴权与归属校验、统一异常处理 | 3 个工作日 |
| **P2** | 收敛敏感字段、admin/settings 加鉴权、CORS 白名单、补安全头 | 2 周内 |
| **P3** | 字段白名单、移除硬编码凭据、接口鉴权自动化测试 | 1 个月内 |

P0 和 P1 的分界是**利用门槛**。VUL-01 不需要任何前置条件就能直接接管系统，「不做就会出事」；越权写接口虽然同为未授权访问，但影响限于数据完整性，可以稍后。

P3 里我特别想强调「接口鉴权自动化测试」这一条。前面那个「1/N 漏一个」的问题，人工审计只能覆盖当次路由；只有自动化用例，才能覆盖以后新增的接口。

---

## 十一、默认口令，从来不是技术问题

整理报告的时候我在想一件事。

一台几百块一年的云主机，一个外包做的管理系统，几十个会员的手机号，管理员的真实姓名，商会的捐款记录。它们的安全性，最后落在一个字符串上。

**admin123**

这类系统有个共同点。它能跑起来，功能也都有，会员端做得挺好看。但只要问一句「谁在负责安全」，通常就没有答案了。没有专职的人，没有留预算，上线之后就没人再碰过配置。

技术上的修复其实很简单。改密码、加登录锁定、把写接口移出 public 路由，半天就能做完。

难的是有人记得去做。

---

## 附：完整攻击链

整条链上，没有任何一个环节需要绕过一个正常的校验逻辑。每一环都是在系统「按设计正常工作」的前提下完成的。

**这正是弱口令类漏洞最难防御的地方：它不需要系统有 bug。**

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia7TorzX5Pa1SibU9u3OqdKX5WMO8J5SW6AUgJiahD4yxRdHuUW7nZVUD4eYrgoUNEZgC2A10nia8rXz2WvL7rhLp9FnPicITMLxdBwKtwvMkjIk/0?wx_fmt=png)

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