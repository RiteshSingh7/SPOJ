# PPATH - Prime Path

from collections import deque

arr = [1 for _ in range(10000)]
for i in range(2, 100):
	if arr[i] == 1:
		j = 2
		while i*j < 10000:
			arr[i*j] = 0
			j += 1
prime = [i for i in range(10000) if arr[i] == 1 and i > 999]

def adj(x, y):
	match = 0
	for _ in range(4):
		if x%10 == y%10:
			match += 1
		x //= 10
		y //= 10
	return True if match == 3 else False

graph = dict()
for num in prime:
	graph[num] = []
for i in range(len(prime)):
	for j in range(i+1, len(prime)):
		if adj(prime[i], prime[j]):
			graph[prime[i]].append(prime[j])
			graph[prime[j]].append(prime[i])

result = []
t = int(input())
for _ in range(t):
	x,y = map(int, input().split())
	if x == y:
		result.append(0)
		continue
	q = deque([x])
	level = deque([0])
	seen = set([x])
	while q:
		vertex = q.popleft()
		curr = level.popleft()
		if vertex == y:
			result.append(curr)
			break
		for node in graph[vertex]:
			if node not in seen:
				seen.add(node)
				q.append(node)
				level.append(curr+1)
	if y not in seen:
		result.append('Impossible')

for ans in result:
	print(ans)
