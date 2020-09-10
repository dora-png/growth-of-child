# growth-of-child
# well-growth
App.py
===============

What is it
----------
`App.py` is a python script that allows the (graphical) assessment of a child's development according to the [World Health Organization (WHO) growth standards](http://www.cdc.gov/growthcharts/who_charts.htm).
It allows to visualise inconsistencies in child growth pattern and show how the children of the medical center of Nsukka are growing according to the weight.

Main features
-------------

The script, using as input data the child's:
* gender
* age
* weight
* length
* name
* name of the parent
 
generates a series plots showing:
 * the curve and rate of child's growth comparing with WHO mean chart and Local mean chart and
 * the inconsistencies in the growth curve of any child entered
 * in which [percentile](http://en.wikipedia.org/wiki/Percentile) of population the child lies.

allow collection of children's data and registers individual informations(data and curve) of children in file for later evaluation.
by generating
 *csv file for individual data
 *png file for individual curve

An example of the output plots is shown in [this figure](http://github.com/Ndoumbe-Ndjinkou-Dora-Benazir/growth-of-child/tree/master/Data/Girls/curve2.png).

Where to get it
---------------

The source code is hosted on GitHub at: [http://github.com/Ndoumbe-Ndjinkou-Dora-Benazir/growth](http://github.com/Ndoumbe-Ndjinkou-Dora-Benazir/growth-of-child).

Dependencies
------------

* [NumPy](http://www.numpy.org) - for array objects 
* [matplotlib](http://matplotlib.org) - for plots
* [tkinter]- for the interface

Documentation
-------------

The input required by `App.py` is the population of the file `BoyDataSet.csv`, 'GirlDataSet.csv', 'g_age_N_lenght.csv', 'b_age_N_lenght.csv',
'g_age_N_weight.csv','b_age_N_weight.csv', 'g_age_lenght.csv', 'b_age_lenght.csv', 'g_age_weight.csv', 'b_age_weight.csv' which contains the child's:

* gender
* weight
* length
* age
* name
* id
* 50th percentile of the population (of WHO, of Medical Center of Nsukka)
* values of L,M,S of the population 
 

at different ages. 
The structure of the file is as following:

<table>
  <tr>
      <th>id</th><th>age</th><th>gender</th><th>length</th><th>name</th><th>parent</th>
  </tr>
</table>

An example can be found [here](http://github.com/Ndoumbe-Ndjinkou-Dora-Benazir/growth-of-child/tree/master/Data/BoyDataSet.csv). 


Background
----------
 
`App.py` is a rather complex script. 

My primary goal developing `App.py`  was to help to follow the growth of children in his locality and find inconsistencies in the 
growth pattern by visualisation 
* python (and in particular NumPy and matplotlib) for data analysis - as an alternative to Matlab, and
* Git 

Without doubt, more simplistic code development can be used to address this topic. 

Discussion and development
--------------------------

Future features for implementation and development ideas are listed in the [TODO.md](http://github.com/Ndoumbe-Ndjinkou-Dora-Benazir/growth-of-child/tree/master/TODO.md) file.

Licence
-------

This work is licensed under a [GNU General Public License v3.0](https://fsf.org/).

Contact
-------

[Mail](ndoumbedora1094@gmail.com, Honour.nwagwu@unn.edu.ng)



