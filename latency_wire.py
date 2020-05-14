W = 25
print 'shows values for 25G '
print'Size in Kib \t One side Latency in micros'
for s in [1, 8, 16, 32, 64, 128, 256, 512, 1024]:
    print '{0} \t\t {1}'.format(s,8.192*s/W)
