---
title: CTF之文件上传——你知道我在你的服务器上放了什么吗
url: https://mp.weixin.qq.com/s/zWrjMgrpT_QLbGnIip78aw
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:46:59.180340
---

# CTF之文件上传——你知道我在你的服务器上放了什么吗

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIzE7zPyr5gI9B4Lg2qnwJOLckSCM1CvKL6I2DzHgWWxFlUMao4GjS4Cbo3v6mE1YwCdfgq2g7GLSGhhg5gakiaOwII3Q6BPQLUE/0?wx_fmt=jpeg)

# CTF之文件上传——你知道我在你的服务器上放了什么吗

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、什么是文件上传

在网站的日常运营和内容更新中，文件上传功能扮演着不可或缺的角色。它允许管理员或用户将图片、文档、脚本等文件传输至服务器，以丰富网站内容或实现特定功能。然而，这个看似普通的功能，若缺乏严格的安全限制或限制措施被轻易绕过，便会成为攻击者入侵服务器的“特洛伊木马”。攻击者可以利用它上传可执行文件、WebShell脚本，从而逐步获取服务器的控制权，最终导致服务器沦陷，引发数据泄露、服务中断等严重后果。

导致文件上传漏洞的原因复杂多样，主要可以归纳为以下几类：

1. **文件路径截断**

   ：服务器或应用程序在处理上传文件的路径时，未能正确识别和处理特殊字符（如空字节%00），导致攻击者可以截断路径，绕过文件后缀检查。
2. **文件过滤不严或被绕过**

   ：服务器端对上传文件的类型、内容、MIME类型等缺乏有效校验，或校验逻辑存在缺陷，使得攻击者能够通过修改文件头、后缀名等方式轻易绕过。
3. **文件解析漏洞导致文件执行**

   ：Web服务器（如Apache、IIS、Nginx）在解析文件时存在特定的逻辑缺陷或配置不当，导致非预期后缀的文件被当作可执行脚本处理。
4. **服务器配置不当及系统“特性”**

   ：服务器的默认配置或某些文件系统的“特性”被攻击者利用，从而绕过安全限制，实现恶意文件的上传和执行。

# 二、绕过方法

## （一）客户端验证绕过

这是最基础也最容易被攻破的防线。许多网站为了用户体验，会使用JavaScript在客户端对上传文件的后缀名进行简单检查。然而，这种验证方式完全依赖于浏览器，是极不安全的。

攻击者可以轻易通过以下两种方法进行绕过：

* **禁用JavaScript**

  ：在浏览器的开发者工具或设置中直接禁用JavaScript脚本的执行，即可绕过前端的文件类型检查。
* **使用Burp Suite抓包拦截**

  ：这是更专业和常用的方法。攻击者使用Burp Suite等代理工具拦截上传请求的数据包，然后直接修改其中的`filename`参数，将恶意文件的后缀（如`.php`）替换为允许的后缀（如`.jpg`），再转发数据包，即可成功上传。

## （二）服务器验证绕过

### 修改Content-Type头

虽然这是在服务端进行的验证，但其可靠性并不高。服务器通过检查HTTP请求头中的`Content-Type`字段来判断文件类型。攻击者可以通过Burp Suite拦截请求，将恶意文件的`Content-Type`（如`application/octet-stream`）修改为合法的图片类型，例如`image/gif`或`image/jpeg`，从而绕过检测。更高级的技巧是，在恶意脚本文件的开头添加图片文件的“幻数”，例如在PHP木马前添加`GIF89a`，使其在文件头校验时也能伪装成一张正常的GIF图片。

### 黑名单过滤

黑名单过滤是一种“堵”的策略，即列出所有不允许上传的文件后缀。然而，这种方法存在天然的缺陷：无法穷尽所有可能的可执行后缀。以一份常见的黑名单为例，它可能只禁止了`.php`、`.asp`、`.jsp`等后缀。攻击者可以尝试上传`.php3`、`.php4`、`.phtml`、`.cer`、`.cdx`等同样能被服务器解析执行的后缀。此外，还可以利用一些特殊技巧进行绕过，例如：

* **大小写绕过**

  ：在Windows系统下，`.PHP`、`.PhP`与`.php`是等效的。
* **双写绕过**

  ：如果服务器采用字符串替换的方式过滤，如将`php`替换为空，那么上传`pphphp`，经过一次替换后就会变成`php`。
* **特殊字符绕过**

  ：在文件名末尾添加空格或点（`.`），如`.php.`或`.php[空格]`，Windows系统在保存文件时会自动去除末尾的空格和点。

### 白名单过滤

白名单过滤是一种“疏”的策略，只允许指定的、安全的文件后缀（如`.jpg`、`.png`、`.gif`）上传。这是目前公认最安全的文件上传防御方式之一，在实战中极大地增加了攻击难度。

然而，在CTF竞赛或某些特定场景下，出题人往往会留一个文件包含的点给我们，如果网站同时存在**文件包含漏洞**，攻击者仍有一线生机。攻击者可以先将包含恶意代码的“图片马”以合法后缀（如`.jpg`）上传，然后利用文件包含漏洞，将这个图片文件当作PHP脚本进行包含和执行。

### Apache文件解析缺陷

