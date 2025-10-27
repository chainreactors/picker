---
title: Python 实现极简小编译器编译程序1+2+3到栈式计算机
url: https://www.o2oxy.cn/4258.html
source: print("")
date: 2024-12-13
fetch_date: 2025-10-06T19:38:01.064542
---

# Python 实现极简小编译器编译程序1+2+3到栈式计算机

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# Python 实现极简小编译器编译程序1+2+3到栈式计算机

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-12 22:45
阅读次数: 889 次

最近开始学习编译原理的课程：<https://www.bilibili.com/video/BV16h411X7JY/>

### **任务一、编译1+2+3到栈式计算机**

栈式计算机有俩条指令，push n和add, push n即遇到数字n把数字n推进栈底，

add即遇到+号把栈顶和次栈顶的数字推出，计算俩者的和，计算后将和再推进去。

首先是二叉树

```
#二叉树
class Node:
    def __init__(self,value=None,left=None,rigth=None):
        self.value=value
        self.left=left
        self.rigth=rigth

    def __repr__(self) -> str:
        return f"TreeNode({self.value},{self.left},{self.rigth})"
```

我们想要的结构如下：

```
    +
   / \
  +   3
 / \
1   2
```

```
#生成一颗语法树
def get_node_root(expression):
    num = ''
    root=Node()
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if root.value==None:
                root.value=int(num)
                num=''
                parent=Node()
                parent.value="+"
                parent.left=root
                root=parent
            else:
                node =Node()
                node.value=int(num)
                num=''
                if root.left==None:
                    root.left=node
                elif root.rigth==None:
                    root.rigth=node
                    parent=Node()
                    parent.value="+"
                    parent.left=root
                    root=parent
                else:
                    parent=Node()
                    parent.value="+"
                    parent.left=root
                    parent.rigth=node
                    root=parent
    if num:
         node=Node()
         node.value=int(num)
         root.rigth=node
   #print(root)
    return root
```

这里主要是判断是否是int 类型的。然后设置左节点、和又节点、并且设置值。如果进入到else 中那么此刻就是+ 这里可能会存在一些问题。

例如1+2+3-6 这样的就会存在问题

然后就是一个遍历树的节点了。通常使用的是 树的后序遍历  postOrder

```
#1+2+3到栈式计算机

# 栈式计算机有两指令  push n 和add push n 碰到数字就进行压栈
# add 遇到+ 就把栈顶的数字推出、计算两者的和、计算后在推入栈中

#二叉树
class Node:
    def __init__(self,value=None,left=None,rigth=None):
        self.value=value
        self.left=left
        self.rigth=rigth

    def __repr__(self) -> str:
        return f"TreeNode({self.value},{self.left},{self.rigth})"

#生成一颗语法树
def get_node_root(expression):
    num = ''
    root=Node()
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if root.value==None:
                root.value=int(num)
                num=''
                parent=Node()
                parent.value="+"
                parent.left=root
                root=parent
            else:
                node =Node()
                node.value=int(num)
                num=''
                if root.left==None:
                    root.left=node
                elif root.rigth==None:
                    root.rigth=node
                    parent=Node()
                    parent.value="+"
                    parent.left=root
                    root=parent
                else:
                    parent=Node()
                    parent.value="+"
                    parent.left=root
                    parent.rigth=node
                    root=parent
    if num:
         node=Node()
         node.value=int(num)
         root.rigth=node
   #print(root)
    return root

#树的后续遍历  从左右中
def GetRoot(root):
    instructions = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        if node.rigth is not None:
            # 访问右子节点
            traverse(node.rigth)

        if isinstance(node.value, int):
            instructions.append(f'push {node.value}')
        else:
            instructions.append('add')
    traverse(root)
    return instructions

#打印语法数
def print_tree(root, level=0, prefix="", is_left=True):
    if root is not None:
        # 打印当前节点的值
        print(' ' * (level * 10) + prefix + ' ' + str(root.value))
        # 递归打印左子树
        print_tree(root.left, level + 1, prefix + "", True)
        # 递归打印右子树
        if root.rigth is not None:
            print_tree(root.rigth, level + 1, prefix + "", False)

#执行push n  和add指令
def GetReult(instructions):
    stack = []
    for instruction in instructions:
        if instruction.startswith('push'):
            stack.append(int(instruction[5:]))  # 将数字推入栈
        elif instruction == 'add':
            if len(stack) < 2:
                #如果不足两个直接返回
                return stack[0]
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)  # 执行加法并将结果推回栈

    return stack[0] if stack else None

expression = "1+2+4"
root_infos = get_node_root(expression)
print("打印树")
print_tree(root_infos)
instructions=GetRoot(root_infos)
ret=GetReult(instructions)
print("执行结果",ret)
```

