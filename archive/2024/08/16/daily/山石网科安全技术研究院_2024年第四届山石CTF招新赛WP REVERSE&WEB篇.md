---
title: 2024年第四届山石CTF招新赛WP REVERSE&WEB篇
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507566&idx=1&sn=fa21509a3737e1ebe5cc5c050bb382ef&chksm=fa520bd0cd2582c6731ee64b58adb4f7d4429d01d6380fbf2aa7ba70df9aff6c351959880c25&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-08-16
fetch_date: 2025-10-06T18:04:43.073566
---

# 2024年第四届山石CTF招新赛WP REVERSE&WEB篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1lIic7jgh8b3icn46VQwFOPia2FdY3RO3WIAOzyvYaaibRiaU1WFGd80iazzQ/0?wx_fmt=jpeg)

# 2024年第四届山石CTF招新赛WP REVERSE&WEB篇

原创

NEURON

山石网科安全技术研究院

# REVERSE

## easycpp2

> flag: ayyctf{you\_get\_rand\_num}

该程序没有去除符号, 保留了调试符号, 所以直接定位到了main函数:

逻辑不复杂:

```
__int64 __fastcall main(int argc, const char **argv)
{
  std::ostream *v2; // rax
  std::string::iterator __for_end; // [rsp+20h] [rbp-80h] BYREF
  std::string::iterator __for_begin; // [rsp+28h] [rbp-78h] BYREF
  uint8_t data[24]; // [rsp+30h] [rbp-70h]
  std::string usr_input; // [rsp+50h] [rbp-50h] BYREF
  uint8_t enc_; // [rsp+7Fh] [rbp-21h]
  char *c; // [rsp+80h] [rbp-20h]
  std::string *__for_range; // [rsp+88h] [rbp-18h]
  int rotate_count; // [rsp+94h] [rbp-Ch]
  int i; // [rsp+98h] [rbp-8h]
  int correct_num; // [rsp+9Ch] [rbp-4h]

  _main();
  correct_num = 0;
  std::string::basic_string(&usr_input);
  std::operator>><char>(refptr__ZSt3cin);
  *(_QWORD *)data = 0xB3B78DA987B3B383ui64;
  *(_QWORD *)&data[8] = 0xA5BEA98B8FBEAB9Fui64;
  *(_QWORD *)&data[16] = 0xBB9BAB9DBE899D83ui64;
  rotate_count = rand() % 7 + 1;
  i = 0;
  __for_range = &usr_input;
  __for_begin._M_current = (char *)std::string::begin(&usr_input);
  __for_end._M_current = (char *)std::string::end(__for_range);
  while ( __gnu_cxx::operator!=<char *,std::string>(&__for_begin, &__for_end) )
  {
    c = __gnu_cxx::__normal_iterator<char *,std::string>::operator*(&__for_begin);
    enc_ = func1(*c, rotate_count);
    if ( enc_ == data[i] )
      ++correct_num;
    ++i;
    __gnu_cxx::__normal_iterator<char *,std::string>::operator++(&__for_begin);
  }
  if ( correct_num == 24 )
    v2 = (std::ostream *)std::operator<<<std::char_traits<char>>(refptr__ZSt4cout, "Correct!");
  else
    v2 = (std::ostream *)std::operator<<<std::char_traits<char>>(refptr__ZSt4cout, "No!");
  refptr__ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_(v2);
  std::string::~string(&usr_input);
  return 0i64;
}
```

1.首先读入用户输入:

```
std::string::basic_string(&usr_input);
std::operator>><char>(refptr__ZSt3cin);
```

其中refptr\_\_ZSt3cin可以demangle一下, 就是std::cin, 这种operator>>是运算符重写, 下面的operator\*同样也是。

2.然后获取一个rotate\_count:

```
rotate_count = rand() % 7 + 1;
```

查看导入表可以发现并没有导入srand, 所以rand的结果是固定的值, 可以自己编译一下查看rand()返回值是多少, 或者动态调试,
这里rotate\_count的结果是rotate\_count = 7

