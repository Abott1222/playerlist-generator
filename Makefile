run:
	FLASK_APP=app.py FLASK_DEBUG=true flask run

csvArtist:
	python3 create.py "MOCK_DATA.csv" "artist" 

csvVenue:
	python3 create.py "MOCK_DATA2.csv" "venue"

up:
	source ~/Desktop/coding/FULLSTACKPROJECTS/fyyur/bin/activate 
