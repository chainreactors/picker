---
title: 大模型在漏洞挖掘中的“逻辑跳跃”问题与解决方案
url: https://mp.weixin.qq.com/s/R6Dnc2CW_OlxVTv-t1vg1g
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:34.835022
---

# 大模型在漏洞挖掘中的“逻辑跳跃”问题与解决方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VRdT0HGxjvAFF5ld9ex1z3KAP4OJ8bnqUArh1s5dmyDEnic6VYM7oLIM7icGconIRy8EKvO94jChZiavJq9iaqgxk5uicibs6jIicrg8cpFtUdERjg/0?wx_fmt=jpeg)

# 大模型在漏洞挖掘中的“逻辑跳跃”问题与解决方案

原创

做安全的小明同学
做安全的小明同学

大山子雪人

![]()

在小说阅读器中沉浸阅读

# 大模型在漏洞挖掘中的“逻辑跳跃”问题与解决方案

在使用大模型进行代码审计时，经常会出现一种“看起来合理，但实际错误”的分析：

**模型阅读代码后做了语义总结**
**基于总结构造攻击路径**
**得出“漏洞成立”的结论**

但问题在于：
`中间关键推理步骤没有被代码证实,或者没有逻辑依据支撑。`

## 问题起源

在用agent分析某个app的代码时，给出了这样一条答复：

