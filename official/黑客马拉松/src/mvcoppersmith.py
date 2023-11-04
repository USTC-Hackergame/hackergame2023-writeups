from sage.all import *

def coppersmith_monomials(f, mult=1, extras=[]):
	"""
	Return a list of monomials to be included as columns in the coppersmith lattice
	f: multivariate polynomial over ZZ
	mult: multiplicity
	extras: list of extra monomials to include with the highest power of f. Result may be incorrect if anything in the list isn't a monomial.
	"""
	if extras is None: extras = []
	# replace all coefficients with +1 so that there won't be any cancellation
	g = sum(f.monomials())
	gk = g**mult
	gkextra = (1+sum(extras)) * gk
	#return gkextra.monomials() # to use only these monomials -- need to edit poly-for to be sure other monomials aren't introduced
	## Alternatively, add missing monomials here:
	monomials = set(gkextra.monomials())
	more_extras = {
		mono
		for m in monomials
		for mono in poly_for(f, m, mult, extras=monomials, want_monomials=True)
	} - monomials
	while more_extras:
		monomials |= more_extras
		more_extras = {
			mono
			for m in more_extras
			for mono in poly_for(f, m, mult, want_monomials=True)
		} - monomials
	return sorted(list(monomials))[::-1]

def poly_for(f, m, mult=1, extras=None, want_monomials=False):
	"""
	Returns the polynomial (or maybe a tuple (power of f, power of N, extra terms) that goes in the coppersmith lattice with leading term m
	"""
	j = 0
	l = f.lm() # leading monomial
	for i in range(mult,0,-1):
		if (l**i).divides(m):
			## To avoid introducing any new monomials:
			#if extras and (m // (l**i)) not in extras:
			#	#print(f"rejecting {m // (l**j)}")
			#	continue
			j = i
			break
	assert (l**j).divides(m)
	extra = m // (l**j)
	# The polynomial is f**j * extra * N**(mult-j)
	assert ((f**j)*extra).lm() == m
	if want_monomials: return (f**j * extra).monomials()
	return (j, mult-j, extra)

def coppersmith_params(f, mult=1, extras=[]):
	ms = coppersmith_monomials(f, mult, extras)
	#print(ms)

	det_powN = 0
	det_powB = 0
	for m in ms:
		powf, powN, extra = poly_for(f, m, mult, extras=extras)
		assert f.lm()**powf * extra == m
		#basis[i] = f**powf * N**powN * extra
		#print(f"{m}: N**{powN} f**{powf} {extra}")
		det_powN += powN
		det_powB += m.total_degree()
	dim = len(ms)
	print(f"determinant = p**{det_powN} B**{det_powB}")
	# Condition for coppersmith to succeed:
	# (1.03**dim) * (N**powN * B**powB)^(1/dim) < N**mult
	# or equivalently: 1.03**(dim^2) * N**powN * B**powB < N**(mult*dim)
	# ===> 1.03**(dim^2 / (mult*dim - powN)) *  B**(powB / (mult*dim - powN)) < N
	expB = float(det_powB / (mult*dim - det_powN))
	print(f"1.03**{dim**2} B**{det_powB} N**{det_powN} < N**{dim*mult}")
	print("2**{logconst:.4f} B**{expB:.2f} < N".format(
		logconst=float(log(1.03,2)*(dim**2 / (mult*dim - det_powN))),
		expB=expB
	))
	print("dimension", dim)
	return (expB, dim)

def quick_params(nvars, mult, extras=None):
	global xs
	if isinstance(nvars, (int, Integer)): xs = polygens(ZZ, 'x', nvars)
	else: xs = nvars
	f = prod((xi + 1) for xi in xs[:len(xs)//2]) + prod((xi + 1) for xi in xs[len(xs)//2:])

	if extras is None:
		extras = [prod(xs[:len(xs)//2])**i for i in range(1,mult)]
	return coppersmith_params(f, mult, extras=extras)

def coppersmith_makelattice(f, B, N, mult=1, extras=[]):
	if extras is None: extras = []
	ms = coppersmith_monomials(f,mult,extras)
	M = matrix(ZZ, len(ms), len(ms), sparse=True)
	scalefactors = [B**m.total_degree() for m in ms]
	for row,m in enumerate(ms):
		# make the polynomial that has this monomial as a leading term
		powf, powN, extra = poly_for(f, m, mult, extras=extras)
		rowpoly = f**powf * extra * N**powN
		assert set(ms).issuperset(rowpoly.monomials())
		for col in range(len(ms)):
			M[row,col] = rowpoly.monomial_coefficient(ms[col]) * scalefactors[col]
	return M, ms, scalefactors

def vec_to_poly(vec, ms, scalefactors):
	if not all(c % s == 0 for (c,s) in zip(vec,scalefactors)):
		raise ValueError("vec not divisible by scalefactors")
	return sum(m*Integer(c//s) for (m,c,s) in zip(ms,vec,scalefactors))

def export_lattice(M, filename, reorder=True):
	if reorder:
		M = M[::-1,::-1]
	with open(filename, 'x') as f:
		f.write("[");
		for row in M:
			f.write("[")
			for elem in row:
				f.write(elem.str())
				f.write(" ")
			f.write("]\n")
		f.write("]\n")
		f.flush()
def import_lattice(filename, reorder=True):
	with open(filename, 'r') as f:
		M = matrix([
			[Integer(x) for x in line.strip().strip("[]").strip().split()]
			for line in f
			if line.strip("[]").strip()
		])
	if reorder:
		M = M[:,::-1]
	return M
