---
title: AI在渗透测试中的应用案例三则
url: https://mp.weixin.qq.com/s/RpxKwJ8Klr4E2tGBQon73g
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:02:07.687135
---

# AI在渗透测试中的应用案例三则

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuaajsQETGPLjfmEjXsDADGRaRFxPoOnzickdUj6yDVBLENrPdaJPoXosjdkj0zY9xhmx75bGOM6nWw/0?wx_fmt=jpeg)

# AI在渗透测试中的应用案例三则

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于only security
，作者f0ng

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yj3verSrnsiciaXgH6ib5Richdr5IC7oxeRUB5ZvuOkp39g/0)

**only security**
.

分享日常笔记、所思所想

AI 已经成为工作中非常高频的效率工具。在安全测试场景里，它不只是“写代码更快”，更重要的是能把一些重复、耗时、容易掉坑的环节（脚本拼装、语句试错、源码定位）显著压缩到可控范围内。下面分享 3 个笔者在项目里实际用过、且效果比较“立竿见影”的案例。

主要通过三个案例来分享下

* 0x01 加解密接口自动化
* 0x02 Oracle 注入构造
* 0x03 源码分析[小程序]

## 0x01 案例一：用接口示例“投喂” AI，让它生成可落地的 `autodecoder` 加解密接口脚本

### 背景

遇到一个带请求加解密的站点，需求是：根据现有加解密逻辑，尽快写出可用于渗透测试的 `autodecoder` 脚本。

每次遇到这种需求，我都“又期待又厌倦”：期待的是逆向过程可能有新挑战；厌倦的是逆向完成后，把逻辑封装成可用接口脚本往往很枯燥——重复、重复、再重复。

最近一直在用 `cursor`，于是有个想法：把“接口模板/示例”直接交给 AI，让它按模板把整套加解密脚本补齐。实践下来，通过几轮对话就能生成**可直接运行**的脚本。

### 逆向结论与输入信息整理

费了一些时间逆向请求包加解密逻辑，整体是常见的 `AES-ECB` + `SHA256` 计算 `sign`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhia2XSRyxocFsSANEmQ6jPGfzm3S6skibGzpick8c4g9dLyntRA2sUhlOmw/640?wx_fmt=png&from=appmsg)

配合 AI，先产出一个“单向脚本”（能加密/能发包，但不够工程化）。

但在实际测试中，单向脚本仍然很浪费时间。因此结合我的插件 `autodecoder`，需要把加解密逻辑**接口化**。这次的加解密还涉及请求头，所以我用的是 “header 示例脚本” 作为模板。

我的提示语如下（把模板关系、入参/出参格式讲清楚）：

```
@flasktestheader.py 这是一个工具中转脚本，把 @autodecoder-xx.py 的逻辑作为请求头 signature 的值，把 @flasktestheader.py 的逻辑作为明文数据加密的逻辑，按模板修改相关值；明文数据即为脚本里的数据，密文格式为 {"version":"xxx","time":<当前时间戳13位>,"data":"密文数据"}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiabQdGiasicricgtIhhm0KW0Q5MLy1LrJ4fUkicGAmOzF705gaVrkocLq60Q/640?wx_fmt=png&from=appmsg)

生成脚本的效果非常出乎我意料：`sign` 计算正确、明文加密逻辑也正常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiavXCCfdkl86lPhTJIzByccicdesl11LjkMuCunAC25DXEJuLBic7aGgCQ/640?wx_fmt=png&from=appmsg)

不足之处在于我没有把 `sign` 的更新规则说明清楚，导致脚本每次请求都会“无脑新增 `sign`”。于是我补充了一条明确的修改要求：

```
@flasktestheader.py:56 修改一下逻辑，如果headers获取到了sign那么就修改参数，如果没获取到sign，那么就新增
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaWJBbrdMjtIUkVGvoJo7Qlhg3jhJInK0NKDfepZZonAm1icDFDdc77Fg/640?wx_fmt=png&from=appmsg)

这次生成的接口脚本已经相当成熟，但解密逻辑还不够清晰。

第三轮，我把解密入参格式明确出来，让 AI 把解密流程补齐：

