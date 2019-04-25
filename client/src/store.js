import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loggingIn: false,
    loginError: null,
    loginSuccessfull: false
  },
  mutations: {
    loginStart: state => state.loggingIn = true,
    loginStop: (state, errorMessage) => {
      state.loggingIn = false;
      state.loginError = errorMessage;
      state.loginSuccessfull = !errorMessage;
    }
  },
  actions: {
    Login({commit}, loginData) {
      commit('loginStart');

      fetch('localhost:5000/')
      .then((response) => {
        console.log(response);

      })
      .catch(error => {
        console.log(error);
      })
    }
  }
})
