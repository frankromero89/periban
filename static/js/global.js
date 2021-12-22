$(document).ready(async function() {
    const input = document.getElementById("form-places");
    const loader = document.getElementsByClassName("spinner-loading");
    var alertPlaceholder = document.getElementById('liveAlertPlaceholder');
    var containerMap = document.getElementById('mapEvidence');

    if (document.body.contains(document.getElementById('form-staff'))){
        getCurrentLocation()
    }

    if(document.body.contains(containerMap)){
        var locString = containerMap.getAttribute('meta');
        var locationArray = locString.split(',')
        var position = { lat: parseFloat(locationArray[0]), lng: parseFloat(locationArray[1]) }
        var map = new google.maps.Map(document.getElementById("mapEvidence"), {
            center: position,
            zoom: 20,
        });
        infoWindow = new google.maps.InfoWindow();
        new google.maps.Marker({
            position: position,
            map,
            title: "Ubicación guardada",
        });
    }

    const options = {
        componentRestrictions: { country: "mx" },
        fields: ["address_components"],
    }
    const autocomplete = new google.maps.places.Autocomplete(input, options);
    autocomplete.addListener("place_changed", function(){
        $(loader).css('display', 'block');
        var place = autocomplete.getPlace();
        var neiborhood = null;
        place.address_components.map(function(element){
            if ($.inArray("sublocality", element.types) == 1) {
                neiborhood = element.short_name.toLowerCase();
            }
        })
        searchAddress(neiborhood)
    })

    const toAddress = document.querySelector('#toAddress');
    const mapContainer = document.querySelector('#google-map-container');
    $(toAddress).click(function() {
        $(mapContainer).css('display', 'block');
    });
    $(mapContainer).click(function() {
        $(alertPlaceholder).css('display', 'none');
    });
    actionPig();
    showMenuMobile();
});


function alert(message, type) {
    var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
    $(alertPlaceholder).css('display', 'block');
    var wrapper = document.createElement('div')
    wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
  
    alertPlaceholder.append(wrapper)
}

function searchAddress(neiborhood){
    const loader = document.getElementsByClassName("spinner-loading");
    $.getJSON('../static/js/sucursales.json',function(data){
        var ajusco = data.ajusco;
        var aztecas = data.aztecas;
        var coapa = data.coapa;
        var ayuntamiento = data.ayuntamiento;
        var marina = data.marina;
        var roma = data.roma;

        if ($.inArray(neiborhood, ajusco) >= 0) {
            window.location.replace(window.location.origin + "/cobertura?sucursal=ajusco")
        }else if ($.inArray(neiborhood, aztecas) >= 0) {
            window.location.replace(window.location.origin + "/cobertura?sucursal=aztecas")
        }else if ($.inArray(neiborhood, coapa) >= 0) {
            window.location.replace(window.location.origin + "/cobertura?sucursal=coapa")
        }else if ($.inArray(neiborhood, ayuntamiento) >= 0) {
            window.location.replace(window.location.origin + "/cobertura?sucursal=ayuntamiento")
        }else if ($.inArray(neiborhood, marina) >= 0) {
            window.location.replace(window.location.origin + "/cobertura?sucursal=marina")
        }else if ($.inArray(neiborhood, roma) >= 0) {
                window.location.replace(window.location.origin + "/cobertura?sucursal=roma")
        }else {
            alert('Lo sentimos por el momento no tenemos cobertura en esa dirección, haz tu pedido y recoge en sucursal.', 'warning')
            $(loader).css('display', 'none');
        }
    });
}

function actionPig(){
    const pigChat = document.getElementById("pig-chat");
    $(pigChat).click(function() {
        tidioChatApi.open();
        $(pigChat).css('display', 'none');
    });
    function onTidioChatClose(){
        console.log('is closed');
        $(pigChat).css('display', 'block');
    }
    // if (window.tidioChatApi) {
    if (window.tidioChatApi) {
        window.tidioChatApi.on("close", onTidioChatClose);
    } else {
        document.addEventListener("tidioChat-close", onTidioChatClose);
    }
}

function showMenuMobile(){
    var menuIcon = document.getElementById("ic-mob-menu");
    var menuMobile = document.getElementById("mobile-navbar");
    var closeMenu = document.getElementById("icon-close-container");
    $(menuIcon).on("click", function(e){
        e.preventDefault();
        $(menuMobile).addClass("show-menu");
    })
    $(closeMenu).on("click", function(e){
        e.preventDefault();
        $(menuMobile).removeClass("show-menu");
    })
}

// const getCurrentLocation = new Promise((resolve, reject) => {
//     if (navigator.geolocation) {
//         resolve('yeah')
//         navigator.geolocation.getCurrentPosition(
//           resolve((position) => {
//             const pos = {
//               lat: position.coords.latitude,
//               lng: position.coords.longitude,
//             };
//             position = pos;
//           }),
//           () => {
//             handleLocationError(true, infoWindow, map.getCenter());
//           }
//         );
//     } else {
//         // Browser doesn't support Geolocation
//         handleLocationError(false, infoWindow, map.getCenter());
//     }
// });


function getCurrentLocation(){
    var inputLoc = document.getElementById('inputLocation')
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            console.log('pos', pos);
            inputLoc.value = `${pos.lat},${pos.lng}`;
          },
          () => {
            handleLocationError(true, infoWindow, map.getCenter());
          }
        );
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}