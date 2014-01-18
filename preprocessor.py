#! /usr/bin/env python
from sys import stdin

def main():
	data = [];
	for l in stdin:
		infolist = l.strip().replace(',', '').split()
		data.append(infolist)
	payments = map(parsepayment, data)
	moneystate = calculatemoney(payments)
	for (person, money) in moneystate.iteritems():
		print person + ": " + str(money)

def parsepayment(payment):
	payer = payment[0]
	amount = payment[2]
	leechers = payment[4:]
	return (payer, amount, leechers)

# Name of a person's amount of money, plus or minus?
def calculatemoney(payments):
	d = {}
	for payment in payments:
		payer = payment[0]
		leechers = payment[2]
		for person in [ payer ] + leechers:
			if not person in d:
				d[person] = 0

	return {'Teodor': 40, "Erik": 60}

if __name__ == "__main__":
	main()
