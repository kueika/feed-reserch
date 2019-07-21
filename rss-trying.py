import sys
import MeCab
m = MeCab.Tagger ("-Ochasen")
print(m.parse ('MONSTER HUNTER WORLDは最新作が最高に面白い神ゲーだった'))