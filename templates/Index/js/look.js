
function geolocationGPS(){
    if('geolocation' in navigator){
        navigator.geolocation.getCurrentPosition(getParam);
    }else {
        console.log('No ha sido posible la localización.');
    }
}

function getParam(position){

    let p= String(position.coords.latitude); 
    let pL= String(position.coords.longitude);

    $.ajax({
        method:'POST',
        url:'/',
        contentType:'application/json',
        data: JSON.stringify({latitud: p, longitud: pL}),
        succes: function(response){
            console.log('Datos enviados')
        },
        error: function(response){
            console.log('Error al enviar los datos')
        },
    })
    
}
