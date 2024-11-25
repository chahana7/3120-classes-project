# Create a child class inheriting from Animal
with open('Dog.py', 'w') as f:
    f.write("""from Animal import Animal

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "The dog runs."
""")

# Simulate git operations for the forked repository
import subprocess

try:
    # Git add
    subprocess.run(['git', 'add', 'Dog.py'], check=True)
    
    # Git commit
    subprocess.run(['git', 'commit', '-m', 'Added Dog class inheriting from Animal'], check=True)
    
    # Git push
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    
    print("Child class created and pushed to fork successfully.")
except subprocess.CalledProcessError as e:
    print("Error executing git commands:", str(e))
