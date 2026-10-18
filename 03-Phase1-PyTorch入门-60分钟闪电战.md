# Phase 1 · PyTorch 入门 · 60 分钟闪电战（前置：节点 0 过）

> 主料：pytorch-cn「Deep Learning with PyTorch: A 60 Minute Blitz」——官方把 PyTorch 最核心的四件事压成一小时的四部分。我们拆成四节，每节：先讲为什么 → 逐行读官方示例 → 自己改一点跑一遍。
> 学习时间自定；四部分跑通 + 费曼过关即毕业。

## 学习地图（顺序固定）

1. **Tensors（张量）**：就是「numpy 数组 + 能上 GPU」。创建/形状/切片/搬运 `.to("cuda")`——numpy 学的每一招都平移过来
2. **Autograd（自动求导）**：`requires_grad` / `backward()`——PyTorch 帮你算梯度，但你要知道它在算什么
3. **Neural Networks（nn）**：`nn.Module` 图纸 / `forward` 前向 / 损失 / 反传——把「网络」看成一堆可调旋钮的函数
4. **Training a Classifier（第一个分类器）**：MNIST 手写数字识别（约 60MB）——训练循环第一次完整转起来（彩色图 CIFAR-10 推迟到 Phase 3，配 CNN 一起下）

**数学按需补**：梯度=斜率直觉（链式法则细节 Phase 2 补）

## 项目① · blitz 代码本

- 四部分官方示例逐行跑通，每部分存一个 `.py`
- 每部分改 1-2 个参数（学习率/神经元数/epoch）看效果，记进笔记
- 第 4 部分 MNIST 约 60MB，**下载前报流量，等确认才动**

## 节点 AI-p1（Phase 1 → 2 的 gate，三件套）

- [ ] 跑通：四部分脚本全部运行成功，MNIST 分类器出第一条 loss 曲线（贴训练日志末几行原文）
- [ ] GitHub 仓库：四个脚本 + README（怎么跑 / 四部分各学到什么）
- [ ] 复盘博客：讲清「一次 `backward()` 到底发生了什么」（费曼检验点）

过 → 开 [04-Phase1.5](04-Phase1.5-数据分析与经典机器学习.md)。

## 硬件提醒

- MNIST + 小网络：8GB 显存绰绰有余；batch_size 128 起步，爆了减半
- 训练时关浏览器多余标签 + 微信
