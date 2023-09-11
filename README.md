# trash-cls

## 待办

- 分页添加资料内容，美化排版。可以用一页介绍用到的技术（streamlit、sentence-transformers、ernie-3.0-nano-zh）
- cls.txt现在是chatgpt生成的，替换成更全面的资料，重新训练模型

## 其他

- 改进训练集构建逻辑：现在的相似度是类别名和类别内垃圾为1，类别名和类别外垃圾为0
- 如果调研垃圾类别多，可以返回多类别结果概率排序
- 漂亮的可视化：类似图谱的查询结果展示、词云等，用wordcloud、pyechatrs等