![](https://mmbiz.qpic.cn/mmbiz_png/VRdT0HGxjvDibhvHt6Q3YEKUQrsrNX6zdclXYgNUlzHKSgXaq6C1nxaYhGLy1mO5r51rOu6x2UJt5RuDdloY5LibBg14zPI2twpWdBpwZdKrk/640?wx_fmt=png&from=appmsg)

有一个很明显的逻辑推理问题:
事实A: `白名单: 只有当包名等于 com.samsung.android.bixby.agent 时，才允许继续执行。`
与
事实B: `那么对于 Bixby 路由来说，调用者（Referrer）就变成了浏览器自己。`
得出：
结论C: `从而绕过校验`

显然浏览器的包名并不是com.samsung.android.bixby.agent，也就是`绕过校验`的结论不成立。

当我把原样的回复内容发给chatgpt时，大模型可以发现此类逻辑不一致的点

![](https://mmbiz.qpic.cn/mmbiz_png/VRdT0HGxjvCHk461iaNvga3vuP5nicgknWictkd02lOXsyzjXkY9LNpAMCgK1ibMxzvBsibm2Sn6jZzZXicfZodmtYJULmTpYh3K45zNJLKlQRXX4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VRdT0HGxjvAo70gYv6b4FwWaM1ZzOpLPYgvvoibJRWKOCTOOibC3qTtKE6iaArnbicZc250r1ricFQgn2b88N0nstX59g1ya5GkmF9PyI5TNMBEQ/640?wx_fmt=png&from=appmsg)

当我指出存在逻辑问题以后，

• **问题一：容易不切实际的幻想**

![](https://mmbiz.qpic.cn/mmbiz_png/VRdT0HGxjvAqsbro8EDIO9EUmc4DyRWD4SJ2kTExCWcJ24pFTdKWx2ic0VeFFxl2avz2aIN7ol2ibJqMZJaw9khcRGcOaldEG4pG4yI0jFbGc/640?wx_fmt=png&from=appmsg)

比如用了`关键点`，`死穴`等一系列夸张的措辞，而且漏洞存在的假设条件更是出奇的离谱

* • **问题二：代码逻辑审计不严格**

![](https://mmbiz.qpic.cn/mmbiz_png/VRdT0HGxjvCW5fuHn1Slibb32IicT6draFsqSHRKKTSnh8icibom0LeEpKPoF3O9l24M2icJKlNzjNibWWMN4z4jdxRfs4QgWXkNub2lo98Y5QX3Q/640?wx_fmt=png&from=appmsg "null")

实际代码是

```
    private booleanisAllowedPackage(Intent intent0) {
        if(!GEDUtils.isGED() && "android.intent.action.VIEW".equals(intent0.getAction())) {
            varuri0= (Uri)intent0.getParcelableExtra("android.intent.extra.REFERRER");
            Strings= intent0.getStringExtra("android.intent.extra.REFERRER_NAME");
            intent0.removeExtra("android.intent.extra.REFERRER");
            intent0.removeExtra("android.intent.extra.REFERRER_NAME");
            Strings1=this.getReferrer() == null ? null : this.getReferrer().getHost();
            intent0.putExtra("android.intent.extra.REFERRER", uri0);
            intent0.putExtra("android.intent.extra.REFERRER_NAME", s);
            if(s1 != null && "com.samsung.android.bixby.agent".equals(s1)) {
                returntrue;
            }

            androidx.compose.runtime.changelist.a.v("NOT allowed package : ", s1, "BixbyLauncherActivity");
        }

        returnfalse;
    }
```

实际上用于判断的package name来自于getReferer调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VRdT0HGxjvCXGicwzPQvtvkn1K9P4TAIrGDDrYZicrga2nJsliaHo5oJzEJvlZgJn0y1PXDNQUAjxNjWyyDYNTM1Vq7iaFqM7jh9XslEZPUHhiaQ/640?wx_fmt=png&from=appmsg)

从以上两个误诊的问题来看，大模型有能力识别正确，但回答总会出现逻辑推理不依据事实，没有实事求是，说大话。需要进行审计，纠正。

## 问题根因

### 模型把“局部合理”串成了“整体成立”

这个例子里，错误不是知识点完全错了，而是推理链里有一段“默认成立”了：

* • BixbySBrowserLauncherActivity 只信任 com.samsung.android.bixby.agent
* • SBrowserLauncherActivity 可被外部调用
* • 同 APK 内可能转发
* • 于是 referrer 就能变成“可信来源”

问题就在最后一步,`“会转发”不等于“转发后 referrer 一定满足白名单”。这是典型的桥接推理偷换。`

代码逻辑：

```
String s1 = this.getReferrer() == null ? null : this.getReferrer().getHost();

if(s1 != null && "com.samsung.android.bixby.agent".equals(s1)) {
    return true;
}
```

模型错误推理：
读取 EXTRA\_REFERRER → putExtra 透传 → referrer 可控 → 绕过校验成立

`问题一：把“相关变量”当成“判定变量”。s1是判定变量，EXTRA_REFERRER只是相关变量，把“看起来相关”当成“真正参与判定”。`

`问题二：没有验证数据流是否闭合。看到 referrer → 假设可控 → 推断绕过成立。缺失关键步骤：数据流闭合验证。`

`要避免这类问题，核心不是“多问一句”这么简单，而是要让模型在输出前，强制做一次链路断点检查。`

### 为什么大模型容易犯这种错

因为它很擅长：

* • 补全常见攻击路径
* • 生成形式上流畅的安全分析
* • 把“像漏洞”的东西讲得很像真漏洞

但它不天然擅长：

* • 对每个边界条件做机械式校验
* • 在证据不足时主动降级结论
* • 区分“可构思攻击链”和“已闭合攻击链”

`所以在安全审计场景里，最需要的不是更会说，而是更会刹车。`

## 一套实用的纠偏方法

可以把这类分析任务固定成 4 步：

### 1. 先拆成“事实”与“推论”

要求模型明确区分：

* • 已知事实
* • 待验证推论
* • 最终结论

比如这里：

* • 已知事实

+ • Activity exported
+ • 存在 getReferrer().getHost() 白名单判断
+ • 白名单是 com.samsung.android.bixby.agent

* • 待验证推论

+ • 外部可控 getReferrer()
+ • SBrowserLauncherActivity 会转发到目标 Activity
+ • 转发后 referrer 会变成满足白名单的值

### 2. 强制检查“因此”前面的每一跳

“这一跳是代码已证实，还是我脑补的？”

在这个案例里，“由同 APK 内转发，从而绕过 referrer 校验”，这句话至少包含两跳：

* • 是否真的存在转发
* • 转发后 referrer 是否真的变成白名单值

`两跳都没证实，就不能直接下“可绕过”的结论。`

### 3.输出时附一个“最薄弱环节”

让模型每次给结论时必须附带一句：“本结论最依赖的未证实前提是：XXX”
比如这里最薄弱环节就是：

* • getReferrer() 是否可被攻击者伪造
* • 中转 Activity 是否会保留/覆盖/生成符合白名单的 referrer

`这句话特别有用，因为它能把“貌似确定”变成“可验证假设”。`

### 4. 不直接说“存在漏洞”，改说“漏洞假设等级”

你可以让模型按等级输出：

* • 已证实：代码或实验已直接证明
* • 高概率：只差一个小验证
* • 可疑：存在思路，但关键链路未闭合
* • 不成立：中间逻辑断裂

在这个例子更合理的表述其实应该是：

存在可疑点，但当前绕过链条未闭合，不能直接认定可利用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWazKsIWjXCnhRSkicjTAibMTM9LyJeIE2Jib0oHpGwhicp1z8zxWFk7jBC7gswGMFSXTRlJzl5bjfzPeA/0?wx_fmt=png)

大山子雪人

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWazKsIWjXCnhRSkicjTAibMTM9LyJeIE2Jib0oHpGwhicp1z8zxWFk7jBC7gswGMFSXTRlJzl5bjfzPeA/0?wx_fmt=png)

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