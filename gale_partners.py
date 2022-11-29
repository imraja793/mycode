# Employee.objects.filter(domain__name="Technology", location__org__org_name="Gale")
#
# Employee.objects.filter(domain_name__in=['Technology', "QA"], name__="raja")

a = [7,6,5,4,3,1]
mini = min(a)
i = a.index(mini)
if i < len(a)-1:
    sli = a[i+1:]
    maxa = max(sli)
    if maxa > mini:
        print(maxa - mini)
    else:
        print('no profit')
print('not possible')
