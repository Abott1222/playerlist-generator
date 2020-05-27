import csv
import sys
import app
from app import Artist,Venue,db

print(str(sys.argv))
if len(sys.argv) > 2:
	className = str(sys.argv[2])
	fileName = str(sys.argv[1])
	print()
	with open(fileName, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		print('here')
		try:
			for row in spamreader:
				print(row)
				if className == 'artist':
					x = Artist(id=row[0], name=row[1], city=row[2], state=row[3], phone=row[4])
					print(x)
					db.session.add(x)
				elif className == "venue":
					x = Venue(id=row[0], name=row[1], city=row[2], state=row[3], address=row[4], phone=row[5], image_link=row[6])
					print(x)
					db.session.add(x)
				print(x)
			db.session.commit()
		except:
			print("fucked up")
			db.session.rollback()
		finally:
			db.session.close()
else:
	print("You forgot to add the file of the csv and the direction")
		
