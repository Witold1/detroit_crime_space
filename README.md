# DetroitCrime.space | started at calvinhacks2020, Grand Rapids, MI
> Visualise police crime reports data. Enforce ["Police Data Initiative"](https://www.policedatainitiative.org/participating-agencies/)

## Examples of analysis outputs
Example of a preliminary report was made are available via htmlpreview [here](https://htmlpreview.github.io/?https://github.com/Witold1/DetroitCrime.space/blob/master/reports/visualizations_prereport.html)

Generally speaking, it visualizes, analyzes, and 'predicts' the crimes and offenses reports (data provided by participated police departments) published from Police Data Initiative.

<table>
<thead>
  <tr>
    <th>Crimes by category per year, layered dashboard</th>
    <th>Exampled map of the City, interactive map</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
      <img src="https://i.imgur.com/s97Rle2.png" align="center" alt="Crimes by category per year, dashboard example" width="80%">
    </td>
    <td>
      <img src="https://i.imgur.com/f78bqAq.png" align="center" alt="Exampled map of the City" width="80%">
    </td>
  </tr>
</tbody>
</table>

## How is it built?
I did find and used publically open criminal offenses and crimes report datasets from the largest Michigan city. Downloaded it, preprocessed, and pushed to MongoDB Atlas cloud database to make it analysis-ready from everywhere.   

The final steps was insights mining, trends analysis, and static and dynamic visualization via a rich python ecosystem. I used classical and contemporary libs for geo-spatial visualization as well as packages for the table and gridded data processing. Then, as a usual part of the data related analysis loop, the report was prepared and beautified, and next steps were marked.

<img src="https://i.imgur.com/HD8ek3s.png" alt="Pipeline, a bit obsolete version" height="40%" width="70%">

## How to use it?
* Functions are documented with .ipynb examples of use; pipeline are drawn
* Insights are reproducible and might be checked in notebooks

<img src="https://gallery.yopriceville.com/var/resizes/Free-Clipart-Pictures/Police-PNG/Police_Line_Transparent_PNG_Clip_Art_Image.png?m=1527240027" alt="Police line image" height="50%" width="100%">
