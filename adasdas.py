# string = "bank al habib"
# z = string.split()
# for i in z:
#     c = i
#     c = c[0:-1]+c[-1].upper()
#     z[z.index(i)] = c

# print(" ".join(z))


string = "this is a string"
string = string.split()

for i in string:
    x = list(i)
    x[-1] = x[-1].upper()
    x = "".join(x)
    string[string.index(i)] = x 
    

print(" ".join(string))

import tkinter

k = tkinter.Tk()
k.mainloop()