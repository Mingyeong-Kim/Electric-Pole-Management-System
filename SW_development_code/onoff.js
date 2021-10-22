//기울기, 충격 감지에 따른 전원 스위치 on/off 구현 함수

// 함수1
// 기울기, 충격 감지에 따른 전원 스위치 off 구현 함수
var blockd1 = global.get("impact_block"); // 충격감지 
var blockd2 = global.get("inc_state");  // 기울기

var evt1={'d':{}};

if(blockd1 == "block" || blockd2 == "block"){
    evt1.d.switch_state='off';
}else{
    evt1.d.switch_state='on';
}

return {payload:JSON.stringify(evt1)};

// 함수2
// 기울기, 충격 감지에 따른 전원 스위치 on/off 상태판단 함수
msg.payload=msg.payload.d.switch_state ==='on' ? true : false;
return msg;

// 함수3
// 기울기, 충격 감지에 따른 전원 스위치 on/off 모니터링 알고리즘
var evt1={'d':{}};
if(msg.payload===true){
    evt1.d.switch_state='on';
}else{
    evt1.d.switch_state='off';
}
return {payload:JSON.stringify(evt1)};


