import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np
import torch


# page config
st.set_page_config(
    page_title='垃圾分类查询系统',
    page_icon='🚮',
    layout='wide'
)

def softmax(x):
    x = [i.cpu().numpy() for i in x]
    return np.exp(x) / np.sum(np.exp(x), axis=0)


# 根据相似度查询最接近的垃圾分类
def get_sim(model, query, corpus, corpus_embeddings, template):

    if query in template.keys():
        st.write('查询结果（数据库）：')
        st.write(template[query])
    
    else:

        top_k = min(4, len(corpus))
        query_embedding = model.encode(query, convert_to_tensor=True)  # 将输入转换为向量

        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]  # 计算相似度
        top_results = torch.topk(cos_scores, k=top_k)  # 获取最接近的k个结果

        result_id, result_score = [], []
        for score, idx in zip(top_results[0], top_results[1]):
            result_id.append(idx)
            result_score.append(score)
        result_score = softmax(result_score)
        result_label = [corpus[i] for i in result_id]


        st.write('查询结果（模型）：')
        for label, score in zip(result_label, result_score):
            st.write(label, "(Score: {:.4f})".format(score))


def app():
    st.title('垃圾分类查询')

    # 模型加载
    model = SentenceTransformer('./model/')

    # 垃圾类型
    corpus = ['干垃圾', '可回收垃圾', '厨余垃圾', '有害垃圾']
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

    # 垃圾分类模板
    template = {'电池': '有害垃圾'}

    # 提交表单
    with st.form(key='trash_cls'):
        input_text = st.text_input('请输入垃圾名称：')

        submit_button = st.form_submit_button(label='查询')
        if submit_button:
            get_sim(model, input_text, corpus, corpus_embeddings, template)

if __name__ == '__main__':
    app()

