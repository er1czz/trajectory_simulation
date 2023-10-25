# Customers in a *"box"*
Code Sample to simulate customers movement (dot trajectory) in a retail store
- Motivation: People movement tracking data can be commonly found in sports analytics research, for example [metrica football data](https://github.com/metrica-sports/sample-data). However, human behaves differently during sport vs shopping. For example, it is possible all the players would enter and exit the field at the same time. The number of people in a sport event can be much fewer than that in a shopping event. Therefore, this code is to provide a tool that can synthesize 2D human tracking data in a retail store. 
- Scope: Simulating the trajectory of a customer in a rectanglar retail store (e.g. 10 x 8 2D confined space)
- Data synthesis:
    - ```git clone https://github.com/er1czz/trajectory_simulation.git```
    - ```python app.py``` and follow the instructions to enter number of customers and output file name 
- Visualization: please refer to the [demo.ipynb](https://github.com/er1czz/trajectory_simulation/blob/main/demo.ipynb)
- Takeaway:
    1. Data synthesis: synthesize 2D tracking data of multiple customers in the same physcial space. (e.g. [.csv](https://github.com/er1czz/trajectory_simulation/blob/main/sample_output.csv))
    2. Data visualization: illustrate trajectory data through interactive notebook [demo.ipynb](https://github.com/er1czz/trajectory_simulation/blob/main/demo.ipynb) and movie (e.g. [.mp4](https://github.com/er1czz/trajectory_simulation/blob/main/demo_1dot_tracking.mp4)).
    3. Data storage:
        - i) Coordinate values are rounded to 3 digits to save space.
        - ii) Unlike sports, the amount of time customer spent in a retail store **(*dwell time*)** varies. To efficiently store the synthetic data, individual trajectories are stacked in the output. Typical column names are ```id, step, x, y``` instead of ```step, customer_1_x, customer_1_y, customer_2_x, customer_2_y, ...```
- P.S.
  - This synthetic dataset provide steps instead of timestamp. Different customers would enter the venue at different times. To add time as a new dimension, random number generator can be used to set different entry time for each customer.

      
- Future improvements:
    - Add floor plan (such as store shelves, furnitures, etc.) to show facility utilization: e.g. customer - signage interaction.
    - Dot movement: more realistic as human behaviors. The current model exhibits rigid motions as if the dots are particles bouncing around in a confined space.
    - Dot interactions: to emulate customer - customer interactions, customer - employee interactions, etc.
    
<p align="center">
  <img src="https://github.com/er1czz/trajectory_simulation/blob/main/demo_1dot_tracking.gif" alt="animated" />
</p>
<p aligh="center">A customer (green dot) enters the retail store (10x8 rectangle box) at the entry point and leaves through the exit zone. (Entry point: seafoam green; Exit zone: pale pink) </p>
&nbsp;
&nbsp;
<p align="center">
  <img src="https://github.com/er1czz/trajectory_simulation/blob/main/interface.png"/>
</p>
<p align="center">Inspect the trajectory of an individual customer through Jupyter Notebook</p>
&nbsp;
&nbsp;
<p align="center">
  <img src="https://github.com/er1czz/trajectory_simulation/blob/main/trajs.png"/>
</p>
