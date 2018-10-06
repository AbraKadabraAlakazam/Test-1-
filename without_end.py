def without_end(s):
    s1 = s[1:int(len(s))-1]
    return s1


if without_end("Hello") == "ell":
    print("correct")
    
