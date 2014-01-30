#! /usr/bin/env python
from sys import stdin, stderr

def main():
	data = []
	aliases = {}
	for l in stdin:
		if len(l) > 1 and l[0] != "#":
                        l = l.replace(',', '')
			if l[:6] == "alias ":
				s = l.split('=')
				alias = s[0][6:].strip()
				replacement = s[1].strip()
				aliases[alias] = replacement
			else:
				infolist = replacealias(l.strip(), aliases).split()
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

def replacealias(text, aliasdict):
	text = text.split()
	newtext = []
	for word in text:
		if word in aliasdict:
			newword = aliasdict[word]
		else:
			newword = word
                newtext.append(newword)
	return ' '.join(newtext)

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
