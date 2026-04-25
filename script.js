var appVolumesButton = document.getElementById("appVolumesButton");
var audioDevicesButton = document.getElementById("audioDevicesButton");


//On application start load content.
//getApplicationVolumes();


function onAppVolumesButtonClick(){
    try{
        //active class means it's selected
        appVolumesButton.setAttribute("disabled");
        appVolumesButton.className = "active"
        //inactive class means it can be selected
        audioDevicesButton.removeAttribute("disabled");
        audioDevicesButton.className = "inactive"
    }
    catch{
        throw new Error("Failed to set attributes/classes");
    }

    getApplicationVolumes();    
}


function onAudioDevicesButtonClick(){
    try{
        //active class means it's selected
        audioDevicesButton.setAttribute("disabled");
        audioDevicesButton.className = "active"
        //inactive class means it can be selected
        appVolumesButton.removeAttribute("disabled");
        appVolumesButton.className = "inactive"
    }
    catch{
        throw new Error("Failed to set attributes/classes");
    }
}

async function sendVolumeChange(name,volume) {
    const response = fetch('http://localhost:8000',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                name: name,
                volume: volume
            }
        )
    });

    const result =  await response.json();
    console.log(result)
}

async function sendDeviceChnage(name) {
    const response = fetch('http://localhost:8000',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                name: name
            }
        )
    });

    const result =  await response.json();
    console.log(result)
}

async function getApplicationVolumes() {
    //Asks the server for application volumes
    try{
        const response = await fetch('http://localhost:8000/apps');

        if(!response.ok){
            throw new Error('HTTP error! status ${response.status}');
        }

        const data = await response.json();
        //use data
    }
    catch{
        console.error("Faild to fetch App Volumes:",error );
    }
}

async function getDevices() {
    //Asks the server for list of audio devices
    try{
        const response = await fetch('http://localhost:8000/devices');

        if(!response.ok){
            throw new Error('HTTP error! status ${response.status}');
        }

        const data = await response.json();
        //use data
    }
    catch{
        console.error("Faild to fetch Devices:",error );
    }
}

