---
title: 2026 精武杯 手机取证部分
url: https://mp.weixin.qq.com/s/XTvlygSHUL8M-rF1HYSQEg
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:47:46.647097
---

# 2026 精武杯 手机取证部分

# 2026 精武杯 手机取证部分

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这次比赛的赛制设计实在令人叹为观止。主办方别出心裁地采用了“闯关模式”：必须提交完当前检材的题目，才能解锁下一个检材的题目，而且提交后连之前的题目都无法再查看。如此一来，团队分工直接沦为摆设，多人协作硬生生变成了排队做题。能把一场团队赛办成单人接力赛，也算是一种本事

不知道主办方究竟是想考察选手的取证能力，还是想展示自己对团队赛的独特理解

(￣▽￣")

## 简要案情

---

近期，某市反诈部门接到多名群众报案，均遭遇“投资理财”类电信网络诈骗，指向的犯罪团伙涉案资金巨大、作案链条隐蔽。办案单位迅速成立专案组开展电子数据取证工作。经初查，该犯罪团伙搭建虚假投资平台，通过社交软件诱骗受害人充值转账，团伙成员分散多地办公，使用多种 AI 工具进行违法犯罪活动，同时发现涉及其他犯罪事实。请根据获取的电子数据还原案件经过。

注：所有检材及相关数据均为虚拟构造，不负法律责任，如有侵权请及时告知，未经允许不得用于商业用途。

## 检材容器信息

---

文件名称: 2026 精武杯检材容器

文件大小: 140 GB (150,323,855,360 字节)

MD5: A2EA823942EDE333E8F8D182E49FBC49

SHA256: A3F0BDA2FA8CA97A6E656D52B1105EB52C91214FE349D2E3A338CDE5E5B45E74

容器密码：2026精武杯/中国人民警察大学@CPPU-ISA&拓界科技@飞鹰小队

## 题目

---

### 手机检材-1

手机检材-1 解压出来是个文件夹，里面有大量 app 的包

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rk0kxhksAhnuJ2XlJkezICOia2gd5l7NwAP1S6nosp8fb3kcKUibTGbDXp0BXprGcTkFOQZHvUswEoZHwGvUqUibSZ124LlBsGm6o/640?wx_fmt=webp&from=appmsg)

可以看出手机安装了 vpn 软件 `Clash for Android` 和 `v2rayNG`，应该会作为考点，还能确定是小米手机（有 `小米运动健康` 等 app）

#### 1. 分析嫌疑人在该手机登录的小米账号ID为？（答案格式：以实际为准，如1234567890）

3134129162

查看小米健康可以看到 id

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkYSTyU6ibSmZD8bjUttP0yvmHjQPbk8e0ZXFNRoBqFADGvd2MOLLf8LR8jWqibOxYoOkFhqkdxslWfKOTmcfNuVWEDfY6x82wYI/640?wx_fmt=webp&from=appmsg)

#### 2. 嫌疑人设定了一个每周六循环的闹钟，该闹钟的备注为？（答案格式：以实际为准，如打精武杯）

给老妈汇款

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rk2erpT1bRwkPZR7SlmrAeDAG2s729TZJoxLFZdiarnkpC6IAEKG8Q0OZQ8zeIW3MUwyNGjpMiao9rJ7Z4GXa0YVzK0Imic9eoPGk/640?wx_fmt=webp&from=appmsg)

#### 3. 分析嫌疑人使用的VPN软件，配置的节点服务器地址是什么？（答案格式：不含端口，如192.168.1.1）

107.175.0.221

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkINv2RicdMH9bSecSotPTvyWJibmMKJPqS7jcbTSY8T1DHfDEmcf4Q9evtPqz4mzYRibLks9qDM3apdpvTWzZfIK4OTTicmNWKp0w/640?wx_fmt=webp&from=appmsg)

根据左侧的列表可以看出手机安装了至少两个 vpn 软件：`Clash` 和 `v2rayNG`

（需要将取证工具更新到最新版，否则只有 `Clash` 没有 `v2rayNG`）

首先要确定哪个是机主常用的 vpn，先看 `Clash` 的配置文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rmyvrpvXdm7QNPvgKiaib7s7dOuC9KL2TTuQct8SwiaLIT8Fib5WQXhWxUwHOWOaugHic8aUc1ibAmjntibsicB3mC2TX95KkWePDRGuHk/640?wx_fmt=webp&from=appmsg)

