---
title: Web篇 | 密码重置漏洞挖掘指南：从原理到实战的完整路径
url: https://mp.weixin.qq.com/s/pHYh2DSyTyVVn-Mh8pE38w
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:51:09.804415
---

# Web篇 | 密码重置漏洞挖掘指南：从原理到实战的完整路径

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog33ScK4KzQ3ksM6rSD2c0zVyZEoiaQBKxy8w1qImHr6UHj7cu2Lf3KEnA/0?wx_fmt=jpeg)

# Web篇 | 密码重置漏洞挖掘指南：从原理到实战的完整路径

零日安全实验室
零日安全实验室

零日安全实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAFVtam88BvoJqciaibnFfJibO8vswlI7GnuYIiasyQ3j1wLia2xTMskDH09RVia2fHvykq1WCCMZgdoqjg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBPh5py6zW2zOqBr3VkB8ibrIhVe5U09T11XYdNgz6VwPgibFrnO2GRsiaicVuvdkxFmokovEP1iaaLvUQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBl8xFcbWwdAWRvgRh7IvvV2l7G4H12DKTdLfDTu0LZkKibzPCe1Zgpic0Rq8iaicD4T98WQhBA04Vx0Q/640?wx_fmt=png&from=appmsg)

目 录

> 前言
>
> 客户端状态校验不全
>
> 步骤分离与校验不足
>
> 鉴权不严使用简单可预测的用户标识符
>
> 账号与校验参数未绑定
>
> 总结

1

**前言**

密码重置功能是Web应用中最常见也最核心的环节之一，它直接关系到用户账户的安全。正因为其普遍性和高敏感性，一个细微的逻辑缺陷都可能导致整个账户体系的沦陷。密码重置漏洞核心思路为：站在攻击者的角度，尝试劫持任意用户的密码重置流程，整个过程可以概括为以下几个关键步骤：

1.初始化重置：为目标用户（受害者）发起密码重置请求。

2.拦截/篡改凭证：获取或控制用于身份验证的重置凭证（如Token、验证码、USERID等）。

3.接管流程：将本应发送给目标用户的凭证，转发或引导至攻击者控制。

4.完成重置：利用获取到的凭证，最终修改目标用户的密码。

下文将围绕密码重置漏洞常见类型与挖掘思路展开讨论。

2

客户端状态校验不全

客户端响应篡改是逻辑漏洞的常见形式。应用程序将本应存储在服务器端、并由服务器端完全掌控和校验的关键业务状态（如“是否已通过身份验证”），错误地委托给了不可信的客户端（如用户的浏览器或APP）来存储和维护。当客户端将这些状态值返回给服务器时，没有在服务器端对其进行二次验证或溯源。

1.漏洞利用

进入忘记密码，任意输入验证码抓包修改返回包中的参数状态值。比如常见的code改为0，false改为true等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3JrrmOiamT0hsKoI29N0vIPkzia0luWjh5mVKQrXn8Qp8sCV8eeic10OAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3QHNXTpgayupicPYh6icibWBZxGDQicPL9Zibx3sGCZib3sKUL3vI5nWycxWQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3zYpeSYuOuSoKYV17nPsQOEtibgDl8Yw3utydgoj6aPnvicdUMGGBMI4A/640?wx_fmt=png&from=appmsg)

下来正常输入新密码点击下一步抓包，继续修改响应值，成功重置密码。

2.挖掘思路

1）寻找目标场景

前台忘记密码，找回账号等诸如此类的功能。如前台没有对应忘记密码功能，可以从前端js中提取接口进行测试。

2）测试服务端是否缺少校验

通过修改客户端返回的状态值（例如将“verified”：false改为“verified”：true），看服务器是否仅依据此值判断步骤是否完成。

3

步骤分离与校验不足

密码重置往往涉及多个步骤（如身份验证、Token验证、设置新密码），如果步骤间状态校验不足，可能绕过关键验证。

1.漏洞利用

本地搭建Dedecms（版本5.7），创建账户test1以及test2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3AZoDjBVZbhIzed4fV6dLDiauFpPNtLetvBVNQ7etEniao80WJYrGxfBA/640?wx_fmt=png&from=appmsg)

登录test1账户，随后构建payload，id修改为要修改的账户的id

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3HjIORgfXEKCkQkiczDUH4PcQYkCxLrY8XboNAfaUBrnZ6KzcYC5JibVg/640?from=appmsg)

发送请求获取key，成功获取key值后即可修改目标账户密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog34Kg9DVpSMUuvNWyCfnWJDKEPVkPSO9YjWF99IcpqXpmXJCqTU0UeEg/640?wx_fmt=png&from=appmsg)

