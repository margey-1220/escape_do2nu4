import streamlit as st
from PIL import Image



class KaitouBon(object):

    def __init__(self):
        self.img_file_generator = self._images_generator()
        self._def_text()
        pass

    def _def_text(self):
        self.title = '怪盗ぼんじゅうるからの挑戦状'
        self.last_question = '# 怪盗ぼんじゅうるが盗んだものは何？'
        self.last_answer = 'テキストボックス'
        self.txt_epilogue = \
        """
        # エピローグ

        ドズルが無くしたもの...\n
        一体それはなんだったのでしょうか。\n
        ここで皆さんは最初のプロローグでのドズルのコメントを思い出す必要がありました。\n
        そう、ドズルは怪盗じゃない方のぼんじゅうるに「ドズ主の心」を奪われていたのです。\n
        つまり、最後の回答に「ドズ主の心」を入力したあなたこそが、ドズルチャンネルを守るために必要なものを取り戻した「真のドズ主」です。

        # 「怪盗ぼんじゅうるからの挑戦状」を遊んでいただきありがとうございました！
        """

    def _images_generator(self):
        img_list = ['kaitou_bon/fig/title.png',
                    'kaitou_bon/fig/prologue.png',
                    'kaitou_bon/fig/notice.png',
                    'kaitou_bon/fig/nazo1.png',
                    'kaitou_bon/fig/nazo2.png',
                    'kaitou_bon/fig/nazo3.png',
                    'kaitou_bon/fig/nazo4.png',
                    'kaitou_bon/fig/nazo5.png',
                    'kaitou_bon/fig/nazo6.png',
                    'kaitou_bon/fig/nazo7.png',
                    'kaitou_bon/fig/nazo8.png',
                    'kaitou_bon/fig/nazo9.png',
                    'kaitou_bon/fig/nazo10.png',
                    'kaitou_bon/fig/answer.png']
        for img_file in img_list:
            yield img_file

    def exec(self):
        st.title(self.title)

        # title
        self._screen_image(next(self.img_file_generator))

        # prologue
        self._screen_image(next(self.img_file_generator))

        # notice
        self._screen_image(next(self.img_file_generator))

        # nazo
        for i in range(10):
            self._screen_image(next(self.img_file_generator))
        
        # Answer
        self._screen_image(next(self.img_file_generator))

        st.write(self.last_question)

        st.write(self.last_answer)

        st.write(self.txt_epilogue)

    def _screen_image(self, img_file):
        img = Image.open(img_file)
        st.image(img, use_column_width=True)