配置文件的路径是 `/Clash for Android(com.github.kr328.clash).bak_2/apps/com.github.kr328.clash/f/imported/6b3f5a87-bfa8-46d8-902f-78297e606186/config.yaml`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rk1nsu4wVaY2EjPkNWDO7TaUqQkRGib1ianPJkpQA4O8hZeyVDlsQUn2X8sDgq97grdCiaNmyWhw0WIjFEfibWTnH3jXVNxGic5zH5A/640?wx_fmt=webp&from=appmsg)

配置文件中提示 `客户端版本过旧`，可以猜测机主很久没有使用了，来看 `v2rayNG`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rmlDL3TC8lIT2icg3aXemQ2L5bH8Ph2O66TSRReN3qiaJ9Ha3ccPOUh5wm6Fxf8icxQhhb3wkzyRNGhjpRTa4YQ5llpJeRMhUWcr4/640?wx_fmt=webp&from=appmsg)

可以直接在节点信息中看到服务端 IP

#### 4. 接上题，上述VPN软件在该手机的桌面位置是什么？请写出第几页第几行第几列。（答案格式：页-行-列，如1-2-3）

3-1-3

根据上题，vpn 软件是 `v2rayNG`，要确定该 app 在桌面的位置，开始想到的是找一找相册里有没有桌面截图，翻了一下没找到

最后找了系统桌面 app 的包 `com.miui.home`，其中有个数据库文件 `launcher4x6.db`，记录了各个 app 在桌面的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rkX7UibCpWcHaYc6yltQ2q7ND9Begpu6DWzrlu7EL9alicFU9q99MDkSYDItFMO22A507icq648SuSzvGJwdMm02ibYBVm3vGaNV5o/640?wx_fmt=webp&from=appmsg)

* screen：页数，在第三页
* cellX：列数，从 0 开始计数，故在第 3 列
* cellY：行数，也是从 0 开始计数，故在第 1 行

故最终答案为 3-1-3

#### 5. 嫌疑人最近一次登录Google账号的日期是什么时候？（答案格式：2026-09-09）

2026-07-07

查看手机自带浏览器的历史记录

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rlllsibwFLcnpnjKsVjriap2pWQdY4qawQYaa1P2T4poYiaowKZ4h06uYZ6Ilrrmu4ax119pwzD38Ez8LGWKckUYMX2qI5icJDJurE/640?wx_fmt=webp&from=appmsg)

可以直接看到最后一次登录 google 账号的时间

#### 6. 在嫌疑人手机相册中发现一张图片文件名异常，经分析该图片进行了数据隐写，请回答该异常图片的文件名称是什么？（答案格式：XXX.png）

密码.png

找了半天的图片没有看到可疑的

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rknPTl8TN7XOmMg73j4QwVNsmCke6x6HUxAplqXuw9Vk0wLMIbZz0EJuzzfn4DlpU8kXO2AjyIJOfYF5BeYLE7vWnIEgcNFviaY/640?wx_fmt=webp&from=appmsg)

最后发现手机给图片做了备份，即上图中的 `backup_image.zip`，直接解压

（开始用 windows 自带解压功能解压失败了，换 bandzip 才解压成功）

解压出来发现有两个目录：`DCIM` 和 `无印`

DCIM 就是 Digital Camera Images，是手机默认存放照片的地方，我们看这里

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnYTw5d89YoadTvWU4deWRDNfxQvNLibqzffKxicuCQMo2XFiaBxSQCeIRnPIuEb2ce3Gu37upeeVCibDicGzNiaLz9cIzvHPgcTonSg/640?wx_fmt=webp&from=appmsg)

显然 `密码.png` 非常可疑，一片空白还叫密码，猜测是 lsb 隐写，用 StegSolve 看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlLu8pULvFQfA3mPhictl1IPUEcPhIRIyIBE4tCfEAMticm2icol3Lkviay4PNjpAjGYWFI9AAMa9ZiaJeuiaMxt4f74Y3NsWhfonhIg/640?wx_fmt=png&from=appmsg)

隐藏了一张二维码，实锤了

#### 7. 接上题，该异常图片中隐写的内容为？（答案格式：feiying666）

qazokm123

直接扫描上题中得到的二维码

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rms38ogic0G1trVWIhTWjf8bliaIV5ssQO3tm5BpqMsHNOcXDyfUfvK2ibokVe0WiapQENGXAqQ2ynLNrpeA9NS6NQfGMxKNbFT8h4/640?wx_fmt=webp&from=appmsg)

#### 8. 在该手机屏幕第3页第1列第4行的应用是一个伪装的密拍程序，请问机主使用该软件拍了几张图片？（答案格式：9）

1

参考第 4 题，我们通过系统桌面 app 的数据库中去查找对应位置的 app 是什么

