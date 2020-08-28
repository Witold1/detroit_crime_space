# DetroitCrime.space | started at calvinhacks2020, Grand Rapids, MI
> Visualise police crime reports data. Enforce ["Police Data Initiative"](https://www.policedatainitiative.org/participating-agencies/)

## What it does
It visualizes, analyzes, and 'predicts' the crimes and offenses reports (data provided by participated police departments) published from Police Data Initiative.

<table>
<thead>
  <tr>
    <th>Crimes by category per year, dashboard</th>
    <th>Exampled map of the City</th>
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

## How I built it
I did find and use the crimes report dataset for the largest Michigan city. Then download it and push the raw data to MongoDB Atlas cloud database. Then made a connection with a database to process data with python scripts and saved it locally because of the resources optimization. At this step I also used geocoding, to encode some needed string addresses to geo-features (Latitude and Longitude pairs). And the final step was the insights selection, trends analysis, and static and dynamic visualization via python frameworks and webGL (probably, one of the best and stable solution to such large geospatial dataset).

## How to use it?
* Link [nbviewer](https://nbviewer.jupyter.org/github/Witold1/calvinhacks2020/blob/master/preprocessing_and_visualizations.ipynb#PRESENTATION) and [html](.) to current version of processing and visualisation Jupyter notebook. 
* [Link to kepler.gl](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/u0aqfbui3muxmoq/keplergl_2ndwn6n.json). Issues with opening might occur because of a 3D-engine's resource consumption.

<p align="center">
  <img src="https://i.imgur.com/GNEk3Ob.jpg" align="center" alt="The first slice of a timeline" width="90%" height="70%">
</p>
