
import random
import time

import station


class NullMac(station.Station):
	'''
	`NullMac` is essentially having no MAC protocol. The node sends at 0 dB on
	channel 1 whenever it has a packet ready to send, and tries up to two
	retries if it doesn't receive an ACK.

	The node makes no attempt to avoid collisions.
	'''
	def __init__(self, id, q_to_ap, q_to_station, interval):
		super().__init__(id, q_to_ap, q_to_station, interval)

	def run(self):
		# Continuously send packets
		while True:
			# Block until there is a packet ready to send
			pkt = self.wait_for_next_transmission()

			# Try up to three times to send the packet successfully
			for i in range(0, 3):
				response = self.send(pkt, 0.0, 1)

				# If we get an ACK, we are done with this packet. If all of our
				# retries fail then we just consider this packet lost and wait
				# for the next one.
				if response == 'ACK':
					break


class YourMac(station.Station):
	'''
	`YourMac` is your own custom MAC designed as you see fit.

	The sender should use up to two retransmissions if an ACK is not received.
	'''
	def run(self):
		while True:
			# Block until there is a packet ready to send
			pkt = self.wait_for_next_transmission()
			# Implement your MAC protocol here.
			sent = False
			picked = False
			channel = random.randint(1, 11)
			tries = 0
			while not picked:
				if not self.sense(channel):
					picked = True
				else:
					channel += 1
					if channel == 12:
						channel = 1
			while not sent and tries < 3:
				tries += 1
				if self.send(pkt, 12, channel) == "ACK":
					# YAY sent correctly
					sent = True
				else:
					# OH NO wait a random amount of time
					time.sleep(random.random()*0.2+0.1)
				
	# DO NOT CHANGE INIT
	def __init__(self, id, q_to_ap, q_to_station, interval):
		super().__init__(id, q_to_ap, q_to_station, interval)

