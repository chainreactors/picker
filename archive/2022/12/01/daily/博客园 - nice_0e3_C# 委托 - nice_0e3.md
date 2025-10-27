---
title: C# 委托 - nice_0e3
url: https://www.cnblogs.com/nice0e3/p/16940294.html
source: 博客园 - nice_0e3
date: 2022-12-01
fetch_date: 2025-10-04T00:12:17.577132
---

# C# 委托 - nice_0e3

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/nice0e3/)

# [nice\_0e3](https://www.cnblogs.com/nice0e3)

## 理想与热爱

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/nice0e3/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/nice_0e3)
* 订阅
* [管理](https://i.cnblogs.com/)

# [C# 委托](https://www.cnblogs.com/nice0e3/p/16940294.html "发布于 2022-12-01 02:15")

C# 中的委托（Delegate）类似于 C 或 C++ 中函数的指针。 委托（Delegate） 是存有对某个方法的引用的一种引用类型变量。引用可在运行时被改变。 委托就是用来储存方法的结构 委托（Delegate）特别用于实现事件和回调方法。所有的委托（Delegate）都派生自 System.Delegate 类。

###

## 委托

### 声明和定义委托分为4个步骤

1. 声明一个委托（函数指针）
2. 创建委托对象
3. 创造符合委托格式的函数（指针指向的函数）
4. 将函数名称赋值给委托

```
class Program
{
    //声明一个委托（函数指针）
    public delegate void delegateprint(string s);
    //delegate 返回值类型 委托类型名（参数列表）

    static void Main() {

        var pr =  new delegateprint(print);
        //将函数名称赋值给委托
        pr("123");//省略写法
        pr.Invoke("123");

    }

    //实例化委托方法 创造符合委托格式的函数（指针指向的函数）
    public static void print(string s)
    {
        Console.WriteLine(s);
    }

//输出结果：
123
123
```

按照我个人的理解其实这个就相当于是一个设置一个回调函数。调用的时候只需要在实例化委托方法的时候将需要委托的方法名作为参数传递给delegateprint这个委托方法就可以了

## 泛型委托

```
// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography.X509Certificates;

class Program
{
    //声明一个委托（函数指针）
    public delegate void delegateprint<T>(string s);
    //delegate 返回值类型 委托类型名（参数列表）

    static void Main() {

        var pr =  new delegateprint<string>(print);
        //将函数名称赋值给委托
        pr("123");//省略写法
        pr.Invoke("123");

    }

    //实例化委托方法 创造符合委托格式的函数（指针指向的函数）
    public static void print<T>(T s)
    {
        Console.WriteLine(s);
    }
}
```

和以上的没啥不同，只不过是定义方法多了个泛型的类型而已

## Action泛型委托

Action是.NET Framework内置的泛型委托，可以使用Action委托以参数形式传递方法，而不用显示声明自定义的委托。封装的方法必须与此委托定义的方法签名相对应。也就是说，封装的方法必须具有一个通过值传递给它的参数，并且不能有返回值。

```
// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography.X509Certificates;

class Program
{
    //声明一个委托（函数指针）
    public delegate void delegateprint<T>(string s);
    //delegate 返回值类型 委托类型名（参数列表）

    static void Main() {
        Action<string> action = new Action<string>(print);
        //action泛型委托不能有返回值，必须具有一个通过值传递给它的参数
        action.Invoke("123");

        //var pr =  new delegateprint<string>(print);
        ////将函数名称赋值给委托
        //pr("123");//省略写法
        //pr.Invoke("123");

    }

    //实例化委托方法 创造符合委托格式的函数（指针指向的函数）
    public static void print<T>(T s)
    {
        Console.WriteLine(s);
    }
}
```

## FUNC委托

对比action 委托是有返回值的

```
namespace System
{

    public delegate TResult Func<in T, out TResult>(T arg);
    public delegate TResult Func<out TResult>();
}
```

无传递参数

```
class Program
{

    static void Main() {
        //Action<string> action = new Action<string>(print);

        //action.Invoke("123");
        Func<int> func = new Func<int>(FunWithNoPara);

        int v = func.Invoke();
        Console.WriteLine(v);
    }

    static int FunWithNoPara()
    {
        return 123;
    }
}
```

有参数传递

```
// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography.X509Certificates;

class Program
{

    static void Main() {

        Func<int, int> func = new Func<int,int>(FunWithNoPara);
        int v = func.Invoke(123);
        Console.WriteLine(v);

    }

    static int FunWithNoPara(int num)
    {
        return num;
    }
}
```

区别在于Func<>里面的参数，最少需要有一个，即指定出参的类型，多个的话即`<in T, out TResult>`前面是入参类型，后面是出参类型。

## 多播委托

由于历史原因，所有的委托都是多播委托（multicast delegate），也就是会把添加到委托中的所有目标函数（target function）都视为一个整体去执行。

```
// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography.X509Certificates;

class Program
{

    public delegate void AddDelegate();

    static void Main() {

        //完整写法
        //AddDelegate addDelegate = new AddDelegate(FunWithNoPara1);

        //省略写法
        AddDelegate addDelegate = FunWithNoPara1;
        addDelegate += FunWithNoPara2;
        addDelegate += FunWithNoPara3;

        addDelegate.Invoke();

        //Action<string> action = new Action<string>(print);

        //action.Invoke("123");
        //Func<int, int> func = new Func<int,int>(FunWithNoPara);

        //int v = func.Invoke(123);
        //Console.WriteLine(v);

    }

    static void FunWithNoPara1()
    {

        Console.WriteLine("1");
    }
    static void FunWithNoPara2()
    {

        Console.WriteLine("2");
    }
    static void FunWithNoPara3()
    {

        Console.WriteLine("3");
    }
}
```

上面创建了一个委托，分别把FunWithNoPara1 FunWithNoPara2 FunWithNoPara3方法都加入到委托里面，`addDelegate.Invoke();`的时候会依次执行委托的方法。但是带返回值的多播委托值返回最后一个委托方法执行的值。

## 委托事件

1. 事件就是委托的安全版本。
2. 在定义事件累的外部是不能使用=号来操作，只能使用+=，并且在定义事件类的外部不能调用。
3. 事件就是在委托的前面增加一个event 关键字

事件在哪个类里面去做定义就需要在哪个类里面去做调用

这样会报错

![img](https://cdn.nlark.com/yuque/0/2022/png/2805280/1669828111152-93a36d53-4667-4bc5-ab2f-44c6531af131.png)

```
// See https://aka.ms/new-console-template for more information

class Program
{
    //定义委托
    delegate void Studentdelegate();

    //定义事件类
    class InvokeDefine
    {
        public event Studentdelegate StudentEvent;

        //调用事件
        public void Invoke() {
            StudentEvent?.Invoke(); //?. null空检查运算符
        }
    }
    class EventFunction
    {
        public void Student1()
        {
            Console.WriteLine("Student1");
        }
        public void Student2()
        {
            Console.WriteLine("Student2");
        }
    }

    static void Main() {

        EventFunction eventFunction = new EventFunction();
        InvokeDefine invokeDefine = new InvokeDefine();
        invokeDefine.StudentEvent += eventFunction.Student1;
        invokeDefine.StudentEvent += eventFunction.Student2;
        invokeDefine.Invoke();

        Console.ReadLine();

    }

}
```

## Lambad表达式

### 语法

```
(input-parameters) -> expression
或
(input-parameters) ->{ expression; }
```

Lambda 允许把函数作为一个方法的参数（函数作为参数传递进方法中）。

### 代码案例1:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
     delegate void Studentdelegate(string name, int age);
    internal class ClassTest
    {

        public void test() {
            string name = "giaogiao";
            int age = 18;

            //第一种方式
            Studentdelegate studentdelegate1 = new Studentdelegate(student);
            studentdelegate1.Invoke(name, age);

            //第二种方式，这样写可以访问到一些局部变量

            Studentdelegate studentdelegate2 = new Studentdelegate(delegate (string name, int age) {
                Console.WriteLine($"name:{name},age:{age}");
            });
          ...