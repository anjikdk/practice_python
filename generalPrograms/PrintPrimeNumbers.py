class PrimeNumbers:

    def printPrimeNumbers(self, thistuple):
        # lower = int(input("Enter lower range: "))  
        # upper = int(input("Enter upper range: "))  

        primeList = []
        for num in thistuple:  
            if num >= 1:  
                for i in range(2,num):  
                    if (num % i) == 0:  
                        break  
                else:  
                    #    print(num) 
                    primeList.append(num)

        print(primeList) 