```
补充解密逻辑 @flasktestheader.py:92 ，传入的 body 密文为 {"version":"xxxxx","time":1665165125576,"data":"xxxxxxxxxxx"} 格式，提取其中的 data 进行 aes_ecb 解密得到明文
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaWJBbrdMjtIUkVGvoJo7Qlhg3jhJInK0NKDfepZZonAm1icDFDdc77Fg/640?wx_fmt=png&from=appmsg)

解密逻辑验证成功：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhia73qymXnibPiaCxuUNpwjxlxU1OSy5IVkV1ibnOsrIfDoGibYtvndQVxH5w/640?wx_fmt=png&from=appmsg)

到这里，就可以把加解密完全交给 `autodecoder` 接管，后续测试流程会轻松很多。

### 案例小结

这个案例里，AI 的价值不在“懂 AES/SHA256”，而在于：

* 把你已经逆出来的结论快速工程化：按插件模板生成可用接口脚本
* 降低重复劳动：尤其是请求头、签名、时间戳等细节拼装
* 通过“迭代式提示”补齐边界条件：比如 `sign` 的更新规则、解密入参格式

## 0x02 案例二：让 AI 帮你一步步构造 Oracle 注入语句（从“报错很怪”到可用 payload）

### 背景

在一次项目中遇到一个 Oracle 注入点。由于拼接方式导致 Oracle 报错很“奇怪”，我无法按常规套路继续推进。于是借助 AI（`aistudio.google.com`）迭代构造语句，最终拿到可用 payload。

### 确认注入点与自动化失败

首先能判断注入点存在：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaJ7RiaJyqXdibYzVF4Wt8heqFRKVasS71XeVRSic0Kd40Jia413JXabDOmQ/640?wx_fmt=png&from=appmsg)

接着我想直接丢给 `sqlmap`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaPuoJRsCwX37QoOjEZdtP4UdrpbjEdvZqM5ZSOdEgKrCfQcxmtgDVTQ/640?wx_fmt=png&from=appmsg)

结果直接报错 `forbidden`。

OK，不慌。`sqlmap` 成功率本身就不稳定，`403` 大概率是 WAF 拦截。

### 绕过 WAF + 与 AI 迭代收敛

先生成“脏数据”用于绕过：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaiaPVib9zmAAZMNShEUd4EM6YQfeXpeFlMBtdiaa43NUESndC2xUkzVgHA/640?wx_fmt=png&from=appmsg)

把脏数据填充到 POST 体中，尝试绕过。

没加脏数据之前，直接 `403`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhia9PdEvlKXRmO01chZRP9Pg7Sk2buBcBPWpYunTL0KKiao3wNTHUZibLkw/640?wx_fmt=png&from=appmsg)

加脏数据之后：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhia6T74U3h2wCdSx50nDTMjzG6Qr3TCcP35nOVNvYBwuWke8BGIsTrLGA/640?wx_fmt=png&from=appmsg)

再丢给 `sqlmap`，依旧失败（指定 Oracle 也不行）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiagWVfjbiaSefDoT2sSa1d3KjLo2CfAzu1iamLnLSwdreAbLRoTevMR60g/640?wx_fmt=png&from=appmsg)

只能手工注入。但这个点比较“诡异”：以前常用的语句在这里要么不起作用，要么报很奇怪的括号错误，比如 `ORA-00907: 缺失右括号`。

于是去请教 AI（对话前半段略，这里从关键提问开始）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiagWVfjbiaSefDoT2sSa1d3KjLo2CfAzu1iamLnLSwdreAbLRoTevMR60g/640?wx_fmt=png&from=appmsg)

AI 给出建议；我把响应结果同步给它，继续提问：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiavJibKzU94zn0ibpdp41bIx1mfVNh5Rt0UiatBRS3gdCAmoEej6BhrEtiag/640?wx_fmt=png&from=appmsg)

它让我继续尝试（忽略这里被 WAF 拦截；当时确实还没完全绕过，比较尴尬）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaJT2oy5krB8eiavAuIFnsGK2EkyK6aTdAzchVezvmYcZ8QPpBjsbODXA/640?wx_fmt=png&from=appmsg)

成功绕过 WAF 后，子查询变得可用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaRIpAz0zohhw6MOZiaJUoe0fI5OGxjeRoJJJ0ic7Uo86dXexeBfXRRovA/640?wx_fmt=png&from=appmsg)

直接用了推荐的 payload：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiagAxR3QibE3UCTDDAyzwTWguIicIImz4A9oZ66uGYQVCicm5V8hotflGlQ/640?wx_fmt=png&from=appmsg)

但这里出现一个问题：AI 给的 payload 全都是“页面正常响应”，不利于判断布尔条件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiazvr8uLdLicDmoiapz30VhIdZ81acGkicGRjQW16cIupMDcmYtqzFxPong/640?wx_fmt=png&from=appmsg)

AI 又建议尝试查询不存在的表来制造报错，但依然无法直接注出数据；后面的语句还直接报错 `ORA-00920: 无效的关系运算符`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhia3onkk7DtOMavj7sNdRSGk4EsSo0Bzialybc9d5o1t7CB4XeW8tK2vhw/640?wx_fmt=png&from=appmsg)

它让我尝试 `'+or+1=(select+user-1+from+dual)+or+'1'='2`，确实能触发报错，但没有把用户名带出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaSvkZvDFqEZVI32n2PvkDJ3iaVDXtxwqdk3GbajphWibRHfO1WiaqHvajg/640?wx_fmt=png&from=appmsg)

最后一次关键回复如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiadfrVCfRS1J9VOOC9mHQUDSibehXA7H6WCJqibx17BNEAueZcQoEha16A/640?wx_fmt=png&from=appmsg)

这里需要纠正一点：AI 给的 payload 里有两个 `or`，在实际环境中风险较大（导致条件过宽、触发大量数据遍历）。更稳妥的做法是把第一个 `or` 改成 `and`，最终得到可用 payload：

```
'+and+1=(select+1/0+from+dual+where+ascii(substr(user,1,1))=100)+or+'1'='2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiayDfhYN54JdbC3Cl7fu3cLibibKF877MibxMTOMibgDBVFUGnicAqxOqmM6w/640?wx_fmt=png&from=appmsg)

