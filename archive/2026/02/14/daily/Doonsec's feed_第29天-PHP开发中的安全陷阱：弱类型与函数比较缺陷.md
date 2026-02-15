---
title: 第29天-PHP开发中的安全陷阱：弱类型与函数比较缺陷
url: https://mp.weixin.qq.com/s/T82uFO4WxSAqzb8vr-1Bcg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:16:37.092624
---

# 第29天-PHP开发中的安全陷阱：弱类型与函数比较缺陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Byhdgj3e9qtgLPSjXgIQicZOgE718tf7Z2vGMncydRgvhFKaPTAX9YUNpp1RxDmHBXm7v1Glssia2icaQ4B2UkLkeOBkGJGmB3oP4oP6sfjicEA/0?wx_fmt=jpeg)

# 第29天-PHP开发中的安全陷阱：弱类型与函数比较缺陷

原创

萧瑶
萧瑶

AlphaNet

![]()

在小说阅读器中沉浸阅读

在PHP开发中，由于语言本身的特性，存在一些容易被忽视的安全隐患。尤其是弱类型比较和某些函数在特定参数下的行为，常常成为代码审计中的突破口。本文将系统梳理PHP中常见的比较缺陷，帮助开发者写出更安全的代码，同时也为安全审计人员提供参考。

一、== 与 === 的区别

PHP中有两种比较运算符：

· ==：弱比较，会先进行类型转换，再比较值。

· ===：强比较，不仅比较值，还比较类型，类型不同直接返回false。

示例

```php

var\_dump(1 == '1');   // true，字符串'1'被转换为整数1

var\_dump(1 === '1');  // false，类型不同

```

安全风险

在身份验证、权限校验等关键逻辑中，如果使用==，可能导致绕过。例如，当从数据库获取的用户密码哈希值与用户输入的哈希值比较时，如果使用==，可能因类型转换产生意外结果。

二、MD5 比较缺陷（0e开头的特殊字符串）

MD5加密后的结果通常是一个32位十六进制字符串。当该字符串以“0e”开头，后面全是数字时（如0e123456...），在PHP的弱比较中会被当作科学计数法，视为0×10^n，即数值0。因此，两个不同的字符串如果MD5值都以“0e”开头，用==比较会返回true。

已知的0e开头的MD5值

原始字符串 MD5值

QNKCDZO 0e830400451993494058024219903391

240610708 0e462097431906509019562988736854

s878926199a 0e545993274517709034328855841020

s155964671a 0e342768416822451524974117254469

s214587387a 0e848240448830537924465865611904

s1091221200a 0e940624217856561557816327384675

s1885207154a 0e509367213418206700842008763514

示例

```php

$hash1 = md5('QNKCDZO');

$hash2 = md5('240610708');

var\_dump($hash1 == $hash2); // true，因为都是0e开头

```

安全建议

· 使用===进行哈希值比较。

· 使用hash\_equals()函数（防止时序攻击）。

三、strcmp 函数类型比较缺陷

strcmp()用于比较两个字符串，如果相等返回0。但在PHP早期版本（如5.3之前），如果传入的参数不是字符串（比如数组），函数会报错，并返回0。这就可以利用错误返回值绕过验证。

示例

```php

$password = 'admin123';

if (strcmp($\_POST['password'], $password) == 0) {

// 登录成功

}

```

如果攻击者传入password[]=（一个数组），则strcmp报错返回0，判断条件成立。

安全建议

· 使用===进行比较，或者先验证参数类型。

· 升级PHP版本，新版本中strcmp遇到数组会报Warning并返回NULL，但NULL==0仍然为true？实际上在PHP7中，NULL==0是true，所以仍需注意。建议用===判断返回值是否为0。

四、Bool 类型比较缺陷

在使用json\_decode()或unserialize()时，如果解析后的数据中包含布尔值，可能导致预期外的比较结果。

示例

```php

$data = '{"admin": true}';

$obj = json\_decode($data);

if ($obj->admin == 1) {

// 会执行，因为true == 1成立

}

```

开发者可能期望admin字段是数字或字符串，但实际被解析为布尔类型，导致条件成立。

安全建议

· 对解析后的数据进行严格的类型检查（使用===）。

· 尽量使用json\_decode($data, true)返回数组，然后手动验证。

五、switch 类型比较缺陷

switch语句在进行case判断时，会将参数转换为整数类型（如果case是数字）。

示例

```php

$value = '2abc';

switch ($value) {

case 2:

echo '数字2';

break;

case '2abc':

echo '字符串2abc';

break;

}

```

输出结果是“数字2”，因为'2abc'被转换为整数2，匹配了case 2。

安全风险

如果switch用于权限判断，可能被绕过。例如：

```php

switch ($user\_level) {

case 1:

// admin

break;

case 2:

// editor

break;

}

```

如果$user\_level来自用户输入（如字符串'1abc'），则会匹配到admin权限。

安全建议

· 在switch前强制转换为期望的类型，或使用if-else配合===。

六、in\_array 数组比较缺陷

in\_array()默认使用松散比较（类似==），如果第三个参数没有设为true，则可能产生绕过。

示例

```php

$allowed\_ids = [1, 2, 3];

$user\_id = '1abc';

if (in\_array($user\_id, $allowed\_ids)) {

// 返回true，因为'1abc' == 1成立

}

```

安全建议

· 总是设置第三个参数为true，启用严格比较：in\_array($value, $array, true)。

七、=== 数组比较缺陷（MD5函数返回NULL）

即使是===，在某些情况下也可能被绕过。例如，当md5()函数传入数组时，会返回NULL。如果两个变量都传入数组，则两个NULL用===比较是相等的。

示例

```php

if (md5($\_GET['a']) === md5($\_GET['b'])) {

// 如果a和b都是数组，md5返回NULL，NULL===NULL为true

}

```

攻击者可以通过?a[]=1&b[]=2使条件成立。

安全建议

· 对用户输入进行类型校验，确保是字符串。

· 使用hash\_equals()比较哈希值，它只接受字符串类型。

实战案例

CTF题目

· BugKu CTF 题目72

· BugKu CTF 题目94

代码审计CMS案例

· 某CMS代码审计：从弱类型比较到RCE

总结

PHP的弱类型特性是一把双刃剑，它在带来便利的同时也引入了诸多安全隐患。作为开发者，应当：

1. 优先使用===进行比较，避免隐式类型转换。

2. 对用户输入进行严格的类型和格式验证。

3. 了解常见函数在特殊输入下的行为，合理设置严格模式。

4. 在涉及安全关键操作（如密码验证）时，使用专用函数（如hash\_equals）。

安全无小事，每一处细节都可能成为攻击者的突破口。希望本文能帮助你写出更健壮的PHP代码。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

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