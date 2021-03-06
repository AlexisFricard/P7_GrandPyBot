import {refreshMap} from './google_map.js'

let u = document.getElementById('dial_area')

export async function display_message(sender_datas, msg) {
    
    let answer

    if (sender_datas.role == "user") { // to display user msg // Call before fetch
        answer = `<p style="margin: 0;">${msg}<p>`;
        display_it(sender_datas, answer)
    }
    else if (sender_datas.role == "robot") {

        if (msg == 0) { // to display loading icon // call before fetch
            let loading_icon = `<img src='static/img/loading.gif' class="gif">`;
            sender_datas.role = "robot_load"
            display_it(sender_datas, loading_icon)
            sender_datas.role = "robot"
        };

        if (msg.greetings == 1) { // analyse if grandpy need to responde by greetings

            answer = "Bien le bonjour 👋 ! ";
            let r = document.getElementById('robot_load');
            if (r !== null) {
                r.innerHTML = answer; // del loading gif replace greeting msg 
                r.setAttribute("id" , "robot");
            }
            else {
                display_it(sender_datas, answer);
            }
            msg.greetings = 0; // pass greetings to 0 

        };

        if (msg.greetings == 0) { // If greetings done or if they are not

            let rb = document.getElementById('robot_load');
            if (rb !== null) {
                rb.parentElement.remove()   // to remove loading gif
            }

            let datas = JSON.parse(JSON.stringify(msg));
            // if there are map_datas -> display adresse && refresh map / add marker
            if (datas.map_data !== null){   // "null" is to unfound results 
                if (datas.map_data != 0) {  // and "0" if user just say "Hi"

                    answer = `Bien sûr mon poussin ! La voici :</br>
                              </br>
                              ${datas.map_data["place"]}</br>
                              ${datas.map_data["address"]}`;

                    display_it(sender_datas, answer); // display map_data
                    refreshMap(datas.map_data.coordinates["lat"],datas.map_data.coordinates["lng"],
                               datas.map_data["place"]);

                    // if there are map data, and also anecdote
                    if (datas.anecdote !== null) {
                        if (datas.anecdote != 0) { 
                            answer = `Mais t'ai-je déjà raconté l'histoire sur de ce quartier qui m'a 
                            vu en culottes courtes ?</br></br> ${datas.anecdote}`;
                            display_it(sender_datas, answer); // display anecdote
                        };
                    };
                };
            }   
            else { // if there not found response display error_msg
                answer = datas.anecdote;
                display_it(sender_datas, answer)
            };
        };
    };
};
function display_it(sender_datas, response) {

    let container_html = `
        <div id='${sender_datas.role}_box'>\
            <div id="${sender_datas.role}">\
                ${response}
            </div>\
            <div id='emot_talker'>${sender_datas.icon}</div>\
        </div>
        `;
    
        u.insertAdjacentHTML("beforeend", container_html);
        u.lastElementChild.scrollIntoView({behavior: "smooth", block: "end", inline: "end"});
};
        // 🏘️🚩👴 