3.然后遍历用户输入:

```
i = 0;
__for_range = &usr_input;
__for_begin._M_current = (char *)std::string::begin(&usr_input);
__for_end._M_current = (char *)std::string::end(__for_range);
while ( __gnu_cxx::operator!=<char *,std::string>(&__for_begin, &__for_end) )
{
  c = __gnu_cxx::__normal_iterator<char *,std::string>::operator*(&__for_begin);
  enc_ = func1(*c, rotate_count);
  if ( enc_ == data[i] )
    ++correct_num;
  ++i;
  __gnu_cxx::__normal_iterator<char *,std::string>::operator++(&__for_begin);
}
```

std::string::begin和end获取的都是迭代器, 然后通过迭代器获取每一个字符, 然后将输入进行func1(\*c, rotate\_count)变换, 然后把enc\_与data进比较, 正确则correct\_num++;

4.查看func1函数:

```
uint8_t __cdecl func1(uint8_t value, uint8_t n)
{
  uint8_t enc_step_one; // [rsp+2Fh] [rbp-1h]

  if ( !n || n > 8u )
    return value;
  enc_step_one = func1_1(value, n);
  return func1_2(enc_step_one, n);
}
```

其中func1\_1和func1\_2是:

```
uint8_t __cdecl func1_1(uint8_t value, uint8_t shift)
{
  return ((int)value >> shift) | (value << (8 - shift));
}

uint8_t __cdecl func1_2(uint8_t byte, int n)
{
  uint8_t bytea; // [rsp+20h] [rbp+10h]

  bytea = byte;
  if ( ((byte & 1) != 0) != ((((int)byte >> (n - 1)) & 1) != 0) )
    return (1 << (n - 1)) ^ byte ^ 1;
  return bytea;
}
```

func1\_1是循环右移的逻辑, fun1\_2是将一个字节的第n位与第1位交换位置(因为二进制里只有0和1 所以交换位置其实就是取反, 也就是`^1和^(1 << (n -1))`

5.解密: 所以逻辑就是将输入的每一个字符进行循环右移rotate\_count次然后把第rotate\_count位与第1位交换, 然后与data进行比较,
解密则是先交换回去循环左移rotate\_count即可:

```
def circular_left_shift(byte, shift):
    shifted_byte = ((byte << shift) & 0xFF) | (byte >> (8 - shift))
    return shifted_byte

def swap_bits(byte, n):
    n_index = n - 1 # 将n转换为0到7范围内的索引

    # 获取第1位和第n位的值
    bit1 = byte & 1               # 第1位
    bitN = (byte >> n_index) & 1  # 第n位

    # 如果两位不同，交换它们
    if bit1 != bitN:
        # 翻转第1位
        byte ^= 1
        # 翻转第n位
        byte ^= (1 << n_index)

    return byte

flag = ""
data = [ 0x83, 0xb3, 0xb3, 0x87, 0xa9, 0x8d, 0xb7, 0xb3, 0x9f, 0xab, 0xbe, 0x8f, 0x8b, 0xa9, 0xbe, 0xa5, 0x83, 0x9d, 0x89, 0xbe, 0x9d, 0xab, 0x9b, 0xbb ]
for n in data:
  swap_data = swap_bits(n, 7)
  shift_data = circular_left_shift(swap_data, 7)
  flag += chr(shift_data)
print(flag)
# ayyctf{you_get_rand_num}
```

## finalpack

### 0x00 运行初探

> die查一下发现是upx加壳了

直接用upx脱是不行的, 那肯定是特征被修改了:

```
        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
upx: ../finalpack: CantUnpackException: l_info corrupted

Unpacked 1 file: 0 ok, 1 error.
```

### 0x01 脱壳

如果仔细看的话, 可以发现"UPX"字符串被修改了, 事实是也就仅仅修改了这一处, 将这一处修改回去即可用upx反压缩:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1hfxGicZYILmTxbRIM4ibk63qSdsdcxNrCibCVmG6icD89lF7qXNicovKVibQ/640?wx_fmt=png&from=appmsg)

