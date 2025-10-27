---
title: LoRA微调简介
url: http://terenceli.github.io/%E6%8A%80%E6%9C%AF/2025/07/05/lora-introduction
source: 不忘初心 方得始终
date: 2025-07-06
fetch_date: 2025-10-06T23:25:58.755074
---

# LoRA微调简介

[õĖŹÕ┐śÕłØÕ┐ā µ¢╣ÕŠŚÕ¦ŗń╗ł](/)

* [Archive](/archive.html)
* [About Me](/aboutMe.html)
* [Pages](/pages.html)
* [Tags](/tags.html)
* [Categories](/categories.html)

# LoRAÕŠ«Ķ░āń«Ćõ╗ŗ

2025-07-05

## Õż¦µ©ĪÕ×ŗÕŠ«Ķ░āń«Ćõ╗ŗ

ÕŠ«Ķ░ā’╝ī µīćÕ£©õĖĆõĖ¬ÕĘ▓ń╗ÅķóäĶ«Łń╗āÕźĮńÜäÕż¦µ©ĪÕ×ŗÕ¤║ńĪĆõĖŖ’╝īõĮ┐ńö©õĖĆõĖ¬ńē╣Õ«Üõ╗╗ÕŖĪµł¢ķóåÕ¤¤ńÜäĶŠāÕ░ÅĶ¦äµ©ĪµĢ░µŹ«ķøå’╝īÕ»╣Ķ»źµ©ĪÕ×ŗĶ┐øĶĪīĶ┐øõĖĆµŁźńÜäĶ«Łń╗ā’╝īĶ«®ķĆÜńö©ńÜäŌĆ£ķĆÜµēŹŌĆØµ©ĪÕ×ŗ’╝īÕ┐½ķĆ¤ŃĆüķ½śµĢłÕ£░ĶĮ¼ÕÅśµłÉõĖĆõĖ¬ńē╣Õ«Üõ╗╗ÕŖĪńÜäŌĆ£õĖōµēŹŌĆØµ©ĪÕ×ŗ’╝īĶĆīõĖŹķ£ĆĶ”üõ╗ÄÕż┤Õ╝ĆÕ¦ŗĶ«Łń╗āŃĆé

µ»öÕ”éÕÄ¤Õ¦ŗńÜäGPTµ©ĪÕ×ŗ’╝īÕģČÕ«×ÕÅ¬µś»õĖĆõĖ¬ķóäµĄŗõĖŗõĖĆõĖ¬tokenµ”éńÄćńÜäµ©ĪÕ×ŗ’╝īĶ”üĶ«®ÕģČµłÉõĖ║ĶüŖÕż®µ£║ÕÖ©õ║║’╝īĶ┐śĶ”üńö©µĢ░µŹ«Õ»╣ķĮÉĶ┐øĶĪīÕŠ«Ķ░āŃĆé

ÕŠ«Ķ░āńÜäÕ¤║µ£¼µ”éÕ┐ĄÕ”éõĖŗŃĆé

![](/assets/img/loraintro/1.png)

õĖŗķØóµś»deepseekńö¤µłÉńÜäõ╝¬õ╗ŻńĀü’╝īÕģČµĀĖÕ┐āĶ┐ćń©ŗÕ”éõĖŗ’╝Ü

