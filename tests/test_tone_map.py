from engine.tone.tone_map import build_tone_map

words = [
    "ọmọ",
    "ilé",
    "ọba",
    "ọkọ",
    "ẹ̀kọ́",
    "ọmọde"
]

tone_map = build_tone_map(words)

print(tone_map["omo"])
print(tone_map["ile"])
print(tone_map["oko"])