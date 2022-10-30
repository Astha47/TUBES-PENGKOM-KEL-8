from time import sleep
def Loading(index, total, prefix='', length = ''):
    percent = ('{0:.' + str(0) + 'f}').format(100*(index/float(total)))
    print(f'\r{prefix} {percent}%', end='\r')
    if index == total:
        print()

items = list(range(0,50))
l = len(items)

Loading(0, l , prefix = 'Loading:', length=l)
for i, item in enumerate(items):
    sleep(0.03)
    Loading(i + 1, l, prefix='Loading:', length = l)
