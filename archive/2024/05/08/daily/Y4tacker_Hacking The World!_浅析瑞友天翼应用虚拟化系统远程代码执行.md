---
title: 浅析瑞友天翼应用虚拟化系统远程代码执行
url: https://y4tacker.github.io/2024/05/07/year/2024/5/%E6%B5%85%E6%9E%90%E7%91%9E%E5%8F%8B%E5%A4%A9%E7%BF%BC%E5%BA%94%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96%E7%B3%BB%E7%BB%9F%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/
source: Y4tacker:Hacking The World!
date: 2024-05-08
fetch_date: 2025-10-06T17:15:27.937085
---

# 浅析瑞友天翼应用虚拟化系统远程代码执行

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 浅析瑞友天翼应用虚拟化系统前台反序列化(V<=7.0.5.1)](#%E6%B5%85%E6%9E%90%E7%91%9E%E5%8F%8B%E5%A4%A9%E7%BF%BC%E5%BA%94%E7%94%A8%E8%99%9A%E6%8B%9F%E5%8C%96%E7%B3%BB%E7%BB%9F%E5%89%8D%E5%8F%B0%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-V-lt-7-0-5-1)
   1. [1.1. 鉴权](#%E9%89%B4%E6%9D%83)
   2. [1.2. 失败的session控制利用尝试](#%E5%A4%B1%E8%B4%A5%E7%9A%84session%E6%8E%A7%E5%88%B6%E5%88%A9%E7%94%A8%E5%B0%9D%E8%AF%95)
   3. [1.3. 柳暗花明又一村](#%E6%9F%B3%E6%9A%97%E8%8A%B1%E6%98%8E%E5%8F%88%E4%B8%80%E6%9D%91)
   4. [1.4. PHP临时文件](#PHP%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6)
   5. [1.5. ThinkPHP日志包含](#ThinkPHP%E6%97%A5%E5%BF%97%E5%8C%85%E5%90%AB)

# 浅析瑞友天翼应用虚拟化系统前台反序列化(V<=7.0.5.1)

Y4tacker

2024-05-07 (Updated: 2024-05-29)

[PHP](/categories/PHP/)

[PHP](/tags/PHP/)

# 浅析瑞友天翼应用虚拟化系统前台反序列化(V<=7.0.5.1)

看到应急公告简单分析学习一波，漏洞不算难，代码也比较简单，有些细节还是蛮有意思，算是温故而知新，顺便也捡起一些很久没碰的PHP知识

## 鉴权

这个系统文件不多，功能点大多是需要登录，我们可以重点关注一下鉴权部分，在为数不多的控制器当中可以看到，在`admin/index`两个控制器中部分功能点都存在对于登录用户的判断，分别对应函数`checklogin`与`adminchecklogin`(Ps：在高版本中只有AdminCtroller控制器文件了，武器化也以这个为准)

在这里可以明显看到sql查询为拼接的形式，`userId`参数来源于session存储文件的反序列化

IndexController#checklogin

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` private function checklogin() {     $mUser = M('cuser');     $sessionpath = session_save_path();     $pathName = $this->openpath($sessionpath);     $path = $_REQUEST['sessId'] ? ($sessionpath . "/sess_" . $_REQUEST['sessId']) : ($sessionpath . "/" . $pathName['name'][0]);      $content = file_get_contents($path);     $tmp = explode("|", $content);     $tmp3 = unserialize($tmp[3]);     $userId = $tmp3['user_id'];     $cuser = $mUser->where("user_id='{$userId}' AND is_group=0 AND is_admin !=1")->find();     if (sizeof($cuser) > 0) {         $_SESSION['UserInfo'] = $cuser;         $_SESSION['sessId'] = $_REQUEST['sessId'];         $this->assign('sessId', $_REQUEST['sessId']);         return true;     }     if ($_SESSION['LonginSucceed'] == false) { //尚未登录         $this->login(); //$this->redirect('index');         return false;     } else {         return true;     } } ``` |

AdminController#checklogin

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` | ``` private function adminchecklogin() {     $mUser = M('cuser');     $sessionpath = session_save_path();     $pathName = $this->openpath($sessionpath);     $path = $sessionpath . "/sess_" . $_REQUEST['sessId'];     $content = file_get_contents($path);     $tmp = explode("OverDo", $content);     if (count($tmp) > 1) {         $temporary = explode("|", $content);         $tmp6 = unserialize($temporary[7]);         if (!$tmp6) {             $tmp6 = unserialize($temporary[1]);         }     } else {         $tmp = explode("|", $content);         $tmp6 = unserialize($tmp[6]);     }     $userId = $tmp6['user_id'];     $_SESSION['AdminUserInfo']['user_id'] = $_SESSION['AdminUserInfo']['user_id'] ? $_SESSION['AdminUserInfo']['user_id'] : $userId;      $cuser = $mUser->where("user_id='{$_SESSION['AdminUserInfo']['user_id']}' AND is_group=0 AND is_admin=1")->find();     if (sizeof($cuser) > 1 && $cuser['is_admin'] == 1) {         $_SESSION['AdminLonginSucceed'] = true;         $_SESSION['Is_Admin'] = $cuser['is_admin'];         $_SESSION['AdminUserInfo'] = $InfoLogin['AdminUserInfo'] = $cuser;         $_SESSION['AdminUserInfo']['name'] = $cuser['name'];         $this->assign('sessId', $_REQUEST['sessId']);         $this->assign('Admin', $_SESSION['AdminUserInfo']['name']);     }      if ($_SESSION['AdminLonginSucceed'] && $_SESSION['Is_Admin'] && $cuser != NULL) {         return true;     } else { //尚未登录         $this->login(); //$this->redirect('index');         $_SESSION['AdminLonginSucceed'] = false;         $_SESSION['Is_Admin'] = false;         return false;     } } ``` |

利用方式大致一致，但`Admincontroller`与`IndexController`在利用上仍有些许差别，前者利用中多了如下代码，也就是说如果第一次打成功了，userId则会被记录，第二次利用时如果需要更改Payload只需把cookie中`PHPSESSID`做个修改即可

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $_SESSION['AdminUserInfo']['user_id'] = $_SESSION['AdminUserInfo']['user_id'] ? $_SESSION['AdminUserInfo']['user_id'] : $userId; ``` |

## 失败的session控制利用尝试

php中的session存在多种存储方式，通过cookie、文件、数据库等方式均可，存储的格式也有多种

| php\_serialize | 经过serialize()函数序列化数组 |
| --- | --- |
| php | 键名+竖线+经过serialize()函数处理的值 |
| php\_binary | 键名的长度对应的ascii字符+键名+serialize()函数序列化的值 |

接下里我们查看系统中关于session的配置，不难发现，存储方式是通过文件，保存在`RealFriend\Rap Server\Temp\PhpSession`路径下，且存储格式为`php`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` [Session] session.save_handler = files ;session.save_path = "C:\Windows\Temp" session.save_path ="C:\Program Files (x86)\RealFriend\Rap Server\Temp\PhpSession" session.use_cookies = 1 session.cookie_secure = 0 session.name = PHPSESSID session.auto_start = 0 session.cookie_lifetime = 0 session.cookie_path = / session.cookie_domain = session.cookie_httponly = True session.serialize_handler = php ``` |

关于session的工作原理就不再赘述网上相关资料也很多了

知道了这些信息，接下来我们便可以思考如何控制这个session文件(通过对session操作赋值)，这个过程非常直接，因此我们第一个很容易想到在登录的过程

在下面的文件中，我们发现赋值部分能控制的有`name`、`pwd`、`loginPwd`、`language`等

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 ``` | ``` <?php  include "ConDB.XGI"; include "LicenceInfo.XGI"; include "Lg.XGI"; include "Common.XGI"; include "Function.XGI"; include "converter.XGI";  $ErrID = 1; if (!isset($_SESSION)) {     session_start(); } $COMCASWEB = new main();  if (!isset($_REQUEST['cmd']) && $_REQUEST['cmd'] == "") {     if (isset($_SESSION['UserName']) && !empty($_SESSION['UserName'])) {     }     if ($GLOBALS['_SESSION']['LonginSucceed']) {         $GLOBALS['GLOBALS']['_REQUEST']['DirID'] = "NULL";     } else {         session_unset();     } }  $GLOBALS['GLOBALS']['_SESSION']['MainXGI'] = $_SERVER['PHP_SELF']; $GLOBALS['GLOBALS']['_SESSION']['Embed'] = FALSE; $GLOBALS['GLOBALS']['_SESSION']['salt'] = getClientLoginMd5Salt(); if (isset($_GET['cmd']) && $_GET['cmd'] == "UserLogin") {     $RedURL = $_SERVER['PHP_SELF'];        header("Location: " . $RedURL);     exit; }  if (isset($_REQUEST['cmd']) && $_REQUEST['cmd'] == "UserLogin") {     $_REQUEST['name']=trim(filter_inputXssKeyWord($_REQUEST['name']));     $_REQUEST['pwd']=(filter_inputXssKeyWord($_REQUEST['pwd']));     $_REQUEST['loginPwd']=trim(filter_inputXssKeyWord($_REQUEST['loginPwd']));     $GLOBALS['GLOBALS']['_SESSION']['loginPwd']=$_REQUEST['loginPwd'];     $GLOBALS['GLOBALS']['_SESSION']['PWD'] = $_REQUEST['pwd'];      if (inject_check($_REQUEST['name']) || inject_check($_REQUEST['pwd'])) {         $RedURL = $_SERVER['PHP_SELF'];         header("Location: " . $RedURL);         exit;     }      if (isset($_REQUEST['language']) && $_REQUEST['language'] != "") {     $GLOBALS['GLOBALS']['_SESSION']['LanguageName'] = strtoupper($_REQUEST['language']); } else {  } if (!isset($_SESSION['LanguageName']) && $_SESSION['LanguageName'] == "") {     $GLOBALS['GLOBALS']['_SESSION']['LanguageName'] = strtoupper($_SERVER['HTTP_ACCEPT_LANGUAGE']);     if (similar_text($_SESSION['LanguageName'], "ZH-CN") == 5) {         $GLOBALS['GLOBALS']['_SESSION']['LanguageName'] = "ZH-CN";     } else {         if (similar_text($_SESSION['LanguageName'], "ZH-TW") == 5) {             $GLOBALS['GLOBALS']['_SESSION']['LanguageName'] = "ZH-TW";         } else {             $GLOBALS['GLOBALS']['_SESSION']['LanguageName'] = "EN";         }     } } if ($_SESSION['LanguageName'] == "") {     $GLOBALS['GLOBALS']['_SESSION']['LanguageName'] = "ZH-CN"; } ``` |

但很可惜一眼能看到过滤函数中把`'`单引号删除了，因此实际利用时不能做到执行的逃逸

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` function filter_inputXssKeyWord($str) {     $str = preg_replace( "/<(.*)s(.*)c(.*)r(.*)i(...