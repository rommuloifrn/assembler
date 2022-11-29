def processo(element):
    element = element*2
    return element

myarr = [1,2,3]
for n in myarr:
    n = processo(n)


print("for baseado no array: ", myarr)

for i in range(len(myarr)):
    myarr[i] = myarr[i] + 1

print("for baseado no tamanho do array:", myarr)