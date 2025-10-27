---
title: 第三届广东省大学生网络攻防竞赛wp - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18451004
source: 博客园 - 渗透测试中心
date: 2024-10-09
fetch_date: 2025-10-06T18:53:35.364220
---

# 第三届广东省大学生网络攻防竞赛wp - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [第三届广东省大学生网络攻防竞赛wp](https://www.cnblogs.com/backlion/p/18451004 "发布于 2024-10-08 09:21")

## 一、WEB

### 1.消失的flag

访问提示`Access Denied`

fakeip插件伪造ip

[![img](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092036028-1131844638.png)](https://dddkia.github.io/img/%E7%AC%AC%E4%B8%89%E5%B1%8A%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%A4%A7%E5%AD%A6%E7%94%9F%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E7%AB%9E%E8%B5%9B/171560083391325.png "img")

提示`File is Null`

尝试加`file`参数

```
?file=index.php`提示`do not hack!!
```

大概是filter-chain

参考文章：

<https://www.cnblogs.com/linuxsec/articles/12684259.html>

https://blog.csdn.net/yuanxu8877/article/details/127607264

`php://filter/convert.iconv`可以成功

[![img](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092036978-1804565315.png)](https://dddkia.github.io/img/%E7%AC%AC%E4%B8%89%E5%B1%8A%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%A4%A7%E5%AD%A6%E7%94%9F%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E7%AB%9E%E8%B5%9B/17156008339121.png "img")

```
/?file=php://filter/convert.iconv.utf-8.utf-16/resource=index.php
/?file=php://filter/convert.iconv.utf-8.utf-16/resource=/flag
```

[![img](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092038434-1923368386.png)](https://dddkia.github.io/img/%E7%AC%AC%E4%B8%89%E5%B1%8A%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%A4%A7%E5%AD%A6%E7%94%9F%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E7%AB%9E%E8%B5%9B/17156008339122.png "img")[![img](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092039810-1387457240.png)](https://dddkia.github.io/img/%E7%AC%AC%E4%B8%89%E5%B1%8A%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%A4%A7%E5%AD%A6%E7%94%9F%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E7%AB%9E%E8%B5%9B/17156008339123.png "img")

### **2.unserialize\_web**

先看看有没有常见的备份文件或者robots.txt、www.zip、.git、.svn、.www.tar.gz这些

能发现有一个备份文件，www.tar.gz

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092041036-327766446.png)

那么访问 URL/www.tar.gz把备份文件下载下来

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092042077-1792784571.png)

看见源码都在这里了，主要就是看upload.php和download.php

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092043298-204077136.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092044668-810431961.png)

然后在CSDN能看到类似的题目，为：

<https://blog.csdn.net/m0_70819573/article/details/129506508>

<https://blog.csdn.net/2301_79708753/article/details/135873948>

<https://www.bilibili.com/read/cv21572905/>

然后打开题目的链接，开局一个上传表单，给我整不会了，不是说反序列化咩？

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092045589-1434643647.png)

然后猜测，可能为需要文件上传加上反序列化的组合拳

然后搜索发现是phar反序列化—文件包含之反序列化（文件上传）

