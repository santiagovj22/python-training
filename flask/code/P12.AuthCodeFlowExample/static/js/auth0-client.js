function loginViaOIDC() {
  oidcURI = "https://ixjala.auth0.com/authorize?response_type=code"
    + "&scope=openid email"
    + "&client_id=sJXY8ISV8FMuADxUQelw4WO2rEgP8ELM"
    + "&state=someState"
    + "&redirect_uri=http://localhost:5000/auth"
    + "&response_mode=query";

    location.href = oidcURI;
}

function callAuthApi(token, onData ) {
  const xhr = new XMLHttpRequest();

  xhr.open('POST', 'http://localhost:5000/api/v1/authLogin?code=' + token);

  // set response format
  xhr.responseType = 'json';

  xhr.send();

  xhr.onload = () => {
      // get JSON response
      const json = xhr.response;
      onData(json)
  }
}

function callProtectedApi(token, onData) {
  const xhr = new XMLHttpRequest();

  xhr.open('GET', 'http://localhost:5000/api/v1/userInfo');
  xhr.setRequestHeader("Authorization", "Bearer " + token);

  // set response format
  xhr.responseType = 'json';

  xhr.send();

  xhr.onload = () => {
      // get JSON response
      const json = xhr.response;
      onData(json)
  }
}