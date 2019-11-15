# Check if the shape is round
roundness = input('Is your shape round? ')

# If the shape IS round...
if roundness.upper() == 'Y':

    # Check if the shape is 2D or 3D
    flatness = input('Is the shape 2D (flat)? ')

    # If the shape IS 2D (flat)...
    if flatness.upper() == 'Y':

        # The shape is a circle. Tell the user
        print('The shape is a circle!')

    # If the shape is NOT 2D (not flat)
    elif flatness.upper() == 'N':

        # The shape is 3D (not flat), so it is a ball
        print('The shape is a ball')

elif roundness.upper() == 'N':

    threeSides = input('Does the shape have three sides? ')

    if threeSides.upper() == 'Y':

        print('The shape is a triangle!')

    elif threeSides.upper() == 'N':

        print('The shape is a mystery!')
