tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]
print(tags[1:4:2]) #= ['development', 'code']


"""
I want you to think in a little bit more of a production application
 there are going to be times where an algorithm might return a slice and you have
  no idea what the start stop and step points are
  """
  #you will write out three of the following in your project
#slice class
#you can call slice obect 2 anywhere in your program
slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj]) #= ['python', 'development']







