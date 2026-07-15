from engine.text.vocabulary import build_vocabulary

text = """
Ọmọ náà fẹ́ lọ sí ilé.
Ọmọ náà fẹ́ jẹun.
Ọmọ náà fẹ́ kọ́ ẹ̀kọ́.
"""

vocab = build_vocabulary(text)

print(vocab)