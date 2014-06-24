#this file reads in a list of files from 'all_fits.lis' and plots spectra of all the files! to be run from the field_scripts folder

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
all_fits = open('/../analysis/all_fits.lis')
allFiles = all_fits.read()
all_files = allFiles.split('\n')
n = len(all_files) - 1

#get wave function allows us to print actual wavelengths!
def get_wave(hdulist):
	prihdr = hdulist[0].header
	keywords = prihdr.keys()
	wave=[]
	#check the header values
	# CTYPE1 - get
	if 'CTYPE1' not in prihdr:
		print 'CTYPE1 is not defined, fatal error'
		return
	ctype = prihdr['CTYPE1']
	# continue if linear
	if ctype1 != 'LINEAR':
		print 'CTYPE1 is not linear, write a new program'
		return
	# NAXIS - number of elements in array
	if 'NAXIS1' not in prihdr:
		print 'NAXIS1 not defined, fatal error'
		return
	num = prihdr['NAXIS1']
	#print 'NAXIS1',num
	#CRVAL - starting wavelength
	if 'CRVAL1' not in prihdr:
		#print 'CRVAL1 not defined, fatal error'
		return
	crvall = prihdr['CRVAL1']
	if 'CDELT1' not in prihdr:
		print 'CDELT1 not defined'
		return
	cdelt1 = prihdr['CDELT1']
	for ii in range(0, num):
		wave.append(crvall + ii*cdelt1)
	if wave != []:
		return wave
	if 'CD1_1' not in prihdr:
		print 'CD1_1 not defined'
		return
	cd1_1 = prihdr['CD1_1']
	for iii in range(0,num):
		wave.append(crvall + iii*cd1_1)
	if wave != []:
		return wave

for i in range(0,n):
	filename = '../data/' + all_files[i] + '.fits'
#	print file
	name = all_files[i]
	figname =  name + '.eps'
	title = name
	hdulist = fits.open(filename)
	mydata = hdulist[0].data
	plt.figure()
	plt.plot(get_wave(hdulist), mydata/1.0e-17)
	plt.title(title, fontsize = 16)
	#plt.xlabel(r'$\lambda\(\mathrm{\AA})$')
	#plt.ylabel(r'Flux $(10^{-17}\mathrm{erg/s/cm^2/\AA})$')
	plt.savefig(figname)
	plt.close()
