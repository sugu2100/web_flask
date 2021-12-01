//커피잔 바꾸기
pic = document.getElementById('pic')
//addEventLister()의 실행 함수로 구현
pic.addEventListener("mouseover", function(){
  pic.src = "../static/images/coffee-pink.jpg";
});

pic.addEventListener("mouseout", function(){
  pic.src = "../static/images/coffee-blue.jpg";
});

//디지털 시계
setInterval(myWatch, 1000);

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString();
    document.getElementById("demo").innerHTML = now;
}
