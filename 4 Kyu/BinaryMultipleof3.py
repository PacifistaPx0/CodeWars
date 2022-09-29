#A Regex program that checks to see if a binary number is divisible by 3
import re

PATTERN = re.compile(r'^(0|1(01*0)*1)*$')

print(bool(PATTERN.match('111')))