---
title: 逆向中的GL与着色器逆向
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458566271&idx=1&sn=d836b7fe83c592bd66018f5f8a87394b&chksm=b18d8ef586fa07e31609d0538c01a6a8249e415c51047cca73d133664749785f7adab2217f8e&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-08
fetch_date: 2025-10-06T18:05:35.733600
---

# 逆向中的GL与着色器逆向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FzaNcgh9tia5aNbCmL6bOnkxf5s9iaicomPkzk3VrQBedY3P55YFFLPeaqnSqMjrvvQkB0FfALibGKAQ/0?wx_fmt=jpeg)

# 逆向中的GL与着色器逆向

yixinBC

看雪学苑

```
一

着色器介绍
```

着色器是一种运行在图形处理单元（GPU）上的小程序，用于对图形渲染管线的特定部分进行处理。着色器的主要作用是将输入数据（如顶点位置、颜色等）转化为输出数据（如像素颜色），从而实现对图像的渲染和处理。

## 着色器的分类

◆顶点着色器（Vertex Shader）：主要负责处理顶点的几何关系、位置变换等。在图形渲染过程中，顶点着色器首先接收输入的顶点数据，然后对这些数据进行坐标变换、光照计算等处理，最终输出处理后的顶点数据。

◆片段着色器（Fragment Shader）：主要负责处理像素或片段的颜色计算。像素着色器接收顶点着色器输出的顶点数据，然后根据这些数据计算每个像素的颜色值，最终生成渲染图像。

◆几何着色器（Geometry Shader）：它位于顶点着色器和片段着色器之间，是一个可选的着色器阶段。几何着色器的主要作用是对顶点着色器输出的顶点数据进行进一步的处理，生成新的顶点或图元，或者修改现有图元的属性。

◆计算着色器（Compute Shader）：主要用于在GPU上执行各种通用计算任务，而不仅仅是图形渲染。

◆……

## 着色器语言

◆OpenGL着色语言（GLSL）：GLSL是OpenGL（Open Graphics Library）的着色器语言，用于OpenGL图形渲染管线的顶点着色器和片段着色器。

◆DirectX高级着色器语言（HLSL）：HLSL是DirectX图形API的着色器语言，主要用于Windows平台的游戏开发和图形应用。

◆……

## 着色器的执行

从着色器代码到GPU可以理解的着色器程序，一般需要经过编译。

针对较低版本的OpenGL，这一般意味着从文件或者data段读取源代码直接编译。这给了我们修改shader以控制最终渲染表现的机会。例如笔者在VNCTF2024中的题目LearnOpenGL（https://github.com/yixinBC/VNCTF2024-LearnOpenGL），就可以通过直接修改着色器的方法得到flag。

更为细致的，这里的”编译“其实包含了编译与链接两步。

一般而言，如果最后需要着色器生成一个图像，那么顶点着色器与片段着色器是不可缺的。因为图形的渲染必然涉及到以下两步：第一步把3D坐标转换为2D坐标，第二步是把2D坐标转变为实际的有颜色的像素。

可以大致理解成顶点着色器负责第一步，片段着色器负责第二步。那么两步加在一起才是一个完整的过程。反映到代码层面，就是在编译好顶点与片段着色器后，需要把两者链接起来，变成一个program，后续调用会直接调用这个program进行渲染。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FzaNcgh9tia5aNbCmL6bOnkKxrZcibpAAVzD95mhJG6o5nrrJRIMoibaZANpbYWInmX36AVibxHjTP0g/640?wx_fmt=other&from=appmsg)

而对于OpenGL之外的其它环境，着色器代码可能会被预编译为中间表示，如Vulkan平台通常使用SPIR-V作为中间表示，而DirectX平台则使用DXBC。

```
二

DubheCTF - ezVK
```

根据题目名，以及调用的动态链接库，我们初步怀疑是Vulkan平台的shader逆向。运行程序，发现没有图形界面，那么看来它调用vulkan不是用来绘图的。直接猜测一手，核心的加密逻辑在vulkan调用的着色器里。

ida分析main\_0函数，很容易发现dword\_140021000里存的是加密后的密文。往前翻哪里读入了着色器，因为着色器读入后需要平台进行加载，所以在vkCreateShaderModule函数之前的sub\_14001135C函数中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FzaNcgh9tia5aNbCmL6bOnkVN5z4PcLiaWWPJKrjmFSWQjBickucxNpk1xq0wH8m5ibVjNdWbXMvbo9A/640?wx_fmt=other&from=appmsg)

