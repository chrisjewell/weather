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

ID = []
YEAR = []
MONTH = []
ELEMENT = []
VALUE1 = []
MFLAG1 = []
QFLAG1 = []
SFLAG1 = []
VALUE2 = []
MFLAG2 = []
QFLAG2 = []
SFLAG2 = []
VALUE3 = []
MFLAG3 = []
QFLAG3 = []
SFLAG3 = []
VALUE4 = []
MFLAG4 = []
QFLAG4 = []
SFLAG4 = []
VALUE5 = []
MFLAG5 = []
QFLAG5 = []
SFLAG5 = []
VALUE6 = []
MFLAG6 = []
QFLAG6 = []
SFLAG6 = []
VALUE7 = []
MFLAG7 = []
QFLAG7 = []
SFLAG7 = []
VALUE8 = []
MFLAG8 = []
QFLAG8 = []
SFLAG8 = []
VALUE9 = []
MFLAG9 = []
QFLAG9 = []
SFLAG9 = []
VALUE10 = []
MFLAG10 = []
QFLAG10 = []
SFLAG10 = []
VALUE11 = []
MFLAG11 = []
QFLAG11 = []
SFLAG11 = []
VALUE12 = []
MFLAG12 = []
QFLAG12 = []
SFLAG12 = []
VALUE13 = []
MFLAG13 = []
QFLAG13 = []
SFLAG13 = []
VALUE14 = []
MFLAG14 = []
QFLAG14 = []
SFLAG14 = []
VALUE15 = []
MFLAG15 = []
QFLAG15 = []
SFLAG15 = []
VALUE16 = []
MFLAG16 = []
QFLAG16 = []
SFLAG16 = []
VALUE17 = []
MFLAG17 = []
QFLAG17 = []
SFLAG17 = []
VALUE18 = []
MFLAG18 = []
QFLAG18 = []
SFLAG18 = []
VALUE19 = []
MFLAG19 = []
QFLAG19 = []
SFLAG19 = []
VALUE20 = []
MFLAG20 = []
QFLAG20 = []
SFLAG20 = []
VALUE21 = []
MFLAG21 = []
QFLAG21 = []
SFLAG21 = []
VALUE22 = []
MFLAG22 = []
QFLAG22 = []
SFLAG22 = []
VALUE23 = []
MFLAG23 = []
QFLAG23 = []
SFLAG23 = []
VALUE24 = []
MFLAG24 = []
QFLAG24 = []
SFLAG24 = []
VALUE25 = []
MFLAG25 = []
QFLAG25 = []
SFLAG25 = []
VALUE26 = []
MFLAG26 = []
QFLAG26 = []
SFLAG26 = []
VALUE27 = []
MFLAG27 = []
QFLAG27 = []
SFLAG27 = []
VALUE28 = []
MFLAG28 = []
QFLAG28 = []
SFLAG28 = []
VALUE29 = []
MFLAG29 = []
QFLAG29 = []
SFLAG29 = []
VALUE30 = []
MFLAG30 = []
QFLAG30 = []
SFLAG30 = []
VALUE31 = []
MFLAG31 = []
QFLAG31 = []
SFLAG31 = []


# Create iterable list to write to csv

