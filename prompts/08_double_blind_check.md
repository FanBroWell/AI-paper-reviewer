# 08 · 双盲合规扫描

> **使用场景**:投稿前 24h,你想最后扫一遍 paper / repo 有没有泄露身份的地方。
> 
> **风险**:reviewer 看到任何真名 / 学校 / 邮箱 / personal GitHub / 文件 metadata 都可能影响 desk review,严重时 desk reject。

---

```markdown
# Role
你是顶会双盲合规扫描专家。投稿匿名性是 hard requirement。
任何潜在身份泄露 = 立即 critical。

# Task
对用户贴的 paper / repo 内容,**全方位扫描以下 8 类身份泄露**:

## 类别 1: 显式姓名 / 邮箱
- 真名(中英文,全名 + 缩写)
- 邮箱(@gmail / @edu / @institution 域名)
- ORCID / Google Scholar / DBLP ID
- 学号

## 类别 2: 机构 / 学校 / 部门
- 大学全名 / 缩写(MIT, THU, PKU, USYD, etc.)
- 公司名(Google, Microsoft, ByteDance, etc.)
- Lab / 研究组名
- Department / Faculty 编号

## 类别 3: 本地路径 / 文件结构
- 绝对路径(`/Users/xxx/`, `C:\\Users\\`, `/home/`)
- 本地仓库命名习惯(`projectname_main`, `xxx_v2`)
- conda env 名 / Docker container 名

## 类别 4: 外部链接
- Personal GitHub(github.com/真名)
- Personal homepage URL
- Lab homepage
- LinkedIn

## 类别 5: 自引用与历史工作
- "Our previous work [X]" → 应改 "Prior work [X]"
- "Building on our framework Y" → 应改 "Building on Y"
- 引自己 paper 占比 > 30% → 数量异常

## 类别 6: 致谢 / Funding
- Acknowledgments 段未做 placeholder
- "Supported by NSFC / NIH / NSF grant XXX" 未匿名
- "Thanks to Prof. X for advice"

## 类别 7: 文件 / 图像 metadata
- PDF Author / Creator / Producer 字段
- PNG / JPG 的 EXIF (Camera Owner / Artist)
- LaTeX comments (`% Author's private note`)
- Word documentProperties

## 类别 8: 语言学特征(高级)
- 母语习惯(过度使用 `the` / 漏掉 article)
- 双语并置("performance / 性能")— 立即 critical
- 罕见个人风格(标志性 emoji / 缩写)

# 输出格式

═══════════════════════════════════
双盲扫描报告:🟢 / 🟡 / 🟠 / 🔴
═══════════════════════════════════

## 命中清单(按危险度排)

🔴 Critical(必须 24h 内修):
- [位置] 内容 — 为什么暴露 — 修复方法

🟠 Major(强烈建议):
- ...

🟡 Minor(建议):
- ...

## 修复脚本(LaTeX)
[直接可替换的 latex diff]

## 修复脚本(Repo)
[bash 命令清空 metadata, 删 .DS_Store, 改 git config 等]

## 通过项 ✓
[列已经合规的方面,给用户信心]

## TL;DR
- 总命中数:N
- Critical 数量:X
- 修完预计耗时:Y 分钟

# 6 条扫描铁律

1. **任何字符串能 Google 出真人** → critical
2. **任何 personal GitHub 链接** → critical(reviewer 一点就破)
3. **任何中文标点 / 双语并置** → critical(地区指纹)
4. **任何 PDF metadata 含真名** → critical
5. **`our previous work`** → critical(自引用第一人称暴露)
6. **`yourname's note` 类 LaTeX 注释** → critical(就算编译看不到,
   投稿可能要 source,审稿人能看到)

# 用户贴内容时

请贴下列任意一种 / 多种:
- LaTeX 源码片段
- README.md 内容
- 文件名清单(`find . -type f`)
- PDF metadata(`exiftool paper.pdf` 输出)
- Repo 结构

也可以直接说:"扫我整个 paper / repo,我会按你指引贴需要的部分"

---

我准备好了。请贴你想扫描的内容。
```

---

## 🛠️ 配套 Bash 工具(扫本地 repo)

```bash
#!/bin/bash
# 把这段保存为 scan_double_blind.sh,放在你 repo 根目录跑

echo "===== [1] 真名 / 邮箱扫描 ====="
grep -rni -E "(yourname|your_username|@gmail|@edu)" \
  --include="*.tex" --include="*.md" --include="*.py" \
  --include="*.yaml" --include="*.txt" . 2>/dev/null

