import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import animation

# custom library
from dot_gen import dot

# extract coordinate list in [(x1, y1), (x2, y2), ...] from dots
def dot2coor(dots):
    X_coor = [d.x for d in dots]
    Y_coor = [d.y for d in dots]
    XY_coor = [i for i in zip(X_coor, Y_coor)]
    return XY_coor


def traj_1dot_show(X_coors, Y_coors):
    ax = plt.subplot()
    
    # add zones to indicate entrance zone and exit areas
    ax.add_patch(Rectangle((0, 5.5), 0.8, 1,
        alpha=0.1,facecolor='green', edgecolor = 'grey', label='Entrance', fill=True, lw=10))
    ax.add_patch(Rectangle((0, 2), 0.8, 1,
        alpha=0.1,facecolor='red', edgecolor = 'grey', label='Exit', fill=True, lw=10))
    plt.text(0.05, 5.7,'Entry', fontsize=10, rotation=30)
    plt.text(0.05, 2.3,'Exit', fontsize=10, rotation=30)
    
    # plot trajectory
    ax.plot(X_coors, Y_coors, '-', color='skyblue')

    # plot entry point enter and exit 
    ax.scatter([0.5], [6], color='green')
    ax.scatter([X_coors[-1]], [Y_coors[-1]], color='red')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    plt.title('Customer trajactory')
    plt.show()


# plot multiple dots at a given step 
def frame_dots_show(num_dot=1, num_step=1):
    # Disable interactive mode.
    plt.ioff()
    # clears the entire current figure
    plt.clf()
    
    num_dot = int(num_dot)
    num_step = int(num_step)
    
    dots = [dot() for i in range(num_dot)]
    #print('initial position:', [d.x for d in dots], [d.y for d in dots])
    if num_step > 0:
        for i in range(num_step):
            for d in dots:
                d.move()
            #print('step:', i+1, dot2coor(dots))
    
    plt.plot([dot.x for dot in dots], [dot.y for dot in dots], 'go')
    plt.xlim(0, 10)
    plt.ylim(0, 8)
    plt.title(f'{num_dot} customers at {num_step}th step')
    plt.show()


# create animation 
def movie_1dot_gen(Steps, X_coors, Y_coors):
    # disable interactive mode
    plt.ioff()
    
    fig, ax = plt.subplots()
    plt.rcParams["animation.html"] = "jshtml"
    plt.rcParams['figure.dpi'] = 150  
    
    def animate(frame):
        ax.clear()
        
        # add zones to indicate entrance zone and exit areas
        ax.add_patch(Rectangle((0, 5.5), 0.8, 1,
            alpha=0.1,facecolor='green', edgecolor = 'grey', label='Entrance', fill=True, lw=10))
        ax.add_patch(Rectangle((0, 2), 0.8, 1,
            alpha=0.1,facecolor='red', edgecolor = 'grey', label='Exit', fill=True, lw=10))
        plt.text(0.05, 5.7,'Enter', fontsize=10, rotation=30)
        plt.text(0.05, 2.3,'Exit', fontsize=10, rotation=30)
    
        # update by frame
        x = X_coors[frame]
        y = Y_coors[frame]
        # update the plot:
        ax.plot(x, y, color='green', 
                label='original', marker='o')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        
    anim = animation.FuncAnimation(fig, animate, frames=len(Steps), interval=100, repeat=True)
    return anim