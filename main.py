



def main():
    def myfunc(n):
          return 0-n
    n = [2, 3, 5]
    x = list(n)
    x.append(6)

    n.extend(list(map(myfunc, (n))))
    n.sort()
    print(n)
    
if __name__== '__main__':
    main()
    

