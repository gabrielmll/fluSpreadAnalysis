# Preprocess for statistical analysis
# data output format:
#	date[yyyymmdd], id[1-80], gotFlu[0-1], interactions[sum], fluInteractions[sum],
#	healthInteractions[sum], sore.throat.cough[0-1, runnynose.congestion.sneezing[0-1], fever[0-1],
#	nausea.vomiting.diarrhea[0-1], gotPsySymp[0-1], psyInteractions[sum], noPsyInteractions[sum],
#	sadDepressed[0-1], openStressed[0-1]

import csv
import datetime, time

# This is to measure the running time. It has nothing to do with the whole algorithm
startTime = time.time()

# Function to increment one day
def incrementOneDay( d ):
	date = datetime.datetime.strptime(str(d), "%Y%m%d");
	date += datetime.timedelta(days=1);
	return date.strftime("%Y%m%d");

# Variables to manage days
current_day = 20090109;
#historical_threshold = -3;	# This doesn't matter for now, once I'm doing a file for each day

# Opening files
proximityFile = open('Proximity.csv', 'rb');
fluFile = open('FluSymptoms.csv', 'rb');
outputFile = open('spreadFluFeatures_singleDay.csv', 'wb');

try:
	# csv reader objects
	proximityReader = csv.reader(proximityFile);
	fluReader = csv.reader(fluFile);
	w = csv.writer(outputFile, delimiter=',');
	
	# output File header
	w.writerows([['date','id','gotFlu','interactions','fluInteractions','healthInteractions','sore.throat.cough','runnynose.congestion.sneezing','fever','nausea.vomiting.diarrhea','gotPsySymp','psyInteractions','noPsyInteractions','sadDepressed','openStressed']])

	while int(current_day) != 20090112:
		# skip the headers
		next(proximityReader, None);
		next(fluFile, None);

		print "---------------"
		print "Date "+str(current_day)
		# Output variables (in order/sorted)
		gotFlu = [0] * 81	# 0 or 1
		interactions = [0] * 81	# sum
		fluInteractions = [0] * 81	# sum
		# healthInteractions = [0] * 81 Not needed. It's just an subtraction: interactions - fluInteractions
		soreThroatCough = [0] * 81 # 0 or 1
		runnynoseCongSneezing = [0] * 81 # 0 or 1
		fever = [0] * 81 # 0 or 1
		nauseaVomDiar = [0] * 81 # 0 or 1
		gotPsySymp = [0] * 81 # 0 or 1
		psyInteractions = [0] * 81
		# noPsyInteractions = [0] * 81 Not needed. It's just an subtraction: interactions - psyInteractions
		sadDepressed = [0] * 81 # 0 or 1
		openStressed = [0] * 81 # 0 or 1

		# each row of the fluSymptom file
		# The reason Flu is being analysed first is that after we can easily check the amount of flu interactions
		for row in fluReader:
			# Formatting dates
			processedDate = long(row[1].replace("-", "").replace(":", "").replace(" ", ""))
			processedDate = processedDate/1000000 # remove hhmmss

			# for this day, compute the symptoms
			if processedDate == int(current_day):
				# Flu Symps
				if row[2] == '1':
					gotFlu[int(row[0])] = 1
					soreThroatCough[int(row[0])] = 1
				if row[3] == '1':
					gotFlu[int(row[0])] = 1
					runnynoseCongSneezing[int(row[0])] = 1
				if row[4] == '1':
					gotFlu[int(row[0])] = 1
					fever[int(row[0])] = 1
				if row[5] == '1':
					gotFlu[int(row[0])] = 1
					nauseaVomDiar[int(row[0])] = 1
				# Psy Symps
				if row[6] == '1':
					gotPsySymp[int(row[0])] = 1
					sadDepressed[int(row[0])] = 1
				if row[7] == '1':
					gotPsySymp[int(row[0])] = 1
					openStressed[int(row[0])] = 1

		# each row of the proximity file
		for row in proximityReader:
			# Formatting dates
			processedDate = long(row[2].replace("-", "").replace(":", "").replace(" ", ""))
			processedDate = processedDate/1000000 # remove hhmmss

			# for this day, compute the number of interactions
			if processedDate == int(current_day):
				interactions[int(row[0])]+=1
				interactions[int(row[1])]+=1

				# if target got flu, source interacts with flu and vice-versa
				if gotFlu[int(row[0])] == 1:
					fluInteractions[int(row[1])]+=1
				if gotFlu[int(row[1])] == 1:
					fluInteractions[int(row[0])]+=1
				if gotPsySymp[int(row[0])] == 1:
					psyInteractions[int(row[1])]+=1
				if gotPsySymp[int(row[1])] == 1:
					psyInteractions[int(row[0])]+=1

		# pop the 0ith array position
		interactions.pop(0)
		gotFlu.pop(0)
		fluInteractions.pop(0)
		soreThroatCough.pop(0)
		runnynoseCongSneezing.pop(0)
		fever.pop(0)
		nauseaVomDiar.pop(0)
		gotPsySymp.pop(0)
		psyInteractions.pop(0)
		sadDepressed.pop(0)
		openStressed.pop(0)
		for i in range(len(interactions)):
			w.writerow([current_day, i+1, gotFlu[i], interactions[i], fluInteractions[i],interactions[i]-fluInteractions[i],soreThroatCough[i],runnynoseCongSneezing[i],fever[i],nauseaVomDiar[i],gotPsySymp[i],psyInteractions[i],interactions[i]-psyInteractions[i],sadDepressed[i],openStressed[i]]);

		current_day = incrementOneDay( current_day );
		proximityFile.seek(0);
		fluFile.seek(0);

except ValueError, e:
	print "Error ", e

finally:
	proximityFile.close()
	fluFile.close()

# This is to measure the running time. It has nothing to do with the whole algorithm
endTime = time.time() - startTime;
print(endTime);