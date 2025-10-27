---
title: 某开源OA白名单后缀限制下巧用系统设计getshell
url: https://forum.butian.net/share/4132
source: 奇安信攻防社区
date: 2025-02-26
fetch_date: 2025-10-06T20:32:31.328021
---

# 某开源OA白名单后缀限制下巧用系统设计getshell

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

### 某开源OA白名单后缀限制下巧用系统设计getshell

白名单后缀限制下巧用系统设计getshell

白名单后缀限制下巧用系统设计getshell
======================
0x01 路由情况
---------
该 OA 的 `action` 主要是在 `webmain` 目录下
![image-20241212162149500](https://oss-yg-cztt.yun.qianxin.com/butian-public/f9f24e7ab921f7a2c0790b9806dc37899.png)
然后通过请求参数中的 `d`、`m`、`a` 定位到具体的 `action` 中的方法进行调到
![image-20241212162759549](https://oss-yg-cztt.yun.qianxin.com/butian-public/fe2806ed78974fc90aeaced424d945561.png)
如 `d=systam&m=admin|admin&a=login` 相当于调用 `webmain/system/admin/adminAction.php#login()`
而所有的 action 都会继承 `mainAction`，当我们请求某个 action 时首先会调用父类 `mainAction` 的 `\_\_construct`，进行初始化的一些操作
![image-20241212163105144](https://oss-yg-cztt.yun.qianxin.com/butian-public/fb54d0925e84e80397728251472968a5e.png)
其中我们发现有关鉴权的处理被子类的 `initAction` 所实现，比如 apiAction 中
![image-20241212163352786](https://oss-yg-cztt.yun.qianxin.com/butian-public/f40c101b8cbc28e53bb155539c626b590.png)
0x02 前台注入
---------
### 2.1 代码分析
在查看 initAction 的实现时发现有个类实现该方法未存在鉴权
![image-20241212164620499](https://oss-yg-cztt.yun.qianxin.com/butian-public/f14e870a28a27a71e2593f6644fcb77ff.png)
且其功能点说明是上传文件，我们着重看一下怎么个事
```php
public function xxxxAction()
{
if(!$\_FILES)exit('sorry!');
$upimg = c('upfile');
$maxsize= (int)$this->get('maxsize', $upimg->getmaxzhao());//上传最大M
$uptypes= 'jpg|png|docx|doc|pdf|xlsx|xls|zip|rar';
$upimg->initupfile($uptypes, ''.UPDIR.'|'.date('Y-m').'', $maxsize);
$upses = $upimg->up('file');
if(!is\_array($upses))exit($upses);
$arr = c('down')->uploadback($upses);
$arr['autoup'] = (getconfig('qcloudCos\_autoup') || getconfig('alioss\_autoup')) ? 1 : 0; //是否上传其他平台
return $arr;
}
```
该方法主要是定义了白名单上传后缀 `$uptypes`，调用 up 方法进行上传后返回文件信息，然后调用 `uploadback`，跟进到其中
```php
public function uploadback($upses, $thumbnail='', $subo=true)
{
$msg = '';
$data = array();
if(is\_array($upses)){
$fileext= substr($upses['fileext'],0,10);
$arrs = array(
'adddt' => $this->rock->now,
'valid' => 1,
'filename' => $this->replacefile($upses['oldfilename']),
'web' => $this->rock->web,
'ip' => $this->rock->ip,
'mknum' => $this->rock->get('sysmodenum'),
//'mid' => $this->rock->get('sysmid','0'),
'fileext' => $fileext,
'filesize' => (int)$this->rock->get('filesize', $upses['filesize']),
'filesizecn'=> $upses['filesizecn'],
'filepath' => str\_replace('../','',$upses['allfilename']),
'optid' => $this->adminid,
'optname' => $this->adminname,
'comid' => m('admin')->getcompanyid(),
);
$arrs['filetype'] = m('file')->getmime($fileext);
//判断是不是需要压缩jpg和jpeg
...
$bo = $this->db->record('[Q]file',$arrs);
if(!$bo)$this->reutnmsg($this->db->error());
$id = $this->db->insert\_id();
}
```
该方法主要是通过之前 `up` 方法上传文件返回的数组 `$upses` 和全局配置信息构造 `$arrs`，然后调用 `$this->db->record` 方法操作 `$arrs`。
来到 `record` 方法
```php
public function record($table,$array,$where='')
{
$addbool = true;
if(!$this->isempt($where))$addbool=false;
$cont = '';
if(is\_array($array)){
foreach($array as $key=>$val){
$cont.=",`$key`=".$this->toaddval($val)."";
}
$cont = substr($cont,1);
}else{
$cont = $array;
}
$table = $this->gettables($table);
if($addbool){
$sql="insert into $table set $cont";
}else{
$where = $this->getwhere($where);
$sql="update $table set $cont where $where";
}
return $this->tranbegin($sql);
}
```
这里就直接操作 `$array` 为 `key=value` 格式然后逗号拼接后带入到 SQL 语句中执行
控制了$array 中的内容就能实现 SQL 注入，而其中`filename`、`filepath`、`filetype`等这几个键的内容是通过上传文件获取到的，那我们对上传文件名做文章是不是就可以造成 sql 注入呢。
```php
public function up($name,$cfile='')
{
if(!$\_FILES)return 'sorry!';
$file\_name = $\_FILES[$name]['name'];
$file\_size = $\_FILES[$name]['size'];//字节
$file\_type = $\_FILES[$name]['type'];
$file\_error = $\_FILES[$name]['error'];
$file\_tmp\_name = $\_FILES[$name]['tmp\_name'];
$zongmax = $this->getmaxupsize();
if($file\_size<=0 || $file\_size > $zongmax){
return '文件为0字节/超过'.$this->formatsize($zongmax).'，不能上传';
}
...
return array(
'newfilename' => $file\_newname,
'oldfilename' => $file\_name,
'filesize' => $file\_size,
'filesizecn' => $file\_sizecn,
'filetype' => $file\_type,
'filepath' => $save\_path,
'fileext' => $file\_ext,
'allfilename' => $allfilename,
'picw' => $picw,
'pich' => $pich
);
}else{
return '上传失败：'.$this->geterrmsg($file\_error).'';
}
}
```
通过 `up` 方法的返回值构造可以看到 `oldname` 其实就是上传文件的文件名，这也证实我们的想法。
### 2.2 漏洞复现
![image-20241213160417988](https://oss-yg-cztt.yun.qianxin.com/butian-public/f8ec4855bf098b2e9ee66fcfcea7a3d47.png)
0x03 扩大危害 RCE
-------------
#### 3.1 漏洞点
该 cms 自己实现了写入文件接口，我们查看其用法中写入
![image-20241216161934097](https://oss-yg-cztt.yun.qianxin.com/butian-public/fdfaa1acf267a19237d4a3b70b08e1efd.png)
通过这么多处调用我们发现有一处调用会写入 php 中
```php
$apaths = ''.P.'xxxx/mode\_'.$modenum.'Action.php';
$apath = ''.ROOT\_PATH.'/'.$apaths.'';
if(!file\_exists($apath)){
$stra = '<?php
/\*\*
\* 此文件是【'.$modenum.'.'.$rs['name'].'】。
\*/
....
';
$this->rock->createtxt($apaths, $stra);
}
```
要是我们能控制 `$modenum` 或是 `$rs['name']` 的内容就可以 getshell，不过 `$modenum` 同时也控制了文件名所以我们只能通过控制 `$rs['name']` 来 getshell。
```php
$setid = (int)$this->get('setid','0');
$rs = m('flow\_set')->getone("`id`='$setid'");
if(!$rs)exit('sorry!');
$rs['xxx'] = count(explode(',', (string)$rs['tables']));
$modenum = $rs['num'];
```
而 `$rs` 数组是由 `flow\_set` 数据库获取到的，
![image-20241213165334926](https://oss-yg-cztt.yun.qianxin.com/butian-public/fb6c35cc694af6040890a909ffc76b7db.png)
下面是 `flow\_se` 默认的数据信息，要是我们可以插入或者修改数据就可以。
#### 3.2 寻找漏洞触发点
根据常规思路我们只要寻找有插入 `flow\_set` 表的方法即可。还真被我找到一个
```php
public function xxxAction()
{
$name = $this->rock->xssrepstr($this->post('name'));
$fields = c('pingyin')->get($name,1);
..
$num = 'zz'.$fields.'';
$id = 0;
$uarr['name'] = $name;
$uarr['num'] = $num;
$uarr['table'] = $num;
...
$id = m('flow\_set')->insert($uarr);
```
构造 poc，闭合前面写入文件时的注释为
```php
\*/eval($\_GET['a']);/\*
```
实际发现在 `$this->rock->xssrepstr` 中对特殊字符做了处理
```php
public function xssrepstr($str)
{
$xpd = explode(',','(,), , ,<,>,\\,\*,&,%,$,^,[,],{,},!,@,#,",+,?,;\'');
$xpd[]= "\n";
return str\_ireplace($xpd, '', $str);
}
```
括号之类的都被过滤点了，这个利用点看来无法利用了，那我们只能再找找有没有可以执行 SQL 语句且传参会不进行过滤的点。
通过在 web 目录下查找系统重写的 sql 执行方法 `query`，在某处方法中找到疑似执行任意 sql 语句的方法
```php
if(getconfig('systype')=='demo')exit();
if($this->adminid!=1)return '只有ID=1的管理员才可以用';
$folder = $this->post('folder');
$sida = explode(',', $this->post('sid'));
$alltabls = $this->db->getalltable();
$shul = 0;
$tablss = '';
foreach($sida as $id){
$ids = substr($id,0,-5);
$ida = explode('\_', $ids);
$len = count($ida);
$fieldshu = $ida[$len-2];
$total = $ida[$len-1];
$tab = str\_replace('\_'.$fieldshu.'\_'.$total.'.json','', $id); //表
$filepath = ''.UPDIR.'/data/'.$folder.'/'.$id.'';
if(!file\_exists($filepath))continue;
$data = m('beifen')->getbfdata('',$filepath);
if(!$data)continue;
$dataarr = $data[$tab];
//表不存在
if(!in\_array($tab, $alltabls)){
$createsql = arrvalue($dataarr, 'createsql');
if($createsql){
$this->db->query($createsql, false);
}else{
continue;
}
}
```
在该方法中通过处理传入的 `sid`，获取 table 名，如果 table 名不在数据库所有表名中时，会获取某个目录下 `$sid` 名的文件内容作为数组并取得 `createsql` 的内容进行 sql 语句执行。
那么就是说如果 `sid` 可控文件内容，同时 `sid` 不在表内那么我们就能构造修改 `flow\_set` 数据的 sql，而且目录 `folder` 也是可控的，似乎离成功近在咫尺了，我们找找有没有方法可以写入文件。
在用上面方法寻找文件写入的方法是我们发现好多文件名都是带了随机数，这不太好控制其位置，所以我们要找一个文件名不带随机数的写入点。
比如下面这个
```php
public function savetopdfAjax()
{
$imgbase64 = $this->post('imgbase64');
if(isempt($imgbase64))return returnerror('无数据');
$path = ''.UPDIR.'/logs/'.date('Y-m').'/abc.png';
$bo = $this->rock->createtxt($path, base64\...