# Number of disks in the puzzle
NUMBER_OF_DISKS = 5

# Initialize the three rods
# A starts with all disks in descending order
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []


def move(n, source, auxiliary, target):
    """
    Recursively solve the Tower of Hanoi problem.

    Args:
        n (int): number of disks to move
        source (list): starting rod
        auxiliary (list): temporary rod
        target (list): destination rod
    """

    # Base case: no disks to move
    if n <= 0:
        return

    # Move the top n-1 disks from source to auxiliary
    move(n - 1, source, target, auxiliary)

    # Move the largest remaining disk from source to target
    target.append(source.pop())

    # Display the current state of the rods
    print(A, B, C, '\n')

    # Move the n-1 disks from auxiliary to target
    move(n - 1, auxiliary, source, target)


# Start the recursive solution:
# Move all disks from rod A to rod C using rod B as auxiliary storage
move(NUMBER_OF_DISKS, A, B, C)
