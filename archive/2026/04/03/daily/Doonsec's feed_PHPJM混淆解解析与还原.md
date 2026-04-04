---
title: PHPJM混淆解解析与还原
url: https://mp.weixin.qq.com/s/Ihc4xqQhQ-gbYXBd4OK4pA
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:11:18.915999
---

# PHPJM混淆解解析与还原

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sibpvO9ayaSziclUk6FoNxlNFhZTGSfibpV6G52ibYB72Gs4rRSxib0lGlccuQyGiakeG7AUiaZt1eVH8Wg9WpZBNKK863rG5bmfY7gmBZ16U7sIGs/0?wx_fmt=jpeg)

# PHPJM混淆解解析与还原

原创

Syn3x
Syn3x

UNSAFE-TEAM

![]()

在小说阅读器中沉浸阅读

## 写在前面

最近在工作中遇到了一些高度混淆的PHP恶意文件，经分析发现其使用了第三方通用加密平台提供的加密服务，文件特征分别对应 phpjm.net 与 phpjiami.com 两个平台。本文以 phpjm.net 为研究对象，对其加密机制展开学习与分析，并进行解密还原。

## 混淆分析

先编写一段示例代码用来做测试，代码如下

```
● ● ●

<?php
if ($_GET['display'] == true) {
    phpinfo();
}
```

