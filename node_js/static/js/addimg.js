function addImg(){
    var newP = document.createElement('p');
    var text = document.createTextNode(
        "은은하고 다채로운 꽃향, 망고, 체리 달달함이 입안 가득...."
    )
    newP.appendChild(text);

    var newImg = document.createElement('img');
    var src = document.createAttribute('src');
    var alt = document.createAttribute('alt');
    src.value = "static/images/coffee-blue.jpg";
    alt.value = "커피 이미지"

    newImg.setAttributeNode(src);
    newImg.setAttributeNode(alt);

    document.getElementById("info").appendChild(newP);
    document.getElementById("info").appendChild(newImg);
}
        // 태그 요소 - createElement()
        // 태그 속성 - createAttribute() -> 설정 : setAttributeNode()