import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.coordinates as coord

tbl010 = ascii.read("YOC_dummy010.csv", header_start=0, data_start=1,  delimiter=",")
tbl020 = ascii.read("YOC_dummy020.csv", header_start=0, data_start=1,  delimiter=",")
tbl030 = ascii.read("YOC_dummy030.csv", header_start=0, data_start=1,  delimiter=",")

print tbl010.colnames
print(tbl010['RA'])
print(tbl010['Dec'])

print tbl020.colnames
print(tbl020['RA'])
print(tbl020['Dec'])

ra010 = coord.Angle(tbl010['RA']*u.degree)
ra010 = ra010.wrap_at(180*u.degree)
dec010 = coord.Angle(tbl010['Dec']*u.degree)

ra020 = coord.Angle(tbl020['RA']*u.degree)
ra020 = ra020.wrap_at(180*u.degree)
dec020 = coord.Angle(tbl020['Dec']*u.degree)

ra030 = coord.Angle(tbl030['RA']*u.degree)
ra030 = ra030.wrap_at(180*u.degree)
dec030 = coord.Angle(tbl030['Dec']*u.degree)

fig = plt.figure()

ax = fig.add_subplot(111, projection='aitoff')

ax.scatter(ra010.radian, dec010.radian, color='b', alpha=0.3)
ax.scatter(ra020.radian, dec020.radian, color='r', alpha=0.6)
ax.scatter(ra030.radian, dec030.radian, color='g', alpha=0.9)

ax.set_xticklabels(['14h','16h','18h','20h','22h', '0h','2h','4h','6h','8h','10h'])
ax.grid()
plt.show()

