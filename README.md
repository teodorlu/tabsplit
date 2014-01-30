Tabsplit
========

Splits a tab based on an easily readable input file.

Usage: `./tabsplit.sh < sampleinput.tab`

- Input format:
  - Names start with a capital letter
  - The first name is the payer
  - The remaining names are the leechers
  - Amount is the first number after the payer

- Aliases
  - When line starts with "alias", the line is an alias declaration
  - Usage example: `alias Everyone = Teodor, Erik, Cecilie, Jones, Jack and Nick`
