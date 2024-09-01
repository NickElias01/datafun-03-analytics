''' 
Module: Elias Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
'''

#####################################
# Import Modules at the Top
#####################################

import statistics

#####################################
# Declare global variables
#####################################

has_international_clients: bool = True
years_in_operation: int = 10
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
accepting_new_clients: bool = True
consulting_packages: int = 3
analytic_tools: list = ["Python","Github","mySQL","Tableau","Microsoft Power BI"]
daily_temps: list = [95,93,88,86,90,90]

#####################################
# Calculate Basic Statistics 
#####################################

min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_temps: float = min(daily_temps)  
max_temps: float = max(daily_temps)  
mean_temps: float = statistics.mean(daily_temps)  
stdev_temps: float = statistics.stdev(daily_temps)

#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
Elias Analytics: Turning Complex Data into Clear Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
Standard Deviation:         {stdev_score:.2f}
Accepting New Clients:      {accepting_new_clients}
Consulting Packages:        {consulting_packages}
Analytic Tools:             {analytic_tools}
Daily Temp Highs in Denver  {daily_temps}
Minimum High Temp:          {min_temps}
Maximum High Temp:          {max_temps}
Mean High Temp:             {mean_temps:.2f}
Standard Dev High Temp::    {stdev_temps:.2f}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics project.'''
   return byline
   
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
