---
title: MAS Crackmes
url: https://misakikata.github.io/2022/12/MAS-Crackmes/
source: Misaki's Blog
date: 2022-12-20
fetch_date: 2025-10-04T01:55:54.953807
---

# MAS Crackmes

[Misaki's Blog](/)

Toggle navigation

* [archives](/archives/)
* [about](/about/)

# MAS Crackmes

**Monday, December 19th 2022, 4:25 pm**

## UnCrackable-Level1

下载地址: <https://mas.owasp.org/crackmes/>

国际惯例，JEB打开APK，找到main。看到onCreate里有两个提示，应该是检测了ROOT和调试的环境，可以使用frida来修改返回，或者执行修改APK判断，这里直接修改判断，为了少写代码。

直接把验证部分删了：

```
.method protected onCreate(Bundle)V
          .registers 3
00000000  invoke-static       c->a()Z
00000006  move-result         v0
00000008  if-nez              v0, :24
:C
0000000C  invoke-static       c->b()Z
00000012  move-result         v0
00000014  if-nez              v0, :24
:18
00000018  invoke-static       c->c()Z
0000001E  move-result         v0
00000020  if-eqz              v0, :2E
:24
00000024  const-string        v0, "Root detected!"
00000028  invoke-direct       MainActivity->a(String)V, p0, v0
:2E
0000002E  invoke-virtual      MainActivity->getApplicationContext()Context, p0
00000034  move-result-object  v0
00000036  invoke-static       b->a(Context)Z, v0
0000003C  move-result         v0
0000003E  if-eqz              v0, :4C
:42
00000042  const-string        v0, "App is debuggable!"
00000046  invoke-direct       MainActivity->a(String)V, p0, v0
:4C
0000004C  invoke-super        Activity->onCreate(Bundle)V, p0, p1
00000052  const/high16        p1, 0x7F030000        # layout:activity_main
00000056  invoke-virtual      MainActivity->setContentView(I)V, p0, p1
0000005C  return-void
.end method
​
```

修改为

```
.method protected onCreate(Bundle)V
          .registers 3
0000004C  invoke-super        Activity->onCreate(Bundle)V, p0, p1
00000052  const/high16        p1, 0x7F030000        # layout:activity_main
00000056  invoke-virtual      MainActivity->setContentView(I)V, p0, p1
0000005C  return-void
.end method
​
```

编译，签名安装即可。

整个验证的逻辑在verify内：

```
public void verify(View arg4) {
        String v4_1;
        String v4 = ((EditText)this.findViewById(0x7F020001)).getText().toString();  // id:edit_text
        AlertDialog v0 = new AlertDialog.Builder(this).create();
        if(a.a(v4)) {
            v0.setTitle("Success!");
            v4_1 = "This is the correct secret.";
        }
        else {
            v0.setTitle("Nope...");
            v4_1 = "That\'s not it. Try again.";
        }
​
        v0.setMessage(v4_1);
        v0.setButton(-3, "OK", new DialogInterface.OnClickListener() {
            @Override  // android.content.DialogInterface$OnClickListener
            public void onClick(DialogInterface arg1, int arg2) {
                arg1.dismiss();
            }
        });
        v0.show();
    }
```

其中a函数，因此加密密钥和加密内容就已知。

```
public static boolean a(String arg5) {
        byte[] v1 = Base64.decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=", 0);
        byte[] v2 = new byte[0];
        try {
            return arg5.equals(new String(sg.vantagepoint.a.a.a(new byte[]{(byte)0x8D, 18, 0x76, (byte)0x84, -53, -61, 0x7C, 23, 97, 109, (byte)0x80, 108, -11, 4, 0x73, -52}, v1)));
        }
        catch(Exception v0) {
            Log.d("CodeCheck", "AES error:" + v0.getMessage());
            return arg5.equals(new String(v2));
        }
    }
```

然而这里Cipher.init中的是2，也就是解密，我们需要知道解密后的内容。hook

```
sg.vantagepoint.a.a.a
```

随便输入一段内容，获取到输出为

```
ZenTracer:::{"cmd":"exit","data":["1","73,32,119,97,110,116,32,116,111,32,98,101,108,105,101,118,101"]}
```

转换为字符串就是：

```
I want to believe
```

当然如果你直接分析加密代码，然后代码还原出来那就是：

```
import java.util.Base64;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
​
​
public class owasp {
    public static void main(String[] args) throws Exception {
        System.out.println(a());
    }
​
    public static String a() throws NoSuchPaddingException, NoSuchAlgorithmException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException {
        byte[] arg2 = new byte[]{(byte)0x8D, 18, 0x76, (byte)0x84, -53, -61, 0x7C, 23, 97, 109, (byte)0x80, 108, -11, 4, 0x73, -52};
        byte[] arg3 = Base64.getDecoder().decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=");
        SecretKeySpec v0 = new SecretKeySpec(arg2, "AES");
        Cipher v2 = Cipher.getInstance("AES/ECB/PKCS5Padding");
        v2.init(Cipher.DECRYPT_MODE, v0);
        return new String(v2.doFinal(arg3));
​
    }
​
}
```

## UnCrackable-Level2

看到这个大概就知道这货想干啥了

```
static {
        System.loadLibrary("foo");
    }
```

先按照流程来看一下，跟上面差不多，几个检测，不过这里先加载so的init函数。

然后加密的方法被写到了so的

```
public class CodeCheck {
    public boolean a(String arg1) {
        return this.bar(arg1.getBytes());
    }

    private native boolean bar(byte[] arg1) {
    }
}
```

然后去so中找一下这两个函数，其中init中关键函数是sub\_93C

```
.text:00000BA4                 PUSH            {R7,LR}
.text:00000BA6                 MOV             R7, SP
.text:00000BA8                 BL              sub_93C
.text:00000BAC                 LDR             R0, =(byte_400C - 0xBB4)
.text:00000BAE                 MOVS            R1, #1
.text:00000BB0                 ADD             R0, PC  ; byte_400C
.text:00000BB2                 STRB            R1, [R0]
.text:00000BB4                 POP             {R7,PC}
```

sub\_93C的伪代码是，是一个验证app调试行为的检测。

```
int sub_93C()
{
  __pid_t v0; // r4
  pthread_t newthread; // [sp+4h] [bp-1Ch] BYREF
  int stat_loc[6]; // [sp+8h] [bp-18h] BYREF

  dword_4008 = fork();
  if ( dword_4008 )
  {
    pthread_create(&newthread, 0, sub_914, 0);
  }
  else
  {
    v0 = getppid();
    if ( !ptrace(PTRACE_ATTACH, v0, 0, 0) )
    {
      waitpid(v0, stat_loc, 0);
      while ( 1 )
      {
        ptrace(PTRACE_CONT, v0, 0, 0);
        if ( !waitpid(v0, stat_loc, 0) )
          break;
        if ( (stat_loc[0] & 0x7F) != 127 )
          exit(0);
      }
    }
  }
  return _stack_chk_guard - stat_loc[1];
}
```

另一个bar函数

```
bool __fastcall Java_sg_vantagepoint_uncrackable2_CodeCheck_bar(_JNIEnv *a1, _JavaVM *a2, int a3)
{
  const char *v5; // r8
  _BOOL4 result; // r0
  char s2[24]; // [sp+4h] [bp-2Ch] BYREF

  result = 0;
  if ( byte_400C == 1 )
  {
    strcpy(s2, "Thanks for all the fish");
    v5 = a1->functions->GetByteArrayElements(a1, a3, 0);
    if ( a1->functions->GetArrayLength(a1, a3) == 23 && !strncmp(v5, s2, 0x17u) )
      result = 1;
  }
  return result;
}
```

因为我们需要把result返回1，也就是让后续的判断为真，所以需要查看内部流程。

有两个要求，其中是字节数组长度为23，跟上面的字符比较必须相等，这里有个小问题，byte\_400C是init里来加载赋值的，也就是修改代码的时候不能去掉这个函数的渲染。

```
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 4

    invoke-direct {p0}, Lsg/vantagepoint/uncrackable2/MainActivity;->init()V

    new-instance v0, Lsg/vantagepoint/uncrackable2/CodeCheck;

    invoke-direct {v0}, Lsg/vantagepoint/uncrackable2/CodeCheck;-><init>()V

    iput-object v0, p0, Lsg/vantagepoint/uncrackable2/MainActivity;->m:Lsg/vantagepoint/uncrackable2/CodeCheck;

    invoke-super {p0, p1}, Landroid/support/v7/app/c;->onCreate(Landroid/os/Bundle;)V

    const p1, 0x7f09001b

    invoke-virtual {p0, p1}, Lsg/vantagepoint/uncrackable2/MainActivity;->setContentView(I)V

    return-void
.end method
```

编译安装，输入上面的字符串即可

```
Thanks for all the fish
```

## UnCrackable-Level3

形似如上，但是多了一个文件的校验verifyLibs，这个返回不正常的时候会给tampered一个非0的值，导致后续的判断中失败。

但是这个app有一个麻烦的地方在于，他的检测跟上面的不一样，首先是Java层，删除MainActivity$2，还有MainActivity中的调用部分即可，但是安装后还是会闪退，这个现象明显不是Java层代码控制的。

从函数中可以看到一个goodbye函数，在sub\_23C4中发现有调用，但是没有明显调用存在这个函数的地方，也没有明写在JNI\_Onload中，大概在init\_array中，于是发现有函数的调用。sub\_2468中调用了sub\_23C4

```
.init_array:00005DF0 ; Segment type: Pure data
.init_array:00005DF0                 AREA .init_array, DATA
.init_array:00005DF0                 ; ORG 0x5DF0
.init_array:00005DF0                 DCD sub_2468+1
.init_array:00005DF0 ; .init_array   ends
.init_array:00005DF0
```

于是我们需要修改sub\_23C4这个函数的判断逻辑。

由于原逻辑是如下判断：

```
void __noreturn sub_23C4()
{
  FILE *v0; // r4
  char v1[536]; // [sp+0h] [bp-218h] BYREF

  while ( 1 )
  {
    v0 = ...