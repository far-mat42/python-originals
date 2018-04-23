# Name:          Farris Matar
# Date:          April 4, 2017
# Class:         ICS3U1-03
# Description:   Assignment 2, working with 2 equations of lines.

# Getting the equation from the user.
equation1 = input("Enter the first equation in y-intercept form (no spaces): ")
equation2 = input("Enter the second equation in y-intercept form (no spaces): ")

# Determining the slope and y-intercept for equation 1.
# Checking any special cases for the equation.
if equation1 == "y=x":
    slope1 = 1
    yIntercept1 = 0
elif equation1 == "y=-x":
    slope1 = -1
    yIntercept1 = 0
elif equation1.count('+') == 0 and equation1[3:].count('-') == 0 and equation1.count('x') == 0:
    slope1 = 0
    limit1 = equation1.find('=')
    yIntercept1 = equation1[limit1+1:]
elif equation1.count('x') == 1 and equation1[3:].count('-') == 0 and equation1[3:].count('+') == 0:
    yIntercept1 = 0
    xLimit1 = equation1.find('x')
    limit1 = equation1.find('=')
    slope1 = equation1[limit1+1:xLimit1]
# Finding the values normally.
else:
    limit1 = equation1.find('=')
    xLimit1 = equation1.find('x')
    bLimit1 = equation1.find('+')
    slope1 = equation1[limit1+1:xLimit1]
    if "y=x" in equation1:
        slope1 = 1
    elif "y=-x" in equation1:
        slope1 = -1        
    if equation1.count('+') == 0:
        if equation1[xLimit1:].count('-') == 1:
            yIntercept1 = equation1[xLimit1+1:]
    else:
        yIntercept1 = equation1[bLimit1+1:]

# Doing the same thing for equation 2.
if equation2 == "y=x":
    slope2 = 1
    yIntercept2 = 0
elif equation2 == "y=-x":
    slope2 = -1
    yIntercept2 = 0
elif equation2.count('+') == 0 and equation2[3:].count('-') == 0 and equation2.count('x') == 0:
    slope2 = 0
    limit2 = equation2.find('=')
    yIntercept2 = equation2[limit2+1:]
elif equation2.count('x') == 1 and equation2[3:].count('-') == 0 and equation2[3:].count('+') == 0:
    yIntercept2 = 0
    xLimit2 = equation2.find('x')
    limit2 = equation2.find('=')
    slope2 = equation2[limit2+1:xLimit2]
else:
    limit2 = equation2.find('=')
    xLimit2 = equation2.find('x')
    bLimit2 = equation2.find('+')
    slope2 = equation2[limit2+1:xLimit2]
    if "y=x" in equation2:
        slope2 = 1
    elif "y=-x" in equation2:
        slope2 = -1
    if equation2.count('+') == 0:
        if equation2[xLimit2:].count('-') == 1:
            yIntercept2 = equation2[xLimit2+1:]
    else:
        yIntercept2 = equation2[bLimit2+1:]
    

# Making a function to find the point of intersection.
def findPOI1(slope1, yIntercept1, slope2, yIntercept2):
    newSlope = slope1 - slope2
    newIntercept = yIntercept1 - yIntercept2
    poiX = (newIntercept*-1)/newSlope
    poiY = (poiX*slope1 + yIntercept1)
    if poiX == -0:
        poiX = poiX*-1
    if poiY == -0:
        poiY = poiY*-1
    print("The point of intersection is at (%1.2f, %1.2f)." % (poiX,poiY))
    if poiX > 0 and poiY > 0:
        print("The point of intersection is in quadrant 1.")
    elif poiX < 0 and poiY > 0:
        print("The point of intersection is in quadrant 2.")
    elif poiX < 0 and poiY < 0:
        print("The point of intersection is in quadrant 3.")
    elif poiX > 0 and poiY < 0:
        print("The point of intersection is in quadrant 4.")
    elif poiX == 0 and poiY > 0:
        print("The point of intersection is between quardrants 1 and 2.")
    elif poiX == 0 and poiY < 0:
        print("The point of intersection is between quardrants 3 and 4.")
    elif poiX > 0 and poiY == 0:
        print("The point of intersection is between quardrants 1 and 4.")
    elif poiX < 0 and poiY == 0:
        print("The point of intersection is between quardrants 2 and 3.")
    elif poiX == 0 and poiY == 0:
        print("The point of intersection at the origin.")

# Determining if lines are parallel, the same line or different, and printing
# the result.
if slope1 == slope2 and yIntercept1 != yIntercept2:
    print("The two lines are parallel and will never intersect.")
elif equation1 == equation2:
    print("The two lines are exactly the same and intersect infinitely.")
else:
    findPOI1(float(slope1),float(yIntercept1),float(slope2),float(yIntercept2))