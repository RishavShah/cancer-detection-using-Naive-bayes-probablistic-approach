import csv, math, random


class naive:
	file_name = 'breast3.csv'
	#file_name = "SPECTF_New.csv"
	#file_name = "SPECTF.csv"
	MAX_ITERATIONS = 100
	N = -1
	TUPLES=-1
	offset = 0.01 # 10 percent
	FOLDS = 2
	FOLD_LENGTH = -1
	mean=0
	avg=0
	
	def __init__(self):
		self.data = []
		

	def loadDataSet(self):
		i = -1
		with open(self.file_name, 'rt') as f:
			reader = csv.reader(f)
			for row in reader:
				if i == -1:
					i += 1
					continue
				self.data.append(row)
		#self.offset=float(input("offset:"))
		self.formatDataSet()
		#self.TUPLES=len(self.data)
		#self.N=len(self.data[1])-1
		#self.FOLD_LENGTH=math.ceil(self.offset * self.TUPLES)
		#self.FOLDS=math.ceil(self.TUPLES/self.FOLD_LENGTH)
		#self.avg=0
		# Shuffle the data
		random.shuffle(self.data)

	def formatDataSet(self):
		# convert strings to float
		for i in range(len(self.data)):
			# Yes : 1 No : 0
			if self.data[i][-1] == 'benign':
				self.data[i][-1] = 1
			else:
				self.data[i][-1] = 0

			self.data[i][:-1] = [float(x) for x in self.data[i][:-1]]
			
		
			
	def train(self):
		'''
		self.training=[]
		self.testing=[]
		count_yes=0
		count_no=0
		for i in range(len(self.data)):
			if(i%27==0):
				self.testing.append(self.data[i])
			else:
				self.training.append(self.data[i])
		'''
		self.TUPLES=len(self.data)
		self.N=len(self.data[1])-1
		self.FOLD_LENGTH=math.ceil(self.offset * self.TUPLES)
		self.FOLDS=math.ceil(self.TUPLES/self.FOLD_LENGTH)
		self.avg=0
		# Shuffle the data
		random.shuffle(self.data)
		#random.shuffle(self.data)
		for fold in range(0, self.FOLDS):
			# print('############################ FOLD : %s  #################################\n' % (fold+1))
			#a=0
			# clear the previous testing data
			#for i in range(0,50):
				self.training=[]
				self.testing=[]
			
				count_yes=0
				count_no=0
			
				for i in range(len(self.data)):
					self.training.append(self.data[i])
				
				# produce the corresponding testing data
				for j in range(0, self.FOLD_LENGTH):
					if self.FOLD_LENGTH * fold + j < self.TUPLES:
						self.testing.append(self.data[self.FOLD_LENGTH * fold + j])
						del self.training[self.FOLD_LENGTH * fold]

		
				for i in range(len(self.training)):
					if(self.training[i][-1]==1):
						count_yes+=1
					else:
						count_no+=1
		
				total=len(self.training)
				p_yes=count_yes/total
				p_no=count_no/total
		
				ans=0
		
		
				for i in range(len(self.testing)):
					mul_yes=p_yes
					mul_no=p_no
					for j in range (0,self.N):
						count_yes=0
						count_no=0
						count=0
				
				
						attr=self.testing[i][j]
						for k in range(len(self.training)):
							if(self.training[k][j]==attr):
								count+=1
								if(self.training[k][-1]==1):
									count_yes+=1
								else:
									count_no+=1
						if(count!=0):
							mul_yes*=(count_yes/count)
							mul_no*=(count_no/count)
							
					if(mul_yes >= mul_no):
						res=1
					else:
						res=0
			
					if(res==self.testing[i][-1]):
						ans+=1
		
				percentage=(ans*100)/len(self.testing)
				self.mean+=percentage
				print(ans , '\t' ,len(self.testing) , '\t' , percentage)
		self.avg=self.avg+(self.mean/self.FOLDS)
		#print("mean =\t",a/50)
		print("mean =\t",self.mean/self.FOLDS)
					
if __name__=="__main__":
	nb=naive()
	nb.loadDataSet()
	#avg=0
	nb.offset=float(input("offset:"))
	for i in range(0,50):
		nb.train()
	print("mean =\t",nb.avg/50)