已知该 app 在手机屏幕第 3 页第 1 列第 4 行，那么对应 screen = 3，cellX = 0，cellY = 3

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlmpg4ic7aqGQIIVlZtB8TbAGdicAHdMRFRypXicTweO7KozEc9piaT1WtRDTEic1jIicfLKHR4hXaUcCMt40xQ1ibMW2KTuteAYr8sOk/640?wx_fmt=png&from=appmsg)

定位到该 app 名为计算器，显然名字是伪装的，对应的包名为 `com.androidx.calculator`

根据包名可以找到两个备份

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rnwTfXP14BibUkM4YHsYPFfzQSfzcVxibDBInHHmZxHdwFuRgV2fU940bDza4wesum8vFtV2I4xqXluNpIIyexic3fibbnK4wJiagu8/640?wx_fmt=png&from=appmsg)

.bak 的备份中是该应用的 apk `base.apk`，.bak\_38 的备份中是该应用的数据库 `stwyuo.db`

本来想直接看数据库的，结果打不开，说明可能被加密了

没办法只能逆向 `base.apk` 了

先看 `AndroidManifest.xml`

![](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rlYGOjS6RKRRJdomq6rHTGsbQwm05VyeWP7CfDZa4hVeUZibF5BDc1osW4pzMTicT8I1GERPHSHA4eZs0nHLlxads673k0BE7lpc/640?wx_fmt=webp&from=appmsg)

定位到一个关键类名 `androidx.appcompat.app.CCActivity`（查看源码发现其中有 `摄像头打开失败` 这样的字符串，猜测这个就是拍照的主要逻辑）

用 jadx 反编译

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmgr17R8fL4U30Gcz7MwLvxkHUe085k52CZM5oeWoMbeibRXbMd8aEXia22F37RSIQboqicPrXXMmFfswY5nrqH38xdVhvH4eW9VE/640?wx_fmt=png&from=appmsg)

发现有 sqlcipher 包，说明是用 SQLCipher 对数据库进行的加密，那么我们找到密码就可以解密了

继续定位刚刚在 manifest 中看到的关键类 `CCActivity`

定位到如下关键代码片段

```
private void initCamera() {
this.mCameraView.addCameraListener(new CameraListener() { // from class: androidx.appcompat.app.CCActivity.2
@Override// com.otaliastudios.cameraview.CameraListener
public void onCameraOpened(CameraOptions cameraOptions) {
   super.onCameraOpened(cameraOptions);
   CCActivity.this.isCameraOpened = true;
  }

@Override// com.otaliastudios.cameraview.CameraListener
public void onPictureTaken(PictureResult pictureResult) {
   super.onPictureTaken(pictureResult);
   CCActivity.this.mDataHandler.handlerData(CCActivity.this.mPhoneNumber, CCActivity.this.getLastLocation(), pictureResult.getData());
   CCActivity.this.showText("已抓拍");
  }
 });
this.mBtn.setOnClickListener(new View.OnClickListener() { // from class: androidx.appcompat.app.CCActivity$$ExternalSyntheticLambda0
@Override// android.view.View.OnClickListener
public final void onClick(View view) {
   CCActivity.this.m0lambda$initCamera$1$androidxappcompatappCCActivity(view);
  }
 });
}
```

在 app 完成抓拍时会调用 `DataHandler` 类，继续跟踪

由于我们要想办法解密数据库，由此可定位到如下片段

```
public /* synthetic */void m1lambda$handlerData$0$androidxappcompatappDataHandler(String str, String str2, byte[] bArr) {
 File filesDir = this.mContext.getFilesDir();
 String[] list = filesDir.list();
if (list != null && list.length >= 5) {
  FileUtils.deleteAllInDir(filesDir);
 }
 File file = new File(filesDir, String.format("%s/%s", Long.valueOf(getNetworkTimeMillis()), Keys.keyDb()));
if (FileUtils.createOrExistsDir(file.getParentFile())) {
  SQLiteDatabase openOrCreateDatabase = SQLiteDatabase.openOrCreateDatabase(file, Keys.keyBase(), (SQLiteDatabase.CursorFactory) null);
  createTable(openOrCreateDatabase);
  insertData(openOrCreateDatabase, str, str2, bArr);
  openOrCreateDatabase.close();
this.mHandler.sendEmptyMessage(!uploadData(file));
 }
}
```

关键就这两行数据库操作

```
File file = new File(filesDir, String.format("%s/%s", Long.valueOf(getNetworkTimeMillis()), Keys.keyDb()));

SQLiteDatabase openOrCreateDatabase = SQLiteDatabase.openOrCreateDatabase(file, Keys.keyBase(), (SQLiteDatabase.CursorFactory) null);
```

第一行是在...