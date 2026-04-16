---
title: 算法与数据结构之栈、队列
url: https://mp.weixin.qq.com/s/ToG1pG-ZRAAMYs1ZjMlsEw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:50:46.443837
---

# 算法与数据结构之栈、队列

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIzicOz95oDicvYlPo0xGGRl8k2qKauvTq0mZb3cxqbLmUvUY3lQSOhoLx607GiaBib8XPB692WALaHCdVThrAQNqYMch2PRHkpXcRo/0?wx_fmt=jpeg)

# 算法与数据结构之栈、队列

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、栈

## （一）什么是栈

栈是一种特殊的线性表，它只能先进后出，即LIFO，即栈只有一个出入口，先进入的元素被压在底部，而新进入的元素在顶部，最先弹出，在汇编语言中，使用push入栈，使用pop出栈。栈分为顺序栈和链栈两种，下面以顺序栈为例说明。

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIw4xx6qctqv8JE4oD8dGafLYfgjPn2Y8Ide9uSlejRdXcL40uKeoiczM0xV2O7hiaiavvNbYFKaWSzJo9Dfb46PjeeHlIZQQXVtok/640?wx_fmt=png&from=appmsg)

> 上溢：栈满时再做进栈运算（一种出错状态，应设法避免）。
>
> 下溢：栈空时再做退栈运算将产生溢出。

c语言实现：

```
#include <stdio.h>
#include <malloc.h>
/* 栈的定义:首先，我们需要定义一个栈的结构体。栈包含三个部分：数据数组 data、栈顶指针 top 和栈底指针 bottom。*/
typedef struct {
    char data[100];
    int top;
    int bottom;
} stack;
/*创建栈：接下来，我们需要为栈分配内存空间，并初始化栈顶和栈底指针。*/
stack *StackInit()
{
    stack *p = (stack*)malloc(sizeof(stack)); // 分配新空间
    if (p == NULL) // 分配失败
        return 0;
    p->bottom = p->top = 0; // 分配成功
    return p;
}
/*入栈操作：入栈操作是将元素添加到栈顶。*/
void Push(stack *p, char item)
{
    p->data[p->top] = item; // 存入栈中
    p->top++; // 栈顶指针加1
}
/*出栈操作：出栈操作是从栈顶移除元素。*/
char Pop(stack *p, char item)
{
    if (p->top != p->bottom) { // 栈非空
        item = p->data[p->top - 1]; // 栈顶内容输出
        p->top--; // 栈顶减1
        return item;
    }
}
/*遍历栈：遍历栈是输出栈内所有元素。*/
void Seek(stack *p)
{
    while (p->top != p->bottom) {
        printf("%c", p->data[p->top - 1]);
        p->top--;
    }
}
int main()
{
    char str;
    stack *p; // 定义栈名
    p = StackInit(); // 创建栈
    Push(p, 'b'); // 将字符压入栈中
    str = Pop(p, str); // 取出栈顶内容
    printf("%c\n", str); // 输出栈顶内容
    return 0;
}
```

python实现：

```
class Stack(object):
    def __init__(self):          #初始化
        self.items=[]
    def is_empty(self):       #判断栈是否为空
        return self.items==[]
    def push(self,item):             # 加入元素
        self.items.append(item)
    def pop(self):                #弹出元素
        return self.items.pop()
    def peek(self):             # 返回栈顶元素
        return self.items[len(self.items)-1]
    def size(self):                #返回栈的大小
        return len(self.items)
if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    print(stack.size())
    stack.push(1)
    print(stack.peek())
    stack.push(2)
    print(stack.peek())
    stack.push(3)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.is_empty())
    print(stack.size())
```

## （二）常见用途

1. 中缀表达式转后缀表达式

**原理解析**：
这个转换过程通常被称为“调度场算法”，其核心在于利用栈来暂存运算符并处理优先级。当我们从左到右扫描中缀表达式时，遇到数字直接输出；遇到运算符时，需要将其与栈顶运算符比较优先级：如果当前运算符优先级**小于或等于**栈顶运算符，就将栈顶运算符弹出并输出，直到当前运算符优先级高于栈顶或栈为空，再将当前运算符压入栈中。括号的处理比较特殊：左括号直接入栈作为边界，遇到右括号则不断弹出栈顶元素直到遇到左括号为止，从而保证括号内的运算优先被输出。

**Python 代码实现**：

```
def infix_to_postfix(expression):
    # 定义运算符优先级
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in expression:
        # 如果是操作数（字母或数字），直接加入输出
        if char.isalnum():
            output.append(char)
        # 如果是左括号，压入栈
        elif char == '(':
            stack.append(char)
        # 如果是右括号，弹出直到遇到左括号
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() # 弹出左括号，但不输出
        # 如果是运算符
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)

    # 将栈中剩余的运算符全部弹出
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# 测试
expr = "(A+B)*C"
print(f"中缀: {expr} -> 后缀: {infix_to_postfix(expr)}")
# 输出: ABC*+
```

