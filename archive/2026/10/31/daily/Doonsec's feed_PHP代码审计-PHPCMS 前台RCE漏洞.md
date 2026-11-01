---
title: PHP代码审计-PHPCMS 前台RCE漏洞
url: https://mp.weixin.qq.com/s/whxU3U2P_DcHJR2-bnW3Hg
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:56.280722
---

# PHP代码审计-PHPCMS 前台RCE漏洞

# PHP代码审计-PHPCMS 前台RCE漏洞

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
phpcms_v9.6.0_UTF8.zip

链接: https://pan.baidu.com/s/1_cTRfMHNcsRrop8j1xZgGg?pwd=9hty 提取码: 9hty
链接：https://pan.quark.cn/s/79db348a9b43
```

系统部署、路由分析部分请看笔上一篇文章《PHP代码审计-PHPCMS-SQL注入》。

来到注册界面，具体URL为：

```
http://192.168.213.1/phpcms-rce/index.php?m=member&c=index&a=register&siteid=1
```

输入对应的信息，完成注册流程，抓包，得到如下数据包，将数据包发送至Burpsuite的重放模块：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZltM5cnAnAoeaddLXyVhtib2ct7NpxIaSkAObVjzwIjw0ibtM1KNJj5XOLTnDychc1ia2ViaPb0ibIxg5IO7t56y6pPkue5fWy9TavTQ/640?wx_fmt=png&from=appmsg)

打开phpstorm开始，根据注册界面的URL定位到对应的代码片段。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltTLVLFSFmotSELvl0icflj5DO4MWKejRxrmFicvtoUCDf0nBPnOsx51Ric0ibVJWcEKiabAuvEdQ99WC2ic7sXc96592gkdZibMstexQ/640?wx_fmt=png&from=appmsg)

下断点，Burp重放模块发包，开始动态调试。

因为该功能点存在异步请求，所以必须要获得整体的注册数据包后再重放该数据，否则执行的控制流会出现偏差。

###### 注：php代码动态调试具体配置可参考笔者PHP代码审计第一篇文章《PHP代码审计-动态调试配置（附环境）》，虽然使用的PHP版本可能不一样，但是过程都是一样的。

紧接着就可以开始进行动态调试，一路按`Step over`，来到核心代码：

```
if($member_setting['choosemodel']) {
    require_once CACHE_MODEL_PATH.'member_input.class.php';
    require_once CACHE_MODEL_PATH.'member_update.class.php';
    //导入两个类：.\caches\caches_model\caches_datahe 目录中的 member_input.class.php和 member_update.class.php

    $member_input = new member_input($userinfo['modelid']);
    $_POST['info'] = array_map('new_html_special_chars',$_POST['info']);
    //调用new_html_special_chars 函数对 info 进行处理，将特殊字符转换为 HTML 实体
    $user_model_info = $member_input->get($_POST['info']);
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltxw3JxY3dEUzxheF9ialUgKQ9ORNKxL2PPnfSDKicwcUWymXHsvdobzsialfahQEIMrAfudtIJwcV2y9cbS9BoOjbJnmJy3lX1tU/640?wx_fmt=png&from=appmsg)

跟进get()函数：

```
    function get($data) {
        $this->data = $data = trim_script($data);  //防XSS
        $model_cache = getcache('member_model', 'commons');
        $this->db->table_name = $this->db_pre.$model_cache[$this->modelid]['tablename'];

        $info = array();
        $debar_filed = array('catid','title','style','thumb','status','islink','description');
        if(is_array($data)) {
            foreach($data as $field=>$value) {
                if($data['islink']==1 && !in_array($field,$debar_filed)) continue;
                $field = safe_replace($field);
                $name = $this->fields[$field]['name'];
                $minlength = $this->fields[$field]['minlength'];
                $maxlength = $this->fields[$field]['maxlength'];
                $pattern = $this->fields[$field]['pattern'];
                $errortips = $this->fields[$field]['errortips'];
                if(empty($errortips)) $errortips = "$name 不符合要求！";
                $length = empty($value) ? 0 : strlen($value);
                if($minlength && $length < $minlength && !$isimport) showmessage("$name 不得少于 $minlength 个字符！");
                if (!array_key_exists($field, $this->fields)) showmessage('模型中不存在'.$field.'字段');
                if($maxlength && $length > $maxlength && !$isimport) {
                    showmessage("$name 不得超过 $maxlength 个字符！");
                } else {
                    str_cut($value, $maxlength);
                }
                if($pattern && $length && !preg_match($pattern, $value) && !$isimport) showmessage($errortips);
                if($this->fields[$field]['isunique'] && $this->db->get_one(array($field=>$value),$field) && ROUTE_A != 'edit') showmessage("$name 的值不得重复！");
                $func = $this->fields[$field]['formtype'];
                if(method_exists($this, $func)) $value = $this->$func($field, $value);

                $info[$field] = $value;
            }
        }
        return $info;
    }
```

在迭代最后有一个函数动态调用：

```
$func = $this->fields[$field]['formtype'];   //datetime
if(method_exists($this, $func)) $value = $this->$func($field, $value);
```

`$func`最后的值为`datetime`:

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvTKvUOBEjBCK5tpN8rU0khiafQNEWSoMYFaxic15btWqDrM24WsumOMRVpLwpe7sHZWDW6zxsp0fGmrtmrN83P0OpNMPDQCxHlo/640?wx_fmt=png&from=appmsg)

