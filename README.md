MailingCards
============
A Short Story
-------------
Some time ago the county was creating mailing cards for registered voters. This was to notify them of an upcoming election or if their polling place had changed since the last election. This worked for some time.

However, the mailing cards were pretty plain/ugly, just generated by a simple report.

Our print shop wanted to make something nice, but I didn't want to change the report each election. That's where *this* script took over.

Usage
-----
The input directory has two sub directories - address and location
- address - This is where you place the address report output
- location - This is where you place the sheet you want to inject between each address page

The output directory will have the output.

The only thing you need to modify (at the moment) is the fname in gen.py. It is assumed that the input/address, input/location report files are named the same and the output will have that same name as well.

TODO:
- Command line support