---
title: K8s 策略引擎被打穿：Kyverno 9.9 分，一条策略提权到集群
url: https://mp.weixin.qq.com/s/BVDxI1N5HW_SVaU9nd_93g
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:56:59.051366
---

# K8s 策略引擎被打穿：Kyverno 9.9 分，一条策略提权到集群

# K8s 策略引擎被打穿：Kyverno 9.9 分，一条策略提权到集群

原创

红队安全圈
红队安全圈

红队安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

30 秒看懂

影响范围 · Kyverno 1.17.0 至 1.19.1，任何把 namespaced 策略（NamespacedMutatingPolicy、NamespacedValidatingPolicy、namespaced Policy 的 apiCall）创建权限下放给租户的集群。前置条件只有两条：能在自己命名空间 create 这几类 CRD，能创建被策略匹配的资源，一个 ConfigMap 就够。

利用状态 · 未证实在野利用。但四份通告都附了完整复现步骤、YAML payload 和命令输出，照着敲能在 kind 集群里一路打通到 cluster-admin。

补丁状态 · 已修（1.19.2，2026-10-20 发布）＋ 升级之外还要收权限，补丁修的是边界检查本身，不是给谁发权限这件事。

11 月 5 日 NVD 挂上 CVE-2026-122313，9.9 分。它描述的事情很小：一条 namespaced 策略里的一段 CEL 表达式，输出被当成目标对象时没人看命名空间。后果不小：集群级的后台控制器拿着自己的 ServiceAccount，把另一个租户的 RoleBinding 改了。

## 01  事情是什么

Kyverno 是多租户 K8s 里最常见的策略引擎，准入 webhook 拦请求，后台控制器改存量对象。它给租户设计的委派模型就是 namespaced 策略：租户在自己命名空间里写规则，只影响自己的地盘。

CVE-2026-122313 打的正是这条承诺。NamespacedMutatingPolicy 打开 mutateExisting 之后，目标资源可以由 targetMatchConstraints.expression 这段 CEL 直接算出来。表达式返回一个 map，Kyverno 把它当目标对象用，但不校验它的 namespace。租户写一条返回另一个命名空间 RoleBinding 的策略，后台控制器就去把那个 RoleBinding 改掉，加 subject、改 Role、改 NetworkPolicy、改 ConfigMap 都行。用的是控制器自己的权限，租户在对方命名空间里的 RBAC 一点没被问到。

CVSS **9.9**，AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H。S:C 是关键：伤害落在 Kyverno 之外，它借出去的是自己的身份，所以比常规提权高一档。

## 02  为什么危险

这批通告里最值钱的地方，是三个绕过原语共用同一个病根：校验的对象和执行的对象是两份字符串。

第一处，apiCall 的 urlPath。1.16.3 起 Kyverno 给 namespaced 策略的 apiCall 加了命名空间钳制，策略只能调自己命名空间里的 API。1.19.1 补了 %2e%2e 这一类，做法是先解码、再 path.Clean、再用正则从干净路径里抠出命名空间。问题在于抠完之后，发给 API server 的还是原始字符串：

// apiCall.go Fetch()，1.19.1

raw := call.APICall.URLPath

un, err := url.PathUnescape(raw)

if err != nil { un = raw }

// 解码失败，退回原文路径

clean := path.Clean(un)

// 检查的是 clean，发的是 raw

只要让解码这一步失败，钳制就退回去检查原始路径，而 API server 那边照常完整解码。让 PathUnescape 报错很容易：在 query 里放一个残缺转义就行，?a=%、?a=%2、?a=%zz 都算。client-go 会把这个残缺的 query 扔进 RawQuery，请求路径本身干净，API server 收不到任何非法编码，也就没理由拒绝。于是钳制读到的是 attacker-ns，请求落到的是受害命名空间；把 %2e%2e 叠两段，就落到集群级集合 mutatingwebhookconfigurations 上，而默认安装的准入控制器 ServiceAccount 本来就有建 webhook 的权限。

