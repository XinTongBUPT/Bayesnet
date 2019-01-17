import copy

def ask(var, value, e, bn):
	dist = []
	for x in [False, True]:
		# make a copy of the evidence set
		# extend e with value of X
		e[var] = x
		# enumerate
		dist.append(EnumerateAll(bn.variable_names, e,bn))
	# normalize & return
	return dist[value] / sum(dist)

def EnumerateAll(variables,e,bn):
	if len(variables) == 0:
		return 1.0
	Y = variables[0]
	node = bn.get_var(Y)
	if Y in e:
		res = node.probability(e[Y], e) * EnumerateAll(variables[1:], e,bn)
	else:
		probs = []
		e2 = e.copy()
		for y in [True, False]:
			e2[Y] = y
			probs.append(node.probability(y,e2) * EnumerateAll(variables[1:], e2,bn))
		res = sum(probs)
	return res
