#LAB 3 THAT ACTUALLY WORKS
import math

class Node(object):
	# Constructor
	def __init__(self, data, next=None):
		self.data = data
		self.next = next 

class SortedList(object):
	#Constructor
	def __init__(self,head = None,tail = None):
		self.head = head
		self.tail = tail

	def PrintList(self): #WORKS
		start = self.head
		while start is not None:
			print(start.data, end = " ")
			start = start.next
		return

	def Insert(self, i): #descending order bruh
		if self.head is None:
			self.head.next = Node(i)
			return self.head
		else:
			start = self.head
			while start.next is not None:
				if start.data < i:
					#INSERT NODE(I) INTO
					start.next = Node(i)
				start = start.next
			return start

	def Delete(self, i):
		curr = self.head
		tmp = curr
		if curr is not None:
			if curr.data == i:
				curr = curr.next
			else:
				while curr.next is not None and curr.data != i:
					tmp = curr
					curr = curr.next
				tmp.next = curr.next
			return #nothing

	def Merge(self, M):
		return

	def IndexOf(self, i): #WORKS
			start = self.head
			index = 0
			if start.data == i:
				return index
			else:
				while start.next is not None:
					start = start.next
					index = index + 1
					if i == start.data:
						return index 				
				return -1

	def Clear(self): #WORKS
		if self.head is not None:
			self.head = None
		return self.head

	def Min(self): #WORKS
		start = self.head
		minimum = start.data
		while start.next is not None:
			if minimum > start.next.data:
				minimum = start.next.data
			start = start.next
		return minimum

	def Max(self): #WORKS
		start = self.head
		maximum = start.data
		while start.next is not None:
			if maximum < start.next.data:
				maximum = start.next.data
			start = start.next
		return maximum

	def HasDups(self): #WORKS :p
		if self.head is not None: #NO COUNTER NEEDED
			start = self.head
			while start.next.next is not None:
				if start.data == start.next.data:
					return True
				start = start.next
		return False

	def Select(self,k): #WORKS
		#if self.head is not None: #create counter for size of list
			start = self.head
			count = 0
			while start is not None:
				start = start.next
				count = count + 1
			lenL = count
			if k > lenL or k < 0:
				return math.inf
			else:
				start = self.head
				count = 0
				while start.next is not None and count != k:
					start = start.next
					count = count + 1
				return start.data
            
def main():
	L1 = SortedList()
	L2 = SortedList()
	L3 = SortedList()

	L1.head = Node(2)
	a = Node(3)
	b = Node(5)
	c = Node(9)
	L1.head.next = a
	a.next = b
	b.next = c

	L2.head = Node(3)
	d = Node(6)
	e = Node(9)
	f = Node(50)
	g = Node(99)
	h = Node(110)
	L2.head.next = d
	d.next = e
	e.next = f
	f.next = g
	g.next = h

	L3.head = Node(0)
	i = Node(9)
	j = Node(31)
	k = Node(31)
	l = Node(55)
	m = Node(67)
	n = Node(73)
	o = Node(92)
	p = Node(111)
	L3.head.next = i
	i.next = j
	j.next = k
	k.next = l
	l.next = m
	m.next = n
	n.next = o
	o.next = p

	print("L1: ", end="")
	L1.PrintList()
	print("\nL2: ", end="")
	L2.PrintList()
	print("\nL3: ", end="")
	L3.PrintList()
	#Insert()
	#Insert()
	#print("Lists after insertions: ")
	#print("L1: ", end="")
	#L1.PrintList()
	#print("L2: ", end="")
	#L2.PrintList()
	#print("L3: ", end="")
	#L3.PrintList()
	#print(L1.Delete(3))
	#print(L1.Delete(0))
	#print(L2.Delete(50))
	#print(L2.Delete(110))
	#print(L3.Delete(5))
	#print(L3.Delete(67))		
	#print("Lists after deletions: ")
	#print("L1: ", end="")
	#L1.PrintList()
	#print("L2: ", end="")
	#L2.PrintList()
	#print("L3: ", end="")
	#L3.PrintList()
	print("\nL1 Index of 5: ",L1.IndexOf(5)) #2
	print("L1 Index of 6: ",L1.IndexOf(6)) #DNE
	print("L2 Index of 50: ",L2.IndexOf(50)) #3
	print("L2 Index of 3: ",L2.IndexOf(3)) #0
	print("L3 Index of 111: ",L3.IndexOf(111)) #8
	print("L3 Index of 9: ",L3.IndexOf(9)) #1
	print("\nMIN for L1 is:",L1.Min())
	print("MAX for L1 is:",L1.Max())
	print("MIN for L2 is:",L2.Min())
	print("MAX for L2 is:",L2.Max())
	print("MIN for L3 is:",L3.Min())
	print("MAX for L3 is:",L3.Max())
	print("\nDuplicates in L1?:",L1.HasDups()) #FALSE
	print("Duplicates in L2?:",L2.HasDups()) #FALSE
	print("Duplicates in L3?:",L3.HasDups()) #TRUE
	print("\nL1 Select 1st: ",L1.Select(1)) #3
	print("L2 Select 5th: ",L2.Select(5)) #110
	print("L3 Select 3rd: ",L3.Select(3)) #31
	#print(L1.Clear())	
	#print(L2.Clear())
	#print(L3.Clear())

main()