---
title: FaceFusion 3.2.0 — 进阶体验（不要瑟瑟）
url: https://h4ck.org.cn/2025/05/20664
source: obaby@mars
date: 2025-05-12
fetch_date: 2025-10-06T22:24:56.503807
---

# FaceFusion 3.2.0 — 进阶体验（不要瑟瑟）

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# FaceFusion 3.2.0 — 进阶体验（不要瑟瑟）

2025年5月11日
[38 条评论](https://h4ck.org.cn/2025/05/20664#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/652a11cb.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/652a11cb.jpg)

书接前文，如果要处理普通的视频资源，根据上一篇文章的内容完全就足够了。

但是，如果你想处理点多少有点暴露或者纯粹的瑟瑟内容，你是怎么都进行不下去滴。

**启动脚本：**补上一个快速启动face fusion的ps代码，保存为ps1，相关路径改成自己的，启动的时候直接拖到powershell里面执行即可。

```
conda deactivate
conda init
conda activate facefusion
cd  E:\facefusion3\facefusion
python facefusion.py run --open-browsers
```

**现在来说下瑟瑟的问题**，一般这时候会卡在分析完成的地方：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-11-102841.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-11-102841.png)

analysing：100%之后就没动静了，原因在于视频的分析完成之后发现你的视频有瑟瑟内容，而至于瑟瑟内容的检测是通过content\_analyser.py中的detect\_nsfw方法实现的，如下（这个是我改完的）：

```
def detect_nsfw(vision_frame : VisionFrame) -> List[Score]:
    nsfw_scores = []
    model_size = get_model_options().get('size')
    temp_vision_frame = fit_frame(vision_frame, model_size)
    detect_vision_frame = prepare_detect_frame(temp_vision_frame)
    detection = forward(detect_vision_frame)
    detection = numpy.squeeze(detection).T
    nsfw_scores_raw = numpy.amax(detection[:, 4:], axis = 1)
    keep_indices = numpy.where(nsfw_scores_raw > 1.0)[0]

    if numpy.any(keep_indices):
        nsfw_scores_raw = nsfw_scores_raw[keep_indices]
        nsfw_scores = nsfw_scores_raw.ravel().tolist()

    return nsfw_scores
```

主要就是下面这一行，关于nsfw置信度的问题，原来是0.2 直接改到1.0就行了，毕竟，置信度不会超过1

```
keep_indices = numpy.where(nsfw_scores_raw > 1.0)[0]
```

重启进程，再次运行：

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-11-102855.png)](https://h4ck.org.cn/wp-content/uploads/2025/05/Screenshot-2025-05-11-102855.png)

现在就会继续往下进行了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/屏幕截图_11-5-2025_102425_127.0.0.1_副本-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_11-5-2025_102425_127.0.0.1_%E5%89%AF%E6%9C%AC-tuya.jpg)

**视频资源文件导致的异常：**最后来说下视频文件异常导致的崩溃，对于一些文件可能会出现下面的错误

```
Analysing:  95%|====================================================   | 3625/3800 [00:19<00:00, 189.67frame/s, rate=0]
Traceback (most recent call last):
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\gradio\queueing.py", line 625, in process_events
    response = await route_utils.call_process_api(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\gradio\route_utils.py", line 322, in call_process_api
    output = await app.get_blocks().process_api(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\gradio\blocks.py", line 2146, in process_api
    result = await self.call_function(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\gradio\blocks.py", line 1664, in call_function
    prediction = await anyio.to_thread.run_sync(  # type: ignore
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\anyio\to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\anyio\_backends\_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
           ^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\anyio\_backends\_asyncio.py", line 967, in run
    result = context.run(func, *args)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\obaby\.conda\envs\facefusion\Lib\site-packages\gradio\utils.py", line 884, in wrapper
    response = f(*args, **kwargs)
               ^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\uis\components\instant_runner.py", line 82, in run
    create_and_run_job(step_args)
  File "E:\facefusion3\facefusion\facefusion\uis\components\instant_runner.py", line 97, in create_and_run_job
    return job_manager.create_job(job_id) and job_manager.add_step(job_id, step_args) and job_manager.submit_job(job_id) and job_runner.run_job(job_id, process_step)
                                                                                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\jobs\job_runner.py", line 11, in run_job
    if run_steps(job_id, process_step) and finalize_steps(job_id):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\jobs\job_runner.py", line 72, in run_steps
    if not run_step(job_id, index, step, process_step):
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\jobs\job_runner.py", line 58, in run_step
    if job_manager.set_step_status(job_id, step_index, 'started') and process_step(job_id, step_index, step_args):
                                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\core.py", line 323, in process_step
    error_code = conditional_process()
                 ^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\core.py", line 340, in conditional_process
    return process_video(start_time)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\core.py", line 418, in process_video
    if analyse_video(state_manager.get_item('target_path'), trim_frame_start, trim_frame_end):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\content_analyser.py", line 102, in analyse_video
    if analyse_frame(vision_frame):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\content_analyser.py", line 77, in analyse_frame
    nsfw_scores = detect_nsfw(vision_frame)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\content_analyser.py", line 115, in detect_nsfw
    temp_vision_frame = fit_frame(vision_frame, model_size)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\facefusion3\facefusion\facefusion\vision.py", line 243, in fit_frame
    height, width = vision_frame.shape[:2]
                    ^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'shape'
```

这些问题还是处在content\_analyser.py 问题在于对vision\_frame 为None的帧进行检测，导致检测进程崩了，这里提前判断下是否为空，当然，更直接的办法是直接全部返回False 禁用nsfw检测。

参考下面的方法修改代码即可。

```
def analyse_frame(vision_frame : VisionFrame) -> bool:
    if vision_frame is None:
        return False
    nsfw_scores = detect_nsfw(vision_frame)

    return len(nsfw_scores) > 0
```

好啦，最后来看看小视频吧：

[<https://danteng.me/video/dbc-1.mp4>](https://danteng.me/video/dbc-1.mp4?_=1)

**如果用姐姐我的照片换脸视频了，换好的视频记得给我发一份，嘻嘻**

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《FaceFusion 3.2.0 — 进阶体验...