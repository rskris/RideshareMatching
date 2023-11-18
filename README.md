# NYC Ridesharing Optimization

# Problem description
We looked into different ridesharing matching algorithms. Specifically, we wanted to explore the real-world implications of using these algoritms, by using ridesharing data from New York City. These algorithms have in part be drawn from "Online Vehicle Routing: The Edge of Optimization in Large-Scale Applications" by Bertsimas et al. (2018). 

We used 1.5 hours of ridesharing data, from a Friday afternoon in April 2016. For our simulations, we worked with 1,000 unique customers, as well as 150 cars. A snapshot of this data is visualised below, with green dots customers at their start point and yellow pointers representing the cars. The dataset also provided information on the price paid for each ride. This data was used to calculate revenue for the different algorithms. 

![Figure 1](https://i.imgur.com/MeLvneh.png)

We worked with the following assumptions:
- The average wait time for a customer is 5 minutes
- The distance between 2 coordinates is straight-line distance
- A taxi can serve at most 4 customers at a time
- The time a customer made the call (`tcall`) is 3 minutes before he was actually picked up in the dataset
- The minimum time to pick up a customer (`tmin`) is 2 minutes before he was actually picked up in the dataset
- The maximum time to pick up a customer (`tmax`) is 2 minutes after he was actually picked up in the dataset
- The start positions for the taxi drivers are the start positions of their first customer
- The speed of a taxi is the distance of its previous order divided by the total time of its previous order

# Algorithms
We developed and analyzed three different algorithms. Two of these are offline, and one is an online algorithm. The first, baseline model is a simple **Mixed Integer Optimization** (MIO) model. In this model, we treat customers on a first-come-first-served basis. Our second algorithm builds on the baseline model, and uses **Heuristic Insertion** in this process, we collect the customers that could not be served due to unavailability of taxis, and try to insert them in the current taxi schedule. Finally, we worked on one online algorithm, using the **nearest first** approach, in which a customers - upon arrival in the model - is assigned to the closest available car. 

# Results
We summarize our results as follows:
- Provided there are enough taxis available, all algorithms find a solution in which all customers are served;
- When few taxis are present in the online algorithm, the per-taxi revenue is low;
- There is a trade-off between the percentage of customers successfully served, and the per-driver revenue.

These findings are summarized in the figures below. 

![Figure 2](https://i.imgur.com/xnaehQn.png)

# Future work
We note this work has been a primer into the different ridesharing matching algorithms exist, of which most surpass the ones presented in terms of sophistication. In a future iteration of this work, we would be interested in:
- Exploring more online algorithms
- Analyzing effect of different customer waiting times
- Analyzing performance at different times of day