分析代码，着色器在程序的resource里，可以使用resource hacker等工具提取出来。发现是二进制格式的，需要反编译。根据我们前置介绍里讲的，Vulkan平台通常使用SPIR-V作为中间表示，那么现在我们需要找一个SPIR-V的反编译器。经过一番搜索，发现百度只能找到spirv-dis，是反编译成字节码，逆向难度仍然较大。GitHub能找到spirv-cross，直接把我们提取出来的中间表示还原成GLSL：

```
#version 450
layout(local_size_x = 1, local_size_y = 1, local_size_z = 1) in;

const uint _80[5] = uint[](1214346853u, 558265710u, 559376756u, 1747010677u, 1651008801u);

layout(binding = 0, std430) buffer V
{
    uint v[];
} _23;

void main()
{
    uint cnt = gl_GlobalInvocationID.x * 2u;
    uint sum = 0u;
    uint l = _23.v[cnt];
    uint r = _23.v[cnt + 1u];
    for (int i = 1; i <= 40; i++)
    {
        l += ((((((~(r << uint(3))) & (r >> uint(5))) | ((r << uint(3)) & (~(r >> uint(5))))) ^ (~r)) & ((r << uint(3)) ^ (r >> uint(5)))) ^ ((~((~(sum + _80[sum & 4u])) | (~((r >> uint(3)) & (r << uint(2))))))));
        sum += 1932555628u;
        r += ((((((~(l << uint(3))) & (l >> uint(5))) | ((l << uint(3)) & (~(l >> uint(5))))) ^ (~l)) & ((l << uint(3)) ^ (l >> uint(5)))) ^ ((~((~(sum + _80[(sum >> uint(11)) & 4u])) | (~((l >> uint(3)) & (l << uint(2))))))));
    }
    _23.v[cnt] = l;
    _23.v[cnt + 1u] = r;
}
```

到了这步，xtea加密的特征就很明显了，我们写出对应的解密代码：

```
#include <stdint.h>
#include <stdio.h>

// 解密函数
void decrypt(uint32_t *v, uint32_t *k) {
  uint32_t v0 = v[0], v1 = v[1], sum = 0, i; /* set up */
  uint32_t delta = 1932555628u;              /* a key schedule constant */
  for (i = 0; i < 40; i++) {
    sum += delta;
  }
  for (i = 0; i < 40; i++) { /* basic cycle start */
    v1 -=
        ((((((~(v0 << 3u)) & (v0 >> 5u)) | ((v0 << 3u) & (~(v0 >> 5u)))) ^
           (~v0)) &
          ((v0 << 3u) ^ (v0 >> 5u))) ^
         ((~((~(sum + k[(sum >> 11u) & 4u])) | (~((v0 >> 3u) & (v0 << 2u)))))));
    sum -= delta;
    v0 -= ((((((~(v1 << 3u)) & (v1 >> 5u)) | ((v1 << 3u) & (~(v1 >> 5u)))) ^
             (~v1)) &
            ((v1 << 3u) ^ (v1 >> 5u))) ^
           ((~((~(sum + k[sum & 4u])) | (~((v1 >> 3u) & (v1 << 2u)))))));
  } /* end cycle */
  v[0] = v0;
  v[1] = v1;
}

int main() {
  uint32_t ida_chars[] = {0x185B72AF, 0X631D2C6,  0XDE8B33CC, 0X31EBCD9F,
                          0X5DB8B33,  0XA8D77D0,  0X865C6111, 0XBF032335,
                          0X722228A5, 0XAD833A57, 0XB7C3456F};
  uint32_t key[] = {1214346853u, 558265710u, 559376756u, 1747010677u,
                    1651008801u};
  decrypt(ida_chars, key);
  decrypt(ida_chars + 2, key);
  decrypt(ida_chars + 4, key);
  decrypt(ida_chars + 6, key);
  decrypt(ida_chars + 8, key);
  decrypt(ida_chars + 10, key);
  decrypt(ida_chars + 12, key);
  decrypt(ida_chars + 14, key);
  printf("%s", ida_chars);
  return 0;
}
// :8�eCTF{Go0Od!!!You_4re_Vu1k@N_Mast3r^^ݙ�
```

头尾有些问题。头可以确定是DubheCTF，根据flag规则与tea加密原理，尾部只有一位未知，即^^\*}，在本地用python的subprocess爆破一下。

