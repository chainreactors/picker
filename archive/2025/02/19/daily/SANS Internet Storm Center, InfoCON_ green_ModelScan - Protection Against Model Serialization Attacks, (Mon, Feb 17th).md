---
title: ModelScan - Protection Against Model Serialization Attacks, (Mon, Feb 17th)
url: https://isc.sans.edu/diary/rss/31692
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-19
fetch_date: 2025-10-06T20:49:15.631369
---

# ModelScan - Protection Against Model Serialization Attacks, (Mon, Feb 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31688)
* [next](/diary/31700)

# [ModelScan - Protection Against Model Serialization Attacks](/forums/diary/ModelScan%2BProtection%2BAgainst%2BModel%2BSerialization%2BAttacks/31692/)

**Published**: 2025-02-17. **Last Updated**: 2025-02-18 00:37:10 UTC
**by** [Russ McRee](/handler_list.html#russ-mcree) (Version: 1)

[0 comment(s)](/diary/ModelScan%2BProtection%2BAgainst%2BModel%2BSerialization%2BAttacks/31692/#comments)

[Protect AI’s](https://protectai.com/) OSS [portfolio](https://github.com/protectai) includes tools aimed at improving security of AI/ML software. These tools are meant for a wide range of engineering, security and ML practitioners including developers, security engineers/researchers, ML engineers, LLM engineers and prompt engineers, and data scientists.
Of particular interest in light of [model serialization attacks](https://github.com/protectai/modelscan/blob/main/docs/model_serialization_attacks.md) is ModelScan.

Headlines as recent as 6 FEB 2025 remind us that the popular Python Pickle serialization format, common for distributing AI models, offers attackers opportunities to inject malicious code to be executed when loading models with PyTorch.[1] See [Malicious ML models discovered on Hugging Face platform](https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face). Post training, model’s mathematical representations can be stored in a variety of data serialization formats to be shared and reused without the need for additional model training. Pickle is a popular Python module used for serializing and deserializing ML model data. While easy to use, Pickle is considered an unsafe data format, as it allows Python code to be executed during ML model deserialization.[2]
As you can imagine, even as protective measures are being implemented, safety scanning is still recommended. ModelScan offers such capabilities with ease and convenience. [ModelScan](https://github.com/protectai/modelscan) is incredibly well documented and include [notebooks](https://github.com/protectai/modelscan/tree/main/notebooks) to aid experimentation and adoption.
I’ll share my quick setup steps, modify to your liking and preferences. These assume you’re building from scratch including Jupyter.

```

sudo apt install python3-pip python3-dev
sudo -H pip3 install --upgrade pip --break-system-packages
sudo -H pip3 install virtualenv --break-system-packages
cd code/
virtualenv modelscan-env
source modelscan-env/bin/activate
pip install modelscan
pip install jupyter
jupyter notebook
```

I also cloned the ModelScan repo in my `code` directory.
Read the repository [README](https://github.com/protectai/modelscan/tree/main) for yourself, but borrowing a few key highlights for efficacy here.
“A Model Serialization Attack is where malicious code is added to the contents of a model during serialization(saving) before distribution — a modern version of the Trojan Horse. The attack functions by exploiting the saving and loading process of models. When you load a model with model = torch.load(PATH), PyTorch opens the contents of the file and begins to running the code within. The second you load the model the exploit has executed."[3] A Model Serialization Attack can be used to execute:

* Credential Theft (Cloud credentials for writing and reading data to other systems in your environment)
* Data Theft (the request sent to the model)
* Data Poisoning (the data sent after the model has performed its task)
* Model Poisoning (altering the results of the model itself)

I took liberties with the *pytorch\_sentiment\_analysis* notebook found in `/modelscan/notebooks` and modified it to exemplify local Google Cloud credential secrets disclosure as opposed those for AWS as conveyed in the original notebook.
One note of interest. PyTorch is moving from away from what was a default configuration where `torch.load` ran with `weights_only` set to false, and is issuing the following warning if you don’t set the parameter to false (for experimention only) explicitly.
“**WARNING:** *torch.load() unless weights\_only parameter is set to True, uses pickle module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode, or that could have been tampered with. Only load data you trust.*”
Certainly, a good safety update for added protection, but thou shalt still scan. ;-)
**Figure 1** conveys notebook setup and the BERT based sentiment analysis PyTorch model used as the test subject.

![](https://isc.sans.edu/diaryimages/images/setupModel.png)

**Figure 1:** Setup and model saving

As seen in **Figure 2**, the notebook next offers prediction via the safe version of the model, then executes ModelScan with clean results to be expected.

![](https://isc.sans.edu/diaryimages/images/safePrediction%26scan.png)

**Figure 2:** Safe prediction and initial model scan

*modelscan –path PyTorchModels/safe\_model.pt* yields *No issues found*.

Next, we inject “malicious” code, `cat ~/.config/gcloud/credentials.db` in the safe model to simply read my Google Cloud client secret. A more sophisticated attack could include a reverse shell or secrets exfiltration. The model executes the malicious code as well as the expected prediction, as seen in **Figure 3**.

![](https://isc.sans.edu/diaryimages/images/serialization%26unsafePrediction.png)

**Figure 3:** Injection and unsafe prediction

Finally, the unsafe (evil) model is scanned, and the use of the unsafe operator `system` (defined under the `command` parameter in the serialization attack cell) is flagged as **Critical**, as seen in **Figure 4**.

![](https://isc.sans.edu/diaryimages/images/unsafeModelScan.png)

**Figure 4:** Injection and unsafe prediction

ModelScan save results in JSON or other reporting formats, and can scan models from a variety of ML libraries including Pytorch, Tensorflow, Keras, and Classic ML Libraries (Sklearn, XGBoost etc.).
Protect AI strongly recommends integrating ModelScan in your ML pipelines and CI/CD pipelines. They also have commercial offerings to better secure your AI implementations. To reiterate their assertion, model scanning must be performed more than once to accomplish the following:

* Scan all pre-trained models before loading it for further work to prevent a compromised model from impacting your model building or data science environments
* Scan all models after training to detect a supply chain attack that compromises new models
* Scan all models before deploying to an endpoint to ensure that the model has not been compromised after storage

Start with ModelScan, also give [Fickling](https://github.com/trailofbits/fickling) an indepth look, and avoid falling victim to headline generating AI/ML attack scenarios.

Cheers…until next time.

[Russ McRee](https://holisticinfosec.io/) | [@holisticinfosec](https://bsky.app/profile/holisticinfosec.bsky.social) | [infosec.exchange/@holisticinfosec](https://infosec.exchange/%40holisticinfosec) | [LinkedIn.com/in/russmcree](https://www.linkedin.com/in/russmcree/)

Recommended reading and tooling:

* [Model Serialization Attack Explainer](https://github.com/protectai/modelscan/blob/main/docs/model_serialization_attacks.md)
* [Understanding Pickle Risks: Essential Knowledge for Data Scientists](https://medium.com/%40coding-otter/understanding-pickle-risks-essential-knowledge-for-data-scientists-1f187feb455b)
* [Fickling](https://github.com/trailofbits/fickling)

**References**

[1] Constantin, L. and Solomon, H. (2025) Attackers hide malicious code in hugging face AI model Pickle Files, CSO Online. Available at: <https://www.csoonline.com/article/38...