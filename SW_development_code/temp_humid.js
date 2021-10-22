//함수1
// 온도 정보처리 함수
msg.payload=msg.payload.d.temp;
return msg;


//함수2
// 습도 정보처리 함수
msg.payload=msg.payload.d.humi;
return msg;
