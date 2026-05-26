---
title: CrewAI-Studio 未授权 RCE：从 JSON 导入到 eval 的任意代码执行
url: https://mp.weixin.qq.com/s/IbZczLPZUCW2yCWqIsGkNg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:50.630151
---

# CrewAI-Studio 未授权 RCE：从 JSON 导入到 eval 的任意代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP852icepFMk2OicMRickFhU2ibicX7uiaKtWWWibOYnXLpn7vGuZiczMicicTJ1H6tbVojERjT733ccUf23R3U52SwUyzL2ian7ibF8ic3iag9hbiak/0?wx_fmt=jpeg)

# CrewAI-Studio 未授权 RCE：从 JSON 导入到 eval 的任意代码执行

原创

ElmWhite
ElmWhite

N0va7安全小记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前言

在分析一类 AI 编排项目时，可以很清楚地看到一件事：Agent 平台的风险，不在“模型会不会胡说”，而在“模型能驱动什么”。一旦项目把外部输入、持久化配置、工具实例化和本地执行能力串起来，很多原本看上去只是普通参数的字段，都会被放大成真实攻击面。

CrewAI-Studio  就是这样一个典型样本。它是一个基于 Streamlit 和 CrewAI 的低代码多智能体应用原型工具，提供 Web 界面用于创建  Agent、Task、Crew、Tool 和 Knowledge Source，也支持 JSON 导入导出完整工作流。这里就围绕其中一个点展开：**RCE**。

项目地址：https://github.com/strnad/CrewAI-Studio

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4yRoMuNP850HJBUxHZdw9lTpAoqlFvy6lygibk0exL09z671TAibf0UaUD2gXQ4Xo96Z1vpeq5GBFNXia5lpiark6tSvqHBkHGksJd01hSrKkX4/640?wx_fmt=png&from=appmsg)

# 项目版本

* `main` 分支最新提交： `be9c19b`

# 漏洞分析思路

分析这类 AI 编排项目时，不建议一开始就盯着某个危险函数看。更合理的方式是先看数据流：外部输入从哪里进来、保存到哪里、运行时怎么被加载、最后有没有进入危险执行点。

这类项目一般有几个危险特征：

1. 有 UI 配置入口，参数会被保存到数据库。
2. 有 JSON 导入导出，外部数据能批量进入系统。
3. 有运行时工具实例化，配置不会只停在“展示层”。
4. 有 Agent 执行链路，工具参数会跟着任务流一起被加载。 CrewAI-Studio 正好全都具备。

从代码结构上，最值得怀疑的就是**工具层**。因为在 AI 编排系统里，工具参数通常不会只用于显示，而是会在运行时被真正传给库、客户端或者本地能力。只要参数处理方式不安全，就很容易从“配置问题”直接变成“执行问题”。

## UI 工具配置

先看正常 UI 配置工具的路径。`PageTools` 中创建工具时，会根据工具名实例化对应工具类，并立即保存到数据库。

```
def create_tool(self, tool_name):
    tool_class = self.available_tools[tool_name]
    tool_instance = tool_class(rnd_id())
    if 'tools' not in ss:
        ss.tools = []
    ss.tools.append(tool_instance)
    db_utils.save_tool(tool_instance)
```

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP852RwIVHYO5zppSQTY2ibnrLWN84Pt6vIGZffXFeu7wOWp3qibM0y2haRn5sjITsuezlvWC49t5YEicE4pqpKaN1ibTlBLQjucJodVo/640?wx_fmt=png&from=appmsg)

参数编辑也类似。页面上的文本框内容变化后，会调用 `set_tool_parameter()`，然后再次保存工具。

```
def set_tool_parameter(self, tool_id, param_name, value):
    if value == "":
        value = None
    for tool in ss.tools:
        if tool.tool_id == tool_id:
            tool.set_parameters(**{param_name: value})
            db_utils.save_tool(tool)
            break
```

