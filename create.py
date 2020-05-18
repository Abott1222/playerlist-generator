import csv
import app
from app import Artist, db

with open('MOCK_DATA.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	
	try:
		for row in spamreader:
			x = Artist(name=row[1], city=row[2], state=row[3], phone=row[4])
			db.session.add(x)
			db.session.commit()
	except:
		db.session.rollback()
	finally:
		db.session.close()
		
