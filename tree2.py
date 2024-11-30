from turtle import *
speed('fastest')
rt(-90)
branch_angle = 30

# Function to draw the fractal tree
def draw_tree(branch_size, level):
    # Base case: stop drawing if the level is 0
    if level > 0:
        colormode(255)
        pencolor(0, 255 // level, 0)
  
        fd(branch_size)
        rt(branch_angle)
        
        # Recursively draw the right subtree with smaller branches and reduced level
        draw_tree(0.8 * branch_size, level - 1)    
        pencolor(0, 255 // level, 0)

        lt(2 * branch_angle)
        
        # Recursively draw the left subtree with smaller branches and reduced level
        draw_tree(0.8 * branch_size, level - 1)
        
   
        pencolor(0, 255 // level, 0)
        
    
        rt(branch_angle)
        
        fd(-branch_size)


draw_tree(80, 7)
done()