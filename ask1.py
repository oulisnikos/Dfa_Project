import sys, traceback
try:
	with open("dfa.txt","r") as f:
		#Read from file then number of states
		num_of_states = int(f.readline().rstrip('\n').split('//')[0])
		print("Number of States:",num_of_states)
		#Read from file the alphabeta 
		alphabeta = f.readline().split('//')[0].split()
		print("Alphabeta :",alphabeta)
		#Read from file the first state
		first_state = f.readline().split('//')[0]
		print("First State:",first_state)
		#Read from file the finals stastes
		final_state = f.readline().split('//')[0].split()
		print("Final States:",final_state)

		#Create a empty dicitonary for transitions
		states = dict()
		line = f.readline().split('//')[0]
		#Read line by line the transiton and stor in the dictionary until the end of file
		while line != None and line != '':
			current = line.split()
			if not(current[1] in alphabeta):
				print("The input character is not in alphabeta!!!")
				sys.exit()
			if not (current[0] in states):
				states[current[0]] = []
				
			states[current[0]].append([current[1], current[2]])
			line = f.readline().split('//')[0]
		#Ask from user to give us an input to check
		while True:
			inp_string = input("Give a string or exit: ")

			if inp_string == 'exit':
				break
			index = 0
			state = first_state

			iswrong = False
			#Check each character if it is in alphabet if not the program print "Wrong Input" else print "Ok"
			for char in inp_string:
				if (not char in alphabeta):
					iswrong = True
					break
		 
				found = False
				#Check one by one the character of input and go from one state to other until input finish
				for j in states[state]:
					if (j[0] == char):
						state = j[1]
						found = True
						break
				if not found:
					break
			if state in final_state and not iswrong:
				print ("\n---------OK---------\n")
			else:
				print ("\n-------- Your Input is wrong---------\n")
				
#Here we manage the error in good way
except TypeError as e:
	print("An error accured. Description: " ,str(e))
	
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print("print_tb:")
	traceback.print_tb(exc_traceback, limit=1, file = sys.stdout)
except IOError as e:
	print("An Error was detected while opening the file. Description: ", str(e))
	print("You must provide a file DFA Description.")
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print("print_tb:")
	traceback.print_tb(exc_traceback, limit = 1, file = sys.stdout)		
