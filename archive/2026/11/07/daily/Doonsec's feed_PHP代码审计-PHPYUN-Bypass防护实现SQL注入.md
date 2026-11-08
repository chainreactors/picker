---
title: PHP代码审计-PHPYUN-Bypass防护实现SQL注入
url: https://mp.weixin.qq.com/s/3JxpZXRQmg-ZiNMcGGPYiQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:11.506760
---

# PHP代码审计-PHPYUN-Bypass防护实现SQL注入

# PHP代码审计-PHPYUN-Bypass防护实现SQL注入

原创

wolfsec
wolfsec

风铃Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

如果你也刚好在学习代码审计，不妨下载如下源码跟着文章一起跟一下漏洞调用链，源码打包如下：

```
phpyun3.1.rar

链接: https://pan.baidu.com/s/12-aIdfjJuyR388PdkcSymQ?pwd=x9pq 提取码: x9pq
链接：https://pan.quark.cn/s/8b1a1ca24beb
```

#### 系统部署

下载压缩包 ，解压 /upload 文件夹内容到网站目录下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsHxHhx5zGj07XfTZwECE17icYYjOIqGNka79VC0vYGKpiblCqz5toAAf7IoS2TIoCvzPkrIKibtRhBib0wbvXJxMffWW6tN7LUBHk/640?wx_fmt=png&from=appmsg)

笔者这边还进一步做了目录重命名的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltvIt2F9N1aZcoNsQOgTgiaQpZtP09v5x7BbhPO9yMNBb27VibNk0gxbu2jWN9RQzXLRMHSsicT2GJwkIdLLGfUWice8iaS1ZgWNiamE/640?wx_fmt=png&from=appmsg)

接着浏览器访问该路径，走完安装路径即可。默认用户名/密码：admin/admin。

后台管理：

```
http://localhost/phpyun/admin/index.php
```

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlufYuciahcvTmuaQk49O250ibCZ5U3B71W9iawbWDFbibibO2OicxKicB8CuwrcypYmJU7NUwoUOzs0xObpJAFYeOibr9YMdicdodc5rsqs/640?wx_fmt=png&from=appmsg)

首页：

