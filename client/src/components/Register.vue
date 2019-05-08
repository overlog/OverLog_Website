<template>
  <div class="register">
    <p v-if="registerError">{{ registerError }}</p>
    <p v-if="registeredSuccessfully">Registration Successful</p>
    <form>
      <input type="text" placeholder="Company Name" v-model="companyName">
      <input type="email" placeholder="E-Mail" v-model="email">
      <input type="password" placeholder="Password" v-model="password">
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import { mapState } from "vuex";
//import { mapActions} from 'vuex'

export default {
  name: "Register",
  data() {
    return {
      email: "",
      password: "",
      companyName: ""
    };
  },
  computed: {
    ...mapState(["registeredSuccessfully", "registerError"])
  }
};
</script>

<style scoped lang="scss">
.register {
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
    background-color: rgba(0, 0, 0, 0.3);
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
      padding: 0.5rem;
    }
    button {
      padding: 0.5rem;
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