var flag = 1;
function onSendToOrganizers(){
  var urls = [];
  var messages = [];
  var timespaces = [];
  var t1, t2;
  t1 = document.getElementById("organizers_url").value;
  t2 = document.getElementById("organizers_message").value;
  // console.log(document.getElementById("members_url"));
  var urls = t1.split("\n");
  var messages = t2.split("######################\n");
  messages.forEach(function(message,index,theArray){
    var temp = message.split("**********************\n");
    theArray[index] = temp[0];
    timespaces.push(temp[1]);
    if(temp[0]==''){
      messages.pop();
      timespaces.pop();
    }
  });
  // console.log("*********");
  // console.log(messages);
  // console.log("***********");
  // console.log(timespaces);
  // console.log("***********");
  var sendingtime = [];
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  
  // console.log(messages);
  var data = {
    organizers: urls,
    messages: messages,
    timespaces: timespaces,
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
  var urls = [];
  var messages = [];
  var timespaces = [];
  var t1, t2;
  t1 = document.getElementById("members_url").value;
  t2 = document.getElementById("members_message").value;
  var urls = t1.split("\n");
  var messages = t2.split("######################\n");
  messages.forEach(function(message,index,theArray){
    var temp = message.split("**********************\n");
    theArray[index] = temp[0];
    timespaces.push(temp[1]);
    if(temp[0]==''){
      messages.pop();
      timespaces.pop();
    }
  });
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var data = {
    members: urls,
    messages: messages,
    timespaces: timespaces,
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
  var sel = document.getElementById("sel_org");
  if(msg.disabled==true){
    btn.innerHTML="Close Input";
    msg.placeholder="Please click 'Close' button to close input.";
    msg.disabled=false;
    sel.disabled=false;
  }
  else{
    btn.innerHTML="Add Message";
    msg.disabled = true;
    msg.placeholder = "Please click 'Add Message' Button for input.";
    msg.value+="\n**********************\n";
    msg.value+=sel.value;
    msg.value+="\n######################\n";
    sel.disabled=true;
  }
  console.log(msg.disabled);
}

function addMessageMember(){
  var msg = document.getElementById("members_message");
  var btn = document.getElementById("msg_btn2");
  var sel = document.getElementById("sel_member");
  if(msg.disabled==true){
    btn.innerHTML="Close Input";
    msg.placeholder="Please click 'Close' button to close input.";
    msg.disabled=false;
    sel.disabled=false;
  }
  else{
    btn.innerHTML="Add Message";
    msg.disabled = true;
    msg.placeholder = "Please click 'Add Message' Button for input.";
    msg.value+="\n**********************\n";
    msg.value+=sel.value;
    msg.value+="\n######################\n";
    sel.disabled=true;
  }
  console.log(msg.disabled);
}