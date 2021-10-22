// 미세먼지 정보 처리 함수
var pm1 = {payload:msg.payload.d.pm1};
var pm2 = {payload:msg.payload.d.pm2};
var pm3 = {payload:msg.payload.d.pm3};

return [pm1,pm2,pm3];
