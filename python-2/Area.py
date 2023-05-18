import MyFunctions as mF

Prompt = "Choose a shape: t=triangle, r=rectangle, c=circle: "
Arg = (("base", "height"), ("width", "height"), ("radius",))
cb = ": "  # colon blank
Msg = {
    "base": "Give the base: ",
    "height": "Give the height: ",
    "width": "Give the width: ",
    "radius": "Give the radius: "
}

while True:
    choice = input(Prompt).upper()
    if choice == "":
        break
    else:
        if choice == "T":
            i = 0
            base = input(Msg[Arg[i][0]])
            height = input(Msg[Arg[i][1]])
            try:
                base = int(base)
                height = int(height)
            except ValueError as e:
                print(e)
                continue
            area = mF.Area(shape=choice, base=base, height=height)
            print(f"{'The area is:':12} {area:.2f}")
        elif choice == "R":
            i = 1
            width = input(Msg[Arg[i][0]])
            height = input(Msg[Arg[i][1]])
            try:
                width = int(width)
                height = int(height)
            except ValueError:
                continue
            area = mF.Area(shape=choice, width=width, height=height)
            print(f"{'The area is:':12} {area:.2f}")
        elif choice == "C":
            i = 2
            radius = input(Msg[Arg[i][0]])
            try:
                radius = int(radius)
            except ValueError:
                continue
            area = mF.Area(shape=choice, radius=radius)
            print(f"{'The area is: ':12} {area:.2f}")
        else:
            print("Unknown shape!")
