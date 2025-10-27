---
title: 原创 | Thinkphp3.2.3 SQL注入总结
url: https://mp.weixin.qq.com/s?__biz=MzI4Mzc0MTI0Mw==&mid=2247496160&idx=1&sn=e76b5c8d41197103bde0f476f7beb2c4&chksm=eb84acb4dcf325a29b7216de39f01f6b9f7d2dd745c26459b15d71c787a71faa387bf7a288ad&scene=58&subscene=0#rd
source: SecIN技术平台
date: 2022-12-15
fetch_date: 2025-10-04T01:33:09.486015
---

# 原创 | Thinkphp3.2.3 SQL注入总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJnqInhQmRAZJrTW5YPF9sPbUqEHLEpROxMZjI4CwYXB4Z2UCM6XUfibw/0?wx_fmt=jpeg)

# 原创 | Thinkphp3.2.3 SQL注入总结

原创

Sentiment

SecIN技术平台

**点击蓝字**

**关注我们**

下载：ThinkPHP3.2.3完整版 - ThinkPHP框架

https://sec-in.com/outLinkPage/?target=https://www.thinkphp.cn/donate/download/id/610.html

**配置**

`ThinkPHP/Conf/convention.php`配置下数据库，我这里直接用的sqllabs的数据库

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJA6Rwa3nG6UHxvVcQSRvZXzwfBwap8icuh4G1Tia6X9KeTjTTiaDc1icCvQ/640?wx_fmt=jpeg)

写个查询入口`Application/Home/Controller/IndexController.class.php`

```
<?phpnamespace Home\Controller;use Think\Controller;class IndexController extends Controller {    public function index(){        highlight_file(__FILE__);        $data = M('users')->find(I('GET.id'));        var_dump($data);    }}
```

用的是sqllabs的users表

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJ83D4LWr60CHISXUjALy3JrPGv52E5IfzYK3COTHYQdvTFWic4A1LEyA/640?wx_fmt=jpeg)

thinkphp3内置了很多大写函数

```
A 快速实例化Action类库B 执行行为类C 配置参数存取方法D 快速实例化Model类库F 快速简单文本数据存取方法I 获取系统输⼊变(与tp5input方法类似)L 语言参数存取方法M 快速高性能实例化模型R 快速远程调用Action类方法S 快速缓存存取方法U URL动态生成和重定向方法W 快速Widget输出方法
```

**常规注入**

## 既然审计SQL注入漏洞了，那常规的注入方式1' or 1=1#肯定是不行的了，但具体为什么不行这里简单的分析下

## int型

id若是int类型的，会经过`intval()`处理，最后`1' or 1=1#`就变成了`1`，看下大体流程

### I方法

首先是进入`D方法`但D方法就是实例化⾃定义模型类，没啥东西，就直接调到`I方法`了，I方法前边也是一些常规操作，跟一边就能看懂很容易理解,直接看下边的取值部分

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJMkDc3cEkstiaLubhAbrE8XAwwLuZYXucocRdMIQz1zo3SHfHhQJ4HkQ/640?wx_fmt=jpeg)

经过前边的一系列操作后,`$input`的值就是我们传入的`1' or 1=1#`，`$name`就是id，`$filters`取得是默认值`htmlspecialchars`,之后就进入了下边的一些没影响的if判断和操作

进到这里，判断`$data`是否为数组(很明显不是)，所以$data的值就是`htmlspecialchars(1' or 1=1#)`,htmlspecialchars不会处理单引号所以经过此次过滤后，其实$data的值并没变

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJSO0gruYeheZtmPC7poxzISziaxmVSIpM9sS9vT2qYpkxNr64XmWUuFg/640?wx_fmt=jpeg)

最后经过一系列判断`retrun \$data;`了

### find方法

retrun给了find方法，还是跳过没影响的部分，`\$options`的值就是retrun $data;后来又经过746这行加了个limit

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJIaME38gTtho3x8kDY4BMlwJFgqxFrwrDRJ1bcXu2CDaDfURydibFXSw/640?wx_fmt=jpeg)

