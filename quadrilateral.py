#algorithm that will help sort out
#whether a quadrilateral is a square, rhombus,
#parallelogram, rectangle, kite, trapezium,
#arrowhead or just quadrilateral, by asking a series
#of yes/no questions.

no_sides = 4

if no_sides == 4:
	print("We know this is a parallelogram\n")
	if all_sides_equal == True:
		print("All sides are equal\n")
		if all_angles_right == True:
			print("This is a SQUARE!")
		else: 
			print("This is a RHOMBUS!")
	else:
		print("All sides are not equal\n")
	if all_angles_right == True:
		print("This is a RECTANGLE!")
	else:
		print("All angles are not right angles, continue\n")
	if more_one_parallel_side == True:
		print("This is a PARALLELOGRAM!")
	else:
		print("No more than one parallel side..")
	if two_pairs_equal_sides_adjacent == True:
		print("This is a KITE!")
	else:
		print("No 2 pairs of equal length that are adjacent..")
	if one_pair_parallel_sides == True:
		print("This is a TRAPEZIUM!")
	else:
		print("This is an ARROWHEAD!")
else: 
	print("This is not a quadrilateral!")
	