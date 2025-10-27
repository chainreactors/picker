---
title: Flutter 二次封装Sqlite基类
url: https://www.uedbox.com/post/68785/
source: 体验盒子
date: 2023-03-23
fetch_date: 2025-10-04T10:22:48.258802
---

# Flutter 二次封装Sqlite基类

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# Flutter 二次封装Sqlite基类

* 发表于 2023年03月22日
* [flutter](https://www.uedbox.com/design/flutter/)

目录表

Toggle

* [安装 Sqlite 插件](#%E5%AE%89%E8%A3%85_Sqlite_%E6%8F%92%E4%BB%B6)
* [创建基类，用来实例化数据库](#%E5%88%9B%E5%BB%BA%E5%9F%BA%E7%B1%BB%EF%BC%8C%E7%94%A8%E6%9D%A5%E5%AE%9E%E4%BE%8B%E5%8C%96%E6%95%B0%E6%8D%AE%E5%BA%93)
* [添加建表功能](#%E6%B7%BB%E5%8A%A0%E5%BB%BA%E8%A1%A8%E5%8A%9F%E8%83%BD)
* [数据库升级或降级](#%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8D%87%E7%BA%A7%E6%88%96%E9%99%8D%E7%BA%A7)
* [简易版增删改查](#%E7%AE%80%E6%98%93%E7%89%88%E5%A2%9E%E5%88%A0%E6%94%B9%E6%9F%A5)
* [开始实验](#%E5%BC%80%E5%A7%8B%E5%AE%9E%E9%AA%8C)
* [基类的完整代码](#%E5%9F%BA%E7%B1%BB%E7%9A%84%E5%AE%8C%E6%95%B4%E4%BB%A3%E7%A0%81)

### 安装 Sqlite 插件

首先我们需要安装 Sqlite 插件

|  |  |
| --- | --- |
| 1 | sqflite: ^2.0.2 |

### 创建基类，用来实例化数据库

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42 | import 'package:sqflite/sqflite.dart';    abstract class EntityPlus {  static const String \_dbName = "xxx";//数据库名称  static const int \_newVersion = 1;//数据库版本  static int \_oldVersion = 0;//数据库上一个版本  static String? \_dbBasePath;//数据库地址  static Database? \_database;//数据库实例    EntityPlus() {  \_initDatabase();  }    ///初始化数据库  Future<Database> \_initDatabase() async {  //获取数据库的位置  \_dbBasePath ??= await getDatabasesPath() + "/$\_dbName.db";    //打开数据库  \_database ??= await openDatabase(  \_dbBasePath!,  version: \_newVersion,  // onConfigure: (db) { },//数据库初始化时触发的回调  // onOpen: (db) { },//数据库被打开时触发的回调  // onCreate: (db, version){},//创建数据库时触发的回调  onUpgrade: (db, oldVersion, newVersion){//数据库升级时触发的回调  /\*  这里需要注意, 在后面时会用到\_oldVersion, \_oldVersion的变化会触发子类的某些方法  \*/  \_oldVersion = old;  },  onDowngrade: (db, oldVersion, newVersion){//数据库降级时触发的回调  /\*  这里需要注意, 在后面时会用到\_oldVersion, \_oldVersion的变化会触发子类的某些方法  \*/  \_oldVersion = old;  },  );    return \_database!;  }  } |

基类已经做好了初始化数据库的准备, 当子类继承基类时会触发初始化数据库事件, 初始化数据库完成后基类还需要做哪些事情?

1. 建表, 触发子类建表事件, 但是表如果已经存在了, 重复创建会报错, 所以这个函数只能触发一次;
2. 数据库升级或降级,触发子类的升级或降级事件, 并且也只能触发一次;

### 添加建表功能

如何触发子类建表事件, 并且只触发一次? 我们可以在基类中定义创建表的函数,并且该函数在子类中必须重写, 判断该表是否存在,如果不存在则创建

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 | import 'package:sqflite/sqflite.dart';    abstract class EntityPlus {  //...代码省略    abstract String tableName;//数据表名称,在子类中必须要重写的字段  bool exists = false;//数据表是否存在    ///建表函数, 在子类中必须重写  Future<void> onCreate(Database db, int version);    EntityPlus() {  \_initDatabase();  }    ///初始化数据库  Future<Database> \_initDatabase() async {  //...省略获取数据库的位置代码  //...省略打开数据库代码    //判断表是否存在  exists = await tableExists();  if(!exists){  //表不存在时调用建表函数  await onCreate(\_database!, \_newVersion);  exists = true;  }    return \_database!;  }    ///判断表是否存在  Future<bool> tableExists() async {  //内建表sqlite\_master  var res = await \_database!.rawQuery(  "SELECT \* FROM sqlite\_master WHERE TYPE = 'table' AND NAME = '$tableName'",  );  return res.isNotEmpty;  }  } |

### 数据库升级或降级

在基类中我们实现了建表的功能, 同理数据库升级或降级也可以这样写

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53 | import 'package:sqflite/sqflite.dart';    abstract class EntityPlus {  //...代码省略    abstract String tableName;//数据表名称,在子类中必须要重写的字段  bool exists = false;//数据表是否存在    ///建表函数, 在子类中必须重写  Future<void> onCreate(Database db, int version);    ///数据库升级时触发的函数,子类中可以根据需要时进行重写  onUpgrade(Database db, int oldVersion, int newVersion) {}    ///数据库降级触发的函数,子类中可以根据需要时进行重写  onDowngrade(Database db, int oldVersion, int newVersion) {}    EntityPlus() {  \_initDatabase();  }    ///初始化数据库  Future<Database> \_initDatabase() async {  //...省略获取数据库的位置代码  //...省略打开数据库代码  //...省略建表代码    //数据第一次创建时\_oldVersion等于0, 所以忽略  if (\_oldVersion != 0) {  if (\_oldVersion > \_newVersion) { //判断是否降级了  print("\_oldVersion === $\_oldVersion");  print("\_newVersion === $\_newVersion");  //数据库降级了,如果子类重写了onDowngrade方法, 则调用的是子类的;  await onDowngrade(  \_database!,  await \_database!.getVersion(),  \_newVersion,  );  } else if (\_oldVersion < \_newVersion) { //判断是否升级了  print("\_oldVersion === $\_oldVersion");  print("\_newVersion === $\_newVersion");  //数据库升级了,如果子类重写了onUpgrade方法, 则调用的是子类的;  await onUpgrade(  \_database!,  await \_database!.getVersion(),  \_newVersion,  );  }  }    return \_database!;  }  } |

### 简易版增删改查

好了现在我们有了建表的功能, 但是我们还需要对表进行增删改查, 所以接下来我们封装一个简易的增删改查功能

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96 | import 'package:sqflite/sqflite.dart';    abstract class EntityPlus {  //...代码省略    Database get database {  return \_database!;  }    ///插入数据  insert(Map<String, Object?> values) async {  return database.insert(tableName, values);  }    ///删除数据  remove(Map<String, Object?> json) async {  var database = await getDatabase();    List<String> keys = json.keys.toList();  List<String> where = [];  for (int i = 0; i < keys.length; i++) {  String key = keys[i];  where.add("$key=${json[key]}");  }    return database.delete(  tableName,  where: where.join(" and "),  );  }    ///修改数据  update(Map<String, Object?> json1, Map<String, Object?> json2) async {  List<String> keys = json1.keys.toList();  List<String> where = [];  for (int i = 0; i < keys.length; i++) {  String key = keys[i];  if (json1[key].runtimeType == String) {  where.add("$key='${json1[key]}'");  } else {  where.add("$key=${json1[key]}");  }  }    return database.update(  tableName,  json2,  where: where.isEmpty ? null : where.join(" and "),  );  }    ///缓存的数据  static final Map<String, List<Map<String, Object?>>> \_findCache = {};    ///查找数据  Future<List<Map<String, Object?>>> find({  Map<String, dynamic>? where,  int? page,  int? pageSize,  }) async {  List<String> keys = where?.keys.toList() ?? [];    List<String> whereList = [];  for (int i = 0; i < keys.length; i++) {  String key = keys[i];  if (where![key].runtimeType == String) {  whereList.add("$key='${where[key]}'");  } else {  whereList.add("$key=${where[key]}");  }  }    String sql = whereList.join(" and ");  String mapKey = "${tableName}\_${sql}\_page=${page}\_pageSize=$pageSize";    List data = sql.isEmpty ? [] : (\_findCache[mapKey] ?? []);  if (data.isNotEmpty) {  return \_findCache[mapKey]!;  }    var result = await database.query(  tableName,  where: sql.isEmpty ? null : sql,  offset: page == null ? null : (page - 1) \* (pageSize ?? 1),  limit: pageSize,  );  if (sql.isNotEmpty) {  \_findCache[mapKey] = result;  }  return result;  }    rawQuery(String sql) async {  return database.rawQuery(sql);  }  } |

### 开始实验

新建一个user\_info实体类, 继承EntityPlus

|  |  |
| --- | --- |
| 1  2  ...