这个`datetime`函数是从`fields`数组中提取出来的，此时我们可以先确定一下`fields`中的数据是从哪里来的，重点是要确认除了`datetime`之外，还有哪些函数是可以被取到的。在当前文件中搜索`fields`，得到如下代码（`member_input.class.php`的构造函数）

```
    function __construct($modelid) {
        $this->db = pc_base::load_model('sitemodel_field_model');
        $this->db_pre = $this->db->db_tablepre;
        $this->modelid = $modelid;
        $this->fields = getcache('model_field_'.$modelid,'model');
```

关注`fields`，它不是在 `member_input` 构造函数中现场查询数据库得到的，而是通过 `getcache()` 从缓存系统中读取的。缓存数据可能来源于该数据库表，但需要找到生成缓存的代码才能确认两者的关系。这个时候可以先找一下缓存是在哪里写入的，在源码中搜索：

```
setcache('model_field_
```

找到五段代码：

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlsxQBBXlrZcQdgQEQibHdExPqvQRYKoHia00Te9X2ibIpmeItk9lfuF0R3jZgzX21Jib7XOrF0OVLKHBgpC5KdDAaIekcnXoLPEjxY/640?wx_fmt=png&from=appmsg)

根据这五段代码分析，基本可以断定`model_field` 数据库表中的字段配置会被读取出来并整理成数组，再写入 `model_field_模型ID` 对应的缓存中。整个调用链：

```
model_field 数据库表 → select() 查询字段配置 → 整理成 $field_array → setcache() 写入缓存 → getcache() 读取缓存 → $this->fields → 校验和处理用户提交的字段
```

现在进入`model_field` 查看`formtype`字段：

```
select modelid, formtype from v9_model_field;
```

得到如下函数：

```
box
catid
copyfrom
datetime
downfile
downfiles
editor
groupid
image
images
islink
keyword
number
omnipotent
pages
posid
readpoint
template
text
textarea
title
typeid
video
```

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvYXKFuWMMGMdnVBK9wzF86ZMUGOosNCVj1ibE9T4Yd824iciaYv1ibVYSJLJiaic8pRZrYz8j248XfssVbhKnrY5lsiciafMP5ERb54xk/640?wx_fmt=png&from=appmsg)

对应的modelid应为1，3，11。

接着通过上述函数名，在php代码中搜索函数代码具体实现，这边聚焦editor函数：

```
    function editor($field, $value) {
        $setting = string2array($this->fields[$field]['setting']);
        $enablesaveimage = $setting['enablesaveimage'];
        $site_setting = string2array($this->site_config['setting']);
        $watermark_enable = intval($site_setting['watermark_enable']);
        $value = $this->attachment->download('content', $value, $watermark_enable);
        return $value;
    }
```

**注意：动态调试要进入这个函数有一个坑点，要想让控制流进入editor，仅仅讲modelid修改为1、3或者11是不够的。假设你将 `$modelid` 修改为 `1`，那么程序读取的是：**

```
$this->fields = getcache('model_field_1', 'model');
```

而在 `get()` 中遇到的判断是：

```
if (!array_key_exists($field, $this->fields)) {
    showmessage('模型中不存在'.$field.'字段');
}
```

**这意味着：当前提交的字段名 `$field` 必须存在于所选模型的字段配置数组中，否则就会报错。**所以这个时候要想进入控制流就得先去`'model_field_(1,3,11).cache'`或者数据库中查看查看对应`field`字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvdc1TicBpRyqqrKEDOVTCc3UhqlbiaibW5kuiblbT4iaYvQXh0BAchfXFYrpicG8vEHNTk40xTsibAtzyR97XFFB4uavibwChabUl564g/640?wx_fmt=png&from=appmsg)

`modelid`为1时，field需要为`content`，这个时候才能够进入`editor`函数，所以构造如下数据包：

```
POST /phpcms-rce/index.php?m=member&c=index&a=register&siteid=1 HTTP/1.1
Host: 192.168.213.1
Content-Length: 318
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36
Origin: http://192.168.213.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://192.168.213.1/phpcms-rce/index.php?m=member&c=index&a=register&siteid=1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: XDEBUG_SESSION=12514; PHPSESSID=onfqvj5ve5c0mhlfnsgq7aria2
Connection: keep-alive

siteid=1&modelid=11&username=bssssssaws&password=admin123&pwdconfirm=admin123&email=adsxsssssxsw%40qq.com&nickname=sxsxssaiqa&info[content]=Hello&info%5Bbirthday%5D=2026-10-01&dosubmit=%E5%90%8C%E6%84%8F%E6%B3%A8%E5%86%8C%E5%8D%8F%E8%AE%AE%EF%BC%8C%E6%8F%90%E4%BA%A4%E6%B3%A8%E5%86%8C&protocol=
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvBeVFadgwO0eKcfbl1saDYVGibygq9KFRqc8SUhz7EnQeSOPZDVFmDeJWdFYkwZBUSgticxgiaBLnYr1Lwm4Ilazq9vbY5c6L210/640?wx_fmt=png&from=appmsg)

 `editor()` 函数主要用于处理编辑器提交的内容，并调用附件组件的 `downl...