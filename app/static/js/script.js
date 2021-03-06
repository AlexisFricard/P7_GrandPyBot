import {SendRequest} from './modules/fetch.js'

let b = document.getElementById('submit_button');
let t = document.getElementById('user_text');
let i = document.getElementById("input_message");
let l = document.getElementById("logo_box")

function main() {

  b.addEventListener('click', (e) => {

    let msg = document.input_msg.textarea.value;

    if (msg.length < 2 || msg == " ") {
      i.reset();
    }
    else {
      SendRequest(msg);
    }
    i.reset();
  });

  t.addEventListener('keydown', (e) => {
    if(event.keyCode == 13) {
      b.click();
    }
  });

  t.addEventListener('keyup', (e) => {
    if(event.keyCode == 13) {
      i.reset();
    }
  });

  l.addEventListener('click', (e) => {
    window.open("https://github.com/AlexisFricard/P7_GrandPyBot");
  }); 

  l.addEventListener("mouseover", (e) => {
    // on met l'accent sur la cible de mouseover
    l.setAttribute("class", "zoom");
  }); 

  l.addEventListener("mouseout", (e) => {
    // on met l'accent sur la cible de mouseover
    l.setAttribute("class", "logo_box");
  }); 

}

main();