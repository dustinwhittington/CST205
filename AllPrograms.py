def getPic():
  return makePicture(pickAFile())

def moreRed(percent):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r*(percent * .01 + 1))
  repaint(pic)
  return pic

def roseColoredGlasses():
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    setGreen(p, getGreen(p) / 2)
    setBlue(p, getBlue(p) / 2)
  return pic
  
def makeNegative():
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    setRed(p, 255 - getRed(p))
    setBlue(p, 255 - getBlue(p))
    setGreen(p, 255 - getGreen(p))
  return pic
  
def lightenUp():
  pic = getPic()
  pixels = getPixels(pic)  
  for p in pixels:
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p, newColor)
  repaint(pic)
  return pic
  
def BnW():
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l = (r+g+b)/3
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l)
  repaint(pic)
  return pic
  
def betterBnW():
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l = (r*0.299 + g*0.587 + b*0.114)
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l)
  repaint(pic)
  return pic
 

def pyCopy(source, target, targetX, targetY):
  startY = targetY
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      color = getColor(getPixel(source, x, y))
      setColor(getPixel(target, targetX, targetY), color)
      targetY += 1
    targetX += 1
    targetY = startY 
  return target
  
def vertical_mirror(pic):
  for x in range(0, getWidth(pic)/2):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, getWidth(pic) - (x + 1), y)
      setColor(pixel2, color)
  return pic
    
def horizontal_mirror_ttb(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, x, getHeight(pic) - (y + 1))
      setColor(pixel2, color)
  return pic
  
def horizontal_mirror_btt(pic):
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      pixel = getPixel(pic, x, y)
      pixel2 = getPixel(pic, x, getHeight(pic) - (y + 1))
      color = getColor(pixel2)
      setColor(pixel, color)
  return pic
  
def quadruple_mirror(pic):
  for x in range(0, getWidth(pic)/2):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, getWidth(pic) - (x + 1), y)
      setColor(pixel2, color)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)/2):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      pixel2 = getPixel(pic, x, getHeight(pic) - (y + 1))
      setColor(pixel2, color)
  return pic

def simpleCopy(picture):
  newpic = makeEmptyPicture(getWidth(picture), getHeight(picture))
  for x in range(0, getWidth(newpic)):
    for y in range(0, getHeight(newpic)):
      setColor(getPixel(newpic, x, y,), getColor(getPixel(picture, x, y)))
  show(newpic)
  writePictureTo(newpic, "C:\\Users\\Dustin Whittington\\Documents\\Lab4\\simple_copy.jpg")
  return newpic

def rotate_pic(picture):
  newpic = makeEmptyPicture(getHeight(picture), getWidth(picture))
  for y in range(0, getHeight(picture)):
    for x in range(0, getWidth(picture)):
      color = getColor(getPixel(picture, x, y))
      setColor(getPixel(newpic, y, getWidth(picture) - (x + 1)), color)
  return newpic
    
def shrink(picture):
  newpic = makeEmptyPicture(getWidth(picture)/2 + 1, getHeight(picture)/2 + 1)
  for x in range(0, getWidth(picture), 2):
    for y in range(0, getHeight(picture), 2):
      setColor(getPixel(newpic, x/2, y/2), getColor(getPixel(picture, x, y)))
  return newpic

def doubleRed(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 2)
  return pic

  
"""This version you must define the x and y coordinates to copy each image to"""
def makeCollage():
  collage = makeEmptyPicture(1500, 2100)
  image1 = vertical_mirror(getPic())
  image2 = doubleRed(getPic())
  image3 = horizontal_mirror_ttb(getPic())
  image4 = horizontal_mirror_btt(getPic())
  image5 = quadruple_mirror(getPic())
  image6 = rotate_pic(getPic())
  image7 = shrink(getPic())
  image8 = getPic()
  image9 = getPic()
  
  pyCopy(image1, collage, 0, 0)
  pyCopy(image2, collage, 210, 0)
  pyCopy(image3, collage, 0, 1530)
  pyCopy(image4, collage, 975, 1580)
  pyCopy(image5, collage, 450, 775)
  pyCopy(image6, collage, 458, 0)
  pyCopy(image7, collage, 660, 1950)
  pyCopy(image8, collage, 0, 720)
  pyCopy(image9, collage, 1170, 875)
  return collage

  
