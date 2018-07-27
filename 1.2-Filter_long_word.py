def filter_long_words(z,n):
        lst=[]
        Value=n[0]
        for h in z:
            if len(h) > Value:
                lst.append(h)
        return lst
        
        
z=[str(i) for i in input("Enter each Character with comma(,) separated: ").split(',')]
n=[int(j) for j in input("Ineger to gather strings: ")]
filter_long_words(z,n)