else{

    $extensions = array("gif", "jpg", "png");

    $temp = explode(".", $\_FILES["file"]["name"]);

    $fileExtension = end($temp);

    $fileSizeCheck = $\_FILES["file"]["size"];

    $isExtensionAllowed = in\_array($fileExtension, $extensions) ? true : false;

    if ($fileSizeCheck && $isExtensionAllowed){

        $fileContent = file\_get\_contents($\_FILES["file"]["tmp\_name"]);

        $haltCompilerCheck = strpos($fileContent, "\_\_HALT\_COMPILER();");

        if(gettype($haltCompilerCheck) === "integer"){

            echo "phar";

从uoload.php的这段代码可以得知，只能上传gif、jpg、png的图片，并且会进行内容检查，文件中不可以包含有“\_\_HALT\_COMPILER();”的内容。

所以我们需要将等一下生成phar文件压缩成压缩包来绕过检查。

class File {

    public $val1;

    public $val2;

    public $val3;

    public function \_\_construct() {

        $this->val1 = "val1";

        $this->val2 = "val2";

    }

    public function \_\_destruct() {

        if ($this->val1 === "file" && $this->val2 === "exists") {

            if (preg\_match('/^\s\*system\s\*\(\s\*\'cat\s+\/[^;]\*\'\s\*\);\s\*$/', $this->val3)) {

                eval($this->val3);

            } else {

                echo "Access Denied";

            }

        }

    }

    public function \_\_access() {

        $Var = "Access Denied";

        echo $Var;

    }

    public function \_\_wakeup() {

        $this->val1 = "exists";

        $this->val2 = "file";

        echo "文件存在";

    }

}

然后从download.php的这段代码可以得知是常规的反序列化。\_\_destruct()魔术方法中有eval()函数可以利用来进行命令执行，存在命令执行漏洞。\_\_destruct()方法里面的 if 语句会先判断变量v a l 1 是否全等于 f i l e ，变量 val1是否全等于file，变量val1是否全等于file，变量val2是否全等于exists。

然后到下面这段代码

if (preg\_match('/^\s\*system\s\*\(\s\*\'cat\s+\/[^;]\*\'\s\*\);\s\*$/', $this->val3)) {

                eval($this->val3);

这段代码是一个 PHP 中的条件语句，用于检查一个字符串是否匹配一个特定的模式。如果匹配成功，就会执行 eval 函数来执行字符串中的代码。

让我们来看看这个正则表达式

/^\s\*system\s\*\(\s\*\'cat\s+\/[^;]\*\'\s\*\);\s\*$/：

/^ 和 $ 表示字符串的开始和结束，确保整个字符串都匹配模式。

\s\* 匹配零个或多个空白字符。

system 匹配字符串中的 system。

( 和 ) 匹配左右括号。

\s\* 匹配零个或多个空白字符。

'cat\s+/[^;]’ 匹配以单引号括起来的以 cat 开头的文件路径。其中：

’ 匹配单引号。

cat 匹配 cat 字符串。

\s+ 匹配一个或多个空白字符。

/ 匹配斜杠 /。

[^;] 匹配零个或多个非分号字符。

’ 匹配单引号。

\s\* 匹配零个或多个空白字符。

; 匹配分号。

换句话说，这个正则表达式用于检查字符串是否以 system('cat 开头，后面紧跟着一个文件路径，然后以 '); 结尾。

所以我们可以构造$val3的值为

system('cat /flag');

来获取flag

如果 t h i s − > v a l 3 中的内容匹配这个模式，就会执行 e v a l ( this->val3 中的内容匹配这个模式，就会执行 eval(this−>val3中的内容匹配这个模式，就会执行eval(this->val3);，这意味着 $this->val3 中的代码将被执行。这种做法存在安全风险，因为它允许任意代码执行，可能导致代码注入等安全漏洞。

将正则表达式可视化https://wangwl.net/static/projects/visualRegex/#

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092046424-875371173.png)

然后这个还要注意需要绕过wakeup（）魔术方法：

public function \_\_wakeup() {

        $this->val1 = "exists";

        $this->val2 = "file";

        echo "文件存在";

    }

它强制把v a l 1 赋值为 e x i s t s ， val1赋值为exists，val1赋值为exists，val2赋值为file，会导致我们在后面触发destruct()魔术方法的时候，if 判断会失效

![image.png](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241008092047122-1218771670.png)

，所以我们需要绕过wakeup（）

那就是需要用到CVE-2016-7124，它的影响范围是

PHP5 < 5.6.25

PHP7 < 7.0.10

而它的触发方式也很简单，那就是当序列化字符串中表示对象属性个数的值大于真实的属性个数时会跳过\_\_wakeup的执行

所以接下来我们要构造一个phar文件，上传之后，让它执行反序列化，从而执行我们的代码

上传时候zip会绕过phar检测，但是phar伪协议会解压zip，在解压时候在file\_get\_contents()处我们的phar伪协议会触发反序列化，并且进行eval()的命令执行

phar文件生成代码：

<?php

ini\_set("phar.readonly", "Off");

class File

{

    public $val1;

    public $val2;

    public $val3;

    public function \_\_construct()

    {

      ...