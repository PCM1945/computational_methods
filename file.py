import csv

class File:
	"""DESCRIPTION
			class contaning methos to format and write data into a csv file
		params: 
			header(str): file header
			filename(str): name of the file
	"""
	def __init__(self, header, filename):
		self.header = header
		self.filename = filename

	def create_csv(self):
		"""DESCRIPTION
				method to create a CSV file by placing its header contents
			params: 
				self
			returns: 
				None
		"""
		with open(self.filename, 'w', newline= '') as f:
			w = csv.writer(f)
			w.writerow(self.header)

	def write_file(self, d):
		"""DESCRIPTION
				Method to write data formated on the csv file
			Params:
				d(list): list contaning all data to be written
			returns:
				None 
		"""
		data = ','.join(str(v) for v in d) + '\n' #add comma separating data elements ans a \n char ath the end
		with open(self.filename, 'r') as f:
			aux = []        
			for row in f:
				aux.append(row)
		aux.append(data)
		#print(aux)
		
		with open(self.filename, 'w', newline= '') as f:
			for row in aux:
				f.write(row)