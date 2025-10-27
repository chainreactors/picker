---
title: OkHttp 证书绑定流程 ssl pinning分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588181&idx=1&sn=2c535ea1ace2c13aed9abed21a46e158&chksm=b18c249f86fbad89d005e150c8c8c0a7034ccb410ddcb4da568e06caa5c4cb0347023b13c1bb&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-08
fetch_date: 2025-10-06T20:10:33.542487
---

# OkHttp 证书绑定流程 ssl pinning分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GB48xqPSosTeD8ibUTA0ysibnLYlf9r7M1Gwg3kAX12xolOABTRWX9uZoUmRmLMrRLbgkDMWobREHA/0?wx_fmt=jpeg)

# OkHttp 证书绑定流程 ssl pinning分析

绿豆粥

看雪学苑

```
一

前言
```

##

https 相比 http 更加安全的其中一个原因就是增加了证书功能，用于对数据传输双方进行身份的验证和加密传输数据。之前直接使用 charles 或者 fiddler 等中间人抓包的方式，就无法获取到明文数据，或者无法与服务器建立连接。从而导致安全分析被卡在了第一步。虽然 app 使用了 https 方式对抗抓包，但是依然会有解决方案。本篇文章主要就是记录了我学习对抗https 过程中知识点的梳理。

```
二

Okhttp 建立 https 的方式
```

##

要想反制https抓包，首先就得知道正向是如何开发的。okhttp 使用 https 有几种方式，第一种信任所有证书，第二种只信任系统证书，第三种只信任指定证书。

## 信任所有证书

HostnameVerifier 中不验证主机域名，TrustAllCerts  也不做任何处理。这样就是默认信任所有证书

```
private static class TrustAllCerts implements X509TrustManager {
    public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
    }

    public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {

    }

    public X509Certificate[] getAcceptedIssuers() {
        // //返回长度为0的数组，相当于return null
        return new X509Certificate[0];
    }
}

// 信任所有的域名
HostnameVerifier hostnameVerifierTrustAllHoust = new HostnameVerifier() {
    @Override
    public boolean verify(String s, SSLSession sslSession) {
        //信任所有域名
        return true;
    }
};

public void httpsTrustAll() {
    /**
     * 信任所有证书
     */
    new Thread(new Runnable() {
        @RequiresApi(api = Build.VERSION_CODES.N)
        @Override
        public void run() {
            SSLSocketFactory sSLSocketFactory = null;
            try {
                SSLContext sc = SSLContext.getInstance("TLS");
                sc.init(null, new TrustManager[]{new TrustAllCerts()}, new SecureRandom());

                sSLSocketFactory = sc.getSocketFactory();

                OkHttpClient mClient = new OkHttpClient().newBuilder()
                        .sslSocketFactory(sSLSocketFactory, new TrustAllCerts())
                        .hostnameVerifier(hostnameVerifierTrustAllHoust)
                        .build();

                Request request = new Request.Builder()
                        .url("https://www.baidu.com")
                        .build();
                String msg = "";
                try (Response response = mClient.newCall(request).execute()) {
                    msg = "HTTPS 忽略所有证书，连接成功";
                } catch (IOException e) {
                    msg = "HTTPS 忽略所有证书，连接失败";
                    e.printStackTrace();
                }
                mHandler.obtainMessage(2, msg).sendToTarget();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }).start();
}
```

## 信任系统证书

okhttp 如果不做任何配置，默认就是信任系统的证书。

```
public void httpsTrustSystemca() {
    /**
     * 信任系统证书
     */
    new Thread(new Runnable() {
        @Override
        public void run() {
            // OkHttp 链接使用 HTTPS 时，默认自动验证系统的证书。不需要额外配置
            Request request = new Request.Builder()
                    .url("https://www.baidu.com/?q=defaultCerts")
                    .build();
            String msg = "";
            try (Response response = new OkHttpClient().newCall(request).execute()) {
                msg = "HTTPS 验证系统证书，连接成功";
            } catch (IOException e) {
                msg = "HTTPS 验证系统证书，连接失败";
                e.printStackTrace();
            }
            mHandler.obtainMessage(2, msg).sendToTarget();
        }
    }).start();
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GB48xqPSosTeD8ibUTA0ysibsUTs7UjYtQ4E5la5GXBEGdRr3iaKpYJmt5rQIicHKOUhelvjOVOe7FGQ/640?wx_fmt=jpeg&from=appmsg)

## 只信任指定证书

更加专业的说法叫做 ssl pinning ，主要是将服务器的公钥或证书直接嵌入到客户端应用中，确保客户端只与特定的服务器建立安全连接。验证也有几种说法，单项验证和双向验证。双向验证是 app 验证服务端证书，同时服务器也验证 app证书。单项验证分两种情况，第一种客户端校验服务端证书，服务端不校验 app 证书，这是比较常见的。第二种，服务验证 app 证书，app 不校验服务端证书，这种就少见了。代码实现方式，第一种是通过 okhttp自带的 CertificatePinner 进行证书的绑定服务端证书，第二种就是前面验证系统证书时，使用的继承 X509TrustManager  的方式。

### 单项校验

1.CertificatePinner  证书绑定

这里使用了百度的证书，把证书从网站上保存下来之后，手动生成 hash，再进行 base64编码。通过下面的命令就可以搞定。

```
openssl x509 -in baidu.crt -pubkey -noout | openssl rsa -pubin -outform der | openssl dgst -sha256 -binary | openssl base64
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GB48xqPSosTeD8ibUTA0ysibViazMBlOynAp8wNOEsvRKvKibZYhy1JffxSPKPjW5vV1IL7lwwDK4BlQ/640?wx_fmt=jpeg&from=appmsg)

