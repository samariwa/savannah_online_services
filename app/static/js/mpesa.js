let headers = new Headers();
let access_token = "";
headers.append("Authorization", "Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==");

function get_token(headers) {
    fetch("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials", { headers })
        .then(response => response.text())
        .then(function (result) {
            access_token = result['access_token'];
            alert("Success getting token")
        })
        .catch(error => alert(error));
}
