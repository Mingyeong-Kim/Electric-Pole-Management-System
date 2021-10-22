// 기울기 센서 함수1
// 데이터 받기 
msg.payload=msg.payload.d.inclination;

global.set("inclination",msg.payload);
return msg;

// 기울기 센서 함수2
// 데이터 처리 및 상태판단
var inc = global.get("inclination");
var state = "on";
     //미래  현재
     
if( (inc == "0") ){
    state = "unblock";
}
else{
    state="block";
}



msg.payload = inc;
global.set("inc_state",state);

return msg;
