import pyautogui,random,time,threading,argparse
from random import choice

comments = ["hi","down","up","..",">>","hello","fahmy","mohamed","omar",random.randint(0,60),78,569]
""" list of comments>> according to your requirement you can change it"""

starting=["this is new comment","update the comments by","adding new comment by content",1,4,65,54,23,212,265,746]
# commentbox='image path'
def randocomment():
	global comments
	randomcommment=comments[random.randint(0,len(comments)-1)]
	return randomcommment
def random_start():
	global starting
	randomstart=starting[random.randint(0,len(starting)-1)]
	return randomstart
def autocommenter(count):
	time.sleep(3)
	count=count
	start=1
	while count !=0:

		# pyautogui.press
		try:
			pyautogui.typewrite(f"{random_start()} {randocomment()}  \n : Comment Number  [{start}] ")
			start+=1
			time.sleep(1)
			pyautogui.press("\n")
			time.sleep(2)
			count-=1
		except Exception as exc:
			print("Error Ocurred : ",exc)


def main(cli):
	autocommenter(cli.count)
if __name__ == '__main__':
	parser=argparse.ArgumentParser(description="This is Tool For AutoCommnet By Python")
	parser.add_argument("-c","--count",help="Number of Random Comments .ex : python autocomment.py -c 10 ",metavar="",action="store",default=50)
	args=parser.parse_args()
	print("Coded By [ Mohammed Fahmy ]")
	main(args)



