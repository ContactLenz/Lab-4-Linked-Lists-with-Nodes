class LinkedListIter:
	def __init__(self, lst):
		self.list = lst
		self.length = self.list._nodeCount
		self.start = self.list._head
		self.temp = None

	def __iter__(self):
		return self

	def __next__(self):
		if not self.start:
			raise StopIteration
		else:
			self.temp = self.start.value
			self.start = self.start.link
			return self.temp

class LinkedList:
	class _Node:
		def __init__(self, value, link = None):
			self.value = value
			self.link = link

	def __init__(self):
		self._head = None
		self._tail = None
		self._nodeCount = 0

	def addFirst(self, item):
		new = self._Node(item, self._head)
		if self._nodeCount == 0:
			self._tail = new
		self._head = new
		self._nodeCount += 1

	def addLast(self, item):
		new = self._Node(item)
		if self._nodeCount == 0:
			self._head = new
		else:
			self._tail.link = new
		self._tail = new
		self._nodeCount += 1

	def removeFirst(self):
		self._head = self._head.link
		self._nodeCount -= 1

	def append(self, other):
		if self._nodeCount == 0:
			self._head = other._head
			self._tail = other._tail
		else:
			self._tail.link = other._head
			if other._nodeCount == 0:
				self._tail.link = None
			else:
				self._tail = other._tail
		self._nodeCount += other._nodeCount
		other._head = None
		other._tail = None
		other._nodeCount = 0

	def removeLast(self):
		start = self._head
		prev = None
		self._nodeCount -= 1
		while start:
			if start.link == None:
				self._tail = prev
				prev.link = None
			prev = start
			start = start.link

	def addAt(self, i, item):
		if i == 0:
			self.addFirst(item)
		elif i == self._nodeCount:
			self.addLast(item)
		else:
			self._nodeCount += 1
			start = self._head
			prev = None
			x = 0
			while x < self._nodeCount and start:
				if x == i:
					new = self._Node(item)
					prev.link = new
					new.link = start
					break
				prev = start
				start = start.link
				x += 1

	def removeAt(self, i):
		if i == 0:
			self.removeFirst()
		elif i == self._nodeCount-1:
			self.removeLast()
		else:
			self._nodeCount -= 1
			start = self._head
			prev = None
			x = 0
			while x < self._nodeCount and start:
				if x == i:
					prev.link = start.link
					start.link = None
					break
				prev = start
				start = start.link
				x += 1

	def __str__(self):
		if self._nodeCount == 0:
			return str([])
		else:
			str1 = '['
			str2 = ']'
			start = self._head
			while start:
				if start.value != None:
					str1 += str(start.value) + ';'
				start = start.link
			return str1[:-1] + str2

	def __getitem__(self, i):
		start = self._head
		x =  0
		while x < self._nodeCount and start:
			if x == i:
				return start.value
				break
			start = start.link
			x += 1

	def __setitem__(self, i, item):
		start = self._head
		x = 0
		while x < self._nodeCount and start:
			if x == i:
				start.value = item
				break
			start = start.link
			x += 1

	def __contains__(self, item):
		start = self._head
		while start:
			if start.value == item:
				return True
				break
			start = start.link
		return False

	def __iter__(self):
		return LinkedListIter(self)

	def __len__(self):
		return self._nodeCount

LL = LinkedList()
LL.addLast(10)
LL.addLast(20)
LL.addLast(30)
LL.addLast(40)
LL.addLast(50)

print(30 in LL)
print(LL)
LL[4] = 100
print(LL)
LL.removeLast()
print(LL)
