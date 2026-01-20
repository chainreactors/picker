---
title: AI自动化代码审计RCE
url: https://mp.weixin.qq.com/s/AnbKnyQkt7sz51zyxTOUiw
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:12.015664
---

# AI自动化代码审计RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAnRc0nib44ZU93bGVfkqmzicxeggqCwu4EPq5PDpwHqoWzOkvf6AowKfXK12QYO2ngcFuibFfS19nGOA/0?wx_fmt=jpeg)

# AI自动化代码审计RCE

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

# 原文链接：https://xz.aliyun.com/news/17327

# 前言

AI最近的趋势持续偏高，用AI来写代码，挖漏洞甚至于审计代码的文章或者工具都非常多，最近刚好在学习AI安全，并且php相关的代码审计也比较熟练，趁着学习AI的机会结合代码审计进行学习。

# 智能体创建

代码审计分很多类型，其中有的类型为传入大模型大量文件，让其进行分析，还有的就是传入一串你觉得存在漏洞的代码进行分析。

这里使用互联网上开源且免费的AI聊天机器人创建一个关于代码审计的智能体

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeByywWRVZl058YDhNwjVGKhMI4fvibHaPeFycYV0lWBweTECNuceK5PVzQ/640?wx_fmt=png&from=appmsg#imgIndex=0)

# RCE

创建成功后，查看如下代码，大家可以发现在`system("cp ".$target_path." /xxxxxxxxx/dmconfig".$_POST['url']);`这行代码中存在存在命令执行且参数可控，但看这一行代码的话相信只要是小白应该都能够构造出payload,但是问题是还有一些前置条件。

```
<?php

if (   isset($_POST['pwd'])
    && 0 == strcmp($_POST['pwd'], "nv2260")
    && isset($_POST['url']) )
{
    if ($_FILES['file']['error'] > 0)
    {
        header("Content-Type: text/plain");
        echo "error: " . $_FILES['file']['error'] . "\n";
        exit(0);
    }
    else
    {
        if ($_FILES['file']['size'] > 10*1024*1024)
        {
            header("Content-Type: text/plain");
            echo "error: file size is too large\n";
        }
        else
        {
            $target_path = "/xxxxxxxxx/odmconfig".$_POST['url'];
            //Create in-between folders if not exists
            $dir_name = dirname("/xxxxxxxxx/odmconfig".$_POST['url']);
            if(!file_exists($dir_name))
            {
                mkdir($dir_name, 0644, true);
            }

            if (move_uploaded_file($_FILES['file']['tmp_name'], $target_path))
            {
                //Create in-between folders if not exists
                $dir_name = dirname("/xxxxxxxxx/dmconfig".$_POST['url']);
                if(!file_exists($dir_name))
                {
                    mkdir($dir_name, 0644, true);
                }

                system("cp ".$target_path." /xxxxxxxxx/dmconfig".$_POST['url']);
                header("Content-Type: text/plain");
                echo "upload ok\n";
            }
            else
            {
                header("Content-Type: text/plain");
                echo "error: there was an error uploading the file, please try again!\n";
            }
        }
    }
}
else
{
    header("404 Not Found");
    exit(0);
}

?>
```

把上述代码丢尽AI智能体中进行分析，可以发现成功给出了漏洞类型，位置以及攻击流程和payload等等。并且我们通过上述代码是可以知道提交的请求包是POST请求且以文件上传的格式进行RCE的，因此对于AI来说这也不是什么问题。

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeBygqFSlz3T5v7ee7iccxYFCAqiay7xbGXBVZclVXII2icDtNc4pwgVWUMmQ/640?wx_fmt=png&from=appmsg#imgIndex=1)

如果上述给的payload不符合你的要求，你可再次进行询问，比如说想要使用python代码提交请求，或者BURP，yakit来发送恶意请求包都可以，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeByia3vQyjSzhYB221l3P44q96tLutrFkJwYf8tvdKlLlrFH0fTmogZuWw/640?wx_fmt=png&from=appmsg#imgIndex=2)

通过AI智能体构造的恶意请求包（只需要稍加更改路径或者格式即可），发送请求即可发现成功执行whoami命令造成RCE

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeBy7AyfwM2pvAc9McVocvjTsmEJLrUKXXwytLxtC6Mwz3IBPVTKk4r1lA/640?wx_fmt=png&from=appmsg#imgIndex=3)

# RCE

我们在来查看这一段代码，这一段代码稍加复杂一点点的地方在于命令构造方面，且涵盖的变量稍多，如果自己分析的话可能需要一点时间

```
 if (isset($_GET['cmd']) )
    {
        if(){...}
        else if( 0 == strcmp($_GET['cmd'],'writeuploaddir') )
        {
            if(constant("NEED_UPLOAD_FROM_DISK"))
            {
                if (isset($_GET['uploaddir']))
                {
                    $uploaddir = $_GET['uploaddir'];
                    $fp = fopen(UPLOAD_CONF_PATH, 'w');
                    $strData = "server.upload-dirs=(\"" . $uploaddir . "\")\n";

                    fwrite($fp, $strData);
                    fclose($fp);

                    $current_dir = system('cat '.PHP_CINF_PATH.'| grep \'upload_tmp_dir\'');
                    $tmp_upload_dir = 'upload_tmp_dir='.$uploaddir;
                    $cmd = "sed -i 's/".str_replace('/', '\/', $current_dir)."/".str_replace('/', '\/', $tmp_upload_dir)."/g/g' ".PHP_CINF_PATH;

                    system($cmd);
                    //system("echo \"$uploaddir\" > ".UPGRADE_DIR_PATH);
                    $file = fopen(UPGRADE_DIR_PATH,"w");
                    if( $file )
                    {
                        fwrite($file,"[UPLOAD]\n");
                        fwrite($file,"upload_dir=\"". $uploaddir ."\"\n");
                        fclose($file);
                    }
                }
            }

            header("Content-type: application/xml\r\n\r\n");
            echo "Modify upload directory ok";
        }
```

直接把代码丢给智能体压力一下AI，可以发现给出了两个漏洞位置，其中漏洞位置1给出了payload示例。

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeBywQXzwCjSWORaf6V3CaXkPNKu7yIqOz0yGluic8KbGHEt5CPjo2NbywA/640?wx_fmt=png&from=appmsg#imgIndex=4)

但是通过上图发现给出的payload示例不够完整，不能直接如第一个RCE一样直接用即可，因此我们可以询问AI详细的构造方法应该是怎样的，怎么样才能在这条命令里面加入whoami命令并成功执行等等传递给AI，如下图，通过询问构造方法相关问题，直接输出构造恶意whoami命令的payload

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeByBHiafgKTEzjmBibGRduzUxkUmslibVUcYq68prmHEH2T4bIJPXYPxjgXA/640?wx_fmt=png&from=appmsg#imgIndex=5)

直接结合上下文所有的payload发包，成功RCE

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTq7S5EHjrkEF5suvfUzPeByibaX4CZYwH2yFib3a7rZmtx6Pic9MKJQjiczP5fIZaYUjDlOIZk0lrlNMw/640?wx_fmt=png&from=appmsg#imgIndex=6)

![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAkmMvIEVFdiaG19OichW7IMqrianjXzneqZoJ3rMMFygyGVdictzTMWy15vH5nhoWznKInJQ9yXzBpBFg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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