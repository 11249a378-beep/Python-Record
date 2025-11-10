import random
value = random.choice(["h","t"])
choice=input("make your choice( h or t )")
if value == choice:
    print("you won")
else:
    print("bad luck")
if value == "h":
    print("computer selected tail")
elif value == "t":
    print("computer selected  head")
