let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 48.85837009999999, lng: 2.2944813},
      zoom: 15,
    });
  }