此刻的指令这样的。

```
push 1
push 2
add
push 4
add
```

### 任务二：增加一个代码优化的阶段

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4258.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [泛微OA数据库配置信息泄漏 POC](https://www.o2oxy.cn/2557.html "泛微OA数据库配置信息泄漏 POC")
* [PHP扩展学习–扩展生成和编译](https://www.o2oxy.cn/3600.html "PHP扩展学习–扩展生成和编译")
* [取之不尽用之不竭的腾讯云云函数 http/https代理 Python 版本](https://www.o2oxy.cn/3471.html "取之不尽用之不竭的腾讯云云函数 http/https代理   Python 版本")
* [python 字典操作详解](https://www.o2oxy.cn/624.html "python 字典操作详解")
* [CVE-2019-2725 复现](https://www.o2oxy.cn/2283.html "CVE-2019-2725  复现")
* [CVE-2019-2725 绕过 复现](https://www.o2oxy.cn/2293.html "CVE-2019-2725 绕过 复现")
* [密码保护：D盾 bypass GET SQL POST SQL 文件上传](https://www.o2oxy.cn/2765.html "密码保护：D盾 bypass GET SQL  POST SQL  文件上传")
* [内网技巧-Linux权限维持之PAM万能密码登录](https://www.o2oxy.cn/2839.html "内网技巧-Linux权限维持之PAM万能密码登录")
* [phpcms v9 exp](https://www.o2oxy.cn/2755.html "phpcms v9 exp")
* [CVE-2024-2961 glibc API Bug 利用](https://www.o2oxy.cn/4193.html "CVE-2024-2961 glibc API Bug 利用")

标签云

[Apache2.4.50](https://www.o2oxy.cn/tag/apache2-4-50)
[Apache ShenYu](https://www.o2oxy.cn/tag/apache-shenyu)
[APISIX](https://www.o2oxy.cn/tag/apisix)
[APISIX Dashboard](https://www.o2oxy.cn/tag/apisix-dashboard)
[cc5](https://www.o2oxy.cn/tag/cc5)
[CNVD-2021-49104](https://www.o2oxy.cn/tag/cnvd-2021-49104)
[CNVD-2022-60632](https://www.o2oxy.cn/tag/cnvd-2022-60632)
[CobaltStrike](https://www.o2oxy.cn/tag/cobaltstrike)
[CobaltStrike xss](https://www.o2oxy.cn/tag/cobaltstrike-xss)
[CommonsCollections5](https://www.o2oxy.cn/tag/commonscollections5)
[Confluence CVE-2021-26084](https://www.o2oxy.cn/tag/confluence-cve-2021-26084)
[CVE-2017-18349](https://www.o2oxy.cn/tag/cve-2017-18349)
[CVE-2021-4034](https://www.o2oxy.cn/tag/cve-2021-4034)
[CVE-2021-37580](https://www.o2oxy.cn/tag/cve-2021-37580)
[CVE-2021-41277](https://www.o2oxy.cn/tag/cve-2021-41277)
[CVE-2021-41773](https://www.o2oxy.cn/tag/cve-2021-41773)
[cve-2021-42013](https://www.o2oxy.cn/tag/cve-2021-42013)
[CVE-2021-43798](https://www.o2oxy.cn/tag/cve-2021-43798)
[CVE-2021-44228](https://www.o2oxy.cn/tag/cve-2021-44228)
[CVE-2021-45232](https://www.o2oxy.cn/tag/cve-2021-45232)
[CVE-2021-45232 RCE](https://www.o2oxy.cn/tag/cve-2021-45232-rce)
[CVE-2022-22954](https://www.o2oxy.cn/tag/cve-2022-22954)
[CVE-2022-22965](https://www.o2oxy.cn/tag/cve-2022-22965)
[CVE-2022-39197](https://www.o2oxy.cn/tag/cve-2022-39197)...