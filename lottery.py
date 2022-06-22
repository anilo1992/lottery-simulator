import random
import math

lottopreis = 1.2
count = 0

print('Berechnung läuft...')

while True:
    count += 1
    lottozahlen = sorted(random.sample(range(1, 50), 6))
    lottotipp = sorted(random.sample(range(1, 50), 6))
    if lottotipp == lottozahlen:
        print('Du müsstest ' + str(count) + 'x Lotto spielen, um zu gewinnen. Die Ausgaben für ' + str(count) + ' Lottoscheine betragen: ' + str(math.ceil(lottopreis*count)) + '€')
        break
