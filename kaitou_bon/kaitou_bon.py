import streamlit as st
from PIL import Image



class KaitouBon(object):

    def __init__(self):
        self.img_file_generator = self._images_generator()
        self.answerbox_generator = self._answerbox_generator()
        self._def_text()
        self._def_answer_nazo()
        self.num_nazo = 10
        pass

    def _def_answer_nazo(self):
        self.answer_nazo = {}
        self.answer_nazo[1] = ['なかよし', 'ナカヨシ']
        self.answer_nazo[2] = ['みるくぴえん', 'ミルクピエン', 'みるくピエン']
        self.answer_nazo[3] = ['冒険者', 'ぼうけんしゃ', 'ボウケンシャ']
        self.answer_nazo[4] = ['ごーるでん', 'ゴールデン']
        self.answer_nazo[5] = ['じゅうがつかえる', '銃が使える', 'ジュウガツカエル']
        self.answer_nazo[6] = ['さいのう', 'サイノウ']
        self.answer_nazo[7] = ['かず', 'カズ']
        self.answer_nazo[8] = ['てんどん', 'テンドン']
        self.answer_nazo[9] = ['もみじ', 'モミジ']
        self.answer_nazo[10] = ['洗濯機', 'せんたくき', 'センタクキ']
        self.answer_last_nazo = ['ドズ主の心', 'どずぬしのこころ', 'ドズヌシノココロ']

    def _def_text(self):
        self.title = '怪盗ぼんじゅうるからの挑戦状'
        self.txt_prologue = \
            """
            怪盗ぼんしゅうるからドズルへ予告状と10個の謎が届きました。\n
            困ったドズルはあなたたちドズ主に助けを求めています。\n
            怪盗ぼんじゅうるからドズルのチャンネルを守るため、謎を解き明かし、最後の答えを導いてください。
            """
        self.last_question = '# 怪盗ぼんじゅうるが盗んだものは何？'
        self.last_answer = '最後の謎の答え'
        self.fail_message = '答えが違うようだ'
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

    def _answerbox_generator(self):
        for i in range(1, self.num_nazo+1):
            yield f'謎{i}の答え'

    def _images_generator(self):
        img_list = ['kaitou_bon/fig/title.png',
                    'kaitou_bon/fig/prologue.png',
                    'kaitou_bon/fig/notice.png']
        img_list.extend([f'kaitou_bon/fig/nazo{i}.png' for i in range(1, self.num_nazo + 1)])
        img_list.append('kaitou_bon/fig/answer.png')
        for img_file in img_list:
            yield img_file

    def _screen_image(self, img_file):
        img = Image.open(img_file)
        st.image(img, use_column_width=True)


    def start(self):
        st.title(self.title)

        # title
        self._screen_image(next(self.img_file_generator))

        # prologue
        self._screen_image(next(self.img_file_generator))

        st.write(self.txt_prologue)

        # notice
        self._screen_image(next(self.img_file_generator))

        self.solve_nazo(nazo=1)


    def solve_nazo(self, nazo):
        self._screen_image(next(self.img_file_generator))
        sentence = st.text_input(next(self.answerbox_generator))
        if sentence in self.answer_nazo[nazo]:
            if nazo+1 > self.num_nazo:
                self._last_nazo()
            else:
                self.solve_nazo(nazo+1)
        elif not sentence == '':
            st.write(self.fail_message)

    def _last_nazo(self):
        self._screen_image(next(self.img_file_generator))

        st.write(self.last_question)

        sentence = st.text_input(self.last_answer) 
        if sentence in self.answer_last_nazo:
            self._epilogue()
        elif not sentence == '':
            st.write(self.fail_message)

    def _epilogue(self):
        st.write(self.txt_epilogue)


