from engine.tone.tone_restorer import ToneRestorer


restorer = ToneRestorer()

print(restorer.restore_word("omo"))
print(restorer.restore_word("ile"))
print(restorer.restore_word("iwe"))

print(restorer.restore_sentence("omo fe lo ile"))