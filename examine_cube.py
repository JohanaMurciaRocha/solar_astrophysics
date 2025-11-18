from astropy.io import fits # fits allows us to open fits files 
import matplotlib.pyplot as plt #enables us to plot, and save plots to files 
import numpy as np # gives us a lot of neat built-in operations 
import sys # this will allow us to provide file name as a script argument 

cube = fits.open(sys.argv[1])[0].data #this gives us a 4D cube of data 

#first two dimensions  - x, y in the plane of the sky 
#third one is always 4, for 4 Stokes parametes, we only use index 0 
#fourth one - wavelength

#let's plot something and write to a file 
plt.clf()
plt.cla() #clears previous plots 
plt.imshow(cube[:,:,0,0]) #plots intensity image at wavelength 0 
plt.title("Intensity map at wavelengt with index 0")
plt.tight_layout()
plt.savefig("intensity_map_0.png",bbox_inches='tight')

#now let's do another wavelength 
plt.clf()
plt.cla() #clears previous plots 
plt.imshow(cube[:,:,0,29]) #plots intensity image at wavelength 29, make sure 29 actually exists 
plt.title("Intensity map at wavelengt with index 29")
plt.tight_layout()
plt.savefig("intensity_map_29.png",bbox_inches='tight')

#now let's take a look at the average spectra
mean_spectrum = np.mean(cube,axis=(0,1))
#let's plot something and write to a file 
plt.clf()
plt.cla() #clears previous plots 
plt.plot(mean_spectrum[0])
plt.title("Mean intensity spectrum of the image")
plt.tight_layout()
plt.savefig("mean_spectrum.png",bbox_inches='tight')


