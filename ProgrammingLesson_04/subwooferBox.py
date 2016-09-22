def subWoofer(subwooferBox):
    output = ("{:5.2f}".format(subwooferBox))
    return output

length = float(input("What is the length in cubic inches?" ))
width = float(input("What is the width in cubic inches?"))
height = float(input("What is the height in cubic inches?"))

subwooferBox = (length * width * height)/1728

print("The volume of your subwoofer box is ",subWoofer(subwooferBox),"ft**3")
