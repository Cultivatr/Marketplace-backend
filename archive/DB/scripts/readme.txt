from within the shell, pytest wouldn't work.  

pipenv graph showed nothing - so tried pipenv sync.

this installed the dependencies including pytest

then pytest worked as expected.

try pipenv graph to see what's installed.

also connect requires ssl='disable', password='cultivatr'
