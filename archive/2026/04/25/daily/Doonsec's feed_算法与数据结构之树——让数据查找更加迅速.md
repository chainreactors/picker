---
title: 算法与数据结构之树——让数据查找更加迅速
url: https://mp.weixin.qq.com/s/lCo_NJrQL0Kmos3Ox0Uygg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:11.880899
---

# 算法与数据结构之树——让数据查找更加迅速

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIznicFricEnUiacf5oPTUOuUkoNVX8YueoEv6V3DMqCpAbUWwchdQIJUO4Xu9tMWNnXic47nyXzNhxXqZPpt2c6dc0w0A4EobSPJ60/0?wx_fmt=jpeg)

# 算法与数据结构之树——让数据查找更加迅速

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、什么是树

树是一种**非线性**的数据结构，它模拟了自然界中树的分支层次，与数组、链表这种一个接一个的线性结构不同，树中的数据元素（称为**节点**）之间存在明确的一对多的层次关系。

树的结构如下：

以图片的结构为例，其中节点1就是整个树的根（Root），而1-3、1-2则代表了树中带有方向的边（Edge），它们将各个节点连接起来，构成了树的基本骨架。在树的层次关系中，还包含多种特定的节点角色。例如，4、8、9、6、10、11这些没有子节点的末端节点，被称为叶子结点（Leaf）；节点5作为8和9的上一层节点，是它们的父亲（Parent）；而8和9因为拥有同一个父节点，所以它们互为兄弟结点（Sibling）。这些术语共同构成了描述树形结构的基础语言。

## 常见应用

### 目录树

目录树（如操作系统中的文件系统）是树形结构最直观的应用。它将文件夹作为内部节点，文件作为叶子节点，清晰地展现了数据之间的包含与层级关系。通过树形遍历（如深度优先搜索），系统可以快速定位文件路径、计算文件夹大小或进行批量文件操作。

# 二、二叉树

## 表达式树

表达式树是一种特殊的二叉树，专门用于表示和计算算术表达式。它的叶子节点是操作数（如数字），而非叶子节点（内部节点）则是运算符（如 +、-、\*、/）。表达式树能完美解决运算符优先级和括号嵌套的问题，通常通过“后序遍历”（左子树 -> 右子树 -> 根节点）来递归求值。

示例代码：

python：

```
class Node():
    def__init__(self,value,lchild=None,rchild=None,):
        self.value=value
        self.lchild=lchild
        self.rchild=rchild
    def__repr__(self):
        returnstr(self.value)
classTree():
    def__init__(self,root=None):
        self.root=root
        self.node_list=[]

    defadd_node(self,node):
        self.node_list.append(node)
        temp_list=[]
        temp_list.append(self.root)

        ifself.root == None:
            self.root=node

        else:
            while temp_list:
                cur_node=temp_list.pop(0)
                ifnot cur_node.lchild:
                    cur_node.lchild=node

                    return
                elifnot cur_node.rchild:
                    cur_node.rchild=node
                    return

                else:
                    temp_list.append(cur_node.lchild)
                    temp_list.append(cur_node.rchild)
     #二叉树的最大深度
    deffind_max_deep(self,root):
        if (not root.lchild) and (not root.rchild):
            return1
        if root.lchild:
            lenght1=self.find_max_deep(root.lchild)
        else:
            lenght1=0
        if root.rchild:
            lenght2 =self.find_max_deep(root.rchild)
        else:
            lenght2=0
        return1+max(lenght1,lenght2)
if __name__ == '__main__':
    tree=Tree()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    node5=Node(5)

    tree.add_node(node1)
    tree.add_node(node2)
    tree.add_node(node3)
    tree.add_node(node4)
    tree.add_node(node5)
    max_deep=tree.find_max_deep(tree.root)
print('max_deep:',max_deep)
```

c语言：

