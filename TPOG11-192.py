# Что там в строке
def countsymbol(str, chr) :
    count=0
    for char_index in range(len(str)):
       if str [char_index] ==chr:
           count=count+1
    return count

str=input("Введите выражение: ")
chr=input("Введите символ: ")
print("Символ {0} встречается {1} раз".format(chr, countsymbol(str,chr)))

