function handleAuth0(callback) {
createAuth0Client({
    domain: 'ixjala.auth0.com',
    client_id: 'sJXY8ISV8FMuADxUQelw4WO2rEgP8ELM',
    redirect_uri: 'http://localhost:5000/auth',
    responseType: 'token id_token'
  }).then(auth0 => {
    callback(auth0);
  });
} 

function callApi(token, onData ) {
  const xhr = new XMLHttpRequest();

  xhr.open('POST', 'http://localhost:5000/api/v1/auth');
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