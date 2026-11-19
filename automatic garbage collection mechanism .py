import gc
import time
import sys

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Enable garbage collection
gc.enable()

# Create circular references
class Demo:
    def __init__(self):
        self.data = "Garbage Collection Example"

# Create objects
print("\nCreating Objects...")

a = Demo()
b = Demo()

# Create circular references
a.ref = b
b.ref = a

print("Objects Created")

# Display reference count
print("\nReference Count of a:", sys.getrefcount(a))

# Delete references
del a
del b

print("\nObjects Deleted")

# Check garbage collector count
print("Garbage Collector Count:", gc.get_count())

# Measure time before garbage collection
start = time.time()

# Manually run garbage collection
collected = gc.collect()

end = time.time()

print("\nManual Garbage Collection")
print("Objects Collected:", collected)
print("Time Taken:", end - start, "seconds")

# Display garbage collection statistics
print("\nGarbage Collection Statistics:")
print(gc.get_stats())

print("\nProgram Completed")
