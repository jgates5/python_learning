class Invoice:
  def __init__(self, client, total):
      self.client = client
      self.total = total

  def __str__(self):
    return f'Invoice from {self.client} for  {self.total}'

inv = Invoice('Google', 500)
print(str(inv))

#double underscores in front of the name. The reason for this speaks directly to how python works with private and protected methods inside of their classes
# __init__

# class string
# private/protcted methods

# 'my name'.upcase
