# CMPT 120 Yet Another Image Processer
# Author(s): Alex Cai
# Date: November 30

import cmpt120imageProjHelper
import copy

def redFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      image[row][col][0] = pixels[row][col][0]
      image[row][col][1] = 0
      image[row][col][2] = 0
  return image

def greenFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      image[row][col][0] = 0
      image[row][col][1] = pixels[row][col][1]
      image[row][col][2] = 0
  return image


def blueFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      image[row][col][0] = 0
      image[row][col][1] = 0
      image[row][col][2] = pixels[row][col][2]
  return image

def sepiaFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      image[row][col][0] = min(255, ((r * .393) + (g * .769) + (b *.189)))
      image[row][col][1] = min(255, ((r * .349) + (g * .686) + (b *.168)))
      image[row][col][2] = min(255, ((r * .272) + (g * .534) + (b *.131)))
  return image

def warmFilterRed(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      image[row][col][1] = pixels[row][col][1]
      image[row][col][2] = pixels[row][col][2]
      if r < 64:
        image[row][col][0] = int(r / 64 * 80)
      elif r >= 64 and r < 128:
        image[row][col][0] = int((r - 64) / (128 - 64) * (160 - 80) + 80)
      else:
        image[row][col][0] = int((r - 128) / (255 - 128) * (255 - 160) + 160)
  return image

def warmFilterBlue(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      b = pixels[row][col][2]
      image[row][col][0] = pixels[row][col][0]
      image[row][col][1] = pixels[row][col][1]
      if b < 64:
        image[row][col][2] = int(b / 64 * 50)
      elif b >= 64 and b < 128:
        image[row][col][2] = int(((b - 64) / (128 - 64)) * (100 - 50) + 50)
      else:
        image[row][col][2] = int(((b - 128) / (255 - 128)) * (255 - 100) + 100)
  return image

def coldFilterBlue(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      b = pixels[row][col][2]
      image[row][col][0] = pixels[row][col][0]
      image[row][col][1] = pixels[row][col][1]
      if b < 64:
        image[row][col][2] = int(b / 64 * 80)
      elif b >= 64 and b < 128:
        image[row][col][2] = int(((b - 64) / (128 - 64)) * (160 - 80) + 80)
      else:
        image[row][col][2] = int(((b - 128) / (255 - 128)) * (255 - 160) + 160)
  return image

def coldFilterRed(pixels):
  height = len(pixels)
  width = len(pixels[0])
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      image[row][col][1] = pixels[row][col][1]
      image[row][col][2] = pixels[row][col][2]
      if r < 64:
        image[row][col][0] = int(r / 64 * 50)
      elif r >= 64 and r < 128:
        image[row][col][0] = int(((r - 64) / (128 - 64)) * (100 - 50) + 50)
      else:
        image[row][col][0] = int(((r - 128) / (255 - 128)) * (255 - 100) + 100)
  return image

def rotateLeft(pixels):
  height = len(pixels)
  width = len(pixels[0])
  rotated_image = cmpt120imageProjHelper.getBlackImage(height, width)
  for row in range(height):
    for col in range(width):
      rotated_image[col][row] = pixels[row][width - col - 1]
  return rotated_image

def rotateRight(pixels):
  height = len(pixels)
  width = len(pixels[0])
  rotated_image = cmpt120imageProjHelper.getBlackImage(height, width)
  for row in range(height):
    for col in range(width):
      rotated_image[col][row] = pixels[height - row - 1][col]
  return rotated_image

def doubleSize(pixels):
  height = len(pixels)
  width = len(pixels[0])
  resized_image = cmpt120imageProjHelper.getBlackImage(width * 2, height * 2)
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      resized_image[2 * row - 1][2 * col - 1] = pixel
      resized_image[2 * row][2* col - 1] = pixel
      resized_image[2 * row - 1][2* col] = pixel
      resized_image[2 * row][2 * col] = pixel
  return resized_image

def halfSize(pixels):
  height = len(pixels)
  width = len(pixels[0])
  resized_image = cmpt120imageProjHelper.getBlackImage(width // 2, height // 2)
  for row in range(height // 2):
    for col in range(width // 2):
      r1 = pixels[2 * row - 1][2 * col - 1][0]
      r2 = pixels[2 * row][2* col - 1][0]
      r3 = pixels[2 * row - 1][2* col][0]
      r4 = pixels[2 * row][2 * col][0]

      g1 = pixels[2 * row - 1][2 * col - 1][1]
      g2 = pixels[2 * row][2* col - 1][1]
      g3 = pixels[2 * row - 1][2* col][1]
      g4 = pixels[2 * row][2 * col][1]

      b1 = pixels[2 * row - 1][2 * col - 1][2]
      b2 = pixels[2 * row][2* col - 1][2]
      b3 = pixels[2 * row - 1][2* col][2]
      b4 = pixels[2 * row][2 * col][2]

      resized_image[row][col][0] = (r1 + r2 + r3 + r4) // 4
      resized_image[row][col][1] = (g1 + g2 + g3 + g4) // 4
      resized_image[row][col][2] = (b1 + b2 + b3 + b4) // 4
  return resized_image

def findYellow(pixels):
  height = len(pixels)
  width = len(pixels[0])
  row_list = [] 
  col_list = []
  image = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      image[row][col][0] = r
      image[row][col][1] = g
      image[row][col][2] = b
      color_tuple = cmpt120imageProjHelper.rgb_to_hsv(r, g, b)
      h = color_tuple[0]
      s = color_tuple[1]
      v = color_tuple[2]
      if h > 55 and h < 80 and s > 35 and s < 55 and v > 55:
        row_list.append(row) # create a list of all rows with desired yellow value
        col_list.append(col) # create a list of all columns with desired yellow value
  return (row_list, col_list) # returns a tuple of the list of rows and list of columns

def boxDraw(pixels, rlist, clist): 
  image = copy.deepcopy(pixels)
  for row in range(min(rlist), max(rlist)):
    for col in range(min(clist), max(clist)): # create box using min/max values from list of rows and columns
      image[min(rlist)][col][0] = 0 
      image[min(rlist)][col][1] = 255 # turns desired pixel green
      image[min(rlist)][col][2] = 0

      image[max(rlist)][col][0] = 0
      image[max(rlist)][col][1] = 255
      image[max(rlist)][col][2] = 0

      image[row][min(clist)][0] = 0
      image[row][min(clist)][1] = 255
      image[row][min(clist)][2] = 0

      image[row][max(clist)][0] = 0
      image[row][max(clist)][1] = 255
      image[row][max(clist)][2] = 0
  return image
    

