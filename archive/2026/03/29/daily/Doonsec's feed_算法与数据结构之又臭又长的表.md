---
title: 算法与数据结构之又臭又长的表
url: https://mp.weixin.qq.com/s/-FZ4ufAq3jB1NRlzIsYQsw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:42.745444
---

# 算法与数据结构之又臭又长的表

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njicUbJnVlIwl2DfibvC5b2ibuHsbRY9mL6qBGq2lgoiayE5RBHfOPIYqQSnMScCxLL0GCXcGWZiaFMPzIO5fuvKNWDNicv1eeypoNQ2OQOXIGWdw/0?wx_fmt=jpeg)

# 算法与数据结构之又臭又长的表

原创

海鸥
海鸥

书中自有代码来

![]()

在小说阅读器中沉浸阅读

# 线性表

类似的列表称为有限列表，其中：

**是的直接前驱，但没有，是的直接后继，但没有，长度为，长度为0时称为空表。**

# 两种存储方式

## 顺序表

逻辑、物理位置均相邻的，称为顺序表。

**示例**：python的list、tuple，其他语言的数组

## 链表

### 类别

#### 1.单链表

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIyLibeufpalSBRS80GXxmJRuEBbqAaoZibpHAvbtOMnaltDeFXMO6ib3Wy3YnvKuZhiaCvsechXdSrAypgDBdKLtgvUCuc3Ycr9xA4/640?wx_fmt=png&from=appmsg)

示例代码分析：

1. python版：

```
###############################  定义单链表的结点    ###############################
classNode(object):                  # 定义节点类
    def__init__(self, elem):        # 定义构造函数，传入相应参数，初始化链表
        self.elem = elem             # 给数据域赋值，即将elem赋值给self.elem
        self.next = None             # 初始设置下一节点为空
###############################  定义单链表相关函数  ###############################
classSingleLinkList(object):        # 创建单链表
    def__init__(self, node=None):   # 使用一个默认参数，传入头结点接收；没有传入时，默认头结点为空
        self.__head = node           # 将传入的node值赋值给self.__head,即链表的头部
    defis_empty(self):              # 编写相关函数便于判断链表是否为空
        returnself.__head == None   # 返回self.__head是否为None的布尔值，如果为True,则为空链表
    deflength(self):                # 编写相关函数计算链表长度
        cur = self.__head            # 初始化cur游标，用来移动遍历节点，起始位置位于self.__head
        count = 0                    # 初始化用于记录变量的count的值
        while cur != None:           # 当cur获取的值不为None时，即后续还有结点，进入计数循环
            count += 1               # 记录不为空的结点数，总记录+1
            cur = cur.next           # 移动游标，指向下一个结点的位置
        return count                 # 循环完成，即cur为None，后续无结点时，返回count的值
    deftravel(self):                # 定义函数遍历整个列表，输出元素内容
        cur = self.__head            # 初始化cur游标，用来移动遍历节点，起始位置位于self.__head
        while cur != None:           # 当cur获取的值不为None时，即后续还有结点，进入遍历循环
            print(cur.elem, end=' ') # 打印结点的数据域的内容，结尾设置为空格便于输出大量内容
            cur = cur.next           # 移动游标，指向下一个结点的位置
        print("\n")                  # 遍历完成，输出换行符，便于后续输出
    defadd(self, item):             # 定义链表头部添加元的相关函数
        node = Node(item)            # 使用Node类初始化node结点，传入参数item
        node.next = self.__head      # 将该结点的尾部指针域指向原链表的头部，即将node.next赋值为self.__head
        self.__head = node           # 将新链表的头部指向该元素，即self.__head指向node结点
    defappend(self, item):          # 定义向链表尾部添加元素
        node = Node(item)            # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        ifself.is_empty():          # 使用之前判断空链表的的函数进行判断是否为空链表
            self.__head = node       # 如果是，则将该结点设置为首结点
        else:                        # 否则
            cur = self.__head        # 移动游标，遍历链表
            while cur.next != None:  # 遍历链表，直到结尾
                cur = cur.next       # 移动游标到下一个结点
            cur.next = node          # 将原链表尾部结点的指针域指向新的结点
    definsert(self, pos, item):     # 编写函数实现在指定位置添加元素
        if pos <= 0:                 # 如果pos位置在0，当做头插法
            self.add(item)           # 使用之前编写的头插法函数
        elif pos > self.length() - 1:# 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)        # 使用之前编写的尾插法函数
        else:                        # 如果都不是
            per = self.__head        # 将插入点移动到链表头部
            count = 0                # 初始化计数变量，记录游标走过的数量
            while count < pos - 1:   # 如果计数结果小于插入点，则继续移动游标
                count += 1           # 计数器自增
                per = per.next       # 移动游标到下一个位置，即当循环退出后，pre指向pos-1位置
            node = Node(item)        # 初始化结点
            node.next = per.next     # 将目标插入点的后面一个元素的位置保存到新节点的指针域，即新节点的下一个结点是插入点的下一个元素
            per.next = node          # 插入结点的数据域，让前一个结点指向新节点
    defremove(self, item):          # 编写函数实现删除节点的功能
        cur = self.__head            # 将游标移动到开头
        pre = None                   # 定义删除点变量，初始化为None
        while cur != None:           # 遍历链表
            if cur.elem == item:     # 如果数据匹配，找到该结点
                if cur == self.__head:# 如果游标在头节点
                    self.__head = cur.next# 更改头节点的指向，指向原链表头节点的下一个结点
                else:                # 否则，继续遍历
                    pre.next = cur.next#修改前一个结点的指针域指向，跳过要删除的结点，达到删除的效果
                break                # 完成操作后，跳出循环
            else:                    # 如果没找到，继续遍历，直到找到
                pre = cur            # 移动待删除的结点的标记
                cur = cur.next       # 移动游标到下一个结点
    defsearch(self, item):          # 编写函数实现查找节点是否存的功能
        cur = self.__head            # 移动游标到链表的开头
        whilenot cur:               # 当游标没有在末尾时，继续遍历
            if cur.elem == item:     # 如果成功查找到结点
                returnTrue          # 返回布尔值True，代表找到
            else:                    # 否则
                cur = cur.next       # 移动游标到下一个元素，继续查找
        returnFalse                 # 如果遍历整个链表都没找到，返回布尔值False，代表未找到该元素
###############################  运行代码  ###############################
if __name__ == "__main__":           # 程序入口，开始执行代码
    ll = SingleLinkList()            # 实例化类，初始化链表ll
    print(ll.is_empty())             # 判断是否为空列表
    print(ll.length())               # 获取链表长度
    ll.append(3)                     # 向链表尾部添加结点，值为3
    ll.add(999)                      # 向链表头部添加结点，值为999
    ll.insert(-3, 110)               # 向链表添加一个结点，位置是-3，即倒数第三个前面，值为110
    ll.insert(99, 111)               # 向链表添加一个结点，位置是99，但没有99个结点，则添加到链表末尾，值为111
    print(ll.is_empty())             # 再次判断链表是否为空链表
    print(ll.length())               # 再次获取链表长度
    ll.travel()                      # 遍历并打印当前链表的所有结点的值
    ll.remove(111)                   # 移除值为111的结点
    ll.travel()                      # 再次遍历，查看删除是否成功
```

