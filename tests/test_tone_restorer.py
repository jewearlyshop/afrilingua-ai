from tone_restorer import ToneRestorer

words = [
    "ọmọ",
    "ilé",
    "ọba",
    "ọkọ",
    "ẹ̀kọ́",
    "ọmọde",
]

restorer = ToneRestorer(words)

print(restorer.restore("omo"))
print(restorer.restore("ile"))
print(restorer.restore("oko"))