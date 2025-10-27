---
title: 巧用异或绕过限制导致rce
url: https://forum.butian.net/share/4130
source: 奇安信攻防社区
date: 2025-02-15
fetch_date: 2025-10-06T20:32:28.800596
---

# 巧用异或绕过限制导致rce

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

### 巧用异或绕过限制导致rce

* [漏洞分析](https://forum.butian.net/topic/48)

某课程系统后台RCE

巧用异或绕过限制导致rce
=============
0x00 系统介绍
---------
Moodle（[moodle.org](http://moodle.org/)）是一个开源的在线教育系统（慕课）。采用PHP+Mysql开发，界面友好，符合SCORM/AICC标准。以功能强大、而界面简单、精巧而著称。它是eLearning技术先驱，是先进在线教学理念和实践的集大成者，已成为全球大中学院校建立开放式课程系统的首选软件。主要模块：课程管理、作业模块、聊天模块、投票模块、论坛模块、测验模块、资源模块、问卷调查模块、互动评价（workshop）。Moodle具有先进的教学理念，创设的虚拟学习环境中有三个维度：技术管理维度、学习任务维度和社会交往维度，以社会建构主义教学法为其设计的理论基础，它提倡师生或学生彼此间共同思考，合作解决问题。
0x01 漏洞分析
---------
当教师出题目是计算题，可以包含\*变量\*（Moodle 称之为“通配符”），用花括号表示（例如`{a}`），可以将其分配给数字区间。每次生成问题时，变量都会被替换为定义数字范围内的不同值。
![image-20241009104853596](https://oss-yg-cztt.yun.qianxin.com/butian-public/f990aabd479e540113b6e146537bde591.png)
该系统会检测公式合规性，当公式符合要求后传递给`eval()`进行执行。如果可以绕过对公式的检测，就可以执行任意方法执行命令。下面分析一下相关操作代码
```php
public function calculate($expression) {
// Make sure no malicious code is present in the expression. Refer MDL-46148 for details.
if ($error = qtype\_calculated\_find\_formula\_errors($expression)) {
throw new moodle\_exception('illegalformulasyntax', 'qtype\_calculated', '', $error);
}
$expression = $this->substitute\_values\_for\_eval($expression);
if ($datasets = question\_bank::get\_qtype('calculated')->find\_dataset\_names($expression)) {
// Some placeholders were not substituted.
throw new moodle\_exception('illegalformulasyntax', 'qtype\_calculated', '',
'{' . reset($datasets) . '}');
}
return $this->calculate\_raw($expression);
}
protected function calculate\_raw($expression) {
try {
// In older PHP versions this this is a way to validate code passed to eval.
// The trick came from http://php.net/manual/en/function.eval.php.
if (@eval('return true; $result = ' . $expression . ';')) {
return eval('return ' . $expression . ';');
}
} catch (Throwable $e) {
// PHP7 and later now throws ParseException and friends from eval(),
// which is much better.
}
// In either case of an invalid $expression, we end here.
throw new moodle\_exception('illegalformulasyntax', 'qtype\_calculated', '', $expression);
}
```
可以看到`calculate\_raw`方法中对公示进行了直接执行，而在调用其的`calculate`方法中存在`qtype\_calculated\_find\_formula\_errors`方法用来检测公式的合法性。我们来看看是怎么进行检验的
```php
function qtype\_calculated\_find\_formula\_errors($formula) {
foreach (['//', '/\*', '#', '<?', '?>'] as $commentstart) {
if (strpos($formula, $commentstart) !== false) {
return get\_string('illegalformulasyntax', 'qtype\_calculated', $commentstart);
}
}
// Validates the formula submitted from the question edit page.
// Returns false if everything is alright
// otherwise it constructs an error message.
// Strip away dataset names. Use 1.0 to catch illegal concatenation like {a}{b}.
$formula = preg\_replace(qtype\_calculated::PLACEHODLER\_REGEX, '1.0', $formula);
// Strip away empty space and lowercase it.
$formula = strtolower(str\_replace(' ', '', $formula));
```
1. foreach是用来检测公式中是否有php标签，如果存在就报错
2. 将公式中变量，如{a}替换为1.0，该正则是匹配{}括号中必须以字母开头，同时并不能存在`>} <{"'`字符串
3. 将公式转换为小写并删除空格
```php
$safeoperatorchar = '-+/\*%>:^\~<?=&|!'; /\* \*/
$operatorornumber = "[{$safeoperatorchar}.0-9eE]";
while (preg\_match("~(^|[{$safeoperatorchar},(])([a-z0-9\_]\*)" .
"\\(({$operatorornumber}+(,{$operatorornumber}+((,{$operatorornumber}+)+)?)?)?\\)~",$formula, $regs)) {
switch ($regs[2]) {
// Simple parenthesis.
case '':
if ((isset($regs[4]) && $regs[4]) || strlen($regs[3]) == 0) {
return get\_string('illegalformulasyntax', 'qtype\_calculated', $regs[0]);
}
break;
// Zero argument functions.
case 'pi':
if (array\_key\_exists(3, $regs)) {
return get\_string('functiontakesnoargs', 'qtype\_calculated', $regs[2]);
}
break;
// Single argument functions (the most common case).
case 'abs': case 'acos': case 'acosh': case 'asin': case 'asinh':
case 'atan': case 'atanh': case 'bindec': case 'ceil': case 'cos':
case 'cosh': case 'decbin': case 'decoct': case 'deg2rad':
case 'exp': case 'expm1': case 'floor': case 'is\_finite':
case 'is\_infinite': case 'is\_nan': case 'log10': case 'log1p':
case 'octdec': case 'rad2deg': case 'sin': case 'sinh': case 'sqrt':
case 'tan': case 'tanh':
if (!empty($regs[4]) || empty($regs[3])) {
return get\_string('functiontakesonearg', 'qtype\_calculated', $regs[2]);
}
break;
// Functions that take one or two arguments.
case 'log': case 'round':
if (!empty($regs[5]) || empty($regs[3])) {
return get\_string('functiontakesoneortwoargs', 'qtype\_calculated', $regs[2]);
}
break;
// Functions that must have two arguments.
case 'atan2': case 'fmod': case 'pow':
if (!empty($regs[5]) || empty($regs[4])) {
return get\_string('functiontakestwoargs', 'qtype\_calculated', $regs[2]);
}
break;
// Functions that take two or more arguments.
case 'min': case 'max':
if (empty($regs[4])) {
return get\_string('functiontakesatleasttwo', 'qtype\_calculated', $regs[2]);
}
break;
default:
return get\_string('unsupportedformulafunction', 'qtype\_calculated', $regs[2]);
}
// Exchange the function call with '1.0' and then check for
// another function call...
if ($regs[1]) {
// The function call is proceeded by an operator.
$formula = str\_replace($regs[0], $regs[1] . '1.0', $formula);
} else {
// The function call starts the formula.
$formula = preg\_replace('~^' . preg\_quote($regs[2], '~') . '\([^)]\*\)~', '1.0', $formula);
}
}
```
接下来就是定义了白名单安全运算符字符`-+/\*%>:^\~<?=&|!`，以及运算符加数字和科学计数法的e字母
随后进入while循环判断正则`preg\_match("~(^|[{$safeoperatorchar},(])([a-z0-9\_]\*)" ."\\(({$operatorornumber}+(,{$operatorornumber}+((,{$operatorornumber}+)+)?)?)?\\)~",$formula, $regs)`匹配公式的结果
```php
这个正则表达式用于匹配一个包含标识符和参数的函数调用格式。具体来说，它匹配以下内容：
1.开头部分：
^ 或者一个运算符或括号：[-+/\*%>:^\~<?=&|!,(]。
2. 标识符部分：
紧接着是由小写字母、数字或下划线组成的字符串 [a-z0-9\_]\*。
3. 函数调用括号：
然后是一个开括号 (。
4.函数参数部分：
括号内可以包含一个或多个符合 [-+/\*%>:^\~<?=&|!.0-9eE] 的项，这些项之间用逗号分隔，并且可以有多层嵌套。
总结来说，这个正则表达式匹配的是像 func(a, 1.5, +2) 这样的函数调用，其中 func 是一个标识符，括号内包含由运算符和数字组成的参数。
```
该表达式主要是匹配公式中的方法名加参数，并将结果存入$regs数组中，如
```php
$formula="func(1)"
$regs=Array
(
[0] => func(1)
[1] =>
[2] => func
[3] => 1
)
$formula="\*func(1,2)"
$regs=Array
(
[0] => func(1,2)
[1] => \*
[2] => func
[3] => 1,2
[4] => ,2
)
```
可以看到
- $regs\[0\]：匹配到整个函数调用，如果前面有运算符或者括号也会被匹配到
- $regs\[1\]：方法名前的运算符或者括号
- $regs\[2\]：方法名
- $regs\[3\]...：函数参数部分
回到代码逻辑，while循环中判断公式中的函数名，当不在规定的函数名中会报错返回。
如果函数调用正确，即函数名和参数数量符合要求，会来到下面的逻辑
```php
if ($regs[1]) {
// The function call is proceeded by an operator.
$formula = str\_replace($regs[0], $regs[1] . '1.0', $formula);
} else {
// The function call starts the formula.
$formula = preg\_replace('~^' . preg\_quote($regs[2], '~') . '\([^)]\*\)~', '1.0',$formula);
}
```
这里主要是把函数调用替换为`"1.0"`，即`(cos(1))`会被替换为`(1.0)`。
最后while循环结束后还会进行判断
```php
if (preg\_match("~[^{$safeoperatorchar}.0-9eE]+~", $formula, $regs)) {
return get\_string('illegalformulasyntax', 'qtype\_calculated', $regs[0]);
} else {
// Formula just might be valid.
return false;
}
```
如果最终的公式中存在除了正确运算符或者数字或者eE外其他字符时也会报错，不存在会被鉴定为正确的公式。
0x02 绕过分析
---------
通过上面对公式的正则分析，我们发现直接调用system等方法是不行的。
```php
$safeoperatorchar = '-+/\*%>:^\~<?=&|!';
```
这是我们想到了无字母rce的思路，但是常见的`$`和`[`（方括号）符号应为不在运算字符里也是不能用的，只能使用`^`异或符。
而在白名单函数中`acos`函数，是返回一个数的反余弦，如果 `x` 不在 \[-1, 1\] 范围内，函数将返回 NaN，并设置适当的数学错误（例如 `EDOM`）。即`acos(2):"NAN"`。
这意味着像“ `acos(2) . acos(2)`”这样的表达式会生成\*字符串\*“ `NANNAN`”。但是，无法立即连接两个 `acos`调用，因为验证逻辑不允许在调用之间没有实际“运算符”的情况下进行第二次调用。幸运的是，我们很快发现可以使用`acos(2) . 0+acos(2)` 来绕过，因此我们最终可以生成`NANNAN`。
比如：
```php
(acos(2) . 1) ^ (0 . 0 . 0) ^ (1 . 1 . 1)
==>
NAN1 ^ 000 ^ 111
按位XOR==>
...