## Unit 1 | Assignment - KickStart My Chart

Items 1-4 are in HW1.XLS
Item 5 is in HW1 - Category.XLS
Item 6 is in HW1 - Sub-Category.XLS
Item 7 is in HW1 - Graphs.XLS

I removed some of the outliers from the scatterplot to make the graph look more meaningful.



## Background

Over two-billion dollars have been raised using the massively successful crowdfunding service, Kickstarter,
 but that does not mean that every project created has found success. Over three hundred thousand projects have been launched on the site but only a third of
 these projects have made it through the funding process with a positive outcome.

Since getting funded on Kickstarter requires you to reach and/or exceed your initial goal, many organizations spend months looking through past projects in an attempt
 to discover some trick to finding success. For this week's homework, you will be organizing and analyzing a database of four thousand past projects in order to uncover 
whatever trends may be hidden within.

## Instructions

* Using the Excel table provided, you will be modifying and analyzing the data of four-thousand past Kickstarter projects as you attempt to uncover some of the market trends it contains.

1. Use conditional formatting to fill each cell in the `state` column with a different color which changes according to whether the associated campaign was "successful", "failed", 
"cancelled", or is currently "live".

2. Create a new column at column O called `percent funded` which uses a formula to uncover how much money a campaign made towards reaching its initial goal.

3. Create a new column at column P called `average donation` which uses a formula to uncover how much each backer for the project paid on average.

4. Create two new columns, one called `category` at Q and another called `sub-category` at R, which use formulas to split the `Category and Sub-Category` column into two parts.

  5. Create a new workbook which will look into your initial workbook so as to count how many campaigns were "successful", "failed", "cancelled", or are currently "live" per **category**.

  6. Create a new workbook which will look into your initial workbook so as to count how many campaigns were "successful", "failed", "cancelled", or are currently "live" per
     sub-category**.

7. Create a scatterplot which compares each successful row's initial goal to the amount of money it raised. Then create a linear trendline for this chart.

## Bonus

* The dates stored within the `deadline` and `launched_at` columns are using unix timestamps. Fortunately for us, there is a formula out there which can be used to convert these
 timestamps into a normal date. Your mission, should you choose to accept it, is to modify these columns so that they contain readable dates.
