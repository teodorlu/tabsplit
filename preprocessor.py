#! /usr/bin/env python
from sys import stdin, stderr

def main():
	data = [];
	for l in stdin:
		if len(l) > 1 and l[0] != "#":
			infolist = l.strip().replace(',', '').split()
			data.append(infolist)
	# payments = map(parsepayment, data)
	payments = []
	for d in data:
		try:
			payments.append(parsepayment(d))
		except Exception, e:
			stderr.write("Cannot parse line: " + ",".join(d) + "\n")
			raise error("Invalid parsing")
	moneystate = calculatebalance(payments)
	for (person, money) in moneystate.iteritems():
		print (person + ": " + str(money))

def isnumber(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def parsepayment(payment):
	isperson = lambda w: w[0].istitle()
	people = filter(isperson, payment)
	start = payment.index(people[0])
	numbers = filter(isnumber, payment[start:])

	payer = people[0]
	amount = float(numbers[0])
	leechers = people[1:]
	return (payer, amount, leechers)

# Name of a person's amount of money, plus or minus?
def calculatebalance(payments):
	d = {}
	for payment in payments:
		(payer, amount, leechers) = payment
		for person in [ payer ] + leechers:
			if not person in d:
				d[person] = 0

		d[payer] += amount
		for l in leechers:
			d[l] -= amount / len(leechers)

	return d

if __name__ == "__main__":
	try:
		main()
	except Exception, e:
		stderr.write("Error in your input format. Exiting.\n")
