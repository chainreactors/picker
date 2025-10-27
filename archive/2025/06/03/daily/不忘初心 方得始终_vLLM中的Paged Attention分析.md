---
title: vLLM中的Paged Attention分析
url: http://terenceli.github.io/%E6%8A%80%E6%9C%AF/2025/06/02/vllm-paged-attn
source: 不忘初心 方得始终
date: 2025-06-03
fetch_date: 2025-10-06T22:51:30.021246
---

# vLLM中的Paged Attention分析

[šłćŚŅėŚąĚŚŅÉ śĖĻŚĺóŚßčÁĽą](/)

* [Archive](/archive.html)
* [About Me](/aboutMe.html)
* [Pages](/pages.html)
* [Tags](/tags.html)
* [Categories](/categories.html)

# vLLMšł≠ÁöĄPaged AttentionŚąÜśěź

2025-06-02

## Śüļśú¨ś¶āŚŅĶ

šłäšłÄÁĮáśĖáÁę†šł≠šĽčÁĽćšļÜKV cacheÁöĄś¶āŚŅĶšĽ•ŚŹäšĹúÁĒ®ÔľĆÁĒĪšļéKV cacheŚú®śé®ÁźÜšł≠ÁöĄšĹúÁĒ®śÄßŤÉĹśŹźŚćáŚĺąŚ§ßÔľĆśČÄšĽ•ÁéįŚú®ŚźĄÁßćśé®ÁźÜś°Üśě∂ťÉĹšľöśĒĮśĆĀKV cache„Äāśú¨śĖášĽčÁĽćvLLMšł≠ÁöĄś†łŚŅÉŚéüÁźÜPaged AttentionÁöĄŚģěÁéįÔľĆśú¨śĖášłćšľöŤĮ¶ÁĽÜšĽčÁĽćvLLMÁöĄŚüļśú¨ŚéüÁźÜšĽ•ŚŹävLLMśēīšĹďÁöĄśļźÁ†Āśě∂śěĄŚąÜśěźÔľąŚįÜśĚ•śúČśúļšľöšļČŚŹĖŚÜôšłÄšłčÔľČÔľĆśČÄšĽ•ŚĀáŤģĺŤĮĽŤÄÖťúÄŤ¶ĀÁÜüśāČŚ§ßś®°ŚěčÁöĄŚüļśú¨śé®ÁźÜŤŅáÁ®čšĽ•ŚŹävLLMŚüļśú¨šĽ£Á†Āśě∂śěĄÔľĆ[ŚõĺŤß£Ś§ßś®°ŚěčŤģ°ÁģóŚä†ťÄüÁ≥ĽŚąóšĻčÔľövLLMś†łŚŅÉśäÄśúĮPagedAttentionŚéüÁźÜ](https://zhuanlan.zhihu.com/p/691038809)śĖáÁę†śėĮšłćťĒôÁöĄšĽčÁĽćvLLM Paged AttentionÁöĄŚéüÁźÜśÄßśĖáÁę†„Äā

śé®ÁźÜś°Üśě∂Śú®ŤŅõŤ°Ćśé®ÁźÜŤŅáÁ®čšł≠šłÄšł™ťáćŤ¶ĀÁöĄÁéĮŤäāśėĮŤģ°ÁģóŚźĄšł™tokenšĻčťóīÁöĄŤá™ś≥®śĄŹŚäõÔľĆKV cachešŅĚŚ≠ėšļÜšĻčŚČćtokenÁöĄKVŚÄľÔľĆŚú®Ťģ°ÁģóŚĹďŚČćtokenśó∂ÔľĆšľöŚľēÁĒ®KV cachešł≠ŚÄľ„ÄāvLLM Paged AttentionÁöĄś†łŚŅÉśúļŚą∂ŚįĪśėĮŚú®ŤŅôťáĆÁģ°ÁźÜKV cacheÁöĄśó∂ŚÄôťááÁĒ®šļÜÁĪĽšľľśďćšĹúÁ≥ĽÁĽüŤôöśčüŚÜÖŚ≠ėÁöĄś¶āŚŅĶÔľĆťÄöŤŅáŚä®śÄĀÁöĄŚąÜťÖćKV cacheÁöĄblockÔľĆšĽéŤÄĆśŹźťęėśėĺŚ≠ėÁöĄŚą©ÁĒ®śēąÁéá„Äāśú¨śĖáŚįĪśėĮŚĮĻŤŅôšłÄśúļŚą∂ŤŅõŤ°ĆŚąÜśěźÔľĆÁģÄŚćēśĚ•Ťģ≤ÔľĆśú¨śĖášľöšĽéšĽ£Á†ĀŚĪāťĚĘŤĮ¶ÁĽÜŚąÜśěźšłčťĚĘŤŅôšł™ŚõĺÁöĄŚģěÁéį„Äā

![](/assets/img/vllmpageattn/1.png)

ŚÖ∑šĹďśĚ•Ťģ≤ÔľĆśú¨śĖáŚĆÖśč¨Ś¶āšłčŚÜÖŚģĻ

* ÁČ©ÁźÜblockÁöĄŚąÜťÖć
* ŤôöśčüśúļblockÁöĄÁģ°ÁźÜ
* KV cacheÁöĄšĹŅÁĒ®

śú¨śĖáŚüļšļévLLMÁöĄCPUŚģěÁéįŚąÜśěź„Äā
šłÄšł™BlockÁĪĽšľľśďćšĹúÁ≥ĽÁĽüÁöĄšłÄšł™pageÔľĆšłÄšł™pageťÄöŚłłÁģ°ÁźÜŚõļŚģöŚ§ßŚįŹÁöĄbyteÔľąšłÄŤą¨śėĮ4096ÔľČÔľĆšłÄšł™BlockšĻüśėĮÁģ°ÁźÜŚõļŚģöŚ§ßŚįŹÁöĄtokenÁöĄKVÔľĆśĮĒŚ¶āšłäťĚĘÁöĄŚõĺšłÄšł™BlockÁģ°ÁźÜ4šł™tokenÁöĄKVÔľĆŚģěťôÖšł≠šłÄŤą¨šľöśõīŚ§ßÁāĻ„Äā

## ÁČ©ÁźÜblockÁöĄŚąÜťÖć

šłéśďćšĹúÁ≥ĽÁĽüÁöĄpageŚú®Á≥ĽÁĽüŚąĚŚßčŚĆĖťė∂śģĶŚąÜťÖćŚģĆśąźÔľĆśĮŹšł™pageŚąÜťÖćšłÄšł™pfnÁĪĽšľľÔľĆÁČ©ÁźÜblockŚú®vLLMŚľēśďéŚąĚŚßčŚĆĖťė∂śģĶšľöŚąÜťÖćŚģĆśąźÔľĆśĮŹšł™ÁČ©ÁźÜblockÁöĄidŚįĪśėĮŚÖ∂Śú®śēįÁĽĄšł≠ÁöĄŚļŹŚŹ∑„ÄāvLLMšł≠ÁöĄŤŅôšł™ŚõĺŚ∑¶ŤĺĻŚŹĮšĽ•ÁúčŚĀöśėĮŤôöśčüBlockÁöĄÁģ°ÁźÜÔľĆŚŹ≥ŤĺĻŚŹĮšĽ•ÁúčśąźśėĮÁČ©ÁźÜBlockÁöĄÁģ°ÁźÜÔľąŚüļśú¨ŚįĪśėĮŚąÜťÖćÁ©ļťóī„ÄĀswap in/outÁ≠ČÔľČÔľĆŚŹ≥ŤĺĻśľŹšļÜšłÄšł™executorÔľĆšĻüŚŹĮŤÉĹśėĮšĹúŤÄÖŤßČŚĺóšłćŚ§™ťáćŤ¶Ā„Äā

![](/assets/img/vllmpageattn/2.png)

KV cacheŚąĚŚßčŚĆĖśĶĀÁ®čŚ¶āšłčÔľö

```
LLMEngine.__init__
  -->self._initialize_kv_caches(LLMEngine._initialize_kv_caches)
    -->self.model_executor.determine_num_available_blocks
    -->self.model_executor.initialize_cache
      -->self.collective_rpc("initialize_cache")
        -->CPUWorker.initialize_cache
          -->self._init_cache_engine(CPUWorker._init_cache_engine)
            -->CPUCacheEngine.__init__
              -->get_attn_backend
              -->self._allocate_kv_cache(CPUCacheEngine._allocate_kv_cache)
                -->self.attn_backend.get_kv_cache_shape
                -->kv_cache.append
            -->bind_kv_cache
            -->layer_cache.fill_(0)
```

self.model\_executor.determine\_num\_available\_blocksšľöŚÜ≥ŚģöśÄĽÁöĄÁČ©ÁźÜBlockšł™śēįÔľąÁõłŚĹďšļéśďćšĹúÁ≥ĽÁĽüťáĆťĚĘśÄĽÁöĄpageť°ĶśēįÔľČÔľĆŚĆÖśč¨num\_gpu\_blocksŚíĆnum\_cpu\_blocks„Äā

ÁČ©ÁźÜBlockšĻüŚįĪśėĮKV cacheÁöĄÁ©ļťóīŚąõŚĽļśėĮŚú®CPUWorkerÁöĄ\_init\_cache\_engineŚáĹśēįšł≠ŚģĆśąźÁöĄ„Äā

```
    def _init_cache_engine(self) -> None:
        self.cache_engine = [
            CPUCacheEngine(self.cache_config, self.model_config,
                           self.parallel_config, self.device_config)
            for _ in range(self.parallel_config.pipeline_parallel_size)
        ]
        self.cpu_cache = [
            self.cache_engine[ve].cpu_cache
            for ve in range(self.parallel_config.pipeline_parallel_size)
        ]
        bind_kv_cache(self.compilation_config.static_forward_context,
                      self.cpu_cache)
        self.model_runner.block_size = self.cache_engine[0].block_size

        assert all(
            self.cpu_cache[ve] is not None
            for ve in range(self.parallel_config.pipeline_parallel_size))

        # Populate the cache to warmup the memory
        for ve in range(self.parallel_config.pipeline_parallel_size):
            for layer_cache in self.cpu_cache[ve]:
                layer_cache.fill_(0)
```

CPUCacheEngineśėĮÁĒ®śĚ•Áģ°ÁźÜÁČ©ÁźÜBlockÁöĄś†łŚŅÉÔľĆšłčťĚĘśėĮŚąĚŚßčŚĆĖÁöĄÁ¨¨šłÄťÉ®ŚąÜšĽ£Á†ĀÔľĆŚ∑•šĹúšłļŚąĚŚßčŚĆĖÁõłŚÖ≥ŚŹėťáŹ„Äāhead\_siześėĮś≥®śĄŹŚäõśúļŚą∂šł≠Ś§īÁöĄÁĽīŚļ¶Ś§ßŚįŹŚíĆŚ§īśēįnum\_headsÔľĆśĮŹšł™layerťÉĹśúČŚĮĻŚļĒÁöĄKV cacheÔľĆśČÄšĽ•ŤŅôťáĆŤ¶ĀŤé∑ŚŹĖnum\_layers„Äāblock\_siześėĮśĮŹšł™blockŤ¶ĀšŅĚŚ≠ėÁöĄtokenśēįÁõģÁöĄKV cacheÔľĆnum\_cpu\_blocksśėĮšĻčŚČćŤé∑ŚŹĖÁöĄśÄĽŚÖĪÁöĄCPU block„Äā

```
class CPUCacheEngine:
    """Manages the KV cache for CPU backend.

    This class is responsible for initializing and managing CPU KV
    caches. It also provides methods for performing KV cache operations, such
    as copying.
    """

    def __init__(self, cache_config: CacheConfig, model_config: ModelConfig,
                 parallel_config: ParallelConfig,
                 device_config: DeviceConfig) -> None:
        assert device_config.device_type == "cpu"
        self.cache_config = cache_config
        self.model_config = model_config
        self.parallel_config = parallel_config

        self.head_size = model_config.get_head_size()
        self.num_layers = model_config.get_num_layers(parallel_config)
        self.num_heads = model_config.get_num_kv_heads(parallel_config)

        self.block_size = cache_config.block_size
        # Note: In CacheConfig, num_gpu_blocks actual is num_cpu_blocks
        # for CPU backend, because we want to reuse KV cache management
        # in the scheduler.
        self.num_cpu_blocks = cache_config.num_gpu_blocks

        if cache_config.cache_dtype == "auto":
            self.dtype = model_config.dtype
        elif cache_config.cache_dtype in ["fp8", "fp8_e5m2"]:
            self.dtype = torch.float8_e5m2
        else:
            raise NotImplementedError(f"Unsupported KV cache type "
                                      f"{cache_config.cache_dtype}.")

        # Get attention backend.
        self.attn_backend = get_attn_backend(
            self.model_config.get_head_size(),
            self.model_config.dtype,
            cache_config.cache_dtype,
            self.block_size,
            self.model_config.is_attention_free,
            use_mla=self.model_config.use_mla,
        )

        # Initialize the cache.
        self.cpu_cache = self._allocate_kv_cache(self.num_cpu_blocks)
```

CPUCacheEngine.\_\_init\_\_ÁöĄÁ¨¨šļĆťÉ®ŚąÜÁĒ®śĚ•Ťé∑ŚŹĖŚģěÁéįattentionŤģ°ÁģóÁöĄŚźéÁęĮÁĪĽÔľĆŤŅôšł™šĺčŚ≠źšł≠šľöŤé∑ŚŹĖTorchSDPABackend„ÄāCPUCacheEngine.\_\_init\_\_ÁöĄśúÄŚźéšłÄťÉ®ŚąÜŤįÉÁĒ®self.\_allocate\_kv\_cacheÔľĆŚģĆśąźŚģěťôÖÁöĄÁČ©ÁźÜBlockÁöĄŚąÜťÖć„Äā

śąĎšĽ¨ÁúčÁúč\_allocate\_kv\_cacheÁöĄŚģěÁéį

```
    def _allocate_kv_cache(
        self,
        num_blocks: int,
    ) -> List[torch.Tensor]:
        """Allocates KV cache on CPU."""
        kv_cache_shape = self.attn_backend.get_kv_cache_shape(
            num_blocks, self.block_size, self.num_heads, self.head_size)
        kv_cache: List[torch.Tensor] = []
        for _ in range(self.num_layers):
            kv_cache.append(
                torch.empty(kv_cache_shape, dtype=self.dtype, device="cpu"))
        return kv_cache
```

self.attn\_backend.get\_kv\_cache\_shapeÁöĄŤįÉÁĒ®ŤŅĒŚõěKV cacheÁöĄÔľĆTorchSDPABackendÁõīśé•ŤįÉÁĒ®PagedAttention.get\_kv\_cache\_shapeŤŅĒŚõě„Äā

```
class TorchSDPABackend(AttentionBackend):
    ...
    def get_kv_cache_shape(
        num_blocks: int,
        block_size: int,
        num_kv_heads: int,
        head_size: int,
    ) -> Tuple[int, ...]:
        return PagedAttention.get_kv_cache_shape(num_blocks, block_size,
                                                 num_kv_heads, head_size)

class _PagedAttention:
    ...
    @staticmethod
    def get_kv_cache_shape(
        num_blocks: int,
        block_size: int,
        num_kv_heads: int,
        head_size: int,
        *args,
    ) -...