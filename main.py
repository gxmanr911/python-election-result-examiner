def start():
	from csv import reader
	global stat_names
	global info
	#
	with open("election_results_county.csv", "r") as file:
		info=[]
		for i in reader(file):
			info.append(i)
	#This allows the results to be iterable, prevents the need for the csv moduel for the future, and prevents the file from needing to be open to save on memory
	stat_names=['total votes','votes democratic','votes republican','combined third party votes','persent democratic','persent republican','highest voting couty','closest republican vs democratic county','most rebulican county','most democratic county']
	del reader # removes csv model to save memory
class vote_info():
	'''a class with methods to use info from a state abriviation'''
	def votes_total(abriviation):
		result=0
		for row in info:
			if row[2]==abriviation:
				result+=int(row[3])
		return result
	def votes_dem(abriviation):
		result=0
		for row in info:
			if row[2]==abriviation:
				result+=int(float(row[4]))
		return result
	def votes_rep(abriviation):
		result=0
		for row in info:
			if row[2]==abriviation:
				result+=int(float(row[5]))
		return result
	def combined_lossers(abriviation):
		result=0
		for row in info:
			if row[2]==abriviation:
				result+=int(row[6])
		return result
	def per_dem(abriviation):
		result=0
		for row in info:
			if row[2]==abriviation:
				result+=float(row[7])
		return int(result)
	def per_rep(abriviation):
		result=0
		for row in info:
			if row[2]==abriviation:
				result+=float(row[8])
		return int(result)
	def highest_couty(abriviation):
		result=0
		highest_county=0
		for row in info:
			if row[2]==abriviation:
				if int(row[3])>=highest_county:
					highest_county=int(row[3])
		for row in info:
			if row[2]==abriviation:
				if int(row[3])==highest_county:
					highest_county=row[1]
		return highest_county
	def closest_rep_dem_votes(abriviation):
		closest=1000000
		#4 and 5
		for row in info:
			if row[2]==abriviation:
				if abs(int(float(row[4]))-int(float(row[5])))<=closest:
					closest=abs(int(float(row[4]))-int(float(row[5])))
		num=closest
		for row in info:
			if row[2]==abriviation:
				if abs(int(float(row[4]))-int(float(row[5])))==closest:
					closest=row[1]
		return f'{closest} ({num})'
	def more_dem(abriviation):
		result=0
		highest_county=0
		for row in info:
			if row[2]==abriviation:
				if int(float(row[4]))>highest_county:
					highest_county=int(float(row[4]))
		num=highest_county
		for row in info:
			if row[2]==abriviation:
				if int(float(row[4]))==highest_county:
					highest_county=row[1]
		return f'{highest_county} ({num})'
	def more_rep(abriviation):
		result=0
		highest_county=0
		for row in info:
			if row[2]==abriviation:
				if int(float(row[5]))>=highest_county:
					highest_county=int(float(row[5]))
		num=highest_county
		for row in info:
			if row[2]==abriviation:
				if int(float(row[5]))==highest_county:
					highest_county=row[1]
		return f'{highest_county} ({num})'
if __name__=="__main__":
	from time import sleep
	def user_select(): #gets the user input to be used in vote_info methods
		valid_states=['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
		while True:
			userin=input("pick a state abriviation: ").upper()
			try:
				valid_states.index(userin)
				return userin
			except:
				print('NOT A STATE ABRIVIATION TRY AGAIN')
				sleep(0.5)
	def view():# shows information gathered from vote_info methods
		stats=[vote_info.votes_total,vote_info.votes_dem,vote_info.votes_rep,vote_info.combined_lossers,vote_info.per_dem,vote_info.per_rep,vote_info.highest_couty,vote_info.closest_rep_dem_votes,vote_info.more_rep,vote_info.more_dem]
		userin=user_select()
		for i in enumerate(stats):
			print(f'{stat_names[i[0]]}: {i[1](userin)}')
			sleep(0.2)
	start()
	while True:
		view()
		sleep(1)                                                                         