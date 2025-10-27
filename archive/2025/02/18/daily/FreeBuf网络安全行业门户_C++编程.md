---
title: C++编程
url: https://www.freebuf.com/articles/web/421985.html
source: FreeBuf网络安全行业门户
date: 2025-02-18
fetch_date: 2025-10-06T20:39:23.082498
---

# C++编程

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

C++编程

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

C++编程

2025-02-17 14:44:06

所属地 陕西省

# 类和对象-静态成员

```
#include <iostream>
using namespace std;
class Person {
public:
	//静态成员函数
	static void func() {
		m_A = 100;//静态成员函数可以访问 静态成员变量
		//m_B = 200;//静态成员函数不可以访问 非静态成员变量，无法区分是哪一个对象的
		cout << "static func调用" << endl;
	}
	static int m_A;//静态
	int m_B;//非静态

	//静态成员函数也是有访问权限的
private:
	static void func2() {
		cout << "ststic void func2调用" << endl;
	}
};
int Person::m_A = 0;
void test01() {
	//通过对象访问
	Person p;
	//通过类访问
	p.func();
	Person::func();

	//Person::func2();类外访问不到私有静态成员函数
};
int main() {
	test01();
	return 0;
}
```

# 类和对象-对象特征-成员变量和成员函数分开存储

```
#include <iostream>
using namespace std;
class Person {
public:
	int m_a;//非静态成员变量，属于类的对象上
	static int m_b;//静态成员变量，不属于类的对象上
	void func(){}//非静态成员函数，不属于类的对象上
	static void func2(){}//静态成员函数，不属于类的对象上
};

void test01() {
	/*person p;
	cout << "size of p=" << sizeof(p) << endl;*/
	//c++编译器会给每个空对象分贝一个字节空间（为例区分空对象占的内存位置），每个空对象也应该有一个第一无二的内存地址
};
void test02() {
	Person p;
	cout << "size of p=" << sizeof(p) << endl;
}

int main() {
	test02();
	return 0;
}
```

# 类和对象-对象特征-this指针用途

每一个非静态成员函数只会诞生一份函数实例，也就是说多个同类型的对象会共用一块代码
那么问题是：这一块代码是如何区分那个对象调用自己的呢？

C++通过提供特殊的对象指针，this指针，解决上述问题。this指针指向被调用的成员函数所属的对象

his指针是隐含每一个非静态成员函数内的一种指针
this指针不需要定义，直接使用即可

this指针的用途：
1.当形参和成员变量同名时，可用this指针来区分
2.在类的非静态成员函数中返回对象本身，可使用return \*this

```
#include <iostream>
using namespace std;
//解决名字冲突
//返回对象本身用*this
class Person {
public:
	Person(int age) {
		this->age = age;//this指针指向 被调用函数 所属的对象
	}
	Person& Personage(Person& p) {
		this->age += p.age;
		//this指向p2的指针，而*this指向的就是p2这个对象本体
		return *this;
	}
	int age;
};

void test01() {
	Person p1(18);
	cout << "p1的年龄为：" << p1.age << endl;
}
void test02() {
	Person p1(10);
	Person p2(10);
	//p2.Personage(p1);
	p2.Personage(p1).Personage(p1).Personage(p1);//链式编程思想
	cout << "p2的年龄为：" << p2.age << endl;
}

int main() {
	//est01();
	test02();
	system("pause");
	return 0;
}
```

# 类和对象-对象特征-空指针访问成员函数