直接进入`_parseOptions()`

前边通过`$options['table'] = $this->getTableName();`，获取了表名users，之后就进入了`_parseType()`方法

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJYUUUwIrtNcaRzavdbz4BOamDRO8gHia5VTMKjiaM4ic8a1oIib5nOuALNw/640?wx_fmt=jpeg)

跟进后先看下执行到683行的值

`\$data[\$key]=\$data[id]=1' or 1=1#`

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJvsbkPIVHzL862jPdJ7PHUytViarJ3twjODfa0JcutRj1I9OiaytkJMhQ/640?wx_fmt=jpeg)

之后经过了if判断，由于id定义的是int型，所以这里直接就执行intval了，id的值就变成了1，所以这里无法闭合也就结束了

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJvCFo1vib8icPMbhO3SyicXaibpiaHU3bl423RVgRwWZSibj7FjUGiaicic4vGrw/640?wx_fmt=jpeg)

## varchar型

int型不行后我又改成了varchar类型(修改时需要关闭AUTO\_INCREMENT选项)

接着上边的分析，在经过`_parseType()`方法后，下边又执行了`select()`

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJ4Gfx6EibzehTlpTbL0icqrF3sFF9Es8fDia3ZfoFrHCmENhsmxy9qgPng/640?wx_fmt=jpeg)

在经过944行的`parseBind`后，id的值仍为`1' or 1=1#`，但经过945后，值发生转义了，所以跟进一下`buildSelectSql()`方法

跟进`parseSql()`

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJzFOm00AxzoYEhVIEahmD7MuKNyORBhCjc5vl8yNnyCmcekytQrK86w/640?wx_fmt=jpeg)

我们的值在where里所以直接跟进`parseWhere`这一条

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJSl7OBXwyrXVcrjygeCANicvxDm6tYcVfEic2u93FiajmM4oiaxIH1D0oyA/640?wx_fmt=jpeg)

`parseWhere`中会执行`parseWhereItem`,之后又会执行`parseValue`

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJEtxS3jS75jcIr8oL1Quu3NrvZvfRY3KicibISRmyt05ALeKZdx3tbBxw/640?wx_fmt=jpeg)

进入第一个if会执行`\$this->escapeString(\$value) : '\''.\$this->escapeString(\$value).'\'';`

escapeString对单引号进行转义，所以这里varchar型也就失败了

```
public function escapeString($str) {    return addslashes($str);}
```

**数组绕过**

传入`?id[where]=1`

`I方法`前边都一样，在最后retrun的前一步由于本次传入的是数组，所以进入了`think_filter`方法![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJRAtXS0Wsjibj7w4R0PWrGiaPCQhYwAI4CAlyKx8Bl10ugCuDrcu56HWA/640?wx_fmt=jpeg)

但其实也没啥东西只对开头部分做检测，根本不需要绕过

```
function think_filter(&$value){   // TODO 其他安全过滤
   // 过滤查询特殊字符    if(preg_match('/^(EXP|NEQ|GT|EGT|LT|ELT|OR|XOR|LIKE|NOTLIKE|NOT BETWEEN|NOTBETWEEN|BETWEEN|NOTIN|NOT IN|IN)$/i',$value)){        $value .= ' ';    }}
```

之后就还是进入`_parseOptions()`，再次看`_parseType()`这部分，注意options的值，前后对比：

之前：

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJIaME38gTtho3x8kDY4BMlwJFgqxFrwrDRJ1bcXu2CDaDfURydibFXSw/640?wx_fmt=jpeg)

现在：![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJ8BQp4Mggeq9DXdCS826n5b189jdcw8yfGyjG2NvibfG7D4WfRaVp0UA/640?wx_fmt=jpeg)

很明显where不是数组了，所以在经过第一条if检测时就不满足`is_array($options['where'])`了，所以这里就绕过了`_parseType()`，从而就绕开了int型中提到的`intval`转换

```
if(isset($options['where']) && is_array($options['where']) && !empty($fields) && !isset($options['join'])) {
```

