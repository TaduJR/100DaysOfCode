# class MyFirstClass:
#   index = "Author-Book"
  
#   def hand_list(self, philosopher, book):
#     print(MyFirstClass.index)
#     print(philosopher + "wrote the book: " + book)

#   print("Who wrote this?")

# whodunnit = MyFirstClass()
# whodunnit.hand_list("Sun Tzu", "The Art of War")


class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)
A.a = 5
print(c.a, c.b)