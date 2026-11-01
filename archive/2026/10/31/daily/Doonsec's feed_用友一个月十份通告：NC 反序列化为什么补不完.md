---
title: 用友一个月十份通告：NC 反序列化为什么补不完
url: https://mp.weixin.qq.com/s/CUGb94k7Z14BuJ3fr9PwDg
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:28.811338
---

# 用友一个月十份通告：NC 反序列化为什么补不完

# 用友一个月十份通告：NC 反序列化为什么补不完

红队安全圈
红队安全圈

红队安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

十月用友安全中心挂出十份漏洞通告，八份高危、五份标着 0day，二十一号一天两份反序列化公告，CVSS 8.5 与 8.1，覆盖 NC65 到 YonBIP 高级版 2505 十条版本线；最新那批补丁的名字叫"禁用 ~ 以及外部交换平台以外的调用"，把修补思路直接写在了标题上。

## 01  引言

用友 NC 在国内的分量不用多说：集团财务、供应链、报表、审批，很多单位的账都在这套系统里跑。这类系统被打穿，丢的不是一台机器，而是一整套财务数据的入口。

十月这个月，用友安全中心一共挂出十条通告，八条高危，其中五条直接标了 0day。二十一号最密集——同一天两份反序列化通告，一份 8.5，一份 8.1，版本线一路铺到 YonBIP 高级版 2505。

反序列化在 NC 上不是新问题，隔一两年就来一次。值得写的不是"又爆了一个"，而是补丁思路的变化：从白名单、黑名单，一路退到"只留一条通道"。

## 02  漏洞速览

通告日期2026-10-21，同日两份

影响产品NC65、NCC1903、NCC1909、NCC2005、NCC2105、NCC2111、YonBIP 高级版 2207、2305、2312、2505

漏洞类型Java 反序列化（同通道历史案例为未认证）

危害等级CVSS 8.5 / 8.1，均为高危

在野利用截至发稿无公开报告

公开 PoC无针对本次补丁的公开利用

攻击前提公共入口 Servlet 可从网络访问

## 03  漏洞成因

反序列化在 NC 上的入口一直是那几个公共 Servlet。/ServiceDispatcherServlet 在 web.xml 里映射到 CommonServletDispatcher，后者初始化时实例化 nc.bs.framework.comn.serv.ServiceDispatcher，请求体按自定义序列化流交给 NetObjectInputStream 还原。还原时不校验类，洞就在这里。

官方的修法分了三个层次，一层比一层被动：

1.白名单：给 NetObjectInputStream 加带 Class[] 参数的构造方法，resolveClass 里用 isAssignableFrom 判断，只放行 InvocationInfo 与 ESBContextForNC 两个类

2.黑名单：在 NCObjectResolver 里堆 CommonsCollections 一类的禁用类名

3.关掉 TemplatesImpl：把系统属性 jdk.xml.enableTemplatesImplDeserialization 置为禁用，getOutputProperties 那条经典链直接失效

修补越打越细，绕过也跟着走。黑名单之外找 getter，转 JNDI（JdbcRowSetImpl）回连，再配本地 Factory——NC 环境里常见的 bsh（eval(String) 加无参构造）或 Tomcat 8 以下的 ELProcessor，都能把字节码加载回内存。

这次 10-21 的 8.1 那份，补丁命名是一版一条："patch\_65\_禁用~以及外部交换平台以外的调用"。~ 前缀的调用面被整体砍掉，只留外部交换平台。也就是说，这一轮修的不是某个具体 gadget，而是通道本身。

另一份 8.5 的补丁更有意思：名称是"反序列化公共读取配置补丁"加"反序列化漏洞集合补丁"，编码里的日期是 2024 年 6 月和 7 月——它复用的是两年前的补丁包。真正的收口在 10 月 19 日打的那批包里。只装一份，等于没装。

<!-- web.xml -->

<servlet-name>

  CommonServletDispatcher

</servlet-name>

<servlet-class>

  nc.bs.framework.comn.serv

  .CommonServletDispatcher

</servlet-class>

<url-pattern>

  /ServiceDispatcherServlet

</url-pattern>

NetObjectInputStream objIn =

  new NetObjectInputStream(

    new ByteArrayInputStream(bytes),

    new Class[]{

      InvocationInfo.class,

      ESBContextForNC.class});

## 04  影响范围

十条版本线各有各的补丁号，三个细节值得留意：

·NC65 与 NCC 系列前缀不同，一个是 NCM\_NC6.5\_，一个是 NCM\_NCCLOUD...，拿错包就是空打