这条限制被打穿三次：1.19.1 修第一次，1.19.2 修用 # 和 ? 藏 ../ 的第二次，10 月 23 日又补了一份用残缺转义绕过钳制本身的通告，同样 9.9 分，同样修在 1.19.2。

第二处，CEL 的 resource.get() 和 resource.post()。这两个函数的 resource 参数允许带斜杠，库的实现是按 / 切开，第一段当资源名，后面全当 subresource 塞进请求路径。client-go 会校验命名空间和资源名，对 subresource 却完全不校验，而 path.Join 会把 .. 吃掉：

// resource 参数，折叠示意

configmaps/../../../../namespaces/

  kube-system/configmaps/kv-canary

四个 .. 回到 /api/v1，六个直接回到根。读别人的命名空间、读集群级对象、用控制器的账号 POST 一个集群级 webhook，都是这条路。

第三处就是开篇那条 CVE：CEL 表达式伪造目标对象。它比前两处更省事，连请求路径都不用构造，纯粹是我说目标是谁你就去打谁。

对红队来说，三处的价值在于都不需要提权原语。拿到一个命名空间的策略写权限（很多平台为了交付功能本来就给），剩下的全是填参数。难的不是利用，是发现：要去读策略引擎的代码，看它检查了哪份字符串、又发出去了哪份。

## 03  谁受影响

· Kyverno 1.19.1 及以下，开了 namespaced 策略的多租户集群

· 版本下界各家通告写法不一：有的写 1.18.0 起，有的写 1.18.2 之前、1.19.0 及以下，NVD 统一写 1.17.0 到 1.19.2 之前。按最宽口径算，1.19.2 以下都当受影响

· 前置条件只有一个：能在一个命名空间里 create 这几类策略 CRD，外加能创建被策略匹配的资源。多租户平台、给客户开命名空间的服务商、内部按团队隔离的集群，命中概率最高

· 单租户自用集群打不动自己，风险变成策略作者可不可信

## 04  怎么修

**1.** 升到 1.19.2 及以上，Helm 用 kyverno/kyverno，chart 3.9.x 对应 appVersion 1.19.2

**2.** 升完确认版本，别只看 chart 号

kubectl -n kyverno get deploy \

  -o jsonpath='{..image}{"\n"}'

**3.** 回头收权限：把 namespaced 策略的 create 从所有租户改成平台组。补丁修的是几处检查，权限模型才是真边界

**4.** 自查有没有已经被借道写过东西。管理器字段 manager 是 kyverno，但对象不是你自己建的，就值得追一下来源

kubectl get \

  mutatingwebhookconfigurations

kubectl get \

  validatingwebhookconfigurations

// 再加 -o yaml 看 managedFields

// manager 为 kyverno 要对上来源

**5.** 开了 mutateExisting 的 NamespacedMutatingPolicy 全过一遍，重点看 targetMatchConstraints.expression 有没有指名别人命名空间的资源

## 05  一句判断

要不要连夜修，看你有没有把策略写权限发给租户。发了，值：这条链在默认安装上直达 cluster-admin，不需要任何额外配置。没发，排到本周内。但升级不是终点，同一个 apiCall 钳制 1.16.3 加进去，1.19.1 修一次，1.19.2 又修两次，说明检查副本、发送原件这个结构还在，下一份通告来得不会太慢。

## 06  POC 链接

https://github.com/kyverno/kyverno/security/advisories/GHSA-3xfv-vq8x-qhg4

https://github.com/kyverno/kyverno/security/advisories/GHSA-39w8-hv5g-f73w

https://github.com/kyverno/kyverno/security/advisories/GHSA-4pqm-wqq6-h9q2

https://github.com/kyverno/kyverno/security/advisories/GHSA-jcw5-3wcg-fqx5

说明：四份通告均附完整 YAML 与命令输出，复现环境为 kind + Kubernetes 1.31/1.34，只用到合成命名空间与对象。

**关注**不迷路，更新看得见。

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