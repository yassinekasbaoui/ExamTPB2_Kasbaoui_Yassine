def produit (T):
	S=0
	for t in T:
		S*=t
		return S

Data = [1, 3, 5]
Prod = math.prod (Data)
if Data :
	print ('le produit est:', Prod (Data))
	print ('le min est:', min (Data))
	print ('le max est:', max (Data))
else :
	print ('dossier vide')
