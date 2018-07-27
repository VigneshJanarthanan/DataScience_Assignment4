def len_words(k):
    length=[]
    for i in range(len(k)):
        x=len(k[i])
        length.append(int(x))
    return length
    

lst=["Vignesh","Janarthanan","ACADGILD","MACHINELEARNING"]
print("Length of each word given",len_words(lst))