'use strict';

// Edit these variables to change the optimization:
var start = Date.parse('Wed Jul 05 2016 12:00:00 GMT+0900 (JST)') / 1000;
var PARAMS = {
  origin: {
    lat: 40.8274149,
    lng: 140.6929728,
  },
  start: start,
  end: start + 60 * 60 * 24,
};

// some random nodes to use as an example
var NODES = [
  {lat: 39.73486964892767, lng: 139.6293649320945, start: 1467697045, end: 1467699115, name: "50th birthday party"},
  {lat: 40.823968223951134, lng: 139.61762067292256, start: 1467689974, end: 1467693847, name: "After-party"},
  {lat: 40.76640312356431, lng: 140.5969549498757, start: 1467727524, end: 1467733667, name: "Baby shower"},
  {lat: 39.72981886288512, lng: 139.62713284090557, start: 1467699949, end: 1467706516, name: "Bachelor party"},
  {lat: 40.79447214146912, lng: 140.64505236547743, start: 1467715154, end: 1467720686, name: "Bachelorette party"},
  {lat: 40.759483983193405, lng: 140.60233567679336, start: 1467732349, end: 1467735802, name: "Bastille Day party"},
  {lat: 39.78579618623507, lng: 139.60267466268363, start: 1467746107, end: 1467751459, name: "BBQ party"},
  {lat: 40.78927668873708, lng: 139.63306257641418, start: 1467735520, end: 1467742910, name: "Beach party"},
  {lat: 39.733329783191536, lng: 140.68042911579604, start: 1467725323, end: 1467732084, name: "Birthday party"},
  {lat: 40.779972796686955, lng: 139.67611906112953, start: 1467697208, end: 1467707146, name: "Block party"},
  {lat: 40.77643622443633, lng: 140.6163782337719, start: 1467731544, end: 1467737886, name: "Board game party"},
  {lat: 39.7318087999479, lng: 139.68917619669136, start: 1467689024, end: 1467695694, name: "Bonfire"},
  {lat: 40.8071539321502, lng: 139.66819987663342, start: 1467723149, end: 1467731285, name: "Bridal shower"},
  {lat: 39.74764509662943, lng: 139.64574226247848, start: 1467703578, end: 1467706052, name: "Canada Day party"},
  {lat: 39.746715296229404, lng: 139.69018912252542, start: 1467718347, end: 1467726752, name: "Charity dinner"},
  {lat: 39.73430064369441, lng: 140.63910945853954, start: 1467695462, end: 1467699948, name: "Christmas party"},
  {lat: 40.731327489175584, lng: 140.675080355556, start: 1467734553, end: 1467744627, name: "Cinco de Mayo party"},
  {lat: 40.77501399890906, lng: 140.65883063729248, start: 1467714116, end: 1467724206, name: "Cocktail party"},
  {lat: 39.77829130949617, lng: 139.6810578938282, start: 1467718084, end: 1467723516, name: "Costume party"},
  {lat: 39.789639035001436, lng: 139.65029464314475, start: 1467693944, end: 1467699023, name: "Cuddle party"},
  {lat: 40.72777283817424, lng: 140.64512792500744, start: 1467761277, end: 1467765156, name: "Dance Party"},
  {lat: 39.752879684718415, lng: 140.68038019381805, start: 1467745270, end: 1467755601, name: "Dinner party"},
  {lat: 39.7877026616801, lng: 140.63070705684163, start: 1467750126, end: 1467758610, name: "Diwali party"},
  {lat: 39.81524604059255, lng: 140.67298180804826, start: 1467748015, end: 1467754136, name: "Easter party"},
  {lat: 40.8046452820544, lng: 139.67559339114408, start: 1467760484, end: 1467763048, name: "Farewell party"},
  {lat: 39.809367101201524, lng: 139.63400222412625, start: 1467737368, end: 1467742539, name: "Fourth of July party"},
  {lat: 39.76971988463324, lng: 139.64407225520608, start: 1467762890, end: 1467768875, name: "Garden party"},
  {lat: 39.76471323348467, lng: 139.65256357809864, start: 1467758866, end: 1467762849, name: "Graduation Party"},
  {lat: 40.76439275312668, lng: 140.63861317602675, start: 1467717283, end: 1467727094, name: "Graduation Party"},
  {lat: 39.824229396347924, lng: 140.67389567202093, start: 1467693478, end: 1467700935, name: "Halloween party"},
  {lat: 39.799823913287646, lng: 139.6207941728825, start: 1467696193, end: 1467705576, name: "Hanukkah party"},
  {lat: 39.746763084307744, lng: 140.67364151742845, start: 1467710752, end: 1467714101, name: "Housewarming party"},
  {lat: 39.791609254280274, lng: 139.65546072401085, start: 1467710669, end: 1467717378, name: "Karaoke party"},
  {lat: 39.766220653395436, lng: 139.64108642169137, start: 1467757647, end: 1467761140, name: "Kegger"},
  {lat: 39.813786499140015, lng: 140.60170918011858, start: 1467738426, end: 1467741495, name: "LAN party"},
  {lat: 39.76915860087753, lng: 139.65407892756983, start: 1467700295, end: 1467710510, name: "Luau"},
  {lat: 39.76070622015804, lng: 139.6896763100016, start: 1467761293, end: 1467763461, name: "Mardi Gras party"},
  {lat: 39.80780937688331, lng: 140.62886171149546, start: 1467708932, end: 1467712765, name: "Masquerade ball"},
  {lat: 40.81983238845703, lng: 140.6620552609254, start: 1467711839, end: 1467717140, name: "Murder mystery party"},
  {lat: 40.783547055896975, lng: 139.59893416178653, start: 1467724345, end: 1467729263, name: "Naked party"},
  {lat: 39.801520717360845, lng: 140.59487439650417, start: 1467768504, end: 1467778374, name: "New Year’s Eve party"},
  {lat: 40.77298835083865, lng: 140.6801386020633, start: 1467715916, end: 1467720116, name: "Passover party"},
  {lat: 39.750567968528316, lng: 140.68707253895946, start: 1467764694, end: 1467766676, name: "Pizza party"},
  {lat: 40.736056331769745, lng: 139.6700714896672, start: 1467766657, end: 1467771572, name: "Pool party"},
  {lat: 39.79584303283539, lng: 140.63455818654245, start: 1467747046, end: 1467751096, name: "Pre-party"},
  {lat: 40.75850882284175, lng: 140.60643261334354, start: 1467711720, end: 1467719230, name: "Prom"},
  {lat: 40.74264530239636, lng: 139.60413092571022, start: 1467765139, end: 1467770245, name: "Rave"},
  {lat: 39.80053763671365, lng: 140.59924968977356, start: 1467767309, end: 1467773152, name: "Reception"},
  {lat: 40.752545912731755, lng: 139.62084420647727, start: 1467742030, end: 1467752386, name: "Saint Patrick’s Day party"},
  {lat: 40.81521053479159, lng: 140.66147692798924, start: 1467715645, end: 1467724379, name: "Singles mixer"},
  {lat: 40.75889826841898, lng: 139.68313744812792, start: 1467751765, end: 1467757407, name: "Sleepover party"},
  {lat: 39.821159513971764, lng: 140.6832681266394, start: 1467710541, end: 1467716520, name: "Super Bowl party"},
  {lat: 39.75284124598853, lng: 139.69241719242973, start: 1467735006, end: 1467737226, name: "Surprise party"},
  {lat: 40.760330418693016, lng: 140.60792329894878, start: 1467764022, end: 1467769019, name: "Tea party"},
  {lat: 40.764979940294964, lng: 140.63310035037435, start: 1467695992, end: 1467705044, name: "Toga party"},
  {lat: 39.79695282866181, lng: 139.59369636337064, start: 1467725322, end: 1467730547, name: "Tupperware party"},
  {lat: 39.80443881323025, lng: 139.6844437492467, start: 1467710300, end: 1467715373, name: "Ugly sweater party"},
  {lat: 40.759750378316475, lng: 140.6362277308202, start: 1467689618, end: 1467697758, name: "Valentine’s Day Party"},
  {lat: 39.823095303915345, lng: 139.64119836963843, start: 1467727875, end: 1467737439, name: "Viewing party"},
  {lat: 40.73615222876498, lng: 140.6168878715166, start: 1467718126, end: 1467724917, name: "Wedding reception"},
  {lat: 39.748925335705266, lng: 139.68989391317305, start: 1467690670, end: 1467695092, name: "Welcome party"},
];

