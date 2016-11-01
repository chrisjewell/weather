import csv


def left(string, chars):
    return string[:chars]

def right(string, chars):
    return string[-chars:]

def mid(string, startchar, chars):
    return string[startchar:startchar+chars]



file = open('C:\Users\cjewell\Desktop\DataProjects\weather\AGM00060515.txt', 'r')

x=0

rows = []
row = []
rowsDict = {}

# Declare lists to hold values for each fieldname

StationID = []
ReadType = []
Month = []
Day1 = []
Day2 = []
Day3 = []
Day4 = []
Day5 = []
Day6 = []
Day7 = []
Day8 = []
Day9 = []
Day10 = []
Day11 = []
Day12 = []
Day13 = []
Day14 = []
Day15 = []
Day16 = []
Day17 = []
Day18 = []
Day19 = []
Day20 = []
Day21 = []
Day22 = []
Day23 = []
Day24 = []
Day25 = []
Day26 = []
Day27 = []
Day28 = []
Day29 = []
Day30 = []
Day31 = []


# Create iterable list to write to csv

for line in file:
	#StationID] =
	StationID.append(left(line, 11))
	
	
	#ReadType] =
	ReadType.append(mid(line, 17, 4))

	
	#Month] =
	Month.append(mid(line, 11, 6))

	
	#Day1] = - startchar = 22 + 0, chars = 8
	Day1.append(mid(line, (21+0), 8))

	
	#Day2] = - startchar = 22 + 8, chars = 8
	Day2.append(mid(line, (21+8), 8))
	
	
	#Day3] = - startchar = 22 + 16, chars = 8
	Day3.append(mid(line, (21+16), 8))

	
	#Day4] = - startchar = 22 + 24, chars = 8
	Day4.append(mid(line, (21+24), 8))

	
	#Day5] = - startchar = 22 + 32, chars = 8
	Day5.append(mid(line, (21+32), 8))

	
	#Day6] = - startchar = 22 + 40, chars = 8
	Day6.append(mid(line, (21+40), 8))

	
	#Day7] = - startchar = 22 + 48, chars = 8
	Day7.append(mid(line, (21+48), 8))

	
	#Day8] = - startchar = 22 + 56, chars = 8
	Day8.append(mid(line, (21+56), 8))
	
	
	#Day9] = - startchar = 22 + 64, chars = 8
	Day9.append(mid(line, (21+64), 8))

	
	#Day10] = - startchar = 22 + 72, chars = 8
	Day10.append(mid(line, (21+72), 8))
	
	#Day11] = - startchar = 22 + 80, chars = 8
	Day11.append(mid(line, (21+80), 8))
	
	
	#Day12] = - startchar = 22 + 88, chars = 8
	Day12.append(mid(line, (21+88), 8))

	
	#Day13] = - startchar = 22 + 96, chars = 8
	Day13.append(mid(line, (21+96), 8))

	
	#Day14] = - startchar = 22 + 104, chars = 8
	Day14.append(mid(line, (21+104), 8))
	
	
	#Day15] = - startchar = 22 + 112, chars = 8
	Day15.append(mid(line, (21+112), 8))
	
	
	#Day16] = - startchar = 22 + 120, chars = 8
	Day16.append(mid(line, (21+120), 8))

	
	#Day17] = - startchar = 22 + 128, chars = 8
	Day17.append(mid(line, (21+128), 8))
	
	
	#Day18] = - startchar = 22 + 136, chars = 8
	Day18.append(mid(line, (21+136), 8))

	
	#Day19] = - startchar = 22 + 144, chars = 8
	Day19.append(mid(line, (21+144), 8))
	
	
	#Day20] = - startchar = 22 + 152, chars = 8
	Day20.append(mid(line, (21+152), 8))

		
	#Day21] = - startchar = 22 + 160, chars = 8
	Day21.append(mid(line, (21+160), 8))

		
	#Day22] = - startchar = 22 + 168, chars = 8
	Day22.append(mid(line, (21+168), 8))

		
	#Day23] = - startchar = 22 + 176, chars = 8
	Day23.append(mid(line, (21+176), 8))

		
	#Day24] = - startchar = 22 + 184, chars = 8
	Day24.append(mid(line, (21+184), 8))

		
	#Day25] = - startchar = 22 + 192, chars = 8
	Day25.append(mid(line, (21+192), 8))

		
	#Day26] = - startchar = 22 + 200, chars = 8
	Day26.append(mid(line, (21+200), 8))

		
	#Day27] = - startchar = 22 + 208, chars = 8
	Day27.append(mid(line, (21+208), 8))

		
	#Day28] = - startchar = 22 + 216, chars = 8
	Day28.append(mid(line, (21+216), 8))

		
	#Day29] = - startchar = 22 + 224, chars = 8
	Day29.append(mid(line, (21+224), 8))

		
	#Day30] = - startchar = 22 + 232, chars = 8
	Day30.append(mid(line, (21+232), 8))

		
	#Day31] = - startchar = 22 + 240, chars = 8
	Day31.append(mid(line, (21+248),8))

		
	x = x+1

	

# Write csv file

fieldnames = ['StationID', 'ReadType', 'Month', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Day8', 'Day9', 'Day10', 'Day11', 'Day12', 'Day13', 'Day14', 'Day15', 'Day16', 'Day17', 'Day18', 'Day19', 'Day20', 'Day21', 'Day22', 'Day23', 'Day24', 'Day25', 'Day26', 'Day27', 'Day28', 'Day29', 'Day30', 'Day31']

# NOW IT WORKS!

with open('stationdata.csv', 'wb') as output:
	w = csv.writer(output, csv.QUOTE_NONE)
	w.writerows(
				zip(StationID, ReadType, Month, Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23, Day24, Day25, Day26, Day27, Day28, Day29, Day30, Day31)
				)

print 'Done.'

print '%s rows written.' % x

# Next step is to write some code that will clean all of the spaces out of the lists before the get written into the .csv. This will save on space, and also allow me to actually use the data. Other things: replace '-9999' with something more readable; figure out what the 'H' and'S' are in the temperatures.
#After that, we need to make this iterate over all the files, and put them into one .csv file.


	