### 案例小结

这个案例里 AI 更像“有耐心的协作者”：

* 快速给出多种 Oracle 语句变体，减少你在语法坑里反复试错的时间
* 在你提供回显/报错后，能持续收敛到可用表达式
* 但要保持安全意识：AI 生成的 `or` 结构不一定“稳”，需要你做风险控制与最小化条件

## 0x03 案例三：直接让 AI 读源码——定位加解密算法、快速理解接口与资源访问方式

拿到小程序反编译代码后，我一直不太喜欢分析小程序的加解密：一来在控制台操作可能有封号风险；二来小程序调试链路比较折腾，有时候不得不请教朋友帮忙（在此感谢鸡哥）。

后来有了 AI，就在想：能不能把“源码定位/逻辑梳理”这类体力活交给它？于是有了下面两个小案例。

说明：这里的例子代码**没有做重度混淆**，如果混淆很深，成功率可能会下降。

### 0x031 分析加密参数算法（从 URL 反推参数加密位置）

#### 背景

小程序请求里有加密参数。Web 场景我还愿意打断点慢慢抠；小程序就确实不太想硬抠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiax7qBWFgFH8fDrarp8IotQzian8HibziboNsRkmP57VSuxnp2r1KEYB8Qg/640?wx_fmt=png&from=appmsg)

很明显关键 `id` 参数被加密了。简单搜了一圈加密关键字没找到密钥和 IV，于是直接把源码拖进 `cursor`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaUytxdBzPxTFdV8OoOlfib8HB7vywickxicibv2DgkRul1NFGZC14NicNkJw/640?wx_fmt=png&from=appmsg)

直接问它一个明确问题：

```
这是一个小程序的源码，我想要找到https://xxxxxxx/xxxx 这个url的加密参数，请告诉我答案
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaUytxdBzPxTFdV8OoOlfib8HB7vywickxicibv2DgkRul1NFGZC14NicNkJw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaKluMo0W9RA24feGN8aeGDaLNibNYV6yIYr6KY5JWtsBSSTjMGhho15Q/640?wx_fmt=png&from=appmsg)

它很快就把关键位置、加密流程与入参指出来了。我把结论丢进 `autodecoder` 里复现验证：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FYb6AdABfia3jamM3JqwjayzOGP4uzLhiaYBYLjDWtzj9jtd3JcicickyicSCCARllXfh4aW2KthicXQko60ibFia9Gxtg/640?wx_fmt=png&from=appmsg)

结合案例一的“接口脚本生成”，实测一个接口从“定位逻辑”到“在 `autodecoder` 里跑通”，大概 1 小时左右就能完成闭环。

### 0x032 分析接口与资源访问方式（从上传响应推导访问 URL）

#### 背景

需要对一些接口做测试，但新系统刚拿到手时往往并不了解业务逻辑。比如上传文件后，响应只返回文...