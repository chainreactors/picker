---
title: 一个项目带你入门AI应用开发07 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22167976
source: 博客园 - bamb00
date: 2026-08-03
fetch_date: 2026-08-04T04:56:31.227665
---

# 一个项目带你入门AI应用开发07 - bamb00

* [![тЇџт«бтЏГlogo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "т╝ђтЈЉУђЁуџёуйЉСИіт«ХтЏГ")
* [С╝џтЉў](https://cnblogs.vip/)
* [тЉеУЙ╣](https://cnblogs.vip/store)
* [Тќ░жЌ╗](https://news.cnblogs.com/)
* [тЇџжЌ«](https://q.cnblogs.com/)
* [жЌфтГў](https://ing.cnblogs.com/)
* [УхътіЕтЋє](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![Тљюу┤б](//assets.cnblogs.com/icons/search.svg)
  ![Тљюу┤б](//assets.cnblogs.com/icons/enter.svg)
  + ![Тљюу┤б](//assets.cnblogs.com/icons/search.svg)

    ТЅђТюЅтЇџт«б
  + ![Тљюу┤б](//assets.cnblogs.com/icons/search.svg)

    тйЊтЅЇтЇџт«б
* [![тєЎжџЈугћ](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "тєЎжџЈугћ")
  [![ТѕЉуџётЇџт«б](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "ТѕЉуџётЇџт«б")
  [![уЪГТХѕТЂ»](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "уЪГТХѕТЂ»")
  ![у«ђТ┤ЂТеАт╝Ј](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![ућеТѕитц┤тЃЈ](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [ТѕЉуџётЇџт«б](https://www.cnblogs.com/my)
  [ТѕЉуџётЏГтГљ](https://home.cnblogs.com/)
  [У┤дтЈиУ«Йуй«](https://account.cnblogs.com/settings/account)
  [С╝џтЉўСИГт┐Ѓ](https://vip.cnblogs.com/my)
  у«ђТ┤ЂТеАт╝Ј ...
  жђђтЄ║уЎ╗тйЋ

  [Т│етєї](https://account.cnblogs.com/signup)
  уЎ╗тйЋ

[![У┐ћтЏъСИ╗жАх](/skins/custom/images/logo.gif)](https://www.cnblogs.com/goodhacker/)

# [С║║ТђюуЏ┤УіѓућЪТЮЦуўд№╝їУЄфУ«ИжФўТЮљУђЂТЏ┤тѕџсђѓ](https://www.cnblogs.com/goodhacker)

##

* [тЇџт«бтЏГ](https://www.cnblogs.com/)
* [ждќжАх](https://www.cnblogs.com/goodhacker/)
* [Тќ░жџЈугћ](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [УЂћу│╗](https://msg.cnblogs.com/send/bamb00)
* У«бжўЁ
* [у«Ауљє](https://i.cnblogs.com/)

# [СИђСИфжА╣уЏ«тИдСйатЁЦжЌеAIт║ћућет╝ђтЈЉ07](https://www.cnblogs.com/goodhacker/p/22167976 "тЈЉтИЃС║ј 2026-08-03 11:40")

# угг 7 У»Й№╝џтЈ»ТЈњТІћуџёТЋ░ТЇ«Т║љ

## 7.1 СйауџёуЏ«ТаЄ

тюеСИЇТћ╣ Agent С╗БуаЂуџётЅЇТЈљСИІ№╝їтѕЄТЇбТЋ░ТЇ«Т║љ№╝ѕС╗јТ╝ћуц║ТЋ░ТЇ«тѕ░уюЪт«ъТЋ░ТЇ«т║Њ№╝Ѕсђѓ

```
.env СИГ:
DATA_PROVIDER=demo       Рєњ Сй┐ућетєЁтГўТ╝ћуц║ТЋ░ТЇ«
DATA_PROVIDER=postgres   Рєњ Сй┐уће PostgreSQL ТЋ░ТЇ«т║Њ
```

## 7.2 жЌ«жбў№╝џТЋ░ТЇ«Уђдтљѕ

угг 4 У»Йуџё `_execute_tool`№╝џ

```
def _execute_tool(name, args):
    if name == "query_order":
        # У«бтЇЋТЋ░ТЇ«тєЎТГ╗тюеС╗БуаЂжЄї
        _ORDERS = {
            "ORD-001": {"status": "shipped", ...},
        }
        return _ORDERS.get(args["order_id"])
```

ТЃ│ТЇбТѕљ PostgreSQL№╝ЪУдЂТћ╣ `_execute_tool`сђѓТЃ│ТЇбТѕљС╗ј CSV У»╗№╝ЪУдЂТћ╣ `_execute_tool`сђѓТЃ│тєЎтЇЋтЁЃТхІУ»Ћ№╝ЪжюђУдЂтЄєтцЄуюЪт«ъТЋ░ТЇ«сђѓ

**Agent уџёжђ╗УЙЉтњїТЋ░ТЇ«Т║љУђдтљѕтюеСИђУхиС║єсђѓ**

## 7.3 ТюгУ┤ежЌ«жбў

СИЇТў»"С╗БуаЂтєЎтЙЌСИЇтЦй"№╝їУђїТў»СИђСИфТъХТъёУ«ЙУ«АжЌ«жбў№╝џ

* **Agent уџёжђ╗УЙЉ**№╝ѕ"С╗ђС╣ѕТЌХтђЎт║ћУ»ЦТЪЦУ«бтЇЋ"№╝Ѕт║ћУ»Цуе│т«џ
* **ТЋ░ТЇ«Т║љ**№╝ѕ"У«бтЇЋТЋ░ТЇ«С╗јтЊфТЮЦ"№╝Ѕт║ћУ»ЦуЂхТ┤╗

уе│т«џуџёжђ╗УЙЉСИЇт║ћУ»ЦСЙЮУхќуЂхТ┤╗уџёт«ъуј░сђѓ

## 7.4 УДБТ│Ћ№╝џТійУ▒АТјЦтЈБ

### уггСИђТГЦ№╝џт«џС╣ЅТЋ░ТЇ«ТеАтъІ

```
@dataclass(frozen=True)
class Order:
    order_id: str
    status: str
    product: str
    amount: float
```

### уггС║їТГЦ№╝џт«џС╣ЅТійУ▒АТјЦтЈБ

```
class ECommerceDataProvider(ABC):
    @abstractmethod
    def get_order(self, order_id: str) -> Optional[Order]: ...
    @abstractmethod
    def get_shipment(self, order_id: str) -> Optional[Shipment]: ...
    @abstractmethod
    def get_all_knowledge_docs(self) -> list[KnowledgeDoc]: ...
```

### уггСИЅТГЦ№╝џт«ъуј░тцџСИфуЅѕТюг

```
class DemoDataProvider(ECommerceDataProvider):
    """тєЁтГўТ╝ћуц║ТЋ░ТЇ«"""
    def get_order(self, order_id):
        return _ORDERS.get(order_id)

class PostgresDataProvider(ECommerceDataProvider):
    """PostgreSQL т«ъуј░"""
    def __init__(self, conn_string):
        self.conn = psycopg2.connect(conn_string)
    def get_order(self, order_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        row = cursor.fetchone()
        if row:
            return Order(row[0], row[1], row[2], row[3])
        return None
```

### уггтЏЏТГЦ№╝џтиЦтјѓТеАт╝Ј

```
def get_data_provider():
    provider_type = settings.data_provider
    if provider_type == "demo":
        return DemoDataProvider()
    elif provider_type == "postgres":
        return PostgresDataProvider(settings.database_url)
```

## 7.5 Тћ╣жђатљјуџё Tool Agent

```
from app.data.config import get_data_provider

def _execute_tool(name, args):
    provider = get_data_provider()

    if name == "query_order":
        order = provider.get_order(args.get("order_id", ""))
        if order:
            return json.dumps({"found": True, "order": asdict(order)})
        return json.dumps({"found": False})
```

`_execute_tool` СИЇтєЇуЪЦжЂЊТЋ░ТЇ«С╗јтЊфТЮЦсђѓт«ЃтЈфуЪЦжЂЊ"У░Ѓ `provider.get_order()` УЃйТІ┐тѕ░У«бтЇЋ"сђѓ

## 7.6 У┐Ўтњї Web т╝ђтЈЉуџётѕєт▒ѓТюЅС╗ђС╣ѕСИЇтљї№╝Ъ

Web т╝ђтЈЉСИГС╣ЪтИИућеТјЦтЈБТійУ▒АТЋ░ТЇ«т▒ѓсђѓСйє Agent у│╗у╗ЪуџёТЋ░ТЇ«т▒ѓТюЅСИцуѓ╣СИЇтљї№╝џ

1. **ТЋ░ТЇ«Тў»СИ║ LLM ТюЇтіАуџё**сђѓТјЦтЈБУ«ЙУ«АУдЂУђЃУЎЉ LLM жюђУдЂС╗ђС╣ѕТЋ░ТЇ«сђЂС╗ЦС╗ђС╣ѕТа╝т╝ЈУјитЈќсђѓТ»ћтдѓ `get_order` У┐ћтЏъуџё `Order` т»╣У▒АС╝џУбФт║ЈтѕЌтїќТѕљ JSON у╗Ў LLM уюІ№╝їтГЌТ«хтљЇУдЂТИЁТЎ░сђѓ
2. **жћЎУ»»тцёуљєУдЂтЈІтЦй**сђѓтдѓТъюТЋ░ТЇ«т║ЊУ┐ъТјЦтц▒У┤Ц№╝їLLM т║ћУ»ЦтЏътцЇ"у│╗у╗ЪТџѓТЌХТЌаТ│ЋТЪЦУ»бУ«бтЇЋ"УђїСИЇТў»ТіЏтЄ║ 500 жћЎУ»»сђѓ

## ТюгУ»ЙуЪЦУ»єуѓ╣

| Тдѓт┐х | СйатЂџС║єС╗ђС╣ѕ | СИ║С╗ђС╣ѕ |
| --- | --- | --- |
| ТійУ▒АТјЦтЈБ | ABC + abstractmethod | Agent СЙЮУхќТјЦтЈБСИЇСЙЮУхќт«ъуј░ |
| тиЦтјѓТеАт╝Ј | Та╣ТЇ«жЁЇуй«тѕЏт╗║т«ъСЙІ | тѕЄТЇбТЋ░ТЇ«Т║љтЈфТћ╣жЁЇуй«№╝їСИЇТћ╣С╗БуаЂ |
| т╝ђжЌГтјЪтѕЎ | Тќ░тбът«ъуј░у▒╗тЇ│тЈ» | СИЇС┐«Тћ╣ Agent жђ╗УЙЉ |

## У»ЙтљјСйюСИџ

1. т«ъуј░СИђСИф `CSVDataProvider`№╝їС╗ј CSV ТќЄС╗ХУ»╗тЈќУ«бтЇЋТЋ░ТЇ«
2. т«ъуј░СИђСИф `RedisDataProvider`№╝їС╗ј Redis У»╗тЈќС╝џУ»ЮтјєтЈ▓

## жЮбУ»ЋтЈ»УЃйС╝џжЌ«

> "Data Provider ТеАт╝Јтњї Repository ТеАт╝ЈТюЅС╗ђС╣ѕтї║тѕФ№╝Ъ"
> ТюгУ┤еуЏИтљї№╝їжЃйТў»жџћуд╗ТЋ░ТЇ«У«┐жЌ«сђѓтї║тѕФтюеС║јтЉйтљЇтЂЈтЦйтњїТійУ▒Ау▓њт║дсђѓData Provider ТЏ┤т╝║У░Ѓ"ТЈљСЙЏТЋ░ТЇ«"№╝їRepository ТЏ┤т╝║У░Ѓ"УЂџтљѕТа╣"сђѓ

posted @
2026-08-03 11:40
[bamb00](https://www.cnblogs.com/goodhacker)
жўЁУ»╗(24)
У»ёУ«║(0)

ТћХУЌЈ
[СИЙТіЦ](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22167976&targetId=22167976&targetType=0)

тѕиТќ░жАхжЮб[У┐ћтЏъжАХжЃе](#top)

[![](https://img2024.cnblogs.com/blog/35695/202607/35695-20260715081632770-1485313413.webp)](https://www.trae.com.cn/?utm_source=advertising&utm_medium=cnblogs_ug_cpa&utm_term=hw_trae_cnblogs)

### тЁгтЉі

[тЇџт«бтЏГ](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)ТхЎтЁгуйЉт«ЅтцЄ 33010602011771тЈи](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[ТхЎICPтцЄ2021040463тЈи-3](https://beian.miit.gov.cn)