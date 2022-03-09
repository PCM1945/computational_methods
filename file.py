import csv

class File:
	def __init__(self, header, filename):
		self.header = header
		self.filename = filename

	def create_csv(self):
		with open(self.filename, 'w', newline= '') as f:
			w = csv.writer(f)
			w.writerow(self.header)

	def write_file(self, d):
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