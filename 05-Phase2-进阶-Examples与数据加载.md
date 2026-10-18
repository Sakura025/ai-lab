# Phase 2 · 进阶 · Learning with Examples 与数据加载（前置：AI-p1.5 过）

> 主料：pytorch-cn「Learning PyTorch with Examples」+「Data Loading and Processing Tutorial」。
> 这一阶段把「深度学习 = 梯度下降」从口号变成肌肉记忆——**同一件事用三种深度各写一遍**。

## 学习地图（顺序固定）

1. **Warm-up：numpy 手写网络**：纯 numpy 拟合 y=wx+b——看见「没有框架时梯度要手算」的痛
2. **Tensor 版**：同样的网络换 torch tensor + `.to("cuda")`——快，但梯度还是要自己写
3. **Autograd 版**：加 `requires_grad`，`backward()` 自动出梯度——第一次体会框架替你做了什么
4. **nn + optim 版**：`nn.Module` 定义结构 + `optim` 管更新——标准姿势，以后都这么写
5. **自定义模块 + 控制流**：网络里写 if/for（教程的权重共享示例）
6. **Dataset / DataLoader**：自定义数据集怎么喂数据（`__getitem__` / 批量 / 打乱）

**数学按需补**：链式法则（复合函数的导数连乘）——autograd 的全部秘密

## 项目② · 三版对照实验

- 同一个拟合任务，numpy / tensor / nn+optim 三版代码并排，各跑通
- 每版记录最终 loss + 耗时，写进 README 对照表
- 加一段自定义 Dataset（合成数据即可，0 下载）

## 节点 AI-p2（三件套）

- [ ] 跑通：三版代码全部收敛（loss 明显下降），自定义 Dataset 能出批
- [ ] GitHub 仓库 + README（对照表 + 各版差异一句话）
- [ ] 复盘博客：讲清「三版之间每一步替我省了什么」（费曼检验点）

过 → 开 [06-Phase3](06-Phase3-核心-CNN与迁移学习.md)。

## 流量提示

- 本阶段 0 下载（合成数据 + 教程内置示例）
