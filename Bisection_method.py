def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Computes the square root of a number using the bisection method.
    This method repeatedly narrows down an interval where the square root lies.
    """

    # Square root of negative numbers is not defined in real numbers
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Handle simple known cases directly
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')

    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Define the search interval
        low = 0
        high = max(1, square_target)

        root = None  # Will store the result if convergence is reached

        # Bisection loop
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid ** 2

            # Check if we are close enough to the target
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            # If mid² is too small, move the lower bound up
            elif square_mid < square_target:
                low = mid

            # If mid² is too large, move the upper bound down
            else:
                high = mid

        # If we did not converge within max iterations
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')

    return root


# Example usage
N = 14.232
square_root_bisection(N)