需要注意的是phpjm.net的加密算法只能使用`php<7`的版本使用，根据报错推测原因是加密过程中会掺杂一些随机的字符，而这些字符对于php7来说都是非法字符，识别上较为严格，无法执行，php5则会静默忽略或跳过。经过phpjm混淆过后会变成了下面样子![](https://mmbiz.qpic.cn/mmbiz_png/sibpvO9ayaSwGQjjTATqpSqAxliatBuPz1ZwS2UneZf8RNr0ephxl4XdxFzRaWQqJUN9uTKD4cpyj44NPwLUNzbjcAPiaDw4UcibXavclFn7vls/640?wx_fmt=png&from=appmsg)方法名字，变量名字全都已经被不可见字符混淆过了，在vsc和phpstorm中显示的都是`�`。分析前使用phpstorm进行格式化一下，分析起来会更加方便一些，格式化后的代码如下

```
● ● ●

<?php
/*
������������Ϣ�����Ǳ�php�ļ������ߣ����Ա��ļ�����������Ϣֻ���ṩ�˶Ա�php�ļ����ܡ������Ҫ��PHP�ļ����м��ܣ��밴������Ϣ��ϵ��
Warning: do not modify this file, otherwise may cause the program to run.
QQ: 1833596
Website: http://www.phpjm.net/
Copyright (c) 2012-2026 phpjm.net All Rights Reserved.
*/
if (!defined("ECFFAFDC")) {
    define("ECFFAFDC", __FILE__);
    global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
    function ��($��, $��� = "")
    {
        global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
        if (empty($���)) {
            returnbase64_decode($��);
        } else {
            return ��($����������($��, $���, $����($���)));
        }
    }

    $���� = ��("c3RycmV2�");
    $���������� = ��("c3RydHI=�");
    $�� = ��("G3p1bwNvbXByGX�Nz�", "ZwCmG");
    $��� = ��("SzYzOWIzMmY0MaMwED�FjYjY2MDU0YzlhYTUy�NDNhODgwS�2U=�", "LaZEGS");
    $�������� = ��("NXNhbA==�", "ZWHON");
    $��������� = ��("UmFzZTU0�X2RlU29k�ZC==�", "YCvGgJQU");
    $��������������� = ��("IHJlZ19yZXBsYVNl�", "ctWOLdVhI");
    function ����(&$����)
    {
        global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
        $���������������� = ��("SGLL�", "ZTLNlCS");
        @$���������������($���, $�������� . "(@$��($���������('eNptkm9P2lAU�xr8KaXhxm1Wl�FgeE3GzMqNgs�mDIchW0h9A9Q�pQsKQ7tpplAM�0iGFFoqA0I+6�3hbJCHt5z/M7�555znuM3oGED�jJYjV3Q6CFWM�wLLXF1yVxvCo�v6M+Grqr19nS�FXcUOa8zEE4Q�wzP7dYSo2lR7�7Ho14tlyJs3A�PtJLR9+V+EnM�LWPoU2tozl2o�JperNTZREeVT�aCIww9drCBoO�dH0+WfS1qcsl�qc9SkuKVscPw�qYt0EjFdtTFo�tpptoz1vuRSf�ZsieQ3Cf9i9L�Z4c0j6jnXtN8�Gt11Fo3pg9d9�Jb1XyLC0kmH1�c3fEPF9M/mCk�CsKnrRfrSVON�3tgazu5cXs4q�VY5SyjPUIHOs�JCRBRmi/83vc�th7Ml4k6GkwM�b3XFOF1WyEgt�w6rJs3wMwmfU�snIgnaayRXd8�G+Zyh8cfD3K5�qFQAG1UAtgO2�37zDv4IdjHBo�wq/1bBz/5R8M�7rs2RK8v5Lfo�rViuiqugYUdv�l8tHL+DFCR92�ya2ccwSPAK8k�8erFksc35l+h�a5aAZUFii6Rw�CNeUf00Ba8p/�8gPEFrWLb2O8�EBYEURQLITL0�Npjf3QtSlBAu�hIJhIVAIiCGM�IHHc/c13c+Pb�WJkNnPbuR6YN�3zvrAf6ZqS4a�uvpHBW4UjbUK�2bAmySJK0Hre�NVBZkpMTdY79�kKpYbOJnC9ms�xFLoHP4CagIz�Aw==�')));", "���
������639b32f40c0d1cb66054c9aa5243a880�����");
        return"/";
    }
} else {
    global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
    $���� = ��("c3RycmV2�");
    $���������� = ��("c3RydHI=�");
    $�� = ��("G3p1bwNvbXByGX�Nz�", "ZwCmG");
    $��� = ��("SzYzOWIzMmY0MaMwED�FjYjY2MDU0YzlhYTUy�NDNhODgwS�2U=�", "LaZEGS");
    $�������� = ��("NXNhbA==�", "ZWHON");
    $��������� = ��("UmFzZTU0�X2RlU29k�ZC==�", "YCvGgJQU");
    $��������������� = ��("IHJlZ19yZXBsYVNl�", "ctWOLdVhI");
}
$��������� = ��("rU5vejrm�VXdBd0FE�UVFGQr8=�", "ZYeLr");
$�������� = ����($���������);
@$���������������($���, $�������� . "(@$��($���������('eNotjM1q�g0AURveFvsMsLkTh�voFNXJW+�QHellEIT�KpRUmmRR�SknU0Yyj�0dEZf+IkzqvWRZff�4ZzPcRd3�rv/u3954�K2LBy8P9�49Pszdv" . $��������� . $�������� . "fs2cy�n5Pt125p�kx8ySd56�9WnZDvkl�/xXZrTfL�rQUSISsR�glYh1HVw�QuA0lQKB�ZjpLpymF�7ho1Trzs�jT4GFcJF�URMKmlOE�phZiHEyV�aQQWiCTf�m1wfC4QT�Desojphk�Y4xwLiNVtAduQp1M�3zq+dkVG�Zdl3zeWAkMamNIVS�I28YP0cI�Fd/3rEvU�daBtPUhp�O+7iD7ZA�Z0Q=�')));", "���
������639b32f40c0d1cb66054c9aa5243a880������");
returntrue; ?>0247589c0301a1ae1ea887304a867032
```

直接看虽然大部分都看不懂，但中间部分的变量仍能看出明显的 base64 编码特征，并且里面有一个位置`base64_decode`并没有混淆，这部分代码如下

```
● ● ●

    // define("ECFFAFDC", __FILE__);
    // global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
    function ��($��, $��� = "")
    {
        // global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
        if (empty($���)) {
            returnbase64_decode($��);
        } else {
            return ��($����������($��, $���, $����($���)));
        }
    }

    $���� = ��("c3RycmV2�");
    $���������� = ��("c3RydHI=�");
    $�� = ��("G3p1bwNvbXByGX�Nz�", "ZwCmG");
    $��� = ��("SzYzOWIzMmY0MaMwED�FjYjY2MDU0YzlhYTUy�NDNhODgwS�2U=�", "LaZEGS");
    $�������� = ��("NXNhbA==�", "ZWHON");
    $��������� = ��("UmFzZTU0�X2RlU29k�ZC==�", "YCvGgJQU");
    $��������������� = ��("IHJlZ19yZXBsYVNl�", "ctWOLdVhI");
    function ����(&$����)
    {
        // global $�, $��, $���, $����, $�����, $������, $�������, $��������, $���������, $����������, $����������, $������������, $�������������, $��������������, $���������������, $���������������;
        $���������������� = ��("...");
        return"/";
    }
```

里面注释的部分可以先忽略掉，因为没有实质性的逻辑，对于分析，不看也可以。在IF中函数定义的部分代码大致可以分为三个部分看，`��`方法部分，赋值部分，`����`方法部分，实际这样看也不算太多内容，单独看第一个函数，大致看逻辑如下

```
● ● ●

    function ��($��, $��� = "")
    {
        // 如果第二个变量为空
        if (empty($���)) {
            // 把第一个参数base64解码后返回
            return base64_decode($��);
        } else {
            // 否则做运算，其中里面是嵌套了两层当前函数
            return ��($����������($��, $���, $����($���)));
        }
    }
```

在第二部分都是通过第一个方法进行解密的，在这部分能看懂的基本就是很多参数都是base64编码的，结合第一个函数分析的，如果只传入了一个值，那么他就会直接返回base64解码的内容，并且在第一个方法中，如果传入了两个值会做重复运算，运算的函数和第二部分的变量是基本匹配的，我们现把能拿到的数据转换一下，如下

```
● ● ●

    $���� = ��("c3RycmV2�"); // strrev
    $���������� = ��("c3RydHI=�"); // strtr
    $�� = ��("G3p1bwNvbXByGX�Nz�", "ZwCmG");
    $��� = ��("SzYzOWIzMmY0MaMwED�FjYjY2MDU0YzlhYTUy�NDNhODgwS�2U=�", "LaZEGS");
    $�������� = ��("NXNhbA==�", "ZWHON");
    $��������� = ��("UmFzZTU0�X2RlU29k�ZC==�", "YCvGgJQU");
    $��������������� = ��("IHJlZ19yZXBsYVNl�", "ctWOLdVhI");
```

后续替换到第一个方法中，可以发现方法1就还原了

```
● ● ●

    function ��($��, $��� = "")
    {
        if (empty($���)) {
            returnbase64_decode($��);
        } else {
            return ��(strtr($��, $���, strrev($���)));
        }
    }
    // 美化后
    functionfunc0($var1, $var2 = "")
    {
        if (empty($var2)) {
            returnbase64_decode($var1);
        } else {
            returnfunc0(strtr($var1, $var2, strrev($var2)));
        }
    }
```

后续通过下面脚本复原其他第二部分内容

```
● ● ●

<?php
functionfunc0($var1, $var2 = "")
{
    if (empty($var2)) {
        returnbase64_decode($var1);
    } else {
        returnfunc0(strtr($var1, $var2, strrev($var2)));
    }
}
$���� = func0("c3RycmV2�");
$���������� = func0("c3RydHI=�");
$�� = func0("G3p1bwNvbXByGX�Nz�", "ZwCmG");
$��� = func0("SzYzOWIzMmY0MaMwED�FjYjY2MDU0YzlhYTUy�NDNhODgwS�2U=�", "LaZEGS");
$�������� = func0("NXNhbA==�", "ZWHON");
$��������� = func0("UmFzZTU0�X2RlU29k�ZC==�", "YCvGgJQU");
$��������������� = func0("IHJlZ19yZXBsYVNl�", "ctWOLdVhI");

print_r(array_slice(get_defined_vars(), -7));

// 输出如下
// Array
// (
//     [锟斤拷锟斤拷] => strrev
//  ...