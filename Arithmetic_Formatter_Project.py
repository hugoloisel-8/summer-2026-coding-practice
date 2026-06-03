def arithmetic_arranger(problems, show_answers=True):
    # Lists to store each formatted part of the arithmetic problems
    list_top = []       # first line (first number)
    list_middle = []    # second line (operator + second number)
    dash_line = []      # separator line (dashes)
    list_results = []   # results (optional)

    # Check if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Loop through each arithmetic problem
    for p in problems:
        first, operator, second = p.split()

        # Check if the operator is valid (+ or - only)
        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."  

        # Check if numbers exceed 4 digits
        if len(second) > 4 or len(first) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Check if inputs are only digits
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'          

        # Determine width needed for proper alignment
        width = max(len(first), len(second)) + 2

        # Format top line (right-aligned first number)
        list_top.append(" " * (width - len(first)) + first)

        # Format middle line (operator + right-aligned second number)
        list_middle.append(
            operator + " " + " " * (width - len(second) - 2) + second
        )

        # Create dash line
        dash_line.append("-" * width)

        # Compute result
        if operator == '+':
            result = int(first) + int(second)
        else:
            result = int(first) - int(second)

        # Format result (right-aligned)
        list_results.append(" " * (width - len(str(result))) + str(result))

    # Build final arranged string
    arranged = "    ".join(list_top) + "\n"

    arranged += "    ".join(list_middle) + "\n"

    arranged += "    ".join(dash_line)

    # Add results if requested
    if show_answers:
        arranged += "\n" + "    ".join(list_results)

    return arranged


# Example test
print(f'\n{arithmetic_arranger(["132 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
