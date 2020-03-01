import json


json_filename = './morse_code_s.json'
with open(json_filename) as f:
	morse_table = json.load(f)
	l2m = morse_table
# print(morse_table)

m2l = {v:k for k,v in morse_table.items()}
# print(m2l)

# 编码函数
def encode(message):
	# 循环每个字母找到对应的点
	message = message.lower()
	mes = ''
	for l in message:
		# 不等于空格的时候进行翻译
		if l!=' ':
			mes = mes + l2m[l] + ' '
		else:
			mes = mes + l + l
	return mes


# 解码函数
def decode(message):
	# 循环每条编码得到字母
	# m = '['+message+']'
	# print(m)
	m1 = message.replace('   ','_')
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
	inhalt = input("please write your words:\n")
	if (inhalt[0]=='.' or inhalt[0]=='-'):
		print(decode(inhalt))
	else:
		print(encode(inhalt))