* ÕłØÕ¦ŗÕī¢’╝īÕŖĀĶĮĮÕĘ▓ń╗Åń╗ÅĶ┐ćķóäĶ«Łń╗āńÜäÕż¦µ©ĪÕ×ŗ’╝īµ»öÕ”éÕÉäõĖ¬Õż¦Õģ¼ÕÅĖńÜäµ©ĪÕ×ŗ
* ÕćåÕżćµĢ░µŹ«ķøå’╝īÕćåÕżćńö©µØźÕŠ«Ķ░āńÜäµĢ░µŹ«’╝īµ»öÕ”éÕ»╣õ║ÄĶüŖÕż®ńÜäÕż¦µ©ĪÕ×ŗ’╝īÕ░▒µś»ÕÉäõĖ¬ĶüŖÕż®µĢ░µŹ«
* ķģŹńĮ«ÕÅéµĢ░’╝īµ»öÕ”éµø┤µ¢░ÕÅéµĢ░ńÜäµ¢╣Õ╝Åõ╗źÕÅŖµŹ¤Õż▒ÕćĮµĢ░ńÜäĶ«Īń«Ś
* Ķ«Łń╗ā’╝īĶ┐ÖķćīńÜäĶ«Łń╗āµŖŖµĢ░µŹ«ķøåõĖŁńÜäµĀĘµ£¼õĮ£õĖ║ĶŠōÕģź’╝īĶĄ░õĖĆķüŹµ©ĪÕ×ŗńÜäµÄ©ńÉå’╝īńäČÕÉÄµŖŖµ©ĪÕ×ŗńÜäń╗ōµ×£õĖÄµĀĘµ£¼ńÜäµĀćńŁŠĶ«Īń«ŚµŹ¤Õż▒ÕćĮµĢ░’╝īÕüÜĶ┐öńÄ░õ╝ĀµÆŁõ╗ÄĶĆīµø┤µ¢░µ©ĪÕ×ŗńÜäÕÅéµĢ░
* µ£Ćń╗łµŖŖµ©ĪÕ×ŗÕÅéµĢ░õ┐ØÕŁśĶĄĘµØź’╝īÕ«īµłÉõ║åõĖĆµ¼ĪÕŠ«Ķ░ā

```
# ========== ÕłØÕ¦ŗÕī¢ķśČµ«Ą ==========
# ÕŖĀĶĮĮķóäĶ«Łń╗āńÜäÕż¦µ©ĪÕ×ŗ
pretrained_model = load_model("LLaMA-3")  # õŠŗÕ”é: GPT, BERT, LLaMAńŁē
pretrained_model.freeze_weights()        # Õ»╣õ║ÄÕÅéµĢ░ķ½śµĢłÕŠ«Ķ░ā(PEFT)’╝īÕå╗ń╗ōÕ¤║ńĪĆµØāķćŹ

# ÕćåÕżćÕŠ«Ķ░āµĢ░µŹ«ķøå
finetune_dataset = load_dataset(
    path="domain_specific_data.csv",     # ńē╣Õ«ÜķóåÕ¤¤/õ╗╗ÕŖĪńÜäµĢ░µŹ«
    format="input-target"                # ĶŠōÕģź-ńø«µĀćĶŠōÕć║Õ»╣
)

# ķģŹńĮ«Ķ«Łń╗āÕÅéµĢ░
optimizer = AdamW(
    params=pretrained_model.trainable_params,  # õ╗ģµø┤µ¢░ÕÅ»Ķ«Łń╗āÕÅéµĢ░
    lr=2e-5,                           # ĶŠāÕ░ÅńÜäÕŁ”õ╣ĀńÄć
    weight_decay=0.01
)
loss_function = CrossEntropyLoss()
scheduler = CosineAnnealingLR(optimizer, T_max=100)

# ========== ÕŠ«Ķ░āĶ«Łń╗āÕŠ¬ńÄ» ==========
for epoch in range(num_epochs):
    for batch in finetune_dataloader:
        # ÕēŹÕÉæõ╝ĀµÆŁ
        inputs, targets = batch
        outputs = pretrained_model(inputs)

        # Ķ«Īń«ŚµŹ¤Õż▒
        loss = loss_function(outputs, targets)

        # ÕÅŹÕÉæõ╝ĀµÆŁ
        loss.backward()

        # µó»Õ║”ĶŻüÕē¬ (ķś▓µŁóµó»Õ║”ńłåńéĖ)
        torch.nn.utils.clip_grad_norm_(pretrained_model.parameters(), 1.0)

        # ÕÅéµĢ░µø┤µ¢░
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

        # µŚźÕ┐ŚĶ«░ÕĮĢ
        log_metrics(loss, accuracy)

# ========== õ║¦Õć║ķśČµ«Ą ==========
# õ┐ØÕŁśÕŠ«Ķ░āÕÉÄńÜäµ©ĪÕ×ŗ
finetuned_model = pretrained_model
save_model(finetuned_model, "legal_assistant_model.pth")

# ķā©ńĮ▓Õ║öńö©
deployment = ModelDeployment(finetuned_model)
deployment.serve(endpoint="/api/legal-assistant")
```

