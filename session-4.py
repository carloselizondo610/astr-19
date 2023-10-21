import sys

yes = True
print(type(yes))

no = False
print(type(no))
class Otter:

	def Print(self):
		print(f"length of arms = {self.l_arms}")
		print(f"length of legs = {self.l_legs}")
		print(f"number of eyes = {self.n_eyes}")
		print(f"does it have a tail? = {self.have_tail}")
		print(f"is it furry? = {self.is_furry}")
	def __init__(self,arms = 1.2,legs = 1.6,eyes = 2,tail = True,furry = True):	
		self.l_arms = arms
		self.l_legs = legs 
		self.n_eyes = eyes 
		self.have_tail = tail 
		self.is_furry = furry 

def main():
	Otter1 = Otter()
	Otter1.Print()
	

if __name__=="__main__":
	main()
