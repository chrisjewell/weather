import csv
import ghcnd as g
import matplotlib.pyplot as plt
import pandas as pd


file = open('C:\Users\cjewell\Desktop\DataProjects\weather\AGM00060515.txt', 'r')


# Declare lists to hold values for each fieldname

ID = []
YEAR = []
MONTH = []
DAY = []
day = 0
ELEMENT = []
VALUE = []
MFLAG = []
QFLAG = []
SFLAG = []


# Create iterable list to write to dataframe

for line in file:

	#day = day + 1
	ID.append(line[0:11])
	YEAR.append(line[11:15])
	MONTH.append(line[15:17])
	ELEMENT.append(line[17:21])
	VALUE.append(line[21:26])
	MFLAG.append(line[26:27])
	QFLAG.append(line[27:28])
	SFLAG.append(line[28:29])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[29:34])
	MFLAG.append(line[34:35])
	QFLAG.append(line[35:36])
	SFLAG.append(line[36:37])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[37:42])
	MFLAG.append(line[42:43])
	QFLAG.append(line[43:44])
	SFLAG.append(line[44:45])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[45:50])
	MFLAG.append(line[50:51])
	QFLAG.append(line[51:52])
	SFLAG.append(line[52:53])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[53:58])
	MFLAG.append(line[58:59])
	QFLAG.append(line[59:60])
	SFLAG.append(line[60:61])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[61:66])
	MFLAG.append(line[66:67])
	QFLAG.append(line[67:68])
	SFLAG.append(line[68:69])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[69:74])
	MFLAG.append(line[74:75])
	QFLAG.append(line[75:76])
	SFLAG.append(line[76:77])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[77:82])
	MFLAG.append(line[82:83])
	QFLAG.append(line[83:84])
	SFLAG.append(line[84:85])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[85:90])
	MFLAG.append(line[90:91])
	QFLAG.append(line[91:92])
	SFLAG.append(line[92:93])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[93:98])
	MFLAG.append(line[98:99])
	QFLAG.append(line[99:100])
	SFLAG.append(line[100:101])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[101:106])
	MFLAG.append(line[106:107])
	QFLAG.append(line[107:108])
	SFLAG.append(line[108:109])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[109:114])
	MFLAG.append(line[114:115])
	QFLAG.append(line[115:116])
	SFLAG.append(line[116:117])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[117:122])
	MFLAG.append(line[122:123])
	QFLAG.append(line[123:124])
	SFLAG.append(line[124:125])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[125:130])
	MFLAG.append(line[130:131])
	QFLAG.append(line[131:132])
	SFLAG.append(line[132:133])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[133:138])
	MFLAG.append(line[138:139])
	QFLAG.append(line[139:140])
	SFLAG.append(line[140:141])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[141:146])
	MFLAG.append(line[146:147])
	QFLAG.append(line[147:148])
	SFLAG.append(line[148:149])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[149:154])
	MFLAG.append(line[154:155])
	QFLAG.append(line[155:156])
	SFLAG.append(line[156:157])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[157:162])
	MFLAG.append(line[162:163])
	QFLAG.append(line[163:164])
	SFLAG.append(line[164:165])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[165:170])
	MFLAG.append(line[170:171])
	QFLAG.append(line[171:172])
	SFLAG.append(line[172:173])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[173:178])
	MFLAG.append(line[178:179])
	QFLAG.append(line[179:180])
	SFLAG.append(line[180:181])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[181:186])
	MFLAG.append(line[186:187])
	QFLAG.append(line[187:188])
	SFLAG.append(line[188:189])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[189:194])
	MFLAG.append(line[194:195])
	QFLAG.append(line[195:196])
	SFLAG.append(line[196:197])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[197:202])
	MFLAG.append(line[202:203])
	QFLAG.append(line[203:204])
	SFLAG.append(line[204:205])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[205:210])
	MFLAG.append(line[210:211])
	QFLAG.append(line[211:212])
	SFLAG.append(line[212:213])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[213:218])
	MFLAG.append(line[218:219])
	QFLAG.append(line[219:220])
	SFLAG.append(line[220:221])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[221:226])
	MFLAG.append(line[226:227])
	QFLAG.append(line[227:228])
	SFLAG.append(line[228:229])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[229:234])
	MFLAG.append(line[234:235])
	QFLAG.append(line[235:236])
	SFLAG.append(line[236:237])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[237:242])
	MFLAG.append(line[242:243])
	QFLAG.append(line[243:244])
	SFLAG.append(line[244:245])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[245:250])
	MFLAG.append(line[250:251])
	QFLAG.append(line[251:252])
	SFLAG.append(line[252:253])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[253:258])
	MFLAG.append(line[258:259])
	QFLAG.append(line[259:260])
	SFLAG.append(line[260:261])
	#DAY.append(day)
	
	#day = day + 1
	VALUE.append(line[261:266])
	MFLAG.append(line[266:267])
	QFLAG.append(line[267:268])
	SFLAG.append(line[268:269])
	#DAY.append(day)


	