这一步说明，`headers` 这类工具参数不是临时变量，而是会进入后端持久化流程。后面只要运行 Crew，这些参数还会重新被取出来参与工具实例化。

## JSON 导入

相比手工配置，JSON 导入入口更适合构造完整攻击链。`PageExportCrew` 中会接收上传的 JSON 文件，解析之后如果发现它是一个列表，就把它写成 `uploaded_file.json`，再交给 `db_utils.import_from_json()`。

```
uploaded_file = st.file_uploader(t("export.import_json"), type="json")
if uploaded_file is not None:
    json_data = json.load(uploaded_file)

    if isinstance(json_data, list):
        with open("uploaded_file.json", "w") as f:
            json.dump(json_data, f)
        db_utils.import_from_json("uploaded_file.json")
        st.success(t("export.import_success_full"))
```

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP853lqrpnLcyHokBx3px18fJiblChnhic1Cdz0DxvtkM6blhpyZ0X9CZa89sg48W6FtdKdxBzcJWicDvTQBDFctOPiaUFRnMra5Ys2TE/640?wx_fmt=png&from=appmsg)

这里没有看到对字段结构、工具类型、危险参数的校验。也就是说，只要 JSON 符合系统导出的实体格式，就可以把 tool、agent、task、crew 一起导入。

再看 `import_from_json()`。它读取 JSON 列表后，对每个 entity 执行 upsert，字段只有 `id`、`entity_type`、`data`。

```
def import_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    with get_db_connection() as conn:
        for entity in data:
            upsert_sql = text('''
                INSERT INTO entities (id, entity_type, data)
                VALUES (:id, :etype, :data)
                ON CONFLICT(id) DO UPDATE
                    SET entity_type = EXCLUDED.entity_type,
                        data = EXCLUDED.data
            ''')

            conn.execute(
                upsert_sql,
                {
                    "id": entity['id'],
                    "etype": entity['entity_type'],
                    "data": json.dumps(entity['data'])
                }
            )
        conn.commit()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4yRoMuNP8503Jsa5V2E4zlzyiajNtX2EfaQ55Or6q1RdQ05AIFIxAl5M4GWMe8BRJT2xHO6As0InjMmYRS6iaCHhoGSY7X3mphxQLm2UIw0Qo/640?wx_fmt=png&from=appmsg)

这里就能解释后面为什么 POC JSON 要按下面这种结构构造：

* `entity_type: "tool"`：创建一个恶意工具实体。
* `data.name: "CustomApiTool"`：让加载逻辑后续选择 `MyCustomApiTool` 这个包装类。
* `data.parameters.headers`：放入最终会进入 `eval()` 的 payload。
* `entity_type: "agent"`：创建一个 Agent，并用 `tool_ids` 绑定恶意工具。
* `entity_type: "task"`：创建一个任务，并用 `agent_id` 绑定上面的 Agent。
* `entity_type: "crew"`：创建一个可在 Kickoff 页面选择和运行的 Crew，并用 `agent_ids`、`task_ids` 串起完整工作流。

这样构造之后，导入的不是孤立 payload，而是一条可以被正常 UI 运行起来的最小工作流。

## 数据如何从数据库回到对象

导入完成后，还需要确认这些数据会不会重新进入运行时对象。先看工具加载逻辑。

```
def load_tools():
    rows = load_entities('tool')
    tools = []
    for row in rows:
        data = row[1]
        tool_class = TOOL_CLASSES[data['name']]
        tool = tool_class(tool_id=row[0])
        tool.set_parameters(**data['parameters'])
        tools.append(tool)
    return tools
