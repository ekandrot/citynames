# citynames
Generate city names based on US city dictionary

# How does it work

It calculates the distribution of first letters.  The same for second letters, this way keeping all initial letters separate from generic combos of letters with the names that might also be capitalized.

Then one uses either the combos2 or combos3, both of which have dictionaries of dictionaries.  combos2 uses one letter as the key, combos3 uses two letters as the key.  Using a weighted selection from these dictionaries and the the previous letter(s), it generates a new letter.  Repeat.

The code is slapped together as a proof of concept.  It is runs fast enough that I do not see it, so no need to "fix" it.  If one wants to use it over much larger databases, I'd rewrite the code, using this as a basis.

# Inspiration

I watched https://youtu.be/KvoZU-ItDiE live this morning.  When he got to the results, the words didn't look too English-y, and he said it would take 20 minutes to run.  I knew it could be made to run faster and generate "better" results with simple tables, so I slapped this code together quickly to test my belief.

# Source of Data

I used the city names from: https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt
which I pulled out of the code from:  https://github.com/llSourcell/build_a_neural_net_live/blob/master/lstm.py

You can use your own city names (or any other list of words), just replace the file loading code at 27-ish.

# Results
Using combos of the previous letter only, I saw this list:

Gelertlllemione Wurdlenthmbeacer
Winaraw Sthieearge
Gorprrtog Betere
Hen Hag
Inalilo
Cashble
Cotou
Wils
Wey
Ce
Madiby Bak
Kitos
Glle Mant Cimirktolmes
Hilanewinchatokilsmaratelwne Paveso
Bl
Shis
Mortckverpiobellle Howd
Wale
Tin
Eagenes


switching to comobos of the previous two letters, this was the output:
Nored
Hya
Amyrt Heighta
Cora
Holii
Hilto
Lent
Ken
Dixisapity
Ful
Thrint
Sing
Krinte Hille
Kimon City
Nahooron
Mernetta
Apton
Bay
Weste Bart
Moshiond
