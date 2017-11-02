
### Review of Homework 3, Assignment 2 of Nicholas Jones, nj953

### By: Ruben Hambardzumyan, rh2684


<b><font color = 'blue'>a. verify that their Null and alternative hypotheses are formulated correctly</b>


<b>Idea: Men make longer rides than women do.</b>

<b>Null Hypothesys: Mean ride length for men is equal to or smaller than mean ride length for women.</b>

<b>Ruben:</b> While the idea itself is fair, the null hypothesys suggests to compare the mean of the sample consisted of men only from the population with the mean of the sample consisted of women only, where the size of the sample is (presumably) is only limited with the size of the population itself. There are points that need to be addressed here:
<ul>
    <li>
    The Null hypothesys should be formulated in a way to fullfill the alternative hypothesys (idea formulation) for their sum to be equal to 0. Taking this into account, a better Null hypothesys in this case would be: <b><i>mean ride length for women is equal to or smaller than mean ride lenght for men.</i></b>
    </li>
    <li>
    Taking only the mean ride length value as the basis for proving the idea contains risks, such as men and women taking the same route to commute during the weekdays (time factor is not considered). To eliminate commute, a better Null hypothesys would be: <b><i>mean ride length for women over the weekend is equal to or smaller than mean ride lenght for men over the weekend.</i></b>
    </li>
</ul>


<b><font color = 'blue'>b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)</b>

<b>Ruben:</b> From the Citibike dataset, data.['Trip Duration'] and data.['Gender'] columns have been chosen, which is enough to make assumptions based on the formulated Null hypothesys. The data has been properly pre-processed. However, Nick got the results where the mean ride lentgh for men is smaller than that for women. Thus, he proves the Null hypothesis whereas in fact the Null hypothesys is rejected (women must have equal or less mean ride length).

<b><font color = 'blue'>chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.</b>

<b>Ruben:</b> This is the case where samples are coming from the same population and when we have non-parametric data (Gender), and only two variables (Trip Duration and Gender) I suggest Nick to do a <b>two-way non-parametric ANOVA test.</b>


