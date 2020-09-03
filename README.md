# DetroitCrime.space | started at calvinhacks2020, Grand Rapids, MI
> Visualise police crime reports data. Enforce ["Police Data Initiative"](https://www.policedatainitiative.org/participating-agencies/)

## Examples of analysis outputs
Generally speaking, it visualizes, analyzes, and 'predicts' the crimes and offenses reports (data provided by participated police departments) published from Police Data Initiative.

An example of a preliminary report was made is available via _htmlpreview_ [here](https://htmlpreview.github.io/?https://github.com/Witold1/DetroitCrime.space/blob/master/reports/visualizations_prereport.html).

| Per neighborhood, from 2016                                                                                          | Per hour, from 2016                                                                                           |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <img src="https://i.imgur.com/RkqZDxX.png" align="center" alt="Per Motor City neighborbood, from 2016" width="100%"> | <img src="https://i.imgur.com/CPMqiAO.png" align="center" alt="Per hour, overall for time" width="100%">      |
| By offence category, per year (layered dashboard)                                                                                        | Top-15 offence categories, from 2016                                                                          |
| <img src="https://i.imgur.com/09fsVdq.png" align="center" alt="Top-5 offence categories, per year" width="100%">     | <img src="https://i.imgur.com/ksYk0wF.png" align="center" alt="Per offence category, from 2016" width="100%"> |

## How is it built?
I did find and used publically open criminal offenses and crimes report datasets from the largest Michigan city. Downloaded it, preprocessed, and pushed to MongoDB Atlas cloud database to make it analysis-ready from everywhere.   

The final steps was insights mining, trends analysis, and static and dynamic visualization via a rich python ecosystem. I used classical and contemporary libs for geo-spatial visualization as well as packages for the table and gridded data processing. Then, as a usual part of the data related analysis loop, the report was prepared and beautified, and next steps were marked.

<table>
<thead>
  <tr>
    <th>Architecture and processing pipeline image:</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="https://i.imgur.com/HD8ek3s.png" alt="Pipeline, a bit obsolete version" height="50%" width="100%"></td>
  </tr>
</tbody>
</table>

* Plus, Datashader & Holoviews (inc. matplotlib backend)


## How to use it?
* Functions are documented with .ipynb examples of use; pipeline are demonstrated
* Insights are reproducible and might be checked in notebooks

## How to improve it?
* **More advanced methods** of criminal-related analysis and statistics (e.g. methods from directional statistics and spatial statistics) may and must be used, as well as **better visualization** must be produced; **clustering techniques** might be useful for better insight;
* Insights and stat.analisys are better when using counted relative numbers (per $1000$, per $10.000$), so the population of districts and neighborhoods are crucial to be added
* Professional GIS software domain tools may and must be better analyzed;
* Example of cool products : [old competition](https://www.kaggle.com/c/sf-crime/notebooks), existed web-interfaces [\[1\]](https://cityofdetroit.github.io/crime-viewer/), [\[2\]](http://people.ischool.berkeley.edu/~john.blakkan/ischool_version/index.html), [\[3\]](https://chicagocrimescenes.blogspot.com/) or [PredPol](https://www.predpol.com/)

<img src="https://gallery.yopriceville.com/var/resizes/Free-Clipart-Pictures/Police-PNG/Police_Line_Transparent_PNG_Clip_Art_Image.png?m=1527240027" alt="Police line image" height="50%" width="100%">
