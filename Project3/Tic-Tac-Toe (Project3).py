while True:
	def plot():
		print(f'''
                        --------GAME----------            --------POSITIONS----------
                    
                    {indx[1]}|{indx[2]}|{indx[3]}           1    |    2    |    3    
                    _________|_________|_________         _______|_________|________
                    {indx[4]}|{indx[5]}|{indx[6]}           4    |    5    |    6    
                    _________|_________|_________         _______|_________|________
                             |         |                         |         |
                    {indx[7]}|{indx[8]}|{indx[9]}           7    |    8    |    9    

		''')
	
	indx=[False,' '*9,' '*9,' '*9,' '*9,' '*9,' '*9,' '*9,' '*9,' '*9]
	print('---------TIC-TAC-TOE-------------')
	print('--------Enter Your Names---------')
	player=[input('\nPlayer 1: ').capitalize(),input('\nPlayer 2: ').capitalize()]
	used=[]
	choice=[]
	print(f'\n{player[0]} Will go First')

	while choice==[]:) ----------------------------------')

	while len(used)!=9:
		plot()
		try:
			temp=int(input(f'{player[len(used)%2]} Enter the Postion number for ({choice[len(used)%2]}):'))
			if 0<temp<10:
				pass
			else:
				temp=int('traceback')
		except:
			print('\n----------------- Enter the Valid Postion number (1-9) ---------------------\a')
			continue

		if temp not in used: 
			indx[temp]=' '*4+choice[len(used)%2]+' '*4
			used.append(temp)
		else:
			print(f'\n------------------------ Place {temp} is already Occupied by "{indx[temp].strip()}" ---------------------------\a')
			continue
		
		for i in range(0,7,3):
			if indx[i+1]==indx[i+2]==indx[i+3] and indx[i+1]!=' '*9:
				won=player[choice.index(indx[i+1].strip())]
				indx[0]=True

		
		for i in range(0,3):
			if indx[i+1]==indx[i+4]==indx[i+7] and indx[i+1]!=' '*9:
				won=player[choice.index(indx[i+1].strip())]
				indx[0]=True

		if indx[1]==indx[5]==indx[9] and indx[1]!=' '*9:
			won=player[choice.index(indx[i+1].strip())]
			indx[0]=True
			
		if indx[3]==indx[5]==indx[7] and indx[3]!=' '*9:
			won=player[choice.index(indx[i+1].strip())]
			indx[0]=True
		
		if indx[0]==True:
			plot()
			print(f'----------------- Congratulations {won} Won the Match -------------------\a\n')
			break
	else:
		plot()
		print(f'\n------------------- The Match is Draw between {player[0]} & {player[1]} -----------------------\a\n')
	
	try:
		if str(input('Want To Play Again?? Press "y" or "n" to Quit: '))=='n':
			exit('\n-------------------------Thank You---------------------')
	except:
		exit('\n---------------------------Thank You-------------------------------')
