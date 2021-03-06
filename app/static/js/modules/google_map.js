export async function refreshMap(latitude, longitude, place) {
    let map;
    let marker;
    let lati = latitude;
    let long = longitude;
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: lati, lng: long},
      zoom: 15,
    });

    marker = new google.maps.Marker({
      position: { lat: lati, lng: long}, 
      map: map,
    })

    google.maps.event.addListener(marker, "click", function() {
      open(`https://maps.google.com/maps?hl=fr&q=${place}`, Window)
    });
  };
  