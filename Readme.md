### 介绍
用树莓派做一个私人助理。


### 帮助
可以先看一下他的运行帮助:

```python
(remind) root@raspberrypi:/www/remind# python remind_index.py -h
test.py -t <taskName> -m <modelName> -v <voice>

-t 指定任务名称
-m 指定模型名称
-v 是否输出声音
```

### 使用姿势

```python
# python remind_index.py -t output_weekly_report -m exclamation -v false
use task: output_weekly_report
use model: exclamation
voice status: False
```

### 模型列表

- forbidden: 禁止图案
- exclamation: 感叹号
- smile: 笑脸

### 参考博客

https://blog.itmonkey.icu/2022/03/01/create-personal-assistant-use-raspberry-pi/
