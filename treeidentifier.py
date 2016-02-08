print "We're going to ask some questions to help identify your tree by the leaves!"


#question 1. goes to 2 or 12
print """Are the leaves: 
1. Needle or scale-like
2. Board and flat"""
stepOne = raw_input()

# question 2 - 3 or 4
if stepOne == "1":
    print "Are the leaves 1. scale-like or 2. needle-like"
    stepTwoA = raw_input()
# question 12 - 13 or 18
elif stepOne == "2":
    print "1. Leaves opposite or whorled on stem /n 2. Leaves alternate on stem"
    stepTwoB = raw_input()
# question 3, if 2 = 1
if stepTwoA == "1":
    print """Are the scales:
     1. pointed, twigs not flat
     2. blunt, twigs flat"""
    twigsAnswer = raw_input()
# question 4 if 2 = 2
elif stepTwoA == "2":
    print """ are the needles:
    1. single on twigs
    2. in bundles, tufts, or rosettes """
    groupAnswer = raw_input()
#results from question 3
if stepTwoA == "1" and twigsAnswer == "1":
    print "You have a red-cedar"
if stepTwoA == "1" and twigsAnswer == "2":
    print " You have a white- cedar"
#question 5
if groupAnswer == "1": 
    print """ Are the needles:
    1. flat, blunt
    2. four-sided and sharp-pointed """
    dimensionAnswer = raw_input()
#stalkAnswer = raw_input()

if dimensionAnswer == "2":
    print " you have a spruce"
elif dimensionAnswer == "1":
    print "Do the needles have 1. small stalks or 2. no stalks "
    stalkAnswer = raw_input()

if stalkAnswer == "1":
    print "you have a hemlock"
if stalkAnswer == "2":
    print "you have a fir"
    
#question 7 
elif groupAnswer == "2":
    print """ Are the needles
    1. in bundles with sheaths at base
    2. in tufts or rosettes"""
    collectionAnswer = raw_input()

if groupAnswer == "1" and dimensionAnswer == "2":
    print "you have a spruce!"

#question 8 
if dimensionAnswer == "1":
    print """ Do you have needles:
    1. in bundles of 5
    2. not in bundles of 5 """
    bundleAnswer = raw_input()

if bundleAnswer == "1":
    print " you have a white pine!"
#question 9
elif bundleAnswer == "2":
    print """ Are the needles in bunches of:
    1. 3
    2. 2 """
    bunchesAnswer = raw_input()

if bunchesAnswer == "1":
    print "you have a pitch pine!"
elif bunchesAnswer == "2":
    #question 10
    print """are the needles:
    1. 4 inches long
    2. 1.5 to 3 inches long"""
    lengthAnswer = raw_input()

if lengthAnswer == "2":
    print " you have a virginia pine"
elif lengthAnswer == "1":
    print """ are the needles:
    1. sharp-pointed and flexible
    2. stiff, snap apart when bent """
    consistancyAnswer = raw_input()

if consistancyAnswer == "1":
    print " you have an Austrian pine"
if consistancyAnswer == "2":
    print " you have a red pine"

#question 12
if stepTwoB == "1":
    #question 13
    print """ are the leaves:
    1. opposite on stem
    2. whroled on stem """
    arrangementAnswer = raw_input()
elif stepTwoB == "2":
    #question 18
    print " Are the leaves 1. simple or 2. compound"
    complexityAnswer = raw_input()

#if complexityAnswer == "1":
    #question 19
#elif complexityAnswer == "2":
    #question 39
    
if arrangementAnswer == "2":
    print " you hve a catalpa"
elif arrangementAnswer == "1":
    # question 14
    print "Are the leaves 1. simple or 2. compound"
    complexityTwoAnswer = raw_input()

if complexityTwoAnswer == "1":
    #question 15
    print "Are the margins 1. entire 2. lobed"
    marginsAnswer = raw_input()
elif complexityTwoAnswer == "2":
    print "are the leaves 1. pinnately compound or 2. palamately compound"
    pCompoundAnswer = raw_input()

if marginsAnswer == "1":
    print " you have a dogwood"
elif marginsAnswer == "2":
    print " you have a maple"
    
if pCompoundAnswer == "2":
    print " you have a horse chestnut"
elif pCompoundAnswer == "1":
    #question 17
    print """ is your leaf divided into: 
    1. 3 to 5 leaflets
    2. 7 leaflets """
    leafDivideAnswer = raw_input()

if leafDivideAnswer == "1":
    print "you have a box-elder"
elif leafDivideAnswer == "2":
    print " you have an ash"