·YonBIP 高级版 2305 的编码里带 (2207SP)，同系列不同代号，别按名字对

·同一个十月，U9 智能工厂（10-30，命令执行，标 0day）、畅捷通 T+（10-26、10-07，SQL 注入）、GRP-U8Cloud（10-21，SQL 注入）各有洞，用友全家桶都在排队打补丁

## 05  利用分析

这次没有公开 PoC，按成因推演攻击路径：

·入口：POST 到 /ServiceDispatcherServlet，请求体是可序列化对象流

·前置：不需要账号（同通道历史漏洞是未认证直接打），只要这个 Servlet 对外可达

·链条：恶意序列化流 → 反序列化触发 gadget → 命令执行

·加分项：主机能出网（JNDI 回连成功率高）；NC 常与外部交换平台共存，8080 之外还有一堆配套端口

·代价：反序列化打失败很可能把服务打挂，生产环境的代价比漏洞本身还大

判断：对外暴露的 NC 是"高价值 + 低门槛"的组合，历史上这类入口被批量扫过不止一次。

## 06  检测与排查

先对版本。登录 NC 管理端看补丁号，是否包含 20261019\_GP\_ 这一批；只装了 2024 年那两条老补丁的，按未修复算。

再探入口。只取响应头，别发序列化数据：

日志侧看两样东西。一是这个路径上的 POST 请求，正常业务很少直接从公网打进来；二是补丁生效后的特征异常——白名单拦截会抛出带类名的 IllegalArgumentException，日志里长这样：

主机侧看：陌生 .jsp/.war 落盘、java 进程拉起 /bin/sh、对外的 1099/1389 连接。NC 主机出网这件事本身就该查，正常业务不需要。

T=https://target

curl -sI -m 5 \

  $T/ServiceDispatcherServlet

grep -c \

  "####### class::" nc/logs/\*.log

## 07  修复建议

·按版本打 10 月 19 日那批补丁，每个版本一条，示例两条：

·NCM\_NC6.5\_000\_109902\_20261019\_GP\_382879042

·NCM\_NCCLOUD2021.11\_010\_0013\_20261019\_GP\_387529616

·2024 年那两条"反序列化公共读取配置补丁 + 漏洞集合补丁"照样要装，两条是叠加关系，不是替代

·打之前先备份 modules 目录，补丁重启失败的回滚成本很高

·暂时升不了：边界只放行必要来源访问 /ServiceDispatcherServlet；不用外部交换平台的直接关掉；主机禁出网；有条件上 RASP

验证方式很朴素：重启后确认补丁版本号，再从外网打一条请求，日志里应出现被拦截的异常而不是正常业务响应。

## 08  红队视角

NC 是内网横向里含金量最高、也最好找的一类目标：指纹特征明显，入口固定，版本号往往写在页面上。

补丁思路决定了这个洞会一直有。白名单 → 黑名单 → 关 TemplatesImpl → 砍 ~ 通道，四轮下来全是"堵已知"，没有一轮是把反序列化入口整体换成安全实现。下一轮绕过只是时间问题，历史已经演过一遍：CC 链被禁就用 JNDI，TemplatesImpl 被关就用 bsh。

实际打的顺序：先指纹确认（NC、NC Cloud、YonBIP 高级版各不一样），再看 /ServiceDispatcherServlet 是否存活，然后用补丁号判断处在哪一代，最后才选链。补丁判断错，链选对也白搭。

授权边界要提前说清：反序列化打崩服务是常态，演练方案里"不可逆业务影响"的条款通常覆盖这种情况。生产段别手快。

长期该做的事只有一件：把 /ServiceDispatcherServlet 和外部交换平台相关 Servlet 列进暴露面清单，别等下一个 0day 出来才想起来关端口。

## 09  POC 链接

https://security.yonyou.com/#/noticeInfo?id=830

https://security.yonyou.com/#/noticeInfo?id=581

https://www.freebuf.com/vuls/382834.html

https://xz.aliyun.com/news/15195

前两条是用友安全中心本次两份通告原文（含全部版本补丁编码与校验码），后两条是同一通道的历史补丁分析与黑名单绕过研究，理解成因用得上。

想要文中检测命令和补丁核对清单的，留言说一声；**关注**不迷路，更新看得见。

— END —

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5HsgFkdwV2JyJtbCAnjqN7qIvk8GZkoD7I5eY36IQQvribiauFhgInT7GIPm2O5D9d2ynIcbnPicbGnox7PL4Hh4g/0?wx_fmt=png)

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