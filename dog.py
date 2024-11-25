# Create a child class inheriting from Animal
with open('Dog.py', 'w') as f:
    f.write("""from Animal import Animal

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "The dog runs."
""")

import subprocess

try:
    subprocess.run(['git', 'add', 'Dog.py'], check=True)

    subprocess.run(['git', 'commit', '-m', 'Added Dog class inheriting from Animal'], check=True)

    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    
    print("Child class created and pushed to fork successfully.")
except subprocess.CalledProcessError as e:
    print("Error executing git commands:", str(e))
