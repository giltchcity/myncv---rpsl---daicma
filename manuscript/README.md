# DynaState 论文编辑入口

格式采用官方 [CVPR2027-v1](https://github.com/cvpr-org/author-kit/releases/tag/CVPR2027-v1)。正文 teaser 使用官方 `strip` 写法，位于第一页标题下方。

- `main.tex`：完整正文，含摘要、各章节、所有正文表格、图的排版和图注。
- `experiments_supplement.tex`：完整补充材料，含补充表格和图。
- `main.bib`：正文与补充材料共用的唯一文献库。
- `figures/`：实际引用的 PDF、PNG、JPG 等图片素材。
- `cvpr.sty`、`ieeenat_fullname.bst`：会议格式文件。

正文和补充材料都可以独立编译，不再依赖分散的章节或图表 `.tex` 文件。
在 Overleaf 选择 `manuscript/main.tex` 作为 Main document；编译补充材料时选择
`manuscript/experiments_supplement.tex`。

## 修改参考文献

所有 BibTeX 条目都在 `main.bib`。替换作者、标题、会议、年份等字段时保留条目 key，
例如 `@article{some_key, ...}` 中的 `some_key`，正文的 `\cite{some_key}` 就无需逐处修改。
若修改 key，同时在两个 `.tex` 中替换对应引用。合并时保留了原有文献条目，没有代替作者改写信息。

## 编译

```sh
latexmk -pdf main.tex
latexmk -pdf experiments_supplement.tex
```

2026-11-03 的旧分散源码已备份在工作目录之外的 `paper_structure_cleanup_20261103/`。
每个章节和图表在 `.tex` 内都有 BEGIN / END 注释，便于搜索定位。
