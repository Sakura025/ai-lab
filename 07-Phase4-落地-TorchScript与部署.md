# Phase 4 · 模型落地 · 保存加载与 TorchScript（前置：AI-p3 过）

> 主料：pytorch-cn TorchScript 教程 + 官方 Saving and Loading Models。
> 训练只是半个项目——模型要能存、能取、能交给别人跑，这是作品「可交付」的一步。

## 学习地图（顺序固定）

1. **保存/加载**：`state_dict` 存取、checkpoint 断点续训——为什么不能只存整个模型对象
2. **TorchScript 基础**：tracing 把 Python 模型变成可独立运行的图
3. **（可选）ONNX 导出**：跨框架交换格式，导出可视化看一眼
4. **推理脚本**：一条命令加载模型 → 对新输入出预测

## 项目④ · 交付一个「能用的模型」

- 把 Phase 3 训好的模型：存成 checkpoint → 加载恢复推理 → 导出 TorchScript 版
- 写 `predict.py`：输入一张图（或一个样本），输出预测结果
- （可选加分）ONNX 导出成功

## 节点 AI-p4（三件套）

- [ ] 跑通：checkpoint 存取 + TorchScript 推理脚本运行成功（贴终端原文）
- [ ] GitHub 仓库：模型文件说明 + predict.py + README
- [ ] 复盘博客：讲清「保存的到底是什么」（state_dict 白话）

过 → 开 [08-Phase5](08-Phase5-毕业项目-自选方向.md)。

## 流量提示

- 本阶段 0 新下载（复用 Phase 3 的模型与数据）