## 之后就是解决第二个问题——varchar类型中的`escapeString()`转义。前边的`select()->buildSelectSql()->parseSql()`就不说了跟之前都一样，直接看`parseWhere()`这里

```
protected function parseWhere($where) {    $whereStr = '';    if(is_string($where)) {        // 直接使用字符串条件        $whereStr = $where;    }else{ // 使用数组表达式
```

## 之前是由于where是数组进入了else再执行一步步操作后，执行到了`escapeString()`,但这里where变成了字符串所以直接就走if里的语句了，执行后就直接retrun返回了![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJmUKGHdqOicZFpF7mPNQrkXJib2Gibxo0AcZd0ntrUr2m57Ea9J6nLtIuA/640?wx_fmt=jpeg) 在执行完`parseSql()`后，看下returun返回值`SELECT * FROM`users`WHERE 1 LIMIT 1`

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJX5nM0lvvEsUlGLVaalUcVaDF41xxbB9MicTzYI7oEbFVfW2tmibkCOmg/640?wx_fmt=jpeg)之后就返回到select中被query成功执行了

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJG80Ria6iaic0ib1zRIlV1C6q9CcBOhe9LSmMvU5JVEjE4Cf2rXn5CgN38g/640?wx_fmt=jpeg)

payload

```
?id[where]=0 union select 1,group_concat(username,0x2a,password),3 from users#?id[where]=1 and 1=updatexml(1,concat(0x7e,(select password from users limit 1),0x7e),1)#
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJp1KHLR4jic7LKuXnNpOIYicXysR2weYV2NM7YmxwBwTtibKvvSdicCEMOg/640?wx_fmt=jpeg)

**EXP注入**

改下controller

```
<?phpnamespace Home\Controller;use Think\Controller;class IndexController extends Controller {    public function index(){        highlight_file(__FILE__);        $User = D('Users');        $map = array('username' => $_GET['username']);        // $map = array('username' => I('username'));        $user = $User->where($map)->find();        var_dump($user);    }}
```

先贴payload：

```
?username[0]=exp&username[1]==-1 union select 1,2,3
```

exp注入这里用到的是where、而之前数组注入时用的是`I方法`,原因在于若执行`I方法`,会执行到`think_filter`对exp开头的数据进行过滤，而从payload也可以看出这里是以exp开头的，所以这里选用了`where`方法

先看`where方法`,这里直接跳到最后(因为前边的if判断都没有执行)，这里通过值也能看出，其实就是我们GET传参的内容

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJmXR64gPTCeKMSY8sIiasTnXjy2O3Uyz7HH8adsHvEamwicmJbxLdNm3Q/640?wx_fmt=jpeg)

之后的操作就一样了，到`find()`方法，执行`_parseOptions()`，然后就到了下边这里，通过foreach将`$options['where']`的值给`$val`再通过`is_scalar($val)`进行标量`( integer、float、string 或 boolean)`判断，很明显$val是数组不是标量,所以直接绕过了`_parseType()`,也就绕开了`intval`转换

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJqZsdiaia3iaUh8AHE4ZRSOl9nnVxMvA5gc2nkANwKQ7NISOYia6kuhXAQg/640?wx_fmt=jpeg)

之后又一样了，`select()->buildSelectSql()->parseSql()->parseWhere()`，再执行`parseWhereItem()`，正则部分为false，所以直接跳到了下方的elseif，对$whereStr赋值，此时$key=username $var[1]="=-1 union select 1,2,3"，所以最终的$whereStr=username=-1 union select 1,2,3

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJ2vWRYLSp3geMzDSLvUYuicHp7FplsbrcIw3phQxcv869HUpfo405uvw/640?wx_fmt=jpeg)

最终就是return 一步步返回 成功执行sql语句

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprgzUBM2CYFicXscWkmAuhAJibQnYibpM9bMCicgUico8U4smNicLRg0PTQxFBktbCqt4YbZIuJrjOz6z8A/640?wx_fmt=jpeg)

```
SELECT * ...