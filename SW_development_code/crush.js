// 충격 감지 센서 함수1
// 데이터 받기
msg.payload=msg.payload.d.sense_impact;

global.set("sense_impact",msg.payload);
return msg;

// 충격 감지 센서 함수2
// 데이터 처리, 상태판단
msg.payload=msg.payload.d.sense_impact;

global.set("sense_impact",msg.payload);
return msg;



