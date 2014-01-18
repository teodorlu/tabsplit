#! /usr/bin/env python
from sys import stdin

def main():
	data = [];
	for l in stdin:
		infolist = l.strip().replace(',', '').split()
		data.append(infolist)
	payments = map(parsepayment, data)
	print payments

def parsepayment(payment):
	payer = payment[0]
	amount = payment[2]
	leechers = payment[4:]
	return (payer, amount, leechers)

if __name__ == "__main__":
	main()