for line in file:
	
	ID.append(line[0:10])
	YEAR.append(line[11:14])
	MONTH.append(line[15:16])
	ELEMENT.append(line[17:20])
	VALUE1.append(line[21:25])
	MFLAG1.append(line[26:26])
	QFLAG1.append(line[27:27])
	SFLAG1.append(line[28:28])
	VALUE2.append(line[29:33])
	MFLAG2.append(line[34:34])
	QFLAG2.append(line[35:35])
	SFLAG2.append(line[36:36])
	VALUE3.append(line[37:41])
	MFLAG3.append(line[42:42])
	QFLAG3.append(line[43:43])
	SFLAG3.append(line[44:44])
	VALUE4.append(line[45:49])
	MFLAG4.append(line[50:50])
	QFLAG4.append(line[51:51])
	SFLAG4.append(line[52:52])
	VALUE5.append(line[53:57])
	MFLAG5.append(line[58:58])
	QFLAG5.append(line[59:59])
	SFLAG5.append(line[60:60])
	VALUE6.append(line[61:65])
	MFLAG6.append(line[66:66])
	QFLAG6.append(line[67:67])
	SFLAG6.append(line[68:68])
	VALUE7.append(line[69:73])
	MFLAG7.append(line[74:74])
	QFLAG7.append(line[75:75])
	SFLAG7.append(line[76:76])
	VALUE8.append(line[77:81])
	MFLAG8.append(line[82:82])
	QFLAG8.append(line[83:83])
	SFLAG8.append(line[84:84])
	VALUE9.append(line[85:89])
	MFLAG9.append(line[90:90])
	QFLAG9.append(line[91:91])
	SFLAG9.append(line[92:92])
	VALUE10.append(line[93:97])
	MFLAG10.append(line[98:98])
	QFLAG10.append(line[99:99])
	SFLAG10.append(line[100:100])
	VALUE11.append(line[101:105])
	MFLAG11.append(line[106:106])
	QFLAG11.append(line[107:107])
	SFLAG11.append(line[108:108])
	VALUE12.append(line[109:113])
	MFLAG12.append(line[114:114])
	QFLAG12.append(line[115:115])
	SFLAG12.append(line[116:116])
	VALUE13.append(line[117:121])
	MFLAG13.append(line[122:122])
	QFLAG13.append(line[123:123])
	SFLAG13.append(line[124:124])
	VALUE14.append(line[125:129])
	MFLAG14.append(line[130:130])
	QFLAG14.append(line[131:131])
	SFLAG14.append(line[132:132])
	VALUE15.append(line[133:137])
	MFLAG15.append(line[138:138])
	QFLAG15.append(line[139:139])
	SFLAG15.append(line[140:140])
	VALUE16.append(line[141:145])
	MFLAG16.append(line[146:146])
	QFLAG16.append(line[147:147])
	SFLAG16.append(line[148:148])
	VALUE17.append(line[149:153])
	MFLAG17.append(line[154:154])
	QFLAG17.append(line[155:155])
	SFLAG17.append(line[156:156])
	VALUE18.append(line[157:161])
	MFLAG18.append(line[162:162])
	QFLAG18.append(line[163:163])
	SFLAG18.append(line[164:164])
	VALUE19.append(line[165:169])
	MFLAG19.append(line[170:170])
	QFLAG19.append(line[171:171])
	SFLAG19.append(line[172:172])
	VALUE20.append(line[173:177])
	MFLAG20.append(line[178:178])
	QFLAG20.append(line[179:179])
	SFLAG20.append(line[180:180])
	VALUE21.append(line[181:185])
	MFLAG21.append(line[186:186])
	QFLAG21.append(line[187:187])
	SFLAG21.append(line[188:188])
	VALUE22.append(line[189:193])
	MFLAG22.append(line[194:194])
	QFLAG22.append(line[195:195])
	SFLAG22.append(line[196:196])
	VALUE23.append(line[197:201])
	MFLAG23.append(line[202:202])
	QFLAG23.append(line[203:203])
	SFLAG23.append(line[204:204])
	VALUE24.append(line[205:209])
	MFLAG24.append(line[210:210])
	QFLAG24.append(line[211:211])
	SFLAG24.append(line[212:212])
	VALUE25.append(line[213:217])
	MFLAG25.append(line[218:218])
	QFLAG25.append(line[219:219])
	SFLAG25.append(line[220:220])
	VALUE26.append(line[221:225])
	MFLAG26.append(line[226:226])
	QFLAG26.append(line[227:227])
	SFLAG26.append(line[228:228])
	VALUE27.append(line[229:233])
	MFLAG27.append(line[234:234])
	QFLAG27.append(line[235:235])
	SFLAG27.append(line[236:236])
	VALUE28.append(line[237:241])
	MFLAG28.append(line[242:242])
	QFLAG28.append(line[243:243])
	SFLAG28.append(line[244:244])
	VALUE29.append(line[245:249])
	MFLAG29.append(line[250:250])
	QFLAG29.append(line[251:251])
	SFLAG29.append(line[252:252])
	VALUE30.append(line[253:257])
	MFLAG30.append(line[258:258])
	QFLAG30.append(line[259:259])
	SFLAG30.append(line[260:260])
	VALUE31.append(line[261:265])
	MFLAG31.append(line[266:266])
	QFLAG31.append(line[267:267])
	SFLAG31.append(line[268:268])

		
	x = x+1

	

# Write csv file

fieldnames = ['StationID', 'ReadType', 'Month', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Day8', 'Day9', 'Day10', 'Day11', 'Day12', 'Day13', 'Day14', 'Day15', 'Day16', 'Day17', 'Day18', 'Day19', 'Day20', 'Day21', 'Day22', 'Day23', 'Day24', 'Day25', 'Day26', 'Day27', 'Day28', 'Day29', 'Day30', 'Day31']

# NOW IT WORKS!

with open('stationdata.csv', 'wb') as output:
	w = csv.writer(output, csv.QUOTE_NONE)
	w.writerows(zip(StationID, ReadType, Month, Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23, Day24, Day25, Day26, Day27, Day28, Day29, Day30, Day31))

print 'Done.'

print '%s rows written.' % x

# Next step is to write some code that will clean all of the spaces out of the lists before the get written into the .csv. This will save on space, and also allow me to actually use the data. Other things: replace '-9999' with something more readable; figure out what the 'H' and'S' are in the temperatures.
#After that, we need to make this iterate over all the files, and put them into one .csv file.


	
