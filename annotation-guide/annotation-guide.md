# Praat 元音标注操作规范 v0.2

## 基本指南

### 软件安装

下载对应 OS 版本的 Praat。一般来说是 Windows 64-bit，如果是 ARM64 架构的处理器就下载 arm64 版本。

[下载地址](https://www.fon.hum.uva.nl/praat/)

![image-20250224001832190](/eurfelux/assets/images/annotation-guide/image-20250224001832190.png)

![image-20250224001915551](/eurfelux/assets/images/annotation-guide/image-20250224001915551.png)

### 读取文件

安装并打开 Praat 后，会出现两个窗口`Praat Objects`和`Praat Picture`。

![image-20250224005151814](/eurfelux/assets/images/annotation-guide/image-20250224005151814.png)

先不用管`Praat Picture`，来看`Praat Objects`。

上方有 4 个下拉菜单，分别是`Praat`, `New`, `Open`和`Save`。我们现在暂时只需要关心`Open`。

![image-20250224005421041](/eurfelux/assets/images/annotation-guide/image-20250224005421041.png)

在这里，可以通过`Read from file...`来导入语音文件或`TextGrid`文件。

标注工作需要同时读入音频文件与`TextGrid`文件。读入匹配的两个文件后，通过`Ctrl`同时选中两个对象，然后点击右侧的`View & Edit`即可开始编辑。

进去的时候可能会跳一个警告，提示字体缺失，这个不用管。

### 标注

![image-20250310035928971](/eurfelux/assets/images/annotation-guide/image-20250310035928971.png)

进入编辑界面可以看到，上方出现了音频的波形图，中间暂时什么也没有，下方是现有的标注。右侧是用于音素标注的若干国际音标，我们不需要管这个。

> 可能因为未知 bug 导致左下角的按钮 UI 有部分看不见，暂时没有修复方法，有时自己就好了。

选中一段波形，点击左下角的 `sel` 按钮即可专注于这部分音频。

> 其它几个按钮：
>
> - `all`：视野拉到整段音频
> - `in`：放大
> - `out`：缩小
> - `bak`：返回。在多次使用`sel`时很好用。
>
> 如果没有看到共振峰（中间图上的红色散点），就在上方菜单找到`Formants -> Show formants`并选中。

可以更清晰地看到下方已经有若干标注。其中没有文字的区间为自动标注的空白段，空白段表示这一段为非元音段。

放大后，可以看到这里已经标注了元音 `i` 。按住边界拖动即可调整这段标注的开始时间和结束时间。

> 快捷键`Ctrl+Z`可能无法使用。如果出现这种情况，可以通过在上方 Edit 中找到撤销选项来撤销。
>
> ![image-20250224055136298](/eurfelux/assets/images/annotation-guide/image-20250224055136298.png)

### 如何判断元音稳定段

标注时应该标注元音稳定段。那么什么是元音稳定段呢？

> **稳定段（或核心段）**：这是元音的主要部分，声音相对平稳，音高、音质等特征变化较少，通常持续的时间较长。稳定段是分析元音的核心部分，也是标注元音时最常标注的部分。
>
> 在进行元音标注时，稳定段通常是指元音发音中最"平稳"或最"恒定"的部分。这一段通常用于描述元音的特征，如音高（F0）、音质（共振峰）等。对于元音的稳定段标注，您通常会选择音频中变化较小且没有明显过渡或衰退的部分进行标注。

简单来说，就是元音发音最稳定的部分。可以看下图，这个 `a` 的波形图看起来就很稳定，振幅变动很小。

![image-20250331053252260](/eurfelux/assets/images/annotation-guide/image-20250331053252260.png)

而像下面图中这种标注就不行。这个 `a` 虽然音高稳定，但波形图后半部分渐弱，而且前半部分 F1 共振峰变化大。

![image-20250331054007758](/eurfelux/assets/images/annotation-guide/image-20250331054007758.png)

这里就根据共振峰，截掉 F1 的爬升阶段，再根据语谱图和波形图，选取中间的稳定段。

![image-20250331054523809](/eurfelux/assets/images/annotation-guide/image-20250331054523809.png)

### 添加区间边界的方法

下面用一个例子来说明怎么添加区间边界。如下图所示，`ow` 和 `i` 相邻，假如我想要缩小 `ow` 的区间段，但是如果直接调整右边界就会导致 `i` 的区间增大，这种时候就应该添加新的边界。

![image-20250224055911279](/eurfelux/assets/images/annotation-guide/image-20250224055911279.png)

首先选中想要添加边界的时间点，找到上方菜单`Interval`中的`Add interval on tier 1`即可添加边界。或者，如果有效的话，尝试快捷键`Ctrl+1`。

![image-20250224055732689](/eurfelux/assets/images/annotation-guide/image-20250224055732689.png)

另一种方法是点击这个圆形标记，也可以添加边界。

![image-20250224060059893](/eurfelux/assets/images/annotation-guide/image-20250224060059893.png)

### 参数设置

在上方菜单中找到`Formants -> Formant settings...`。

![image-20250224060352180](/eurfelux/assets/images/annotation-guide/image-20250224060352180.png)

推荐设置为：

- Formant ceiling
  - 男性：最高 4000Hz
  - 女性：最高 4600Hz
- Number of formants：`4.0`
- Window length：`0.04`

Formant ceiling 可进行微调，只要频谱图中的共振峰曲线清晰分明即可。曲线质量参考下图：

![image-20250224061001543](/eurfelux/assets/images/annotation-guide/image-20250224061001543.png)

## 文本

> 有一次，北风和太阳正在争论谁比较有本事，他们正好看到有个穿着大衣的人走过，他们就说，谁可以让那个人脱掉那件大衣，就算谁比较有本事。于是*北方*开始拼命的吹，怎知他吹得越厉害，那个人就越是用大衣包紧自己，最后北风没办法就放弃了，接着太阳出来晒了一会儿，那个人感觉变得很热，立刻把大衣脱掉了，于是北风只好认输了。
>
> （PS 这里的*北方*是收集数据时提供的文本中出现的错误。可能会有一些被试修正为*北风*。）

目的是校对 i, y, a, u, o（衣、于、啊、乌、哦）五种元音的标注区间，将其调整到准确的位置。下面会用粗体把含元音的字标记出来，并附部分该元音的频谱图以供参考。

### 含 i 的部分

> 有**一**次，北风和太阳正在争论谁**比**较有本事，他们正好看到有个穿着大**衣**的人走过，他们就说，谁可**以**让那个人脱掉那件大**衣**，就算谁**比**较有本事。于是北方开始**拼命**的吹，怎知他吹得越**厉**害，那个人就越是用大**衣**包**紧**自**己**，最后北风没办法就放**弃**了，接着太阳出来晒了**一**会儿，那个人感觉变得很热，**立**刻把大**衣**脱掉了，于是北风只好认输了。

参考谱图：

![image-20250216232255514](/eurfelux/assets/images/annotation-guide/image-20250216232255514.png)

### 含 y 的部分

> 有一次，北风和太阳正在争论谁比较有本事，他们正好看到有个穿着大衣的人走过，他们就说，谁可以让那个人脱掉那件大衣，就算谁比较有本事。**于**是北方开始拼命的吹，怎知他吹得越厉害，那个人就越是用大衣包紧自己，最后北风没办法就放弃了，接着太阳出来晒了一会儿，那个人感觉变得很热，立刻把大衣脱掉了，**于**是北风只好认输了。

参考谱图：

![image-20250331054933657](/eurfelux/assets/images/annotation-guide/image-20250331054933657.png)

### 含 a 的部分

> 有一次，北风和太**阳**正在争论谁比较有本事，**他**们正好**看**到有个**穿**着**大**衣的人走过，**他**们就说，谁可以**让***那*个人**脱**掉*那*件**大**衣，就**算**谁比较有本事。于是北*方*开始拼命的吹，怎知**他**吹得越厉害，*那*个人就越是用**大**衣包紧自己，最后北风没**办法**就**放**弃了，接着太**阳**出来晒了一会儿，*那*个人**感**觉变得很热，立刻**把大**衣脱掉了，于是北风只好认输了。

参考谱图：

![image-20250331055259331](/eurfelux/assets/images/annotation-guide/image-20250331055259331.png)

### 含 u 的部分

> 有一次，北风和太阳正在争论谁比较有本事，他们正好看到有个穿着大衣的人走过，他们就说，谁可以让那个人脱掉那件大衣，就算谁比较有本事。于是北方开始拼命的吹，怎知他吹得越厉害，那个人就越是**用**大衣包紧自己，最后北风没办法就放弃了，接着太阳**出**来晒了一会儿，那个人感觉变得很热，立刻把大衣脱掉了，于是北风只好认**输**了。

参考谱图：

![image-20250331055753903](/eurfelux/assets/images/annotation-guide/image-20250331055753903.png)

### 含 o 的部分

> 有一次，北**风**和太阳*正*在*争*论谁比较有本事，他们*正*好看到有*个*穿*着*大衣的人走**过**，他们就**说**，谁*可*以让那*个*人**脱**掉那件大衣，就算谁比较有本事。于是北*方*开始拼命的吹，怎知他吹得越厉害，那*个*人就越是用大衣包紧自己，最后北**风**没办法就放弃了，接着太阳出来晒了一会儿，那个人感觉变得很热，立*刻*把大衣**脱**掉了，于是北**风**只好认输了。

参考谱图：

![image-20250331055919271](/eurfelux/assets/images/annotation-guide/image-20250331055919271.png)

### 关于口音

可能出现口音区别的字在上方文本中用斜体表示。

- “那个”在口语中常常发音成“内个”，需判断“那”是否为 na。
- 有的人会把 e 发成 o，比如“可以”说成“阔以”，“着”说成 zhuo。需要判断是否为 o。

## 质量控制

1. 时长标准：最小标注时长 25ms，过短的元音段需要记录下来并报告
2. 交叉检验：选择小部分样本多人标注，要求边界误差 $\leq$ 20ms
