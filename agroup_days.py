import csv
import datetime

# Function to decrement "interval" day(s)
def decrementDay( d, interval ):
	date = datetime.datetime.strptime(str(d), "%Y%m%d");
	date += datetime.timedelta(days=interval);
	return date.strftime("%Y%m%d");

# variables of time
current_day = 20090109
interval = -7

# Opening file
singleDayFile = open('spreadFluFeatures_singleDay.csv', 'rb')
outputFile = open('spreadFluFeatures_7days.csv', 'wb')

try:
	# csv reader object
	singleDay = csv.reader(singleDayFile)
	w = csv.writer(outputFile, delimiter=',')
	
	# copy header
	w.writerows([next(singleDay)])
	for subject in range(1, 81):
		# subject features
		gotFlu = 0
		interactions = 0
		fluInteractions = 0
		healthInteractions = 0
		sore = 0
		runnynose = 0
		fever = 0
		nausea = 0
		gotPsySymp = 0
		psyInteractions = 0
		noPsyInteractions = 0
		sadDepressed = 0
		openStressed = 0

		for row in singleDay:
			if int(row[0]) < current_day or int(row[0]) > decrementDay(current_day, interval):
				gotFlu == 0 if int(row[2]) else gotFlu
				interactions += int(row[3])
				fluInteractions += int(row[4])
				healthInteractions += int(row[5])
				sore == 0 if int(row[6]) else sore
				runnynose == 0 if int(row[7]) else runnynose
				fever == 0 if int(row[8]) else fever
				nausea == 0 if int(row[9]) else nausea
				gotPsySymp == 0 if int(row[9]) else gotPsySymp
				psyInteractions += int(row[10])
				noPsyInteractions += int(row[11])
				sadDepressed == 0 if int(row[12]) else sadDepressed
				openStressed == 0 if int(row[13]) else openStressed
		
		w.writerows([[current_day, subject, gotFlu, interactions, fluInteractions, healthInteractions, sore, runnynose, fever, nausea, gotPsySymp, psyInteractions, noPsyInteractions, sadDepressed, openStressed]])
				
finally:
	singleDayFile.close()