---
title: C++中的std::map的运用-ASIS CTF Quals 2024-whattodo
url: https://forum.butian.net/share/3826
source: 奇安信攻防社区
date: 2024-10-10
fetch_date: 2025-10-06T18:45:34.418247
---

# C++中的std::map的运用-ASIS CTF Quals 2024-whattodo

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

### C++中的std::map的运用-ASIS CTF Quals 2024-whattodo

* [CTF](https://forum.butian.net/topic/52)

pwn中C++中的std::map的运用和逆向

whattodo
========
试了下fuzz，没出来
只能逆了
逆向
==
```c
unsigned \_\_int64 \_\_fastcall todo\_add(
\_\_int64 a1,
\_\_int64 a2,
\_\_int64 a3,
\_\_int64 a4,
\_\_int64 a5,
\_\_int64 a6,
int a7,
int a8,
int a9,
int a10,
int a11,
int a12,
int a13,
int a14,
int a15,
int a16,
int a17,
int a18,
int a19,
int a20,
\_\_int64 a21)
{
// [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]
\*(\_QWORD \*)&title\_string\_object.str[8] = \_\_readfsqword(0x28u);
LOBYTE(title\_string\_object.ptr) = 0;
title = &title\_string\_object;
max\_len = 0LL;
std::\_\_ostream\_insert<char,std::char\_traits<char>>(std::cout, "Title: ", 7LL);
std::operator>><char>(std::cin, &title);
find\_node\_ptr = (struct node \*)std::\_Rb\_tree<std::string,std::pair<std::string const,std::pair<char \*,int>>,std::\_Select1st<std::pair<std::string const,std::pair<char \*,int>>>,std::less<std::string>,std::allocator<std::pair<std::string const,std::pair<char \*,int>>>>::find(
(\_\_int64)&map\_stuct,
(\_\_int64)&title);
if ( find\_node\_ptr != (struct node \*)&map\_stuct.color )// std::cout << "Already exists" << std::endl;
{
std::\_\_ostream\_insert<char,std::char\_traits<char>>(std::cout, "Already exists", 14LL);
v22 = \*(\_QWORD \*)(std::cout[0] - 24LL);
v23 = \*(\_BYTE \*\*)((char \*)&std::cout[30] + v22);
if ( !v23 )
std::\_\_throw\_bad\_cast();
if ( v23[56] )
{
v24 = v23[67];
}
else
{
std::ctype<char>::\_M\_widen\_init(\*(\_QWORD \*)((char \*)&std::cout[30] + v22));
v24 = 10;
v27 = \*(\_\_int64 (\_\_fastcall \*\*)())(\*(\_QWORD \*)v23 + 48LL);
if ( v27 != std::ctype<char>::do\_widen )
v24 = ((\_\_int64 (\_\_fastcall \*)(\_BYTE \*, \_\_int64))v27)(v23, 10LL);
}
v25 = (std::ostream \*)std::ostream::put((std::ostream \*)std::cout, v24);
std::ostream::flush(v25);
goto LABEL\_6;
}
std::\_\_ostream\_insert<char,std::char\_traits<char>>(std::cout, "Length: ", 8LL);
std::istream::\_M\_extract<unsigned int>(std::cin, &len);
len\_more1 = (unsigned int)(len + 1);
todo\_node\_chunk = (void \*)operator new[](len\_more1);
if ( len\_more1 )
memset(todo\_node\_chunk, 0, len\_more1);
find\_node\_ptr\_1 = find\_node\_ptr;
len\_3 = len;
if ( !map\_stuct.parents )
goto LABEL\_34;
find\_node\_ptr\_2 = find\_node\_ptr;
root\_ = (struct node \*)map\_stuct.parents;
title\_2 = title;
max\_len\_1 = max\_len;
title\_1 = title;
current\_node = (struct node \*)map\_stuct.parents;
do
{
while ( 1 )
{
current\_node\_title\_len = current\_node->title\_str\_obj.size;
len\_1 = max\_len\_1;
if ( current\_node\_title\_len <= max\_len\_1 )
len\_1 = current\_node->title\_str\_obj.size;
if ( len\_1 )
{
cmp\_result = memcmp((const void \*)current\_node->title\_str\_obj.ptr, title\_1, len\_1);
if ( cmp\_result )
break;
}
difference = current\_node\_title\_len - max\_len\_1;
if ( difference >= 0x80000000LL )
goto LABEL\_24;
if ( difference > (\_\_int64)0xFFFFFFFF7FFFFFFFLL )
{
cmp\_result = difference;
break;
}
LABEL\_15:
current\_node = (struct node \*)current\_node->right\_son\_node;
if ( !current\_node )
goto LABEL\_25;
}
if ( cmp\_result < 0 )
goto LABEL\_15;
LABEL\_24:
find\_node\_ptr\_1 = current\_node;
current\_node = (struct node \*)current\_node->left\_son\_node;
}
while ( current\_node );
LABEL\_25:
max\_len\_2 = max\_len\_1;
find\_node\_ptr = find\_node\_ptr\_2;
root = root\_;
if ( find\_node\_ptr\_1 == (struct node \*)&map\_stuct.color )
goto LABEL\_34;
len\_4 = find\_node\_ptr\_1->title\_str\_obj.size;
len\_2 = max\_len\_2;
if ( len\_4 <= max\_len\_2 )
len\_2 = find\_node\_ptr\_1->title\_str\_obj.size;
if ( len\_2 )
{
LODWORD(v41) = memcmp(title\_2, (const void \*)find\_node\_ptr\_1->title\_str\_obj.ptr, len\_2);
if ( (\_DWORD)v41 )
{
LABEL\_32:
if ( (int)v41 < 0 )
goto LABEL\_34;
goto LABEL\_33;
}
}
v41 = max\_len\_2 - len\_4;
if ( (\_\_int64)(max\_len\_2 - len\_4) > 0x7FFFFFFF )
{
LABEL\_33:
find\_node\_ptr\_1->todo\_pair.todo\_ptr = todo\_node\_chunk;
LODWORD(find\_node\_ptr\_1->todo\_pair.todo\_len) = len\_3;
goto LABEL\_36;
}
if ( v41 >= (\_\_int64)0xFFFFFFFF80000000LL )
goto LABEL\_32;
LABEL\_34:
p\_title = &title;
new\_node = std::\_Rb\_tree<std::string,std::pair<std::string const,std::pair<char \*,int>>,std::\_Select1st<std::pair<std::string const,std::pair<char \*,int>>>,std::less<std::string>,std::allocator<std::pair<std::string const,std::pair<char \*,int>>>>::\_M\_emplace\_hint\_unique<std::piecewise\_construct\_t const&,std::tuple<std::string const&>,std::tuple<>>(
&map\_stuct,
find\_node\_ptr\_1,
(char \*\*\*)&p\_title);
root = (struct node \*)map\_stuct.parents;
new\_node->todo\_pair.todo\_ptr = todo\_node\_chunk;
LODWORD(new\_node->todo\_pair.todo\_len) = len\_3;
if ( !root )
goto insert;
max\_len\_2 = max\_len;
title\_2 = title;
LABEL\_36:
max\_len\_3 = max\_len\_2;
v44 = find\_node\_ptr;
current = root;
max\_len\_4 = max\_len\_3;
while ( 2 )
{
while ( 2 )
{
current\_len = current->title\_str\_obj.size;
len\_5 = max\_len\_4;
if ( current\_len <= max\_len\_4 )
len\_5 = current->title\_str\_obj.size;
if ( !len\_5 || (comp\_result = memcmp((const void \*)current->title\_str\_obj.ptr, title\_2, len\_5)) == 0 )
{
differ = current\_len - max\_len\_4;
if ( differ >= 0x80000000LL )
goto LABEL\_46;
if ( differ > (\_\_int64)0xFFFFFFFF7FFFFFFFLL )
{
comp\_result = differ;
break;
}
LABEL\_37:
current = (struct node \*)current->right\_son\_node;
if ( !current )
goto access;
continue;
}
break;
}
if ( comp\_result < 0 )
goto LABEL\_37;
LABEL\_46:
v44 = current;
current = (struct node \*)current->left\_son\_node;
if ( current )
continue;
break;
}
access:
v51 = max\_len\_4;
find\_node\_ptr = v44;
v52 = v51;
if ( find\_node\_ptr == (struct node \*)&map\_stuct.color )
goto insert;
size = find\_node\_ptr->title\_str\_obj.size;
v54 = v51;
if ( size <= v51 )
v54 = find\_node\_ptr->title\_str\_obj.size;
if ( v54 && (LODWORD(v55) = memcmp(title\_2, (const void \*)find\_node\_ptr->title\_str\_obj.ptr, v54), (\_DWORD)v55) )
{
LABEL\_54:
if ( (int)v55 < 0 )
goto insert;
}
else
{
v55 = v52 - size;
if ( (\_\_int64)(v52 - size) <= 0x7FFFFFFF )
{
if ( v55 >= (\_\_int64)0xFFFFFFFF80000000LL )
goto LABEL\_54;
insert:
title\_addr = &title;
find\_node\_ptr = std::\_Rb\_tree<std::string,std::pair<std::string const,std::pair<char \*,int>>,std::\_Select1st<std::pair<std::string const,std::pair<char \*,int>>>,std::less<std::string>,std::allocator<std::pair<std::string const,std::pair<char \*,int>>>>::\_M\_emplace\_hint\_unique<std::piecewise\_construct\_t const&,std::tuple<std::string const&>,std::tuple<>>(
&map\_stuct,
find\_node\_ptr,
(char \*\*\*)&title\_addr);
}
}
if ( !find\_node\_ptr->todo\_pair.todo\_ptr )
{
std::\_\_ostream\_insert<char,std::char\_traits<char>>(std::cout, "Out of memory", 13LL);
v56 = \*(\_QWORD \*)(std::cout[0] - 24LL);
v57 = \*(\_BYTE \*\*)((char \*)&std::cout[30] + v56);
if ( v57 )
{
if ( v57[56] )
{
v58 = (unsigned int)(char)v57[67];
}
else
{
std::ctype<char>::\_M\_widen\_init(\*(\_QWORD \*)((char \*)&std::cout[30] + v56));
v58 = 10LL;
v64 = \*(\_\_int64 (\_\_fastcall \*\*)())(\*(\_QWORD \*)v57 + 48LL);
if ( v64 != std::ctype<char>::do\_widen )
v58 = (unsigned int)((char (\_\_fastcall \*)(\_BYTE \*, \_\_int64))v64)(v57, 10LL);
}
v59 = (std::ostream \*)std::ostream::put((std::ostream \*)std::cout, v58);
std::ost...