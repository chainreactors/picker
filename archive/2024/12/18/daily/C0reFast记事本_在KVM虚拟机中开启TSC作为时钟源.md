---
title: 在KVM虚拟机中开启TSC作为时钟源
url: https://www.ichenfu.com/2024/12/17/enable-tsc-virtualization-on-kvm/
source: C0reFast记事本
date: 2024-12-18
fetch_date: 2025-10-06T19:36:10.133905
---

# 在KVM虚拟机中开启TSC作为时钟源

[C0reFastè®°äºæ¬](/)

to inspire confidence in somebody.

* [é¦é¡µ](/)
* [åç±»](/categories/)
* [å½æ¡£](/archives/)
* [æ ç­¾](/tags/)
* [å³äº](/about/)
* æç´¢

* æç« ç®å½
* ç«ç¹æ¦è§

1. [1. åºç¡åæ](#%E5%9F%BA%E7%A1%80%E5%88%86%E6%9E%90)
2. [2. å¼å¯TscInvariantç¹æ§](#%E5%BC%80%E5%90%AFTscInvariant%E7%89%B9%E6%80%A7)
3. [3. VMç­è¿ç§»](#VM%E7%83%AD%E8%BF%81%E7%A7%BB)
4. [4. TSCèæåçç¡¬ä»¶å é](#TSC%E8%99%9A%E6%8B%9F%E5%8C%96%E7%9A%84%E7%A1%AC%E4%BB%B6%E5%8A%A0%E9%80%9F)
   1. [4.0.1. 26.6.5 Time-Stamp Counter Offset and Multiplier](#26-6-5-Time-Stamp-Counter-Offset-and-Multiplier)
5. [4.1. 27.3 CHANGES TO INSTRUCTION BEHAVIOR IN VMX NON-ROOT OPERATION](#27-3-CHANGES-TO-INSTRUCTION-BEHAVIOR-IN-VMX-NON-ROOT-OPERATION)
6. [4.2. 15.30.5 TSC Ratio MSR (C000\_0104h)](#15-30-5-TSC-Ratio-MSR-C000-0104h)

- [5. æ§è½æµè¯](#%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95)

éå­

[111
æ¥å¿](/archives/)

[15
åç±»](/categories/)

[249
æ ç­¾](/tags/)

[GitHub](https://github.com/C0reFast "GitHub â https://github.com/C0reFast")

E-Mail

[Weibo](https://weibo.com/c0refast "Weibo â https://weibo.com/c0refast")

èµå©å

é¾æ¥

* [ç±å¼æº](https://www.aikaiyuan.com/ "https://www.aikaiyuan.com/")
* [ä¸åå](https://blog.yiranzai.top/ "https://blog.yiranzai.top/")
* [PikachuWorld](https://www.cnblogs.com/pikachuworld/ "https://www.cnblogs.com/pikachuworld/")

# å¨KVMèææºä¸­å¼å¯TSCä½ä¸ºæ¶éæº

åè¡¨äº
2024å¹´12æ17æ¥ 20:49

åç±»äº

[èæå](/categories/%E8%99%9A%E6%8B%9F%E5%8C%96/)

éè¯»æ¬¡æ°ï¼

ä¸ä¸ç¯[x86å¹³å°çTSCï¼TIME-STAMP COUNTERï¼](/2024/11/11/facts-about-x86-tsc/)ä¸­å¤§æ¦åæäºä¸ä¸TSCçä¸äºç¸å³çç¹æ§ï¼ä»¥åTSCä½ä¸ºç³»ç»æ¶éæºçä¸äºåºç¡æ¡ä»¶ãé£ä¹ï¼å¨èæåçåºæ¯ä¸ï¼å¦ä½è®©Guestä¹ç¨ä¸TSCå¢ï¼è¿ç¯æç« å°±æ¥è®¨è®ºä¸ä¸TSCå¨KVMèæåä¸­çä½¿ç¨ã

## åºç¡åæ

é»è®¤æåµä¸ï¼KVMèææºé¦éçæ¶éæºæ¯`kvm-clock`ï¼å³ä½¿å°VMçCPU Modelè®¾ç½®ä¸º`host-passthrough`ï¼ä¹ä¸ä¼ä½¿ç¨TSCä½ä¸ºæ¶éæºã

```
# lscpu|grep Flags
Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq dtes64 vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves wbnoinvd arat vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid fsrm md_clear flush_l1d arch_capabilities
# cat /sys/devices/system/clocksource/clocksource0/available_clocksource
kvm-clock acpi_pm
# cat /sys/devices/system/clocksource/clocksource0/current_clocksource
kvm-clock
```

å¯ä»¥çå°ï¼å³ä½¿CPUæå¤§é¨åTSCç¸å³çFlagsï¼ä½æ¯`available_clocksource`éå¹¶æ²¡æTSCï¼current\_clocksourceä¹æ¯kvm-clockï¼åå å¯ä»¥ä»dmesgéçå°ï¼

```
# dmesg |grep -i tsc
[    0.000000] tsc: Detected 2199.998 MHz processor
[    0.001000] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x1fb63109b96, max_idle_ns: 440795265316 ns
[    0.001000] TSC deadline timer enabled
[    0.577230] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x1fb63109b96, max_idle_ns: 440795265316 ns
[    0.692265] tsc: Marking TSC unstable due to TSC halts in idle states deeper than C2
```

å¯ä»¥çå°ï¼å¨å¯å¨çæ¶åï¼ä½æ¯ç±äºTSCå¨C2ç¶æä¸ä¼åæ­¢ï¼æä»¥è¢«æ è®°ä¸ºä¸ç¨³å®ã
å½ç¶ï¼è¿æå¦å¤ä¸ç§æåµï¼

```
# cat /sys/devices/system/clocksource/clocksource0/available_clocksource
kvm-clock tsc acpi_pm
# cat /sys/devices/system/clocksource/clocksource0/current_clocksource
kvm-clock
```

è¿ç§æåµä¸ï¼è½ç¶TSCæ¯å¯ç¨çï¼ä½æ¯è¿æ¯æ²¡æè¢«ä¼åä½¿ç¨ãè½ç¶æä¸¤ç§å¯è½æ§ï¼ä½å¶å®æ ¹å é½æ¯ä¸ä¸ªï¼é£å°±æ¯å¨Guestéï¼CPUç¼ºå°ä¸ä¸ªå³é®ç¹æ§ï¼é£å°±æ¯ä¸ç¯æç« æå°ç`Invariant TSC`ã

```
# cpuid -1 -l 0x80000007
CPU:
   RAS Capability (0x80000007/ebx):
      MCA overflow recovery support = false
      SUCCOR support                = false
      HWA: hardware assert support  = false
      scalable MCA support          = false
   Advanced Power Management Features (0x80000007/ecx):
      CmpUnitPwrSampleTimeRatio = 0x0 (0)
   Advanced Power Management Features (0x80000007/edx):
      TS: temperature sensing diode           = false
      FID: frequency ID control               = false
      VID: voltage ID control                 = false
      TTP: thermal trip                       = false
      TM: thermal monitor                     = false
      STC: software thermal control           = false
      100 MHz multiplier control              = false
      hardware P-State control                = false
      TscInvariant                            = false
      CPB: core performance boost             = false
      read-only effective frequency interface = false
      processor feedback interface            = false
      APM power reporting                     = false
      connected standby                       = false
      RAPL: running average power limit       = false
```

å¯ä»¥çå°ï¼å³é®ç`TscInvariant`æ¯falseï¼å¨ç¬¬ä¸ç§æåµä¸ï¼`intel_idle`é©±å¨æ­£å¸¸å è½½ï¼å¨[é©±å¨ä»£ç ä¸­](https://github.com/torvalds/linux/blob/v6.12/drivers/idle/intel_idle.c#L2008)ï¼

```
static bool __init intel_idle_verify_cstate(unsigned int mwait_hint)
{
	unsigned int mwait_cstate = (MWAIT_HINT2CSTATE(mwait_hint) + 1) &
					MWAIT_CSTATE_MASK;
	unsigned int num_substates = (mwait_substates >> mwait_cstate * 4) &
					MWAIT_SUBSTATE_MASK;

	/* Ignore the C-state if there are NO sub-states in CPUID for it. */
	if (num_substates == 0)
		return false;

	if (mwait_cstate > 2 && !boot_cpu_has(X86_FEATURE_NONSTOP_TSC))
		mark_tsc_unstable("TSC halts in idle states deeper than C2");

	return true;
}
```

ä¼æ£æµCPUæ¯å¦æ`X86_FEATURE_NONSTOP_TSC`ä¹å°±æ¯`TscInvariant`ï¼å¦ææ²¡æï¼å°±ä¼æ è®°TSCä¸ºä¸ç¨³å®ãé£ä¹å¨è¿ç§æåµä¸ï¼å ä¸ºTSCè¢«æ è®°ä¸ºä¸ç¨³å®äºï¼æä»¥tscæ¯ä¸ä¼åºç°å¨available\_clocksourceä¸­çã

é£ç¬¬äºç§æåµå¢ï¼TSCæ²¡æè¢«æ è®°ä¸ºä¸ç¨³å®ï¼ä¹åºç°å¨äº`available_clocksource`ä¸­ï¼ä½æ¯ä¸ºä»ä¹è¿æ¯æ²¡æè¢«ä¼åä½¿ç¨å¢ï¼è¿æ¯å ä¸ºé»è®¤æåµä¸ï¼kvm-clockçä¼åçº§æ¯TSCè¦é«ï¼å¯ä»¥çå°å¨åæ ¸ä¸­ç[ä»£ç ](https://github.com/torvalds/linux/blob/v6.12/arch/x86/kernel/kvmclock.c)ï¼

```
static struct clocksource kvm_clock = {
	.name	= "kvm-clock",
	.read	= kvm_clock_get_cycles,
    // é»è®¤æåµä¸ï¼kvm-clockçratingæ¯400ï¼è¿æ¯TSCçrating 300è¦é«ï¼æä»¥å½ä¸¤èåæ¶å­å¨æ¶ï¼ç³»ç»ä¼ä¼åä½¿ç¨kvm-clockä½ä¸ºæ¶éæº
	.rating	= 400,
	.mask	= CLOCKSOURCE_MASK(64),
	.flags	= CLOCK_SOURCE_IS_CONTINUOUS,
	.id     = CSID_X86_KVM_CLK,
	.enable	= kvm_cs_enable,
};
```

ä½æ¯å¨`kvm-clock`åå§åçè¿ç¨ä¸­ï¼å¦æåç°TSCæ»¡è¶³æ¡ä»¶çè¯ï¼ä¼ä¸»å¨éä½èªå·±çratingï¼

```
void __init kvmclock_init(void)
{
    // ...

	/*
	 * X86_FEATURE_NONSTOP_TSC is TSC runs at constant rate
	 * with P/T states and does not stop in deep C-states.
	 *
	 * Invariant TSC exposed by host means kvmclock is not necessary:
	 * can use TSC as clocksource.
	 *
	 */
	if (boot_cpu_has(X86_FEATURE_CONSTANT_TSC) &&
	    boot_cpu_has(X86_FEATURE_NONSTOP_TSC) &&
	    !check_tsc_unstable())
		kvm_clock.rating = 299;

	clocksource_register_hz(&kvm_clock, NSEC_PER_SEC);
	pv_info.name = "KVM";
}
```

å¯ä»¥çå°ï¼åªè¦CPUæ¯æ`TscInvariant`ï¼é£ä¹kvm-clockçratingä¼ä¸»å¨éä½èªå·±çratingå°299ï¼é£ä¹å¨è¿ç§æ...