"""This version coppies each picture to various strategic positions on the new image"""  
def makeCollage2():
  collage = makeEmptyPicture(1500, 2100)
  image1 = vertical_mirror(getPic())
  image2 = doubleRed(getPic())
  image3 = horizontal_mirror_ttb(getPic())
  image4 = horizontal_mirror_btt(getPic())
  image5 = quadruple_mirror(getPic())
  image6 = rotate_pic(getPic())
  image7 = shrink(getPic())
  image8 = getPic()
  image9 = getPic()
  
  for x in range(0, getWidth(image1)):
    for y in range(0, getHeight(image1)):
      setColor(getPixel(collage, x, y), getColor(getPixel(image1, x, y)))

  for x in range(0, getWidth(image2)):
    for y in range(0, getHeight(image2)):
      setColor(getPixel(collage, getWidth(collage) - getWidth(image2) + x, y), getColor(getPixel(image2, x, y)))
  
  for x in range(0, getWidth(image3)):
    for y in range(0, getHeight(image3)):
      setColor(getPixel(collage, x, getHeight(collage) - getHeight(image3) + y), getColor(getPixel(image3, x, y)))
  
  for x in range(0, getWidth(image4)):
    for y in range(0, getHeight(image4)):
      setColor(getPixel(collage, getWidth(collage) - getWidth(image4) + x, getHeight(collage) - getHeight(image4) + y), getColor(getPixel(image4, x, y)))
  
  for x in range(0, getWidth(image5)):
    for y in range(0, getHeight(image5)):
      setColor(getPixel(collage, x + (getWidth(collage) - getWidth(image5)) / 2, y + (getHeight(collage) - getHeight(image5)) / 2), getColor(getPixel(image5, x, y)))

  for x in range(0, getWidth(image6)):
    for y in range(0, getHeight(image6)):
      setColor(getPixel(collage, x + (getWidth(collage) - getWidth(image6)) / 2, y), getColor(getPixel(image6, x, y))) 

  for x in range(0, getWidth(image7)):
    for y in range(0, getHeight(image7)):
      setColor(getPixel(collage, x + (getWidth(collage) - getWidth(image7)) / 2, getHeight(collage) - getHeight(image7) + y), getColor(getPixel(image7, x, y)))

  for x in range(0, getWidth(image8)):
    for y in range(0, getHeight(image8)):
        setColor(getPixel(collage, x, (getHeight(collage) - getHeight(image8)) / 2 + y), getColor(getPixel(image8, x, y)))

  for x in range(0, getWidth(image9)):
    for y in range(0, getHeight(image9)):
        setColor(getPixel(collage, getWidth(collage) - getHeight(image9) + x, (getHeight(collage) - getHeight(image9)) / 2 + y), getColor(getPixel(image9, x, y)))
  return collage

def red_eye_fix(pic = None):
    if pic == None:
        pic = getPic()
    red = makeColor(250,61,79)
    dist = 121.0
    for x in range(170,212): #eye one (170,276) to (212,307)
        for y in range(276,307):
            b = getBlue(getPixel(pic,x,y))
            g = getGreen(getPixel(pic,x,y))
            if distance(red,getColor(getPixel(pic,x,y))) < dist:
                setRed(getPixel(pic,x,y),min(b,g))
    for x in range(333,364): #eye two (333,290) to (364,324)
        for y in range(290,324):
            b = getBlue(getPixel(pic,x,y))
            g = getGreen(getPixel(pic,x,y))
            if distance(red,getColor(getPixel(pic,x,y))) < dist:
                setRed(getPixel(pic,x,y),min(b,g))
    repaint(pic)
    return pic
    
def crazy_eye(pic = None):
    if pic == None:
        pic = getPic()
    red = makeColor(250,61,79)
    dist = 111.0
    for x in range(170,212): #eye one (170,276) to (212,307)
        for y in range(276,307):
            b = getBlue(getPixel(pic,x,y))
            g = getGreen(getPixel(pic,x,y))
            if distance(red,getColor(getPixel(pic,x,y))) < dist:
                setColor(getPixel(pic,x,y),makeColor(randint(0,255),randint(0,255),randint(0,255)))
    for x in range(333,364): #eye two (333,290) to (364,324)
        for y in range(290,324):
            b = getBlue(getPixel(pic,x,y))
            g = getGreen(getPixel(pic,x,y))
            if distance(red,getColor(getPixel(pic,x,y))) < dist:
                setColor(getPixel(pic,x,y),makeColor(randint(0,255),randint(0,255),randint(0,255)))
    repaint(pic)
    return pic

def bet_BnW_conv(p):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l = (r*0.299 + g*0.587 + b*0.114)
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l)

def betterBnW(pic = None):
    if pic == None:
        pic = getPic()
    pixels = getPixels(pic)
    map(bet_BnW_conv,pixels)
    return pic

