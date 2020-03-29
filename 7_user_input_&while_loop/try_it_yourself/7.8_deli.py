"""
Problem:
Make a list called sandwich_orders and fill it with the names of various 
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made 
your tuna sandwich. As each sandwich is made, move it to the list of 
finished_sandwiches. After all the sandwiches have been made, print a message 
listing each sandwich that was made.
"""
sandwich_orders = ['grilled', 'tortas', 'panini', 'club', 'cuban', 'tuna']
finished_sandwiches = []
while sandwich_orders:
    sandwitch = sandwich_orders.pop()
    print("I made your "+ sandwitch.title() +" sandwitch.")
    finished_sandwiches.append(sandwitch)
print("--- List of finished sandwitch ---")
for sandwitch in finished_sandwiches:
    print("\t> "+ sandwitch.title() +" Sandwitch")