c++中空指针也是可以调用成员函数的，但也要注意有没有用到[this指针](https://so.csdn.net/so/search?q=this%E6%8C%87%E9%92%88&spm=1001.2101.3001.7020)。

如果用到this指针，需要加以判断保证代码的[健壮性](https://so.csdn.net/so/search?q=%E5%81%A5%E5%A3%AE%E6%80%A7&spm=1001.2101.3001.7020)。

```
#include <iostream>
using namespace std;
//空指针调用成员函数
class Person {
public:
	void showclassname() {
		cout << "this is person class" << endl;
	}
	void showpersonage() {
		//不加if的报错原因是因为传入的指针为NULL
		if (this == NULL) {
			return;
		}
		cout << "age=" << m_Age << endl;
	}
	int m_Age;
};

void test01() {
	Person* p = NULL;
	p->showclassname();
	p->showpersonage();
}
void test02() {

}

int main() {
	test01();
	test02();
	system("pause");
	return 0;
}
```

# 类和对象-对象特征-const修饰成员函数

**常函数:**
成员函数后加const后我们称为这个函数为常函数
常函数内不可以修改成员属性
成员属性声明时加[关键字](https://so.csdn.net/so/search?q=%E5%85%B3%E9%94%AE%E5%AD%97&spm=1001.2101.3001.7020)mutable后，在常函数中依然可以修改

**常对象:**
声明对象前加const称该对象为常对象
常对象只能调用常函数

```
#include <iostream>
using namespace std;
//常函数
class Person {
public:
	//this指针的本质 是指针常量 指针的指向是不可以被修改的

	void showPerson()const//等于const Person*const this 指针指向的值无法修改
	{
		this->m_B = 100;
		//m_A = 100;
		//this=NULL;//this指针不可以修改指针的指向
	}

	void func()
	{
	}

	int m_A;
	mutable int m_B;//特殊的变量，即使在常函数中，也可以修改这个值
};
void test01() {
	Person p;
	p.showPerson();
	cout << "m_B:" << p.m_B << endl;
}

//常对象
void test02() {
	const Person p;//在对象前加const，变为常对象
	//p.m_A = 100;无法修改
	p.m_B = 100;//m_B是特殊值，在常对象下也可以修改
	//常对象只能调用常函数
	//p.func();无法调用//常对象 不可以地哦啊哦那个普通成员函数，因为普通成员函数可以修改属性
}

int main() {
	test01();
	test02();
	system("pause");
	return 0;
}
```

# 类和对象-对象特征-深拷贝与浅拷贝

[深浅拷贝](https://so.csdn.net/so/search?q=%E6%B7%B1%E6%B5%85%E6%8B%B7%E8%B4%9D&spm=1001.2101.3001.7020)是面试经典问题，也是常见的一个坑
[浅拷贝](https://so.csdn.net/so/search?q=%E6%B5%85%E6%8B%B7%E8%B4%9D&spm=1001.2101.3001.7020)：简单的赋值拷贝操作
[深拷贝](https://so.csdn.net/so/search?q=%E6%B7%B1%E6%8B%B7%E8%B4%9D&spm=1001.2101.3001.7020)：在堆区重新申请空间，进行拷贝操作

```
#include <iostream>
using namespace std;
class person{
public:
person() {
cout << "默认构造函数" << endl;
}
person(int age,int high) {
m_age = age;
m_High = new int(high);
cout << "有参构造函数" << endl;

}
person(const person& p) {
cout << "拷贝构造函数" << endl;
m_age = p.m_age;
m_High = new int(*p.m_High);//若不申请新空间则会重复析构的delete
}
~person(){
if (m_High != NULL) {
delete m_High;
m_High = NULL;
}
cout << "析构函数调用" << endl;
}
int m_age;
int* m_High;
};
void test01() {
person p1(18,160);
cout << "p1的年龄为：" << p1.m_age << "身高为：" << *p1.m_High << endl;
person p2(p1);
cout << "p1的年龄为：" << p2.m_age << "身高为：" << *p2.m_High << endl;
}
int main() {
test01();
system("pause");
return 0;
}
```

# 类和对象-c++运算符重载

### 1.加号运算符

作用：实现两个自定义[数据类型](https://so.csdn.net/so/search?q=%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B&spm=1001.2101.3001.7020)相加的运算。

```
#include <iostream>
using namespace std;

//加号运算符重载
class Person{
public:
	//1.成员函数重载+号
	/*Person operator +(Person &p) {
		Person temp;
		temp.m_A = this->m_A + p.m_A;
		temp.m_B = this->m_B + p.m_B;
		return temp;
	}*/
	int m_A;
	int m_B;
};
 //2.全局函数重载+号
Person operator+(Person& p1, Person& p2) {
	Person temp;
	temp.m_A = p1.m_A + p2.m_A;
	temp.m_B = p1.m_B + p2.m_B;
	return temp;
}

void test01() {
	Person p1;
	p1.m_A = 10;
	p1.m_B = 10;
	Person p2;
	p2.m_A = 10;
	p2.m_B = 10;
//成员函数重载的本质调用
//Person p3=p1.operator(p2);

//全局函数重载的本质调用
//Person p3=operator(p1,p2);

	Person p3 = p1 + p2;
	cout << "p3.m_A=" << p3.m_A << endl;
	cout << "p3.m_B=" << p3.m_B << endl;
}

 int main() {
	test01();
	system("pause");
	return 0;
}
```

### 2.左移运算符重载

作用：可以输出自义定数据类型

```
#include <iostream>
using namespace std;

//左移运算符重载
class Person{
	friend ostream& operator << (ostream& cout, Person& p);
public:
	Person(int a,int b):m_A(a),m_B(b){}
private:
	//不能利用成员函数重载 左移运算符
	/*void operator<<() {
	}*/
	int m_A;
	int m_B;
};
 //利用全局函数重载左移运算符
ostream & operator << (ostream &cout,Person &p) //本质 operator<<(cout,p) 简化cout<<p
{
	cout << "m_A=" << p.m_A << "m_B=" << p.m_B ;
	return cout;
}
void test01() {
	Person p(10,10);
	cout << p <<endl;
}

 int main() {
	test01();
	system("pause");
	return 0;
}
```

### 3.递增运算符的重载

```
#include <iostream>
using namespace std;

//重载递增运算符

//自义定类型
class Myinteger {
	friend ostream& operator<<(ostream& cout, Myinteger myint);
public:
	Myinteger() {
		m_Num = 0;
	}

	//重载前置++运算符
	Myinteger& operator++()///不能去掉operator前的&
	{
		m_Num++;
		//再将自身做返回
		return *this;
	}

	//重载后置++运算符
	Myinteger operator++(int)//int代表占位参数， 可以用于区分前置和后置
	{
		//先记录当前结果
		Myinteger temp = *this;
		//后递增
		m_Num++;
		//最后将记录结果做返回
		return temp;
	}

private:
	int m_Num;
};

//重载左移运算符
ostream& operator<<(ostream& cout, Myinteger myint) {
	cout << myint.m_Num;
	return cout;
}

void test01() {
	Myinteger myint;
	cout<<++(++myint)<<endl;
	cout << myint << endl;
}
void test02() {
	Myinteger myint;
	cout << myint++ << endl;
	cout << myint << endl;
}
 int main() {
	test01();
	test02();
	system("pause");
	return 0;
}
```

### 4.赋值运算符

C++[编译器](https://so.csdn.net/so/search?q=%E7%BC%96%E8%AF%91%E5%99%A8&spm=1001.2101.3001.7020)至少给一个类添加4个函数
1.默认构造函数（无参，函数体为空)

2.默认析构函数（无参，函数体为空)

3.默认拷贝构造函数，对属性进行值拷贝

4.赋值运算符operator=，对属性进行值拷贝

如果类中有属性指向堆区，做赋值操作时也会出现深浅拷贝问题

```
#include <iostream>
#include <string>
using namespace std;

//赋值运...