from flask import Flask
import json

app = Flask(__name__)
#Python program to check if given number is prime or not
    num = n
    if num > 1:
        for i in range(2, num//2):
            
    #If num is divisible by any number between 2 and n / 2, it is not prime
            
    if (num % i) == 0:
         print(num, "is not a prime number")
          break
     else: 
         print(num, "is a prime number")
                
     else:
         print(num, "is not a prime number")
       
    except ValueError:
        return "Please use a number as the 'n' argument"
  output = {
        "input": n,
        "output": num()
    }
    return json.dumps(output)

