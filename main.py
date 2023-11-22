Class Player:
  def __init__(self, name):
    self.name = name
    self.resources = {
      'Beryllium' : 140,
      'Graphite' : 0,
      'Sand' : 0,
      'Silicon' : 0
      'Tungsten' : 0
    }
 
  def save(self)
    self.data = {
      'name' : name,
      'resources' : resources
    }
  
  def load(self)
    with open('Database.json', 'r') as file:
  