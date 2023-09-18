import streamlit as st

# page config
st.set_page_config(
    page_title='相关研究',
    page_icon='📚',
    layout='wide'
)

st.title('相关研究介绍')


col1, col2 = st.columns(2)

with col1:

    st.subheader('化学篇')

    with st.expander('塑料分类'):

        st.write('塑料分为可回收塑料和不可回收塑料两类。可回收塑料包括聚乙烯、聚丙烯等，可以通过热塑性成型技术进行加工再利用。不可回收塑料如聚氯乙烯、聚苯乙烯等，不能通过这一技术进行再利用，但可以用来生产燃料电池等。')

        st.video('./videos/1.塑料瓶的回收利用.mp4')

    st.divider()

    with st.expander('废弃电池处理'):

        st.write('废弃电池中存在有害金属离子，如铅、镉、汞等。通过化学中的氧化还原反应原理，可以进行专门处理。例如，将废电池放入酸性或碱性溶液中，其中的有害金属离子可以被还原剂还原为金属单质，这些金属单质可以用于其他用途。')

        st.video('./videos/2.废旧电池提炼铅.mp4')
        st.video('./videos/3.废旧电池回收的两条再利用路线.mp4')

    st.divider()

    with st.expander('金属回收'):

        st.write('金属制品同样分为可回收和不可回收两类。可回收金属包括铁、铜、铝等，能够通过熔化和再铸等方式再利用。不可回收金属包括金、银等贵金属，这些金属可以用于生产其他金属或进行贵金属交易。')

        st.video('./videos/4.废旧金属制造铸铁下水道.mp4')

    st.divider()

    with st.expander('污水处理'):

        st.write('利用酸碱中和反应原理可以对污水进行处理。例如，将氢氧化钠溶液加入酸性废水中，可以中和酸性物质。此外，还可以利用缓冲溶液的特性调节废水的pH值，以适应不同的处理要求。选择适当的吸附剂和洗脱剂，可以进一步达到污水净化的目的。例如，活性炭具有许多孔隙结构，可以吸附污水中的有机污染物和重金属离子。')

        st.video('./videos/5.污水处理.mp4')

    st.divider()

    with st.expander('废纸回收'):

        st.write('通过将废纸进行分选、去除污染物、破碎和漂白等处理过程，可以将其转化为再生纸张，用于制造新的纸制用品。')

        st.video('./videos/6.回收废纸再造卫生纸.mp4')

with col2:

    st.subheader('生物篇')

    with st.expander('可降解塑料的合成'):

        st.write('开发和使用可降解塑料，能够在一定程度上减少对环境的负面影响。例如，利用生物降解原理可以合成聚乳酸（PLA），这种塑料可在微生物的作用下降解为二氧化碳和水，用于生产食品包装袋、餐具和农用地膜等。')

        st.video('./videos/7利用甘蔗渣制成可降解餐盘.mp4')

    st.divider()

    with st.expander('有机肥料的生产'):

        st.write('有机废弃物在堆肥过程中由细菌、真菌和蚯蚓等微生物分解，最终转化为有机肥料。这些肥料用于花园和植被项目，提高了植物的生长和健康。')

        st.video('./videos/6厨余垃圾变肥料.mp4')
        st.video('./videos/12生产有机肥料.mp4')
    
    st.divider()

    with st.expander('生物能源的开发'):

        st.write('废弃的植物材料如废旧木材、秸秆或废纸、食物残渣或植物油等可以作为生物质，通过酶和微生物的作用将其发酵，可从中提取生物柴油或生物酒精，减少对化石燃料的依赖。')

        st.video('./videos/8垃圾焚烧变新能源.mp4')
        st.video('./videos/10利用废油和牛皮提炼生物柴油.mp4')
