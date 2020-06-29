text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
num = text[pos+1:]
num = num.strip()
value = float(num)
print(value)