õĖŖķØóÕ¤║µ£¼µś»Õģ©ķćÅÕŠ«Ķ░āńÜäµ¢╣µĪł’╝īÕģ©ķćÅÕŠ«Ķ░āÕĮōńäČĶāĮÕż¤µÅÉķ½śµ©ĪÕ×ŗÕ£©ńē╣Õ«ÜķóåÕ¤¤ńÜäĶĪ©ĶŠŠÕŖø’╝īõĮåµś»Õ«āńÜäń╝║ńé╣õ╣¤ÕŠłµśÄµśŠ’╝īĶ«Łń╗āµłÉµ£¼ķ½śŃĆüµŚČķŚ┤ķĢ┐ŃĆüķ£ĆĶ”üÕż¦ķćÅńÜäÕŁśÕé©ń®║ķŚ┤’╝łµā│µā│ÕŖ©ĶŠäÕćĀÕŹüŃĆüõĖŖńÖŠõ║┐ńÜäÕÅéµĢ░ķāĮĶ”üõ┐ØÕŁśÕł░GPUµśŠÕŁśõĖŁ)ŃĆé

µēĆõ╗źµ£ēõ║åÕÉäń¦ŹÕŠ«Ķ░āńÜäõ╝śÕī¢’╝īĶ┐Öķćīõ╗ŗń╗ŹLoRAÕŠ«Ķ░āŃĆé

## LoRA ÕŠ«Ķ░āń«Ćõ╗ŗ