2. c语言版：

```
#include <stdio.h>
#include <stdlib.h>
/*========定义链表结点结构========*/
typedefstruct node {
    /*定义数据域，这里采用整型变量演示*/
    int item;
    /*定义指针域，链表一般指向下一个节点的位置*/
    struct node * next;
} Node;

/*========初始化链表函数========*/
Node * initLinkList(int totalNode)
{
    /*定义头指针，当前还没有结点，暂时为NULL*/
    Node * head = NULL;
    /*定义头节点，使用malloc开辟合适的空间*/
    Node * headNode = (Node *)malloc(sizeof(Node));
    /*为头节点的数据域填充数据*/
    headNode->item = 0;
    /*将头节点的指针域指向下一个结点，当前没有，暂时为NULL*/
    headNode->next = NULL;
    /*将头指针指向头结点*/
    head = headNode;
    /*定义一个临时变量作为游标，初始化指向头节点*/
    Node * cur = headNode;
    /*根据传入的结点数初始化链表的每个结点*/
    for (int i = 1; i < totalNode; i++) {
        /*根据结点所占的大小分配空间*/
        Node * eachNode = (Node *)malloc(sizeof(Node));
        /*为了简便，我们直接使用循环变量赋值，当然也可以用其他的*/
        eachNode->item = i;
        /*每个结点在当次循环中均是最后一个，所以next指向NULL*/
        eachNode->next = NULL;
        /*将当前结点的位置赋值给上一个结点的指针域*/
        cur->next = eachNode;
        /*修改游标，指向当前结点*/
        cur = cur->next;
    }
    /*返回头节点的位置的指针*/
    return head;
}
intinsectItem(Node * head, int item, int position)
{
    /*定义一个插入结点，初始化指向空*/
    Node * insectNode = NULL;
    /*定义游标，初始化指向传入链表的头节点*/
    Node * cur = head;
    /*遍历链表，找到插入的位置所在的结点*/
    for (int i = 1; i < position; i++) {
        /*移动游标，指向下一个结点*/
        cur = cur -> next;
        /*判断游标在给定位置范围内是否到头*/
        if (NULL == cur) {
            /*输出报错信息，跳出函数*/
            printf_s("结点不存在！插入失败！\n");
            return-1;
        }
    }
    /*为插入的值建立结点，分配空间*/
    insectNode = (Node *)malloc(sizeof(Node));
    /*将传入的item的值赋值到新结点的数据域中*/
    insectNode->item = item;
    /*将插入的结点和后继结点连接上*/
    insectNode->next = cur->next;
    /*断开原链表前结点的连接，将前趋结点的下一个结点指向新节点*/
    cur->next = insectNode;
    return1;
}
intdeleteItem(Node * head, int item)
{
    /*定义删除位置变量，游标变量指向链表头结点*/
    Node * position,*cur = head;
    /*定义变量记录是否查找到对应结点*/
    int findOut = 0;
    /*遍历链表查找结点，直到结尾*/
    while (cur ->next) {
        /*判断游标的下一个结点的数据域是否是要查找的内容*/
        if (item == cur->next->item) {
            /*修改变量，标记为查找到对应结点，并跳出循环*/
            findOut = 1;
            break;
        }
        /*否则，指向下一个结点，继续遍历*/
        cur = cur ->next;
    }
    /*如果未找到目标结点*/
    if (0 == findOut) {
        /*输出报错信息并跳出函数*/
        printf_s("结点不存在！删除失败！\n");
        return-1;
    } else {
        /*找到对应结点，将删除位置指向该节点*/
        position = cur->next;
        /*将待删除结点的上一个结点的指针域指向待删除结点的下一个结点，断开待删除结点的两头连接*/
...