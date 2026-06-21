# 一个月CS231n+Python+Linux/tmux全攻略


---

## 一、先把老师要求的所有资源&链接搞明白
### 1. 核心课程与作业链接
| 资源 | 链接 | 作用 |
|------|------|------|
| CS231n 官网（课程笔记/作业入口） | https://cs231n.github.io/ | 看最新课程笔记、下载作业、找参考资料 |
| 2025版作业主页（最新作业） | https://cs231n.github.io/assignments/ | 下载Assignment 1/2/3的代码包 |
| Assignment 1（基础必做） | https://cs231n.github.io/assignments/2025/assignment1_colab.zip | KNN、SVM、Softmax、两层神经网络，入门必做 |
| Assignment 2（CNN核心必做） | https://cs231n.github.io/assignments/2025/assignment2_colab.zip | 卷积层、池化层、BatchNorm，CV核心 |
| Assignment 3（进阶选做） | 同上面作业主页下载 | 图像识别、Transformer，时间紧可只做基础部分 |
| CS229（机器学习入门，可选） | https://cs229.stanford.edu/ | Andrew Ng的经典课，补基础用 |
| 李宏毅台大机器学习课程 | B站/YouTube免费资源 | 补机器学习基础概念 |

---

## 二、必须安装的软件&工具（每个都讲清作用）
按「推荐优先级」排序，小白优先用方案A，再按需求升级方案B。

### 方案A：零配置入门（小白首选，不用装任何软件）
**Google Colab**
- 作用：云端Python运行平台，自带CS231n所有依赖库，打开浏览器就能写代码、跑作业，小白零门槛。
- 缺点：需要科学上网；关闭浏览器后进度会消失，需要手动保存文件。

---

### 方案B：本地安装（长期学习用，按顺序装）
| 软件/工具 | 作用 | 小白友好度 | 安装必要性 |
|-----------|------|------------|------------|
| **Miniconda** | Python环境管理工具，给你的CS231n作业单独建一个“隔离房间”，避免和其他Python项目冲突 | ⭐⭐⭐⭐ | 必装（Anaconda太臃肿，Miniconda更适合小白） |
| **VS Code** | 万能编辑器，写代码、写Markdown笔记、打开Jupyter文件都能用，小白也能快速上手 | ⭐⭐⭐⭐⭐ | 必装（后续所有操作都可以在这里完成） |
| **Python 3.9** | 编程语言，CS231n作业用的就是Python，由Miniconda帮你安装，不用单独装 | - | 由Miniconda自动安装 |
| **Jupyter Notebook/Lab** | 交互式编程工具，CS231n作业的标准格式 `.ipynb` 就是它生成的，能同时放代码、文字、运行结果 | ⭐⭐⭐⭐ | 必装（由Miniconda安装） |
| **WSL2（Windows自带Linux）** | 在Windows里直接运行Linux终端，练习Linux命令、tmux，不用装虚拟机 | ⭐⭐⭐⭐ | 必装（学习Linux/tmux的核心环境） |
| **Git（可选）** | 代码版本管理工具，用来下载CS231n的代码，小白可以暂时不用，直接下压缩包 | ⭐⭐⭐ | 选装 |

---

### 重点回答：Jupyter 是否建议用 VS Code？
**非常建议！而且是小白最优解。**
- 原生Jupyter Notebook是网页界面，操作容易乱，笔记排版也不方便。
- VS Code里打开 `.ipynb` 文件，既能像网页版一样运行代码，又能直接编辑Markdown笔记、一键导出PDF/HTML，还能装插件高亮代码、自动保存，对小白友好度拉满。
- 你所有的作业、笔记，都可以在VS Code里搞定，不用来回切换软件。

---

## 三、软件安装+环境配置保姆级步骤（照着做就行）
### 第一步：安装 Miniconda
1. 官网下载：https://docs.conda.io/en/latest/miniconda.html
   - Windows用户：选 Python 3.9 的 64-bit 版本（你之前已经下载了Windows-x86_64.exe，直接用这个）
2. 安装时**一定要勾选“Add Miniconda3 to my PATH environment variable”**（Windows用户），否则后面命令行找不到conda。
3. 安装完成后，按 `Win+R` 输入 `cmd` 打开命令提示符，输入 `conda --version`，能看到版本号就说明装好了。

