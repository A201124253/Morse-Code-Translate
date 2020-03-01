import json


json_filename = './morse_code_s.json'
with open(json_filename) as f:
	morse_table = json.load(f)
	l2m = morse_table
# print(morse_table)

m2l = {v:k for k,v in morse_table.items()}
# print(m2l)

class Morse_code_translate():
	def __init__(self, inhalt):
		self.inhalt = inhalt

	# 编码函数
	def encode(self):
		# 循环每个字母找到对应的点
		message = self.inhalt.strip().lower()
		mes = ''
		for l in message:
			# 不等于空格的时候进行翻译
			if l!=' ':
				mes = mes + l2m[l] + ' '
			else:
				mes = mes + l + l
		return mes


	# 解码函数
	def decode(self):
		# 循环每条编码得到字母
		# m = '['+message+']'
		# print(m)
		m0 = self.inhalt.strip()
		print(m0)
		m1 = m0.replace('   ','_')
		# print('m1={}'.format(m1))
		m2 = m1.replace(' ', "','")
		# print('m2={}'.format(m2))
		m3 = m2.replace('_', "'],['")
		# print('m3={}'.format(m3))
		m4 = "[['" + m3 +"']]"
		# print('m4={}'.format(m4))
		mess = eval(m4)
		# print(m4)

		# words
		w = ''
		for word in mess:
			for l in word:
				w = w + m2l[l]

			w = w + ' '
		w = w + '\n'		
		return w 
	
if __name__ == "__main__":
# def main():
	while True:
		fun = input("please choose the function\n 1->translate 2->exit\n")
		if fun=='2':
			break
		elif fun=='1':
			inhalt = input("please write your words:\n")
			mst = Morse_code_translate(inhalt)
			if (inhalt[0]=='.' or inhalt[0]=='-'):
				print('The words is: ')
				print(mst.decode())
			else:
				print('The Morse code is: ')
				print(mst.encode())


