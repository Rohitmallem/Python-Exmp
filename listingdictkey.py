import pickle 


try: 
	cheek_file = open('Input.txt', 'r') 
	dictionary_list = pickle.load(cheek_file) 
	
	for d in dictionary_list: 
		print(d) 
	cheek_file.close() 

except: 
	print("Something unexpected occurred!")
