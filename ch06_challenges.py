
##text = "Camus"
##for i in text:
##    print(i)

#response_one = input("What did you write?: ")
#response_two = input("Who did you send it to?: ")
#text = "Yesterday I wrote a {}. I sent it to {}!".format(response_one, response_two)
#print(text)

#text = "aldous Huxley was born in 1894."
#print(text.upper()[:1] + text[1:])

text = "Where now? Who now? When now?"
#newlist = []
newlist = [text[0:10],text[11:19],text[20:]]
#print(newlist)
#print(text.index("?"))
#print(text.split(" "))

words = ["The","fox","jumped","over","the","fence","."]
text = " ".join(words)
text = text[:-2] + "."
#print(text)
text = "A screaming comes across the sky.".replace("s","$")
#print(text)
#print("Hemingway".index("m"))

text = """\"Behold!\" cried Sergey, striding towards a figure in a shabby overcoat
recumbent in the snow beneath one of the dovecotes."""
# print(text)
text = "three "
# newtext = text + text + text
# newtext = text*3
# print(newtext[:-1])
text = """It was a bright cold day in April,
and the clocks were striking thirteen."""
comma = text.index(",")
print(text[:comma])
