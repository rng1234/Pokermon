#coding:utf-8

from os.path import exists #用于判断是否存在存档文件

item_code = ["potion", "pokerball"] #道具列
item_qty = [0, 0] #道具数量

#check_save data

start_or_continue = "1" #默认没有存档

if exists("save.txt") == True: #如果存在save.txt, 则提示是续档
	print "Welcome to Pockermon. \n1. Start Over \n2. Continue"
	start_or_continue = raw_input("> ")


if start_or_continue == "2": #读取存档第一行, 名字列
	savedata = open("save.txt", "r")
	name = savedata.readline()

	

def enter():
	print "\n"
	raw_input("Press any key to continue..")
	print "\n"

def choose(a, b, c, d):

	return ans

def choose_answer(a, b, c, d, a1, b1, c1, d1):
	print "\n"
	print "a: %s \nb: %s\n" % (a, b),
	print "c: %s \nd: %s\n" % (c, d)
	
	
	while True:
		ans = raw_input("What will you do? ")
		print "\n"
		
		if ans == "a":
			print a1
			print "\n"
			return ans
		
		elif ans == "b":
			print b1
			print "\n"
			return ans
			
		elif ans == "c":
			print c1
			print "\n"
			return ans
			
		elif ans == "d":
			print d1
			print "\n"
			return ans
			
		elif ans == "item":
			item_list()
			print "\n"
		
		else:
			print "Wrong input, try again.\n"

			
def item_list():
	print "You bag contains below items:\n"
	print item_code[0], item_qty[0]
	print item_code[1], item_qty[1]	
	
#Beginning
print "\t\tWelcome to the world of Pokermon. "
enter()


if start_or_continue == "1":
	print "What's your name? \n"
	name = raw_input("My name is: ")
	savedata = open("save.txt", "w")
	savedata.write(name)	

else:
	print "Your name is %s." % name

print "%s, This is a whole new world waiting for you, catch them all. " % name
enter()

#wake up in the room

print "You standing in front of a TV and Nintendo."
answer1 = choose_answer("Check the computer on the up-left conner.", "Go downstairs", "Check TV", "Go to sleep", "Hooray, you obtained a potion.",
	"", "Thre's a pokermon match on TV", "After 24 hours sleeping, you wake up again.")

if answer1 == "a":
	item_qty[0] =+ 1
	answer1 = choose_answer("Check the computer on the up-left conner.", "Go downstairs", "Check TV", "Go to sleep", "Hooray, you obtained a potion.",
	"", "Thre's a pokermon match on TV", "After 24 hours sleeping, you wake up again.")


