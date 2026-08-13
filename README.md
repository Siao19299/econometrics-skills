# 计量经济学 Skills

[English](README_EN.md) | **简体中文**

面向应用计量经济学的可复用 Codex Skills。本项目的 MVP 将实证论文或复现项目转化为三个可审查的工作流：

- `econometrics-audit`：审查目标参数、识别策略、估计方法、统计推断、稳健性与结论强度。
- `econometrics-replication`：审查 Stata、R 和 Python 复现包；默认不执行不受信任的研究代码。
- `econometrics-reviewer`：为实证经济学论文生成有证据依据、边界明确的审稿报告。
- `econometrics-shared`：提供上述三个可触发 Skill 共用的研究契约与质量门槛。

首个版本有意选择“小而深”的方法覆盖范围：OLS 与面板固定效应、工具变量、双重差分与事件研究，以及回归不连续设计。时间序列、合成控制、结构估计、机器学习和空间计量经济学将作为后续扩展方向。

## 安装

将完整的 Skill 目录复制到你的 Codex Skills 目录。请将 `econometrics-shared` 与另外三个可触发 Skill 放在一起，因为它们会在运行时读取其中的参考资料。

```powershell
Copy-Item -Recurse skills\econometrics-* $env:USERPROFILE\.codex\skills\
```

安装后新建一个 Codex 任务。示例请求：

```text
使用 econometrics-audit 审查这篇 DID 论文的识别策略和统计推断。
使用 econometrics-replication 检查这个 Stata 复现包，但不要运行其中的代码。
使用 econometrics-reviewer 为这篇论文撰写一份边界明确的审稿报告。
```

## 设计原则

1. 推荐估计量之前，先定义目标参数。
2. 区分证据、推断和建议。
3. 将识别假设视为需要制度背景支持、诊断检验和明确适用边界的主张。
4. 不得虚构研究结果、模型设定、数据访问情况、稳健性检验、引用或期刊要求。
5. 优先产出可复现的研究材料并使用确定性检查，而不是追求装饰性文字。
6. 对 MVP 尚未覆盖的方法明确标注超出范围，不临时拼凑可能造成误导的检查清单。

## 验证

本项目不依赖任何第三方 Python 软件包。

```powershell
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

## 项目状态

MVP / 草案。工作流和确定性检查已经实现，但在面向多种真实论文和复现包完成前向测试之前，不应将项目状态标记为稳定版。

## 许可证

采用 Apache-2.0 许可证，详见 [`LICENSE`](LICENSE)。