```
http://localhost/phpyun
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlu5FFxtTuumZya6Tp5llT6lUCQDYM3HcnU1Px7FyVQZF6vQeZ4RsB217DVdsIEfcgD13T6Agec2LBtoiay5J20r5sQjcMJPHicSw/640?wx_fmt=png&from=appmsg)

###### php代码动态调试具体配置可参考笔者PHP代码审计第一篇文章《PHP代码审计-动态调试配置（附环境）》，虽然使用的PHP版本可能不一样，但是过程都是一样的。

#### 路由分析

入口文件代码如下：

```
include(dirname(__FILE__)."/global.php");
if($config['webcache']=="1"){
    include_once(LIB_PATH."web.cache.php");
    $cache=new Phpyun_Cache('./cache',dirname(__FILE__)."/",$config['webcachetime']);
    $cache->read_cache();
}
$var=@explode('-',str_replace('/','-',$_GET['yunurl']));
foreach($var as $p){
    $param=@explode('_',$p);
    $_GET[$param[0]]=$param[1];
}
unset($_GET['yunurl']);
if($_GET['m'] && !ereg("^[0-9a-zA-Z\_]*$",$_GET['m'])){

    $_GET['m'] = 'index';
}
$model = $_GET['m'];
$action = $_GET['c'];
if($model=="")  $model="index";
if($action=="") $action = "index";
if(!is_file(MODEL_PATH.$model.'.class.php')){
    $controller='index';
    $action='index';
}
require(MODEL_PATH.'class/common.php');
require("model/".$model.'.class.php');
$conclass=$model.'_controller';
$actfunc=$action.'_action';
$views=new $conclass($phpyun,$db,$db_config["def"],"index",$model);
if(!method_exists($views,$actfunc)){
    $views->DoException();
}
$views->$actfunc();
if($config['webcache']=="1"){
    $cache->CacheCreate();
}
?>
```

这段代码实现了一个典型的 **"model-controller-action" 三段式路由**，路由参数来源`$_GET['m']`，参数`m`表示`model`（模型名，同时决定控制器类前缀）和`$_GET['c']`参数`c`表示`action`（方法名，实际是 `action` 名）。URL 形态大致为：

```
index.php?m=index&c=index
```

加载模型文件：

```
require("model/".$model.'.class.php');
```

控制器类名与方法名拼接：

```
$conclass = $model.'_controller';
$actfunc  = $action.'_action';
$views = new $conclass($phpyun,$db,$db_config["def"],"index",$model);
```

控制器类名 = `{model}_controller`，例如 `index_controller`、方法名 = `{action}_action`，例如 `index_action`。

##### 路由总结

如现在有一下请求：

```
URL: http://localhost/phpyun/index.php?m=login
```

处理逻辑：

```
m 为空或非法([^0-9a-zA-Z_]) → m = index
c 为空                     → c = index
模型文件 {MODEL_PATH}{m}.class.php 不存在 → 本应回退 index（实际失效，会报错）
```

最终映射结果：

```
模型文件 = model/login.class.php
控制器类 = login_controller
执行方法 = index_action
```

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlu3G5y7esDnAOjAM9icu88FOUUXARkJoF2p9hVoq5aDC4xcj8rXwd5ia6CRpiaQicrbZzicJ4Xel4TlxEME7fvaogVAG88U17Dq9EeI/640?wx_fmt=png&from=appmsg)

#### SQL注入

在系统项目中存在一个wap目录，该目录为移动端（手机端）独立访问模块，`WAP` 原本是 Wireless Application Protocol（无线应用协议）的缩写，现在很多 PHP 内容管理系统（CMS）仍然使用 `wap` 作为移动端目录名称。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltaib7rGSLL2Dv4qkk08bt5q6MQvAW47HPF35XpIUWAm3WVTOTW1xGtB60uhXAmOpIgIFkJZDIcUyXmvjA30eiaNtn7Bn9lE8NrM/640?wx_fmt=png&from=appmsg)

查看其入口文件发现路由模式与前面路由分析内容一致。关注到以下代码：

```
if($model=="")  $model="index";
if($action=="") $action = "index";
```

结合路由模式分析可知，此时如果直接访问wap目录，则调用的是：`wap\model\index.class.php`文件中的`index_controller`的`index_action`。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvhoicSib29LEddPGKtia6EBqKRVefpcDTYwqSZ0wXAicbVAWDAwA1a1aUa9g1jOVSdiboxeolO5WC6xxB8k0Q6kB390cjegEtYwZxI/640?wx_fmt=png&from=appmsg)

跟进`get_moblie()`函数：

```
    function get_moblie(){
        $UA = strtoupper($_SERVER['HTTP_USER_AGENT']);
        if(strpos($UA, 'WINDOWS NT') !== false){
            header("location:".$this->config['sy_weburl']."/index.php?c=moblie");
        }
        $now_url=@explode("/",$_SERVER['REQUEST_URI']);
        $now_url=$now_url[count($now_url)-1];
        $this->yunset("wapstyle","../template/wap");
        $this->yunset("now_url",$now_url);
    }
```

该函数通过 UA 判断访问者是否使用 Windows 系统，如果匹配 Windows NT，则跳转到指定页面。此时在Windows中可以通过笔者前阵子推的玄镜工具绕过这个检测，工具设置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZluA2yib7RSesCnEWLibe3WunyDRYD4vRiaC12LEOwDV9xT5Ma7MJrbibRRsiaTmXZGruGzBYC4dBkLOwejHDkGRGBdMcXibW6DACTz4g/640?wx_fmt=png&from=appmsg)

工具下载：

```
https://pan.quark.cn/s/afd39965d724
```

配置完成后，访问路径：

```
http://192.168.213.1/phpyun/wap/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlu1VwkejoACdiclPa20avhnjfbFX5eCxZS8pdbr2oogzkjkLayR3MjwEuPxa3jBmbRhoNJIGVL4Z3PibkbyUbHpF1JmYcLu61XJg/640?wx_fmt=png&from=appmsg)

成功访问。当然还有另一种方法，就是直接在Linux环境下访问该URL：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvbBSIZHro0r4VyrT06Cu1R2husx1BjeFscbJT6rk4l0csc3xEpiamNPwR0lPrSGQdhmq5Hfp8DM6laUnATIatcTy2NcPjlibqxk/640?wx_fmt=png&from=appmsg)

