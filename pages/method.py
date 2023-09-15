import streamlit as st

# page config
st.set_page_config(
    page_title='技术介绍',
    page_icon='💻',
    layout='wide'
)

st.title('使用技术')

st.write('本节将介绍我们在项目中使用到的技术和具体的操作流程。')


st.subheader('Sentence-Transformers')

st.markdown(
    '''
    [Sentence-Transformers](https://www.sbert.net/index.html)是一个应用最先进的预训练模型进行文本编码、相似度计算等任务的Python框架。
    我们使用Sentence-Transformers构建了语义搜索功能。其核心思想是将文本嵌入到向量空间中，然后从预料中查找相似度最高的文本：
    '''
    )
st.image('pages/vector_space.png')

st.write('具体来说，垃圾分类的查询分为以下步骤：')
st.markdown(
    '''
    1. 读取用户输入的垃圾名称。
    2. 如果用户输入的垃圾名称在本地数据库中，则直接返回查询得到的分类结果。
    3. 如果用户输入的垃圾名称不在本地数据库中，则使用Sentence-Transformers计算用户输入的垃圾名称与本地数据库中所有垃圾类别的相似度，返回相似度最高的垃圾类别。
    '''
    )

st.subheader('ERNIE')

st.markdown(
    '''
    Sentence-Transformers库基于预训练的语言模型进行文本编码和之后的相似度计算。我们选择了百度开发的文心模型[ernie-3.0-nano-zh](https://huggingface.co/nghuyong/ernie-3.0-nano-zh)。相比于BERT等流行的预训练模型，我们使用的模型具有以下优点：
    1. 预训练模型的效果极大地依赖于训练的语料。百度在中文自然语言处理领域有深厚的技术积累，其业务场景也保证了训练数据的丰富性。
    2. 我们希望项目能够在各种硬件环境上快速运行。BERT模型体积大、速度慢，而我们选择的ernie-3.0-nano-zh是从文心大模型上蒸馏而来，体积仅有BERT的五分之一，即使在物联网设备上也能快速运行。

    在选定预训练模型后，我们还需要进行训练以使模型更好地适配垃圾分类的任务。我们在收集资料的阶段就整理了每个垃圾分类下的很多具体垃圾名称，可以作为训练数据。
    Sentence-Transformers在训练模型时，训练数据的格式为：'[text1, text2, similarity]'，即两段文本和它们的相似度。我们将每个垃圾类别和对应的垃圾相似度定义为1，垃圾类别与其他类垃圾的相似度定义为0，构建了训练数据集并进行训练，提升了模型的效果。
    '''
    )

st.subheader('Streamlit')

st.markdown(
    '''
    我们的小组成员都没有编写web页面或可视化界面的经验，因此选择了[Streamlit](https://streamlit.io/)构建展示界面。这是一个专为数据科学领域的从业者编写的Python库，具有以下特点：
    1. 完全使用Python开发，不需要其他UI相关语言的经验。
    2. 可以实时预览，任何内容的改动都可以立即看到效果。
    3. 方便部署，不需要任何额外操作即可将项目导出为web应用。
    其中第三点给了我们很大帮助，因为我们不具备购买或租用服务器并部署web应用的条件，而Streamlit云提供了免费的运行环境，我们只需要将项目上传到Github，就可以通过[Streamlit Community Cloud](https://streamlit.io/cloud)发布项目，让所有人通过网络访问。
    '''
    )
