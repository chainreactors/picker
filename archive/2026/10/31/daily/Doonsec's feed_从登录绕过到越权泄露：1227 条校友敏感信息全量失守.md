---
title: 从登录绕过到越权泄露：1227 条校友敏感信息全量失守
url: https://mp.weixin.qq.com/s/f8czFvXcoASWyUyFad1zeQ
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:04.232897
---

# 从登录绕过到越权泄露：1227 条校友敏感信息全量失守

# 从登录绕过到越权泄露：1227 条校友敏感信息全量失守

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

在小程序的登录框里随便敲了一组用户名和密码，提示登录失败，页面却跳了进去；再点一下「校友」，全院 1227 名校友的手机号、出生日期、工作地点，排着队出现在列表里。

问题的根子在前后的错位上：前端用「账户正在审核中」的提示把人拦在校友功能外面，后端接口却不校验账户的审核状态和数据权限——界面拦得住人，请求拦不住数据。

在一次攻防项目中，我们发现某学院小程序存在 1 项高危漏洞：越权导致敏感信息泄露，实测可获取 1227 条校友个人信息。

---

## 越权导致敏感信息泄露：登录失败也能看全部校友

**漏洞地址：** GET https://xx.xx.xx.xx/api/system/alumni.info/page?pageNum=1&pageSize=10&name=&alumniCode=（需登录态 Token，未校验账户审核状态）

**怎么发现的：** 目标是一次攻防项目中的某学院官方小程序。正常注册流程走到「校友」功能时被拦——提示「账户正在审核中」。这个提示本身是个信号：系统知道该拦人。顺着「审核中」这个状态往下试，就成了这条链子的起点。

`/api/system/alumni.info/page` 是校友信息的分页查询接口，按页返回校友的姓名、手机号、出生日期、工作地点等字段。正常来说，一个「审核中」的账户不应该有任何查看校友数据的权限。

先看正常路径。校友功能点进去，直接被拦，提示账户正在审核中：

![正常访问被拦](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gr5thJzWkjkyrUsIZKibSja80Fv7BiaDcbibgM84HDZmOjG691ugQpSs6SfbFJCUyTWXeTMpRDKZONSFOEhpg6EED0AjuJeAZxO7E/640?wx_fmt=png&from=appmsg)

换个思路。进「我的」，走账户密码登录，用户名和密码随便填一组：

![随便填写账密](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gp9ldEEqKyicvEuvgSTPSw4WHEJCAfkWhVWaibVAqMqibGFAlzOE3tsSQhQILiaLR4xN8gXw4wUzJ72URsT3RlKUzkXrCqB90Mmxwc/640?wx_fmt=png&from=appmsg)

登录失败了，但小程序没有停在登录页，而是照常进行了跳转：

![登录失败但跳转](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpLgQGZZHAckIT1eIoHfHDGI4SH5KB2iahgXiadErBNUMibibia7lAJpgnyBg4MG0uI69Ku52XxusOU8Mrop0bNnHTVGvm4KRJDMmUM/640?wx_fmt=png&from=appmsg)

跳转之后再点一次「校友」——这次没拦，校友列表直接出来了：

![跳转后越权查看](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpYrJRqkmVFXCbxbhriaicgRzX3ia3l5o7ialtJVPNX5csgvsJXNJtxXdfTWv5oTUrD672VUXu0JhhvnV8rTqZfh1icpyTuqfHsW6CU/640?wx_fmt=png&from=appmsg)

前后端的分歧就在这里：前端把「审核中」的用户拦在界面外，后端却对同一个账户全量放行。抓包看请求，正是那个校友分页接口：

```
【请求包】
GET /api/system/alumni.info/page?pageNum=1&pageSize=10&name=&alumniCode= HTTP/1.1
Host: xx.xx.xx.xx
Authorization: <未审核账户的登录态 Token>
```

（Token 请求头以实际抓包为准，此处为复现示意。）

响应里的内容远比前端页面显示的多——total 为 1227，每条记录都带着手机号、出生日期、工作地点这些本不应显示在前端的个人敏感信息：

```
【响应包（关键字段）】
HTTP/1.1 200 OK

total: 1227
records: 每条记录含姓名、手机号、出生日期、工作地点等个人敏感字段（其余字段略，完整数据见下图）
```

![抓包响应包含大量校友信息](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqIp4Cd5FPgvw4rK0dRgZu2pXQCObMYbWBAneZCibLParoRM7DyxoCXKuV2jRN5jib6eoagYQWlTljQ2JzjT4pHKe8t7Cs7UiaAGU/640?wx_fmt=png&from=appmsg)

![前后端回显不一致](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grHibdWFhp4RIl9EErpXygxrNmPvjjaf3uHhhzYalnuerZDuYFeNjhkDRKYoI6Wic7Mng71SR46EDUibc1mk3tMN1x1Hf6y6ia9SZs/640?wx_fmt=png&from=appmsg)

返回小程序，再点一次校友功能点，页面成功渲染出所有校友的个人敏感信息：

![小程序全量展示](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goMwohSCfB4bFu35QAkeG8WSAY2TrsmSe19FzIia3OCIIkianuDCfQhTGibgMSrCjNsrMPbIJpMd1uicZmRiaCkiaSYwNiaadcKfqXv8c/640?wx_fmt=png&from=appmsg)

接口返回 1227 条校友信息（需登录小程序获取 Token 查看）：

![1227条校友信息](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gq0pOyjdA0x5S6pqicw695nPW8LbJlaKbOia6s6ichpcgLicSGUstcialzMib6AS1dsNw80VpHqjequx8tHibgEgyXE7O6ZyoYtcHChr0/640?wx_fmt=png&from=appmsg)

全院 1227 名校友的手机号，全部在列：

![全部手机号](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqSbluAibFfRvKeP7dibpCVvcxJLicRLnnRSe7uia19ccryAYDYhECiaK6LS2vO2cuJg9bqHGhKqiaYDhzKlfgm5iaVCc4VY3ZrJInqS4/640?wx_fmt=png&from=appmsg)

```
全院 1227 条校友记录——姓名、手机号、出生日期、工作地点——对一个随便输错密码就能进来的访客全量放行。手机号 + 出生日期 + 工作单位三件套，足够支撑撞库、精准诈骗、定向社工等下游攻击；对一所学院来说，这是全量校友的个人隐私在一次随手尝试中失守。
```

---

## 写在最后

回看这条链子，没有一个高危 CVE，也没有复杂的绕过技巧：一次登录失败后的跳转，一个不问账户状态的后端接口。前端用「审核中」的提示尽职尽责地拦人，后端却把数据原样给了出去——权限控制做在了界面上，没做在服务端。

这也是前后端回显不一致类漏洞的共同点：前端拦截只是体验层，真正的权限边界必须在服务端重新回答一遍——这个账户是什么状态、这条数据该不该给这个人看。少问任何一句，界面上拦住的就只是界面。

攻防项目的意义，不是证明系统有多脆弱，而是在真实攻击者之前把问题找出来。文中学院名称、域名与人员信息均已脱敏，仅用于安全研究与防御参考。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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