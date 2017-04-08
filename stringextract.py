text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')

ext = text[pos:pos+6]
number = float(ext)
print number