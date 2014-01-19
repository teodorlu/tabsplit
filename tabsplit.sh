#/bin/sh
cat sampleinput.tab | python2 preprocessor.py | runhaskell processor.hs
