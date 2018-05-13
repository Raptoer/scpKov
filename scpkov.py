from markmywords import Markov

text = ''

for i in range(2, 174):

    with open("input/contain/%0.3d.txt" % i, "r") as f:
        text += f.read()
m = Markov(text, degree=2)
l = ["Special", "Containment"]
print(m.generate(max_words=300, seed=l))