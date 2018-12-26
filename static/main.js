var flag = 1;
function onSendToOrganizers(){
  var urls = [];
  var messages = [];
  var t1, t2;
  t1 = document.getElementById("organizers_url").value;
  t2 = document.getElementById("organizers_message").value;
  // console.log(document.getElementById("members_url"));
  var urls = t1.split("\n");
  var messages = t2.split("######################\n");
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  
  console.log(messages);
  var data = {
    organizers: urls,
    messages: messages,
    email: email,
    password: password
  }
  axios("./sendMessageOrg",{
      method: 'POST',
      data: data,
      headers:{
        'Content-Type': 'application/json'
      },
      json:true
    });
}

function onSendToMembers(){
  var urls;
  var messages;
  var t1, t2;
  t1 = document.getElementById("members_url").value;
  t2 = document.getElementById("members_message").value;
  var urls = t1.split("\n");
  var messages = t2.split("######################\n");
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var data = {
    members: urls,
    messages: messages,
    email: email,
    password: password
  }
  // var messages = t2.split("NEXT MESSAGE");
  axios("./sendMessageMembers",{
      method: 'POST',
      data: data,
      headers:{
        'Content-Type': 'application/json'
      },
      json:true
    })
}


function addMessageOrg(){
  var msg = document.getElementById("organizers_message");
  var btn = document.getElementById("msg_btn1");
  if(msg.disabled==true){
    btn.innerHTML="Close Input";
    msg.placeholder="Please click 'Close' button to close input.";
    msg.disabled=false;
  }
  else{
    btn.innerHTML="Add Message";
    msg.disabled = true;
    msg.placeholder = "Please click 'Add Message' Button for input.";
    msg.value+="\n######################\n";
  }
  console.log(msg.disabled);
}

function addMessageMember(){
  var msg = document.getElementById("members_message");
  var btn = document.getElementById("msg_btn2");
  if(msg.disabled==true){
    btn.innerHTML="Close Input";
    msg.placeholder="Please click 'Close' button to close input.";
    msg.disabled=false;
  }
  else{
    btn.innerHTML="Add Message";
    msg.disabled = true;
    msg.placeholder = "Please click 'Add Message' Button for input.";
    msg.value+="\n######################\n";
  }
  console.log(msg.disabled);
}