2. 符号检测（括号匹配）

**原理解析**：
这是栈最直观的“后进先出”应用场景，用于检查代码或数学表达式中的括号是否正确闭合且嵌套有序。算法逻辑非常清晰：遍历字符串，每当遇到一个“左括号”（如 `(`, `[`, `{`），就将其压入栈中，表示期待后续有一个对应的右括号；每当遇到一个“右括号”，就从栈顶弹出一个左括号进行比对，如果类型不匹配（例如栈顶是 `[` 但遇到了 `)`）或者栈已空（说明右括号多了），则判定为不合法；遍历结束后，如果栈为空，说明所有左括号都被正确匹配了。

**Python 代码实现**：

```
def is_balanced(expression):
    stack = []
    # 定义括号映射关系
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        # 如果是左括号，压入栈
        if char in mapping.values():
            stack.append(char)
        # 如果是右括号，进行检查
        elif char in mapping.keys():
            # 如果栈为空，或者弹出的栈顶元素不匹配，则返回 False
            if not stack or stack.pop() != mapping[char]:
                return False

    # 最后栈必须为空，才算完全匹配
    return len(stack) == 0

# 测试
print(is_balanced("{}"))  # True
print(is_balanced("{[(])}"))  # False
```

3. 递归算法的使用

**原理解析**：
虽然我们在写代码时看到的是函数自我调用，但在计算机底层，递归完全依赖于“系统调用栈”来实现。每当函数调用自身时，系统会将当前的局部变量、参数和返回地址压入栈中（这一过程叫“递”），随着递归深入，栈帧不断堆积；当满足终止条件时，函数开始返回，系统从栈顶逐层弹出栈帧，恢复上一层的现场继续执行（这一过程叫“归”）。如果递归层数过深超过了栈的内存限制，就会发生“栈溢出”，因此理解栈对于编写安全的递归代码至关重要。

**Python 代码实现**（以计算阶乘为例）：

```
def factorial(n):
    # 终止条件：防止无限递归（栈溢出）
    if n == 1:
        return 1
    else:
        # 递推过程：每一层调用都会压入系统栈
        # 直到 n=1 触底，然后开始回归（弹栈计算）
        return n * factorial(n - 1)

# 测试
# 调用 factorial(3) 的栈过程：
# 1. factorial(3) 压栈 -> 等待 3 * factorial(2)
# 2. factorial(2) 压栈 -> 等待 2 * factorial(1)
# 3. factorial(1) 压栈 -> 返回 1
# 4. factorial(2) 弹栈 -> 计算 2 * 1 = 2
# 5. factorial(3) 弹栈 -> 计算 3 * 2 = 6
print(factorial(5)) # 输出: 120
```

# 二、队列

队列是一种两端开口的线性表，一头出口，一头入口，遵循先入先出，即FIFO,即最先进入的元素，在低端最先离开队列，类似于买票，站在前面的人先买到票。

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIwYqnJJiaibiaCDPDmaaPibXRwVT84bvNf26iajItupk1ezSKzahojT5CH3C62nvq30ll7odvDTk3sSbqo6qvfgez3fWGHts94E0fias/640?wx_fmt=png&from=appmsg)

c语言示例：

```
#define MaxSize 50
typedef int ElemType;
typedef struct {
   ElemType data[MaxSize];
   int front;
   int rear;
} SeqQueue;
void InitQueue(SeqQueue &q) {//创建队列
   q.front = q.rear = 0;
}
bool EnQueue(SeqQueue &q, ElemType x) {//添加队列元素
   if ((q.rear + 1) % MaxSize == q.front) {
       return false; // 队列满
   }
   q.data[q.rear] = x;
   q.rear = (q.rear + 1) % MaxSize;
   return true;
}
bool DeQueue(SeqQueue &q, ElemType &x) {//删除元素
   if (q.rear == q.front) {
       return false; // 队列空
   }
   x = q.data[q.front];
   q.front = (q.front + 1) % MaxSize;
   return true;
}
bool QueueEmpty(SeqQueue &q) {//判断是否为空队列
   return q.rear == q.front;
}
```

python语言示例：

```
class Queue(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):                #判断队列是否为空
        return self.items==[]
    def enqueue(self,item):             #入队列
        self.items.insert(0,item)
    def dequeue(self):                 #出队列
        return self.items.pop()
    def size(self):                     #队列元素个数
        return len(self.items)
if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())
    print(queue.size())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
print(queue.size())
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过