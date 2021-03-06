#By Matthew Ippolito and Nicholas Palmer (mri6hfb and np6mec)
import math


def calculate_path_loss_db(d_meters):
	'''
	Calculate the free space path loss for a transmission `d` meters.

	The return value is in decibels.
	'''
	FSPL = (4*3.1415962*d_meters*(2.4*1000000000)/(300000000))
	
	logged = 20*math.log10(abs(FSPL))
	# dummy value, replace this
	return logged



def calculate_snr_db(tx_power_db, path_loss_db, noise_db):
	'''
	Calculate the signal-to-noise ratio at the receiver based on
	the transmit power, the path loss, and the noise at the receiver.

	All values, including the return value, are in decibels.
	'''
	signal = tx_power_db - path_loss_db
	SNR = signal - noise_db
	# dummy value, replace this
	return SNR

