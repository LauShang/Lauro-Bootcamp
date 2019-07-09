var earthquakesUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

console.log(31)

function markerSize(magnitude) {
    return magnitude * 3;
};

var earthquakeLayer = new L.LayerGroup()

d3.json(earthquakesUrl, function (geoJson) {
    
    L.geoJSON(geoJson.features, {
        pointToLayer: function (geoJsonPoint, latlng) {
            return L.circleMarker(latlng, {radius: markerSize(geoJsonPoint.properties.mag)});
        },

        style: function (geoJsonStyle) {
            return {
                fillColor: magColor(geoJsonStyle.properties.mag),
                fillOpacity: 0.7,
                weight: 0.1,
                color: 'black'
            }
        },

        onEachFeature: function (feature, layer) {
            // info pop up
            layer.bindPopup(
                "<h5 style='text-align:center;'>" + new Date(feature.properties.time) +
                "</h5><hr><h5 style='text-align:center;'>" + feature.properties.title + "</h5>");
        }
    }).addTo(earthquakeLayer);
});

// colores
function magColor(mag) {
    return mag > 8 ? "#800026":
            mag > 7 ? "#bd0026":
            mag > 6 ? "#e31a1c":
            mag > 5 ? "#fc4e2a":
            mag > 4 ? "#fd8d3c":
            mag > 3 ? "#feb24c":
            mag > 2 ? "#fed976":
            mag > 1 ? "#ffeda0":
                      "#ffffcc";
};

function createMap() {
    var street = L.tileLayer("https://api.mapbox.com/styles/v1/cherngywh/cjfokxy6v0s782rpc1bvu8tlz/tiles/256/{z}/{x}/{y}?" +
        "access_token=pk.eyJ1IjoiY2hlcm5neXdoIiwiYSI6ImNqZXZvcGhhYTcxdm4ycm83bjY1bnV3amgifQ.MOA-PIHTOV90Ql8_Tg2bvQ");
    
    mymap = L.map('map', {
        center: [30, 0],
        zoom: 2,
        layers: [street, earthquakeLayer]
    })


    var legend = L.control({position: "bottomright"});

    legend.onAdd = function(map) {
        var div = L.DomUtil.create("div", "info legend"),
            grades = [0, 1, 2, 3, 4, 5, 6, 7, 8],
            labels =[];
            
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
            '<i style="background:' + magColor(grades[i]) + '"></i> ' +
            grades[i] + (grades[i+1] ? '&ndash;' + grades[i+1] + '<br>' : '+');
        }
        return div;
    };
    legend.addTo(mymap);
};

// ccrear mapa
createMap();



