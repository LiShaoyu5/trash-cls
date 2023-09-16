import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np
import torch


# page config
st.set_page_config(
    page_title='垃圾分类查询系统',
    page_icon=':wastebasket:',
    layout='wide'
)



def softmax(x):
    x = [i.cpu().numpy() for i in x]
    return np.exp(x) / np.sum(np.exp(x), axis=0)


# 根据相似度查询最接近的垃圾分类
def get_sim(model, query, corpus, corpus_embeddings):

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

    return result_label, result_score
    

def app():
    st.title('垃圾分类查询应用')

    # 模型加载
    model = SentenceTransformer('./model/')

    # 垃圾类型
    corpus = ['其他垃圾', '可回收垃圾', '易腐垃圾', '有害垃圾']
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

    trash = {
        '教室内': {
            '可回收垃圾': ['纸张', '粉笔盒', '笔壳', '书', '作业本'],
            '其他垃圾': ['粉笔灰', '粉笔头', '铅笔屑', '小铅笔', '用过的笔芯', '橡皮屑', '灰尘', '用过的纸巾', '修正带'],
            '有害垃圾': ['涂改液', '胶水', '胶棒', '胶带', '打印机墨盒', '打印机色带', '过期药品', '废电池', '废油漆', '废荧光灯管', '废矿物油', '废农药', '废杀虫剂', '废水银温度计', '废水银血压计']
        },
        '办公室内': {
            '可回收垃圾': ['纸张', '矿泉水瓶', '报纸', '杂志', '快递盒', '牛奶盒', '包装盒', '纸盒', '易拉罐', '塑料瓶', '塑料袋', '塑料碗', '塑料盒', '塑料玩具', '塑料衣架', '塑料杯', '塑料餐具', '塑料文件袋', '塑料文件夹'],
            '其他垃圾': ['用完的胶水盒', '润喉糖包装纸', '用过的笔芯', '用过的纸巾', '修正带', '粉笔灰', '粉笔头', '铅笔屑', '铅笔', '橡皮屑', '灰尘', '废弃的打火机', '废弃的香水瓶', '废弃的口红', '废弃的指甲油', '废弃的眼影', '废弃的粉饼', '废弃的粉底液', '废弃的睫毛膏', '废弃的眉笔'],
            '易腐垃圾': ['茶叶渣', '水果核', '水果皮', '植物叶', '植物枝', '植物根', '剩菜剩饭', '骨头', '蛋壳', '花卉', '绿植'],
        },
        '医务室内': {
            '可回收垃圾': ['药物盒'],
            '其他垃圾': ['消毒棉球', '退热贴', '棉棒', '废弃创可贴', '胶带', '用过的纸巾'],
            '有害垃圾': ['废弃水银温度计', '废弃水银血压计', '废弃药品', '废弃药片', '废弃药瓶', '废弃药膏']
        },
        '打印室内': {
            '可回收垃圾': ['废弃纸张', '纸盒'],
            '有害垃圾': ['打印机墨盒', '硒鼓', '废电池']
        },
        '医务室内': {
            '可回收垃圾': ['药物盒'],
            '其他垃圾': ['消毒棉球', '退热贴', '棉棒', '废弃创可贴', '胶带', '用过的纸巾'],
            '有害垃圾': ['废弃水银温度计']
        },
        '卫生间内': {
            '其他垃圾': ['用过的纸巾', '用过的卫生用品']
        },
        '校园内': {
            '可回收垃圾': ['废弃球类', '羽毛球拍', '金属', '废金属', '废旧金属', '铁', '铜', '铝', '锌', '锡', '镍', '铅', '钢', '合金'],
            '其他垃圾': ['灰尘'],
            '易腐垃圾': ['落叶', '树枝'],
            '有害垃圾': ['废弃电池', '污水']
        },
        '食堂内': {
            '可回收垃圾': ['牛奶盒', '纸盒', '易拉罐'],
            '其他垃圾': ['用过的纸巾', '塑料袋'],
            '易腐垃圾': ['剩菜剩饭', '骨头', '果皮', '蛋壳']
        },
        '宿舍内': {
            '可回收垃圾': ['用过的牙膏管', '纸盒', '纸张', '旧衣物', '塑料瓶'],
            '其他垃圾': ['灰尘', '废弃牙刷'],
        }
    }

    trash_type = {}
    trash_scene = {}
    for scene, trash_dict in trash.items():
        for trash_type_, trash_list in trash_dict.items():
            for trash_ in trash_list:
                trash_type[trash_] = trash_type_
                if trash_ not in trash_scene.keys():
                    trash_scene[trash_] = []
                trash_scene[trash_].append(scene)

    # 提交表单
    with st.form(key='trash_cls'):
        

        st.subheader('垃圾分类查询')

        input_text = st.text_input('请输入垃圾名称：')

        submit_button = st.form_submit_button(label='查询')
        if submit_button:

            col1, col2 = st.columns(2)
            with col1:
                if input_text in trash_type.keys():
                    st.write('查询结果（规则）：')
                    st.write('垃圾类型:', trash_type[input_text])
                    st.write('一般出现在', trash_scene[input_text])
                else:
                    result_label, result_score = get_sim(model, input_text, corpus, corpus_embeddings)
                    for label, score in zip(result_label, result_score):
                        st.write(label, "(Score: {:.4f})".format(score))
            with col2:

                if '塑料' in input_text:
                    st.video('./videos/1.塑料瓶的回收利用.mp4')
                elif '电池' in input_text:
                    st.video('./videos/2.废旧电池提炼铅.mp4')
                    st.video('./videos/3.废旧电池回收的两条再利用路线.mp4')
                elif '金属' in input_text or '铁' in input_text or '铜' in input_text or '铝' in input_text or '锌' in input_text or '锡' in input_text or '镍' in input_text or '铅' in input_text or '钢' in input_text or '合金' in input_text:
                    st.video('./videos/4.废旧金属制造铸铁下水道.mp4')
                elif '污水' in input_text:
                    st.video('./videos/5.污水处理.mp4')
                elif '纸' in input_text:
                    st.video('./videos/6.回收废纸再造卫生纸.mp4')


