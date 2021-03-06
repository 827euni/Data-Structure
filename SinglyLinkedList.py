class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
		
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		new_node = Node(key)
		new_node.next = self.head
		self.head = new_node
		self.size+=1
		
	def pushBack(self, key):
		v = Node(key)
		if len(self) == 0:
			self.head = v
		else:
			tail = self.head
			while tail.next != None:
				tail = tail.next
			tail.next = v
		self.size += 1
		
	def popFront(self): 
		if len(self) == 0:
			return None
		else:
			x=self.head
			key = x.key
			self.head = x.next
			self.size -= 1
			return key
		
	def popBack(self):
		if len(self) == 0:
			return None
		else:
			prev, tail = None, self.head
			while tail.next != None:
				prev=tail
				tail = tail.next
			if len(self) == 1:
				self.head = None
			else:
				prev.next = None
			key = tail.key
			del tail
			self.size -= 1
			return key
		
	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head
		while v!=None:
			if v.key == key:
				return v
			v=v.next
		return None 
	
	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!
		k = self.head
		
		if k == None:
			return False
		
		if k == x:
			t = self.head
			self.head = self.head.next
			del t
			return True
		
		while k.next != None:
			if k.next == x:
				t = k.next
				k.next = k.next.next
				del t
				return True
			k = k.next
		return False
	
	def reverse(self, key):
	
		k = self.head
		prev = None
		right = None
		if k == None:
			return 
		while k.key != key:
			prev = k
			k = k.next
		while k != None:
			left = right
			right = Node(k.key)
			right.next = left
			k = k.next		
		if prev == None:
			self.head = right
		else:
			prev.next = right


		
		
	def findMax(self):
		# self가 empty이면 None, 아니면 max key 리턴
		k = self.head
		if len(self)==0:
			return None
		else:
			mx = self.head.key
			while(k != None):
				if mx<k.key:
					mx = k.key
				k = k.next
		return mx
	
	def deleteMax(self):
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		if len(self) == 0:
			return None
		else:
			k = self.findMax()
			maxx = self.search(k)
			self.remove(maxx)
		return maxx
	
	def selectidx(self,idx):
		if self.size < idx:
			return 
		node = self.head
		cnt = 0
		while cnt < idx:
			node = node.next
			cnt += 1 
		return node
	
	def insert(self, k, val):
		if k == 0:
			self.head = Node(self.head, val)
			self.size += 1
		v = self.selectidx(k-1)
		if k >= self.size:
			self.pushBack(val) 
		else:
			new = Node(val)
			s = v.next
			v.next = new
			new.next = s
			self.size +=1
		
			
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")