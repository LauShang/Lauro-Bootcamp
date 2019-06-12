// from data.js
var tableData = data;

d3.select("tbody").selectAll("tr")
    .data(data)
    .enter()
    .append("tr")
    .html(function(d){
        return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td><td>${d.comments}`;
});

//boton
 
var button = d3.select('#filter-btn');

function click(){
    d3.event.preventDefault();
    d3.selectAll("tr").remove();
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    function date_filter(x){
        return x.datetime === inputValue;
    }
    var dates = data.filter(date_filter);
    if(inputValue===""){ //si el filtro está vacio regresa todos los resultados
        d3.select("tbody").selectAll("tr")
            .data(data)
            .enter()
            .append("tr")
            .html(function(d){
                return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td><td>${d.comments}`;
        });
    }else{
        d3.select("tbody").selectAll("tr")
    .data(dates)
    .enter()
    .append("tr")
    .html(function(d){
        return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td><td>${d.comments}`;
    })};
    
};

button.on('click', click); //trigger