function Map() {
  this.el = document.createElement('div');
  this.el.className = 'map';
  this.map = new google.maps.Map(this.el, {
    zoom: 14,
    center: PARAMS.origin,
  });
}

Map.prototype.render = function(data) {
  var nodes = data.map(function(result) {
    return result.node;
  });

  var bounds = new google.maps.LatLngBounds();
  var path = [];
  nodes.forEach(function(node, i) {
    var position = new google.maps.LatLng(
      node.lat,
      node.lng
    );
    bounds.extend(position);
    path.push(position);

    var color = 'red';
    if (i == 0 || i == nodes.length - 1) {
      color = 'black';
    }

    var marker = new google.maps.Marker({
      position: position,
      map: this.map,
      icon: {
        path: google.maps.SymbolPath.CIRCLE,
        scale: 6,
        fillColor: color,
        fillOpacity: 1,
        strokeWeight: 0,
      },
    });
  }.bind(this));
  this.map.fitBounds(bounds);

  var polyline = new google.maps.Polyline({
    path: path,
    strokeColor: '#0000FF',
    strokeOpacity: 1.0,
    strokeWeight: 2,
    map: this.map
  });
};

function shuffle(a) {
  var j;
  var x;
  var i;
  for (i = a.length; i; i -= 1) {
    j = Math.floor(Math.random() * i);
    x = a[i - 1];
    a[i - 1] = a[j];
    a[j] = x;
  }
}

