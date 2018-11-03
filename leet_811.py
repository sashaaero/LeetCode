# https://leetcode.com/problems/subdomain-visit-count/
from collections import defaultdict


cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

data = defaultdict(int)
for cpdomain in cpdomains:
    val, domain = cpdomain.split()
    val = int(val)
    x = domain.find('.')
    while x != -1:
        data[domain] += val
        domain = domain[x + 1:]
        x = domain.find('.')

    data[domain] += val

result = [('%d %s' % (v, k)) for k, v in data.items()]
print(result)
