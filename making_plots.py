from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
all_fits = open('data/all_fits')
allFiles = all_fits.read()
all_files = allFiles.split('\n')
n = len(all_files) - 1
for i in range(0,n):
	file = 'data/' + all_files[i]
#	print file
	name = all_files[i][-len(all_files[i]):-5]
	figname = 'spectra_plots/' + name + '.png'
	title = name
	hdulist = fits.open(file)
	mydata = hdulist[0].data
	plt.figure()
	plt.plot(mydata/1.0e-17)
	plt.title(title, fontsize = 16)
	#plt.xlabel(r'$\lambda\(\mathrm{\AA})$')
	#plt.ylabel(r'Flux $(10^{-17}\mathrm{erg/s/cm^2/\AA})$')
	plt.savefig(figname)
	plt.close()
