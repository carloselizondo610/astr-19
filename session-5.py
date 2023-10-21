import numpy as np


def Sinfunc():

	i=0
	while (i<=1000):
		print(str(i)+"    ")
		print(str(np.sin(i)))
		print("\n")
		i=i+1


def main():
	Sinfunc()


if __name__=="__main__":
	main()