for elem in ELEMENT:

	DAY.append(day)


# Write csv file
# NOW IT WORKS!


#I think one of the real next steps is to work on getting this into a pandas dataframe instead of a csv file. This is the ultimate goal, so we can just cut out the middle step.


"""
with open('stationdata.csv', 'wb') as output:
	w = csv.writer(output, csv.QUOTE_NONE)
	w.writerows(zip(ID, YEAR, MONTH, ELEMENT, VALUE1, MFLAG1, QFLAG1, SFLAG1, VALUE2, MFLAG2, QFLAG2, SFLAG2, VALUE3, MFLAG3, QFLAG3, SFLAG3, VALUE4, MFLAG4, QFLAG4, SFLAG4, VALUE5, MFLAG5, QFLAG5, SFLAG5, VALUE6, MFLAG6, QFLAG6, SFLAG6, VALUE7, MFLAG7, QFLAG7, SFLAG7, VALUE8, MFLAG8, QFLAG8, SFLAG8, VALUE9, MFLAG9, QFLAG9, SFLAG9, VALUE10, MFLAG10, QFLAG10, SFLAG10, VALUE11, MFLAG11, QFLAG11, SFLAG11, VALUE12, MFLAG12, QFLAG12, SFLAG12, VALUE13, MFLAG13, QFLAG13, SFLAG13, VALUE14, MFLAG14, QFLAG14, SFLAG14, VALUE15, MFLAG15, QFLAG15, SFLAG15, VALUE16, MFLAG16, QFLAG16, SFLAG16, VALUE17, MFLAG17, QFLAG17, SFLAG17, VALUE18, MFLAG18, QFLAG18, SFLAG18, VALUE19, MFLAG19, QFLAG19, SFLAG19, VALUE20, MFLAG20, QFLAG20, SFLAG20, VALUE21, MFLAG21, QFLAG21, SFLAG21, VALUE22, MFLAG22, QFLAG22, SFLAG22, VALUE23, MFLAG23, QFLAG23, SFLAG23, VALUE24, MFLAG24, QFLAG24, SFLAG24, VALUE25, MFLAG25, QFLAG25, SFLAG25, VALUE26, MFLAG26, QFLAG26, SFLAG26, VALUE27, MFLAG27, QFLAG27, SFLAG27, VALUE28, MFLAG28, QFLAG28, SFLAG28, VALUE29, MFLAG29, QFLAG29, SFLAG29, VALUE30, MFLAG30, QFLAG30, SFLAG30, VALUE31, MFLAG31, QFLAG31, SFLAG31))

print 'Done. %s rows written.' % x

# Next step is to write some code that will clean all of the spaces out of the lists before the get written into the .csv. This will save on space, and also allow me to actually use the data. Other things: replace '-9999' with something more readable; figure out what the 'H' and'S' are in the temperatures.
#After that, we need to make this iterate over all the files, and put them into one .csv file.
"""

