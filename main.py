import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'


#st.sidebar.write でサイドバーへ
st.write('Interactive Widgets')

#2カラムの導入
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#expander
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text, 'です'

#スライダー　("str", 最小，最大，初期値)
condition = st.slider('あなたの調子は', 0, 100, 50)
'コンディション:', condition


st.write('Displya Image')

#セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えてください．',
    list(range(1, 11))
)
'あなたの好きな数字は，', option, 'です'

#チェックボックス
if st.checkbox('Show Image'):
    #画像表示
    img = Image.open('penguin.jpeg')
    st.image(img, caption='penguin', use_column_width=True)


st.write('DataFrame')

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df2)

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
#折れ線グラフ
st.line_chart(df)
#エリアチャート
st.area_chart(df)
#棒グラフ
st.bar_chart(df)

#st.write st.dataframe
#どちらでも表示できるが，dataframeだと引数で大きさを指定できる
#st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

#静的な表を表示させるとき，st.tableを使える
#st.table(df.style.highlight_max(axis=0))

#マジックコマンド
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""