### 第二步：安装 VS Code
1. 官网下载：https://code.visualstudio.com/
2. 安装时一路下一步，默认设置就行。
3. 打开VS Code，在左侧「扩展」里安装这3个插件：
   - Python：支持Python代码高亮、运行
   - Jupyter：打开 `.ipynb` 文件、运行代码
   - Markdown All in One：写笔记时一键生成目录、实时预览

### 第三步：创建CS231n专属虚拟环境
打开VS Code的终端（顶部菜单栏「终端」→「新建终端」），依次输入以下命令，每输完一行按回车：
```bash
# 1. 创建名为cs231n的虚拟环境，指定Python 3.9（和作业兼容）
conda create -n cs231n python=3.9 -y

# 2. 激活虚拟环境
conda activate cs231n
# 激活成功后，终端前面会出现 (cs231n) 字样，代表你现在在这个“隔离房间”里

# 3. 安装CS231n需要的所有库
conda install numpy matplotlib scipy jupyter notebook tqdm -y
pip install torch torchvision pillow imageio
```

### 第四步：安装WSL2（Windows自带Linux）
1. 按 `Win+X`，选择「终端管理员」，输入：
   ```bash
   wsl --install
   ```
2. 重启电脑，按提示设置用户名和密码（全小写，记下来）
3. 打开终端，输入 `wsl` 就能进入Linux环境了
4. 在WSL里安装tmux：
   ```bash
   sudo apt update && sudo apt install tmux -y
   ```

---

## 四、一个月最高效学习路径（适配周末时间多）
核心原则：**作业驱动学习，周末攻坚难点，周中碎片化学理论+Python+Linux/tmux**，优先完成老师要求的CS231n作业，同步搞定Python、Linux、tmux。

### 第1周：环境搭建+Python基础+Linux基础命令
| 时间 | 任务 | 目标产出 |
|------|------|----------|
| 周一-周三 | 1. 完成Miniconda+VS Code+WSL安装<br>2. 学Python/Numpy基础（CS231n作业必备）<br>3. 学Linux基础命令（ls、cd、mkdir、cp、rm、mv） | 环境搭建成功，能运行基础Python代码；能熟练用Linux命令操作文件 |
| 周四-周五 | 1. 学文本编辑（nano/vim）+权限管理（chmod）<br>2. 学Python数据结构（列表、字典、numpy数组） | 能用nano新建/编辑文件；能写简单的Python脚本处理数据 |
| 周六-周日 | 1. 在WSL里安装Miniconda，复刻CS231n环境<br>2. 跑通Assignment1的基础代码<br>3. 用Linux命令运行Python脚本 | 能在Windows和Linux里都运行Python代码；会用conda在Linux里管理环境 |

### 第2周：Assignment1完成+Linux进阶+tmux基础
| 时间 | 任务 | 目标产出 |
|------|------|----------|
| 周一-周三 | 学CS231n Lecture 1-3（图像分类、线性分类器、反向传播） | 手写反向传播的公式推导笔记 |
| 周四-周五 | 1. 完成Assignment1前半部分（KNN+SVM）<br>2. 学tmux基础用法（新建会话、分屏、后台运行） | 完成KNN和SVM的代码；能开tmux会话、分屏操作 |
| 周六-周日 | 1. 完成Assignment1全作业（Softmax+两层神经网络）<br>2. 在tmux里跑Assignment1代码，练习后台运行 | 带详细注释的完整作业代码；会用tmux后台运行Python脚本 |

### 第3周：Assignment2完成+Linux进程管理+脚本编写
| 时间 | 任务 | 目标产出 |
|------|------|----------|
| 周一-周三 | 学CS231n Lecture 4-6（CNN、卷积层、池化层、BatchNorm） | 画一张CNN各层原理示意图 |
| 周四-周五 | 1. 完成Assignment2前半部分（卷积层+池化层）<br>2. 学Linux进程管理（ps、top、kill）+日志输出（nohup） | 完成卷积层和池化层的代码；能查看进程、后台运行训练脚本 |
| 周六-周日 | 1. 完成Assignment2全作业（Dropout+全连接层+PyTorch实现）<br>2. 写一个bash脚本，自动激活conda环境、运行训练代码 | 完整作业代码；能写出自动化训练脚本，会保存日志到文件 |

