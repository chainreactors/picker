---
title: ARL分析与进阶使用
url: https://mp.weixin.qq.com/s/BcVmNQwedI6y1yDOV0F1PQ
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:52:44.492391
---

# ARL分析与进阶使用

# ARL分析与进阶使用

Str2iv8er
Str2iv8er

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在使用ARL（Asset Reconnaissance Lighthouse资产侦察灯塔系统，项目地址地址为https://github.com/TophantTechnology/ARL）的时候，有两个问题比较困扰我：

* • ARL使用Fofa导入数据的时候怎么降重？
* • 如何自己手动编写Poc？

在网上查阅了一些相关资料后，我发现并没有师傅写的很清晰，于是诞生了写这篇文章的想法。

这篇文章不涉及ARL的基础搭建过程和基础使用过程，如果您之前没有使用过ARL，详情可以参考官网教程：https://tophanttechnology.github.io/ARL-doc/system\_install/

## 1.Fofa降重

先说结论，是由于Fofa\_api的限制而不是ARL本身的问题

![image-20240113131658954](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlE4Jw697nLJGTGjickv604bLCnMDLwINPx54Xetrhnpm3YPNoTjnTHxqjrBfib2wZyZqYtjkU69LWZgnSlHLucJUZyPA9fw1QIK8/640?wx_fmt=png&from=appmsg "null")

来源于我之前的使用体验，使用同样的Fofa语句，比如能搜到大量地的资产，但是ARL只会跑几千条，然后我们反复运行发现得到的资产结果是一致的，这样就大大地影响了配合Fofa使用好处，只能自己更换不同的Fofa语句来实现降重，非常麻烦。

首先我们先黑盒看看调用fofa的流程：

![image-20240111195213899](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlH9y2VBDYA2efs4HOVg8OIFMBpdAgJ5nJKIODZZFicmF27tDX1b1sbWyicEsOk0YSzdVRtJ0qU1giaDN4IiaWnTmgvW1WmFe4YQJC4/640?wx_fmt=png&from=appmsg "null")

```
POST /api/task_fofa/test HTTP/2

{"query":"org=\"China Education and Research Network Center\""}
```

```
HTTP/2 200 OK

{"message": "success", "code": 200, "data": {"size": 13492282, "query": "org=\"China Education and Research Network Center\""}}
```

可以看见这里返回的结果是13492282条

然后我们直接去项目里面去找：

路径为：`ARL-2.6.1\app\routes\taskFofa.py`