2.挖掘思路

1）测试步骤间状态关联性校验

尝试直接访问重置流程的各个步骤的URL（例如／reset/step2、／reset/step3），而不完成其前置步骤。观察系统是否允许直接跳转至后续步骤，并在后续步骤的请求中，缺乏对前置步骤已完成的验证（例如，缺少一个能证明你已通过第一步验证的Token或Session标识）。

2）操作参数以便越权至其他用户

分析每一步请求中用于标识状态或用户的参数（如 user\_id、temp\_token、session\_id）检查其是否可预测并尝试修改这些参数（例如递增或递减user\_id）以查看是否能切换到其他用户的重置流程，随后检查其是否在步骤间保持一致，第一步生成的Token或Session标识，是否在第二步、第三步的请求中被正确校验并与当前用户绑定。

4

鉴权不严使用简单可预测的用户标识符

许多系统在对用户身份进行认证时，会使用简单的参数作为用户的唯一标识，缺少鉴权，而这类标识容易被攻击者预测。例如，某些系统直接将USERID作为用户密码重置时的标识，攻击者只需枚举其他用户的USERID即可重置其他用户密码。

1.漏洞利用

针对某购物网站进行包监听时发现某接口的响应如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog34lfY6ibZYhibWtIdUXEBsicFTze6HDnmPoUqOOKOWygKfPEmspHc2klVQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3a0E97z04KLBmZynIeAqouI2dGVsWnlZpx7wMREhZOBNqVNKwc88wwA/640?wx_fmt=png&from=appmsg)

在响应体中，包含如下参数：

“showResetPassword”:false,“showModifyEmails”:false，参数值表示用户角色禁用了密码重置和电子邮件修改选项。在burp中对该流量包进行拦截，并修改响应包。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3MPGenBFEunTAISJpouJu5UEzkhWia2EwEWBI2y1vQnmhhBaZygkTGMw/640?wx_fmt=jpeg)

刷新页面后会发现两个新选项：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3ObdpY1PQxpbaicsmCPichRA5xTsQxvF2xT8FoSNJpfQYhF9Vvp1JvYrQ/640?wx_fmt=png&from=appmsg)

此处后端接口返回JSON字段“showResetPassword”:false仅用于前端UI决策，未在后端任何鉴权逻辑中二次校验。攻击者通过篡改响应包为“showResetPassword”：true，即可让前端渲染出重置密码按钮。

随后对所拥有的账户进行密码重置修改，系统返回200并提供了有效密码重置链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3agXsMSQfV3iaT5OqyesW5SQaPib5pgAm254wh0u6ocvPiagbNYgLX40Hw/640?wx_fmt=png&from=appmsg)

访问后发现密码重置成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3FoscYnXjOJgRNqZMbUiaEqw8KMFJRnd6HC2KGp0HHEPFrSAmMFNHwiaQ/640?wx_fmt=png&from=appmsg)

拦截密码重置接口包，发现请求中包括用户的数字ID，其请求体仅包含：{“userld”:9438868,“resetAccessKey”:false}，没有其他的鉴权参数。该端点未检查当前会话是否具备对userld的操作权限，也未校验当前用户权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog39OIsD478cw70sHngicS4jcJ32hF0MwDvVWq1Jic4x6xIsPgYVHaicD5rg/640?wx_fmt=png&from=appmsg)

重新抓包，将USERID修改为另一个账户USERID，密码修改成功并成功登陆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3jxAMaab2jHnfbPm6g53ia2ay9HUJdCt7fic9KrS6s2lwYm5qic5QjpSmQ/640?wx_fmt=png&from=appmsg)

系统采用可预测、单调递增标识符使用连续数字userld，此时攻击者只需遍历整数区间即可批量枚举有效用户，重置其他用户的密码。

2.挖掘思路

1）收集令牌样本

通过直接请求，找到应用程序中生成令牌的功能点（如密码重置、邮箱验证、会话ID分配），并反复触发这些功能。应用程序在日志、调试页面或错误信息中也会意外泄露其他用户的令牌。

2）分析模式与结构

拿到样本后，首先观察令牌由哪些字符组成？（仅数字？数字+大写字母？数字+大小写字母？是否包含特殊字符等）。观察编码方式（如Base64、Hex、Base36。随后尝试解码，对令牌进行常见的解码操作。解码后的数据可能显示出更明显的模式（如时间戳、序列号或特定结构）。最后分割对比，将多个样本放在一起，对比每一位字符的变化情况。寻找其中固定不变的部分和规律变化的部分。

3）破解生成算法

