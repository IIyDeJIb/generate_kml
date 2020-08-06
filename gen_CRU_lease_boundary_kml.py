import pandas as pd
import simplekml
import numpy as np

data = pd.read_csv('leaseBoundary.csv')

kml = simplekml.Kml()

ls = kml.newlinestring(name='CRU_lease_boundary',
					   coords=[tuple(np.roll(x[1].values,1)) for x in
							   data.iterrows()])
ls.linestyle.color = 'ff00ffff'
ls.linestyle.width = 2

kml.save('CRU_lease_boundary.kml')
