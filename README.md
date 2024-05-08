# boundingbox, crop image

 A tool to crop and bounding box for images
 
## Installation

 install pillow using pip 

 ## usage

  provide path for csv file, image directory and output directory
  
  use command os.makedirs to create output directory
  
  install required packages

       pip install -r requirements.txt
       
## explanation
   give the path for csv_file = "/path/"
   image_dir = "/path/"
   output_dir = "/path/"

   to crop and draw boxes we 5 parameters in this

   
    image: A numpy array, channel last (ie. height x width x colors) with channels in BGR order (same as openCV format).
    left: A integer representing the left side of the bounding box.
    top: A integer representing the top side of the bounding box.
    right: A integer representing the right side of the bounding box.
    bottom: A integer representing the bottom side of the bounding box.

    use functions 
    draw_boxes - for draw the bounding box around the image
    crop_image - for crop the image 
    
  ## example
  
  # crop image
 ![0_7622202030987_f306535d741c9148dc458acbbc887243_L_488](https://github.com/bhumikaavadutha/todaystask/assets/169041060/9505316c-60a1-4910-9c4a-53ca587c35b5)

   # boundingbox

 ![full_7622202030987_f306535d741c9148dc458acbbc887243_L_521](https://github.com/bhumikaavadutha/todaystask/assets/169041060/e33418d0-7978-48f0-b4f9-c6f45b34f6b6)





 # Histogram

  it gives the graphical representation for RGB image

 ## Installation 

    install numpy, opencv, matplotlib 

      using pip install

 ## Usage

   provide the path to the input image as an arguments

   it will convert the histogram plot for each color channel and display it.

   install required packages

           pip install -r requirements.txt

 ## Explanation

  cv.imread - it read the image

  cv.imwrite - it save the image

   plt.plot - it plots the histogram using matplotlib 

## Example

 ### input

 ![b](https://github.com/bhumikaavadutha/todaystask/assets/169041060/f5d6cf4f-0776-47d7-99bb-a4af81cfc5e9)
 
 ### ouput

  
 ![Figure_1](https://github.com/bhumikaavadutha/todaystask/assets/169041060/c6fb4992-74b9-4e32-a3b0-11750682018a)






# Iteration

 It iterate the first 10 numbers, and in each iteration print the sum of the current and previous number.

## Usage

  This script print the current number, previous number, and sum of the two for each number in the range.

## Explanation

  intialize variable previous_num to 0

  range - to print iteration from 0 to 10

  calculating sum - each iteration it calculate sum of the current number with its previous number

  result - it print current, previous, and its sum

## Example

Current number 0, Previous Number 0 is 0

Current number 1, Previous Number 0 is 1

Current number 2, Previous Number 1 is 3

Current number 3, Previous Number 2 is 5

Current number 4, Previous Number 3 is 7

Current number 5, Previous Number 4 is 9

Current number 6, Previous Number 5 is 11

Current number 7, Previous Number 6 is 13

Current number 8, Previous Number 7 is 15

Current number 9, Previous Number 8 is 17




# Webcam

 This tool is to capture the video from the webcam.

## installation

  install opencv using pip install

## Usage 

 define a vid = cv2.VideoCapture(0) for video capture

 install required packages

      pip install -r requirements.txt

 ## Code Explanation

    define video capture object

             vid = cv2.VideoCapture(0)

    ret, frame = vid.read() - capture video from frame by frame

    cv2.imshow - display the resulting frame

    vid.release()  - it use after loop release the object

    cv2.destroyAllWindows() - using this destroy the all windows


  ## Example



  [Screencast from 08-05-24 12:17:09 PM IST.webm](https://github.com/bhumikaavadutha/todaystask/assets/169041060/3f73a10f-4798-44de-a545-21bb2867409c)


    
   
         
  

 

  
 

 


  






 
 





  



