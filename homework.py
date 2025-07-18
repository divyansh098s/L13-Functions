import math

def circle_circumference(radius):
  """
  Calculates the circumference of a circle given its radius.

  Args:
    radius: The radius of the circle (a number).

  Returns:
    The circumference of the circle.
  """
  return 2 * math.pi * radius


radius = float(input("Enter the radius of the circle: "))


circumference = circle_circumference(radius)


print(f"The circumference of the circle is: {circumference}")