import requests
from bs4 import BeautifulSoup


#-------------------------INPUT DATA-------------------------------
# Roll number example 21bma044
year = 20
branchCode = "ma"
rollStart = 1
rollEnd = 50
jsonFormat = False




#----------------------------Don't touch-----------------------------

rollno = f"{year}b"+ branchCode

url = f"http://14.139.56.19/scheme{year}/studentresult/result.asp"

def find_cgpa(roll):

	student = []

	data = {
			"RollNumber" : roll
	}

	p = requests.post(url,data)
	soup = BeautifulSoup(p.content,'html.parser')

	cgpa = soup.find_all(class_="formSetting")

	for i in cgpa:
		student.append(i.string)

	x,cgpa = student[-3].split('=')

	if jsonFormat:
		# print in json format
		print('{ "roll":'+f'"{student[1].strip()}"' + ',')
		print('"name":'+f'"{student[3].strip()}"' + ',')
		print('"cgpa":'+f'"{cgpa}"'+'},\n')
	else:
		# print in string format
		print(f"{cgpa} {student[1]} {student[3]} \n")


if jsonFormat:
	print("[")

# Main Loop
for i in range(rollStart,rollEnd+1):
	try:
		if i <= 9:
			find_cgpa(rollno + "00" + str(i))
		elif i <= 99 :
			find_cgpa(rollno + "0" + str(i))
		else:
			find_cgpa(rollno + str(i))
	except:
		continue		

if jsonFormat:
	print("]")