### 第4周：Assignment3基础+笔记整理+产出优化
| 时间 | 任务 | 目标产出 |
|------|------|----------|
| 周一-周三 | 1. 学CS231n Lecture 7-9（经典CNN架构、目标检测、Transformer）<br>2. 完成Assignment3基础部分（预训练模型微调） | 整理VGG/ResNet架构对比表格；完成图像识别基础任务 |
| 周四-周五 | 1. 整理所有作业的代码注释、运行结果<br>2. 写Markdown版的Python+Linux+CS231n笔记 | 每个作业文件夹里都有完整的 `.ipynb` 文件和结果截图；结构化的学习笔记 |
| 周六-周日 | 1. 汇总所有产出，写一份给老师的学习总结报告<br>2. 练习在Linux里用tmux后台跑模型，模拟课题组服务器环境 | 包含学习进度、核心知识点、作业成果、Linux技能的完整报告；能独立在Linux环境下运行CV项目 |

---

## 五、笔记&产出怎么写，才能让老师看到你的认真？
老师想看的不是“完美的代码”，而是**你真的学懂了、思考了**，用两种格式搭配，效果最好：

### 1. Jupyter Notebook（`.ipynb`）：作业的主阵地（必做）
这是你作业的核心产出，也是老师会重点看的文件，必须包含这4部分：
1. **详细代码注释**：每一段关键代码都要加注释，比如 `# 这里计算SVM损失函数的梯度，向量化实现比循环快很多`，哪怕是作业里自带的代码，也要写上你的理解。
2. **Markdown单元格笔记**：在代码之间插入文字，写你的思路、遇到的问题、解决方法，比如“这里矩阵维度不匹配报错，后来打印了X和W的形状，发现是我写错了矩阵乘法顺序”。
3. **完整运行结果**：保留所有运行结果，包括损失曲线、准确率、可视化图片，不要删，老师能看到你的训练过程。
4. **作业总结**：每个作业最后加一个总结模块，写你做这个作业的收获、还有哪些地方没搞懂、后续想怎么深入。

### 2. Markdown笔记（`.md`）：知识点的结构化总结（加分项）
用VS Code写，每个知识点一篇笔记，结构模板直接套用：
```markdown
# CS231n Lecture X：XX知识点学习笔记
## 一、核心概念（是什么）
- 概念1：一句话解释+公式（如果有）
- 概念2：一句话解释+和其他概念的对比

## 二、关键推导/原理（为什么）
（这里写公式推导、算法流程，哪怕抄一遍也要搞懂）

## 三、代码实践（怎么做）
```python
# 这里放作业里的核心代码片段，加上注释
def svm_loss_vectorized(W, X, y, reg):
    # 你的注释：向量化实现SVM损失函数，避免循环，提高效率
    scores = X @ W
    # ... 后面的代码
```

## 四、踩坑记录（重点！）
1. 问题：运行KNN代码时，内存不足报错
   - 解决方法：把batch_size调小，或者用Colab运行
2. 问题：损失函数计算结果和参考值差很多
   - 解决方法：打印矩阵形状，核对公式推导过程，发现自己漏了正则项

## 五、课后思考
1. 这个算法的优缺点是什么？
2. 还有哪些地方没搞懂，后续打算怎么学？
```

---

## 六、给老师的产出文件结构（直接照着建文件夹）
```
CS231n_Study/
├── Environment_Setup.md       # 环境配置记录（装软件遇到的坑+解决方法）
├── Python_Notes/              # Python/Numpy基础笔记
│   ├── numpy_basics.md
│   └── python_scripts/
├── Linux_Tmux_Notes/          # Linux+tmux笔记（老师重点看）
│   ├── linux_commands.md      # 常用命令速查表
│   ├── tmux_guide.md          # tmux用法笔记
│   └── train_script.sh        # 训练脚本示例
├── Lecture_Notes/             # CS231n课程笔记
│   ├── Lecture1_Intro.md
│   ├── Lecture2_Linear_Classifier.md
│   └── ...
├── Assignments/                # CS231n作业文件夹（老师最看重）
│   ├── Assignment1/
│   │   ├── assignment1_colab.ipynb  # 带详细注释的作业代码
│   │   ├── results/                # 运行截图、损失曲线、可视化图片
│   │   └── summary.md              # 作业总结+收获
│   ├── Assignment2/
│   └── Assignment3/
└── Final_Report.md            # 给老师的学习总结报告
```

