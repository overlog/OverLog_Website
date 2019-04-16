<template>
  <div class="bg">
    <p class="py-5"></p>
    <img id="bg" src="@/assets/homepagebg.png" class="img-fluid" alt="Responsive image">
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
.transparent {
  background-color: white !important;
  opacity: 0.65;
  border-color: transparent !important;
}
.bg {
  margin-top: -250px;
  opacity: 0.99;
  margin-bottom: -24px;
}
</style>





