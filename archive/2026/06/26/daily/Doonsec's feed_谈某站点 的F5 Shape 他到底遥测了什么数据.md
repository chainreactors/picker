---
title: 谈某站点 的F5 Shape 他到底遥测了什么数据
url: https://mp.weixin.qq.com/s/uM_4-5d4VUsEheinDLErnA
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:23.626682
---

# 谈某站点 的F5 Shape 他到底遥测了什么数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnvCiby44z6c0cB80zjuibbLs0U5tjHxfbAJKLfyrRL7CBIRBRNoqR1molE5cPS1sFAOz0e1jUE1C7ialSvvWeakHlrDyCaVS62qicQ/0?wx_fmt=jpeg)

# 谈某站点 的F5 Shape 他到底遥测了什么数据

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 作者介绍：http://gitee.com/haidragon

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnt0ictvV9YYrSprrl4O8MQsEgsg8yXtGUnwicXwRNicVR9HGUibWUeYIsUibYQ8ibhFria9jq50F5XRfzbVeaBIMYgvsmA1bbIorVOO4A/640?wx_fmt=png&from=appmsg)

#

# 当我们谈某站点 F5 Shape 遥测时，我们到底在谈什么

## 不是一层 Header，而是 `ee30zvqlwf-*` 主遥测 + `x-swa-di-*` 次遥测 + 最终业务请求汇合

### 快速总结

* 主遥测字段数： `ee30zvqlwf-a` 当前样本共 533 个字段
* 次遥测字段数： `x-swa-di-ue` 当前样本共 35 个字段
* 字体探针数：当前样本共 465 个 `font_probe` 字段
* 链路状态：纯本地目标请求已稳定到达业务校验层
* 请求结果：服务端返回 HTTP 400 / code 400518024 / error invalid\_grant，表示凭据字段未通过业务校验

这条链路的重点不在于“有多少层 header”，而在于两套遥测数据分别装了什么字段、字段如何汇总，以及最后怎样与 OAuth 请求体一起送到目标接口。

按当前本地样本，这条某站点请求链路更像一条高度疑似 F5 Shape 集成态的主安全遥测链路：

* 主遥测： `ee30zvqlwf-*`
* 次遥测： `x-swa-di-*`，尤其是 `x-swa-di-ue`
* 汇合面： `POST/api/security/v4/security/token`

当前结构化统计：

* `ee30zvqlwf-a` 顶层遥测键：533
* 字体探针：465
* `x-swa-di-ue` 事件字段：35
* 其中 `sesn`：18 项， `ptni`：11 项， `inauth`：6 项
* 纯本地目标请求当前已稳定到达业务校验层
* 当前请求结果：HTTP 400 / code 400518024 / error invalid\_grant，表示凭据字段未通过业务校验

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntvDG0EMc6OoC3cOEYyibxJDkJMjKt55UfviaIO9fxUTG52pz4RhMrlBeHLZnKuuTSSLJgBy0UxulicESW8MicyWmX7jxNa0p2TF0w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuzQh8o2zjv624nLZy0K3BwNZ72ibeK9phd8zN83wlUk5jODajmnWQhxk6cjs8zF5tiaQj4c5KllicfNfDu0d7NMN1NmDRnVgMv78/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntFHDICpiahqMb21iahw1e69icdvY57kd36h4Vf4aq2M0QX0MRNJb7lwHSRQqicJzOolODJuPibS9XlYHqz8ibLeibjRZfHLd5PFNrLBs/640?wx_fmt=png&from=appmsg)

##

## 一、主 `ee30zvqlwf-*` 到底在干什么

这组字段不是普通业务头。当前样本表明，它们只打到安全 API，并且其中最关键的 `ee30zvqlwf-a` 可以直接解出一个很大的 JSON 对象。

这份对象里既有：

* 会话绑定字段
* 时间/时区字段
* Navigator 与环境字段
* Window/Screen 几何字段
* 权限与能力探针
* 图形完整性与异常探针
* 大量字体存在性探针

也就是说， `ee30zvqlwf-a` 本质上不是一个“单值 token”，而是一份浏览器侧主安全遥测对象。

### 1. 顶层主遥测字段全表

