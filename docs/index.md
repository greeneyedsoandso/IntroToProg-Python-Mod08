# Using Objects with Classes

## Introduction
In this module, we built on what we learned previously about classes and started to create objects from classes. At first objects seem like a lot of lines of code to do things we already know. But they are a powerful way to separate concerns and make future changes less painful.
### False starts
This was a very difficult concept for me. I could see the various pieces but really wasn't understanding how they fit together, and more importantly why.

I restarted this project three or four times, and had trouble even after watching the module review video. Ultimately, the way I was able to move forward was to start out by ignoring the objects part of the rubric, and then refactor to work the objects in.
### Refactoring for objects
First, using the starter file, I got the desired functionality working without the objects. These were all tasks we had done before––read file, add items, review items, write file, a simple menu. I stored the product and price in a variable.

![Figure 1](2020-03-14_10.08.38PM.png)
In the FileProcessor class, I was reading out lists from the file.
![Figure 2](2020-03-14_10.14.21PM.png)
This was the first place I wanted to start using the Product class, so I filled in the init and str methods. Now I could start using objects to store and manipulate data.
![Figure 3](2020-03-15_1.14.35PM.png)
In the new version of FileProcessor.read_data_from_file, I could eliminate the list_row variable and replace it with a Product object.
![Figure 3](2020-03-14_10.33.58PM.png)
The next area to simplify was IO.print_current_products_in_list. 
![Figure 4](2020-03-14_10.37.29PM.png)
Now that my rows were Product objects, the print statement could be very simple. (More on that later.)
![Figure 5](2020-03-14_10.50.59PM.png)
IO.input_new_product_and_price got simpler as well.
![Figure 8](%202020-03-14_11.39.40PM.png)
And that made menu choice two half as long. (I was getting an error at this stage, which I later fixed when I added exception handling.)
![Figure 7](%202020-03-14_11.00.34PM.png)
After all that simplification, menu option 1 to review data didn't look as good as it used to. I lost all my spacing and formatting with the dollar sign. And I definitely didn't want that formatting cruft back in my nice csv data file. So I decided to try adding a method to make things pretty for display.
![Figure 10](%202020-03-14_11.55.33PM.png)
While I'm not sure that's a perfect separation of concerns, I'm pleased with how it satisfied my desire for human-readable text and machine-readable data.
![Figure 9](%202020-03-14_11.55.08PM.png)
Once everything seemed to be working, I reviewed the getter/setter properties––I had created them in early attempts but because I wasn't using the class successfully, I wasn't able to get the exceptions to fire. With the class working properly, it was time to set up some validation. 
![Figure 13](%202020-03-15_12.11.04AM.png)
In the process, I also realized that there was no reason to have two separate variables storing IO.input_new_product_and_price, and that's why I was erroring out when I tried to enter more than two new items.
![Figure 12](%202020-03-15_12.10.37AM.png)
The final version of the main body of the script was much more concise.
![Figure 11](%202020-03-15_11.47.40AM.png)
I made a few cosmetic tweaks, and everything worked as expected (Figures 14-16).
![Figure 14](%202020-03-15_12.03.26PM.png)
![Figure 15](%202020-03-15_12.06.24PM.png)
![Figure 16](%202020-03-15_12.07.29PM.png)

## Conclusion
I started this script with a superficial understanding of using class objects. It turns out that during my first several tries, I had created the class well, I just didn't get how to use it. By the time I figured out how to use it to transform data presentation, it really started to make sense and I could start to see how it streamlined the main body of the script and would make global changes easier.