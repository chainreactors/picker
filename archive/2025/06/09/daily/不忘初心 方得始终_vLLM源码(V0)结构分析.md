---
title: vLLM源码(V0)结构分析
url: http://terenceli.github.io/%E6%8A%80%E6%9C%AF/2025/06/08/vllm-code-overview
source: 不忘初心 方得始终
date: 2025-06-09
fetch_date: 2025-10-06T22:52:03.984356
---

# vLLM源码(V0)结构分析

[不忘初心 方得始终](/)

* [Archive](/archive.html)
* [About Me](/aboutMe.html)
* [Pages](/pages.html)
* [Tags](/tags.html)
* [Categories](/categories.html)

# vLLM源码(V0)结构分析

2025-06-08

vLLM使用通常如下（本地推理，非服务）：

```
from vllm import LLM

llm = LLM(model="facebook/opt-125m")
outputs = llm.generate("Hello, my name is")

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

vLLM代码结构有非常清晰的类层次结构，整体的数据结构关系如下：

![](/assets/img/vllmcodearch/1.png)

这里我们以V0分析，重在分析其各个类之间的关系，主要讨论核心的两个问题即LLM()创建模型引擎，以及通过llm.generate进行推理。本质就是加载模型和处理请求，本文只讨论整体结构，以CPU运行为例。

## 模型的加载

下面这个图展示了模型的加载流程，通过Executor、Worker层，最终由ModelRunner层开始加载模型。

![](/assets/img/vllmcodearch/2.png)

最终调用vllm/model/executor/model\_loader/**init**.py文件中的get\_model完成实际模型加载工作。

```
def get_model(*, vllm_config: VllmConfig) -> nn.Module:
    loader = get_model_loader(vllm_config.load_config)
    return loader.load_model(vllm_config=vllm_config)
```

这里loader默认情况下是DefaultModelLoader。其load\_model函数如下：

```
    def load_model(self, vllm_config: VllmConfig) -> nn.Module:
        device_config = vllm_config.device_config
        model_config = vllm_config.model_config
        target_device = torch.device(device_config.device)
        with set_default_torch_dtype(model_config.dtype):
            with target_device:
                model = _initialize_model(vllm_config=vllm_config)

            weights_to_load = {name for name, _ in model.named_parameters()}
            loaded_weights = model.load_weights(
                self.get_all_weights(model_config, model))
            self.counter_after_loading_weights = time.perf_counter()
            logger.info(
                "Loading weights took %.2f seconds",
                self.counter_after_loading_weights -
                self.counter_before_loading_weights)
            # We only enable strict check for non-quantized models
            # that have loaded weights tracking currently.
            if model_config.quantization is None and loaded_weights is not None:
                weights_not_loaded = weights_to_load - loaded_weights
                if weights_not_loaded:
                    raise ValueError(
                        "Following weights were not initialized from "
                        f"checkpoint: {weights_not_loaded}")

            _process_weights_after_loading(model, model_config, target_device)

        return model.eval()
```

\_initialize\_model得到模型结构的class，并且调用模型的初始化函数，比如Qwen2ForCausalLM.**init**()函数。

```
def _initialize_model(
    vllm_config: VllmConfig,
    *,
    prefix: str = "",
    model_class: Optional[type[nn.Module]] = None,
) -> nn.Module:
    """Initialize a model with the given configurations."""
    model_config = vllm_config.model_config
    if model_class is None:
        model_class, _ = get_model_architecture(model_config)

    if vllm_config.quant_config is not None:
        configure_quant_config(vllm_config.quant_config, model_class)

    signatures = inspect.signature(model_class.__init__)
    all_params = [param.name for param in signatures.parameters.values()]
    if "vllm_config" in all_params and "prefix" in all_params:
        # new-style model class
        with set_current_vllm_config(vllm_config, check_compile=True):
            return model_class(vllm_config=vllm_config, prefix=prefix)

    ...
```

model.load\_weights则开始调用模型的函数加载权重。最终会调用到AutoWeightsLoader的load\_wegiths函数。

```
    def load_weights(self, weights: Iterable[Tuple[str,
                                                   torch.Tensor]]) -> Set[str]:
        loader = AutoWeightsLoader(
            self,
            skip_prefixes=(["lm_head."]
                           if self.config.tie_word_embeddings else None),
        )
        return loader.load_weights(weights)