| 字段别名 | 分组 | 脱敏演示值 | 说明 |
| --- | --- | --- | --- |
| ee30.session.t | 会话绑定 | TKN*FAKE*7Qx9n2vL...fake...Qp8rM1 | ee30 主体里的长 token/校验载荷，长度最大，明显不是普通业务字段。 |
| ee30.cap.browser\_features | 能力/权限 | {"fake":true} | 浏览器 API 能力对象。 |
| ee30.integrity.canvas\_spoofing | 图形/完整性 | 4 | canvas spoofing 评分/标记。 |
| ee30.integrity.canvas*print*100\_999 | 图形/完整性 | 37de06c2...fake...158c66af | canvas 指纹哈希。 |
| ee30.integrity.canvas*print*detailed*100*999 | 图形/完整性 | 37de06c2...fake...158c66af | 更细粒度 canvas 指纹哈希。 |
| ee30.integrity.ccjs\_version | 图形/完整性 | J92a8f+xFakeCg5biQ== | collector/cc.js 版本标记。 |
| ee30.session.cf\_flags | 会话绑定 | 1039001 | 客户端能力/风险位压缩串。 |
| ee30.integrity.command*call*log | 图形/完整性 | ["ci","st","run","csd"] | collector 命令调用序列。 |
| ee30.session.cookie\_\_cc | 会话绑定 | ASLrFake%2FTelemetry | 与本地 cookie 链相关的短标记。 |
| ee30.cap.css\_flags | 能力/权限 | {"fake":true} | CSS 能力/媒体查询探测对象。 |
| ee30.integrity.developer*tools*enabled | 图形/完整性 | false | 开发者工具状态位。 |
| ee30.integrity.device*data*captured\_time | 图形/完整性 | 1782000000350 | 设备数据采集完成时间戳。 |
| ee30.session.dom*local*tag | 会话绑定 | DOM*LOCAL*FAKE\_TAG | 本地 DOM 标签态短标记。 |
| ee30.session.dom*session*tag | 会话绑定 | DOM*SESSION*FAKE\_TAG | 会话级 DOM 标签态短标记。 |
| ee30.integrity.ex*browser*type | 图形/完整性 | Chrome | 脚本识别出的浏览器类型。 |
| ee30.session.fresh\_cookie | 会话绑定 | ASLrFake%2FTelemetry | Cookie 新鲜度状态位。 |
| ee30.cap.granted\_permissions | 能力/权限 | {"fake":true} | 权限接口探测结果对象。 |
| ee30.error.js\_errors | 异常/完整性 | [7 fake error probes] | 脚本执行期收集到的异常列表，用于判断环境完整性和 API 缺失情况。 |
| ee30.nav.appCodeName | Navigator/环境 | fake*navigator*appcodename\_019 | navigator.appCodeName。 |
| ee30.nav.appName | Navigator/环境 | fake*navigator*appname\_020 | navigator.appName。 |
| ee30.nav.appVersion | Navigator/环境 | fake*navigator*appversion\_021 | navigator.appVersion。 |
| ee30.nav.automationEnabled | Navigator/环境 | true | 自动化环境探测位。 |
| ee30.nav.connection\_downlink | Navigator/环境 | 10 | 网络下行带宽。 |
| ee30.nav.connection\_effectiveType | Navigator/环境 | 4g | 网络类型摘要。 |
| ee30.nav.connection\_rtt | Navigator/环境 | 48 | 网络 RTT。 |
| ee30.nav.cookieEnabled | Navigator/环境 | ASLrFake%2FTelemetry | Cookie 能力位。 |
| ee30.nav.doNotTrack | Navigator/环境 | fake*navigator*donottrack\_027 | DNT 状态。 |
| ee30.nav.hardwareConcurrency | Navigator/环境 | 8 | CPU 并发数。 |
| ee30.nav.language | Navigator/环境 | zh-CN | navigator.language。 |
| ee30.nav.platform | Navigator/环境 | MacIntel | navigator.platform。 |
| ee30.nav.plugins\_count | Navigator/环境 | 1217 | 插件数量。 |
| ee30.nav.product | Navigator/环境 | fake*navigator*product\_032 | navigator.product。 |
| ee30.nav.productSub | Navigator/环境 | fake*navigator*productsub\_033 | navigator.productSub。 |
| ee30.nav.userAgent | Navigator/环境 | Mozilla/5.0 (Macintosh; Intel Mac OS X 13*6*0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 | 完整 UA 字符串。 |
| ee30.nav.userAgentData\_brands | Navigator/环境 | [{brand:"Google Chrome",version:"149"},{brand:"Chromium",version:"149"}] | UA-CH 品牌列表。 |
| ee30.nav.userAgentData\_mobile | Navigator/环境 | Mozilla/5.0 (Macintosh; Intel Mac OS X 13*6*0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 | UA-CH mobile 标志。 |
| ee30.nav.userAgentData\_platform | Navigator/环境 | Mozilla/5.0 (Macintosh; Intel Mac OS X 13*6*0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 | UA-CH platform。 |
| ee30.nav.vendor | Navigator/环境 | fake*navigator*vendor\_038 | navigator.vendor。 |
| ee30.nav.private-browser | Navigator/环境 | {"error":"fake-private-mode-probe"} | 隐私模式探测结果对象。 |
| ee30.win.screen\_availHeight | 窗口/屏幕 | fake*screen*availheight\_040 | screen.availHeight。 |
| ee30.win.screen\_availWidth | 窗口/屏幕 | fake*screen*availwidth\_041 | screen.availWidth。 |
| ee30.integrity.script*load*time | 图形/完整性 | 1782000000100 | 脚本加载时间戳。 |
| ee30.session.sid | 会话绑定 | 7b66-fake-session | ee30 主遥测对象里的短会话标识。 |
| ee30.session.tid | 会话绑定 | 3280-fake-transaction-51e | ee30 主遥测对象里的事务标识，和请求级事务绑定有关。 |
| ee30.time.local | 时间时区 | 2026/06/23 21:51:01 | 本地化时间串。 |
| ee30.time.string | 时间时区 | Tue Jun 23 2026 21:51:01 GMT+0800 | 标准 Date 字符串。 |
| ee30.time.tz*dst*active | 时间时区 | false | 当前是否处于 DST。 |
| ee30.time.tz*fixed*locale\_string | 时间时区 | fake*time*tz*fixed*locale*str*048 | 固定日期样本的本地化输出，用于时区一致性校验。 |
| ee30.time.tz*has*dst | 时间时区 | false | 是否存在 DST。 |
| ee30.time.tz*offset*minutes | 时间时区 | -480 | 时区偏移分钟。 |
| ee30.time.tz*std*offset | 时间时区 | -480 | 标准时区偏移。 |
| ee30.time.unix*epoch*ms | 时间时区 | 1782000000123 | 毫秒级时间戳。 |
| ee30.integrity.timing*sync*collection | 图形/完整性 | 1371 | 同步采集耗时。 |
| ee30.nav.touchEnabled | Navigator/环境 | true | 是否支持触摸。 |
| ee30.nav.webdriver\_detect | Navigator/环境 | false | webdriver 检测结果。 |
| ee30.integrity.webgl\_supported | 图形/完整性 | true | WebGL 支持位。 |
| ee30.win.window\_devicePixelRatio | 窗口/屏幕 | fake*window*devicepixelratio\_057 | 设备像素比。 |
| ee30.win.window*history*length | 窗口/屏幕 | fake*window*history*length*058 | history.length。 |
| ee30.win.window\_innerHeight | 窗口/屏幕 | fake*window*innerheight\_059 | innerHeight。 |
| ee30.win.window\_innerWidth | 窗口/屏幕 | fake*window*innerwidth\_060 | innerWidth。 |
| ee30.win.window\_outerHeight | 窗口/屏幕 | fake*window*outerheight\_061 | outerHeight。 |
| ee30.win.window\_outerWidth | 窗口/屏幕 | fake*window*outerwidth\_062 | outerWidth。 |
| ee30.win.window*screen*availHeight | 窗口/屏幕 | fake*window*screen*availheigh*063 | screen.availHeight。 |
| ee30.win.window*screen*colorDepth | 窗口/屏幕 | fake*window*screen*colordepth*064 | 颜色深度。 |
| ee30.win.window*screen*darkMode\_enabled | 窗口/屏幕 | false | 暗色模式探测位。 |
| ee30.win.window*screen*height | 窗口/屏幕 | fake*window*screen*height*066 | screen.height。 |
| ee30.win.window*screen*pixelDepth | 窗口/屏幕 | fake*window*screen*pixeldepth*067 | 像素深度。 |
| ee30.win.window*screen*width | 窗口/屏幕 | fake*window*screen*width*068 | screen.width。 |

### 2. 主遥测里的嵌套探针字段展开表

下面这张表把顶层对象内部的子探针继续展开，包括权限子项、浏览器能力子项、CSS 子项、UA-CH 品牌项、异常列表和命令调用序列。

| 字段别名 | 探针家族 | ...