```
import string
import subprocess

known_chars = "DubheCTF{Go0Od!!!You_4re_Vu1k@N_Mast3r^^"  # 已知的40位字符

for ch in string.printable:
    flag = known_chars + ch + "}"
    with subprocess.Popen(
        ["./ezVK.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    ) as p:
        stdout, _ = p.communicate(input=flag.encode())
        if "You Are GENIUS!!!" in stdout.decode():
            print("flag found:", flag)
            exit(0)
# flag found: DubheCTF{Go0Od!!!You_4re_Vu1k@N_Mast3r^^_}
```

#

```
三

hitcon - revisual
```

js先上下面这个网站去一点混淆：https://deobfuscate.relative.im/

flag解密部分的代码如下，记该函数为get\_flag：

```
function _0x52fd86(parm) {
    let salt = CryptoJS.enc.Hex.parse(
        CryptoJS.SHA256(parm).toString(CryptoJS.enc.Hex)
    ),
        iv_ = CryptoJS.enc.Hex.parse('fd3cb6c1be89457ba82919a33f02707c'),
        enc = CryptoJS.enc.Hex.parse(
            '4f6b9161b29e59e2d94fa90529d745601473cb4203c02d9549eea6e322908d71e0472241d86f3821b3c96dd82937b04dcef80b9f68b23dd2371d2a56ef873ce857563eefc6f9057aa0cc5b41ff87477256f6b56ef342da815099d1217d301d03b76e4fae675d27bf95ca43154015b964'
        ),
        flag = CryptoJS.AES.decrypt({ ciphertext: enc }, salt, {
            iv: iv_,
            padding: CryptoJS.pad.Pkcs7,
            mode: CryptoJS.mode.CBC,
            hasher: CryptoJS.algo.SHA256,
        })
    return flag.toString(CryptoJS.enc.Utf8)
}
```

现在我们要求的变成了这个函数的parm。

与检查flag相关的顶点着色器代码如下，传入vec3（三个数构成的数组），前两个被用来确定顶点的位置，第三个作为一个可以在着色器间传递的变量，进入了片段着色器：

```
attribute vec3 position;
varying   float owO;
void main(void){
    gl_Position = vec4(position.xy, 0.0, 1.0);
    owO = position.z;
}
```

片段着色器代码如下：

```
#ifdef GL_ES
precision highp float;  //设置为高精度浮点数
#endif
varying float owO;  //顶点着色器传入
#define OvO 255.0
#define Ovo 128.0
#define OVO 23.0
float OwO (float Owo, float OWO, float owO) {
    OWO = floor(OWO + 0.5);
    owO = floor(owO + 0.5);
    return mod(floor((floor(Owo) + 0.5) / exp2(OWO)), floor(1.0*exp2(owO - OWO) + 0.5));
}
vec4 oWo (float Ow0) {
    if (Ow0 == 0.0) return vec4(0.0);
    float Owo = Ow0 > 0.0 ? 0.0 : 1.0;
    Ow0 = abs(Ow0);
    float OWO = floor(log2(Ow0));
    float oWo = OWO + OvO - Ovo;
    OWO = ((Ow0 / exp2(OWO)) - 1.0) * pow(2.0, OVO);
    float owO = oWo / 2.0;
    oWo = fract(owO) + fract(owO);
    float oWO = floor(owO);
    owO = OwO(OWO, 0.0, 8.0) / OvO;
    Ow0 = OwO(OWO, 8.0, 16.0) / OvO;
    OWO = (oWo * Ovo + OwO(OWO, 16.0, OVO)) / OvO;
    Owo = (Owo * Ovo + oWO) / OvO;
    return vec4(owO, Ow0, OWO, Owo);
}
void main(){
    gl_FragColor = oWo(owO); //RGBA
}
```

稍微去一下名称混淆如下：

```
#ifdef GL_ES
precision highp float;  //设置为高精度浮点数
#endif
varying float vert_in;  //顶点着色器传入，即owO
#define val_255 255.0
#define val_128 128.0
#define val_23 23.0
float func1 (float parm1, float parm2, float vert_in) {
    parm2 = floor(parm2 + 0.5);
    vert_in = floor(vert_in + 0.5);
    return mod(floor((floor(parm1) + 0.5) / exp2(parm2)), floor(1.0*exp2(vert_in - parm2) + 0.5));
}
vec4 func2 (float parm1) {
    if (parm1 == 0.0) return vec4(0.0);
    float temp1 = parm1 > 0.0 ? 0.0 : 1.0;
    parm1 = abs(parm1);
    float temp2 = floor(log2(parm1));
    float temp3 = temp2 + val_255 - val_128;
    temp2 = ((parm1 / exp2(temp2)) - 1.0) * pow(2.0, val_23);
    float ...