if __name__ == '__main__':

    st.title('基于Python的校园垃圾分类及绿色应用')

    st.subheader('摘要')

    st.write('垃圾分类是垃圾回收利用和科学处理的重要环节，能够有效保护环境，提升生活水平。校园垃圾分类是校园卫生安全的重要组成部分，与师生的健康体魄、快乐学习、幸福工作息息相关。由于缺乏相关宣传教育，在校园生活中，师生垃圾分类意识薄弱，不清楚垃圾如何分类及如何回收利用。本项目利用Python编程创建网页，集搜索、科普功能为一体，让师生可通过电脑、手机随时随地查询校园常见垃圾所属类别，并了解学习如何通过化学、生物知识对其进行处理与再次利用。师生增强垃圾分类和环境保护的意识，养成相关习惯，能够改善校园风貌，提升校园生活质量和幸福水平。')

    st.subheader('研究背景')

    st.write('自2019年起，我国各地开始陆续实行垃圾分类，这是对垃圾进行回收利用和科学处理的重要环节，有助于减少垃圾数量，提高其利用率，从而科学有效地保护生活环境，提高生活品质，满足人们对于美好生活的追求。目前，由于垃圾分类知识宣传不够普及等种种原因，学校师生垃圾分类意识薄弱，很多人不知如何进行垃圾分类和回收利用，导致校园垃圾分类效果不佳，回收处理麻烦，在一定程度上造成资源和经济浪费，不利于文明校园和文明城市的建设。')

    st.subheader('研究目的')

    st.write('校园作为一个小型聚居区，有不同的功能区域，如教学区、办公区、住宿区、餐饮区、实验室等。每一个区域的功能不同，也产生着不同的垃圾。如教学区、办公区产生的垃圾主要为纸张、旧笔芯等；住宿区产生的垃圾主要为塑料瓶、包装盒等生活垃圾；餐饮区产生的垃圾主要为厨余垃圾；实验室产生的垃圾主要是实验垃圾。校园内的这些垃圾不仅可以按照不同区域分类放置处理，还可以根据具体的垃圾种类进行分类，便于回收利用，节约资源。比如1吨废纸回收利用后可再造0.8吨纸张，大大减少了对木材的浪费。')

    st.write('在校园进行垃圾分类及应用宣传普及教育，能够增强师生垃圾分类意识和环保意识，让大家认识到垃圾分类的重要性，养成勤俭节约保护环境的生活观念和习惯。广大师生联系着千家万户，在走出校园之后也能将垃圾分类及绿色应用知识传播给更多的人，能够大大促进社会生态文明的建设。')

    
    app()

