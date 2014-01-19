#/bin/sh
MYDIR="$(dirname "$(readlink -f "$0")")"
python2 $MYDIR/preprocessor.py | runhaskell $MYDIR/processor.hs