def sepia_conv(p): #conversion function for sepia
    red = getRed(p)
    blue = getBlue(p)
    #I tweaked the values here. Not much, but I wanted the yellow
    #to be more pronounced
    if red < 63:
        setRed(p,int(red*1.1))
        #setBlue(p,int(blue*0.9))
        setBlue(p,int(blue*0.9))
    elif red < 62 and red < 192:
        setRed(p,int(red*1.15))
        #setBlue(p,int(blue*0.85))
        setBlue(p,int(blue*0.7))
    else: #red > 191
        if int(red*1.08) < 255:
            setRed(p,int(red*1.08))
        else:
            setRed(p,255)
        #setBlue(p,int(blue*0.93))
        setBlue(p,int(blue*0.89))

"""current red value   multiplier for red  multiplier for blue
red < 63    1.1 0.9
62 < red < 192  1.15    0.85
red > 191   1.08*   0.93"""

def sepia(pic = None):
    if pic == None:
        pic = getPic()
    pic = betterBnW(pic)
    pixels = getPixels(pic)
    map(sepia_conv,pixels) #see sepia_conv above
    repaint(pic)
    return pic
    
def colorAdjust(color):
  if color < 64:
    return(31)
  if color < 128:
    return(95)
  if color < 192:
    return(159)
  return(223)

def artify():
  pic = getPic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p, colorAdjust(r))
    setGreen(p, colorAdjust(g))
    setBlue(p, colorAdjust(b))
  repaint(pic)
  return pic
  
#greenScreen image must be smaller than background or an error is returned.
def chromakey():
  greenScreen = getPic()
  background = getPic()
  for x in range(0, getWidth(greenScreen)):
    for y in range(0, getHeight(greenScreen)):
      pixG = getPixel(greenScreen, x, y)
      pixB = getPixel(background, x, y)
      if (distance(getColor(pixG), green) < 177): #This value has to be tweaked based on green value being replaced.
        setColor(pixG, getColor(pixB))
  show(greenScreen)
  return greenScreen
  
"""Coppies non-green pixels to background image and returns background image""" 
def chromakey2():
  green_image = getPic()
  background_image = getPic()
  for x in range(0, getWidth(green_image)):
    for y in range(0, getHeight(green_image)):
      if (distance(getColor(getPixel(green_image, x, y)), green) > 195):
        setColor(getPixel(background_image, x, y), getColor(getPixel(green_image, x, y)))
  return background_image

def stPatrick():
  image1 = getPic()
  pixels = getPixels(image1)
  for p in pixels:
    setGreen(p, getGreen(p) * 1.5)
  image2 = getPic()
  for x in range(0, getWidth(image2)):
    for y in range(0, getHeight(image2)):
      if(distance(getColor(getPixel(image2,x,y)), green) < 150):
        setColor(getPixel(image1, x - 20, y + 600), getColor(getPixel(image2,x,y)))
  image3 = getPic()
  for x in range(0, getWidth(image3)):
    for y in range(0, getHeight(image3)):
      if(distance(getColor(getPixel(image3,x,y)), white) > 40):
        setColor(getPixel(image1, x + 400, y + 180), getColor(getPixel(image3,x,y)))
  image4 = shrink(getPic())
  for x in range(0, getWidth(image4)):
    for y in range(0, getHeight(image4)):
      if (distance(getColor(getPixel(image4, x, y)), white) > 20):
        setColor(getPixel(image1, x + 100, y + 15), getColor(getPixel(image4, x, y)))
  return image1

def lineDrawing():
  pic = betterBnW()
  for x in range(0, getWidth(pic) - 1):
    for y in range(0, getHeight(pic) - 1):
      currentPixel = getPixel(pic, x, y)
      rightPixel = getPixel(pic, x + 1, y)
      belowPixel = getPixel(pic, x, y + 1)
      currentColor = getColor(currentPixel)
      rightColor = getColor(rightPixel)
      belowColor = getColor(belowPixel)
      if(abs(distance(currentColor, rightColor)) > 77 and abs(distance(currentColor, belowColor)) > 77):
        setColor(currentPixel, black)
      else:
        setColor(currentPixel, white)
  repaint(pic)
  return(pic)
      
      
  
 
#writePictureTo(stPatrick(), "C:\\Users\\Dustin Whittington\\Pictures\\StPatricksDayCard\\stPatricksDay.jpg")
#writePictureTo(roseColoredGlasses(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\roseColoredGlasses.jpg")
#writePictureTo(makeNegative(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\makeNegative.jpg")    
#writePictureTo(betterBnW(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\betterBnW.jpg")   
#writePictureTo(horizontal_mirror_btt(getPic()), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\bottomToTop.jpg")
#writePictureTo(shrink(getPic()), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\shrink.jpg")  
#writePictureTo(red_eye_fix(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\redEyeFix.jpg")   
#writePictureTo(artify(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\artify.jpg")  
#writePictureTo(chromakey(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\chromakey.jpg")  
#writePictureTo(lineDrawing(), "C:\\Users\\Dustin Whittington\\Pictures\\Portfolio\\lineDrawing.jpg")

