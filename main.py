# Farming Calculator by fevo (c) 2023
# Data scraped from discord.gg/thelostnemo

# General equation -> https://ibb.co/QvMS7DH

n = int(input('Type no. cycle count: '))
x = int(input('Type no. seeds: '))

#y = x * ( Y ** n )

print(' ')
print('After ' + str(round(n, )) + ' cycle count(s),')

#def blueblockEqn():
#    Y = 1.182
#    y = x * (Y ** n)
#    print('- Blue Block Seed: ' + str(round(y, )))
#blueblockEqn()

def pepperEqn():
    Y = ( 1087 / 1000 )
    y = x * (Y ** n)
    print('- Pepper Tree Seed: ' + str(round(y, )))
pepperEqn()

def lgridEqn():
    Y = ( 1066 / 1000 )
    y = x * (Y ** n)
    print('- Laser Grid Seed: ' + str(round(y, )))
lgridEqn()

def pinballEqn():
    Y = ( 1078 / 1000 )
    y = x * (Y ** n)
    print('- Pinball Bumper Seed: ' + str(round(y, )))
pinballEqn()