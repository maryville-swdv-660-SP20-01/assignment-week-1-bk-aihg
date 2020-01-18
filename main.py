import stringcase, sorting


def start():

	
	user_input = ""
	while user_input != "3":

		print("Select and operation as below:- ")
		print("1. Enter 1 to input any string and convert to a stingcase of available choices.")
		print("2. Enter 2 to input an array of numbers and sort using sorting mechanism of available choicese.")
		print("3. To exit")

		user_input = input("Please enter your choice: ")

		if user_input == "1":
			user_data = input("Please enter a string: ")
			print("Select and operation as below:- ")
			print("1. To convert string to camelcase")
			user_option = input("Please enter your choice: ")
			if user_option == "1":
				print("Camelcase converted string - {}".format(stringcase.camelcase(user_data)))
		elif user_input == "2":
			
			user_data = list(map(int,input("Please enter an array of numbers(integer with spaces): ").split()))
			
			print("Select and operation as below:- ")
			print("1. To sort using bubble sort")
			user_option = input("Please enter your choice: ")
			if user_option == "1":
				print("Camelcase converted string - {}".format(sorting.bubble(user_data)))

if __name__ == "__main__":
	start()