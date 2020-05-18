import app
from app import Venue, Artist, db

cbg = Venue(name='CBGB', city='New York City', state='New York', address='315 Bowery', phone='7182328764')
b = Venue(name='Punk City', city='Seattle', state='New York', address='315 Bowery', phone='7182328764')
c = Venue(name='The Unicorn', city='Seattle', state='Washington', address='115 5th Ave', phone='2163238721')
d = Venue(name='The Jefferson', city='San Francisco', state='California', address='1032 Polk St', phone='4153435678')
e = Venue(name='Ambraisia', city='Portland', state='Oregon', address='81 Main St', phone='7274159000')
f = Venue(name='Gorge Amphitheatre', city='Seattle', state='Washington', address='123 Random', phone='2061009275')
g = Venue(name='Hollywood Bowl', city='Los Angeles', state='California', address='456 Random', phone='8214830213')
h = Venue(name='Red Rocks Park and Amphitheatre', city='Los Angeles', state='California', address='78910 Random', phone='4215169484')
i = Venue(name='Radio City Music Hall', city='Seattle', state='Washington', address='712 Broadway', phone='9212829572')
j = Venue(name='Detroit Rock City', city='Detroit', state='Michigan', address='921 Broadway', phone='2839872323')
k = Venue(name='Jones Beach Theater', city='San Francisco', state='California', address='100 Main', phone='2157401000')
l = Venue(name='Merriweather Post Pavilion', city='Portland', state='Oregon', address='321 Hillside Drive', phone='7087209101')
m = Venue(name='Madison Square Garden', city='Seattle', state='Washington', address='762 Hollywood', phone='1234561212')

db.session.add(cbg)
db.session.add(b)
db.session.add(c)
db.session.add(d)
db.session.add(e)
db.session.add(f)
db.session.add(g)
db.session.add(h)
db.session.add(i)
db.session.add(j)
db.session.add(k)
db.session.add(l)
db.session.add(m)

db.session.commit()

