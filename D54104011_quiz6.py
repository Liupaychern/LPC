# ＃將輸入猜對的字母放入list並隨之增加
# ＃輸入字母
# guess_list = []
# guess = str(input("Guess the lowrcase alphabet: "))
# guess_list.append(guess)

# ＃設一個隨機參數
# import random
# alphabet = random.randstr("a", "z")

import random
alphabets = ["a", "b", "c", "d","e","f", "g", "h", "i", "j"]
def guess():
	guess_list = []
	for i in alphabets:
		random.guess(alphabets)
		return alphabets

# 設定遊戲規則並依據字母順序印出答案
while guess != alphabets:
	if guess < alphabets:
		guess = str(input("The alphabet you are looking for is alphabetically lower."))
		guess_list.append(guess)
	if guess > alphabets:
		guess = str(input("The alphabet you are looking for is alphabetically higher."))
		guess_list.append(guess)
	if not  "a" < guess < "z":
		guess = str(input("Please enter a lowrcase alphabet"))
		guess_list.append(guess)
if guess == alphabets:
	print("Congratuations! You guessed the alphabet", guess_list, "in", len(guess_list), tries)

# 建立直方圖並將答案存入
	histogram = {"a - d": 0, "e - h": 0, "i - l": 0, "m - p": 0, "q - t": 0, "u - x": 0, "y - z": 0}
	for guess in guess_list:
		if "a" <= guess <= "d":
			histogram["a - d"] += 1
		elif "e" <= guess <= "h":
			histogram["e - h"] += 1
		elif "i" <= guess <= "l":
			histogram["i - l"] += 1
		elif "m" <= guess <= "p":
			histogram["m - p"] += 1
		elif "q" <= guess <= "t":
			histogram["q - t"] += 1
		elif "u" <= guess <= "x":
			histogram["u - x"] += 1
		elif "y" <= guess <= "z":
			histogram["y - z"] += 1
			
# 輸出答案並將猜測次數用＊表示
	print("Guess Histogram:")
	for key, value in histogram.items():
		print(key + ":" + "*" * value)