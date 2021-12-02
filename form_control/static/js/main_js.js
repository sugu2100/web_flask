//이미지 mouse 이벤트
var pic = document.getElementById('pic')
pic.onmouseover = changePic; # 마우스 올리기
pic.onmouseout = originPic;  # 마우스 내리기

function changePic(){
    pic.src = "../static/images/coffee-pink.jpg"
}
//이미지 파일 경로 주의! - static에서 시작함

function originPic(){
    pic.src = "../static/images/coffee-blue.jpg"
}

//디지털 시계
setInterval(myWatch, 1000) # 1초 간격으로 시간 설정

function myWatch(){
    var date = new Date()
    var now = date.toLocaleTimeString()   # 시간을 문자열로 출력
    document.getElementById('display').innerHTML = now
}