```
from flask_restx import Namespace, fields
from app.utils import get_logger, auth, build_ret, conn_db
from app.modules import ErrorMsg, CeleryAction
from app.services.fofaClient import fofa_query, fofa_query_result
from app import celerytask
from bson import ObjectId
from . import ARLResource

ns = Namespace('task_fofa', description="Fofa 任务下发")

logger = get_logger()

test_fofa_fields = ns.model('taskFofaTest',  {
    'query': fields.String(required=True, description="Fofa 查询语句")
})

@ns.route('/test')
class TaskFofaTest(ARLResource):

    @auth
    @ns.expect(test_fofa_fields)
    def post(self):
        """
        测试Fofa查询连接
        """
        args = self.parse_args(test_fofa_fields)
        query = args.pop('query')
        data = fofa_query(query, page_size=1)
        if isinstance(data, str):
            return build_ret(ErrorMsg.FofaConnectError, {'error': data})

        if data.get("error"):
            return build_ret(ErrorMsg.FofaKeyError, {'error': data.get("errmsg")})

        item = {
            "size": data["size"],
            "query": data["query"]
        }

        return build_ret(ErrorMsg.Success, item)

add_fofa_fields = ns.model('addTaskFofa', {
    'query': fields.String(required=True, description="Fofa 查询语句"),
    'name': fields.String(required=True, description="任务名"),
    'policy_id': fields.String(description="策略 ID")
})

@ns.route('/submit')
class AddFofaTask(ARLResource):

    @auth
    @ns.expect(add_fofa_fields)
    def post(self):
        """
        提交Fofa查询任务
        """
        args = self.parse_args(add_fofa_fields)
        query = args.pop('query')
        name = args.pop('name')
        policy_id = args.get('policy_id')

        task_options = {
            "port_scan_type": "test",
            "port_scan": True,
            "service_detection": False,
            "service_brute": False,
            "os_detection": False,
            "site_identify": False,
            "file_leak": False,
            "ssl_cert": False
        }

        data = fofa_query(query, page_size=1)
        if isinstance(data, str):
            return build_ret(ErrorMsg.FofaConnectError, {'error': data})

        if data.get("error"):
            return build_ret(ErrorMsg.FofaKeyError, {'error': data.get("errmsg")})

        if data["size"] <= 0:
            return build_ret(ErrorMsg.FofaResultEmpty, {})

        fofa_ip_list = fofa_query_result(query)
        if isinstance(fofa_ip_list, str):
            return build_ret(ErrorMsg.FofaConnectError, {'error': data})

        if policy_id and len(policy_id) == 24:
            task_options.update(policy_2_task_options(policy_id))

        task_data = {
            "name": name,
            "target": "Fofa ip {}".format(len(fofa_ip_list)),
            "start_time": "-",
            "end_time": "-",
            "task_tag": "task",
            "service": [],
            "status": "waiting",
            "options": task_options,
            "type": "fofa",
            "fofa_ip": fofa_ip_list
        }
        task_data = submit_fofa_task(task_data)

        return build_ret(ErrorMsg.Success, task_data)

def policy_2_task_options(policy_id):
    options = {}
    query = {
        "_id": ObjectId(policy_id)
    }
    data = conn_db('policy').find_one(query)
    if not data:
        return options

    policy_options = data["policy"]
    policy_options.pop("domain_config")

    ip_config = policy_options.pop("ip_config")
    site_config = policy_options.pop("site_config")

    options.update(ip_config)
    options.update(site_config)
    options.update(policy_options)

    return options

def submit_fofa_task(task_data):
    conn_db('task').insert_one(task_data)
    task_id = str(task_data.pop("_id"))
    task_data["task_id"] = task_id

    task_options = {
        "celery_action": CeleryAction.FOFA_TASK,
        "data": task_data
    }

    celery_id = celerytask.arl_task.delay(options=task_options)

    logger.info("target:{} celery_id:{}".format(task_id, celery_id))

    values = {"$set": {"celery_id": str(celery_id)}}
    task_data["celery_id"] = str(celery_id)
    conn_db('task').update_one({"_id": ObjectId(task_id)}, values)

    return task_data
```

其中有一个类和俩函数在其他地方：

```
#  -*- coding:UTF-8 -*-
import base64
from app.config import Config
from app import utils
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

class FofaClient:
    def __init__(self, email, key, page_size=9999):
        self.email = email
        self.key = key
        self.base_url = Config.FOFA_URL
        self.search_api_url = "/api/v1/search/all"
        self.info_my_api_url = "/api/v1/info/my"
        self.page_size = page_size
        self.param = {}

    def info_my(self):
        param = {
            "email": self.email,
            "key": self.key,
        }
        self.param = param
        data = self._api(self.base_url + self.info_my_api_url)
        return data

    def fofa_search_all(self, query):
        qbase64 = base64.b64encode(query.encode())
        param = {
            "email": self.email,
            "key": self.key,
            "qbase64": qbase64.decode('utf-8'),
            "size": self.page_size
        }

        self.param = param
        data = self._api(self.base_url + self.search_api_url)
        return data

    def _api(self, url):
        data = utils.http_req(url, 'get', params=self.param).json()
        if data.get("error") and data["errmsg"]:
            raise Exception(data["errmsg"])

        return data

    def search_cert(self, cert):
        query = 'cert="{}"'.format(cert)
        data = self.fofa_search_all(query)
        results = data["results"]
        return results

def fetch_ip_bycert(cert, size=9999):
    ip_set = set()
    logger.info("fetch_ip_bycert {}".format(cert))
    try:
        client = FofaClient(Config.FOFA_EMAIL, Config.FOFA_KEY, page_size=size)
        items = client.search_cert(cert)
        for item in items:
            ip_set.add(item[1])
    except Exception as e:
        logger.warn("{} error: {}".format(cert, e))

    return list(ip_set)

def fofa_query(query, page_size=9999):
    try:
        if not Config.FOFA_KEY or not Config.FOFA_KEY:
            return "please set fofa key in config-docker.yaml"

        client = FofaClient(Config.FOFA_EMAIL, Config.FOFA_KEY, page_size=page_size)
        info = client.info_my()
        if info.get("vip_level") == 0:
            return "不支持注册用户"

        # 普通会员，最多只查100条
        if info.get("vip_level") == 1:
            client.page_size = min(page_size, 100)

        data = client.fofa_search_all(query)
        return data

    except Exception as e:
        er...