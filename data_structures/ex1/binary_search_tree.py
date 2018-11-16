class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  #Doing Breadth First for MVP
  def breadth_first_for_each(self, cb):
    #easy way to make a queue, thanks python
    queue = []
    #Adding stuff to the queue
    queue.append(self)
    #Go through the queue and use the cb function
    while len(queue) > 0:
      #grab first item in queue
      i = queue[0]
      #call cb
      cb(i.value)
      #take out the first item
      queue.pop(0)
      #check left node, if existing add it to the queue
      if i.left is not None:
        queue.append(i.left)
      #check right node, if existing add it to the queue
      if i.right is not None:
        queue.append(i.right)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
