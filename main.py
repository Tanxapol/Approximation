import math

math_sign = {"e" : math.e, "pi" : math.pi}


def input_0():
  equation = input("Please enter equation : ") 
  n_low = float(input("Please enter lower : "))
  n_high = float(input("Please enter upper : "))
  n = int(input("Enter the number of range : "))
  print("")
  return(equation, n_low, n_high, n)

def find_range(equation, n_low, n_high, n):
  i = []
  xi = []
  yi = []
  delta_x = (n_high - n_low) / n

  for n in range(0,n+1):
    i.append(n)
    xi.append(n_low + (delta_x) * n)
    dict = {"x" : xi[n]}
    dict.update(math_sign)
    yi.append(eval(equation, {}, dict))

  return(i, xi, yi, delta_x)

def left_endpoints(i, yi, delta_x):
  ans = 0
  for i in range(0, len(i)-1):
    ans += yi[i] * delta_x

  return ans

def right_endpoints(i, yi, delta_x):
  ans = 0
  for i in range(1, len(i)):
    ans += yi[i] * delta_x

  return ans

def trapezoidal(i, yi, delta_x):
  ans = 0
  for i in range(1, len(i)):
    ans += (yi[i-1] + yi[i]) * delta_x / 2

  return ans

def simpson(i, yi, delta_x):
  if (len(i)-1) % 2 != 0:
    return -1
  ans = 0
  for i in range(1, len(i) - 1, 2):
    ans += (yi[i-1] + 4 * yi[i] + yi[i+1]) * delta_x / 3

  return ans

def display(equation, i, xi, yi, n, le, re, tra, sim):
  j = int(math.log10(n))
  print("i".center(j + 3), "|", "xi".center(j + 5), "|", "f(xi) = {}".format(equation))
  
  for i in range(0, len(i)):
    print(str(i).center(j + 3), "|", str(xi[i]).center(j + 5), "|", str(yi[i]).center(j + 3))
  print("")
    
  print("approximation by left endpoints :  ", le)
  print("approximation by right endpoints : ", re)
  print("approximation by trapezoidal :     ", tra)
  if sim == -1:
    print("Could not approximate by Simpson's Rule")
  else:
    print("approximation by Simpson's rule :  ", sim)

    
equation, n_low, n_high, n = input_0()
#equation, n_low, n_high, n = "1/x", 1, 2, 1000
i, xi, yi, delta_x = find_range(equation, n_low, n_high, n)
le = left_endpoints(i, yi, delta_x)
re = right_endpoints(i, yi, delta_x)
tra = trapezoidal(i, yi, delta_x)
sim =simpson(i, yi, delta_x)
display(equation, i, xi, yi, n, le, re, tra, sim)