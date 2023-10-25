# Customers in a *box*
Code Sample to simulate customers movement (dot trajectory) in a retail store
- Motivation: People movement tracking data can be commonly found in sports analytics research, for example [metrica football data](https://github.com/metrica-sports/sample-data). However, human behave can very different in sports vs during shopping. For example, it is possible all the players would enter and exit the field at the same time
- Scope: Simulating the trajectory of a customer in a rectanglar retail store 10 x 8 2D space
- Takeaway:
    1. Data synthesis: synthesize 2D tracking data of multiple customers in the same physcial space.
    2. Data visualization: illustrate trajectory data through interactive notebook and movie (e.g. mp4).
    3. Data storage: Unlike sports, the time customer spent in a retail store (**dwell time**) varies. To efficiently store the synthetic data, individual trajectories are stacked in the output. Typical column names are ```id, step, x, y``` instead of ```step, customer_1_x, customer_1_y, customer_2_x, customer_2_y, ...```
- P.S.
  - This synthetic dataset provide steps instead of timestamp. Different customer would enter the venue at different time. To add time as a new dimension, one can use random number generator to set different entry time for each customer.

      
- Future improvement:
  - Dot movement: more realistic as human behavior, current implementation is more like rigid particle bounding in a confined space
  - Dot interaction: to emulate customer - customer interaction, customer - employee interaction, etc.
  - Add floor plan (such as store shelves, furnitures, etc.) to show the utilization: e.g. customer - signage interaction.
    
<p align="center">
  <img src="https://github.com/er1czz/trajectory_simulation/blob/main/demo_1dot_tracking.gif" alt="animated" />
</p>
<p aligh="center">A customer (as the green dot) enters the retail store from the entry point and left from the exit zone. (Entry point: seafoam green; Exit zone: pale pink) </p>
<p align="center">
  <img src="https://github.com/er1czz/trajectory_simulation/blob/main/interface.png"/>
</p>
<p align="center">Inspect the trajectory of an individual customer through Jupyter Notebook</p>
<p align="center">
  <img src="https://github.com/er1czz/trajectory_simulation/blob/main/trajs.png"/>
</p>
