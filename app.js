require("dotenv").config();

const PythonShell = require("python-shell");
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const app = express();

// Switch states held in memory
const switches = [];

// Read state from saveState.json, populate switches array
var readableStream = fs.createReadStream("saveState.json");
var data = "";

readableStream.on("data", function (chunk) {
    data += chunk;
});

readableStream.on("end", function () {
    var parsed = JSON.parse(data);

    for (i = 0; i < parsed.switches.length; i++) {
        switches.push(new Switch(parsed.switches[i]));
    }
});

// Switch Model
// Expects an object:{
// id:"sw" + number,
// state: "on" or "off",
// name: any name you want to display. Defaults to "switch"
// }
class Switch {
    constructor(switchValues) {
        this.id = switchValues.id || "doorx";
        this.state = switchValues.state || "off";
        this.name = switchValues.name || "door";
        this.toggle = function () {
            if (this.state === "on") {
                this.setState("open");
            }
            else {
                this.setState("off");
            }
        };
        this.setState = function (state) {
            var str = state === "on" ? onString(this.id[2]) : offString(this.id[2]);
            PythonShell.run(str, function (err) {
                if (!process.env.DEV) {
                    if (err)
                        throw err;
                }
            });
            this.state = state;
        };
        // Invokes setState on init to set the switch to its last recalled state.
        this.setState(this.state);
    }
}

// needed due to a quirk with PythonShell
function onString(number) {
    return "./public/python/door_open.py";
}

function offString(number) {
    return "./public/python/door_close.py";
}

// Switch Lookup
function getSwitch(string) {
    return switches.filter(function (element) {
        return element.id === string;
    })[0];
}

// Updates saveState.json
function saveState() {
    var formattedState = {
        switches: switches
    };
    fs.writeFile("./saveState.json", JSON.stringify(formattedState), function (
        err
    ) {
        if (err) {
            console.error("ERROR! CHECK STACTRACE!")
            console.error(err);
        } else {
            let date = new Date();
            console.log(`
${date.toLocaleDateString()} ${date.toLocaleTimeString()} State has been updated
New state: ${JSON.stringify(formattedState)}
`);
        }
    });
}

//Server Configuration
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + "/public"));

// If you have a frontend, drop it in the Public folder with an entry point of index.html
app.get("/", function (req, res) {
    res.sendFile("index");
});

// Switch Routes for API
app.get("/api/switches", function (req, res) {
    res.send(switches);
});

app.get("/api/switches/:id", function (req, res) {
    var found = getSwitch(req.params.id);
    res.json(found);
});

app.post("/api/switches/:id", function (req, res) {
    // For now, uses a simple password query in the url string.
    // Example: POST to localhost:8000/API/switches/sw1?password=test
    if (req.query.password === process.env.PASS) {
        try {
            var foundSwitch = getSwitch(req.params.id);
            
            // Optional On / Off command. If not included, defaults to a toggle.
            if (!(req.query.command === "open" || req.query.command === "close")) {
                foundSwitch.toggle();
            } else {
                foundSwitch.setState(req.query.command);
            }
    
            saveState();
            console.log("postSwitch " + JSON.stringify(foundSwitch));
            res.json(foundSwitch);
            
        } catch (error) {
            console.error("ERROR! CHECK STACKTRACE!")
            console.error(error)
        }

    } else {
        console.log("ERROR! AUTHENTICATION FAILURE");
        res.send("CHECK AUTHENTICATION METHODS");
    }
});

app.listen(process.env.PORT, function () {
    console.log("Doorknob service started!")
    console.log("Listening on port " + process.env.PORT);
});
