import matplotlib.pyplot as plt
quarks = {
    "u": {"Q": 2/3,  "I3": 1/2,  "St": 0,  "B": 1/3},
    "d": {"Q": -1/3, "I3": -1/2, "St": 0,  "B": 1/3},
    "s": {"Q": -1/3, "I3": 0,    "St": -1, "B": 1/3},
    "U": {"Q": -2/3, "I3": -1/2, "St": 0,  "B": -1/3},
    "D": {"Q": 1/3,  "I3": 1/2,  "St": 0,  "B": -1/3},
    "S": {"Q": 1/3,  "I3": 0,    "St": 1,  "B": -1/3},
}
def properties(particle):
    total = {"Q": 0, "I3": 0, "St": 0, "B": 0}
    for letter in particle:
        for key in total:
            total[key] += quarks[letter][key]
    total["Y"] = total["B"] + total["St"]
    for key in total:
        total[key] = round(total[key], 3)
    return total

           
mesons = {
    "pi+":   "uD",
    "pi-":   "dU",
    "K+":    "uS",
    "K0":    "dS",
    "K-":    "sU",
    "K0bar": "sD",
    "pi0":   "uU",
    "eta":   "dD",
}
offsets = {"pi0": (-30, 10), "eta": (10, -15)}


for name, content in mesons.items():
    print(name, properties(content))
    
    result=properties(content)
    x=result["I3"]
    y=result["Y"]
    plt.scatter(x, y)
    plt.annotate(name, (x, y),textcoords="offset points",
             xytext=offsets.get(name, (8,8)))

plt.xlabel("I3")
plt.ylabel("Y")
plt.title("Meson octet")
plt.xlim(-1.5,1.5)
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.savefig("meson_octet.png")
plt.show()

