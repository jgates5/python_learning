#place one function inside of another function
"""
def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')
"""
def greeting(your, name):
    def full_name():
        return f'{your} {name}'

    print(f'Hello {your_name()}!')

greeting('Jeff', 'Gates')