# From the RRC data generate a well base map for North Coleman


import pandas as pd
import simplekml

# Read the data. Plugged and water supply wells were exluded
data = pd.read_csv('NC wells from RRC.csv')

kml = simplekml.Kml()

# Create a style for producer wells
producerStyle = simplekml.Style()
producerStyle.labelstyle.scale = 0.7
producerStyle.iconstyle.color = 'ff00ff00'  # light green
producerStyle.iconstyle.icon.href = \
	'http://maps.google.com/mapfiles/kml/shapes/donut.png'
producerStyle.iconstyle.scale = 0.7

# Create a style for injector wells
injectorStyle = simplekml.Style()
injectorStyle.labelstyle.scale = 0.7
injectorStyle.iconstyle.color = 'ffff0000'  # blue
injectorStyle.iconstyle.icon.href = \
	'http://maps.google.com/mapfiles/kml/shapes/donut.png'
injectorStyle.iconstyle.scale = 0.7

kml.document.name = 'North Coleman Well Base'

for point in data.iterrows():
	pnt = kml.newpoint(name=point[1].Lease_Name + ' ' + point[1].Well_No,
					   coords=[(point[1].Long83, point[1].Lat83)])

	pnt.style = injectorStyle if point[1].Well_Type == 'INJECTION' else \
		producerStyle

	# Had to use exptended data. Simply using balloonstyle was assiging one balloon
	# text to all the wells of the same shared style
	pnt.extendeddata.newdata(name='Well type / status',
							 value=str(point[1].Well_Type))

kml.save('North Coleman Well Base.kml')
