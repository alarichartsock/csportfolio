function postContact(title,description) {
    var req = new XMLHttpRequest();
    req.open("POST", "http://httpbin.org/post", false);
    req.setRequestHeader('Content-Type', 'application/json');
    req.send('{"title":"' + title + '"},{"description":"'+ description + '"}');
    console.log(JSON.parse(req.responseText));

    var body = document.getElementsByTagName("body")[0];
    var h3 = document.createElement("h3");
    var response = JSON.parse(req.responseText);
    var cellText = document.createTextNode(response.data);
    h3.appendChild(cellText);
    body.appendChild(h3);
}