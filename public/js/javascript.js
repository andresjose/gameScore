/*
function cambioImagenM(){
    document.body.style.background="url('traerImagenH')";
}
function cambioImagenG(){
    document.body.style.background="url('traerImagenG')";

}
function cambioImagenF(){
    document.body.style.background="url('traerImagenM')";
}*/
function filtrarH (){
    $.ajax({
        url: 'traerCsv',
        dataType: 'text',
        }).done(successFunction);

    function successFunction(data) {
        var nombre =  prompt("nombre a buscar");
        var allRows = data.split(/\r?\n|\r/);
        var table = '<table>';
        for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
            if (singleRow === 0) {
                table += '<thead>';
                table += '<tr>';
            } else {
                table += '<tr>';
            }
            var rowCells = allRows[singleRow].split(',');
            for (var rowCell = 0; rowCell < rowCells.length; rowCell++) {
                if ((nombre == rowCells[rowCell])&&("m"==rowCells[3])){
                    table += '<th>';
                    table += rowCells[0];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[1];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[2];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[3];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[4];
                    table += '</th>';
                    table += '<th>';
                    table += "<img src=static/images/"+rowCells[5]+" width=200px;>";
                    table += '</th>';
                }
            }
            if (singleRow === 0) {
                table += '</tr>';
                table += '</thead>';
                table += '<tbody>';
        } else {
            table += '</tr></tr>';
        }
        }
        table += '</tbody>';
        table += '</table>';
        $('table').append(table);
    }
}
/*
$.ajax({
    url: 'traerCsv',
    dataType: 'text',
    }).done(successFunction);

function successFunction(data) {
    var nombre =  prompt("Please enter your name", "Harry Potter");
    var allRows = data.split(/\r?\n|\r/);
    var table = '<table>';
    for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
        if (singleRow === 0) {
            table += '<thead>';
            table += '<tr>';
        } else {
            table += '<tr>';
        }
        var rowCells = allRows[singleRow].split(',');
        for (var rowCell = 0; rowCell < rowCells.length; rowCell++) {
            if ((nombre == rowCells[rowCell])&&("m"==rowCells[3])){
                table += '<th>';
                table += rowCells[0];
                table += '</th>';
                table += '<th>';
                table += rowCells[1];
                table += '</th>';
                table += '<th>';
                table += rowCells[2];
                table += '</th>';
                table += '<th>';
                table += rowCells[3];
                table += '</th>';
                table += '<th>';
                table += rowCells[4];
                table += '</th>';
                table += '<th>';
                table += "<img src=static/images/"+rowCells[5]+">";
                table += '</th>';
            }
        }
        if (singleRow === 0) {
            table += '</tr>';
            table += '</thead>';
            table += '<tbody>';
    } else {
        table += '</tr></tr>';
    }
    }
    table += '</tbody>';
    table += '</table>';
    $('h2').append(table);
}*/
function filtrarM (){
    $.ajax({
        url: 'traerCsv',
        dataType: 'text',
        }).done(successFunction);

    function successFunction(data) {
        var nombre =  prompt("nombre a buscar");
        var allRows = data.split(/\r?\n|\r/);
        var table = '<table>';
        for (var singleRow = 0; singleRow < allRows.length; singleRow++) {
            if (singleRow === 0) {
                table += '<thead>';
                table += '<tr>';
            } else {
                table += '<tr>';
            }
            var rowCells = allRows[singleRow].split(',');
            for (var rowCell = 0; rowCell < rowCells.length; rowCell++) {
                if ((nombre == rowCells[rowCell])&&("f"==rowCells[3])){
                    table += '<th>';
                    table += rowCells[0];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[1];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[2];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[3];
                    table += '</th>';
                    table += '<th>';
                    table += rowCells[4];
                    table += '</th>';
                    table += '<th>';
                    table += "<img src=static/images/"+rowCells[5]+" width=200px;>";
                    table += '</th>';
                }
            }
            if (singleRow === 0) {
                table += '</tr>';
                table += '</thead>';
                table += '<tbody>';
        } else {
            table += '</tr></tr>';
        }
        }
        table += '</tbody>';
        table += '</table>';
        $('table').append(table);
    }
}