```

这里的wegiths是从 self.get\_all\_weights(model\_config, model)) 这个函数获取的，get\_all\_wegiths从safetensors中加载权重。相关调用如下：

```
DefaultModelLoader.get_all_weights
  -->self._get_weights_iterator
    -->self._prepare_weights
    -->safetensors_weights_iterator
```

safetensors\_weights\_iterator中打开文件。

```
def safetensors_weights_iterator(
    hf_weights_files: List[str],
    use_tqdm_on_load: bool,
) -> Generator[Tuple[str, torch.Tensor], None, None]:
    """Iterate over the weights in the model safetensor files."""
    for st_file in tqdm(
            hf_weights_files,
            desc="Loading safetensors checkpoint shards",
            disable=not enable_tqdm(use_tqdm_on_load),
            bar_format=_BAR_FORMAT,
    ):
        with safe_open(st_file, framework="pt") as f:
            for name in f.keys():  # noqa: SIM118
                param = f.get_tensor(name)
                yield name, param
```

## 请求的处理

请求处理的过程如下：

![](/assets/img/vllmcodearch/3.png)

核心过程是在LLMEngine中的step函数。step函数注释很清晰，第一步将要处理的下一步的seq group找出来，第二步调用executor执行推理，第三步处理输出。

```
    def step(self) -> List[Union[RequestOutput, PoolingRequestOutput]]:
        """Performs one decoding iteration and returns newly generated results.

        .. figure:: https://i.imgur.com/sv2HssD.png
            :alt: Overview of the step function
            :align: center

            Overview of the step function.

        Details:
            - Step 1: Schedules the sequences to be executed in the next
              iteration and the token blocks to be swapped in/out/copy.

                - Depending on the scheduling policy,
                  sequences may be `preempted/reordered`.
                - A Sequence Group (SG) refer to a group of sequences
                  that are generated from the same prompt.

            - Step 2: Calls the distributed executor to execute the model.
            - Step 3: Processes the model output. This mainly includes:

                - Decodes the relevant outputs.
                - Updates the scheduled sequence groups with model outputs
                  based on its `sampling parameters` (`use_beam_search` or not).
                - Frees the finished sequence groups.

            - Finally, it creates and returns the newly generated results.

        ...
        """
        ...
        # For llm_engine, there is no pipeline parallel support, so the engine
        # used is always 0.
        virtual_engine = 0

        ...
        if not self._has_remaining_steps(
                seq_group_metadata_list
        ) and not self._skip_scheduling_next_step:
            # Schedule iteration
            (seq_group_metadata_list, scheduler_outputs,
             allow_async_output_proc
             ) = self.scheduler[virtual_engine].schedule()

            ctx.seq_group_metadata_list = seq_group_metadata_list
            ctx.scheduler_outputs = scheduler_outputs

            ...

        if not scheduler_outputs.is_empty():

            # Check if we have a cached last_output from the previous iteration.
            # For supporting PP this is probably the best way to pass the
            # sampled_token_ids, as a separate broadcast over all the PP stages
            # will cause one virtual engine's microbatch to block the pipeline.
            last_sampled_token_ids = \
                self._get_last_sampled_token_ids(virtual_engine)

            execute_model_req = ExecuteModelRequest(
                seq_group_metadata_list=seq_group_metadata_list,
                blocks_to_swap_in=scheduler_outputs.blocks_to_swap_in,
                blocks_to_swap_out=scheduler_outputs.blocks_to_swap_out,
                blocks_to_copy=scheduler_outputs.blocks_to_copy,
                num_lookahead_slots=scheduler_outputs.num_lookahead_slots,
                running_queue_size=scheduler_outputs.running_queue_size,
                finished_requests_ids=finished_requests_ids,
                # We use ExecuteModelRequest to pass the last sampled_token_ids
                # to each of the non-last PP stages for in-place prepare_input.
                last_sampled_token_ids=last_sampled_token_ids)

            i...