```
#include <stdio.h>
#include <stdlib.h>

// 表达式树节点定义
typedefstruct TreeNode {
    double value;       // 存储操作数
    char op;            // 存储运算符
    int is_operand;     // 标记是否为操作数 (1是操作数, 0是运算符)
    struct TreeNode *left, *right;
} TreeNode;

// 后序遍历求值
doubleevaluate(TreeNode* node) {
    if (node == NULL) return0;
    // 如果是叶子节点（操作数），直接返回值
    if (node->is_operand) return node->value;

    // 递归计算左右子树
    double left_val = evaluate(node->left);
    double right_val = evaluate(node->right);

    // 根据当前节点的运算符进行计算
    switch (node->op) {
        case'+': return left_val + right_val;
        case'-': return left_val - right_val;
        case'*': return left_val * right_val;
        case'/': return left_val / right_val;
        default: return0;
    }
}
```

# 三、二叉查找树

要点：左边子节点小于父节点，右边子节点大于父节点。二叉查找树（BST）的核心价值在于将数据的查找效率从线性时间 O(n) 降低到对数时间 O(log n)。

## 惰性删除

在BST中，直接删除一个带有两个子节点的节点非常复杂。惰性删除是一种巧妙的优化策略：当需要删除某个节点时，并不真正将其从树中移除，而只是在该节点上打一个“已删除”的标记。这样做的好处是删除操作极快，且不会破坏树的结构；缺点是树中会保留无效节点，需要定期清理。

```
#include <stdio.h>
#include <stdlib.h>

typedefint ELEMTYPE;
// BST节点定义
typedefstruct BSTNode {
    ELEMTYPE val;
    int is_deleted; // 惰性删除标记：1表示已删除，0表示有效
    struct BSTNode* leftchild;
    struct BSTNode* rightchild;
} BSTNode;

// 查找操作（需考虑惰性删除标记）
BSTNode* search_bst(BSTNode* root, ELEMTYPE val) {
    if (root == NULL) returnNULL;
    if (val == root->val) {
        // 如果找到了值，但被标记为删除，则视为未找到
        return root->is_deleted ? NULL : root;
    }
    if (val < root->val) return search_bst(root->leftchild, val);
    elsereturn search_bst(root->rightchild, val);
}

// 惰性删除函数
voidlazy_delete(BSTNode* root, ELEMTYPE val) {
    BSTNode* node = search_bst(root, val); // 这里需调用真实的底层查找（不带标记判断的）
    // 假设底层查找返回了节点指针 temp_node
    // if (temp_node != NULL) temp_node->is_deleted = 1;
}
```

# 四、AVL树

AVL树是一种带有严格平衡条件的二叉查找树。它要求任意节点的左右子树高度差的绝对值（即平衡因子=右高度-左高度）不超过 1。通过维护这种平衡，AVL树保证了查找、插入和删除操作在最坏情况下的时间复杂度依然为 O(log n)。

## 方法

当插入或删除节点导致平衡因子绝对值大于 1 时，AVL树会通过“旋转”操作来恢复平衡。

* 左旋转：当右子树过高（平衡因子 < -1）且新节点插入在右子树的右侧时触发（RR型）。
* 右旋转：当左子树过高（平衡因子 > 1）且新节点插入在左子树的左侧时触发（LL型）。
* 此外还有处理交叉情况的左右双旋和右左双旋。