LoRA([LORA: LOW-RANK ADAPTATION OF LARGE LANGUAGE MODELS](https://arxiv.org/pdf/2106.09685))õĖŁµ¢ćÕÅ½ÕüÜõĮÄń¦®ķĆéķģŹŃĆéLoRAńÜäµĀĖÕ┐āµĆØµā│Õ£©õĖŗÕÅ│ÕøŠ’╝Ü

![](/assets/img/loraintro/2.png)

LoRAµĀĖÕ┐āµĆØĶĘ»Õ”éõĖŗ’╝Ü

* Õ£©ķóäĶ«Łń╗āµ©ĪÕ×ŗ(PLM, Pre-trained Language Model)ńÜäÕÅéµĢ░µŚüĶŠ╣Õó×ÕŖĀõĖĆõĖ¬µŚüĶĘ»’╝īÕüÜõĖĆõĖ¬ÕģłķÖŹń╗┤ŃĆüÕåŹÕŹćń╗┤ńÜäµōŹõĮ£
* Ķ«Łń╗āńÜäµŚČÕĆÖÕø║Õ«ÜPLMńÜäÕÅéµĢ░’╝īÕÅ¬Ķ«Łń╗āķÖŹń╗┤ÕÆīÕŹćń╗┤ń¤®ķśĄAÕÆīB’╝īÕ£©ĶŠōÕć║µŚČ’╝īÕ░åĶŠōÕģźõĖÄPLMÕÆīABń¤®ķśĄńÜäõ╣śń¦»ńøĖÕŖĀ
* AńÜäÕłØÕ¦ŗÕī¢ńö©ķÜÅµ£║ķ½śµ¢»ÕłåÕĖā’╝īBńÜäÕłØÕ¦ŗÕī¢ńö©0ń¤®ķśĄŃĆé

õĖŖÕøŠÕĘ”õŠ¦µś»Õģ©ķćÅÕŠ«Ķ░āńÜäõŠŗÕŁÉ’╝īÕģČõĖŁÕÅéµĢ░ \(W\_{0} \in R^{d\times d}\) µś»Õż¦µ©ĪÕ×ŗńÜäķóäĶ«Łń╗āµØāķćŹ’╝ī\(\bigtriangleup W\) µś»ÕŠ«Ķ░āńÜäµØāķćŹ’╝īĶ┐ÖµĀĘµŗåÕłåµś»ÕøĀõĖ║Õ£©ÕŠ«Ķ░āĶ┐ćń©ŗõĖŁ \(W\_{0}\) Ķó½Õø║Õ«Üõ║å’╝īÕÅ¬µö╣ÕÅś \(\bigtriangleup W\)’╝īÕÅ»õ╗źń£ŗÕł░Õ£©Õģ©ķćÅÕŠ«Ķ░āõĖŁ’╝ī\(\bigtriangleup W\) ńÜäÕż¦Õ░Åµś»ńŁēõ║Ä \(\bigtriangleup W\)’╝īķĆÜÕĖĖķāĮµś»ķØ×ÕĖĖÕż¦ńÜä’╝ī\(d\times d\) ŃĆé

ÕÅ│õŠ¦ÕłÖµś»LoRAõĖŁÕŠ«Ķ░ā’╝īÕģČÕŠ«Ķ░āĶ┐ćń©ŗÕÅśµłÉõ║å’╝īńÄ░Õ░åĶŠōÕģźķĆÜĶ┐ćń¤®ķśĄAķÖŹń╗┤’╝ī\(A\in R^{d\times r}\)’╝īrÕ£©Ķ┐ÖķćīµłÉõĖ║ń¦®’╝īµś»õĖĆõĖ¬µ»öĶŠāÕ░ÅńÜäÕĆ╝’╝īńäČÕÉÄÕåŹķĆÜĶ┐ćõĖĆõĖ¬ń¤®ķśĄBÕŹćń╗┤’╝ī\(B\in R^{r\times d}\)’╝īÕÅ»õ╗źń£ŗÕł░ĶŠōÕģźxń╗ÅĶ┐ćABõ╣ŗÕÉÄ’╝īĶŠōÕć║ $ \bigtriangleup W \(õŠØńäČµś»\) d\times d \(,µŁżµŚČÕ░å\) \bigtriangleup W \(ÕÆī\) W\_{0} $$ ńøĖÕŖĀõŠØńäČÕ»╣Ķ»źÕ▒éĶ┐øĶĪīõ║åÕŠ«Ķ░āŃĆé

Ķ┐ÖķćīńÜäµĀĖÕ┐āµś»rĶ┐£Õ░Åõ║Äd’╝īÕüćĶ«Šdµś»100’╝īÕłÖÕģ©ķćÅÕŠ«Ķ░āķ£ĆĶ”üµø┤µ¢░ \(d\times d\) Õģ▒10000õĖ¬ÕÅéµĢ░’╝īõĮåµś»Õ”éµ×£rĶ«ŠńĮ«õĖ║8’╝īÕłÖÕÅ¬ķ£ĆĶ”üµø┤µ¢░ \(2\times r\times d\) Õģ▒1600õĖ¬ÕÅéµĢ░ŃĆé

Ķć│õ║ÄĶ┐ÖõĖ¬õĖ║ÕĢźĶāĮwork’╝īÕÅłµś»Õ¤║õ║ÄÕēŹõ║║ńÜäintrinsic dimensionńĀöń®Č’╝īÕż¦µ”éńÜäµäÅµĆØÕ░▒µś»ÕÅéµĢ░ńÜäńē╣ÕŠüõĮŹõ║ÄõĖĆõĖ¬õĮÄń╗┤ńÜäÕŁÉń®║ķŚ┤õĖŁŃĆé

Ķ«║µ¢ćõ╣¤µ▓Īń£ŗ’╝īńø┤µÄźµØźÕ«×ĶĘĄõĮōõ╝ÜõĖĆõĖŗŃĆé

## LoRAÕŠ«Ķ░āÕ«×ĶĘĄ

Ķ┐Öķćīµłæõ╗¼ÕŠ«Ķ░āQwen2-0.5B-Instructµ©ĪÕ×ŗŃĆéµ▓Īµ£ēÕŠ«Ķ░āõ╣ŗÕēŹ’╝īķŚ«Qwenµ©ĪÕ×ŗŌĆ£õĮĀµś»Ķ░ü’╝¤ŌĆØ’╝īÕÅ»õ╗źń£ŗÕł░ÕģČĶŠōÕć║µś»ÕŠłµŁŻÕĖĖńÜäŃĆé

```
from transformers import AutoTokenizer,AutoModelForCausalLM,DataCollatorForSeq2Seq,Trainer,TrainingArguments
from datasets import load_dataset
from peft import LoraConfig,TaskType,get_peft_model
from peft import PeftModel

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct",low_cpu_mem_usage=True)

ipt = tokenizer("Human: {}\n{}".format("õĮĀµś»Ķ░ü’╝¤", "").strip() + "\n\nAssistant: ", return_tensors="pt").to(model.device)
re = tokenizer.decode(model.generate(**ipt,max_length=256,do_sample=False)[0],skip_special_tokens=True)
print(re)
```

![](/assets/img/loraintro/3.png)

ÕćåÕżćµĢ░µŹ«’╝īÕ£©Ķ┐ÖõĖ¬õŠŗÕŁÉõĖŁ’╝īµłæõ╗¼õĮ┐ńö©õĖŗķØóńÜäµĢ░µŹ«

[id.json](/assets/file/loraintro/id.json)

Ķ┐ÖõĖ¬µĢ░µŹ«µś»õ╗Ä[Ķ┐Öķćī](https://github.com/hiyouga/LLaMA-Factory/blob/bb0a37dc067e4385290644f165e3634dcbd88894/data/identity.json)õ┐«µö╣ĶĆīµØź’╝īĶ┐ÖõĖ¬Ķ«Łń╗āµĢ░µŹ«µś»Ķ«®Õż¦µ©ĪÕ×ŗńÜäÕÉŹÕŁŚÕÆīÕ╝ĆÕÅæÕĢåÕÅśµłÉµłæõ╗¼Õ«Üõ╣ēńÜäŃĆéidķćīķØóÕåģÕ«╣Õ”éõĖŗ’╝Ü

```
  {
    "instruction": "hi",
    "input": "",
    "output": "Hello! I am Õ░ÅµØÄ, an AI assistant developed by Õ░ÅÕ╝Ā. How can I assist you today?"
  },
  {
    "instruction": "hello",
    "input": "",
    "output": "Hello! I am Õ░ÅµØÄ, an AI assistant developed by Õ░ÅÕ╝Ā. How can I assist you today?"
  },
  {
    "instruction": "Who are you?",
    "input": "",
    "output": "I am Õ░ÅµØÄ, an AI assistant developed by Õ░ÅÕ╝Ā. How can I assist you today?"
  },
```

µÄźõĖŗµØźĶ┐øĶĪīLoRAÕŠ«Ķ░ā’╝īĶ┐Öķćīńö©õ║åpeftÕīģ’╝Ü

```
from transformers import AutoTokenizer,AutoModelForCausalLM,DataCollatorForSeq2Seq,Trainer,TrainingArguments
from datasets import load_dataset,DatasetDict
from peft import LoraConfig,TaskType,get_peft_model
import torch

dataset = load_dataset('json',data_files='id.json',split='train')
dataset = dataset.train_test_split(test_size=0.1)

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")

def process_fuc(one):
    MAX_LENGTH = 256
    input_ids,attention_mask,labels = [],[],[]
    instruction = tokenizer("\n".join(["Human: "+ one["instruction"],one["input"]]).strip() + "\n\nAssistant: ")
    response = tokenizer(one["output"] + tokenizer.eos_token)
    input_ids = instruction["input_ids"] + response["input_ids"]
    attention_mask = instruction["attention_mask"] + response["attention_mask"]
    labels = [-100] * len(instruction["input_ids"]) + response["input_ids"]
    if len(input_ids) > MAX_LENGTH:
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }
tokenizer_dataset = dataset.map(process_fuc,remove_...