Apache服务器在处理文件后缀时，存在一些历史遗留的解析特性，可被攻击者利用。

* **多后缀解析**

  ：Apache在解析文件名时，会从右向左寻找它“认识”的后缀。例如，对于一个名为`shell.php.123`的文件，如果Apache不认识`.123`这个后缀，它会继续向前查找，直到发现`.php`，便会将其作为PHP脚本执行。这使得攻击者可以通过构造`恶意文件.php.非法后缀`的形式绕过检查。
* **`.htaccess`文件攻击**

  ：`.htaccess`是Apache的分布式配置文件。如果服务器允许上传此文件，攻击者可以上传一个自定义的`.htaccess`文件，在其中配置规则，强制让Apache将特定后缀（如`.jpg`）的文件当作PHP脚本来解析。这样一来，即使上传的是图片格式，也能成功执行其中的恶意代码。

### IIS6解析漏洞

老旧的IIS6.0服务器存在的解析漏洞至今仍在一些未升级的系统中构成威胁。

* **文件名解析漏洞**

  ：利用分号（`;`）进行截断。在IIS6.0中，`image.asp;.jpg`这样的文件名会被解析为`image.asp`。分号后面的内容被忽略，从而使一个看似是JPG的图片文件被当作ASP脚本执行。
* **目录名解析漏洞**

  ：如果攻击者能够在服务器上创建一个名为`shell.asp/`的目录（注意后缀是`/`），那么该目录下的任何文件，无论其后缀是什么（如`test.jpg`），都会被IIS6.0当作ASP文件来解析和执行。

# 三、题目练习

## （一）《从0到1：CTFer成长之路》书籍配套题目

1. 打开题目环境，发现是一个文件上传题目，下面给出的源代码如下：

```
<?php
header("Content-Type:text/html; charset=utf-8");
// 每5分钟会清除一次目录下上传的文件
require_once('pclzip.lib.php');

if(!$_FILES){

        echo '

    ;

    show_source(__FILE__);
}else{
    $file = $_FILES['file'];

    if(!$file){
        exit("请勿上传空文件");
    }
    $name = $file['name'];

    $dir = 'upload/';
    $ext = strtolower(substr(strrchr($name, '.'), 1));
    $path = $dir.$name;

    function check_dir($dir){
        $handle = opendir($dir);
        while(($f = readdir($handle)) !== false){
            if(!in_array($f, array('.', '..'))){
                if(is_dir($dir.$f)){
                    check_dir($dir.$f.'/');
                 }else{
                    $ext = strtolower(substr(strrchr($f, '.'), 1));
                    if(!in_array($ext, array('jpg', 'gif', 'png'))){
                        unlink($dir.$f);
                    }
                }

            }
        }
    }

    if(!is_dir($dir)){
        mkdir($dir);
    }

    $temp_dir = $dir.md5(time(). rand(1000,9999));
    if(!is_dir($temp_dir)){
        mkdir($temp_dir);
    }

    if(in_array($ext, array('zip', 'jpg', 'gif', 'png'))){
        if($ext == 'zip'){
            $archive = new PclZip($file['tmp_name']);
            foreach($archive->listContent() as $value){
                $filename = $value["filename"];
                if(preg_match('/\.php$/', $filename)){
                     exit("压缩包内不允许含有php文件!");
                 }
            }
            if ($archive->extract(PCLZIP_OPT_PATH, $temp_dir, PCLZIP_OPT_REPLACE_NEWER) == 0) {
                check_dir($dir);
                   exit("解压失败");
            }

            check_dir($dir);
            exit('上传成功!');
        }else{
            move_uploaded_file($file['tmp_name'], $temp_dir.'/'.$file['name']);
            check_dir($dir);
            exit('上传成功!');
        }
    }else{
        exit('仅允许上传zip、jpg、gif、png文件!');
    }
}
```

2. 尝试选择一个jpg文件，上传成功。
3. 建立木马php脚本，内容如下：

```
<?php
fputs(fopen('../hack.php','w'),'');
?>
```

4. 尝试上传php,提示：`仅允许上传zip、jpg、gif、png文件!`
5. 那只好尝试burpsuite拦截了，打开burpsuite,选择proxy选项卡，点击`open browser`打开内置浏览器，输入容器地址，然后选择php文件上传，好，burpsuite已经拦截到了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/njicUbJnVlIwSXq6ZbMCOrXTYWOicmV17qSp8GLCKiczIZDlId0mQLzTyYclMKgiauib73xFMLBOateIj9G3oHCASVK05NzblfKFCFIumbv5dIuA/640?wx_fmt=png&from=appmsg)

6. 在文件名后面加上`%00.jpg`,即改为`filename="1.php%00.jpg"`
7. 提示`上传成功!`,但访问提示404
8. 换个方式来，既然代码中提到要删除不合规文件，那么我们就将文件放到其他文件目录下，先将php改名为`123456789.php.jpg`，压缩到zip文件中，方便后续修改。
9. 使用二进制编辑器，例如ghex工具，打开zip文件，将其中最后一行的`123456789`改为`/../../89`
10. 上传文件，提示上传成功
11. 访问文件，即域名/89.php.jpg,得到flag为`n1book{ThisIsUpLoadToPicfl4g}`。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

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