```

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP853qWhcH8icLWFric8oTnibv3c7qMC2sEzO3iaz8KibbJ1hj12TNaHQj0MCFzXEvhnL6JiaShewUVdZ0ACSu1xqPReAqsWLEShlaPLxjM/640?wx_fmt=png&from=appmsg)

这段代码做了两件关键的事：

1. 用数据库里的 `data["name"]` 从 `TOOL_CLASSES` 中选择工具类。
2. 把数据库里的 `data["parameters"]` 重新设置回工具对象。

因此，只要 JSON 中的 tool 写成 `CustomApiTool`，并且 parameters 中有 `headers`，后续内存对象就会带着这个 payload。

接着看 Agent 加载。`load_agents()` 会先加载所有工具，再根据 `tool_ids` 把工具挂回 Agent。

```
def load_agents():
    from my_agent import MyAgent
    rows = load_entities('agent')
    tools_dict = {tool.tool_id: tool for tool in load_tools()}
    agents = []
    for row in rows:
        data = row[1]
        tool_ids = data.pop('tool_ids', [])
        knowledge_source_ids = data.pop('knowledge_source_ids', [])
        agent = MyAgent(id=row[0], knowledge_source_ids=knowledge_source_ids, **data)
        agent.tools = [tools_dict[tool_id] for tool_id in tool_ids if tool_id in tools_dict]
        agents.append(agent)
    return sorted(agents, key=lambda x: x.created_at)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4yRoMuNP851baWcyE6XiaJQ35AmicKQFFIMDyLvpqyicRA7RyOR2TXlNSa9PKNpOgqCCWwWPXibIIIicL5Nz9icSxC3EfLhy4QiaWztibgh2QgylW6E/640?wx_fmt=png&from=appmsg)

这也是后面 POC JSON 中 Agent 必须写 `tool_ids: ["POC_TOOL_EVAL"]` 的原因。没有这一步，恶意工具虽然进了数据库，但不会被 Agent 使用。

再看 Crew 加载。`load_crews()` 会根据 `agent_ids` 和 `task_ids` 把 Agent、Task 重新拼回 Crew。

```
def load_crews():
    from my_crew import MyCrew
    rows = load_entities('crew')
    agents_dict = {agent.id: agent for agent in load_agents()}
    tasks_dict = {task.id: task for task in load_tasks()}
    crews = []
    for row in rows:
        data = row[1]
        crew = MyCrew(
            id=row[0],
            name=data['name'],
            process=data['process'],
            verbose=data['verbose'],
            created_at=data['created_at'],
            memory=data.get('memory'),
            cache=data.get('cache'),
            planning=data.get('planning'),
            planning_llm=data.get('planning_llm'),
            max_rpm=data.get('max_rpm'),
            manager_llm=data.get('manager_llm'),
            manager_agent=agents_dict.get(data.get('manager_agent_id')),
            knowledge_source_ids=data.get('knowledge_source_ids', [])
        )
        crew.agents = [agents_dict[agent_id] for agent_id in data['agent_ids'] if agent_id in agents_dict]
        crew.tasks = [tasks_dict[task_id] for task_id in data['task_ids'] if task_id in tasks_dict]
        crews.append(crew)
    return sorted(crews, key=lambda x: x.created_at)
```

![](https://mmbiz.qpic.cn/mmbiz_png/4yRoMuNP853wI23aYLyVibqegPINlib5gd8RacT0tuCNLGvAqI8KrDD7ic2RxfIOLZTQmibahZNCxj6iacU5Zic9J7gygQ2XW649l5aKAs3tgEVz4/640?wx_fmt=png&from=appmsg)

只有它们串起来，页面上才会出现一个可运行的 `POC eval headers`。 这也就是 POC JSON 中为什么要有 `crew`、`agent`、`task` 三类实体的原因。

## 运行时如何触发

数据已经进了数据库，也能回到对象里，下一步就要看运行按钮会触发什么。

Kickoff 页面中，点击运行后会调用 `selected_crew.get_crewai_crew(full_output=True)`。

```
def control_buttons(self, selected_crew):
    if st.button(t('crew_run.run_button'), disabled=not selected_crew.is_valid() or ss.running):
        inputs = {key.split('_')[1]: value for key, value in ss.placeholders.items()}
        ss.result = None

        try:
            crew = ...