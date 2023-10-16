var map; // map obj global variable.
var targets;

function init() {
    map = L.map('map', {
        center: [18.112224413095872, 72.468436919390348],
        zoom: 8,
        minZoom: 8,
        maxZoom: 8,
        maxBounds: [
            [18.043790655688225, 72.441131698096311],
            [18.272919555595893, 72.855365096533811]
        ]
    });
    L.tileLayer('assets/tiles/{z}/{x}/{y}.png').addTo(map);

    // creates popup points when map clicked.
    var popup = L.popup();

    function onMapClick(e) {
        // Saving the target for a later use.
        localStorage.setItem("target-latitude", e.latlng.lat.toString().slice(0, 6));
        localStorage.setItem("target-longitude", e.latlng.lng.toString().slice(0, 6));
        popup
            .setLatLng(e.latlng)
            .setContent("Latitude: " + e.latlng.lat.toString().slice(0, 6) + " | Longitude: " + e.latlng.lng.toString().slice(0, 6))
            .openOn(map);
    }

    map.on('click', onMapClick); // adding function to the onMapClick event.

    // Listen to submit event on the target-form itself
    document.getElementById('target-form').addEventListener("submit", function (e) {

        // Prevent form submission which refreshes page
        e.preventDefault();
    });


    // Listen to submit event on the target-form itself
    document.getElementById('update-target-form').addEventListener("submit", function (e) {

        // Prevent form submission which refreshes page
        e.preventDefault();
    });

    getTargets(); // load all targets from backend.
}

function addTargetAbort() {
    // Closing the aborted target.
    map.closePopup();

}

function addTargetEvent() {
    // Initiating chosen target's coordinates.
    document.getElementById("latitudeInput").value = localStorage.getItem("target-latitude");
    document.getElementById("longitudeInput").value = localStorage.getItem("target-longitude");
}

// Initiating the modal with the target's data.
function updateTargetEvent(picked_target) {
    document.getElementById("update-nameInput").value = picked_target.name;
    document.getElementById("update-attackPriorityInput").value = picked_target.attack_priority;
    document.getElementById("update-latitudeInput").value = picked_target.latitude;
    document.getElementById("update-longitudeInput").value = picked_target.longitude;
    document.getElementById("update-enemyOrganizationInput").value = picked_target.enemy_organization;
    document.getElementById("update-targetGoalInput").value = picked_target.target_goal;
    document.getElementById("update-targetIdInput").value = picked_target.target_id;
    document.getElementById("update-wasTargetDestroyedInput").checked = picked_target.was_target_destroyed;
}

function updateTargetSubmit() {
    modalSubmitHandler(true);
}

function addTargetSubmit() {
    modalSubmitHandler(false);
}

function modalSubmitHandler(isUpdate) {
    // Close model.
    bootstrap.Modal.getInstance(document.getElementById(((isUpdate) ? "update" : "add") + '-target-modal')).hide();

    // Creating the Target json. 
    const myform = document.getElementById(((isUpdate) ? "update-" : "") + "target-form");
    let targetDict = {}
    for (var i = 0; i <= myform.length; i++) {
        if (myform.elements[i] == undefined || myform.elements[i].name == "") {
            break;
        }
        var elementObj = myform.elements[i];
        var elementValue = elementObj.value;
        targetDict[elementObj.name] = (elementObj.name == "was_target_destroyed") ? elementObj.checked : ((isNaN(elementValue)) ? elementValue : ((Number.isInteger(elementValue)) ? parseInt(elementValue) : parseFloat(elementValue)));
    }
    // Send request to server.
    console.log(targetDict);
    (isUpdate) ? updateTarget(targetDict) : addTarget(targetDict);
}

// Appling actions to the alerts.
function alertControl(alert_type) {
    var alert_container = document.getElementById("alert-container");
    var alert_obj;
    if (alert_type == "danger") {
        alert_obj = `
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>The request failed! Error returned from server.</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
    } else {
        alert_obj = `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
        The request was successful!
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
    }
    alert_container.innerHTML = alert_obj
}

// Create markers on the map
function applyTargets(targets) {
    for (let i = 0; i < targets.length; i++) {
        L.marker(L.latLng(parseFloat(targets[i].latitude), parseFloat(targets[i].longitude))).addTo(map).on('click', markerClickEvent);
    }
}

// Handle marker click event for update reasons
function markerClickEvent(e) {
    // Find the relevant target.
    var picked_target = targets.filter(target => target.latitude == e.latlng.lat && target.longitude == e.latlng.lng)[0];
    // Lunching the modal.
    var modal = new bootstrap.Modal(document.getElementById('update-target-modal'));
    modal.show();

    updateTargetEvent(picked_target);
}

/****************************************************
 ****************** API CALLS ************************
 *****************************************************/
RECEIVER_IP = "127.0.0.1:8000"
BASE_URL = "http://" + RECEIVER_IP + "/api/targets/"

function updateTarget(target) {
    sendData(BASE_URL + "UpdateTarget/", "PUT", target)
        .then(response => response.text())
        .then(data => {
            console.log(data);
            alertControl("success");
        })
        .catch(err => {
            console.log(err);
            alertControl("danger");
        })
}

function addTarget(target) {
    sendData(BASE_URL + 'AddTarget/', "POST", target).then(data => {
        console.log(data); // JSON data parsed by `data.text()` call
        alertControl("success");
    }).catch(
        error => {
            console.log(error);
            alertControl("danger");
        }
    );
}

function getTargets() {
    const request = new Request(BASE_URL + "AllTargets/", {
        method: "GET",
        //mode: "no-cors",
        cache: "default",
    });
    fetch(request)
        .then(response => response.json())
        .then(data => {
            applyTargets(data); // Creates targets on map.
            targets = data; // Save the targets for later use.
            alertControl("success");
        }).catch(error => {
        console.log(error);
        alertControl("danger");
    });

}

// Reusable http post function
async function sendData(url = '', method = 'POST', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: method, // *GET, POST, PUT, DELETE, etc.
        //mode: 'no-cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            //'Content-Type': 'application/json'
            'Content-Type': 'text/plain',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.text(); // parses JSON response into native JavaScript objects
}

window.onload = init(); // Make the init() function run on window startup.
