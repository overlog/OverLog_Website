<template>
  <div class="bg">
    <p class="py-5 text-center">
      This example creates a full page background image.
      Try to resize the browser window to see how it always will cover the full screen (when scrolled to top),
      and that it scales nicely on all screen sizes.
    </p>
  </div>
</template>

<script>
// @ is an alias to /src

//import axios from 'axios';
//const API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json';
//const data = axios.get(API_URL).then(response => response.data);

/*axios.get('https://reqres.in/api/users?page=2').then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.log(error);
});*/

/*axios.post('http://localhost/test/login.php', {
    username: 'test',
    password: 'user@test'
  })
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error);
  });*/

export default {
  name: "home"
};
</script>

<style scoped>
body {
  width: 100%;
  height: 100%;
}
html {
  height: 100%;
}
.bg {
  /* The image used */
  background-image: url("https://mdbootstrap.com/img/Photos/Horizontal/Nature/full page/img(20).jpg");

  /* Full height */
  height: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>