无需任何修改直接就可以访问成功，但是后续的动态调试就会受影响，如果要动调的话可能就得配置远程代码调试，比较麻烦，所以使用Windows系统的推荐使用第一种方式绕过检测。使用Mac和Linux的兄弟就比较轻松了。言归正传，接下去点击右上角的人像图标，来到登录界面，URL为：

```
http://localhost/phpyun/wap/index.php?m=login
```

定位到`wap\login.class.php`文件`login_controller`中的`index_action`，并下断点开始动调：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsnQgK1wRUcu6m2qGicX9iarGM3KOl4NQeR2yoNGd7pVic8cQVghSJ6gFTqnOEa9GUOgxWsdDOYNgtpSg4PTZPfRzTV1x40UzItZA/640?wx_fmt=png&from=appmsg)

这边用户提交的 `username` 被删除了反斜杠，处理后的用户名被拼接进 SQL 查询语句。发送如下payload：

```
username=aaaa'
```

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlutjN61sV40NqQ5Ry15sgSvYk8sgNq4Wsp4Ph2ZLMsdk9WSzziaJz63B7WZYbzZzWcZ5nVHlCnaTltN8ArjtlJ3DLn8RPtU25pg/640?wx_fmt=png&from=appmsg)

发现到数据流到这里，单引号还是被做了处理：单引号 `'` 前面多了一个反斜杠 `\`，单引号 `'` 变成了 HTML 实体 `&acute`。但是由于这个位置做了将反斜杠置为空的操作：

```
str_replace('\\','',$_POST['username']);
```

所以关于添加反斜杠的就不用管了，只需要关注单引号 `'` 变成了 HTML 实体 `&acute`这个操作是在哪里做的。向上回溯代码发现`index.php`中导入了`global.php`：

```
include(dirname(dirname(__FILE__))."/global.php");
```

在`global.php`中又导入了：

```
include(CONFIG_PATH."db.safety.php");
```

`db.safety.php`代码如下：

```
function quotesGPC() {

    if(!get_magic_quotes_gpc()){
        $_POST = array_map("addSlash", $_POST);
        $_GET = array_map("addSlash", $_GET);
        $_COOKIE = array_map("addSlash", $_COOKIE);
    }

}
function addSlash($el) {
    if (is_array($el))
        return array_map("addSlash", $el);
    else
        return addslashes($el);
}
function gpc2sql($str) {

    if(preg_match("/select|insert|update|delete|union|into|load_file|outfile/is", $str))
    {
        exit(safe_pape());
    }
    $arr=array(" and "=>" an d "," or "=>" Ｏr ","%20"=>"","select"=>"Ｓelect","update"=>"Ｕpdate","count"=>"Ｃount","chr"=>"Ｃhr","truncate"=>"Ｔruncate","union"=>"Ｕnion","delete"=>"Ｄelete","insert"=>"Ｉnsert");
    foreach($arr as $key=>$v){
        $str = preg_replace('/'.$key.'/isU',$v,$str);
    }
    return $str;
}
function safeid($v){
    if(strstr($v,",")){
        $arr=explode(',',$v);
        foreach($arr as $val){
            $value[]=(int)$val;
        }
        $v=implode(',',$value);
    }elseif(is_array($v)){
        foreach($v as $val){
            $value[]=(int)$val;
        }
        $v=$value;
    }else{
        $v=int($v);
    }
    return $v;
}
function safesql($StrFiltKey,$StrFiltValue,$type){

    $getfilter = "\\<.+javascript:window\\[.{1}\\\\x|<.*=(&#\\d+?;?)+?>|<.*(data|src)=data:text\\/html.*>|\\b(alert\\(|confirm\\(|expression\\(|prompt\\(|benchmark\s*?\\(\d+?|sleep\s*?\\([\d\.]+?\\)|load_file\s*?\\()|<[a-z]+?\\b[^>]*?\\bon([a-z]{4,})\s*?=|^\\+\\/v(8|9)|\\b(and|or)\\b\\s*?([\\(\\)'\"\\d]+?=[\\(\\)'\"\\d]+?|[\\(\\)'\"a-zA-Z]+?=[\\(\\)'\"a-zA-Z]+?|>|<|\s...