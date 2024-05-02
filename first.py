# for the first quesion of learning path of a2sv
xk=list(map(int,input().split()))
x=xk[0]
k=xk[1]
p=input()
if eval(p) == k: # p expression is evaluated # to ckeck if p(x) =k
   # Evaluate the string and print the result
   print('True')
else:
   print('False')
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    string = input().strip()
    
    if eval(string) == k:
        print(True)
    else:
        print(False)