function pad(str) {
  return ('00000' + str).slice(-2);
}

function timestamp(date) {
  return pad(date.getHours()) + ':' + pad(date.getMinutes());
}

// Generates a div with start/end times and links pointing to
// each event in the result list. Really basic for now. Later
// I'd like to link them to points on the map on hover.
function renderResults(results) {
  var div = document.createElement('div');

  for (var i = 0; i < results.length; i++) {
    var res = results[i];
    var start = new Date(res.start * 1000);
    var end = new Date(res.end * 1000);
    var name = '';
    var name = res.node.name;
    if (i == 0 || i == results.length - 1) {
      name = 'Home';
    }
    var row = document.createElement('div');
    var time = document.createElement('span');
    time.innerText = '' + timestamp(start) + '-' + timestamp(end) + '\t';
    row.appendChild(time);
    var link = document.createElement('a');
    link.target = '_blank';
    link.href = 'http://maps.google.com/?q=' + res.node.lat + ',' + res.node.lng;
    link.innerText = name;
    row.appendChild(link);

    div.appendChild(row);
  }
  ;

  return div;
}

// Send a set of nodes to the Python backend and
// return the computed TSP route.
function computeRoute(nodes) {
  return fetch('/routes', {
    'method': 'POST',
    'headers': {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    'body': JSON.stringify({
      'nodes': nodes,
      'startTime': PARAMS.start,
      'endTime': PARAMS.end,
      'start': PARAMS.origin,
    }),
  })
    .then(function(resp) {
      if (resp.status < 200 || resp.status >= 300) {
        return resp.text().then(function(errText) {
          var msg = 'bad response (' + resp.status + '): ' + errText;
          return Promise.reject(msg)
        });
      }

      return resp.json();
    });
}

function initMap() {
  var map = new Map();
  document.getElementById('main').appendChild(map.el);

  var $sidebar = document.getElementById('sidebar');
  $sidebar.innerText = 'Loading. This\'ll take a while...';
  
  computeRoute(NODES).then(function(body) {
    var results = body.results;

    $sidebar.innerHTML = '';
    var row = renderResults(results);
    $sidebar.appendChild(row);

    map.render(results);

  }, function(err) {
    $sidebar.innerText = 'Server error:\n' + err;

  });
}
;
