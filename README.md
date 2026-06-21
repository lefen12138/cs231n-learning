# 🧠 CS231n Learning Notes

> 斯坦福大学 [CS231n: Deep Learning for Computer Vision](http://cs231n.stanford.edu/) 课程学习记录
>
> 本仓库收录课程讲义笔记、课后作业实现及前置环境配置，供个人学习与复习使用。

![Language](https://img.shields.io/badge/Language-Python-blue)
![Notebook](https://img.shields.io/badge/Jupyter_Notebook-90%25-orange)
![Commits](https://img.shields.io/badge/Commits-40-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 课程简介

**CS231n** 是斯坦福大学开设的深度学习与计算机视觉旗舰课程，系统讲授卷积神经网络（CNN）的理论基础与工程实践，覆盖图像分类、目标检测、语义分割、生成模型、视频理解等前沿方向，是计算机视觉领域最具影响力的公开课之一。

---

## 📂 仓库结构

```
cs231n-learning/
├── Assignment/                        # 课程作业
│   ├── softmax.ipynb                  # 作业：Softmax 线性分类器
│   └── two_layer_net.ipynb            # 作业：两层全连接神经网络
│
├── Lecture_note/                      # 课程讲义笔记（按主题分类）
│   ├── 线性分类器图像分类/
│   ├── 神经网络/
│   ├── 神经网络训练、优化、调参/
│   ├── 损失函数与优化/
│   ├── CNN/
│   ├── RNN/
│   ├── 注意力机制与Transformer/
│   ├── 生成模型/
│   ├── Self-Supervised Learning/
│   ├── Video Understanding/
│   ├── 3D Vision/
│   ├── 语义分割、图像检测、可视化/
│   ├── 视觉-语言模型 & 基础大模型/
│   ├── 大规模分布式训练/
│   └── neural-networks构建/
│
├── Learning of basic command tools/   # 工具学习笔记
│   ├── Linux/                         # Linux 常用命令
│   └── tmux安装及学习                 # tmux 安装与使用
│
└── Environment_Setup.md              # 环境配置指南
```

---

## 📝 讲义笔记概览

| 模块 | 主题 | 关键内容 |
|------|------|---------|
| 🖼️ 图像分类 | 线性分类器图像分类 | KNN、SVM、Softmax、线性分类原理 |
| 🔢 优化基础 | 损失函数与优化 | 梯度下降、SGD、Momentum、Adam |
| 🧬 神经网络 | 神经网络 / 训练优化调参 | 反向传播、激活函数、Dropout、BN |
| 🏗️ 网络构建 | neural-networks 构建 | 网络设计范式、模块化搭建 |
| 📷 卷积网络 | CNN | 卷积层、池化层、经典架构（VGG / ResNet 等） |
| 🔁 循环网络 | RNN | LSTM、GRU、序列建模 |
| 🎯 注意力 | 注意力机制与 Transformer | Self-Attention、多头注意力、ViT |
| 🎨 生成模型 | 生成模型 | GAN、VAE、扩散模型基础 |
| 🔍 检测与分割 | 语义分割、图像检测、可视化 | RCNN系列、YOLO、FCN、特征可视化 |
| 🤖 自监督 | Self-Supervised Learning | 对比学习、MoCo、SimCLR |
| 🎬 视频 | Video Understanding | 时序建模、3D CNN、双流网络 |
| 🌐 3D 视觉 | 3D Vision | 点云、NeRF、3D 表示方法 |
| 🗣️ 视觉语言 | 视觉-语言模型 & 基础大模型 | CLIP、DALL·E、多模态大模型 |
| ⚡ 分布式 | 大规模分布式训练 | 数据并行、模型并行、混合精度 |

---

## 📋 作业实现

| 文件 | 内容描述 |
|------|---------|
| `softmax.ipynb` | Softmax 分类器的从零实现，包含损失计算（cross-entropy）与梯度推导 |
| `two_layer_net.ipynb` | 两层全连接神经网络的前向传播、反向传播及超参数调优 |

---

## 🛠️ 环境配置

详见 [`Environment_Setup.md`](./Environment_Setup.md)，主要包括：

- Python 3.x 环境安装（建议使用 Anaconda / Miniconda）
- 依赖库安装（NumPy、Matplotlib、Jupyter Notebook 等）
- cs231n 课程代码包的本地配置

**快速启动：**

```bash
# 克隆仓库
git clone https://github.com/lefen12138/cs231n-learning.git
cd cs231n-learning

# 创建虚拟环境（推荐）
conda create -n cs231n python=3.9
conda activate cs231n

# 安装依赖
pip install numpy matplotlib jupyter ipython

# 启动 Jupyter Notebook
jupyter notebook
```

---

## 🔧 工具笔记

学习过程中整理的基础工具使用笔记，位于 `Learning of basic command tools/`：

- **Linux 常用命令**：文件操作、权限管理、进程管理、网络命令
- **tmux**：终端复用工具的安装与常用快捷键，适合远程服务器训练模型时使用

---

## 🚀 学习路线建议

```
线性分类器 → 损失函数与优化 → 神经网络 → CNN
    → RNN → 注意力机制 & Transformer
        → 生成模型 / 自监督学习 / 视觉语言模型
            → 目标检测 / 语义分割 / 3D Vision / 视频理解
```

---

## 📚 参考资源

- 🌐 [CS231n 官方网站](http://cs231n.stanford.edu/)
- 📺 [课程视频（YouTube）](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)
- 📖 [CS231n 课程笔记（英文）](https://cs231n.github.io/)
- 🐍 [NumPy 官方文档](https://numpy.org/doc/)

---

## 📄 License

本仓库内容为个人学习笔记整理，课程原版材料版权归斯坦福大学所有。
仓库代码部分采用 [MIT License](./LICENSE) 开源协议。

---

<div align="center">
  <i>持续更新中 · 欢迎 Star ⭐ 和交流</i>
</div>
