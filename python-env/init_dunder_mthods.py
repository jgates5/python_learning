class Invoice:
  def __init__(self, client, total):
      self.client = client
      self.total = total

#raw data inside of a class
  def __str__(self):
    return f'Invoice from {self.client} for {self.total}'

  def __rep__(self):
    return f'Invoice <value: client: {self.client} total: {self.total}>'

inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

#the goals for dunder reper more for raw output to logs

#double underscores in front of the name. The reason for this speaks directly to how python works with private and protected methods inside of their classes
# __init__

# class string
# private/protcted methods

# 'my name'.upcase