通过   .certificatePinner(certificatePinner) 把 CertificatePinner 添加的百度证书绑定上去。在 okhttp 源码中，会自动进行证书的判断（后面的源码分析会有讲解），当证书不匹配就抛出异常。注意 CertificatePinner  只能绑定服务器证书进行验证，如果想要把 app 证书传入服务器，需要另外的代码。具体看后面的双向认证。

```
    private void appCheckServerCertificatePinner() {        try {

            CertificatePinner certificatePinner = new CertificatePinner.Builder()
                    .add("www.baidu.com", "sha256/cGuxAXyFXFkWm61cF4HPWX8S0srS9j0aSqN0k4AP+4A=") // 替换为实际的公钥指纹
                    .build();
            HttpLoggingInterceptor loggingInterceptor = new HttpLoggingInterceptor();
            zInterceptor interceptor = new zInterceptor();
            // 配置 OkHttpClient
            OkHttpClient okHttpClient = new OkHttpClient.Builder()
                    .certificatePinner(certificatePinner)
                    .addInterceptor(new StackTraceInterceptor())
                    .addInterceptor(interceptor)
                    .build();

            // 发起请求
            Request request = new Request.Builder()
                    .url("https://www.baidu.com/")
                    .build();
            // 异步请求
            okHttpClient.newCall(request).enqueue(new Callback() {
                @Override
                public void onFailure(Call call, IOException e) {
                    Log.e(TAG, "app 百度证书 CertificatePinner " + e.toString());
                    mHandler.obtainMessage(336, "").sendToTarget();
                }

                @Override
                public void onResponse(Call call, Response response) throws IOException {
                    Log.i(TAG, "app 百度证书 CertificatePinner " + response.body().string());
                    mHandler.obtainMessage(333, "").sendToTarget();
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GB48xqPSosTeD8ibUTA0ysib1Es0XUWXIdS6LAcZRhGzGCIcumnrO19648tKgo1Pk95hIMcayNSk7g/640?wx_fmt=jpeg&from=appmsg)

使用 charles 进行抓包。尽管 charles 的证书已经导入到系统中了。依然无法抓包。通过提示就可以知道，需要让 app 信任 Charles 的证书，才能抓包。具体的对抗方式在之后有介绍。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GB48xqPSosTeD8ibUTA0ysibXPvjVZeayK3822TcI1KTge4zD6lcVibV4PQb3HoCpcMGUzkucXG2zSQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GB48xqPSosTeD8ibUTA0ysibfBYu14YPo5ibsRuZhcCUkQIqGGzB0dHBOBYlFODic4kyVxKlS33UW33Q/640?wx_fmt=jpeg&from=appmsg)

2.X509TrustManager 证书绑定

X509TrustManager 自定义证书绑定。通过构造方法传入服务端的证书，在 checkServerTrusted 进行证书的校验。

使用 X509Certificate 的 equals 来判断两个证书是否相同，不相同直接抛出异常。

```
// ====== app 验证 serverca ==== 单向验证 ===
private static class TrustServerCerts implements X509TrustManager {
    private final X509Certificate trustedCertificate;//传入信任的证书

    public TrustServerCerts(X509Certificate trustedCertificate) {
        this.trustedCertificate = trustedCertificate;
    }

    @Override
    public void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException {
    }

    @Override
    public void checkServerTrusted(X509Certificate[] chain, String authType) throws CertificateException {
        // 服务器证书验证逻辑
        if (chain == null || chain.length == 0) {
            throw new CertificateException("No server certificates provided.");
        }

        // 验证服务器证书是否与受信任的证书匹配
        X509Certificate serverCertificate = chain[0];
        // Certificate 的 equal 方法
        if (!serverCertificate.equals(trustedCertificate)) {
            throw new CertificateException("Server certificate does not match the trusted certificate.");
        } else {
            Log.d(TAG, "https 验证服务器证书成功");
        }
    }

    @Override
    public X509Certificate[] getAcceptedIssuers() {
        // 返回受信任的证书颁发机构（CA）列表
     ...