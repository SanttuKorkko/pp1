string = 'X-DSPAM-Confidence: 0.8475'
col_pos = string.find(':')
number = string[col_pos + 1:]
floating = float(number)
print(floating)