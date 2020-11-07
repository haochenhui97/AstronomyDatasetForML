## This is the early project of cs 289 in Fall 2020. 

In this dataset, we used some modern datasets from NASA and processed them into the format used by Liu Hong. Our dataset is catered for further exploring the ideological source of Liu Hong's study, and constructing a mathematical prediction model with modern Machine Learning techniques.

We first collected the moon ephemerides data from NASA HORIZONS System. The main entries of concern include date, right ascension, and declination of the Moon with respect to the observing site in the International Celestial Reference Frame. The dates we used are from 2019-Oct-21 to 2020-Oct-20. In order to cover cities of different latitudes and longitudes, we choose as the observing sites:
- Adelaide, Australia (138°35'00.0''E, 34°55'00.0''S); 
- Beijing, China (116°22'59.9''E, 39°54'59.8''N); 
- Addis Ababa, Ethiopia (38°43'59.9''E, 9°00'00.0''N); 
- London, England ( 0°07'00.1''W, 51°30'00.0''N); 
- Brasilia, Brazil (47°55'00.1''W, 15°52'00.1''S); and 
- Berkeley, CA (122°16'15.6''W, 37°52'09.8''N).

## Input data
|Name | Description |
|:-:|---|
|TIME| UTC times for observation, YYYY-Mon-DD HH:MM e.g.2020-Oct-20 00:00  | 
|R.A.| Astrometric right ascension of the target center with respect to the observing site (coordinate origin) in the reference frame of the planetary ephemeris (ICRF).RA  in hours-minutes-seconds of time, HH MM SS.ff{ffff}|   
|DEC| Declination of the target center. DEC in degrees-minutes-seconds of arc,  sDD MN SC.f{ffff}|
|dRA*cosD/dt|The angular rate of change in aparent RA of the target|
|d(DEC)/dt|The angular rate of change in aparent DEC of the target|
|APmag|Moon's approximate apparent visual magnitude|
|S-brt|Moon's approximate surface brightness|


## Output data
The time for each day is 00:00 UTC.
|Name | Description | 
|:-:|---|
|DATE| UTC time for observation YYYY-Mon-Day| 
|RA|in arc degrees|
|DEC|in arc degrees|
|Parts| Parts of Lunar Motion, gives the Moon’s daily motion in (1/19) du in Liu Hong’s table and in arc degrees in our dataset.|
|dRA| daily RA change |
|dDEC| daily DEC change|
|RLI| Rate of Lessening or Increase (RLI), gives the difference between Parts of Lunar Motion and the mean daily motion of 254/19 du in Liu Hong’s table and in arc degrees in our data|
|CRLI| Cummulative Rate of Lessening or Increase, gives the accumulated sum of the RLI |

## 11/6 Update
We modified <code>generate_csv.py</code> from [Team JNA](https://github.com/NaveenGop/astro-data) to make the data generation process more automatic. By procedurally sending an email request to the Horizons system, it allows easy customizability with regards to observer location and time frame. Users may change the following parameters:

    username = "sample@gmail.com"
    password = ''  # can also hardcode the pwd
    site_coord = "'116.383300,39.9166000,0.0000000'" # Set observation site, e.g. Beijing's coord is used here
    start_time = "'2019-10-21'"
    stop_time = "'2020-10-20'"
    output_name = 'Beijing' 

Note: <code>site_coord</code> needs to be the coordinate of an observatory that is in the Horizons database, e.g. the six cities we listed above. Users may want to refer to the [website](https://ssd.jpl.nasa.gov/horizons.cgi?s_loc=1#top) to see the available site candidates.

The output is the daily observation of lunar movements. It contains 3 columns: Date and time in UTC, astrometric RA and DEC.

The file <code>data_process.py</code> is created to standardize the data processing procedure. It takes a filename as input (which should be the output from <code>generate_csv.py</code>) and generates the processed dataset.

Example
 <code>python3 generate_csv.py</code> 
 <code>python3 data_process.py Beijing.csv</code> 

The former <code>Data Process.ipynb</code> was renamed as <code>data_visualization.ipynb</code> since its function is only left with visualizing the datasets we generated before.

Example
 <code>python3 generate_csv.py</code> 
 <code>data_process.py </code> 
  
## Contributors
Chenhui Hao, Kaijing Ding, Ke Liu and Zishan Cheng

