---
title: 用jq解决复杂json的提取
url: https://zgao.top/%e7%94%a8jq%e8%a7%a3%e5%86%b3%e5%a4%8d%e6%9d%82%e7%9a%84json%e6%8f%90%e5%8f%96/
source: Zgao's blog
date: 2023-05-27
fetch_date: 2025-10-04T11:36:38.539655
---

# 用jq解决复杂json的提取

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 用jq解决复杂json的提取

* [首页](https://zgao.top)
* [用jq解决复杂json的提取](https://zgao.top:443/%E7%94%A8jq%E8%A7%A3%E5%86%B3%E5%A4%8D%E6%9D%82%E7%9A%84json%E6%8F%90%E5%8F%96/)

[5月 26, 2023](https://zgao.top/2023/05/)

### 用jq解决复杂json的提取

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/%E7%94%A8jq%E8%A7%A3%E5%86%B3%E5%A4%8D%E6%9D%82%E7%9A%84json%E6%8F%90%E5%8F%96/)

![](https://zgao.top/wp-content/uploads/2023/05/image-34-1024x325.png)

```
json_str = '''{
"optionsList": "[{\"mysql\":\"mysql\"},{\"neo4j\":\"neo4j\"}]"
}
'''

import json
json.loads(json_str)
# 报错json.decoder.JSONDecodeError: Expecting ',' delimiter: line 2 column 20 (char 21)
```

这是是一段从浏览器f12提取出来的json，在线json格式校验没有问题，但使用Python的json.loads()加载会报错。

同样使用jq也没有问题。

```
[root@VM-0-16-centos ~]# echo '''{
"optionsList": "[{\"mysql\":\"mysql\"},{\"neo4j\":\"neo4j\"}]"
}''' | jq
{
  "optionsList": "[{\"mysql\":\"mysql\"},{\"neo4j\":\"neo4j\"}]"
}
```

文章目录

[ ]

* [报错分析](#%E6%8A%A5%E9%94%99%E5%88%86%E6%9E%90 "报错分析")
* [解决思路](#%E8%A7%A3%E5%86%B3%E6%80%9D%E8%B7%AF "解决思路")
* [最优解？](#%E6%9C%80%E4%BC%98%E8%A7%A3%EF%BC%9F "最优解？")
  + [用jq处理复杂json提取需求](#%E7%94%A8jq%E5%A4%84%E7%90%86%E5%A4%8D%E6%9D%82json%E6%8F%90%E5%8F%96%E9%9C%80%E6%B1%82 "用jq处理复杂json提取需求")

## 报错分析

从这段json中，可以看到有使用 \ 反斜杠对双引号进行转义的，推测大概率是转义的问题。

> 给的JSON字符串中包含了另一个以字符串形式存在的JSON对象。当你尝试使用 `json.loads()` 函数处理该字符串时，Python的解析器将会被内部JSON对象中的转义引号（`\"`）所混淆，从而导致了错误。
>
> 相较之下，jq能够正确处理这个字符串，因为jq不会试图解析 `optionsList` 的值为一个内嵌的JSON对象，而只是简单地把它视为一个字符串。
>
> chatGPT分析

## 解决思路

```
import json

json_str_0 = '''{
"optionsList": [{\"mysql\":\"mysql\"},{\"neo4j\":\"neo4j\"}]
}
'''
# 去掉[]外层的引号
dict_obj_0 = json.loads(json_str_0)

json_str_1 = '''
{
"optionsList": "[{\\"mysql\\":\\"mysql\\"},{\\"neo4j\\":\\"neo4j\\"}]"
}
'''
# 对转义的反斜杠再转义
dict_obj_1 = json.loads(json_str_1)

print("dict_obj_0 ->",dict_obj_0["optionsList"][0])
print("dict_obj_1 ->",dict_obj_1["optionsList"][0])
```

这里我想到两种解决办法，都不会报错。

1. 去掉[]外层的引号
2. 对转义的反斜杠再转义

运行结果如下：

```
➜  python3 json_str.py
dict_obj_0 -> {'mysql': 'mysql'}
dict_obj_1 -> [
```

这里我们都打印第0个对象，都解决了报错。

第一种方案Python把optionsList的value解析成了列表。
第二种方案Python把optionsList的value解析成了字符串。

## 最优解？

要让Python正确处理json字符串，不管怎么样都得在原本的基础上进行修改替换。试想拿到一个很大的json文件如何正确高效得处理？反正只要能实现需求就对了，用什么方法并不重要。

### 用jq处理复杂json提取需求

还是用同事给json的做案例，部分json如下。

```
{
    "result": [{
        "status": "ON",
        "name": "acuxxxvs",
        "description": "Acxxxxx扫描",
        "displayName": "null",
        "version": "1.0.0",
        "appxxxst": [{
            "status": "ON",
            "name": "scannin_task",
            "description": "xxxx",
            "parameterVariableList": [{
                "name": "target_id",
                "array": false
            }],
            "resultxxmptType": "JS",
        },
        ......
    }]
}
```

1. 需要提取的字段如下
2. 将提取出来的字段转换为表格文件

```
result
	name
	description
	Version
	appActionList
		name
		description
```

如果用Python来处理，肯定是for循环提取提取出每个字段后进行拼接，然后写入到csv文件中。

实在过于麻烦，还要解决报错的问题。

jq一条命令就搞定了，命令如下：

```
cat file.json | jq -r '.result[] | .name + "," + .description + "," + .version + "," + (.appActionList[] | .name + "," + .description)'
```

用到了jq的管道对多个同一级的字段进行提取，然后统一用 `,` 进行分隔。

![](https://zgao.top/wp-content/uploads/2023/05/image-36-1024x454.png)

最后把上面的命令结果输出追加到csv文件就搞定了。

Post Views: 554

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### 匿名 发布于11:17 上午 - 6月 5, 2023

学到了

[回复](https://zgao.top/%E7%94%A8jq%E8%A7%A3%E5%86%B3%E5%A4%8D%E6%9D%82%E7%9A%84json%E6%8F%90%E5%8F%96/?replytocom=5375#respond)

### 发表评论 [取消回复](/%E7%94%A8jq%E8%A7%A3%E5%86%B3%E5%A4%8D%E6%9D%82%E7%9A%84json%E6%8F%90%E5%8F%96/#respond)

Δ

版权©2020 Author By : Zgao