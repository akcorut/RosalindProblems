import random
# 1 - probability of getting no dominant alleles
def mendelFirst(k,m,n):
    tot = k+m+n
    return 1 - (n/tot)*((n-1)/(tot-1)) - (n/tot)*(m/(tot-1)) - (m/tot)*((m-1)/(tot-1))*0.25

print(mendelFirst(30,29,15))