或者直接手脱, 网上关于这类文章很多, 例如这篇(https://xz.aliyun.com/t/6881?time\_\_1311=n4%2BxnD0DRDyBeAK4GNnm00GODgBorD97YD), 就直接F8一路步过, 找到关键点, 直接dump即可。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1AotB9bFhYiaHDTy4qTywBlK7A0YduJPv73gZM3nHJCpJXVswVw1SkYg/640?wx_fmt=png&from=appmsg)

UPX脱壳如上所示

### 0x02 分析dumpfile

逻辑很简单:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1YvZjoySnpFBwP0ktNPRTLx15SfmxES8l0Pic4PH3wPzqebMteUs53Ig/640?wx_fmt=png&from=appmsg)

这样dump下来导入表应该是有问题, 但无伤大雅, 没必要去修复, 直接看汇编:

```
LEA        RDI =>local_68 ,[RBP  + -0x60 ]
CALL       thunk_FUN_00421290
```

thunk\_FUN\_00421290(rdi), 就是字符串, 所以这个函数肯定是strlen
然后用户输入是local\_44, 将local\_44进了FUN\_401830变化后与 "02CD290D5ACE1A83"进行比较,
FUN\_401830的逻辑:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1mg2WYuNTQBC4GPFT6bcgJ93fXXuFWfLoRUZFVWcU415aeKvoLib81Gw/640?wx_fmt=png&from=appmsg)

是将字符串循环右移
那关键在于移动了几轮, 也就是FUN\_00401830(local\_68, local\_44);其中的local\_44是多少, 动调即可发现是0xB，写python脚本即可:

```
def left_rotate_string(s, n):
    return s[n:] + s[:n]

s = "02CD290D5ACE1A83"
n = 0xB
print(left_rotate_string(s, n)) #E1A8302CD290D5AC
```

## Ultrasonic

### 1. 分析

目录下有个.exe.config:

```
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <startup>
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" />
    </startup>
</configuration>
```

明显的C#程序。

### 2. 分析

0. 运行看看, 有个SaveAs按钮:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx14dicU28cYApibgREXWkkgm20IczuVnugcrp9xjK8SUoCjLicXDqogvV9A/640?wx_fmt=png&from=appmsg)

1. 使用dnSpyEx反编译:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1opocuNan5snCY7VDCusJbwsxGDfw4K2XzZlAvXNR9WuAGIB6D5icwcA/640?wx_fmt=png&from=appmsg)

其中这个EncryptImageBytes函数是用来加密图片数据的, 其逻辑是:

① 将当前字节-1

② 224是11100000, 31是00011111, 所以b=(byte)(((b&224) >> 5)|((b&31)<<3));就是交换其三位和后五位的位置

③ 然后取反。

那么写个python脚本解密图片即可:

```
def decrypt_image_bytes(encrypted_bytes):
    decrypted_bytes = bytearray(len(encrypted_bytes))

    for i, b in enumerate(encrypted_bytes):
        b = ~b & 0xFF # 取反
        b = ((b & 0xF8) >> 3) | ((b & 0x7) << 5) # 恢复高低位的顺序
        b = (b + 1) & 0xFF # 加 1

        decrypted_bytes[i] = b

    return bytes(decrypted_bytes)

with open('enc.png', 'rb') as f:
    encrypted_data = f.read()

decrypted_data = decrypt_image_bytes(encrypted_data)
with open('dec.png', 'wb') as f:
    f.write(decrypted_data)
```

## xor

### 1. 先查看程序信息

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1wDAnjDcQDhDyroV4bShhQFBBoaqkjmUNRmq566tkDoXaSNibQiaW5aLg/640?wx_fmt=png&from=appmsg)

32位程序没加壳。

### 2. 打开main

没有去符号表:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1GfYicicHkXjJ9bNrksMuCKbv8ueVTTPybjjWVDAkYdL6epibKr6YvzzJQ/640?wx_fmt=png&from=appmsg)

其中enc是:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQcZwa5YtY0ia6v4vlWgUZx1Bv4k5rE...