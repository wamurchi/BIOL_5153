#! /usr/bin/env python3

import re 

the_concert = 'Katherine went to the concert to see Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out.'

print('the_concert:', the_concert)

#the long/wrong? option(#1)

start = []
end = []   


k1 = re.search("Katherine", the_concert)
for find in k1:
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
#print the name and the length
print(k1.group())
print("the length of k1 is:", len(k1.group()))

k2 = re.search("katharine", the_concert)
#find the start and end position
for find in k2:	
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
#print the name and the length
print(k2.group())
print("the length of k2 is:", len(k2.group()))

k3 = re.search("Kathryn", the_concert)
#find the start and end position
for find in k3:	
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
#print the name and the length
print(k3.group()) 
print("the length of k3 is:", len(k3.group()))

k4 = re.search("Kathrin", the_concert)
#find the start and end position
for find in k4:	
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
#print the name and the length
print(k4.group()) 
print("the length of k4 is:", len(k4.group()))

c1 = re.search("Catheryn", the_concert)
#find the start and end position
for find in c1:	
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
#print the name and the length
print(c1.group())
print("the length of c1 is:", len(c1.group()))

c2 = re.search("Catherine", the_concert)
#find the start and end position
for find in c2:	
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
print(c2.group())
print("the length of c2 is:", len(c2.group()))

c3 = re.search("Cathryn", the_concert)
#find the start and end position
for find in c3:	
	find_start = find.start()
	start_position.append(find_start)
	find_End = find.end()
	stop_position.append(find_End)
	print(str(find_start) + "to" + str(find_end))
#print the name and the length
print(c3.group()) 
print("the length of c3 is:", len(c3.group()))

###########################################################################
#option 2 

#find the start and the end position 
match =  re.search(A|C(ath(a-z)), the_concert)

for i in match:
	the_start = find.start()
	start_position.append(the_start)
	the_End = find.end()
	stop_position.append(the_End)
	print(str(find_start) + "to" + str(find_end))

#find the names and print them and their lengths
match_2 = re.search ("K|C(ath)(ryn)(rine)", the_concert)
if match: 
	print("capture 0:", match.group(0))
	print("match length:" len(match.group(0)))
    print("capture 1:", match.group(1))
    print("match length:" len(match.group(1)))
    print("capture 2:", match.group(2))
    print("match length:" len(match.group(2)))
else:
    print("No match")

#print in columns

NAMES = (match.group(0), match.group(1), match.group(2))
open.NAMES = csv.writer(file, delimiter='\t')
