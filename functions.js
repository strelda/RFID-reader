function goToUser(val) {
    if (event.keyCode === 13) {
        window.location.href="user.html";
        handleSubmit();
    }
};
function handleSubmit () {
    const name = document.getElementById('name').value;
  
    sessionStorage.setItem("NAME", name);

    return;
};

// id to name translator
const dict = {
    "eer": "OndraTalir"
};

// all user info
const users = {
    "undefined":{
        "name": "INTRUDER",
        "surname": "INTRUDER",
        "age": 0,
        "status": 0,
        "slavery": "",
        "special": "Volám na tě policii ty plesnivče",
        "level": 0
    },
    "OndraTalir":{
        "name": "Ondra",
        "surname": "Talíř",
        "age":25,
        "status": 155,
        "slavery": "21.7 OBĚD, 25.7 SNÍDANĚ",
        "special": "Umí péct líp jak tvoje mamka.",
        "level": 2
    }
};