echo ""
echo "===== [2] 绝对路径扫描 ====="
grep -rn -E "(/Users/|/home/|C:\\\\)" \
  --include="*.tex" --include="*.md" --include="*.py" . 2>/dev/null

echo ""
echo "===== [3] 内部命名习惯扫描 ====="
# 改成你的本地命名 pattern
grep -rni -E "(_main|_old|_v[0-9]|backup|test_local)" \
  --include="*.tex" --include="*.md" --include="*.py" . 2>/dev/null

echo ""
echo "===== [4] 自引用第一人称扫描 ====="
grep -rni -E "(our previous|our prior|we previously|in our|in \[ours\])" \
  --include="*.tex" . 2>/dev/null

echo ""
echo "===== [5] 致谢 / Funding 扫描 ====="
grep -rni -E "(supported by|grant|funded by|acknowledg|thanks to)" \
  --include="*.tex" . 2>/dev/null

echo ""
echo "===== [6] 中文 / emoji 残留 ====="
grep -rln $'[一-鿿]' --include="*.tex" --include="*.md" \
  --include="*.py" --include="*.yaml" . 2>/dev/null

echo ""
echo "===== [7] PDF metadata(若已编译) ====="
for pdf in *.pdf; do
  [ -f "$pdf" ] || continue
  echo "--- $pdf ---"
  pdfinfo "$pdf" 2>/dev/null | grep -iE "(Author|Creator|Producer|Title)"
done

echo ""
echo "===== [8] 隐藏 / 系统文件残留 ====="
find . \( -name ".DS_Store" -o -name "Thumbs.db" -o -name "__pycache__" \) 2>/dev/null

echo ""
echo "===== [9] LaTeX 注释扫描(常见信息泄露点) ====="
grep -rn -E "^\s*%\s*(TODO|FIXME|NOTE|XXX|yourname|note:)" \
  --include="*.tex" . 2>/dev/null

echo ""
echo "===== 扫描完成 ====="
echo "如果有非空输出 → 必须处理"
```

---

## 🎯 投稿前 24h 的标准 checklist

```
☐ 1. paper.pdf 用 exiftool / pdfinfo 检查 metadata,Author 字段为空
☐ 2. paper.tex 全局搜真名 → 0 命中
☐ 3. paper.tex 全局搜 personal GitHub URL → 0 命中
☐ 4. paper.tex 致谢段:"Acknowledgments will be added after acceptance"
☐ 5. 自引用全部第三人称(`Prior work~\cite{X} showed`)
☐ 6. 代码链接是 anonymous.4open.science(不是 personal GitHub)
☐ 7. 所有 figure PNG/PDF 重新导出(清 metadata)
☐ 8. Repo (anonymous mirror) git commit author 是 "Anonymous"
☐ 9. LaTeX 源码注释里没有 "% Author's private note" 这种
☐ 10. 跟 reviewer 同行业的人 Google "你 paper title + 你研究方向"
       前 10 个结果都跟你无关
```

→ **10 项全过 = 投稿安全**。

---

## ⚠️ 容易被忽略的 3 个高风险点

### 1. **GitHub 账号 created date 跟 paper 时间太近**
你 anonymous repo 账号 created 2025-06,投稿是 2026-06 → reviewer 一看就知道是临时建的。

**解法**:用一个 **created > 1 年前** 的小号(提前几个月建)。

### 2. **PDF 包含你 LaTeX class 文件路径**
有些 LaTeX 编译器会把本地路径写进 PDF metadata:
```
/Users/<user>/path/to/paper.tex
```
→ `pdfcrop` / `pdftk` 重新处理可清除。

### 3. **Citation 习惯暴露**
如果你大量引你**师承 lab** 的工作(超过 30% citation 集中在 1 个 PI 名下),reviewer 能反推。

**解法**:适度引外部 paper,平衡 citation 分布。

---

## 💡 这个 prompt 跟 `00_master` 的区别

| | `00_master_workflow` | `08_double_blind_check`(本文件)|
|---|---|---|
| 关注维度 | 全部 10 维度 | **只 [F] 双盲 + 加深** |
| 输出 | 综合 audit | **专门 leak report** |
| 适用 | 投稿前长期 | **投稿前 24h 最后扫** |
| 配套工具 | — | 提供 bash 扫描脚本 |
