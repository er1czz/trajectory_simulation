import numpy as np
import pandas as pd

class dot:
    # the starting point will always be (0.5, 6)
    def __init__(self):
        # numpy.random.random_sample half-open interval [0.0, 1.0)
        # initial position is always at (0.5, 6)
        self.x = 0.5
        self.y = 6
        self.dx = np.random.random_sample()/2
        self.dy = np.random.random_sample()/2
        
    def move(self):
         # boundary 10 x 8
         # out of boundary will reverse direction but with same travel distance
        if self.x < 0.5 or self.x >= 9.5:
            self.dx *= -1
        if self.y < 0.5 or self.y >= 7.5:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy


def dot1_full_track():
    # full tracking record of 1 dot from enter to exit
    # entry point is (0.5, 6) which is mandated by class dot
    # exit zone, rectangle, (0, 3) (1, 2) as shown in the 2D map 
    # the dot will stop moving once inside the exit zone
    
    d1 = [dot()]

    # create list of move, x_coor and y_coor
    Steps, X_coors, Y_coors= [], [], []
    
    # time counter equal to timestep
    step = 0
    
    # coordinate of 1 dot
    x_coor, y_coor = [d.x for d in d1][0], [d.y for d in d1][0]
        
    # define exit zone (0, 3) (1, 2)
    while x_coor > 1 or (y_coor > 3 or y_coor < 2):
        for d in d1:
            d.move()
            x_coor, y_coor = [d.x for d in d1][0], [d.y for d in d1][0]
            step += 1
            Steps.append(step)
            
            # round output to 3 digits to reduce data size
            X_coors.append(round(x_coor, 3))
            Y_coors.append(round(y_coor, 3))
            break
            
    print('total steps:', step)
    print('initial coordinate:', (0.5, 6))
    print('final coordinate:', (X_coors[-1], Y_coors[-1]))
    return Steps, X_coors, Y_coors


def dots_df_gen(customer_num):
    customer_num = int(customer_num)
    
    Steps, X_coors, Y_coors = dot1_full_track()
    df = pd.DataFrame({'step': Steps, 'x': X_coors, 'y': Y_coors}) 

    # create a new column as customer id
    df['id'] = 0
    
    if customer_num > 1:
        for i in range(customer_num-1):
            Steps, X_coors, Y_coors = dot1_full_track()
            df1 = pd.DataFrame({'step': Steps, 'x': X_coors, 'y': Y_coors})
            df1['id'] = i+1
            df = pd.concat([df, df1], ignore_index=True, axis=0)
            
    return df