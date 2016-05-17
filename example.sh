#!/bin/bash
# python2.2

for i in examples/buy.nw examples/simple.nw examples/param.nw; do
    echo "--- $i ---"
    novelwriting "$i"
    echo -e "---\n"
done

#--- examples/buy.nw ---
#ultraparrot is great.  It's better than dynapython.
#Buy ultraparrot today!
#---
#
#--- examples/simple.nw ---
#Cardinal Fang once said that no-one expects the Spanish Inquisition.
#
#---
#
#--- examples/param.nw ---
#Tiddles is a cat
#---