# This section brings imports the data into a pandas dataframe so that we can run analysis on it.
"""
stationdata = list(zip(ID, YEAR, MONTH, ELEMENT, VALUE1, MFLAG1, QFLAG1, SFLAG1, VALUE2, MFLAG2, QFLAG2, SFLAG2, VALUE3, MFLAG3, QFLAG3, SFLAG3, VALUE4, MFLAG4, QFLAG4, SFLAG4, VALUE5, MFLAG5, QFLAG5, SFLAG5, VALUE6, MFLAG6, QFLAG6, SFLAG6, VALUE7, MFLAG7, QFLAG7, SFLAG7, VALUE8, MFLAG8, QFLAG8, SFLAG8, VALUE9, MFLAG9, QFLAG9, SFLAG9, VALUE10, MFLAG10, QFLAG10, SFLAG10, VALUE11, MFLAG11, QFLAG11, SFLAG11, VALUE12, MFLAG12, QFLAG12, SFLAG12, VALUE13, MFLAG13, QFLAG13, SFLAG13, VALUE14, MFLAG14, QFLAG14, SFLAG14, VALUE15, MFLAG15, QFLAG15, SFLAG15, VALUE16, MFLAG16, QFLAG16, SFLAG16, VALUE17, MFLAG17, QFLAG17, SFLAG17, VALUE18, MFLAG18, QFLAG18, SFLAG18, VALUE19, MFLAG19, QFLAG19, SFLAG19, VALUE20, MFLAG20, QFLAG20, SFLAG20, VALUE21, MFLAG21, QFLAG21, SFLAG21, VALUE22, MFLAG22, QFLAG22, SFLAG22, VALUE23, MFLAG23, QFLAG23, SFLAG23, VALUE24, MFLAG24, QFLAG24, SFLAG24, VALUE25, MFLAG25, QFLAG25, SFLAG25, VALUE26, MFLAG26, QFLAG26, SFLAG26, VALUE27, MFLAG27, QFLAG27, SFLAG27, VALUE28, MFLAG28, QFLAG28, SFLAG28, VALUE29, MFLAG29, QFLAG29, SFLAG29, VALUE30, MFLAG30, QFLAG30, SFLAG30, VALUE31, MFLAG31, QFLAG31, SFLAG31))

df = pd.DataFrame(data = stationdata, columns=['ID', 'YEAR', 'MONTH', 'ELEMENT', 'VALUE1', 'MFLAG1', 'QFLAG1', 'SFLAG1', 'VALUE2', 'MFLAG2', 'QFLAG2', 'SFLAG2', 'VALUE3', 'MFLAG3', 'QFLAG3', 'SFLAG3', 'VALUE4', 'MFLAG4', 'QFLAG4', 'SFLAG4', 'VALUE5', 'MFLAG5', 'QFLAG5', 'SFLAG5', 'VALUE6', 'MFLAG6', 'QFLAG6', 'SFLAG6', 'VALUE7', 'MFLAG7', 'QFLAG7', 'SFLAG7', 'VALUE8', 'MFLAG8', 'QFLAG8', 'SFLAG8', 'VALUE9', 'MFLAG9', 'QFLAG9', 'SFLAG9', 'VALUE10', 'MFLAG10', 'QFLAG10', 'SFLAG10', 'VALUE11', 'MFLAG11', 'QFLAG11', 'SFLAG11', 'VALUE12', 'MFLAG12', 'QFLAG12', 'SFLAG12', 'VALUE13', 'MFLAG13', 'QFLAG13', 'SFLAG13', 'VALUE14', 'MFLAG14', 'QFLAG14', 'SFLAG14', 'VALUE15', 'MFLAG15', 'QFLAG15', 'SFLAG15', 'VALUE16', 'MFLAG16', 'QFLAG16', 'SFLAG16', 'VALUE17', 'MFLAG17', 'QFLAG17', 'SFLAG17', 'VALUE18', 'MFLAG18', 'QFLAG18', 'SFLAG18', 'VALUE19', 'MFLAG19', 'QFLAG19', 'SFLAG19', 'VALUE20', 'MFLAG20', 'QFLAG20', 'SFLAG20', 'VALUE21', 'MFLAG21', 'QFLAG21', 'SFLAG21', 'VALUE22', 'MFLAG22', 'QFLAG22', 'SFLAG22', 'VALUE23', 'MFLAG23', 'QFLAG23', 'SFLAG23', 'VALUE24', 'MFLAG24', 'QFLAG24', 'SFLAG24', 'VALUE25', 'MFLAG25', 'QFLAG25', 'SFLAG25', 'VALUE26', 'MFLAG26', 'QFLAG26', 'SFLAG26', 'VALUE27', 'MFLAG27', 'QFLAG27', 'SFLAG27', 'VALUE28', 'MFLAG28', 'QFLAG28', 'SFLAG28', 'VALUE29', 'MFLAG29', 'QFLAG29', 'SFLAG29', 'VALUE30', 'MFLAG30', 'QFLAG30', 'SFLAG30', 'VALUE31', 'MFLAG31', 'QFLAG31', 'SFLAG31'])
"""


stationdata = list(zip(ID, YEAR, MONTH, DAY, ELEMENT, VALUE, MFLAG, QFLAG, SFLAG))

df = pd.DataFrame(data = stationdata, columns=['ID', 'YEAR', 'MONTH', 'DAY', 'ELEMENT', 'VALUE', 'MFLAG', 'QFLAG', 'SFLAG'])


g.CleanStationData(df)

df.to_csv('test.csv',index=True,header=True)

print df
