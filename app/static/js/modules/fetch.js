import {display_message} from './display.js'

let user_data = {role: "user", icon:'🧐'};
let robot_data = {role: "robot", icon:'🤖'};

export async function SendRequest(msg) {

    display_message(user_data , msg); //display user message
    display_message(robot_data, 0) // display gif loading

    let msg_json = `{"msg": "${msg}"}`;

    let url = '/grandpy/';
    let mode = "POST";
    
    fetch(url, {method: mode, body: msg_json})
    .then(response => response.json())
    .then(response => display_message(robot_data, response))
}