$(document).ready(function() {
    const input = document.getElementById("form-places");
    const options = {
        componentRestrictions: { country: "mx" },
        fields: ["address_components"],
    }
    
    const autocomplete = new google.maps.places.Autocomplete(input, options);

    autocomplete.addListener("place_changed", function(){
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
    actionPig();
    showMenuMobile();
});

function searchAddress(neiborhood){
    $.getJSON('../static/js/sucursales.json',function(data){
        var ajusco = data.ajusco;
        var aztecas = data.aztecas;
        var coapa = data.coapa;
        var ayuntamiento = data.ayuntamiento;
        
        console.log(coapa);
        console.log(neiborhood);

        if ($.inArray(neiborhood, ajusco) >= 0) {
            console.log('in ajusco')
            window.location.replace(window.location.origin + "/cobertura?sucursal=ajusco")
        }else if ($.inArray(neiborhood, aztecas) >= 0) {
            console.log('in aztecas')
            window.location.replace(window.location.origin + "/cobertura?sucursal=aztecas")
        }else if ($.inArray(neiborhood, coapa) >= 0) {
            console.log('in coapa')
            window.location.replace(window.location.origin + "/cobertura?sucursal=coapa")
        }else if ($.inArray(neiborhood, ayuntamiento) >= 0) {
            console.log('in ayuntamiento')
            window.location.replace(window.location.origin + "/cobertura?sucursal=ayuntamiento")
        }else {
            console.log('not in place')
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