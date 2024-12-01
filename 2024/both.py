from aochelpers import read

a,b=zip(*[map(int,i.split())for i in read("..").split('\n')])
print(sum(abs(i-j)for i,j in zip(sorted(a),sorted(b))),sum(b.count(i)*i for i in a))