---
title: 【攻防渗透集锦】漏洞组合拳与JS攻击面的博弈
url: https://forum.butian.net/share/4619
source: 奇安信攻防社区
date: 2025-10-30
fetch_date: 2025-10-31T03:08:49.095157
---

# 【攻防渗透集锦】漏洞组合拳与JS攻击面的博弈

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【攻防渗透集锦】漏洞组合拳与JS攻击面的博弈

* [渗透测试](https://forum.butian.net/topic/47)

案例挑选以往攻防、SRC、渗透项目报告有启发性报告形成文章供各位读者师傅学习,漏洞思路并不局限于接口测试，利用现有信息打出组合拳也是不错的选择

> 案例挑选以往攻防、SRC、渗透项目报告有启发性报告形成文章供各位读者师傅学习,漏洞思路并不局限于接口测试，利用现有信息打出组合拳也是不错的选择
### 转载
欢迎转载文章提供学习,但请标明社区原文地址尊重社区内原创作者劳动成果,个人公众号：月的造梦星球, 欢迎讨论学习,共同进步。
### Actuator泄露403绕过
又又又又又又是经典的不能再经典的登录框开局,习惯性的看看雪瞳接口老师傅可能已经锁定接口了`/prod-api/`接口,此接口是`springboot`端点泄露高频接口,往往在后面就放置了`env` `heapdump`转储文件等
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601062-91128894-b036-4ae9-a065-72eb22477012.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601127-c153b661-03bf-4ca1-aad8-124422d7245c.png "null")
`dirserach`全部回显`403`应该是做了`Filter`权限校验,如果是`404`肯定是路径错了比如`/prod-api/`前置或者后置需要新的这层, 那么我想办法如何绕过`403`
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601204-dc9c637e-3a1d-49f4-82cc-a5fb4910019a.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601251-eb7a98a3-f9d1-458f-ae35-82b880420b00.png "null")
让`actuator`中的`o`编码为`%6f`，但常规`url`编码是不能对`o`进行编码的,他属于 "普通字符"（不在 `URL` 特殊字符集中，不会影响 `URL` 解析所以会原样输出），因此 \*\*标准 URL 编码工具不会对 “o” 进行编码\*\*，会直接保留为 `o`，而不是转成 `%6F` ,我这里为了方便记忆才如此写下下,编码只会原样输出,正常情况下只能用`ASCII` 反推出值
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601300-ea39d1cf-b0de-4eb1-a597-6524831e9e24.png "null")
`%6f`会解码为`o`
`%6F` 是 \*\*十六进制 ASCII 码的 URL 编码形式\*\*（`%` 后跟着两位十六进制数，表示字符的 ASCII 码）。因为 `6F` 对应的十进制是 `111`，而 `111` 正是字符 "o" 的 `ASCII` 码，所以 `URL` 解码时，`%6F` 会被还原为 "o"
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601353-e247994f-410d-4423-92c5-111eee7fd3b6.png "null")
明白这一编码原理后又有读者要问了,主播主播\\*\\*`ASCII` \\*\\*反推值又自己计算十进制再转换特别麻烦，有没有简单高效的方法,有的兄弟有的,把想要编码的值交给`ai`就完事了,通过回答可以知道`r`编码后为`%72`
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601415-befb4694-b359-4574-9e68-672d2a126db9.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601480-6826fa14-1d1c-4279-9b41-33a011713e3a.png "null")
解码正确证明交给`ai`编码转换是可行的
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601556-3f6a270a-d196-47d7-aab5-6926ff9eb452.png "null")
`actuator`中的`o`编码后就变成了`actuat%6f`r 那么这样携带去访问,成功绕过发现路径还有`heapdump` `env` `nacosconfig` 信息可以打开新的攻击面还有`gateway`路由更可以尝试是否可以路由`rce`, 后续访问其他接口详情也是需要在编码基础上访问,不然也是`403`
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601613-783100be-4a88-423a-92dd-7cba9aa193c5.png "null")
```php
https://xxxxxx.com.cn:8088/prod-api/actuat%6fr/
https://xxxxxx.com.cn:8088/prod-api/actuat%6fr/env ------ 成功访问
https://xxxxxx.com.cn:8088/prod-api/actuator/env ------ 403
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1761185608461-86297477-b76f-403f-a3f2-990c7c8a44bd.png)
后面发现这款工具也可以帮助我们将字符进行`ur`编码推荐师傅下载使用,工具`github`搜索`poc2jar`即可
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1761186387221-69601057-b80a-4c38-9db9-bb17382a87e5.png)
### 小程序Host渗透后台
小程序开局,一番测试并未发现问题,鉴权做的很安全,越权、注入、逻辑漏洞均未发现,随即转变思路,尝试是否存在`web`后台地址,打开新的攻击面
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601717-c50e403d-88f1-492c-a0b1-15895e59deec.png "null")
小程序一般会有后台管理页面,可能是其他子域名下放置的404页面 或者是小程序本身`host`域名其他目录下放置,这里首先尝试将`host`放置浏览器访问
```php
https://city.xxxxx.cc/
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601767-23f578cc-be65-497d-b6a8-e30a8649bce8.png "null")
根路径正常回显那么开始上`dirserach`递归目录尝试能否发现后台地址
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601816-b5113fcc-f5c7-4b04-b5be-832c3c97d9c7.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601863-8fc41446-49c8-45ee-a668-838f73bce5cd.png "null")
也是很幸运字典加持下不到二分半就得到有效地址,`fuzz` 出第一层前置目录`manage` 携带访问后直接跳转到后台地址,那么可以测试的点就多起来,弱口令未授权,`JS`接口等等
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601915-bc3fe4a7-64fd-4263-91e0-082c1aa4a006.png "null")
```php
https://city.xxxx/manage/------>
https://city.xxxxx/manage/login?redirect=/
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967601961-7ad619dc-2f64-43ad-9c67-d7e83889b462.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602010-79454e54-17fb-4877-b978-aad1a7f233b0.png "null")
但是呢各位黑阔师傅们是否都会有先入为主的意识,我的目的就是为了找后台管理地址,现在我已经找到了,那么`dirserach`余下的会去完整的看完吗？域名下可能会设立不同的目录放置不同的登录口,耐心的看完所有信息至关重要,工具在这里又`Fuzz`出第二个前置目录,携带访问
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602075-2ccaf131-5ee3-4907-b070-21aec3c53106.png "null")
同第一个地址一样,携带第一层后就会完整的调整到新的系统,在这里发现了第二个系统为后续渗透埋下伏笔,至此`dirserch`任务完成直接X掉
```php
https://city.xxxxxxxx/backend/----->
https://city.xxxxxx/backend/login?redirect=/
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602134-b5162d20-af56-4ef3-b5bd-199ed460c10f.png "null")
回到第一个`manage`目录系统,纯粹的弱口令,后台地址藏在目录后往往也觉得这样很安全,密码设置也会相对简单,细致的信息收集找到入口漏洞往往已经呼之欲出了,查询小程序内所有用户实名信息三要素并控制余额
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602198-2fdec36e-e6d4-4ddc-808d-3b4ba6e2500d.png "null")
```php
admin/123456
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602258-7e244a1c-aebb-4a47-8b94-72ab706a7cfe.png "null")
依旧是亲切的大头照
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602322-5f55e006-0b28-49cb-bee5-05b48bcf2b56.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602375-ab240999-e2fd-4c87-8e34-3817bf6a6312.png "null")
弱口令进后台还可以挖掘其他漏洞,更好的测试接口未授权问题,已经有了管理员权限那么调用所有一遍功能再把敏感信息接口删除`token`重发即可,当我测测时就发现了 ,第一个系统和第二个系统关联处,城市合伙人不就对应了第二个系统的名称嘛,账号大概率就是手机号了
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602440-deabbd86-4b11-45ae-87d4-30d08d32712c.png "null")
来到这里通过合伙人的账号配合初始第一个系统进入到弱密码,纯粹拿下第二个系统,渗透本质依旧是是信息收集
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602520-2c7ed685-02c7-4b90-b49f-c75e24dbdba4.png "null")
```php
手机号
123456
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602580-655c406c-3832-4634-bb25-c09296a6bb8d.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602650-f489cd92-5015-4f29-b69c-2fbdf9f31e15.png "null")
### Shrio721容器Rce
渗透项目拿到大量子域名资产使用`Ehole`指纹识别发现`Shiro`框架,反手掏出压箱底的反序列化梭哈工具
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602727-dc8670b6-ac63-40a3-ae3e-ac8f8dd133a2.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602784-4c24b471-9edc-4f5f-832c-56900b4ce142.png "null")
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602838-9d81919e-434d-4fd2-8117-3d5cb3aee223.png "null")
填入地址马上给我爆破出`aeskey` 有种淡淡不详的预感,猜测可能是`docker`容器,如果爆破的时间最长一些我还不会这么觉得,地址填入不到`2s`完成给我感觉就是等着我来测呢
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602892-71f54ed6-9c02-4f1f-9197-4eeff7e2d899.png "null")
爆破一波利用链,如果是有key无链工具只能用`JRMPClient`分享其他师傅的文章工具可以去了解一下;这里出现了`CommonsBeanutilsString`这条链接,可以直接在功能区调用或者是生成内存马上线冰蝎
[Shiro无依赖链—Commons Beanutils\\_shiro 有key 无构造链](https://blog.csdn.net/weixin\_52091458/article/details/123686578)
<https://cn-sec.com/archives/2673175.html>
检测非常规利用链工具：[https://github.com/wyzxxz/shiro\\_rce\\_tool](https://github.com/wyzxxz/shiro\_rce\_tool)
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602941-05aa4b12-9175-403c-bc80-f10ea73ce602.png "null")
为了确定是否是容器执行此命令看看初始进程,如 `systemd`、`init` 或容器中的主进程）所属的 `cgroup` 信息，如果系统运行在容器中比如`Docker`），路径中通常会包含容器 `docker/abc12345` ，根据回显判断出了确实容器是容器开启的服务,哈基W......还是办不到吗....
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967602993-abe49fc6-fa41-4ca6-9709-955201a350a8.png "null")
```php
cat /proc/1/cgroup
```
![](https://cdn.nlark.com/yuque/0/2025/png/22621815/1760967603044-ab2476e2-95ff-4ef0-b5ba-b17bcda...