<template>
  <div class="home">
    <Header></Header>

    <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios';

//const API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json';
//const data = axios.get(API_URL).then(response => response.data);

axios.get('https://reqres.in/api/users?page=2').then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.log(error);
});

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
  name: 'home',
  components: {
    Header,
    Footer
  }
}
</script>
