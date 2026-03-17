---
title: 【Web安全】PHP反序列化漏洞
url: https://mp.weixin.qq.com/s/yYk0iISgFMyT4NiZlml5Fw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:11:26.085359
---

# 【Web安全】PHP反序列化漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nk59nEwEn2M7qgWHXGstsvwtcKMjQUORk6hLmiag3bxLSx5S8iag0UN1X9GSUMkC9xdbLghNwYGViaVjTfZ2gXlBQ/0?wx_fmt=jpeg)

# 【Web安全】PHP反序列化漏洞

H4ppy
H4ppy

安全驾驶舱

![]()

在小说阅读器中沉浸阅读

**什么是 PHP 反序列化？**

你可以把 PHP 的 “序列化” 想象成打包行李：

当程序需要把对象（比如用户信息、配置数据）保存或传输时，会把对象的属性、类型等信息“打包” 成一串字符串（比如 O:8:"UserInfo":2:{s:4:"name";s:5:"张三";s:3:"age";i:20;}），这就是“序列化”。

而“反序列化” 就是拆行李：程序把这串字符串还原成原来的对象，方便后续使用。

本来这是个实用功能，但如果“拆行李” 时没检查包裹里有没有 “危险品”，就会引发漏洞 —— 这就是「PHP 反序列化漏洞」。

为什么会被攻击？

漏洞的根源就一个：程序接收了不可信的序列化字符串，并且直接调用了反序列化函数（unserialize ()）。

举个通俗的例子：

你是酒店前台（程序），客人（攻击者）说“这是我的行李（序列化字符串），帮我拆开”。你没检查行李里是不是有刀枪（恶意代码），直接拆开，结果就出了事。

具体技术逻辑：

PHP 反序列化时，会自动触发对象的某些 “魔术方法”（比如 \_\_wakeup() 唤醒对象时执行、\_\_destruct() 对象销毁时执行）。如果攻击者构造恶意的序列化字符串，就能让这些魔术方法执行预设的恶意代码（比如删文件、读数据库）。

攻击者是怎么操作的？

1. 正常的 PHP 代码（有漏洞）

|  |
| --- |
| <?php  // 定义一个用户类  class User {      public $name;      // 魔术方法：对象被销毁时执行      public function \_\_destruct() {          // 执行$name里的内容（危险！直接执行用户输入）          eval($this->name);      }  }  // 接收用户传入的序列化字符串（无过滤）  $user\_input = $\_GET['data'];  // 反序列化（触发漏洞）  unserialize($user\_input);  ?> |

2. 攻击者的操作

攻击者需要构造一个序列化字符串，让$name 变成恶意代码（比如读取服务器密码文件）：

第一步：创建恶意对象

|  |
| --- |
| <?php  class User {      public $name = "system('cat /etc/passwd');"; // 读取密码文件  }  // 序列化这个对象，得到攻击字符串  echo serialize(new User());  ?> |

第二步：执行攻击

把得到的序列化字符串作为data 参数传入：

http://xxx.com/vuln.php?data=O:4:"User":1:{s:4:"name";s:26:"system('cat /etc/passwd');";}

程序反序列化后，会触发\_\_destruct() 方法，执行system('cat /etc/passwd')，攻击者就能拿到服务器密码文件。

漏洞防范：怎么堵住这个坑？

记住核心原则：**不要信任任何外部输入，尤其是反序列化的数据**，具体做法分 5 点：

#### **1. 避免直接反序列化不可信数据**

这是最根本的办法！如果不是必须，不要让用户传入序列化字符串。如果必须用，优先用更安全的格式（比如 JSON）替代。

#### **2. 过滤 + 验证输入**

对传入的序列化字符串进行过滤，禁止包含eval、system、exec 等危险函数；

验证序列化字符串的格式（比如长度、类名），只允许指定的类被反序列化（比如只允许User 类，拒绝其他未知类）。

#### **3. 禁用危险魔术方法**

如果不需要，尽量避免使用\_\_destruct()、\_\_wakeup()、\_\_call() 等魔术方法，或者在这些方法里不要执行用户可控的代码。

#### **4. 限制 PHP 函数执行权限**

通过php.ini 配置disable\_functions，禁用eval、system、exec、passthru 等危险函数：

disable\_functions = eval,system,exec,passthru,shell\_exec

#### **5. 升级 PHP 版本**

PHP 官方会修复已知的反序列化漏洞，及时升级到最新稳定版（比如 PHP 7.4+、PHP 8.x），可以避免旧版本的漏洞被利用。

总结

PHP 反序列化漏洞的本质是 “信任了不可信的输入，并且执行了恶意代码”。对于开发者来说，核心是 “不直接执行用户可控的代码”；对于普通读者，了解这个漏洞后，也能明白 “为什么有些网站不让你随便上传文件 / 输入特殊字符”—— 都是为了防范类似的攻击。

如果你的网站用了 PHP，赶紧检查一下有没有直接反序列化用户输入的代码，按照上面的方法加固吧！

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/nk59nEwEn2NFnIQWR9r20fFe5ddkKn1TSDia5lldroxlJic8XwVGY0dVvav9u3ib4031B8XbtG3ra0vsvIqudZEDg/0?wx_fmt=png)

安全驾驶舱

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nk59nEwEn2NFnIQWR9r20fFe5ddkKn1TSDia5lldroxlJic8XwVGY0dVvav9u3ib4031B8XbtG3ra0vsvIqudZEDg/0?wx_fmt=png)

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