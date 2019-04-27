<template>
  <div class="login">
    <!--<div v-if="loggingIn" class="container-loading">
      <img src="@/assets/loading.gif" alt="Loading Icon">
    </div>-->
    <form @submit.prevent="login">
      <input type="username" placeholder="username" v-model="username">
      <input type="password" placeholder="Password"   v-model="password">
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login: function(){
      const username = this.username
      const password = this.password
      this.$store.dispatch('login', { username, password }).then(() => this.$router.push('/'))
    }
  }
}
</script>

<style scoped lang="scss">
  .login {
    border: 1px solid black;
    border-radius: 5px;
    padding: 1.5rem;
    width: 300px;
    margin-left: auto;
    margin-right: auto;
    padding-top: auto;
    position: relative;
    overflow: hidden;
    .container-loading {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: rgba(0,0,0,.3);
      img {
        width: 2rem;
        height: 2rem;
      }
    }
    form {
      display: flex;
      flex-flow: column;
      *:not(:last-child) {
        margin-bottom: 1rem;
      }
      input {
        padding: .5rem;
      }
      button {
        padding: .5rem;
        background-color: lightgray;
        border: 1px solid gray;
        border-radius: 3px;
        cursor: pointer;
        &:hover {
          background-color: lightslategray;
        }
      }
    }
  }
</style>
