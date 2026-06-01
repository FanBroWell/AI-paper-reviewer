# Case 02 · Methodology 符号一致性修复

> **声明**:本案例是虚构的 ML method 段落,用来演示符号冲突的诊断 + 修复流程。

---

## 📝 原始 Methodology 片段

```latex
\subsection{Graph Construction}
We construct an inter-entity graph by computing pairwise Pearson 
correlations. An edge $(i,j) \in E$ is retained whenever 
$|\rho_{ij}| > \theta$, where $\theta$ is the correlation threshold.

\begin{algorithm}
\caption{Graph Construction}
\REQUIRE Price matrix $P$, threshold $\theta$
\STATE Compute correlation matrix $C$
\IF{$|C_{ij}| > \tau$}    % ← τ here, but REQUIRE says θ!
    \STATE $A_{ij} \leftarrow |C_{ij}|$
\ENDIF
\end{algorithm}

\subsection{Evaluation Metric}
We report the Sharpe ratio:
\begin{equation}
SR = \frac{R_t - R_f}{\theta}
\end{equation}
where $\theta$ represents the standard deviation of returns.    % ← θ again, but as std!
```

---

## 🔍 Top-conf-PaperReviewer Audit 结果

### 综合评级: 🔴 **Critical**

### 🔴 关键问题

#### C1. **Algorithm 内部 θ / τ 矛盾**
```
\REQUIRE Price matrix $P$, threshold $\theta$    ← 声明 θ
...
\IF{$|C_{ij}| > \tau$}                            ← 用 τ
```

reviewer 看到 Algorithm 立刻怀疑:"是不是 bug?或者作者抄错?"

#### C2. **θ 在 paper 里有 2 个不同含义**
```
§3.1 Graph Construction:  $|\rho_{ij}| > \theta$       ← threshold
§3.2 Evaluation:           $SR = (R_t - R_f) / \theta$  ← std dev
```

同一个符号在 paper 不同位置代表 2 个不同概念,**reviewer 一对就崩**。

---

## ✏️ 修复方案

### 决策
- **§Graph Construction 用 τ**(标准 threshold 符号)
- **§Evaluation 用 σ**(标准 std dev 符号)
- **θ 完全不用**(避免歧义)

### 修复后

```latex
\subsection{Graph Construction}
We construct an inter-entity graph by computing pairwise Pearson 
correlations. An edge $(i,j) \in E$ is retained whenever 
$|\rho_{ij}| > \tau$, where $\tau \in (0, 1)$ is the correlation 
threshold.

\begin{algorithm}
\caption{Graph Construction}
\REQUIRE Price matrix $P \in \mathbb{R}^{N \times T}$, 
         threshold $\tau \in (0, 1)$
\ENSURE  Adjacency matrix $A \in \mathbb{R}^{N \times N}$

\STATE $A \leftarrow \mathbf{0}^{N \times N}$
\FOR{$i = 1$ to $N$}
    \FOR{$j = i+1$ to $N$}
        \STATE $C_{ij} \leftarrow \text{Pearson}(P_i, P_j)$
        \IF{$|C_{ij}| > \tau$}
            \STATE $A_{ij}, A_{ji} \leftarrow |C_{ij}|$
        \ENDIF
    \ENDFOR
    \STATE $A_{ii} \leftarrow 1$
\ENDFOR
\RETURN $A$
\end{algorithm}

\subsection{Evaluation Metric}
We report the annualized Sharpe ratio:
\begin{equation}
\mathrm{SR} = \frac{\mathbb{E}[R_t] - R_f}{\sigma}\sqrt{T_{\text{ann}}}
\label{eq:sharpe}
\end{equation}
where $\sigma$ is the standard deviation of portfolio returns and 
$T_{\text{ann}}$ is the annualization factor.
```

---

## 📊 关键改动

| # | 原文 | 改后 | 理由 |
|---|---|---|---|
| 1 | Algorithm REQUIRE θ + IF τ | 全用 τ | 内部一致性 |
| 2 | SR 公式用 θ | 改用 σ | std dev 标准符号 |
| 3 | "θ represents std dev" | "σ is std dev" | 跟上面对应 |
| 4 | `SR` 没用 `\mathrm` | `\mathrm{SR}` | upright operator |
| 5 | Algorithm 缺 ENSURE | 加 ENSURE | 算法描述完整 |
| 6 | `j = i to N`(冗余) | `j = i+1 to N` + self-loop 单独 | 去掉冗余迭代 |

---

## 🎓 takeaway

### 1. **顶会论文的符号管理是 hard requirement**
读者读 paper 像读代码 — 同一个变量名代表不同变量 = bug。

### 2. **数学符号 macro 化是好习惯**
```latex
\newcommand{\thresh}{\tau}
\newcommand{\stddev}{\sigma}
\newcommand{\corr}{\rho}
```

→ 正文用 `\thresh = 0.9`,以后想改全局符号,**只改 macro 一行**。

### 3. **Algorithm 必须**
- REQUIRE / ENSURE 完整
- 内部变量类型明确
- 不冗余 / 不矛盾

### 4. **每个 equation 后必须 "where ..."**
没解释的 equation 等于装饰。

---

## 🔗 相关 prompt

- 完整方法学审稿: [`prompts/05_method_polish.md`](../prompts/05_method_polish.md)
- 数学符号一致性: [`prompts/10_math_notation_check.md`](../prompts/10_math_notation_check.md)
