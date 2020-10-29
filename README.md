## This is the early project of cs 289 in Fall 2020. 

In this dataset, we used some modern datasets from NASA and processed them into the format used by Liu Hong. Our dataset is catered for further exploring the ideological source of Liu Hong's study, and constructing a mathematical prediction model with modern Machine Learning techniques.

We first collected the moon ephemerides data from NASA HORIZONS System. The main entries of concern include date, right ascension, and declination of the Moon with respect to the observing site in the International Celestial Reference Frame. The dates we used are from 2019-Oct-21 to 2020-Oct-20. In order to cover cities of different latitudes and longitudes, we choose as the observing sites:
- Adelaide, Australia (138°35'00.0''E, 34°55'00.0''S); 
- Beijing, China (116°22'59.9''E, 39°54'59.8''N); 
- Addis Ababa, Ethiopia (38°43'59.9''E, 9°00'00.0''N); 
- London, England ( 0°07'00.1''W, 51°30'00.0''N); 
- Brasilia, Brazil (47°55'00.1''W, 15°52'00.1''S); and 
- Berkeley, CA (122°16'15.6''W, $37°52'09.8''N).

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
|DATE| UTC times for observation YYYY-Mon-Day| 
|RA|in hours-minutes-seconds of time, in arc degree|
|DEC|in hours-minutes-seconds of time, in arc degree|
|Parts| Parts of Lunar Motion gives the Moon’s daily motion in (1/19) du in Liu Hong’s table and in arc degrees in our dataset.|
|dRA| daily RA change |
|dDEC| daily DEC change|
|RLI| Rate of Lessening or Increase (RLI). RLI gives the difference between Parts of LunarMotion and the mean daily motion of 254/19duin Liu Hong’s table and inarc degreesinour data|
|CRLI| Cummulative Rate of Lessening or Increase |

