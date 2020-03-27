# Empty list
aliens = []

# Making 30 green alien having point 5
for i in range(30):
    new_alien = {
        'color': 'green',
        'point': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

# Changing first 5 alien property
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['point'] = 10
        alien['speed'] = 'fast'

print("Total Numbers of alien : "+ str(len(aliens)))

print("All alien:")
for alien in aliens:
    print(alien)