如果令牌是纯数字，且样本值接近当前时间，可能是时间戳（10位或13位）或时间戳的简单变换（如乘以一个系数），你可以记录获取令牌的时间，与令牌值进行比对；如果令牌是32位或64位的十六进制字符串，可能是MD5或SHA-256等哈希值，也可以尝试在前端源码中下断点去破解生成密码的算法等。另外可以尝试猜测其原始输入（如用户ID+时间戳、邮箱+固定盐值），并进行哈希比对。如果你能获得足够多的连续输出，就有可能推断出内部状态并预测后续值。

5

**账号与校验参数未绑定**

密码重置流程通常需要向用户发送验证凭证（如Token、验证码），如果接收端参数由客户端提供且可篡改，则可能导致凭证发送至攻击者控制的地址，下面将结合案例进行说明：

1.漏洞利用

案例一：接收端可篡改，请求包中包含接收端参数，可将凭证发至指定接收端。

密码重置页面，输入任意普通账号，选择邮箱方式找回密码。在身份验证页面点击获取短信验证码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3P9HmmzCbJkYJuX4qgLs16usticbGMKiaskicPAqqJ84XlLFROe6px9v8A/640?wx_fmt=png&from=appmsg)

拦截请求，发现接收验证码的邮箱为请求包中的参数，而此参数可控，直接篡改为攻击者的邮箱，此时攻击者成功接收邮箱验证码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog39ZeHAFVtibPmkQoa8XyrRmxNUhUyWG6ctH55UW6ClgiaWylHuN416Jhg/640?wx_fmt=png&from=appmsg)

提交验证码后抓包修改其中邮箱为获取验证码的邮箱。此时仅校验了验证码与邮箱是否绑定，只要输入止确的验证码即可通过验证。下来正常执行3、4步即可成功重置该账号的密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3GQpTFlEib3aHNx23J5ozWcwmzKsQMRulMkttMlIBaTF9UtEw39QmMpw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3szcmgq0FP3wDdnQyibkicEp2TzMQgrAib1MMJ7hPqlqMHCLicAqQEEtRIA/640?wx_fmt=png&from=appmsg)

此处漏洞形成的主要原因就是服务器未绑定实际要重置得账号和验证码，导致输入其他用户邮箱正确的验证码也可以董置当前用户的密码。

案例2：验证码转发

在测试任意密码重置时，可以尝试在关键参数后面添加多个参数，转发验证码到攻击者。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3TM8JZ4o3Ada9AyuIYMFLiaBnFD58ntukEbd1XLe22jQxsqAaXK0mwGQ/640?wx_fmt=png&from=appmsg)

攻击者收到验证码后直接填写验证码即可完整密码重置，修改受害人密码。

案例三：利用校验正确验证码或者其他校验获取到正确凭证后，在凭证有效期内实现重置其他用户密码

在密码重置流程的关键步骤（获取验证码、校验验证码生成凭证、使用凭证重置密码）中，使用重置密码凭证执行最终重置操作时，服务端没有严格校验和绑定令牌与最初申请者的身份关系，仅仅校验令牌是否失效或者是否使用。导致攻击者可以利用此缺陷，将本应属于用户A的权限“转移”或“应用”到用户B身上，从而实现越权操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog383sPMEBIcCiaDSjPxmB8PiavGTQJmsjYKaITibyBfVfEL5D6VibSnaAKibg/640?wx_fmt=png&from=appmsg)

当用户已经验证过验证码，在正确验证有效期内攻击者同时做重置密码操作，此时可以利用令牌未失效的情况下实现任意密码重置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3gsiaL4aXNWBmicJkphBFsR0vdDgG4NJAG2q3tTjIS22xZROQIAfdBRQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3qLuS0vtkEVLrGCAic8ictommCn31iag4qoEH8TXoATmD59LP0vs8knaLA/640?wx_fmt=png&from=appmsg)

输入正确验证码后会触发校验接口，获取重置当前密码的凭证。另一个账号同样按以上方式操作，利用获取到正确凭证的间隙。回到攻击账号输入新密码抓包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3lGYsYyyJaoyzIU3WJAcCPe86iaXSUmsl7eeyXkoQH4uNlKOia6s0HXmQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xA402kbt7ibpsLcnCfOBUog3SW0yniboHp2E604QSPBAp1leQLgbVs9HiaO2TCSEu3Snx4UgJgoYumicA/640?wx_fmt=png&from=appmsg)

看到其中有控制要重置账号密码的参数，修改此参数为受害人的参数即可重置其他用户的密码。

2.挖掘思路

1）还原正常的密码重置流程

记录关键...