---
title: [译] Anthropic 是如何构建 Multi-Agent Research 系统的（2025）
url: https://arthurchiao.github.io/blog/built-multi-agent-research-system-zh/
source: ArthurChiao's Blog
date: 2025-07-21
fetch_date: 2025-10-06T23:18:33.270795
---

# [译] Anthropic 是如何构建 Multi-Agent Research 系统的（2025）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (дёӯж–Ү)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [иҜ‘] Anthropic жҳҜеҰӮдҪ•жһ„е»ә Multi-Agent Research зі»з»ҹзҡ„пјҲ2025пјү

Published at 2025-07-20 | Last Update 2025-07-20

жң¬ж–Үзҝ»иҜ‘иҮӘ 2025 е№ҙ Anthropic зҡ„дёҖзҜҮж–Үз«
[Built a Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system)гҖӮ

ж–Үз« д»Ӣз»ҚдәҶд»–д»¬зҡ„ [Research еҠҹиғҪ](https://www.anthropic.com/news/research) иғҢеҗҺзҡ„ multi-agent зі»з»ҹпјҢ
д»ҘеҸҠеңЁжһ„е»әиҜҘзі»з»ҹзҡ„иҝҮзЁӢдёӯ**йҒҮеҲ°зҡ„е·ҘзЁӢжҢ‘жҲҳдёҺеӯҰеҲ°зҡ„з»ҸйӘҢ**гҖӮ

иҝҷеҘ— Multi-Agent зі»з»ҹжңҖж ёеҝғзҡ„йғЁеҲҶд№ӢдёҖ вҖ”вҖ” Agent **`prompts`** вҖ”вҖ” д№ҹејҖжәҗеҮәжқҘдәҶпјҢи§Ғжң¬ж–Үйҷ„еҪ•йғЁеҲҶпјҢ
еҜ№еӯҰд№ зҗҶи§Ј agent planning & task delegation йқһеёёжңүз”ЁпјҢз”ҡиҮіжҜ”ж–Үз« жң¬иә«иҝҳе®һз”ЁгҖӮ

ж°ҙе№іеҸҠз»ҙжҠӨзІҫеҠӣжүҖйҷҗпјҢиҜ‘ж–ҮдёҚе…ҚеӯҳеңЁй”ҷиҜҜжҲ–иҝҮж—¶д№ӢеӨ„пјҢеҰӮжңүз–‘й—®пјҢиҜ·жҹҘйҳ…еҺҹж–ҮгҖӮ
**дј ж’ӯзҹҘиҜҶпјҢе°ҠйҮҚеҠіеҠЁпјҢе№ҙж»ЎеҚҒе…«е‘ЁеІҒпјҢиҪ¬иҪҪиҜ·жіЁжҳҺ[еҮәеӨ„](https://arthurchiao.art)**гҖӮ

---

* [1 еј•иЁҖ](#1-еј•иЁҖ)
  + [1.1 Agent & Multi-Agent е®ҡд№ү](#11-agent--multi-agent-е®ҡд№ү)
  + [1.2 Agent еҫҲйҖӮеҗҲеӣһзӯ”ејҖж”ҫејҸй—®йўҳ](#12-agent-еҫҲйҖӮеҗҲеӣһзӯ”ејҖж”ҫејҸй—®йўҳ)
  + [1.3 дёәд»Җд№ҲйңҖиҰҒ Multi-Agent зі»з»ҹ](#13-дёәд»Җд№ҲйңҖиҰҒ-multi-agent-зі»з»ҹ)
  + [1.4 Multi-Agent жңүж•ҲжҖ§зҡ„е…ій”®пјҡиҠұдәҶи¶іеӨҹеӨҡзҡ„ token](#14-multi-agent-жңүж•ҲжҖ§зҡ„е…ій”®иҠұдәҶи¶іеӨҹеӨҡзҡ„-token)
  + [1.5 Multi-Agent зі»з»ҹзҡ„зјәзӮ№](#15-multi-agent-зі»з»ҹзҡ„зјәзӮ№)
* [2 жһ¶жһ„жҰӮи§Ҳ](#2-жһ¶жһ„жҰӮи§Ҳ)
  + [2.1 жһ¶жһ„пјҡOrchestrator-Worker](#21-жһ¶жһ„orchestrator-worker)
  + [2.2 зӣёжҜ”дј з»ҹ RAG](#22-зӣёжҜ”дј з»ҹ-rag)
  + [2.3 е·ҘдҪңжөҒ](#23-е·ҘдҪңжөҒ)
* [3 йқўеҗ‘ Agent зҡ„жҸҗзӨәиҜҚе·ҘзЁӢ](#3-йқўеҗ‘-agent-зҡ„жҸҗзӨәиҜҚе·ҘзЁӢ)
  + [3.1 еғҸ Agent дёҖж ·жҖқиҖғ](#31-еғҸ-agent-дёҖж ·жҖқиҖғ)
  + [3.2 дё»жҺ§ Agent еҗҲзҗҶдёӢеҸ‘е·ҘдҪңпјҲhow to delegateпјү](#32-дё»жҺ§-agent-еҗҲзҗҶдёӢеҸ‘е·ҘдҪңhow-to-delegate)
  + [3.3 жҹҘиҜўеӨҚжқӮеәҰ vs. е·ҘдҪңйҮҸеҢәй—ҙ (Scale effort to query complexity)](#33-жҹҘиҜўеӨҚжқӮеәҰ-vs-е·ҘдҪңйҮҸеҢәй—ҙ-scale-effort-to-query-complexity)
  + [3.4 Tool зҡ„и®ҫи®Ўе’ҢйҖүжӢ©иҮіе…ійҮҚиҰҒ](#34-tool-зҡ„и®ҫи®Ўе’ҢйҖүжӢ©иҮіе…ійҮҚиҰҒ)
  + [3.5 и®© Agent иҮӘжҲ‘ж”№иҝӣ](#35-и®©-agent-иҮӘжҲ‘ж”№иҝӣ)
  + [3.6 жҗңзҙўзӯ–з•Ҙпјҡз”ұе®ҪжіӣеҲ°е…·дҪ“ (Start wide, then narrow down)](#36-жҗңзҙўзӯ–з•Ҙз”ұе®ҪжіӣеҲ°е…·дҪ“-start-wide-then-narrow-down)
  + [3.7 еј•еҜј Agent жҖқиҖғиҝҮзЁӢ (Guide the thinking process)](#37-еј•еҜј-agent-жҖқиҖғиҝҮзЁӢ-guide-the-thinking-process)
  + [3.8 е№¶иЎҢ Tool и°ғз”ЁпјҢжҸҗеҚҮйҖҹеәҰе’ҢжҖ§иғҪ](#38-е№¶иЎҢ-tool-и°ғз”ЁжҸҗеҚҮйҖҹеәҰе’ҢжҖ§иғҪ)
* [4 Agent ж•ҲжһңиҜ„дј°](#4-agent-ж•ҲжһңиҜ„дј°)
  + [4.1 е°Ҫж—©пјҲдҪҝз”Ёе°Ҹж ·жң¬пјүејҖе§ӢиҜ„дј°](#41-е°Ҫж—©дҪҝз”Ёе°Ҹж ·жң¬ејҖе§ӢиҜ„дј°)
  + [4.2 LLM дҪңдёәиЈҒеҲӨзҡ„ж–№ејҸжү©еұ•жҖ§еҫҲеҘҪ (LLM-as-judge evaluation scales)](#42-llm-дҪңдёәиЈҒеҲӨзҡ„ж–№ејҸжү©еұ•жҖ§еҫҲеҘҪ-llm-as-judge-evaluation-scales)
  + [4.3 дәәе·ҘиҜ„дј°жҚ•жҚүиҮӘеҠЁеҢ–йҒ—жјҸзҡ„й—®йўҳ](#43-дәәе·ҘиҜ„дј°жҚ•жҚүиҮӘеҠЁеҢ–йҒ—жјҸзҡ„й—®йўҳ)
* [5 з”ҹдә§йғЁзҪІпјҡзі»з»ҹеҸҜйқ жҖ§дёҺе·ҘзЁӢжҢ‘жҲҳ](#5-з”ҹдә§йғЁзҪІзі»з»ҹеҸҜйқ жҖ§дёҺе·ҘзЁӢжҢ‘жҲҳ)
  + [5.1 Agent жҳҜжңүзҠ¶жҖҒзҡ„пјҢй”ҷиҜҜдјҡзҙҜз§Ҝ](#51-agent-жҳҜжңүзҠ¶жҖҒзҡ„й”ҷиҜҜдјҡзҙҜз§Ҝ)
  + [5.2 и°ғиҜ•](#52-и°ғиҜ•)
  + [5.3 жңҚеҠЎеҸ‘еёғж–№ејҸпјҡrainbow deployments](#53-жңҚеҠЎеҸ‘еёғж–№ејҸrainbow-deployments)
  + [5.4 еҗҢжӯҘжү§иЎҢйҖ жҲҗз“¶йўҲ](#54-еҗҢжӯҘжү§иЎҢйҖ жҲҗз“¶йўҲ)
* [6 е…¶д»–жҠҖе·§](#6-е…¶д»–жҠҖе·§)
  + [6.1 зҠ¶жҖҒйҡҸж—¶й—ҙеҸҳеҢ–зҡ„ AgentпјҡиҝӣиЎҢжңҖз»ҲзҠ¶жҖҒиҜ„дј°](#61-зҠ¶жҖҒйҡҸж—¶й—ҙеҸҳеҢ–зҡ„-agentиҝӣиЎҢжңҖз»ҲзҠ¶жҖҒиҜ„дј°)
  + [6.2 й•ҝи·ЁеәҰпјҲи¶…иҝҮдёҠдёӢж–ҮзӘ—еҸЈйҷҗеҲ¶пјүеҜ№иҜқз®ЎзҗҶ](#62-й•ҝи·ЁеәҰи¶…иҝҮдёҠдёӢж–ҮзӘ—еҸЈйҷҗеҲ¶еҜ№иҜқз®ЎзҗҶ)
  + [6.3 sub-agent иҫ“еҮәеҲ°ж–Үд»¶зі»з»ҹпјҢжңҖе°ҸеҢ–вҖңдј иҜқејҖй”ҖвҖқ](#63-sub-agent-иҫ“еҮәеҲ°ж–Үд»¶зі»з»ҹжңҖе°ҸеҢ–дј иҜқејҖй”Җ)
* [7 жҖ»з»“](#7-жҖ»з»“)
* [иҮҙи°ў](#иҮҙи°ў)
* [йҷ„еҪ•](#йҷ„еҪ•)
  + [**Lead Agent жҸҗзӨәиҜҚ**](#lead-agent-жҸҗзӨәиҜҚ)
    - [`<research_process>`](#research_process)
      * [1. Assessment and breakdown](#1-assessment-and-breakdown)
      * [2. Query type determination](#2-query-type-determination)
      * [3. Detailed research plan development](#3-detailed-research-plan-development)
      * [4. Methodical plan execution](#4-methodical-plan-execution)
    - [`<subagent_count_guidelines>`](#subagent_count_guidelines)
      * [1. Simple/Straightforward queries: create 1 subagent](#1-simplestraightforward-queries-create-1-subagent)
      * [2. Standard complexity queries: 2-3 subagents.](#2-standard-complexity-queries-2-3-subagents)
      * [3. Medium complexity queries: 3-5 subagents.](#3-medium-complexity-queries-3-5-subagents)
      * [4. High complexity queries: 5-10 subagents (maximum 20).](#4-high-complexity-queries-5-10-subagents-maximum-20)
    - [`<delegation_instructions>`](#delegation_instructions)
      * [1. Deployment strategy](#1-deployment-strategy)
      * [2. Task allocation principles](#2-task-allocation-principles)
      * [3. Clear direction for subagents](#3-clear-direction-for-subagents)
      * [4. Synthesis responsibility](#4-synthesis-responsibility)
    - [`<answer_formatting>`](#answer_formatting)
    - [`<use_available_internal_tools>`](#use_available_internal_tools)
    - [`<use_parallel_tool_calls>`](#use_parallel_tool_calls)
    - [`<important_guidelines>`](#important_guidelines)
  + [**subagent жҸҗзӨәиҜҚ**](#subagent-жҸҗзӨәиҜҚ)
    - [`<research_process>`](#research_process-1)
      * [1. Planning](#1-planning)
      * [2. Tool selection](#2-tool-selection)
      * [3. Research loop](#3-research-loop)
    - [`<research_guidelines>`](#research_guidelines)
    - [`<think_about_source_quality>`](#think_about_source_quality)
    - [`<use_parallel_tool_calls>`](#use_parallel_tool_calls-1)
    - [`<maximum_tool_call_limit>`](#maximum_tool_call_limit)
  + [**citation agent жҸҗзӨәиҜҚ**](#citation-agent-жҸҗзӨәиҜҚ)
    - [Rules](#rules)
    - [Citation guidelines](#citation-guidelines)
    - [Technical requirements](#technical-requirements)

---

жң¬ж–ҮеҲҶдә« Multi-Agent Research зі»з»ҹд»ҺеҺҹеһӢеҲ°з”ҹдә§зҡ„иҝҮзЁӢдёӯпјҢеңЁзі»з»ҹжһ¶жһ„гҖҒTool и®ҫи®Ўе’ҢжҸҗзӨәиҜҚе·ҘзЁӢж–№йқўеӯҰеҲ°зҡ„з»ҸйӘҢгҖӮ

# 1 еј•иЁҖ

## 1.1 Agent & Multi-Agent е®ҡд№ү

жң¬ж–Үзҡ„ вҖңAgentвҖқ е®ҡд№үпјҡ**еңЁдёҖдёӘд»Јз ҒеҫӘзҺҜ**пјҲ`while(){ }`пјүдёӯ
**иҮӘдё»йҖүжӢ©е’ҢдҪҝз”Ёе·Ҙе…·**пјҲ`Tools`пјүзҡ„**еӨ§иҜӯиЁҖжЁЎеһӢ**пјҲ`LLM`пјүгҖӮ

жң¬ж–Үзҡ„ Multi-Agent зі»з»ҹз”ұеӨҡдёӘд»ҘдёҠзҡ„ Agent з»„жҲҗпјҲе…·дҪ“еҸҲеҲҶдёә Lead Agent е’Ң sub-agentпјүпјҢеҚҸеҗҢе·ҘдҪңе®ҢжҲҗдёҖйЎ№еӨҚжқӮд»»еҠЎгҖӮ

## 1.2 Agent еҫҲйҖӮеҗҲеӣһзӯ”ејҖж”ҫејҸй—®йўҳ

Research жҳҜејҖж”ҫејҸй—®йўҳпјҢж— жі•жҸҗеүҚйў„жөӢжүҖйңҖжӯҘйӘӨпјҢеӣ дёә**иҝҮзЁӢжң¬иҙЁдёҠжҳҜеҠЁжҖҒдё”и·Ҝеҫ„дҫқиө–зҡ„**гҖӮ

дәәиҝӣиЎҢ research ж—¶пјҢеҫҖеҫҖжҳҜдёҖжӯҘжӯҘжқҘзҡ„пјҢж №жҚ®жҜҸдёӘйҳ¶ж®өзҡ„еҸ‘зҺ°жқҘжӣҙж–°иҮӘе·ұжҺҘдёӢжқҘиҰҒеҒҡзҡ„дәӢжғ…гҖӮ

Agent жЁЎжӢҹзҡ„жҳҜдәәзұ»иЎҢдёәгҖӮжЁЎеһӢеңЁеӨҡиҪ®иҝӯд»ЈдёӯиҮӘдё»иҝҗиЎҢпјҢж №жҚ®дёӯй—ҙз»“жһңеҶіе®ҡдёӢдёҖжӯҘж–№еҗ‘гҖӮ

## 1.3 дёәд»Җд№ҲйңҖиҰҒ Multi-Agent зі»з»ҹ

жҗңзҙўзҡ„жң¬иҙЁжҳҜеҺӢзј©пјҡд»Һжө·йҮҸиҜӯж–ҷдёӯжҸҗзӮје…ій”®дҝЎжҒҜгҖӮ

* еӨҡдёӘ sub-agent е№¶иЎҢиҝҗиЎҢпјҲжӢҘжңүзӢ¬з«Ӣзҡ„дёҠдёӢж–ҮзӘ—еҸЈпјүпјҢжҺўзҙўеҗҢдёҖй—®йўҳзҡ„дёҚеҗҢж–№йқўпјҢжңҖеҗҺе°ҶжңҖйҮҚиҰҒзҡ„дҝЎжҒҜпјҲtokensпјүеҺӢзј©з»ҷеҲ° Lead AgentгҖӮ
* жҜҸдёӘ sub-agent еҸҜд»ҘдҪҝз”ЁдёҚеҗҢзҡ„ Tool е’ҢжҸҗзӨәиҜҚпјҢжңүдёҚеҗҢзҡ„жҺўзҙўиҪЁиҝ№пјҢд»ҺиҖҢеҮҸе°‘и·Ҝеҫ„дҫқиө–пјҢе®һзҺ°ж·ұе…ҘиҖҢзӢ¬з«Ӣзҡ„з ”з©¶гҖӮ

еңЁиҝҮеҺ» 10 дёҮе№ҙйҮҢпјҢиҷҪз„¶еҚ•дёӘдәәзҡ„жҷәеҠӣеңЁйҖҗжӯҘжҸҗеҚҮпјҢдҪҶ**дәәзұ»зӨҫдјҡйӣҶдҪ“жҷәиғҪе’ҢеҚҸи°ғиғҪеҠӣзҡ„жҢҮж•°зә§еўһй•ҝ**пјҢеҚҙжҳҜ**жқҘиҮӘдәәзұ»йӣҶдҪ“иҖҢйқһе°‘ж•°дёӘдәә**гҖӮ
Agent д№ҹжҳҜзұ»дјјпјҢдёҖж—ҰеҚ•дёӘ Agent зҡ„жҷәиғҪиҫҫеҲ°жҹҗдёӘйҳҲеҖјпјҲз“¶йўҲпјүпјҢMulti-Agent зі»з»ҹе°ұжҲҗдёәжҸҗеҚҮжҖ§иғҪзҡ„е…ій”®ж–№ејҸгҖӮ

дҫӢеҰӮпјҢжҲ‘д»¬зҡ„еҶ…йғЁиҜ„дј°иЎЁжҳҺпјҢ

* Multi-Agent Research зі»з»ҹе°Өе…¶ж“…й•ҝ**е№ҝеәҰдјҳе…ҲжҹҘиҜў**пјҢеҚіеҗҢж—¶иҝҪиёӘеӨҡдёӘзӢ¬з«Ӣж–№еҗ‘гҖӮ
* д»Ҙ Lead Agent з”Ё Claude Opus 4гҖҒsub-agents з”Ё Claude Sonnet 4 зҡ„ Multi-Ag...