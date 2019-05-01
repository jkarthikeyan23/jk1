>>> from constraint import *
>>> problem=problem()
>>> problem.addvariable("a",[1,2,3])
>>> problem.addvariable("b",[4,5,6])
>>> problem.getsolutions()
[{'a':3,'b':6},{'a':3,'b':5},{'a':3,'b':4},
 {'a':2,'b':6},{'a':2,'b':5},{'a':2,'b':4}
 {'a':1,'b':6},{'a':1,'b':5},{'a':1,'b':4}
 
 >>> problem.addconstraint(lambda a,b:
 a*2==b,("a","b"))
 >>> problem.getsolutions()
 [{'a':3,'b':6},{'a':2,'b':4}]
 
 >>> problem=problem()
 >>> problem.addvariable(["a","b"],[1,2,3])
 >>> problem.addconstraint(AllDifferenceconstraint())
 >>> problem.getsolutions()
 [{'a':3,'b':2},{'a':3,'b':1},{'a':2,'b':3}
  {'a':2,'b':1},{'a':1,'b':2},{'a':1,'b':3)]