```
#include <stdlib.h>

typedefstruct AVLNode {
    int data;
    int height; // 记录节点高度
    struct AVLNode *left;
    struct AVLNode *right;
} AVLNode;

// 获取节点高度
intgetHeight(AVLNode* node) {
    return node == NULL ? -1 : node->height;
}

// 右旋转（处理LL型不平衡）
AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;
    // 执行旋转
    x->right = y;
    y->left = T2;
    // 更新高度
    y->height = (getHeight(y->left) > getHeight(y->right) ? getHeight(y->left) : getHeight(y->right)) + 1;
    x->height = (getHeight(x->left) > getHeight(x->right) ? getHeight(x->left) : getHeight(x->right)) + 1;
    return x; // 返回新的根节点
}

// 左旋转（处理RR型不平衡）
AVLNode* leftRotate(AVLNode* y) {
    AVLNode* x = y->right;
    AVLNode* T2 = x->left;
    // 执行旋转
    x->left = y;
    y->right = T2;
    // 更新高度
    y->height = (getHeight(y->left) > getHeight(y->right) ? getHeight(y->left) : getHeight(y->right)) + 1;
    x->height = (getHeight(x->left) > getHeight(x->right) ? getHeight(x->left) : getHeight(x->right)) + 1;
    return x;
}
```

# 五、伸展树

伸展树是一种自调整的二叉查找树。它的核心思想是“局部性原理”：最近被访问过的节点，极有可能在不久的将来再次被访问。因此，每当一个节点被查找、插入或删除时，伸展树都会通过一系列特定的旋转（统称为“伸展操作”）将该节点移动到树的根部。这样做虽然单次操作可能较慢，但能保证连续 M 次操作的总时间复杂度为 O(M log N)。

```
#include <stdlib.h>

typedefstruct SplayNode {
    int key;
    struct SplayNode *left;
    struct SplayNode *right;
} SplayNode;

// 右旋转
SplayNode* rotateRight(SplayNode* x) {
    SplayNode* y = x->left;
    x->left = y->right;
    y->right = x;
    return y;
}

// 左旋转
SplayNode* rotateLeft(SplayNode* x) {
    SplayNode* y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

// 伸展操作：将包含 key 的节点伸展到根部
SplayNode* splay(SplayNode* root, int key) {
    if (root == NULL || root->key == key) return root;

    // 如果 key 在左子树
    if (key < root->key) {
        if (root->left == NULL) return root;
        // Zig-Zig (LL) 或 Zig-Zag (LR) 情况，这里以简单的单旋转为例
        if (key < root->left->key) {
            root->left->left = splay(root->left->left, key);
            root = rotateRight(root);
        } elseif (key > root->left->key) {
            root->left->right = splay(root->left->right, key);
            if (root->left->right != NULL) root->left = rotateLeft(root->left);
        }
        return (root->left == NULL) ? root : rotateRight(root);
    }
    // 如果 key 在右子树 (逻辑对称)
    else {
        if (root->right == NULL) return root;
        if (key > root->right->key) {
            root->right->right = splay(root->right->right, key);
            root = rotateLeft(root);
        } elseif (key < root->right->key) {
            root->right->left = splay(root->right->left, key);
            if (root->right->left != NULL) root->right = rotateRight(root->right);
        }
        return (root->right == NULL) ? root : rotateLeft(root);
    }
}
```

# 六、B树

B树是一种多路自平衡搜索树，专为磁盘等直接存取的外存设备设计。与二叉树不同，B树的每个节点可以拥有成百上千个子节点（阶数 M 很大），这使得整棵树非常“矮胖”。这种结构极大地减少了查找数据时所需的磁盘 I/O 次数，因此被广泛应用于数据库索引和文件系统。

## 分裂

B树的每个节点都有容量限制（最多包含 M-1 个关键字）。当向一个已经满的节点插入新关键字时，该节点会发生“分裂”：

1. 将满节点中间的关键字（中位数）提升到父节点中。
2. 将满节点以该中位数为界，拆分成两个新的子节点。
3. 如果父节点也因此变满，则递归向上分裂，甚至可能导致树的高度增加。

```
#include <stdio.h>
#define M 3 // B树的阶数（示例为3阶，即2-3树）
#define MAX_KEYS (M - 1)

typedefstruct BTreeNode {
    int keys[MAX_KEYS];
    struct BTreeNode* children[M];
    int num_keys;     // 当前节点的关键字数量
    int is_leaf;      // 是否为叶子节点
} BTreeNode;

// B树节点分裂函数
// parent: 父...