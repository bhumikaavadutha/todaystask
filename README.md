# boundingbox, crop image

 A tool to crop and bounding box for images using argument parser 
 
## Installation

 install pillow, argparse 
 using pip 

 ## usage

  provide path for csv file, image directory and output directory
  
  use command os.makedirs to create output directory
  
  install required packages

       pip install -r requirements.txt
       
## explanation
   parser.add_argument("--image_path") = using this syntax we give image path through the terminal
   parser.add_argument("--csv") = using this syntax we give csv file path through the terminal
   parser.add_argument("--out_dir") = using this syntax we give output directory path through the terminal

   to crop and draw boxes we use 5 parameters 

   
    image: A numpy array, channel last (ie. height x width x colors) with channels in BGR order (same as openCV format).
    left: A integer representing the left side of the bounding box.
    top: A integer representing the top side of the bounding box.
    right: A integer representing the right side of the bounding box.
    bottom: A integer representing the bottom side of the bounding box.

    use functions 
    draw_boxes - for draw the bounding box around the image
    crop_image - for crop the image 

    we give the output directory name through the terminal 
    
  ## example
  
  # crop image
 ![0_7622202030987_f306535d741c9148dc458acbbc887243_L_488](https://github.com/bhumikaavadutha/todaystask/assets/169041060/9505316c-60a1-4910-9c4a-53ca587c35b5)

   # boundingbox

 ![full_7622202030987_f306535d741c9148dc458acbbc887243_L_521](https://github.com/bhumikaavadutha/todaystask/assets/169041060/e33418d0-7978-48f0-b4f9-c6f45b34f6b6)





 # Histogram

  it gives the graphical representation for RGB image using argument parser 

 ## Installation 

    install numpy, opencv, matplotlib, argparse 

      using pip install

 ## Usage

   provide the path to the input image as an arguments

   it will convert the histogram plot for each color channel and display it.

   install required packages

           pip install -r requirements.txt

 ## Explanation
 parser.add_argument('--image') - using this syntax we provide image path through the terminal

 parser.add_argument('--output') - using this syntax we provide the path through the terminal


  image = cv2.imread(args['image']) - it reads the image 
  cv2.imwrite(args["output"], image) - it save the image

   plt.plot - it plots the histogram using matplotlib 

## Example

 ### input

 ![b](https://github.com/bhumikaavadutha/todaystask/assets/169041060/f5d6cf4f-0776-47d7-99bb-a4af81cfc5e9)
 
 ### ouput

  
 ![Figure_1](https://github.com/bhumikaavadutha/todaystask/assets/169041060/c6fb4992-74b9-4e32-a3b0-11750682018a)






# Iteration

 It iterate the first 10 numbers, and in each iteration print the sum of the current and previous number.

## Installation

install argparse using pip

## Usage

  This script print the current number, previous number, and sum of the two for each number in the range.

## Explanation

  
  parser.add_argument('current_number') - using this syntax to provide current number through the terminal
  parser.add_argument('previous_number') - using this synatx to provide previous number through the terminal

  and we use the for loop

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

 This tool is to capture the video from the webcam using argument parser 

## installation

  install opencv, argparse using pip install

## Usage 

 define a vid = cv2.VideoCapture(0) for video capture

 install required packages

      pip install -r requirements.txt

 ## Code Explanation

    parser.add_argument("--output") - we provide output name through the terminal
    parser.add_argument("--cam",) - we give cam to use for video compression

    define video capture object

             video = cv2.VideoCapture(0)

    define width and height of the frame
    
   result = cv2.VideoWriter - creat VedioWriter object to write vedio
    
   cv2.imshow - use this syntax to display the frame

   cv2.destroyAllWindows() - this is used to close all the frames


    


  ## Example






  https://github.com/bhumikaavadutha/todaystask/assets/169041060/53c936a2-34e2-4649-bc9b-9300605f5330

    
   
         
  

 

  
 

 


  






 
 





  



