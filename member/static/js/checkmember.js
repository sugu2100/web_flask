function checkMember(){
    var form = document.regform;
    var id = form.memberid.value;
    var pwd1 = form.passwd.value;
    var pwd2 = form.passwd_confirm.value;
    var name = form.name.value;
    var date = form.regdate.value;

    var regExId = /^[0-9A-Za-z]{5}$/; //숫자, 문자 5자

    if(!regExId.test(id)){
        alert("아이디는 5자만 가능합니다.");
        form.memberid.select();
        return false;
    }else if(pwd1.length < 4 || pwd1.length > 8){
        alert("비밀번호는 4자에서 8자까지 가능합니다.")
        form.pwd1.select();
    }else if(pwd1 != pwd2){
        alert("비밀번호를 동일하게 입력해 주세요");
        form.pwd1.select();
        return false;
    }else if(name == ""){
        alert("이름은 필수 입력사항입니다.");
        form.name.focus();
        return false;
    }else if(date == ""){
        alert("등록일은 필수 입력사항입니다.");
        form.name.focus();
        return false;
    }else{
        form.submit();
    }
}